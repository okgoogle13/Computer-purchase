# How to Maintain the Rubric Pipeline

This note explains how to maintain the evidence-based rubric and weighting system (based on the "Rethinking Rubric Generation" paper) applied to your personal hardware procurement process.

## 1. Adding or Removing Criteria (Human-Driven RRD)
If the ranking feels wrong (e.g., a machine you hate ranks above one you like), you need to decompose a broad criterion into a finer one:
1. Open `policy_expandable_workstation_scoring.md`.
2. Add a new row to the **Scoring Rubric (Atomic Dimensions)** table with a clear 0-10 scale.
3. Update `template_product_card_output.md` to extract the new subcriterion.
4. Add the new column to your `candidates_scores.csv` file.

*Stop decomposing when the ranking aligns with your intuition and no surprising results remain.*

## 2. Adjusting Manual Weight Overrides
The Python weighting engine uses correlation-aware math to prevent "double counting" of overlapping criteria (like three different thermal metrics). However, since this is for your personal use, you have the final say.
1. Open `rubric_weighting_engine.py`.
2. Find the `MANUAL_MIN_WEIGHTS` dictionary.
3. Add or adjust the minimum required weight for any criterion (e.g., `"VRAM Adequacy": 0.20` ensures VRAM is always worth at least 20% of the final score).
4. The script will apply these minimums first, then use "whitening" to intelligently distribute the remaining weight pool among the other criteria.

## 3. Defining "Never Buy" Misalignment
Sometimes a criterion is perfectly valid for a gaming PC but terrible for an expandable AI workstation (e.g., a small chassis).
1. Open `rubric_weighting_engine.py`.
2. Find the `NEVER_BUY_MACHINES` list.
3. Add the exact string name of a candidate machine that you would *never* buy for your use case (e.g., `"16GB_Compact_Gamer"`).
4. Run the script. The engine will compare the average scores of your "Never Buy" machines against your preferred machines. If a criterion scores the "Never Buy" machines higher, it will FLAG that criterion.
5. **Action:** When you see a flag, open the markdown policy and rewrite the criterion's 0-10 scale to explicitly penalize the bad trait, or delete the criterion.

## 4. Understanding the Math Logs
When you run the script, it will print:
- **Sample size:** If it's < 4, the engine falls back to equal weights because covariance is unstable. Add more machines to your CSV.
- **Lambda:** Set to `0.1` by default for stability.
- **Final Weights:** Shows the effective percentage each criterion has on the final 100-point score, post-overrides and post-whitening.
