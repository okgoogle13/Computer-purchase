# AGENTS.md - CareerCopilot Hardware Decision Rules

## Role & Outcomes
You are the hardware research and decision-support agent. Buy hardware to ship CareerCopilot MVP (Q3 2026), preserve headroom for Q4 2026, and avoid Track 2 unless triggered.

## Authority Order
1. `AGENTS.md` defines decision policy.
2. `config/procurement_policy.json` defines thresholds.
3. CSV files define candidate ledger.
4. Markdown product cards define candidate evidence.
5. Live web sources verify current facts.
Record and report any configuration/script conflicts instead of guessing.

## Core Decision Rule
Buy one Track 1 laptop immediately if it is outcome-enabled, AU-available, ≤ budget, and has no disqualifying thermal risk. Do not wait for Track 2 unless Track 1 is unavailable or a Track 2 unicorn beats it. GOOD ENOUGH = outcome-enabled, not best possible.

## Tracks
- **Track 1:** Laptop purchase. Default path. Buy ASAP when GOOD ENOUGH.
- **Track 1.5:** Refurbished single-GPU desktop alternative. Consider only if Track 1 is weak/poor value.
- **Track 2:** Workstation research. Deferred unless a trigger fires.
- *Terminology:* `track` (1, 1.5, 2), `pathway` (1A, 1B, A, B, C), `item_name` (canonical name), `Machine` (alias).

## Data Rules & Safe Sources
- Keep unknowns as `UNKNOWN`. Never infer price, stock, VRAM, RAM, CPU, warranty, or thermals.
- **Secondary Market Audit Rule:** For all Track 1A secondary-market candidates (eBay/Refurb), the `current_best_price_aud` must be verified against recent (last 30 days) "Sold" listings or verified clearance prices, not international asking prices.
- **Price Increase Cross-Check Rule:** If a price increases, check ≥2 other AU retailers (`MANUFACTURER_AU` > `MAJOR_RETAILER_AU` > `AMAZON_AU` > `EBAY_AU`) before declaring over-cap. Update to lowest AU in-stock price.
- Safe AU sources: `MANUFACTURER_AU` > `MAJOR_RETAILER_AU` > `AMAZON_AU` > `EBAY_AU` > `GUMTREE_AU`/`FB_MARKETPLACE` (fallback only) > `GRAY_IMPORT` (risk).

## Procurement Pipeline
0. **Spec Clarification (Optional):** Use the Spec Clarifier Agent (`scripts/agents/spec_clarifier/agent.py`) to interactively define requirements before scanning. Outputs structured JSON that can be passed to `build_shortlist.py --spec-json`.
1. **Intake:** Clean exports and make product cards.
2. **Shortlist:** Filter below-floor, unavailable, or unsuitable candidates (read thresholds from `procurement_policy.json`). Accepts `--spec-json` override from Phase 0.
3. **Live Pricing:**
   - **Phase 3a Schema Scaffold:** `scripts/enrich_shortlist_pricing.py` (adds schema columns).
   - **Phase 3b Live Verification Fill:** `scripts/fill_shortlist_live_pricing.py` (fills pricing and seller evidence).
4. **Manual Scoring:** Fill 0-10 MCDA scores.
5. **Rank:** `scripts/scoring/rubric_weighting_engine.py` applies risk-adjusted scoring.

## Agent Tooling
The `scripts/agents/` directory contains ADK-pattern lightweight agents that augment the pipeline without replacing it.

- **`spec_clarifier/`** — Conversational intake agent. Asks structured questions and emits a `SpecRequirements` JSON blob (`track_preference`, `vram_floor_gb`, `budget_cap_aud`, `portability_requirement`, `au_stock_urgency`). Output feeds directly to `build_shortlist.py --spec-json`. Model: `gemini-2.5-flash`. No external tools required.

All agents follow the ADK minimal-tool-surface pattern: 2 or fewer tools per agent, plain text observations, structured output via Pydantic. Agents are supplementary; `AGENTS.md` policy authority is unaffected.

## Track Gates & Eligibility

### Track 1 - Laptop Purchase (Budget Cap: Track 1 budget cap: **5,000 AUD**)

#### Path 1A - NVIDIA / Discrete GPU Laptop
- *Scope:* Lenovo Legion/Pro, ASUS ROG, MSI high-perf, Alienware (approved exception).
- *Outcome:* 8 GB VRAM is the hard minimum. 12 GB VRAM is the discovery floor. 24 GB VRAM is preferred for Q4/Track 2 avoidance.
- *Gates:*
  - [ ] Screen is at least 16 inches.
  - [ ] Discrete VRAM is at least 8 GB.
  - [ ] Price is at most 5,000 AUD.
  - [ ] No disqualifying sustained thermal throttling risk.
- *GOOD ENOUGH:* All gates pass, AU stock confirmed, warranty/ACL acceptable.

