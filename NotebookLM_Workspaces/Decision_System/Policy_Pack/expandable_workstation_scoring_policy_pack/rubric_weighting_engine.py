import numpy as np
import pandas as pd
import yaml
import os

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

# The "never buy" configurations that define misalignment for this user.
# If a criterion highly correlates with these machines being ranked well,
# it is flagged as misaligned for the expandable AI workstation goal.
NEVER_BUY_MACHINES = [
    "Gaming_PC_16GB_Compact",
    "Prebuilt_SFF_No_Upgrade"
]

# Manual Weight Overrides (Tool, not Law)
# Set minimum weights for dimensions that are critical to YOU.
# Remaining weight pool (after satisfying these minimums) is distributed via whitening.
MANUAL_MIN_WEIGHTS = {
    "VRAM Adequacy": 0.20,
    "Second PCIe x16 Slot Usability": 0.10,
    "PSU Headroom for Current GPU": 0.05
}

# Regularization parameter for the covariance matrix
LAMBDA_REG = 0.1

# Minimum sample size before falling back to simpler pruning
MIN_SAMPLE_SIZE = 4

# ---------------------------------------------------------
# ENGINE LOGIC
# ---------------------------------------------------------

def check_misalignment(df):
    """
    Flags criteria that score 'never buy' machines higher than the mean of preferred machines.
    """
    print("\n--- MISALIGNMENT CHECK ---")
    if len(df) == 0:
        return []
    
    flagged = []
    never_buys = df[df['Machine'].isin(NEVER_BUY_MACHINES)]
    others = df[~df['Machine'].isin(NEVER_BUY_MACHINES)]
    
    if len(never_buys) == 0 or len(others) == 0:
        print("Not enough labeled data to run misalignment check.")
        return flagged
    
    never_buy_means = never_buys.mean(numeric_only=True)
    other_means = others.mean(numeric_only=True)
    
    for col in never_buy_means.index:
        if never_buy_means[col] > other_means[col]:
            print(f"[!] FLAG: '{col}' rewards 'Never Buy' machines more than preferred machines.")
            print(f"    (Never Buy avg: {never_buy_means[col]:.1f} vs Preferred avg: {other_means[col]:.1f})")
            print(f"    -> ACTION: Consider rewriting or deleting this criterion. It is not aligned with your preferences.")
            flagged.append(col)
            
    if not flagged:
        print("No misaligned criteria detected.")
        
    return flagged

def compute_whitened_weights(df_scores):
    """
    Computes correlation-aware (whitened) weights.
    Returns a dictionary of {criterion: weight}.
    """
    print("\n--- CORRELATION-AWARE WEIGHTING (WHITENING) ---")
    criteria = df_scores.columns
    n_samples = len(df_scores)
    
    print(f"Sample size: {n_samples} candidates")
    
    if n_samples < MIN_SAMPLE_SIZE:
        print(f"WARNING: Sample size < {MIN_SAMPLE_SIZE}. Covariance may be unstable.")
        print("Fallback: Using equal weights for now. Add more candidates to enable whitening.")
        return {c: 1.0 / len(criteria) for c in criteria}
    
    # Standardize scores
    std_devs = df_scores.std()
    # Avoid division by zero for constant columns
    std_devs = std_devs.replace(0, 1)
    df_std = (df_scores - df_scores.mean()) / std_devs
    
    # Estimate Covariance Matrix Sigma
    Sigma = df_std.cov().values
    
    # Regularize: Sigma_lambda = Sigma + lambda * I
    Sigma_lambda = Sigma + LAMBDA_REG * np.eye(len(criteria))
    
    try:
        # Inverse square root transform
        eigvals, eigvecs = np.linalg.eigh(Sigma_lambda)
        # Ensure positive eigenvalues
        eigvals = np.maximum(eigvals, 1e-6)
        inv_sqrt_Sigma = eigvecs @ np.diag(1.0 / np.sqrt(eigvals)) @ eigvecs.T
        
        # Whitened-uniform weights are row sums of inv_sqrt_Sigma (normalized)
        raw_weights = np.sum(inv_sqrt_Sigma, axis=1)
        raw_weights = np.maximum(raw_weights, 0) # ensure positive
        
        # Normalize to sum to 1
        weights = raw_weights / np.sum(raw_weights)
        
    except np.linalg.LinAlgError:
        print("ERROR: Linear algebra computation failed. Falling back to equal weights.")
        weights = np.ones(len(criteria)) / len(criteria)
        
    return dict(zip(criteria, weights))

def apply_manual_overrides(whitened_weights):
    """
    Applies the manual minimum weights to the whitened weights.
    Redistributes the remaining weight pool proportionally.
    """
    print("\n--- APPLYING MANUAL OVERRIDES ---")
    final_weights = {}
    remaining_pool = 1.0
    
    # Apply minimums
    for c, w in MANUAL_MIN_WEIGHTS.items():
        if c in whitened_weights:
            final_weights[c] = w
            remaining_pool -= w
            print(f"Override: {c} forced to min weight {w:.2f}")
            
    if remaining_pool <= 0:
        print("WARNING: Manual minimums sum to >= 1.0. Normalizing overrides directly.")
        total = sum(final_weights.values())
        return {c: w/total for c, w in final_weights.items()}
        
    # Redistribute remainder to non-overridden criteria based on whitened ratio
    non_override_pool = sum(w for c, w in whitened_weights.items() if c not in final_weights)
    
    if non_override_pool == 0:
        non_override_pool = 1.0 # fallback
        
    for c, w in whitened_weights.items():
        if c not in final_weights:
            adj_w = (w / non_override_pool) * remaining_pool
            final_weights[c] = adj_w
            
    return final_weights

def rank_candidates(csv_path="candidates_scores.csv"):
    if not os.path.exists(csv_path):
        print(f"Dataset {csv_path} not found. Please create it or run with mocked data.")
        return
        
    df = pd.read_csv(csv_path)
    if 'Machine' not in df.columns:
        print("Error: CSV must have a 'Machine' column.")
        return
        
    # Score columns
    score_cols = [c for c in df.columns if c != 'Machine']
    df_scores = df[score_cols]
    
    # 1. Misalignment
    check_misalignment(df)
    
    # 2. Whitened Weights
    w_weights = compute_whitened_weights(df_scores)
    
    # 3. Manual Overrides
    final_weights = apply_manual_overrides(w_weights)
    
    print("\n--- FINAL WEIGHTS ---")
    for c, w in sorted(final_weights.items(), key=lambda item: item[1], reverse=True):
        print(f"{c}: {w:.3f} ({w*100:.1f}%)")
        
    # 4. Score Calculation
    df['Final_Score'] = 0.0
    for c in score_cols:
        df['Final_Score'] += df[c] * final_weights.get(c, 0)
        
    # Standardize to 100 point scale
    df['Final_Score_100'] = df['Final_Score'] * 10
    
    df_ranked = df.sort_values(by='Final_Score_100', ascending=False).reset_index(drop=True)
    
    print("\n=== FINAL RANKING ===")
    for idx, row in df_ranked.iterrows():
        print(f"{idx+1}. {row['Machine']} - Score: {row['Final_Score_100']: .1f}/100")

    print("\nSee 'ranking_feedback_loop.py' to compare this with a naive equal-weight ranking.")
    return df_ranked

if __name__ == "__main__":
    print("Welcome to the Personal RRD Rubric Weighting Engine.")
    rank_candidates("candidates_scores.csv")
