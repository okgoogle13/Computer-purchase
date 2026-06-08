---
name: refurb-workstation-au
description: Search eBay AU and Gumtree for refurbished desktop workstations (GPU VRAM ≥ 16 GB) as Track 1.5 candidates. Only invoke under Exception A — no viable Track 1 found.
---

# Refurb Workstation AU (Track 1.5)

Triggers a Track 1.5 refurbished desktop sweep. Only use when Exception A applies: Track 1 has been re-checked for discounts/refurb and no viable candidate remains.

## Workflow

### Step 1 — eBay AU search via agent-browser

Use the `agent-browser` skill to search eBay Australia for:
- `RTX 3090 desktop Australia`
- `RTX 4090 desktop Australia`
- `RTX 3090 Ti desktop Australia`

For each result, capture: price (ask + recent Sold comps), seller name, seller feedback %, condition, AU location, URL.

Classify seller using source priority: `EBAY_AU` with `seller_class = EBAY_POWER_SELLER` or `REFURB_SELLER` as appropriate.

### Step 2 — Gumtree desktop collection

```bash
python scripts/data_collection/gumtree_collect.py \
  --query "desktop RTX 3090 OR RTX 4090 OR RTX 3080 Ti" \
  --output data/processed/gumtree_desktops_$(date +%Y-%m-%d).csv \
  --max-pages 3
```

### Step 3 — Normalize and build desktop shortlist

```bash
python scripts/normalize_intake.py data/processed/gumtree_desktops_$(date +%Y-%m-%d).csv
python scripts/intake_to_cards.py NotebookLM_Workspaces/intake/processed/$(date +%Y-%m-%d)_batch_processed.csv --overwrite
# Use the archetype flag — applies Track 1.5 ceiling ($4,000), 16GB VRAM floor, Exception A gate
python scripts/build_shortlist.py --archetype refurb_workstation_au
```

### Step 4 — Completion check

```bash
grep -E "track.*1\.5|1_5|desktop" shortlists/shortlist_profile-desktop.csv 2>/dev/null | grep -iE "vram_gb|gpu" | head -5
```

Expected: rows showing `vram_gb >= 16`. If none, report what was found and why it fell short of the VRAM floor.

## Policy context (Track 1.5)
- Applies only under Exception A — re-check Track 1 first
- GPU VRAM hard floor: ≥ 16 GB (24 GB preferred)
- Credible AU seller required — no gray import, no overseas-only stock
- Price: verify against last-30-days eBay Sold listings, not asking price
