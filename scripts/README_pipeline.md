# Hardware Procurement Pipeline — 5 Phases

This repository implements a strict 5-phase data pipeline to turn raw AI hardware research into outcome-driven, MCDA-ranked purchase recommendations, driven by `AGENTS.md` and `config/procurement_policy.json`.

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

## 💸 Phase 3a — Pricing Schema Scaffold
**Goal:** Prepare the shortlist schema for live lookups without doing any live lookup.

**Script:** `enrich_shortlist_pricing.py`

**Workflow:**
```bash
python scripts/enrich_shortlist_pricing.py NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist.csv
```
**Rule:** This script must stay scaffold-only. It only appends missing pricing columns and initializes blanks.

Adds/ensures these metadata columns:
- `source_platform`, `seller_class`, `seller_risk_score`
- `current_best_price_aud`, `current_best_retailer`, `current_best_url`, `in_stock_now`
- `student_discount_possible`, `cashback_possible`, `cashback_source`
- `stackable_coupons_confirmed`, `price_match_possible`, `price_beat_possible`
- `effective_best_price_aud`, `promo_notes`, `pricing_checked_at`
- `warranty_months_confirmed`, `acl_covered`

---

## 💸 Phase 3b — Live Verification Fill
**Goal:** Fill current AU price/stock/seller/source evidence for queued rows.

**Script:** `fill_shortlist_live_pricing.py`

**Workflow:**
```bash
python scripts/fill_shortlist_live_pricing.py NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist_pricing_enriched.csv
```
Writes:
`NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist_pricing_enriched_live.csv`

**Human Step:** Use `scripts/prompt_templates/browser_pricing_lookup.md` with your browser agent integration and fill live values, keeping unresolved fields as `UNKNOWN`.
The browser prompt template is the contract source-of-truth for live pricing response keys and enum values.

---

## 📝 Phase 4 — Manual Scoring
**Goal:** Evaluate the surviving, enriched candidates against the rubric.

**Human Step:** Open the enriched CSV. Fill in the 0–10 MCDA columns (`Performance_Headroom`, `Price_Value`, `Future_Proof`, `Portability`, `Track2_Avoidance`) based on verified evidence and the newly found `effective_best_price_aud`.

---

## 🏆 Phase 5 — Score & Rank
**Goal:** Apply the fixed-weight CareerCopilot MCDA engine to the shortlisted candidates to output a final ranked decision.

**Script:** `rubric_weighting_engine.py`

**Workflow:**
```bash
python NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/rubric_weighting_engine.py \
    --csv NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist_pricing_enriched_live.csv \
    --output-csv NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist_ranked.csv
```
**Outcome:** Keep core MCDA factor weighting unchanged, then apply transparent seller/source risk adjustment columns (`Seller_Risk_Multiplier`, `Source_Platform_Penalty`, `Risk_Adjustment`, `Adjusted_MCDA_Total`). Buy the highest-ranked `GOOD_ENOUGH` candidate or apply the Track Escalation Rule if none clears policy.

---

## Script Ownership Summary
- `build_shortlist.py`: Phase 2 filtering and shortlist generation.
- `enrich_shortlist_pricing.py`: Phase 3a schema scaffold only (no live pricing).
- `fill_shortlist_live_pricing.py`: Phase 3b live verification fill.
- `rubric_weighting_engine.py`: Phase 5 MCDA ranking, policy blockers, risk-aware post-processing output.
