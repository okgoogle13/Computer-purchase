# How to Maintain the Rubric Pipeline

This guide is for "future you" — written assuming you haven't touched this in weeks.

---

## Quick-start commands

```bash
# From: NotebookLM_Workspaces/Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/

# Full ranking run with whitening details, gate results, and old-vs-new diff:
python3 rubric_weighting_engine.py

# Interactive pairwise review + redundancy check:
python3 ranking_feedback_loop.py
```

---

## How the scoring pipeline works (top to bottom)

```
candidates_scores.csv
        ↓
[1] HARD-FAIL GATE     Second_x16_Usability == 0  →  [HARD FAIL] flag, score capped at 38/100
        ↓
[2] SOFT EXPANSION GATE  avg(Second_x16, Chassis_2nd_GPU, PSU_Wattage_Ceiling) < 6.0
                         →  zero Price_per_GB_VRAM, Warranty_Coverage, Enterprise_Pedigree
        ↓
[3] WHITENING          Sigma estimated on ELIGIBLE rows only
                       (gate PASS + not NeverBuy)
        ↓
[4] MANUAL OVERRIDES   VRAM ≥ 18%, Second_x16 ≥ 8%, PSU_Ceiling ≥ 5%
        ↓
[5] SCORING
        Old_Score    = equal weights × raw scores  (baseline)
        PreGate_Score = final weights × raw scores  (weight effect only)
        PostGate_Score = final weights × gated scores + hard-fail cap  (actual rank)
        Gate_Cost    = PostGate - PreGate  (negative = gate penalty)
```

---

## Key design decisions (what changed and why)

| What | How it works |
|---|---|
| **Expandability gate** | If a machine's avg(`Second_x16_Usability`, `Chassis_2nd_GPU`, `PSU_Wattage_Ceiling`) < 6.0, its `Price_per_GB_VRAM`, `Warranty_Coverage`, and `Enterprise_Pedigree` scores are **zeroed before scoring**. A great deal on a non-expandable machine can't rescue its rank. |
| **Whitening method** | Follows RRD paper §4: standardise columns → estimate Σ → regularise Σ_λ = Σ + λI → compute Σ_λ^{-1/2} via eigen-decomp → weights ∝ row sums of Σ_λ^{-1/2}. This down-weights clusters of correlated metrics so they don't dominate collectively. |
| **Manual overrides** | Applied **before** whitening distributes the remainder. VRAM ≥ 18%, `Second_x16_Usability` ≥ 8%, `PSU_Wattage_Ceiling` ≥ 5%. These represent your non-negotiable buying priorities. |
| **Misalignment filter** | Pairwise NeverBuy-vs-Preferred per criterion. Only flags SUSPECT (> 50% of pairs go the wrong way). Does not auto-invert — you decide. |
| **Contribution math** | Points shown in the diff are `raw_score × final_weight × 10` so they sum to the displayed New_Score. |

---

## 1. Adding a new "Never Buy" example

Open `rubric_weighting_engine.py`, find `NEVER_BUY_MACHINES`, add the machine name exactly as it appears in `candidates_scores.csv`:

```python
NEVER_BUY_MACHINES = [
    "PLE_RTX5070Ti_16GB_Desktop",
    "My_New_Bad_Machine",   # <-- add here
]
```

Then re-run: `python3 rubric_weighting_engine.py`

---

## 2. Adding a new candidate machine

Add a row to `candidates_scores.csv`. Score each criterion 0–10 using the scale in `policy_expandable_workstation_scoring.md`. Set `Type` to `Preferred`, `NeverBuy`, `Borderline`, or `Special`.

```
NewMachine,Preferred,8,8,7,8,8,8,7,8,8,8,9,9,8,9,5,2
```

Re-run `python3 rubric_weighting_engine.py`. The covariance matrix will be re-estimated with the new data point.

---

## 3. Reviewing SUSPECT vs CONFIRMED misalignment

The engine prints two buckets at the start of every run:

- **SUSPECT** — criterion rewards NeverBuy machines more than Preferred > 50% of the time. **Do not auto-invert.** Ask: "Is this criterion just overweighted, or genuinely measuring the wrong thing?"
  - If **overweighted**: leave it, rely on whitening + manual overrides to dampen it.
  - If **genuinely wrong**: edit the 0–10 scale in the policy markdown, or delete it from the CSV entirely.
- **CONFIRMED** — you've already decided to suppress it. Add it to `CONFIRMED_MISALIGNED_COLS` in the script (currently none).

---

## 4. Adjusting manual weight overrides

Edit `MANUAL_MIN_WEIGHTS` in `rubric_weighting_engine.py`:

```python
MANUAL_MIN_WEIGHTS = {
    "VRAM_Adequacy":        0.25,   # bump from 18% → 25%
    "Second_x16_Usability": 0.10,   # bump from 8% → 10%
    "PSU_Wattage_Ceiling":  0.05,
}
```

The remaining weight pool (1 − sum of overrides) is automatically redistributed via whitening. Re-run to see the new weight vector and ranking diff.

---

## 5. Adjusting the expandability gate

Edit two constants in `rubric_weighting_engine.py`:

```python
EXPANSION_GROUP_COLS      = ["Second_x16_Usability", "Chassis_2nd_GPU", "PSU_Wattage_Ceiling"]
EXPANSION_FLOOR_THRESHOLD = 6.0   # raise to 7.0 to be stricter
GATED_BEHIND_EXPANSION    = ["Price_per_GB_VRAM", "Warranty_Coverage", "Enterprise_Pedigree"]
```

Raising the threshold makes the gate stricter (more machines fail). Lowering it relaxes it. You can also add/remove criteria from `GATED_BEHIND_EXPANSION`.

---

## 6. Adding or removing a rubric criterion

1. Edit the table in `policy_expandable_workstation_scoring.md` (add the new row with its 0–10 scale).
2. Add the same column name to every row in `candidates_scores.csv`.
3. Update `template_product_card_output.md` so NotebookLM extracts the new score.
4. Re-run `python3 rubric_weighting_engine.py`.

**Before adding**: run `python3 ranking_feedback_loop.py` first — it will warn you if a new criterion would be > 0.9 correlated with an existing one. If so, adjust weights instead.

---

## 7. Understanding the whitening parameters

| Parameter | Location | Effect |
|---|---|---|
| `LAMBDA_REG = 0.1` | `rubric_weighting_engine.py` | Regularisation strength. Increase (e.g. 0.3) if weights look noisy or if eigenvalues are very small. |
| `MIN_SAMPLE_SIZE = 8` | `rubric_weighting_engine.py` | Below this, the engine skips whitening and uses equal weights. Add more candidate rows to unlock. |

The eigenvalues printed during each run tell you how spread out the variance is. A large dominant eigenvalue (e.g. 9.4 vs 0.1) means one dimension dominates the raw scores — whitening pulls that dimension's weight back down.
