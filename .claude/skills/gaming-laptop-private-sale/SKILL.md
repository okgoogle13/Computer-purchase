---
name: gaming-laptop-private-sale
description: Search Gumtree and Facebook Marketplace AU for private-sale gaming laptops (Track 1A), ingest into the intake pipeline, and build a refreshed laptop shortlist. Pass a HAR file path as an argument for Facebook data; Gumtree runs automatically.
---

# Gaming Laptop — Private Sale Search (AU)

Triggers a Track 1A private-sale sweep across Gumtree AU and optionally Facebook Marketplace.

## Arguments

Optionally pass a HAR file path: `/gaming-laptop-private-sale data/raw/facebook_marketplace/session.har`

If no HAR path is provided, skip the Facebook steps and run Gumtree only.

## Workflow

### Step 1 — Gumtree collection (always runs)

```bash
python scripts/data_collection/gumtree_collect.py \
  --query "gaming laptop RTX 4090 OR RTX 4080 OR RTX 3080 OR RTX 3080 Ti" \
  --output data/processed/gumtree_$(date +%Y-%m-%d).csv \
  --max-pages 5
```

### Step 2 — Facebook Marketplace (only if HAR path provided)

Capture a HAR file if you haven't already:
1. Log into Facebook, open Marketplace → Computers & Laptops
2. Scroll 2–3 pages of listings
3. DevTools (F12) → Network tab → right-click any request → "Save all as HAR with content"
4. Save to `data/raw/facebook_marketplace/`

Then run:
```bash
python scripts/data_collection/facebook_collect.py \
  --har <HAR_PATH_FROM_ARGUMENT> \
  --output data/processed/facebook_marketplace_$(date +%Y-%m-%d).csv
```

Then map (no arguments — auto-resolves today's file):
```bash
python scripts/data_collection/map_facebook_to_intake.py
```

### Step 3 — Normalize and ingest

```bash
python scripts/normalize_intake.py data/processed/gumtree_$(date +%Y-%m-%d).csv
python scripts/intake_to_cards.py NotebookLM_Workspaces/intake/processed/$(date +%Y-%m-%d)_batch_processed.csv --overwrite
# Use the archetype flag — applies private-sale ceiling ($3,500), 12GB VRAM floor, and 4yr age constraint
python scripts/build_shortlist.py --archetype gaming_laptop_private_sale
```

### Step 4 — Completion check

Verify new rows appeared with private-sale sources:
```bash
grep -E "GUMTREE_AU|FB_MARKETPLACE" shortlists/shortlist_profile-laptop.csv | wc -l
```

Expected: count > 0. If 0, report which step produced no output.

## Policy context (Track 1A)
- Discrete VRAM ≥ 8 GB hard floor; 12 GB preferred for secondary-market scans
- Screen ≥ 16 inches
- Price ≤ 5,000 AUD
- Private sellers: set `seller_class = PRIVATE_SELLER`; flag thermal/condition risk
- Verify eBay/FB prices against last-30-days Sold listings — not asking prices
