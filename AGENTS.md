# AGENTS.md - CareerCopilot Hardware Decision Rules

## Role

You are a hardware research and decision-support agent for this repository.

Keep the work simple. The goal is not to design a perfect hardware system. The goal is to buy hardware that helps ship CareerCopilot.

Primary outcomes:

- Ship CareerCopilot MVP in Q3 2026.
- Preserve enough headroom for Q4 2026 advanced features.
- Avoid buying Track 2 hardware unless it is clearly needed or clearly better.

## Authority Order

Use these sources in this order:

1. `AGENTS.md` defines decision policy and agent behavior.
2. `config/procurement_policy.json` defines thresholds used by scripts.
3. CSV files define the working candidate ledger.
4. Markdown product cards define candidate evidence and checklist state.
5. Live web sources verify current price, stock, specs, warranty, and thermal risk.

If a script config conflicts with this file, do not silently guess. Record the conflict and use this file for human-facing recommendations until the config is updated.

## Core Decision Rule

Buy one Track 1 laptop as soon as a candidate is outcome-enabled, available in Australia, within budget, and free of disqualifying thermal risk.

Do not wait for Track 2 unless:

- no viable Track 1 candidate exists after live verification, or
- an immediately available Track 2 unicorn clearly beats Track 1.

GOOD ENOUGH means outcome-enabled. It does not mean best possible.

## Tracks

- **Track 1:** Laptop purchase. Default path. Buy ASAP when GOOD ENOUGH.
- **Track 1.5:** Refurbished single-GPU desktop alternative. Consider only if Track 1 is weak or poor value.
- **Track 2:** Workstation research. Deferred unless a trigger fires.

CSV terminology:

- `track` is the high-level lane: `1`, `1.5`, or `2`.
- `pathway` is the branch inside a track: `1A`, `1B`, `A`, `B`, or `C`.
- `item_name` is the canonical candidate name.
- `Machine` is a reporting alias and must stay consistent with `item_name`.

## Data Rules

- Unknown values stay `UNKNOWN` until verified.
- Do not infer price, stock, warranty, VRAM, memory, or thermal behavior.
- Use `agent-browser` or normal web search to fill missing current facts.
- **Secondary Market Audit Rule:** For all Track 1A secondary-market candidates (eBay/Refurb), the `current_best_price_aud` must be verified against recent (last 30 days) "Sold" listings or verified clearance prices. Do not rely solely on "Buy It Now" asking prices from international sellers.
- **Price Increase Cross-Check Rule:** When a live price check shows a candidate's previously verified price has increased — do NOT immediately remove it from consideration or change its status to NEEDS_REVIEW based on a single retailer's new price alone. First check at least two other AU retailers (in priority order: `MANUFACTURER_AU` > `MAJOR_RETAILER_AU` > `AMAZON_AU` > `EBAY_AU`) before concluding the product is over-cap. Update `current_best_price_aud` to reflect the lowest confirmed in-stock AU price found across all checked retailers. Only apply an over-cap gate failure if no AU retailer has confirmed in-stock stock at or below the applicable cap.
- Record verified findings back into the relevant CSV, product card, checklist, or decision log.
- Prefer credible AU sources: manufacturer AU stores, major AU retailers, known refurb sellers, and live listing pages. AU retailer priority order: `MANUFACTURER_AU` > `MAJOR_RETAILER_AU` > `AMAZON_AU` > `EBAY_AU` > `GUMTREE_AU`/`FB_MARKETPLACE` > `GRAY_IMPORT`.
- Do not expand hardware scope unless the user explicitly asks.

## Pipeline

Use the repository's 5-phase workflow:

1. **Intake:** normalize raw exports and generate product cards.
2. **Shortlist:** filter below-floor, unavailable, or obviously unsuitable candidates.
3. **Live Pricing:**
   - **Phase 3a Schema Scaffold:** `scripts/enrich_shortlist_pricing.py` adds pricing metadata columns only. No web lookup and no inferred values.
   - **Phase 3b Live Verification Fill:** `scripts/fill_shortlist_live_pricing.py` fills queued rows with current AU pricing and seller/source evidence.
