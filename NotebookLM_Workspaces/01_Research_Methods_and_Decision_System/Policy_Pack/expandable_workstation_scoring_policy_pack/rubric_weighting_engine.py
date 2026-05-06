"""
rubric_weighting_engine.py
Personal-use RRD + Whitened Weighting Engine — Two-Stage Model, Multi-Profile

USAGE
  python3 rubric_weighting_engine.py --profile laptop
  python3 rubric_weighting_engine.py --profile workstation   (default)

TWO-STAGE ARCHITECTURE (applies to both profiles)
══════════════════════════════════════════════════════════════════════
  STAGE 1 — BINARY GATES  (non-negotiable disqualification)
    Hard-fail rules:  absolute physical/procurement impossibilities.
                      Machine is flagged [HARD FAIL], score capped.
    Soft gate:        group average below threshold zeros secondary
                      criteria (value/warranty can't rescue a bad platform).

  STAGE 2 — CONTINUOUS SCORING  (whitened rubric)
    Whitening estimated on ELIGIBLE rows only (soft gate PASS + not NeverBuy).
    Manual minimum-weight overrides applied first; whitening distributes remainder.
    Good-enough threshold: any machine meeting it is marked [GOOD ENOUGH — stop].

ADDING A NEW PROFILE
  Copy either profile dict below, add an entry to PROFILES, define a
  candidates CSV, and run with --profile <name>.
══════════════════════════════════════════════════════════════════════
"""

import argparse
import numpy as np
import pandas as pd
import os
import sys

# =============================================================================
# PROFILES — one dict per scoring context
# =============================================================================

