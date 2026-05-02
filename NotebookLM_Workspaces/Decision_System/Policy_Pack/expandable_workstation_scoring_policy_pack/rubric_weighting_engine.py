"""
rubric_weighting_engine.py
Personal-use RRD + Whitened Weighting Engine — Two-Stage Model

══════════════════════════════════════════════════════════════════════
TWO-STAGE ARCHITECTURE
══════════════════════════════════════════════════════════════════════

  STAGE 1 — BINARY GATES (non-negotiable disqualification rules)
  ──────────────────────────────────────────────────────────────
  Hard-fail rules check absolute physical impossibilities first.
  Any machine triggering a hard-fail rule is flagged [HARD FAIL]
  and its final score is capped at HARD_FAIL_SCORE_CAP regardless
  of how it scores on all other dimensions.

  Current hard-fail rules (see HARD_FAIL_RULES config):
    - Second_x16_Usability == 0  →  no PCIe expansion slot
    - Chassis_2nd_GPU == 0       →  no physical clearance for a 2nd GPU

  Why PSU_Wattage_Ceiling == 0 is NOT a hard-fail (reasoning captured):
    A score of 0 here means a proprietary PSU < 800W with no obvious
    upgrade path. However, some OEM workstations accept third-party PSU
    replacements; it is not an absolute physical impossibility the way
    a missing x16 slot or absent chassis clearance is. It is instead
    caught by the soft expansion gate (averaged with the other two).
    If you want to promote it to a hard-fail, add it to HARD_FAIL_RULES.

  Soft gate:  avg(Second_x16_Usability, Chassis_2nd_GPU, PSU_Wattage_Ceiling)
              must be >= EXPANSION_FLOOR_THRESHOLD (default 6.0).
              Failure zeros out GATED_BEHIND_EXPANSION columns before scoring.

  STAGE 2 — CONTINUOUS SCORING (whitened rubric)
  ───────────────────────────────────────────────
  On machines not disqualified by Stage 1, score each criterion 0–10,
  apply whitened-uniform weights (RRD paper §4), then apply manual
  minimum-weight overrides.

  Whitening is estimated from ELIGIBLE rows only (soft gate PASS +
  not in NEVER_BUY_MACHINES) to avoid NeverBuy machines' zero expansion
  scores distorting the covariance structure.

  Small-sample fallback hierarchy (fully logged):
    Level 0 — Full whitening        (n_eligible >= MIN_FOR_FULL_WHITEN)
    Level 1 — Diagonal shrinkage    (MIN_FOR_DIAGONAL <= n < MIN_FOR_FULL_WHITEN)
              Uses inverse-std weighting on the eligible rows.
              Stable for n >= 2 without a full covariance estimate.
    Level 2 — Equal weights         (n_eligible < MIN_FOR_DIAGONAL)

  Pre-gate vs post-gate score delta is shown for every machine so you
  can see exactly what each gate costs in ranking points.

══════════════════════════════════════════════════════════════════════
"""

import numpy as np
import pandas as pd
import os

# =============================================================================
# CONFIGURATION — edit these sections to tune the system
# =============================================================================

NEVER_BUY_MACHINES = [
    "PLE_RTX5070Ti_16GB_Desktop",
    "MSI_RTX4080S_16GB_Prebuilt",
    "Lenovo_Legion_RTX4090_16GB_Laptop",
    "Dell_Alienware_m18_RTX4090_Laptop",
    "MSI_Vector_A18_RTX5070Ti_12GB",
]

PREFERRED_WORKSTATIONS = [
    "Custom_RTX3090_24GB_Tower",
    "Dell_Precision_T7920_Dual_A5000",
    "HP_Z8_G4_Workstation_RTX3090",
]

# ──────────────────────────────────────────────────────────────────────────────
# STAGE 1 CONFIG
# ──────────────────────────────────────────────────────────────────────────────

# Hard-fail rules: {criterion: strict_less_than_threshold}
# Any machine where the criterion value is strictly below threshold → HARD FAIL.
# Default threshold 1 means "== 0 triggers hard fail".
HARD_FAIL_RULES = {
    "Second_x16_Usability": 1,   # No PCIe x16 expansion slot → physical impossibility
    "Chassis_2nd_GPU":       1,   # No chassis clearance for 2nd GPU → physical impossibility
    # "PSU_Wattage_Ceiling": 1,  # NOT a hard-fail by default: PSU upgrades are theoretically
                                  # possible in some OEM towers. Caught by soft gate instead.
                                  # Uncomment to promote to hard-fail if your candidates differ.
}
HARD_FAIL_SCORE_CAP = 38.0       # max PostGate_Score for any hard-fail machine (out of 100)