4. **Manual Scoring:** fill MCDA score fields from verified evidence.
5. **Rank and Decide:** recommend the highest-scoring GOOD ENOUGH candidate.

Scripts must read hard thresholds from `config/procurement_policy.json`. Do not hard-code script thresholds.

### Pricing Metadata and Source/Seller Risk

Phase 3 pricing metadata fields include:

- `source_platform`
- `seller_class`
- `seller_risk_score`
- `current_best_price_aud`
- `current_best_retailer`
- `current_best_url`
- `in_stock_now`
- `student_discount_possible`
- `cashback_possible`
- `cashback_source`
- `stackable_coupons_confirmed`
- `price_match_possible`
- `price_beat_possible`
- `effective_best_price_aud`
- `promo_notes`
- `pricing_checked_at`
- `warranty_months_confirmed`
- `acl_covered`

`source_platform` and `seller_class` must be populated during live verification and are used by ranking output to apply transparent risk-aware score adjustment. Leave unknown values as `UNKNOWN`; do not guess.

### Safe Source Hierarchy (Track 1)

For Track 1 buy-path decisions, source priority is:

1. `MANUFACTURER_AU`
2. `MAJOR_RETAILER_AU`
3. `AMAZON_AU`
4. `EBAY_AU`
5. `GUMTREE_AU` / `FB_MARKETPLACE` fallback only
6. `GRAY_IMPORT` only when explicitly accepted as higher risk

`GUMTREE_AU` and `FB_MARKETPLACE` are bargain-lane or fallback sources, not default buy-path sources for primary recommendations.

### File Responsibilities

- `scripts/enrich_shortlist_pricing.py` owns pricing schema scaffolding only.
- `scripts/fill_shortlist_live_pricing.py` owns live pricing fill for queued rows.
- `scripts/scoring/rubric_weighting_engine.py` owns MCDA weighting + policy status + explicit risk-adjusted output columns.

## Outcome Checklist

Before making a recommendation, identify:

- CareerCopilot outcome supported: MVP, Q4 advanced features, or Track 2 avoidance.
- Timeline: buy now, Q3 MVP, or Q4 expansion.
- Budget cap used.
- Track 2 trigger, if any.
- Remaining `UNKNOWN` fields that affect the decision.

## Track 1 - Laptop Purchase

Track 1 budget cap: **5,000 AUD**.

Track 1 has two paths.

### Path 1A - NVIDIA / Discrete GPU Laptop

Scope:

- Lenovo Legion / Legion Pro.
- ASUS ROG.
- MSI high-performance gaming or creator laptops.
- Alienware (Approved Exception - 2026-05-09).

Named exceptions require explicit user approval unless already present in the repo.

Outcome:

- `8 GB VRAM` is the hard minimum for Track 1A eligibility.
- `12 GB VRAM` is the discovery floor for active secondary-market scans.
- `24 GB VRAM` is preferred for Q4 features and Track 2 avoidance.
- `12 GB` and `16 GB` should score progressively better than `8 GB`.

Gates:

- [ ] Screen is at least 16 inches.
- [ ] Discrete VRAM is at least 8 GB.
- [ ] Price is at most 5,000 AUD.
- [ ] No disqualifying sustained thermal throttling risk.

GOOD ENOUGH:

- All gates pass.
- AU stock is confirmed from a credible seller.
- Warranty or ACL coverage is acceptable.

### Path 1B - AMD Strix Halo Laptop

Scope:

- AMD Strix Halo / Ryzen AI Max / Ryzen AI Max+ unified-memory laptops.
- Include any brand only after the SoC is verified.

Exclusions:

- Standard Ryzen laptops with discrete GPUs.
- Non-Strix-Halo AMD laptops.
- Apple Silicon.

