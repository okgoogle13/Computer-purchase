# CareerCopilot MCDA Policy Pack

Generated from the simplified `AGENTS.md` policy.

## Purpose

This pack supports outcome-driven hardware scoring for CareerCopilot:

- buy one Track 1 laptop ASAP when GOOD_ENOUGH,
- keep a narrow 12 GB Track 1A bargain exception visible,
- use Track 1.5 only as a value fallback,
- keep Track 2 deferred unless an escalation trigger fires.

The bargain exception can improve `Price_Value`, but it must reduce `Performance_Headroom`,
`Future_Proof`, and `Track2_Avoidance`. Below 12 GB discrete VRAM cannot clear GOOD_ENOUGH.

## Active Files

- `rubric_weighting_engine.py` - fixed-weight MCDA ranking engine.
- `template_product_card_output.md` - current product card template.
- `HOW_TO_MAINTAIN_RUBRIC.md` - maintenance notes.

Older workstation-specific rubric files in this folder are historical references unless explicitly reopened.
