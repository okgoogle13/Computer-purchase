# Hardware Procurement Pipeline — 5 Phases

This repository implements a strict 5-phase data pipeline to turn raw AI hardware research into outcome-driven, MCDA-ranked purchase recommendations, driven by `AGENTS.md` and `config/procurement_policy.json`.

---

## 🕵️‍♂️ Phase 0 — Data Collection (Optional)
**Goal:** Gather targeted hardware listings from secondary markets and raw data sources.

**Scripts:**
- `facebook_search_automator.py` — Hijacks an open Chrome session to perform automated searches on Facebook Marketplace and dumps intercepted GraphQL JSON.
  > **Note:** To use this, close all Chrome windows and launch it via terminal on Mac:
  > `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222`
- `trigger_parsehub.py` — Triggers a cloud-based ParseHub run (bypassing local browser requirements) and downloads structured JSON results.
- `facebook_collect.py` — Parses HAR files, targeted search GraphQL JSON dumps, or ParseHub JSON dumps into the canonical scraping schema.
- `gumtree_collect.py` — Scrapes Gumtree AU listings.
- `scrape_ebay_watchlist.py` / `map_ebay_to_intake.py` — Extracts specs from eBay watchlists.

Outputs from these scripts can be piped directly into `intake_to_cards.py`.

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
Cards are organized under `cards/` category subfolders (`laptops/`, `desktops/`, `mini_pcs/`, `components/`, `apple_silicon/`); shortlist scanning is recursive.
Profile-specific shortcuts:
```bash
python scripts/build_shortlist_laptops.py
python scripts/build_shortlist_desktops.py
python scripts/build_shortlist_mini_pcs.py
python scripts/build_shortlist_components.py
python scripts/build_shortlist_apple_silicon.py
```
**Human Step:** The script flags `[OVER BUDGET]` and `[PRICE UNKNOWN]` candidates instead of silently dropping them, saving exceptional outliers (e.g., RTX 5090) for manual review.

---

## 💸 Phase 3a — Pricing Schema Scaffold
**Goal:** Prepare the shortlist schema for live lookups without doing any live lookup.

**Script:** `enrich_shortlist_pricing.py`

**Workflow:**
```bash
python scripts/enrich_shortlist_pricing.py shortlists/YYYY-MM-DD_shortlist.csv
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
python scripts/fill_shortlist_live_pricing.py shortlists/YYYY-MM-DD_shortlist_pricing_enriched.csv
```
Writes:
`shortlists/YYYY-MM-DD_shortlist_pricing_enriched_live.csv`

**Important:** the current `fill_shortlist_live_pricing.py` implementation is a scaffold integration point. By default it uses a placeholder lookup and does not perform real web pricing verification unless a browser-agent lookup is explicitly wired.

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
python scripts/scoring/rubric_weighting_engine.py \
    --csv shortlists/YYYY-MM-DD_shortlist_pricing_enriched_live.csv \
    --output-csv shortlists/YYYY-MM-DD_shortlist_ranked.csv
```
**Outcome:** Keep core MCDA factor weighting unchanged, then apply transparent seller/source risk adjustment columns (`Seller_Risk_Multiplier`, `Source_Platform_Penalty`, `Risk_Adjustment`, `Adjusted_MCDA_Total`). Buy the highest-ranked `GOOD_ENOUGH` candidate or apply the Track Escalation Rule if none clears policy.

---

## ✅ Policy Drift Gate (Run Before Ranking)
Check `AGENTS.md` policy constants against `config/procurement_policy.json`:

```bash
python scripts/policy_drift_check.py
```

If mismatches are detected, recommendation language must follow `AGENTS.md` until config is aligned.

---

## 🔗 Prompt Chain Orchestration
Use the orchestration runner to execute deterministic script stages and enforce manual/agent checkpoints:

```bash
python scripts/run_prompt_chain.py --batch YYYY-MM-DD_notebooklm_batchN
```

This runner executes:
1. `policy_drift_check.py`
2. `build_shortlist.py`
3. `enrich_shortlist_pricing.py`
4. `rubric_weighting_engine.py` (after manual/agent pricing + MCDA fill checkpoints)

Prompt checkpoint order:
1. `notebooklm_system_prompt.md`
2. `audit_checklist_prompt.md`
3. `pre_scoring_validation_prompt.md`
4. `browser_pricing_lookup.md`
5. `track1_card_shortlist_sync_prompt.md`
6. `ai_scoring_execution_prompt.md`
7. `final_purchase_justification_prompt.md`

---

## 🧪 Validation Checks
Prompt contract validation:

```bash
python scripts/validate_prompt_templates.py
```

Pipeline integrity validation:

```bash
python scripts/pipeline_integrity_check.py \
  --enriched shortlists/YYYY-MM-DD_shortlist_pricing_enriched_live.csv \
  --ranked shortlists/YYYY-MM-DD_shortlist_ranked.csv
```

---

## Script Ownership Summary
- `build_shortlist.py`: Phase 2 filtering and shortlist generation.
- `enrich_shortlist_pricing.py`: Phase 3a schema scaffold only (no live pricing).
- `fill_shortlist_live_pricing.py`: Phase 3b live verification fill.
- `rubric_weighting_engine.py`: Phase 5 MCDA ranking, policy blockers, risk-aware post-processing output.