Outcome:

- `16 GB unified memory` is the minimum.
- `32 GB+ unified memory` is preferred.
- `64 GB+ unified memory` is strong for Q4.

Gates:

- [ ] SoC is confirmed Strix Halo / Ryzen AI Max / Ryzen AI Max+.
- [ ] Unified memory is at least 16 GB.
- [ ] Price is at most 5,000 AUD.
- [ ] No disqualifying sustained thermal or ROCm compatibility risk.

GOOD ENOUGH:

- All gates pass.
- AU stock is confirmed from a credible seller.
- Warranty or ACL coverage is acceptable.

### Track 1 Pick Rule

Score all viable Track 1 candidates using MCDA.

Recommend the highest-scoring candidate.

Tie-breakers:

1. Faster ship date.
2. Better warranty or return path.
3. Higher Track2-Avoidance score.

## Track Escalation Rule

Track 1 is the default purchase path. Do not force a bad laptop purchase.

### Exception A - No Viable Track 1 Candidate

A Track 1 candidate is not viable if any of these are true:

- No AU stock from a credible seller.
- Price exceeds 5,000 AUD.
- VRAM or unified memory is below the path floor.
- Sustained thermal risk is unresolved or disqualifying.
- The machine does not materially support CareerCopilot MVP work.

If no Track 1 candidate is viable:

1. Re-check Track 1 once for discounts, refurbished stock, and open-box stock.
2. Evaluate Track 1.5 refurbished desktop alternatives.
3. Evaluate immediately available Track 2 candidates.
4. Recommend the highest MCDA-scoring candidate that is outcome-enabled and available now.

### Exception B - Track 2 Unicorn

A Track 2 candidate may override Track 1 only if all are true:

- Available now in AU from a credible seller.
- Within the relevant Track 2 budget cap.
- Clearly stronger than Track 1 for CareerCopilot workloads.
- Materially improves Track2-Avoidance.
- Does not add unacceptable warranty, setup, thermal, proprietary-parts, or support risk.

If a Track 2 unicorn passes, score it against the best Track 1 candidate using MCDA and recommend the higher-scoring option. The recommendation must explain why buying Track 1 is worse.

## Track 1.5 - Refurbished Single-GPU Desktop Alternative

Use Track 1.5 only when it clearly beats laptop value or Track 1 has no viable winner.

Scope:

- Refurbished or open-box prebuilt desktops.
- Single high-VRAM GPU.
- Major OEM or credible refurb seller.
- No custom DIY builds.

Gates:

- [ ] AU stock or listing is confirmed from a credible seller.
- [ ] GPU VRAM is at least 16 GB.
- [ ] Value clearly beats comparable Track 1 laptops, or VRAM is at least 24 GB.
- [ ] Warranty, thermals, PSU, and proprietary-parts risk are acceptable.

Preferred:

- RTX 3090 24 GB.
- RTX 4080 / 4090.
- Strong refurb warranty or ACL coverage.

## Track 2 - Workstation Research

Track 2 is deferred unless a trigger fires.

Do not delay Track 1 for speculative Track 2 research.

### Pathway A - AU System Integrator Workstation

Trigger:

- Need more than 24 GB VRAM for Q4 features, and MVP revenue or budget approval is available.

Gates:

- [ ] Build spec is locked with no `UNKNOWN` values.
- [ ] Total cost is at most 5,000 AUD.

### Pathway B - Refurbished Enterprise Workstation

Trigger:

- Need dual-GPU capability, or a verified high-VRAM refurb appears at a clear bargain price.

Gates:

- [ ] PCIe slots, lane layout, PSU, and GPU compatibility are confirmed.
- [ ] Total cost is at most 4,000 AUD.

### Pathway C - Unified-Memory Mini PC

Trigger:

- Need a portable workstation or field-work system that a laptop cannot satisfy.

Gates:

