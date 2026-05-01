import pandas as pd
import os
from rubric_weighting_engine import compute_whitened_weights, apply_manual_overrides

def run_feedback_loop(csv_path="candidates_scores.csv"):
    if not os.path.exists(csv_path):
        print(f"Dataset {csv_path} not found.")
        return
        
    df = pd.read_csv(csv_path)
    score_cols = [c for c in df.columns if c != 'Machine']
    df_scores = df[score_cols]
    
    # Calculate Naive (Equal) Weights
    naive_weights = {c: 1.0/len(score_cols) for c in score_cols}
    
    df['Naive_Score'] = 0.0
    for c in score_cols:
        df['Naive_Score'] += df[c] * naive_weights[c]
        
    df_naive = df.sort_values(by='Naive_Score', ascending=False).reset_index(drop=True)
    
    # Calculate New Whitened Weights
    w_weights = compute_whitened_weights(df_scores)
    final_weights = apply_manual_overrides(w_weights)
    
    df['New_Score'] = 0.0
    for c in score_cols:
        df['New_Score'] += df[c] * final_weights.get(c, 0)
        
    df_new = df.sort_values(by='New_Score', ascending=False).reset_index(drop=True)
    
    print("\n--- RANKING COMPARISON ---")
    print("Rank | Naive (Equal Weight) | New (Correlation-Aware + Overrides)")
    for i in range(len(df)):
        naive_mach = df_naive.loc[i, 'Machine']
        new_mach = df_new.loc[i, 'Machine']
        print(f" {i+1:2d}  | {naive_mach:25s} | {new_mach:25s}")
        
    print("\n--- PAIRWISE REVIEW ---")
    print("Are there cases where Machine A is ranked above Machine B, but you strongly prefer B?")
    print("If YES:")
    print("1. Identify ONE new subcriterion that cleanly separates them in the direction of your preference.")
    print("2. Add it to 'policy_expandable_workstation_scoring.md'.")
    print("3. Update your 'candidates_scores.csv' with the new column.")
    print("4. Re-run this loop.")
    print("\nIf NO:")
    print("Your rubric is now well-calibrated and fully decomposed for your personal use-case.")

if __name__ == "__main__":
    run_feedback_loop()