# Soft gate: expansion group average must reach this threshold.
EXPANSION_GROUP_COLS      = ["Second_x16_Usability", "Chassis_2nd_GPU", "PSU_Wattage_Ceiling"]
EXPANSION_FLOOR_THRESHOLD = 6.0

# These columns are zeroed on soft-gate failures before Stage 2 scoring.
# Rationale: good value or warranty on a non-expandable machine should not rescue its rank.
GATED_BEHIND_EXPANSION = ["Price_per_GB_VRAM", "Warranty_Coverage", "Enterprise_Pedigree"]

# ──────────────────────────────────────────────────────────────────────────────
# STAGE 2 CONFIG
# ──────────────────────────────────────────────────────────────────────────────

# Minimum guaranteed weight share for dimensions critical to your priorities.
MANUAL_MIN_WEIGHTS = {
    "VRAM_Adequacy":        0.18,
    "Second_x16_Usability": 0.08,
    "PSU_Wattage_Ceiling":  0.05,
}

# Whitening fallback thresholds (eligible rows = soft gate PASS + not NeverBuy).
LAMBDA_REG           = 0.1   # regularisation for Sigma_lambda = Sigma + lambda*I
MIN_FOR_FULL_WHITEN  = 4     # >= this: full Sigma^{-1/2} whitening
MIN_FOR_DIAGONAL     = 2     # >= this: diagonal-only (inverse-std) fallback
                              # <  this: equal weights


# =============================================================================
# STAGE 1 — BINARY GATES
# =============================================================================

def _banner(title: str, width: int = 70):
    bar = "═" * width
    print(f"\n╔{bar}╗")
    print(f"║  {title:<{width-2}}║")
    print(f"╚{bar}╝")


def apply_gates(df_raw: pd.DataFrame, score_cols: list):
    """
    Returns:
      df_gated      — copy with GATED_BEHIND_EXPANSION zeroed on soft-fail rows
      hard_fail     — boolean Series (True = any HARD_FAIL_RULES triggered)
      hard_fail_reasons — dict {machine: [reason strings]}
      soft_fail     — boolean Series (True = expansion avg < threshold)
      expansion_avg — Series of per-machine expansion group averages
    """
    _banner("STAGE 1 — BINARY GATES  (non-negotiable disqualification)")

    df = df_raw.copy()

    # ---- Hard-fail: check each rule independently ----
    hard_fail_reasons = {m: [] for m in df["Machine"]}
    any_hard_fail     = pd.Series(False, index=df.index)

    print("\n  Hard-fail rules:")
    for col, thresh in HARD_FAIL_RULES.items():
        col_vals = df[col].astype(float)
        triggered = col_vals < thresh
        for i in df[triggered].index:
            m = df.at[i, "Machine"]
            reason = f"{col}={col_vals[i]:.0f} < {thresh}"
            hard_fail_reasons[m].append(reason)
        any_hard_fail |= triggered
        print(f"    {col} < {thresh}  →  [HARD FAIL]  "
              f"(cap score at {HARD_FAIL_SCORE_CAP}/100)")

    print(f"\n  Rationale: PSU_Wattage_Ceiling is NOT a hard-fail rule because a PSU")
    print(f"  can sometimes be replaced in OEM towers. It is caught by the soft gate instead.")
    print(f"  To promote it, uncomment its entry in HARD_FAIL_RULES.")

    # ---- Soft gate ----
    expansion_avg = df[EXPANSION_GROUP_COLS].astype(float).mean(axis=1)
    soft_fail     = expansion_avg < EXPANSION_FLOOR_THRESHOLD

    print(f"\n  Soft gate: avg({', '.join(EXPANSION_GROUP_COLS)}) < {EXPANSION_FLOOR_THRESHOLD}")
    print(f"  Failure →  zero {GATED_BEHIND_EXPANSION} before Stage 2 scoring")

    # ---- Gate results table ----
    print(f"\n  {'Machine':35s}  {'ExpAvg':>7}  {'HardFail':>9}  {'SoftFail':>8}")
    print(f"  {'-'*35}  {'-'*7}  {'-'*9}  {'-'*8}")
    for i, row in df.iterrows():
        hf = "[HF]" if any_hard_fail[i] else "    "
        sf = "[SF]" if soft_fail[i]     else "    "
        reasons = "; ".join(hard_fail_reasons[row["Machine"]]) if any_hard_fail[i] else ""
        print(f"  {row['Machine']:35s}  {expansion_avg[i]:7.1f}  {hf:>9}  {sf:>8}"
              + (f"   ← {reasons}" if reasons else ""))

    # ---- Apply soft gate: zero gated columns ----
    for i in df.index:
        if soft_fail[i]:
            for col in GATED_BEHIND_EXPANSION:
                df.at[i, col] = 0

    return df, any_hard_fail, hard_fail_reasons, soft_fail, expansion_avg


