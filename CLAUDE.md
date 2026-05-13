# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

AI-assisted hardware procurement decision system for selecting hardware to ship CareerCopilot MVP (Q3 2026). The system uses a 5-phase pipeline: intake → shortlist → live pricing → manual MCDA scoring → ranked recommendation.

**Default goal:** Buy one Track 1 laptop that is outcome-enabled, AU-available, ≤5,000 AUD, and free of disqualifying thermal risk. Do not wait for Track 2.

## Pipeline Commands

```bash
# Phase 1 — Intake: normalize raw CSV and generate product cards
python scripts/normalize_intake.py NotebookLM_Workspaces/intake/raw/YYYY-MM-DD_batch.csv
python scripts/intake_to_cards.py NotebookLM_Workspaces/intake/processed/YYYY-MM-DD_batch_processed.csv --overwrite

# Phase 2 — Shortlist
python scripts/build_shortlist.py

# Phase 3a — Pricing schema scaffold only (no live lookup)
python scripts/enrich_shortlist_pricing.py shortlists/YYYY-MM-DD_shortlist.csv

# Phase 3b — Live pricing fill (AU verification)
python scripts/fill_shortlist_live_pricing.py shortlists/YYYY-MM-DD_shortlist_pricing_enriched.csv

# Phase 5 — MCDA ranking
python scripts/scoring/rubric_weighting_engine.py \
  --csv shortlists/YYYY-MM-DD_shortlist_pricing_enriched_live.csv \
  --output-csv shortlists/YYYY-MM-DD_shortlist_ranked.csv

# Full orchestrated run
python scripts/run_prompt_chain.py --batch YYYY-MM-DD_notebooklm_batchN

# Validation
python scripts/policy_drift_check.py
python scripts/validate_prompt_templates.py
python scripts/pipeline_integrity_check.py \
  --enriched shortlists/YYYY-MM-DD_shortlist_pricing_enriched_live.csv \
  --ranked shortlists/YYYY-MM-DD_shortlist_ranked.csv

# Tests
pytest tests/
```

## Architecture

**Policy authority order** (highest to lowest):
1. `AGENTS.md` — decision rules and track definitions
2. `config/procurement_policy.json` — hard thresholds consumed by scripts (do not hardcode these in scripts)
3. CSV files — working candidate ledger
4. Markdown product cards in `cards/` — per-candidate evidence and checklist state
5. Live web sources — current AU price/stock/warranty verification

**Key files:**
- `AGENTS.md` — all decision rules, track gates, MCDA weights, and scoring rubrics
- `config/procurement_policy.json` — budget caps, VRAM floors, MCDA weights (source of truth for scripts)
- `shortlists/` — CSV working files at each pipeline stage
- `cards/` — markdown product cards (naming: `intake-NNN_...md` or `harvest-YYYYMMDD-NNN_...md`)
- `scripts/README_pipeline.md` — detailed per-phase workflow

**Script ownership (strict):**
- `enrich_shortlist_pricing.py` — schema scaffold ONLY, no web lookup, no inferred values
- `fill_shortlist_live_pricing.py` — live AU pricing fill for queued rows only
- `rubric_weighting_engine.py` — MCDA weighting + risk-adjusted output columns

## Track Gates

### Track 1A — NVIDIA/Discrete GPU Laptop (budget cap: 5,000 AUD)

Scope: Lenovo Legion/Legion Pro, ASUS ROG, MSI high-performance, Alienware (approved exception 2026-05-09). Named exceptions require explicit user approval.

Gates (all must pass):
- [ ] Screen ≥ 16 inches
- [ ] Discrete VRAM ≥ 8 GB
- [ ] Price ≤ 5,000 AUD
- [ ] No disqualifying sustained thermal throttling risk

VRAM floors: 8 GB minimum eligibility · 12 GB discovery floor for secondary-market scans · 24 GB preferred for Q4/Track2-avoidance.