PROFILES = {

    # ──────────────────────────────────────────────────────────────────────────
    # LAPTOP PROFILE
    # Goal: choose one 17-18 inch AI-capable laptop for purchase now (AU market).
    # ──────────────────────────────────────────────────────────────────────────
    "laptop": {
        "DEFAULT_CSV": "laptop_candidates.csv",

        "NEVER_BUY_MACHINES": [
            "MSI_Titan_GT77_RTX5090_24GB",   # poor AU retailer confidence, overpriced
        ],
        "PREFERRED_MACHINES": [
            "ASUS_ROG_Scar17_RTX4090_16GB",
            "ASUS_ROG_Scar18_RTX4090_16GB",
            "Lenovo_Legion_Pro7i_RTX4090_16GB",
        ],

        # Stage 1 — hard-fail rules
        # {criterion: strict_less_than_threshold}
        "HARD_FAIL_RULES": {
            "VRAM_Adequacy":        3,    # < 12 GB VRAM — too small for target workloads
            "Sustained_TGP_Rating": 1,    # == 0 — thermal failure risk under sustained load
        },
        "HARD_FAIL_SCORE_CAP": 35.0,

        # Stage 1 — soft gate
        # If avg(SOFT_GATE_COLS) < threshold, GATED cols are zeroed before scoring.
        # Rationale: AU availability/price shouldn't reward a machine that can't
        # sustain a reasonable TGP under extended local inference.
        "SOFT_GATE_COLS":      ["AU_Retailer_Confidence", "Thermal_Reputation"],
        "SOFT_GATE_THRESHOLD":  5.0,
        "GATED_BEHIND_SOFT":   ["Price_AUD_Competitiveness"],

        # Stage 2 — weight minimums
        "MANUAL_MIN_WEIGHTS": {
            "VRAM_Adequacy":        0.20,   # VRAM ceiling is the primary constraint
            "Sustained_TGP_Rating": 0.12,   # real-world sustained throughput
            "AU_Retailer_Confidence": 0.10, # AU procurement is non-negotiable
        },

        # Stage 2 — good-enough stop condition
        # Print [GOOD ENOUGH — stop searching] if ALL conditions met AND score >= threshold.
        "GOOD_ENOUGH_THRESHOLD": 72.0,
        "GOOD_ENOUGH_REQUIREMENTS": {
            "VRAM_Adequacy":          5,    # >= 16 GB
            "AU_Retailer_Confidence": 8,    # confirmed AU stock + local warranty
            "Sustained_TGP_Rating":   6,    # >= ~100 W confirmed sustained TGP
        },

        # Criterion scale reference (printed in output header)
        "SCALE_NOTES": {
            "VRAM_Adequacy":            "10=24GB+, 8=20GB, 5=16GB, 2=12GB, 0=<12GB",
            "GPU_Compute_Tier":         "10=RTX5090, 8=RTX4090/5080, 6=RTX4080/5070Ti",
            "Sustained_TGP_Rating":     "10=>=175W, 8=150W, 6=120W, 3=100W, 0=<100W",
            "Thermal_Reputation":       "10=excellent sustained (reviewed), 5=mixed, 0=throttles",
            "RAM_Ceiling":              "10=64GB upgradeable, 5=32GB max, 0=soldered/no upgrade",
            "Storage_Expandability":    "10=2+ free M.2, 7=1 free slot, 3=full but accessible, 0=none",
            "AU_Retailer_Confidence":   "10=new+local warranty confirmed, 5=orderable, 0=grey/unavail",
            "Price_AUD_Competitiveness":"10=exceptional value in class, 5=fair, 0=overpriced",
            "Display_Usability":        "10=18-inch, 8=17-inch, 5=16-inch, 2=<16-inch",
            "Portability_Penalty":      "10=light(<2kg), 7=moderate(2-2.5kg), 4=heavy(2.5-3kg), 1=desktop-rep(3kg+)",
        },
    },

    # ──────────────────────────────────────────────────────────────────────────
    # WORKSTATION PROFILE
    # Goal: evaluate expandable dual-GPU AI workstations (deferred track).
    # STATUS: Deferred — not the active purchase decision. Preserved for future use.
    # ──────────────────────────────────────────────────────────────────────────
    "workstation": {
        "DEFAULT_CSV": "workstation_candidates.csv",

        "NEVER_BUY_MACHINES": [
            "PLE_RTX5070Ti_16GB_Desktop",
            "MSI_RTX4080S_16GB_Prebuilt",
            "Lenovo_Legion_RTX4090_16GB_Laptop",
            "Dell_Alienware_m18_RTX4090_Laptop",
            "MSI_Vector_A18_RTX5070Ti_12GB",
        ],
        "PREFERRED_MACHINES": [
            "Custom_RTX3090_24GB_Tower",
            "Dell_Precision_T7920_Dual_A5000",
            "HP_Z8_G4_Workstation_RTX3090",
        ],

        "HARD_FAIL_RULES": {
            "Second_x16_Usability": 1,   # No PCIe expansion slot
            "Chassis_2nd_GPU":      1,   # No physical clearance for 2nd GPU
            # "PSU_Wattage_Ceiling": 1,  # PSU can sometimes be replaced; in soft gate instead
        },
        "HARD_FAIL_SCORE_CAP": 38.0,

        "SOFT_GATE_COLS":      ["Second_x16_Usability", "Chassis_2nd_GPU", "PSU_Wattage_Ceiling"],
        "SOFT_GATE_THRESHOLD":  6.0,
        "GATED_BEHIND_SOFT":   ["Price_per_GB_VRAM", "Warranty_Coverage", "Enterprise_Pedigree"],

        "MANUAL_MIN_WEIGHTS": {
            "VRAM_Adequacy":        0.18,
            "Second_x16_Usability": 0.08,
            "PSU_Wattage_Ceiling":  0.05,
        },

        # No stop condition on workstation track — it's a planning tool, not a live decision.
        "GOOD_ENOUGH_THRESHOLD": None,
        "GOOD_ENOUGH_REQUIREMENTS": {},

        "SCALE_NOTES": {
            "VRAM_Adequacy":        "10=48GB+, 8=24GB, 5=16GB, 0=<16GB",
            "GPU_Compute_Tier":     "10=RTX4090/A6000, 8=RTX3090, 6=RTX4080/5070Ti",
            "Second_x16_Usability": "10=true x16/x8 clear, 5=shared x4, 0=none/blocked",
            "PSU_Wattage_Ceiling":  "10=1200W+(multi-GPU), 8=1000W, 5=850W, 0=proprietary<800W",
        },
    },

    # ──────────────────────────────────────────────────────────────────────────
    # MERGED PROFILE
    # Goal: rank candidates from build_shortlist.py across ALL categories
    #       (laptops, desktops, mini PCs, components) using a single shared
    #       8-column schema. Designed to work directly with the shortlist CSV
    #       output of scripts/build_shortlist.py.
    #
    # Usage:
    #   python rubric_weighting_engine.py --profile merged \
    #       --csv NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist.csv
    # ──────────────────────────────────────────────────────────────────────────
    "merged": {
        "DEFAULT_CSV": "NotebookLM_Workspaces/intake/shortlist/shortlist.csv",

        # Populate these after your first shortlist run — move specific
        # intake IDs here once you have identified strong/weak candidates.
        "NEVER_BUY_MACHINES":  [],
        "PREFERRED_MACHINES":  [],

        # Stage 1 — hard-fail rules
        # Verification_Confidence < 1 means the card has essentially no data.
        "HARD_FAIL_RULES": {
            "VRAM_Adequacy":           2,   # < 8 GB effective — below absolute floor
            "Verification_Confidence": 1,   # == 0 — no data at all, cannot score
        },
        "HARD_FAIL_SCORE_CAP": 30.0,

        # Stage 1 — soft gate
        # If a candidate has poor verification confidence AND poor value, do not
        # let price-to-perf rescue it from the bottom.
        "SOFT_GATE_COLS":      ["Verification_Confidence", "Value_Score"],
        "SOFT_GATE_THRESHOLD":  3.0,
        "GATED_BEHIND_SOFT":   ["Price_to_Perf"],

        # Stage 2 — weight minimums
        # VRAM is always the primary constraint; verification is required for
        # a recommendation to be actionable.
        "MANUAL_MIN_WEIGHTS": {
            "VRAM_Adequacy":            0.22,  # VRAM ceiling is the dominant constraint
            "Verification_Confidence":  0.12,  # unverified data must not rank highly
            "Value_Score":              0.10,  # price/VRAM ratio matters for budget
        },

        # Stage 2 — good-enough stop condition
        # Cross-category: any machine scoring >=70 that also has confirmed
        # verification and solid VRAM is good enough to stop searching.
        "GOOD_ENOUGH_THRESHOLD": 70.0,
        "GOOD_ENOUGH_REQUIREMENTS": {
            "VRAM_Adequacy":            5,   # >= 16 GB effective
            "Verification_Confidence":  7,   # verified or near-verified
            "Value_Score":              5,   # at least average value
        },

        # Criterion scale reference
        "SCALE_NOTES": {
            "VRAM_Adequacy":           "10=48GB+/128GB-unified, 8=24GB/64GB, 5=16GB, 2=8GB, 0=<8GB",
            "GPU_Compute_Tier":        "10=RTX5090/4090/Pro, 8=RTX3090/5080/4090M, 6=RTX5070Ti/4080",
            "Value_Score":             "10=exceptional $/GB VRAM (<$100/GB), 5=average, 0=poor",
            "Price_to_Perf":           "10=best-in-class overall value, 5=fair market, 0=overpriced",
            "Condition_Risk":          "10=New+warranty, 8=OpenBox, 6=Refurb+warranty, 4=Used, 0=Unknown",
            "Verification_Confidence": "10=AU stock+URL+specs confirmed, 5=needs verification, 2=unverified, 0=no data",
            "Sustained_TGP_Rating":    "10=>=175W (laptops), 8=150W, 5=100W, 0=N/A (desktops/components OK at 0)",
            "Portability_Score":       "10=<2kg, 7=2-2.5kg, 4=2.5-3kg, 1=3kg+, 0=N/A (non-mobile OK at 0)",
        },
    },
}