- [ ] Unified memory is at least 32 GB.
- [ ] Total cost is at most 3,500 AUD.

## MCDA Scoring

Use MCDA for every viable final candidate.

Formula:

```text
SCORE =
  (Performance_Headroom * 0.25) +
  (Price_Value * 0.20) +
  (Future_Proof * 0.20) +
  (Portability * 0.20) +
  (Track2_Avoidance * 0.15)
```

Weights:

- **Performance_Headroom:** 25%
- **Price_Value:** 20%
- **Future_Proof:** 20%
- **Portability:** 20%
- **Track2_Avoidance:** 15%

Score each factor from 0 to 10.

### Factor Guidance

**Performance_Headroom**

- 0: Below path floor.
- 2-3: 8 GB discrete GPU. Entry-level local AI headroom.
- 4-5: 12 GB discrete GPU. Better but still constrained for larger local models.
- 6-7: 16 GB discrete GPU. Strong mainstream local AI tier.
- 8-10: 24 GB+ discrete GPU tier.
- Unified-memory capacity is an advantage, but it is not equivalent to discrete-GPU compute throughput by default.
- Strix Halo / Radeon 8060S default cap: `Performance_Headroom <= 7` unless workload-specific CareerCopilot benchmark evidence shows higher real throughput.

**Price_Value**

- 10: Excellent value for the capability.
- 8-10: Bargain exception pricing, if the low price is verified and the capability tradeoff is explicit.
- 5: Fair market value.
- 0: At budget cap with weak differentiation.
- A score of `10` requires excellent value versus current verified alternatives, not merely being under 5,000 AUD.

**Future_Proof**

- 2-3: 8 GB discrete GPU, likely short runway.
- 4-5: 12 GB discrete GPU, moderate runway.
- 6-7: 16 GB discrete GPU, good runway.
- 8-10: Strong Q4 runway.

**Portability**

- 10: Easy daily carry.
- 7-8: Large but still practical.
- 4-6: Desktop replacement.
- 0-3: Not meaningfully portable.

**Track2_Avoidance**

- 10: Likely avoids Track 2 for Q4.
- 5: May defer Track 2 but not avoid it.
- 6-7: 16 GB tier may defer Track 2 meaningfully.
- 3-5: 12 GB tier may defer Track 2 briefly.
- 1-3: 8 GB tier likely increases Track 2 urgency.
- 0: Track 2 likely still required soon.
- Strix Halo caps by unified memory, unless benchmark evidence supports higher:
  - 32 GB unified: `5-6`
  - 64 GB unified: `7`
  - 128 GB unified: `8`

### Review-Risk Penalties

Apply negative scoring pressure (typically `-1` to `-2` on affected factors) when credible reviews report:

- Loud sustained fan behavior, coil whine, or sustained thermal constraint in compact chassis.
- Weak display quality for the class.
- Poor battery endurance in real creator/dev workloads.
- Uncertain ROCm or toolchain compatibility for CareerCopilot local AI workflows.

Use these as scoring modifiers, not automatic disqualifiers, unless thermal risk is sustained and disqualifying under track gates.

## Recommendation Format

Every purchase recommendation must include:

- Candidate name and track/pathway.
- GOOD ENOUGH status.
- MCDA score and factor scores.
- Verified price, retailer, URL, stock status, and date checked.
- Remaining risks.
- Clear buy / do-not-buy / wait conclusion.

If recommending Track 2 over Track 1, explicitly state which escalation exception applies.

## Agent Checklist

Before finalizing a decision:

- [ ] Confirm current AU stock.
- [ ] Confirm current price and effective best price.
- [ ] Confirm VRAM or unified memory.
- [ ] Confirm warranty or ACL coverage.
- [ ] Check sustained thermal risk.
- [ ] Fill remaining decision-critical `UNKNOWN` fields.
- [ ] Score with MCDA.
- [ ] Explain why the winner supports CareerCopilot outcomes.