# =============================================================================
# STAGE 2 — CONTINUOUS SCORING
# =============================================================================

# ── Misalignment check ────────────────────────────────────────────────────────

def check_misalignment(df_raw: pd.DataFrame, score_cols: list):
    """Pairwise NeverBuy vs Preferred per criterion on raw pre-gate scores."""
    print("\n  ── Misalignment check (raw scores, pre-gate) ──")

    nbs  = df_raw[df_raw["Machine"].isin(NEVER_BUY_MACHINES)]
    pref = df_raw[df_raw["Machine"].isin(PREFERRED_WORKSTATIONS)]

    if len(nbs) == 0 or len(pref) == 0:
        print("  Not enough labeled data.\n")
        return [], []

    suspect = []
    for col in score_cols:
        fails = sum(nb[col] > pr[col]
                    for _, nb in nbs.iterrows()
                    for _, pr in pref.iterrows())
        rate = fails / (len(nbs) * len(pref))
        if rate > 0.50:
            suspect.append((col, rate))

    if suspect:
        print("  [SUSPECT — review manually]  "
              "(NeverBuy scores > Preferred > 50% of pairs)")
        for col, rate in suspect:
            print(f"    - {col:32s}  {rate*100:.0f}% of pairs wrong direction")
        print("  Decide: overweighted (use whitening/override) "
              "vs genuinely wrong (rewrite/delete column).")
    else:
        print("  No suspect criteria detected.")

    print("  [CONFIRMED MISALIGNED] None. "
          "Add to CONFIRMED_MISALIGNED_COLS in this file to suppress.")
    return [c for c, _ in suspect], []


# ── Whitening with explicit fallback hierarchy ─────────────────────────────────

def compute_whitened_weights(df_eligible: pd.DataFrame,
                             all_criteria: list) -> tuple[dict, str]:
    """
    Returns (weights_dict, fallback_level_str).

    Fallback hierarchy:
      Level 0 — Full whitening:    n >= MIN_FOR_FULL_WHITEN
        Standardise → Sigma → Sigma_lambda^{-1/2} → row sums
      Level 1 — Diagonal shrinkage: MIN_FOR_DIAGONAL <= n < MIN_FOR_FULL_WHITEN
        weights ∝ 1/sqrt(var + lambda)  — stable without full covariance
      Level 2 — Equal weights:     n < MIN_FOR_DIAGONAL
    """
    n     = len(df_eligible)
    n_c   = len(all_criteria)
    df_e  = df_eligible[all_criteria].astype(float)

    print(f"\n  Eligible rows for Sigma estimation : {n}  "
          f"(soft gate PASS + not NeverBuy)")
    print(f"  Criteria                           : {n_c}")
    print(f"  Regularisation lambda              : {LAMBDA_REG}")
    print(f"  Fallback thresholds                : full >= {MIN_FOR_FULL_WHITEN}, "
          f"diagonal >= {MIN_FOR_DIAGONAL}, else equal")

    print(f"\n  Criteria means / std across eligible rows:")
    for c in all_criteria:
        print(f"    {c:32s}  mean={df_e[c].mean():5.2f}  std={df_e[c].std():5.2f}")

    # ─────────────────── Level 0: full whitening ─────────────────────────────
    if n >= MIN_FOR_FULL_WHITEN:
        stds = df_e.std().replace(0, 1)
        Z    = (df_e - df_e.mean()) / stds
        Sigma     = Z.cov().values
        Sigma_lam = Sigma + LAMBDA_REG * np.eye(n_c)

        try:
            eigvals, eigvecs = np.linalg.eigh(Sigma_lam)
            print(f"\n  Sigma_lambda eigenvalues (ascending):")
            print("  " + np.array2string(eigvals, precision=3, floatmode="fixed",
                                         max_line_width=110))

            safe_ev   = np.maximum(eigvals, 1e-6)
            inv_sqrt  = eigvecs @ np.diag(1.0 / np.sqrt(safe_ev)) @ eigvecs.T
            raw       = np.maximum(inv_sqrt.sum(axis=1), 0)

            if raw.sum() > 0:
                weights = raw / raw.sum()
                level   = "Level 0 — full whitening (Sigma^{-1/2} row sums)"
                print(f"\n  Whitening: {level}")
                print("  Covariance estimated on workstation-eligible rows only.")
                print("  NeverBuy machines excluded: their zero expansion scores would")
                print("  inflate expansion-column variance and distort the weight signal.")
                return dict(zip(all_criteria, weights)), level

        except (np.linalg.LinAlgError, ValueError) as exc:
            print(f"\n  WARNING: full whitening failed ({exc}). Falling to Level 1.")

    # ─────────────────── Level 1: diagonal shrinkage ─────────────────────────
    if n >= MIN_FOR_DIAGONAL:
        variances  = df_e.var().values + LAMBDA_REG          # var + lambda, always > 0
        inv_std    = 1.0 / np.sqrt(variances)
        inv_std    = np.maximum(inv_std, 0)
        weights    = inv_std / inv_std.sum() if inv_std.sum() > 0 \
                     else np.ones(n_c) / n_c
        level = (f"Level 1 — diagonal shrinkage (inverse-std, n={n} < {MIN_FOR_FULL_WHITEN}). "
                 f"Stable but ignores inter-criterion correlations. "
                 f"Add more eligible candidates to unlock full whitening.")
        print(f"\n  Whitening fallback: {level}")
        return dict(zip(all_criteria, weights)), level

    # ─────────────────── Level 2: equal weights ───────────────────────────────
    level = (f"Level 2 — equal weights (n={n} < {MIN_FOR_DIAGONAL}). "
             f"No covariance signal. Add more eligible candidates.")
    print(f"\n  Whitening fallback: {level}")
    return {c: 1.0 / n_c for c in all_criteria}, level