# =============================================================================
# WHITENING PARAMETERS (shared across profiles)
# =============================================================================
LAMBDA_REG           = 0.1
MIN_FOR_FULL_WHITEN  = 4
MIN_FOR_DIAGONAL     = 2


# =============================================================================
# UTILITIES
# =============================================================================

def _banner(title: str, width: int = 72):
    bar = "═" * width
    print(f"\n╔{bar}╗")
    print(f"║  {title:<{width-2}}║")
    print(f"╚{bar}╝")


def _load_profile(name: str) -> dict:
    if name not in PROFILES:
        print(f"ERROR: Unknown profile '{name}'. Available: {list(PROFILES.keys())}")
        sys.exit(1)
    return PROFILES[name]


# =============================================================================
# STAGE 1 — BINARY GATES
# =============================================================================

def apply_gates(df_raw: pd.DataFrame, score_cols: list, p: dict):
    """
    Returns:
      df_gated        — copy with GATED_BEHIND_SOFT zeroed on soft-fail rows
      hard_fail       — boolean Series
      hard_fail_reasons — dict {machine: [reason strings]}
      soft_fail       — boolean Series
      soft_avg        — Series of per-machine soft-gate group averages
    """
    _banner("STAGE 1 — BINARY GATES  (non-negotiable disqualification)")

    df = df_raw.copy()
    hard_fail_reasons = {m: [] for m in df["Machine"]}
    any_hard_fail     = pd.Series(False, index=df.index)

    print("\n  Hard-fail rules:")
    for col, thresh in p["HARD_FAIL_RULES"].items():
        triggered = df[col].astype(float) < thresh
        for i in df[triggered].index:
            m = df.at[i, "Machine"]
            hard_fail_reasons[m].append(f"{col}={df.at[i,col]:.0f}<{thresh}")
        any_hard_fail |= triggered
        print(f"    {col} < {thresh}  →  score capped at {p['HARD_FAIL_SCORE_CAP']:.0f}/100")

    soft_avg  = df[p["SOFT_GATE_COLS"]].astype(float).mean(axis=1)
    soft_fail = soft_avg < p["SOFT_GATE_THRESHOLD"]

    print(f"\n  Soft gate: avg({', '.join(p['SOFT_GATE_COLS'])}) < {p['SOFT_GATE_THRESHOLD']}")
    print(f"  Failure → zero {p['GATED_BEHIND_SOFT']}")

    print(f"\n  {'Machine':38s}  {'GateAvg':>7}  {'Hard':>6}  {'Soft':>6}")
    print(f"  {'-'*38}  {'-'*7}  {'-'*6}  {'-'*6}")
    for i, row in df.iterrows():
        hf = "[HF]" if any_hard_fail[i] else "    "
        sf = "[SF]" if soft_fail[i]     else "    "
        reasons = " | ".join(hard_fail_reasons[row["Machine"]]) if any_hard_fail[i] else ""
        suffix  = f"  ← {reasons}" if reasons else ""
        print(f"  {row['Machine']:38s}  {soft_avg[i]:7.1f}  {hf:>6}  {sf:>6}{suffix}")

    for i in df.index:
        if soft_fail[i]:
            for col in p["GATED_BEHIND_SOFT"]:
                df.at[i, col] = 0

    return df, any_hard_fail, hard_fail_reasons, soft_fail, soft_avg


