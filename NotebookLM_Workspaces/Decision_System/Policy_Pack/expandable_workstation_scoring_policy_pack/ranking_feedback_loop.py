import pandas as pd
import numpy as np
import os
import sys

def run_feedback_loop(csv_path="candidates_scores.csv"):
    if not os.path.exists(csv_path):
        print(f"Dataset {csv_path} not found.")
        return
        
    df = pd.read_csv(csv_path)
    score_cols = [c for c in df.columns if c not in ['Machine', 'Type']]
    df_scores = df[score_cols]
    
    print("\n--- PAIRWISE REVIEW & REDUNDANCY CONTROL ---")
    print("Are there cases where Machine A is ranked above Machine B, but you strongly prefer B?")
    print("If YES:")
    print("Before proposing a new subcriterion, consider: Will it be highly correlated (>0.9) with an existing metric?")
    
    # Calculate correlation matrix
    corr_matrix = df_scores.corr().abs()
    
    # Find highly correlated pairs
    high_corr_pairs = []
    for i in range(len(score_cols)):
        for j in range(i+1, len(score_cols)):
            if corr_matrix.iloc[i, j] > 0.9:
                high_corr_pairs.append((score_cols[i], score_cols[j], corr_matrix.iloc[i, j]))
                
    if high_corr_pairs:
        print("\n[!] WARNING: You already have highly correlated metrics. Do not over-decompose.")
        for col1, col2, corr in high_corr_pairs:
            print(f" - {col1} and {col2} (Correlation: {corr:.2f})")
        print("\nSUGGESTION: Instead of adding a new criterion, consider adjusting the MANUAL_MIN_WEIGHTS for existing ones.")
    
    print("\nIf you must add a new metric:")
    print("1. Ensure it cleanly separates the machines in the direction of your preference.")
    print("2. Add it to 'policy_expandable_workstation_scoring.md'.")
    print("3. Update 'candidates_scores.csv' with the new column.")
    print("4. Re-run this loop.")
    
    # Stopping signal
    if len(score_cols) > 15 and len(high_corr_pairs) > 3:
        print("\n*** STOPPING SIGNAL ***")
        print("You have many criteria and several are highly redundant.")
        print("Consider stopping decomposition and tuning weights instead.")
    else:
        print("\nIf NO surprising rankings remain:")
        print("Your rubric is now well-calibrated and fully decomposed for your personal use-case.")

if __name__ == "__main__":
    # Let the user run the engine first, then this loop.
    os.system(f"{sys.executable} rubric_weighting_engine.py")
    run_feedback_loop()
