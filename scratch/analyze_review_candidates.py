import csv
import subprocess
from collections import Counter

# Read shortlists/2026-06-07_ranked_final.csv from git HEAD
out = subprocess.check_output(['git', 'show', 'HEAD:shortlists/2026-06-07_ranked_final.csv'], text=True)
reader = csv.DictReader(out.splitlines())

review_candidates = []
for row in reader:
    if row.get('Policy_Status') == 'NEEDS_REVIEW':
        review_candidates.append(row)

print(f"Total NEEDS_REVIEW candidates in HEAD: {len(review_candidates)}")

# Group by category
categories = Counter(r.get('category', 'UNKNOWN') for r in review_candidates)
print("\nBy Category:")
for cat, count in categories.items():
    print(f"  - {cat}: {count}")

# Group by track
tracks = Counter(r.get('track', 'UNKNOWN') for r in review_candidates)
print("\nBy Track:")
for t, count in tracks.items():
    print(f"  - Track {t}: {count}")

# Analyze blocker combinations
blockers_list = []
for r in review_candidates:
    blockers_str = r.get('Policy_Blockers', '')
    if blockers_str:
        # split by semicolon and strip
        parts = [b.strip() for b in blockers_str.split(';') if b.strip()]
        blockers_list.extend(parts)

blockers_counts = Counter(blockers_list)
print("\nMost Common Blockers:")
for blocker, count in blockers_counts.most_common():
    print(f"  - {blocker}: {count}")

# Let's look at specific items with price > Track 1 cap or Track 2 cap
over_budget = []
for r in review_candidates:
    blockers_str = r.get('Policy_Blockers', '')
    if 'price >' in blockers_str:
        over_budget.append((r.get('item_name') or r.get('Machine'), r.get('price_aud'), r.get('track'), r.get('pathway')))

print(f"\nOver-Budget Candidates ({len(over_budget)}):")
for name, price, track, pathway in over_budget:
    print(f"  - {name}: {price} AUD (Track {track}, Pathway {pathway})")