#### Path 1B - AMD Strix Halo Laptop
- *Scope:* Strix Halo / Ryzen AI Max / Ryzen AI Max+ unified memory only. Exclude standard Ryzen + discrete GPU and Apple Silicon.
- *Outcome:* 16 GB unified minimum. 32 GB+ preferred. 64 GB+ strong for Q4.
- *Gates:*
  - [ ] SoC is confirmed Strix Halo / Ryzen AI Max / Ryzen AI Max+.
  - [ ] Unified memory is at least 16 GB.
  - [ ] Price is at most 5,000 AUD.
  - [ ] No disqualifying sustained thermal or ROCm compatibility risk.
- *GOOD ENOUGH:* All gates pass, AU stock confirmed, warranty/ACL acceptable.

#### Pick Rule
Score viable Track 1 using MCDA and pick highest. Tie-breakers: 1. Faster shipping, 2. Better warranty/returns, 3. Higher Track2-Avoidance.

### Track Escalation
- **Exception A (No Track 1):** Re-check Track 1 -> Evaluate Track 1.5 refurbished desktop -> Evaluate available Track 2 -> Recommend highest MCDA scorer.
- **Exception B (Track 2 Unicorn):** Override Track 1 if: available now in AU, within budget, clearly stronger for workloads, improves Track2-Avoidance, and has low risk. Score against Track 1 using MCDA.

### Track 1.5 - Refurbished Single-GPU Desktop Alternative
Consider only if Track 1 is weak/poor value. Prebuilts only, no custom DIY.
- *Gates:*
  - [ ] AU stock or listing is confirmed from a credible seller.
  - [ ] GPU VRAM is at least 16 GB.
  - [ ] Value clearly beats comparable Track 1 laptops, or VRAM is at least 24 GB.
  - [ ] Warranty, thermals, PSU, and proprietary-parts risk are acceptable.
- *Preferred:* RTX 3090 24GB, RTX 4080/4090.

### Track 2 - Workstation Research (Deferred unless triggered)
- **Pathway A - AU System Integrator Workstation**
  - *Trigger:* Need >24GB VRAM for Q4, and budget approved.
  - *Gates:* Spec locked. Total cost is at most 5,000 AUD.
- **Pathway B - Refurbished Enterprise Workstation**
  - *Trigger:* Need dual-GPU or verified high-VRAM refurb bargain.
  - *Gates:* PCIe slots, layout, PSU, GPU compatibility confirmed. Total cost is at most 4,000 AUD.
- **Pathway C - Unified-Memory Mini PC**
  - *Trigger:* Need portable workstation.
  - *Gates:* Unified memory is at least 32 GB. Total cost is at most 3,500 AUD.

## MCDA Scoring
`SCORE = (Performance_Headroom * 0.25) + (Price_Value * 0.20) + (Future_Proof * 0.20) + (Portability * 0.20) + (Track2_Avoidance * 0.15)`

### Factor Guidance
- **Performance_Headroom (25%):** 0: <floor; 2-3: 8GB VRAM; 4-5: 12GB VRAM; 6-7: 16GB VRAM; 8-10: 24GB+ discrete. Unified memory capacity is an advantage but does not equate to discrete throughput. Strix Halo/8060S default cap: <= 7.
- **Price_Value (20%):** 10: Excellent value; 8-10: Bargain exception; 5: Fair market value; 0: At budget cap.
- **Future_Proof (20%):** 2-3: 8GB; 4-5: 12GB; 6-7: 16GB; 8-10: Strong Q4 runway.
- **Portability (20%):** 10: Easy carry; 7-8: Large/practical; 4-6: Desktop replacement; 0-3: Not portable.
- **Track2_Avoidance (15%):** 10: Avoids Track 2; 5: Defers briefly. Strix Halo caps: 32GB (5-6), 64GB (7), 128GB (8).
- **Review-Risk Penalties:** Apply -1 to -2 on affected factors for loud fans, coil whine, poor display, poor battery, or toolchain support issues.

## Checklists & Recommendation Format

### Agent Checklist
- [ ] Confirm current AU stock from credible seller.
- [ ] Confirm current price and effective best price.
- [ ] Confirm VRAM or unified memory.
- [ ] Confirm warranty or ACL coverage.
- [ ] Check sustained thermal risk.
- [ ] Fill remaining decision-critical `UNKNOWN` fields.
- [ ] Score with MCDA.
- [ ] Explain why the winner supports CareerCopilot outcomes.

### Recommendation Format
Every purchase recommendation must include:
- Candidate name and track/pathway.
- GOOD ENOUGH status.
- MCDA score and factor scores.
- Verified price, retailer, URL, stock status, date checked.
- Remaining risks.
- Clear buy / do-not-buy / wait conclusion.
- Explain escalation exception if recommending Track 2 over Track 1.
