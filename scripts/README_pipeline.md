# Hardware Procurement Pipeline — 5 Phases

This repository implements a strict 5-phase data pipeline to turn raw AI hardware research into objective, mathematically ranked purchase recommendations, driven by the `config/procurement_policy.json` source of truth.

---

## 🏗️ Phase 1 — Intake
**Goal:** Clean dirty CSV data from AI exports and generate markdown product cards for manual verification.

**Scripts:**
1. `normalize_intake.py` — Cleans raw data, enforces enums, deduplicates.
2. `intake_to_cards.py` — Reads the clean CSV, generates an `intake-NNN.md` product card with a Verification Checklist, and places it in the correct lane folder.

**Workflow:**
```bash
python scripts/normalize_intake.py NotebookLM_Workspaces/intake/raw/2026-05-05_notebooklm_batch1.csv
python scripts/intake_to_cards.py NotebookLM_Workspaces/intake/processed/2026-05-05_notebooklm_batch1_processed.csv --overwrite
```

---

## 🎯 Phase 2 — Shortlist
**Goal:** Filter out stock/VRAM failures and apply budget soft-penalties based on `config/procurement_policy.json`.

**Script:** `build_shortlist.py`

**Workflow:**
```bash
python scripts/build_shortlist.py
```
**Human Step:** The script flags `[OVER BUDGET]` and `[PRICE UNKNOWN]` candidates instead of silently dropping them, saving exceptional outliers (e.g., RTX 5090) for manual review.

---

## 💸 Phase 3 — Live Pricing Enrichment
**Goal:** Prepare the shortlist for live lookups of student discounts, cashback, and stackable coupons.

**Script:** `enrich_shortlist_pricing.py`

**Workflow:**
```bash
python scripts/enrich_shortlist_pricing.py NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist.csv
```
**Human Step:** Use the prompt template located at `scripts/prompt_templates/browser_pricing_lookup.md` to instruct the Vercel Browser Agent to do the live lookup. Fill the newly generated empty columns in the `_pricing_enriched.csv`.

---

## 📝 Phase 4 — Manual Scoring
**Goal:** Evaluate the surviving, enriched candidates against the rubric.

**Human Step:** Open the enriched CSV. Fill in the 0–10 score columns (`VRAM_Adequacy`, `GPU_Compute_Tier`, `Value_Score`, etc.) based on your research and the newly found `effective_best_price_aud`.

---

## 🏆 Phase 5 — Score & Rank
**Goal:** Apply the 2-stage "Whitened" scoring engine to the shortlisted candidates to output a final ranked decision.

**Script:** `rubric_weighting_engine.py`

**Workflow:**
```bash
python scripts/rubric_weighting_engine.py --profile merged \
    --csv NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist_pricing_enriched.csv
```
**Outcome:** Buy the machine that hits `#1` and is flagged `[GOOD ENOUGH — stop searching]`.