# ── Manual overrides ──────────────────────────────────────────────────────────

def apply_manual_overrides(whitened: dict) -> dict:
    """
    Locks minimum weight share for user-specified criteria.
    Redistributes remainder proportionally using whitened ratios.
    """
    final = {}
    pool  = 1.0

    print("\n  Manual weight overrides:")
    for c, min_w in MANUAL_MIN_WEIGHTS.items():
        if c in whitened:
            actual   = max(whitened[c], min_w)
            final[c] = actual
            pool    -= actual
            flag = " ← override active" if whitened[c] < min_w else " (whitened already above min)"
            print(f"    {c:32s}  min={min_w:.2f}  whitened={whitened[c]:.4f}  "
                  f"applied={actual:.4f}{flag}")

    if pool <= 0:
        print("  WARNING: overrides sum >= 1.0. Normalising.\n")
        total = sum(final.values())
        return {c: w / total for c, w in final.items()}

    others  = {c: w for c, w in whitened.items() if c not in final}
    o_total = sum(others.values()) or 1.0
    for c, w in others.items():
        final[c] = (w / o_total) * pool

    return final


# ── Score helpers ─────────────────────────────────────────────────────────────

def weighted_score(df: pd.DataFrame, weights: dict, score_cols: list) -> pd.Series:
    """Weighted sum scaled to 0-100."""
    w_vec = pd.Series([weights[c] for c in score_cols], index=score_cols)
    return df[score_cols].astype(float).multiply(w_vec).sum(axis=1) * 10


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def rank_candidates(csv_path: str = "candidates_scores.csv"):
    if not os.path.exists(csv_path):
        print(f"ERROR: {csv_path} not found.")
        return

    df_raw    = pd.read_csv(csv_path)
    meta_cols = ["Machine", "Type"]
    s_cols    = [c for c in df_raw.columns if c not in meta_cols]

    # ══════════════════════════════════════════════════════════
    # STAGE 1
    # ══════════════════════════════════════════════════════════
    df_gated, hard_fail, hf_reasons, soft_fail, expansion_avg = \
        apply_gates(df_raw, s_cols)

    # ══════════════════════════════════════════════════════════
    # STAGE 2
    # ══════════════════════════════════════════════════════════
    _banner("STAGE 2 — CONTINUOUS SCORING  (whitened rubric)")

    # Misalignment check on raw scores (before gate suppression)
    check_misalignment(df_raw, s_cols)

    # Identify eligible rows for covariance estimation
    eligible_mask = (~soft_fail) & (~df_raw["Machine"].isin(NEVER_BUY_MACHINES))
    df_eligible   = df_gated[eligible_mask][s_cols]

    print(f"\n  Eligible machines for Sigma estimation:")
    for m in df_raw[eligible_mask]["Machine"]:
        print(f"    - {m}")

    # Whitening
    w_weights, whiten_level = compute_whitened_weights(df_eligible, s_cols)
    final_w                 = apply_manual_overrides(w_weights)

    # Weight vector display
    print(f"\n  ── Final weight vector ──")
    print(f"  Whitening: {whiten_level}")
    print()
    for c, w in sorted(final_w.items(), key=lambda x: x[1], reverse=True):
        bar = "█" * max(1, int(w * 100 / 2)) if w > 0 else ""
        print(f"    {c:32s}  {w*100:5.1f}%  {bar}")

    # ══════════════════════════════════════════════════════════
    # SCORING & RANKING DIFF
    # ══════════════════════════════════════════════════════════
    old_eq_w = {c: 1.0 / len(s_cols) for c in s_cols}

    pre_gate  = weighted_score(df_raw,   final_w,  s_cols)  # new weights, raw scores
    post_gate = weighted_score(df_gated, final_w,  s_cols)  # new weights, gated scores
    old_score = weighted_score(df_raw,   old_eq_w, s_cols)  # equal weights, raw (baseline)

    # Apply hard-fail cap
    post_capped = post_gate.copy()
    post_capped[hard_fail] = post_capped[hard_fail].clip(upper=HARD_FAIL_SCORE_CAP)

    # Build output dataframe
    df_out = df_raw[meta_cols].copy()
    df_out["HardFail"]       = hard_fail.values
    df_out["SoftFail"]       = soft_fail.values
    df_out["Old_Score"]      = old_score.values
    df_out["PreGate_Score"]  = pre_gate.values
    df_out["PostGate_Score"] = post_capped.values
    df_out["Gate_Delta"]     = (post_capped - pre_gate).values

    df_new = df_out.sort_values("PostGate_Score", ascending=False).reset_index(drop=True)
    df_old = df_out.sort_values("Old_Score",      ascending=False).reset_index(drop=True)
    old_rank_map = {r.Machine: i + 1 for i, r in df_old.iterrows()}

    _banner("RANKING DIFF  —  Old (equal-weight, raw) vs New (two-stage whitened)")

    hdr = (f"  {'#':>3}  {'Machine':35s}  "
           f"{'OldR':>4}  {'Δ':>3}  "
           f"{'OldScr':>7}  {'PreGate':>7}  {'PostGate':>8}  "
           f"{'GateCost':>8}  Status")
    print(hdr)
    print("  " + "─" * (len(hdr) - 2))

    for new_rank, row in df_new.iterrows():
        m     = row.Machine
        old_r = old_rank_map[m]
        delta = old_r - (new_rank + 1)
        d_str = f"+{delta}" if delta > 0 else str(delta)

        status = ""
        if row.HardFail:
            reasons = "; ".join(hf_reasons.get(m, []))
            status  = f"[HARD FAIL: {reasons}]"
        elif row.SoftFail:
            status = "[SOFT FAIL]"

        cost_str = f"{row.Gate_Delta:+.1f}" if row.Gate_Delta != 0 else "     0.0"

        print(f"  {new_rank+1:>3}  {m:35s}  "
              f"{old_r:>4}  {d_str:>3}  "
              f"{row.Old_Score:7.1f}  {row.PreGate_Score:7.1f}  "
              f"{row.PostGate_Score:8.1f}  {cost_str:>8}  {status}")

        # Contribution breakdown: actual points = gated_score × weight × 10
        row_g    = df_gated[df_gated.Machine == m].iloc[0]
        contribs = {c: row_g[c] * final_w[c] for c in s_cols}
        sc       = sorted(contribs.items(), key=lambda x: x[1], reverse=True)
        top3     = sc[:3]
        bot3     = sc[-3:]

        pos = "  ".join(f"{c}={v*10:.1f}pt" for c, v in top3)
        neg = "  ".join(f"{c}={v*10:.1f}pt" for c, v in bot3)
        print(f"       + {pos}")
        print(f"       - {neg}")

        if row.Type == "NeverBuy" and (new_rank + 1) <= len(PREFERRED_WORKSTATIONS):
            print("       [!!] STILL FAILING: NeverBuy ranked above preferred workstations")
        if row.Type == "NeverBuy" and delta < 0:
            print(f"       [OK] NeverBuy correctly dropped {abs(delta)} rank(s)")

    print()


if __name__ == "__main__":
    rank_candidates()