### Track 1B — AMD Strix Halo Laptop (budget cap: 5,000 AUD)

Scope: Strix Halo / Ryzen AI Max / Ryzen AI Max+ unified-memory laptops only. Exclude standard Ryzen + discrete GPU and Apple Silicon.

Gates (all must pass):
- [ ] SoC confirmed as Strix Halo / Ryzen AI Max / Ryzen AI Max+
- [ ] Unified memory ≥ 16 GB
- [ ] Price ≤ 5,000 AUD
- [ ] No disqualifying sustained thermal or ROCm compatibility risk

### Track 1 Tie-breakers (in order)
1. Faster ship date
2. Better warranty or return path
3. Higher Track2_Avoidance score

### Track Escalation

**Exception A — No Viable Track 1:** Re-check Track 1 once for discounts/refurb/open-box → evaluate Track 1.5 refurbished desktop (GPU VRAM ≥ 16 GB, credible AU seller) → evaluate immediately available Track 2 → recommend highest MCDA scorer that is outcome-enabled and available now.

**Exception B — Track 2 Unicorn:** May override Track 1 only when: available now in AU from a credible seller, within Track 2 budget cap, clearly stronger for CareerCopilot workloads, materially improves Track2_Avoidance, and does not add unacceptable warranty/setup/thermal/parts/support risk. Must score higher than best Track 1 under MCDA and explicitly state why Track 1 is worse.

## Data Rules

- Unknown values stay `UNKNOWN`; never infer price, stock, VRAM, or warranty.
- All `current_best_price_aud` for Track 1A secondary-market (eBay/Refurb) must be verified against last-30-days "Sold" listings or confirmed clearance prices — not asking prices from international sellers.
- Prefer AU sources: `MANUFACTURER_AU` > `MAJOR_RETAILER_AU` > `AMAZON_AU` > `EBAY_AU` > `GUMTREE_AU`/`FB_MARKETPLACE` > `GRAY_IMPORT`.
- **Price Increase Cross-Check Rule:** When a live price check shows a previously verified price has increased on one retailer, do NOT remove a candidate or change status to over-budget based on that single retailer alone. Check at least two other AU retailers (in priority order above) before applying an over-cap gate failure. Set `current_best_price_aud` to the lowest confirmed in-stock AU price across all retailers checked.
- Use `agent-browser` skill for live AU pricing verification.
- Policy drift between `AGENTS.md` and `config/procurement_policy.json`: follow `AGENTS.md` for recommendations until config is updated.

## Pre-Decision Checklist

Before finalising any recommendation, confirm all of:
- [ ] Current AU stock confirmed from a credible seller
- [ ] Current price and effective best price confirmed
- [ ] VRAM or unified memory confirmed
- [ ] Warranty or ACL coverage confirmed
- [ ] Sustained thermal risk assessed
- [ ] All decision-critical `UNKNOWN` fields identified and either filled or flagged
- [ ] MCDA score computed
- [ ] Recommendation explains which CareerCopilot outcome (MVP / Q4 / Track2-avoidance) is supported

## Recommendation Format

Every purchase recommendation must include:
- Candidate name and track/pathway
- GOOD ENOUGH status (all gates pass, AU stock confirmed, warranty acceptable)
- MCDA score and all five factor scores
- Verified price, retailer, URL, stock status, and date checked
- Remaining risks
- Clear **buy / do-not-buy / wait** conclusion

If recommending Track 2 over Track 1, state which escalation exception applies and why Track 1 is worse.

## MCDA Formula

```
SCORE = (Performance_Headroom × 0.25) + (Price_Value × 0.20) +
        (Future_Proof × 0.20) + (Portability × 0.20) + (Track2_Avoidance × 0.15)
```

Strix Halo caps: `Performance_Headroom ≤ 7` by default; `Track2_Avoidance` capped at 6/7/8 for 32/64/128 GB unified memory unless workload benchmarks show otherwise.
