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
# (e.g. they lack expansion, lack VRAM, etc.)
NEVER_BUY_MACHINES = [
    "PLE_RTX_5070_Ti_16GB",
    "Lenovo_Legion_RTX_4090_16GB",
    "MSI_RTX_4080_Super_16GB"
]

PREFERRED_WORKSTATIONS = [
    "Custom_RTX_3090_24GB_Desktop",
    "Dell_Precision_Dual_A5000"
]

# Manual Weight Overrides (Tool, not Law)
# Set minimum weights for dimensions that are critical to YOU.
MANUAL_MIN_WEIGHTS = {
    "VRAM Adequacy": 0.20,
}

LAMBDA_REG = 0.1
MIN_SAMPLE_SIZE = 4

# ---------------------------------------------------------
# ENGINE LOGIC
# ---------------------------------------------------------

def check_misalignment(df):
    """
    Flags criteria that consistently push a 'Never Buy' machine above a preferred workstation.
    """
    print("\n--- TIGHTENED MISALIGNMENT CHECK ---")
    
    never_buys = df[df['Machine'].isin(NEVER_BUY_MACHINES)]
    preferred = df[df['Machine'].isin(PREFERRED_WORKSTATIONS)]
    
    if len(never_buys) == 0 or len(preferred) == 0:
        print("Not enough labeled data to run pairwise misalignment check.")
        return [], []
    
    suspect_criteria = []
    
    score_cols = [c for c in df.columns if c not in ['Machine', 'Type']]
    
    for col in score_cols:
        pairwise_fails = 0
        total_pairs = len(never_buys) * len(preferred)
        
        for _, nb_row in never_buys.iterrows():
            for _, pref_row in preferred.iterrows():
                # If NeverBuy scores strictly better than Preferred on this metric
                if nb_row[col] > pref_row[col]:
                    pairwise_fails += 1
                    
        fail_rate = pairwise_fails / total_pairs
        
        if fail_rate > 0.5: # If it fails more than 50% of the time
            suspect_criteria.append((col, fail_rate))
            
    # Print Buckets
    confirmed_misaligned = [] # To be filled by user later, but we can simulate the lists
    suspect_misaligned = []
    
    if suspect_criteria:
        print("\n[SUSPECT MISALIGNMENT - Review Manually]")
        print("These criteria often reward gaming PCs/Never Buys more than your preferred workstations.")
        print("Do NOT auto-invert. Decide if they are useful but overweighted, or genuinely wrong for you.")
        for col, rate in suspect_criteria:
            print(f" - {col} (Fails {rate*100:.0f}% of pairs)")
            suspect_misaligned.append(col)
    else:
        print("No suspect criteria detected.")
        
    print("\n[CONFIRMED MISALIGNED - Rewritten/Removed]")
    print("(None currently configured. Edit this script or policy to handle them.)")
        
    return suspect_misaligned, confirmed_misaligned

def compute_whitened_weights(df_scores):
    print("\n--- CORRELATION-AWARE WEIGHTING (WHITENING) DETAILS ---")
    criteria = df_scores.columns
    n_samples = len(df_scores)
    
    print(f"Number of candidates used: {n_samples}")
    print(f"Regularization Lambda: {LAMBDA_REG}")
    
    print("\nCriteria Means and Standard Deviations:")
    for c in criteria:
        print(f" - {c}: Mean={df_scores[c].mean():.2f}, Std={df_scores[c].std():.2f}")
    
    if n_samples < MIN_SAMPLE_SIZE:
        print(f"WARNING: Sample size < {MIN_SAMPLE_SIZE}. Falling back to equal weights.")
        return {c: 1.0 / len(criteria) for c in criteria}
    
    # 1. Standardize rubric columns
    std_devs = df_scores.std()
    std_devs = std_devs.replace(0, 1) # Avoid div zero
    df_std = (df_scores - df_scores.mean()) / std_devs
    
    # 2. Estimate Covariance Matrix Sigma
    Sigma = df_std.cov().values
    
    # 3. Regularize: Sigma_lambda = Sigma + lambda * I
    Sigma_lambda = Sigma + LAMBDA_REG * np.eye(len(criteria))
    
    try:
        # Compute eigenvalues
        eigvals, eigvecs = np.linalg.eigh(Sigma_lambda)
        
        print("\nCovariance Matrix Eigenvalues:")
        print(np.array2string(eigvals, precision=2, floatmode='fixed'))
        
        # 4. Compute Sigma_lambda^{-1/2}
        eigvals = np.maximum(eigvals, 1e-6)
        inv_sqrt_Sigma = eigvecs @ np.diag(1.0 / np.sqrt(eigvals)) @ eigvecs.T
        
        # 5. Set weights proportional to Sigma_lambda^{-1/2} * 1 (row sums)
        raw_weights = np.sum(inv_sqrt_Sigma, axis=1)
        raw_weights = np.maximum(raw_weights, 0)
        
        # Normalize
        weights = raw_weights / np.sum(raw_weights)
        
    except np.linalg.LinAlgError:
        print("ERROR: Linear algebra computation failed. Falling back to equal weights.")
        weights = np.ones(len(criteria)) / len(criteria)
        
    print("\nConfirmation: Using whitened-uniform weighting logic as requested.")
    return dict(zip(criteria, weights))

