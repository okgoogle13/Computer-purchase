---
name: price-verify
description: Live AU price check for a named hardware candidate. Pass the model name as the argument, e.g. /price-verify "Lenovo Legion Pro 7i RTX 4090". Returns structured JSON matching the browser_pricing_lookup.md output contract.
---

# Price Verify

Read `scripts/prompt_templates/browser_pricing_lookup.md` and follow it exactly for the candidate named in the argument.

Target item: (use the argument passed to this skill)

Completion check: output must be a single valid JSON object matching the contract defined in `browser_pricing_lookup.md`. If the price on one retailer has increased vs a previously recorded value, check at least two other AU retailers before applying an over-cap gate failure — per the Price Increase Cross-Check Rule in CLAUDE.md.
