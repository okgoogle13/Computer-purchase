# How to Maintain the Rubric Pipeline

This guide explains how to maintain the evidence-based rubric and weighting system applied to your personal hardware procurement process.

## 1. Adding a new "Never Buy" example
Your "Never Buy" examples act as ground truth for the misalignment filter.
1. Open `rubric_weighting_engine.py`.
2. Locate the `NEVER_BUY_MACHINES` list at the top.
3. Add the exact machine name from your `candidates_scores.csv` (e.g., `"Gaming_PC_16GB_Compact"`).
4. Run the script: `python3 rubric_weighting_engine.py`.

## 2. Reviewing Misalignment SUSPECT vs CONFIRMED lists
The script checks if any criterion consistently pushes a "Never Buy" machine above a preferred workstation across multiple pairwise comparisons.
- **SUSPECT MISALIGNMENT**: Printed in the logs. These are criteria that fail the pairwise check > 50% of the time. 
  - *Action*: Review them manually. Do not auto-invert them. If they are genuinely opposite to your preferences, rewrite them in `policy_expandable_workstation_scoring.md` or delete them. If they are just overweighted (like Warranty Coverage), rely on the whitening engine to down-weight them, or cap them.
- **CONFIRMED MISALIGNED**: You must manually handle these by editing the markdown policy or deleting the column from the CSV.

## 3. Adjusting Manual Weight Overrides
If the correlation-aware weighting is down-weighting something you care deeply about (e.g., VRAM), force it:
1. Open `rubric_weighting_engine.py`.
2. Find the `MANUAL_MIN_WEIGHTS` dictionary.
3. Adjust the minimum required weight:
   ```python
   MANUAL_MIN_WEIGHTS = {
       "VRAM Adequacy": 0.25, # Bumped from 20% to 25%
       "Second PCIe x16 Slot Usability": 0.15
   }
   ```
4. The script applies these minimums first, then uses "whitening" to intelligently distribute the remaining weight pool among the other criteria.

## 4. Avoiding Redundancy / Over-decomposition
Before adding a new criterion:
1. Run `python3 ranking_feedback_loop.py`.
2. It will alert you if existing metrics are highly correlated (> 0.9).
3. If you see a "STOPPING SIGNAL", stop decomposing and tune weights instead.

## 5. Re-running the pipeline & Generating the Ranking Diff
To see the impact of your changes on real candidates:
1. Add new candidate scores to `candidates_scores.csv`.
2. Run the engine standalone: 
   ```bash
   python3 rubric_weighting_engine.py
   ```
   This will output the whitening details (eigenvalues, means, stds), the misalignment checks, and a table showing the **Old vs New Ranking Diff**, highlighting where "Never Buy" machines correctly dropped in rank.
3. Run the feedback loop:
   ```bash
   python3 ranking_feedback_loop.py
   ```