def apply_manual_overrides(whitened_weights):
    print("\n--- APPLYING MANUAL OVERRIDES ---")
    final_weights = {}
    remaining_pool = 1.0
    
    for c, w in MANUAL_MIN_WEIGHTS.items():
        if c in whitened_weights:
            final_weights[c] = w
            remaining_pool -= w
            print(f"Override: '{c}' forced to exactly {w:.2f} (or minimum)")
            
    non_override_pool = sum(w for c, w in whitened_weights.items() if c not in final_weights)
    if non_override_pool == 0: non_override_pool = 1.0
        
    for c, w in whitened_weights.items():
        if c not in final_weights:
            final_weights[c] = (w / non_override_pool) * remaining_pool
            
    return final_weights

def rank_candidates(csv_path="candidates_scores.csv"):
    if not os.path.exists(csv_path):
        print(f"Dataset {csv_path} not found.")
        return
        
    df = pd.read_csv(csv_path)
    score_cols = [c for c in df.columns if c not in ['Machine', 'Type']]
    df_scores = df[score_cols]
    
    check_misalignment(df)
    
    w_weights = compute_whitened_weights(df_scores)
    final_weights = apply_manual_overrides(w_weights)
    
    print("\n--- FINAL WEIGHT VECTOR (Post-Whitening & Overrides) ---")
    for c, w in sorted(final_weights.items(), key=lambda item: item[1], reverse=True):
        print(f"{c:32s}: {w:.4f} ({w*100:.1f}%)")
        
    df['New_Score'] = 0.0
    df['Old_Score'] = 0.0
    
    old_weight = 1.0 / len(score_cols)
    for c in score_cols:
        df['New_Score'] += df[c] * final_weights.get(c, 0)
        df['Old_Score'] += df[c] * old_weight
        
    df['New_Score'] = df['New_Score'] * 10
    df['Old_Score'] = df['Old_Score'] * 10
    
    df_new = df.sort_values(by='New_Score', ascending=False).reset_index()
    df_old = df.sort_values(by='Old_Score', ascending=False).reset_index()
    
    print("\n=== OLD VS NEW RANKING DIFF ===")
    print(f"{'Machine':30s} | {'Old Rank':>8s} | {'New Rank':>8s} | {'Delta':>5s} | {'Old Score':>9s} | {'New Score':>9s}")
    print("-" * 85)
    
    for new_rank, row in df_new.iterrows():
        machine = row['Machine']
        old_rank = df_old[df_old['Machine'] == machine].index[0]
        delta = old_rank - new_rank
        delta_str = f"+{delta}" if delta > 0 else str(delta)
        
        # Calculate top contributors for New Score
        contributions = {c: row[c] * final_weights.get(c, 0) for c in score_cols}
        sorted_contrib = sorted(contributions.items(), key=lambda item: item[1], reverse=True)
        top_pos = ", ".join([f"{c}" for c, v in sorted_contrib[:3]])
        top_neg = ", ".join([f"{c}" for c, v in sorted_contrib[-3:]])
        
        print(f"{machine:30s} | {old_rank+1:8d} | {new_rank+1:8d} | {delta_str:>5s} | {row['Old_Score']:9.1f} | {row['New_Score']:9.1f}")
        print(f"  + Top Pos: {top_pos}")
        print(f"  - Top Neg: {top_neg}")
        
        if row['Type'] == 'NeverBuy' and new_rank < 2:
            print(f"  [!] STILL FAILING: NeverBuy machine ranked too high!")
        if row['Type'] == 'NeverBuy' and delta < 0:
            print(f"  [FIXED]: NeverBuy machine correctly dropped in rank.")
            
if __name__ == "__main__":
    rank_candidates()
