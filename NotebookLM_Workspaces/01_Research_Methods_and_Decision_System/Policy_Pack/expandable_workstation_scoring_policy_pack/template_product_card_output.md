# Template - Product Card Output

Use this structure for new candidate cards.

```markdown
<!-- PRODUCT CARD START: [item_name] -->
---
id: [slug]
category: [laptop | desktop | mini pc | component | ...]
track: [1 | 1.5 | 2 | UNKNOWN]
pathway: [1A | 1B | A | B | C | UNKNOWN]
name: [item_name]
gpu: [GPU model or UNKNOWN]
vram: [GB or UNKNOWN]
unified_memory: [GB or UNKNOWN]
screen_size_in: [inches or UNKNOWN]
thermal_flag: [Clear | Flagged | Disqualifying | UNKNOWN]
price_aud: [AUD or UNKNOWN]
condition: [New | Refurbished | Open Box | Used | UNKNOWN]
au_stock: [Yes | No | UNKNOWN]
verification: [Verified | Needs Verification | Unverified]
status: [Active | Watchlist | Out of Stock | Superseded]
score: UNKNOWN - pending MCDA scoring
---

# [item_name]

## Outcome Fit
- **CareerCopilot MVP:** UNKNOWN
- **Q4 advanced features:** UNKNOWN
- **Track2_Avoidance:** UNKNOWN

## Track Status
- **Track:** [1 | 1.5 | 2 | UNKNOWN]
- **Pathway:** [1A | 1B | A | B | C | UNKNOWN]
- **GOOD ENOUGH check:** PENDING

## Overview
- **Price (AUD):** UNKNOWN
- **Retailer:** UNKNOWN
- **URL:** UNKNOWN
- **Condition:** UNKNOWN
- **AU Stock:** UNKNOWN
- **Warranty / ACL:** UNKNOWN

## Key Specs
- **GPU:** UNKNOWN
- **VRAM:** UNKNOWN
- **Unified Memory:** UNKNOWN
- **Screen Size:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Thermal risk:** UNKNOWN

## MCDA Scores
- **Performance_Headroom:** UNKNOWN
- **Price_Value:** UNKNOWN
- **Future_Proof:** UNKNOWN
- **Portability:** UNKNOWN
- **Track2_Avoidance:** UNKNOWN
- **MCDA_Total:** UNKNOWN

## Verification Checklist
- [ ] Confirm current AU stock from named seller with URL
- [ ] Confirm current price or effective best price
- [ ] Confirm VRAM or unified memory
- [ ] Confirm screen size where applicable
- [ ] Confirm warranty / ACL coverage
- [ ] Check sustained thermal risk
- [ ] Confirm CareerCopilot outcome fit
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared

<!-- PRODUCT CARD END: [item_name] -->
```