# =============================================================================
# STAGE 2 — CONTINUOUS SCORING
# =============================================================================

def check_misalignment(df_raw: pd.DataFrame, score_cols: list, p: dict):
    """
    Pairwise NeverBuy vs Preferred per criterion on raw pre-gate scores.
    NOTE: 'Target' type machines are intentionally BETTER than 'Preferred' —
    that is the goal, not a misalignment. Only NeverBuy vs Preferred matters here.
    """
    print("\n  ── Misalignment check (raw scores, pre-gate) ──")
    print("  Comparing NeverBuy machines vs Preferred machines only.")
    print("  'Target' machines scoring above 'Preferred' is expected and desired.")
    nbs  = df_raw[df_raw["Machine"].isin(p["NEVER_BUY_MACHINES"])]
    pref = df_raw[df_raw["Machine"].isin(p["PREFERRED_MACHINES"])]

    if len(nbs) == 0 or len(pref) == 0:
        print("  Not enough NeverBuy/Preferred labeled rows for pairwise check.")
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
        print("  [SUSPECT — review manually]")
        for col, rate in suspect:
            print(f"    - {col:32s}  {rate*100:.0f}% of NeverBuy/Preferred pairs wrong direction")
        print("  Decide: genuinely wrong (rewrite/delete col) vs overweighted (use whitening/override).")
    else:
        print("  No suspect criteria detected.")

    print("  [CONFIRMED MISALIGNED] None configured.\n")
    return [c for c, _ in suspect], []


