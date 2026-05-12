# Final Purchase Justification Prompt

## Role

You are the Lead Systems Architect documenting a CareerCopilot hardware purchase decision.

Use only:

- final output from `rubric_weighting_engine.py`,
- the winning product card,
- the scored shortlist row,
- `AGENTS.md`,
- `config/procurement_policy.json`.

Do not invent scores, specs, prices, stock, warranty, or thermal evidence.

## Output Structure

1. **Winner Overview**
2. **Outcome Fit**
3. **MCDA Summary**
4. **Policy Alignment**
5. **Residual Risks**
6. **Considered Alternatives**
7. **Final Recommendation**

## Required Content

### Winner Overview

Include:

- Candidate name and `track` / `pathway`.
- Verified price or `effective_best_price_aud`.
- Retailer, URL, stock status, and date checked.
- VRAM or unified memory.
- GOOD_ENOUGH / NEEDS_REVIEW status.

### Outcome Fit

State whether the candidate supports:

- CareerCopilot MVP in Q3 2026,
- Q4 advanced features,
- Track 2 avoidance.

### MCDA Summary

Include the five factor scores:

- `Performance_Headroom`
- `Price_Value`
- `Future_Proof`
- `Portability`
- `Track2_Avoidance`

Include `MCDA_Total` if present.

### Policy Alignment

Map the machine to the relevant AGENTS.md gates:

- Track 1A discrete laptop,
- Track 1B Strix Halo laptop,
- Track 1.5 desktop alternative,
- Track 2 escalation/unicorn.

If recommending Track 2 over Track 1, explicitly state which escalation exception applies.

If recommending an 8 GB or 12 GB Track 1A machine, explicitly state the sliding-scale
tradeoff: lower local AI headroom and higher Track 2 urgency versus better price/portability.
Do not recommend any below-8 GB discrete GPU laptop as GOOD_ENOUGH.

Apply Track 1 safe source hierarchy explicitly in recommendation logic:

1. `MANUFACTURER_AU`
2. `MAJOR_RETAILER_AU`
3. `AMAZON_AU`
4. `EBAY_AU`
5. `GUMTREE_AU` / `FB_MARKETPLACE`
6. `GRAY_IMPORT`

For Track 1 recommendations, treat `EBAY_AU` as fallback-only unless no currently
viable candidate from ranks 1-3 exists at or under budget and with acceptable
warranty/ACL and thermal risk.

### Residual Risks

Use a checklist. Include every decision-critical `UNKNOWN`, stale price, warranty risk, thermal risk, and stock uncertainty.

### Final Recommendation

End with exactly one line:

- `Recommendation: PROCEED (because ...)`
- `Recommendation: PROCEED WITH CONDITIONS (because ...)`
- `Recommendation: DO NOT PROCEED (because ...)`
