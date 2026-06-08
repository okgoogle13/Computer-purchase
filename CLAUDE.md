# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

AI-assisted hardware procurement decision system for selecting hardware to ship CareerCopilot MVP (Q3 2026). The system uses a 5-phase pipeline: intake → shortlist → live pricing → manual MCDA scoring → ranked recommendation.

**Default goal:** Buy one Track 1 laptop that is outcome-enabled, AU-available, ≤5,000 AUD, and free of disqualifying thermal risk. Do not wait for Track 2.

## Token Efficiency

**Anti-patterns (avoid):**
- Re-reading full CSVs when you need one row — use `grep` or `head -2` instead
- Running `build_shortlist.py` when only pricing changed — use `fill_shortlist_live_pricing.py`
- Browser sweeps across 20 pages when a targeted search suffices
- Asking for "all candidates" when the question is about the top 3

**Compact before:** Phase 3b browser pricing runs (context-heavy) and MCDA ranking.

**Model routing:**

| Task type | Tier |
|---|---|
| Grep, read cards, search CSVs | Haiku |
| Shortlist filtering, policy checks | Haiku |
| MCDA scoring, price cross-checks | Sonnet |
| Final recommendation, escalation | Sonnet |

Switch: `/model haiku` before search sweeps; `/model sonnet` before scoring.

## Pipeline Commands

```bash
# Phase 0 — Spec Clarification (optional, interactive)
# Outputs structured JSON to feed into --spec-json below
python scripts/agents/spec_clarifier/agent.py

# Phase 1 — Intake: normalize raw CSV and generate product cards
python scripts/normalize_intake.py NotebookLM_Workspaces/intake/raw/YYYY-MM-DD_batch.csv
python scripts/intake_to_cards.py NotebookLM_Workspaces/intake/processed/YYYY-MM-DD_batch_processed.csv --overwrite

# Phase 2 — Shortlist (accepts optional --spec-json from Phase 0 or --archetype)
python scripts/build_shortlist.py
python scripts/build_shortlist.py --spec-json '{"track_preference":"1A","budget_cap_aud":4500}'
python scripts/build_shortlist.py --archetype gaming_laptop_private_sale
python scripts/build_shortlist.py --archetype gaming_laptop_retailer
python scripts/build_shortlist.py --archetype strix_halo_laptop
python scripts/build_shortlist.py --archetype refurb_workstation_au

# Phase 3a — Pricing schema scaffold only (no live lookup)
# Shortlist files use profile-based names, e.g. shortlist_profile-laptop.csv
python scripts/enrich_shortlist_pricing.py shortlists/shortlist_profile-laptop.csv

# Phase 3b — Live pricing fill (AU verification)
python scripts/fill_shortlist_live_pricing.py shortlists/shortlist_profile-laptop_pricing_enriched.csv

# Phase 4 — Fill any missing MCDA score columns
python scripts/fill_mcda_gaps.py shortlists/shortlist_profile-laptop_pricing_enriched_live.csv

# Phase 5 — MCDA ranking
python scripts/scoring/rubric_weighting_engine.py \
  --csv shortlists/shortlist_profile-laptop_pricing_enriched_live.csv \
  --output-csv shortlists/shortlist_profile-laptop_ranked.csv

# Full orchestrated run
python scripts/run_prompt_chain.py --batch YYYY-MM-DD_notebooklm_batchN

# Validation
python scripts/policy_drift_check.py
python scripts/validate_prompt_templates.py
python scripts/pipeline_integrity_check.py \
  --enriched shortlists/shortlist_profile-laptop_pricing_enriched_live.csv \
  --ranked shortlists/shortlist_profile-laptop_ranked.csv

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
- `config/search_archetypes.json` — canonical archetype config: GPU sweep lists, price ceilings, source rules, intent notes. Update here when adding new GPU tiers or archetype rules. Referenced by `build_shortlist.py --archetype` and all cross-platform prompts.
- `shortlists/` — CSV working files at each pipeline stage (named `shortlist_profile-<type>*.csv`)
- `cards/` — markdown product cards, organised in subdirectories by hardware class:
  - `cards/laptops/` — primary Track 1A/1B candidates
  - `cards/desktops/`, `cards/apple_silicon/`, `cards/components/`, `cards/mini_pcs/`
  - Naming prefixes: `intake-NNN_` (normalised intake), `harvest-YYYYMMDD-NNN_` (LLM harvest), `fb-NNN_` (Facebook/Gumtree sourced), numeric-only (eBay secondary-market)
- `scripts/README_pipeline.md` — detailed per-phase workflow
- `scripts/agents/spec_clarifier/` — Phase 0 conversational intake agent (ADK pattern; outputs `--spec-json` blob)
- `scripts/data_collection/` — eBay/Facebook/Gumtree scraping and mapping scripts
- `scripts/import/` — browser agent JS scripts for eBay watchlist ingestion
- `scripts/requirements.txt` — Python dependencies (install before running pipeline)

**Script ownership (strict):**
- `enrich_shortlist_pricing.py` — schema scaffold ONLY, no web lookup, no inferred values
- `fill_shortlist_live_pricing.py` — live AU pricing fill for queued rows only
- `fill_mcda_gaps.py` — fills missing MCDA score columns before ranking
- `rubric_weighting_engine.py` — MCDA weighting + risk-adjusted output columns
- `scoring/auto_score_cards.py` — auto-scores cards from shortlist data
- `harvest_llm_recommendations.py` — harvests LLM-sourced candidates into intake format

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