def compute_whitened_weights(df_eligible: pd.DataFrame,
                             all_criteria: list) -> tuple[dict, str]:
    """
    Level 0 — Full whitening         (n >= MIN_FOR_FULL_WHITEN)
    Level 1 — Diagonal shrinkage     (MIN_FOR_DIAGONAL <= n < MIN_FOR_FULL_WHITEN)
    Level 2 — Equal weights          (n < MIN_FOR_DIAGONAL)
    """
    n   = len(df_eligible)
    n_c = len(all_criteria)
    df_e = df_eligible[all_criteria].astype(float)

    print(f"\n  Eligible rows for Sigma estimation : {n}  (soft gate PASS + not NeverBuy)")
    print(f"  Criteria                           : {n_c}")
    print(f"  Lambda                             : {LAMBDA_REG}")
    print(f"  Fallback thresholds                : full>={MIN_FOR_FULL_WHITEN}, "
          f"diagonal>={MIN_FOR_DIAGONAL}, else equal")

    print(f"\n  Criteria means / std across eligible rows:")
    for c in all_criteria:
        print(f"    {c:32s}  mean={df_e[c].mean():5.2f}  std={df_e[c].std():5.2f}")

    # Level 0: full whitening
    if n >= MIN_FOR_FULL_WHITEN:
        stds      = df_e.std().replace(0, 1)
        Z         = (df_e - df_e.mean()) / stds
        Sigma     = Z.cov().values
        Sigma_lam = Sigma + LAMBDA_REG * np.eye(n_c)
        try:
            eigvals, eigvecs = np.linalg.eigh(Sigma_lam)
            print(f"\n  Sigma_lambda eigenvalues (ascending):")
            print("  " + np.array2string(eigvals, precision=3, floatmode="fixed",
                                         max_line_width=110))
            safe_ev  = np.maximum(eigvals, 1e-6)
            inv_sqrt = eigvecs @ np.diag(1.0 / np.sqrt(safe_ev)) @ eigvecs.T
            raw      = np.maximum(inv_sqrt.sum(axis=1), 0)
            if raw.sum() > 0:
                weights = raw / raw.sum()
                level   = "Level 0 — full Sigma^{-1/2} whitening"
                print(f"\n  Whitening: {level}")
                return dict(zip(all_criteria, weights)), level
        except (np.linalg.LinAlgError, ValueError) as exc:
            print(f"\n  WARNING: full whitening failed ({exc}). Falling to Level 1.")

    # Level 1: diagonal shrinkage
    if n >= MIN_FOR_DIAGONAL:
        variances = df_e.var().values + LAMBDA_REG
        inv_std   = 1.0 / np.sqrt(variances)
        inv_std   = np.maximum(inv_std, 0)
        weights   = inv_std / inv_std.sum() if inv_std.sum() > 0 else np.ones(n_c) / n_c
        level = (f"Level 1 — diagonal shrinkage (n={n} < {MIN_FOR_FULL_WHITEN}). "
                 f"Add more eligible candidates to unlock full whitening.")
        print(f"\n  Whitening fallback: {level}")
        return dict(zip(all_criteria, weights)), level

    # Level 2: equal weights
    level = f"Level 2 — equal weights (n={n} < {MIN_FOR_DIAGONAL}). Add more candidates."
    print(f"\n  Whitening fallback: {level}")
    return {c: 1.0 / n_c for c in all_criteria}, level


def apply_manual_overrides(whitened: dict, p: dict) -> dict:
    """Locks minimum weights; distributes remainder proportionally."""
    final = {}
    pool  = 1.0

    print("\n  Manual weight overrides:")
    for c, min_w in p["MANUAL_MIN_WEIGHTS"].items():
        if c in whitened:
            actual   = max(whitened[c], min_w)
            final[c] = actual
            pool    -= actual
            flag = " ← override active" if whitened[c] < min_w else " (whitened already above min)"
            print(f"    {c:32s}  min={min_w:.2f}  whitened={whitened[c]:.4f}  "
                  f"applied={actual:.4f}{flag}")

    if pool <= 0:
        total = sum(final.values())
        return {c: w / total for c, w in final.items()}

    others  = {c: w for c, w in whitened.items() if c not in final}
    o_total = sum(others.values()) or 1.0
    for c, w in others.items():
        final[c] = (w / o_total) * pool
    return final


def weighted_score(df: pd.DataFrame, weights: dict, score_cols: list) -> pd.Series:
    w_vec = pd.Series([weights[c] for c in score_cols], index=score_cols)
    return df[score_cols].astype(float).multiply(w_vec).sum(axis=1) * 10


def check_good_enough(row: pd.Series, score: float, p: dict) -> bool:
    """Returns True if machine meets the good-enough stop condition."""
    threshold = p.get("GOOD_ENOUGH_THRESHOLD")
    reqs      = p.get("GOOD_ENOUGH_REQUIREMENTS", {})
    if threshold is None:
        return False
    if score < threshold:
        return False
    df_row = row  # row is a Series with original machine scores
    for col, min_val in reqs.items():
        if col in df_row and df_row[col] < min_val:
            return False
    return True


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def rank_candidates(profile_name: str, csv_path: str = None):
    p = _load_profile(profile_name)

    if csv_path is None:
        csv_path = p["DEFAULT_CSV"]

    if not os.path.exists(csv_path):
        print(f"ERROR: {csv_path} not found.")
        return

    df_raw    = pd.read_csv(csv_path)
    meta_cols = ["Machine", "Type"]
    s_cols    = [c for c in df_raw.columns if c not in meta_cols]

    # Print scale reference
    _banner(f"SCORING PROFILE: {profile_name.upper()}")
    scale = p.get("SCALE_NOTES", {})
    if scale:
        print("\n  Criterion scale reference:")
        for c, note in scale.items():
            if c in s_cols:
                print(f"    {c:32s}  {note}")

    # ══════════════════════════════════════════════════════════
    # STAGE 1
    # ══════════════════════════════════════════════════════════
    df_gated, hard_fail, hf_reasons, soft_fail, soft_avg = \
        apply_gates(df_raw, s_cols, p)

    # ══════════════════════════════════════════════════════════
    # STAGE 2
    # ══════════════════════════════════════════════════════════
    _banner(f"STAGE 2 — CONTINUOUS SCORING  (whitened rubric, profile={profile_name})")

    check_misalignment(df_raw, s_cols, p)

    # Eligible rows: soft gate PASS + not NeverBuy
    eligible_mask = (~soft_fail) & (~df_raw["Machine"].isin(p["NEVER_BUY_MACHINES"]))
    df_eligible   = df_gated[eligible_mask][s_cols]

    print(f"  Eligible machines for Sigma estimation:")
    for m in df_raw[eligible_mask]["Machine"]:
        print(f"    - {m}")

    w_weights, whiten_level = compute_whitened_weights(df_eligible, s_cols)
    final_w                 = apply_manual_overrides(w_weights, p)

    print(f"\n  ── Final weight vector ──  ({whiten_level})")
    for c, w in sorted(final_w.items(), key=lambda x: x[1], reverse=True):
        bar = "█" * max(1, int(w * 100 / 2)) if w > 0 else ""
        print(f"    {c:32s}  {w*100:5.1f}%  {bar}")

    # ══════════════════════════════════════════════════════════
    # SCORING
    # ══════════════════════════════════════════════════════════
    old_eq = {c: 1.0 / len(s_cols) for c in s_cols}

    pre_gate  = weighted_score(df_raw,   final_w, s_cols)
    post_gate = weighted_score(df_gated, final_w, s_cols)
    old_score = weighted_score(df_raw,   old_eq,  s_cols)

    post_capped = post_gate.copy()
    post_capped[hard_fail] = post_capped[hard_fail].clip(upper=p["HARD_FAIL_SCORE_CAP"])

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

    # ══════════════════════════════════════════════════════════
    # RANKING DIFF
    # ══════════════════════════════════════════════════════════
    _banner("RANKING DIFF  —  Old (equal-weight, raw) vs New (two-stage whitened)")

    good_enough_found = False
    hdr = (f"  {'#':>3}  {'Machine':38s}  "
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

        # Build status string
        status_parts = []
        if row.HardFail:
            reasons = " | ".join(hf_reasons.get(m, []))
            status_parts.append(f"[HARD FAIL: {reasons}]")
        elif row.SoftFail:
            status_parts.append("[SOFT FAIL]")

        # Good-enough check (use raw df_raw row for original scores)
        raw_row = df_raw[df_raw.Machine == m].iloc[0]
        if not row.HardFail and not row.SoftFail:
            if check_good_enough(raw_row, row.PostGate_Score, p):
                status_parts.append("[GOOD ENOUGH — stop searching]")
                good_enough_found = True

        status    = "  ".join(status_parts)
        cost_str  = f"{row.Gate_Delta:+.1f}" if row.Gate_Delta != 0 else "     0.0"

        print(f"  {new_rank+1:>3}  {m:38s}  "
              f"{old_r:>4}  {d_str:>3}  "
              f"{row.Old_Score:7.1f}  {row.PreGate_Score:7.1f}  "
              f"{row.PostGate_Score:8.1f}  {cost_str:>8}  {status}")

        # Contribution breakdown
        row_g    = df_gated[df_gated.Machine == m].iloc[0]
        contribs = {c: row_g[c] * final_w[c] for c in s_cols}
        sc       = sorted(contribs.items(), key=lambda x: x[1], reverse=True)

        pos_str = "  ".join(f"{c}={v*10:.1f}pt" for c, v in sc[:3])
        neg_str = "  ".join(f"{c}={v*10:.1f}pt" for c, v in sc[-3:])
        print(f"       + {pos_str}")
        print(f"       - {neg_str}")

        if row.Type == "NeverBuy" and (new_rank + 1) <= len(p["PREFERRED_MACHINES"]):
            print("       [!!] STILL FAILING: NeverBuy ranked above preferred machines")
        if row.Type == "NeverBuy" and delta < 0:
            print(f"       [OK] NeverBuy correctly dropped {abs(delta)} rank(s)")

    if good_enough_found and p.get("GOOD_ENOUGH_THRESHOLD"):
        threshold = p["GOOD_ENOUGH_THRESHOLD"]
        print(f"\n  ✓ At least one candidate meets the good-enough threshold ({threshold}/100).")
        print(f"  Stop searching — review [GOOD ENOUGH] candidates above and choose.")
    elif p.get("GOOD_ENOUGH_THRESHOLD"):
        print(f"\n  ✗ No candidate yet meets the good-enough threshold ({p['GOOD_ENOUGH_THRESHOLD']}/100).")
        print(f"  Continue searching or relax requirements.")

    print()


# =============================================================================
# CLI
# =============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Two-stage whitened rubric ranking engine.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 rubric_weighting_engine.py --profile laptop
  python3 rubric_weighting_engine.py --profile workstation
  python3 rubric_weighting_engine.py --profile laptop --csv my_custom_candidates.csv
        """)
    parser.add_argument("--profile", default="workstation",
                        choices=list(PROFILES.keys()),
                        help="Scoring profile to use (default: workstation)")
    parser.add_argument("--csv", default=None,
                        help="Path to candidates CSV (overrides profile default)")
    args = parser.parse_args()
    rank_candidates(args.profile, args.csv)
