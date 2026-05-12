# Cross-Platform Consolidation Prompt — Perplexity Variant

Use this in Perplexity for web-heavy consolidation.

```text
You are consolidating CareerCopilot hardware research with web-priority evidence handling.

Perplexity-specific evidence hierarchy:
- Prioritize authoritative AU sources first (manufacturer AU store, major AU retailers, trusted refurb channels, then marketplace sources).
- Rank evidence strength for each critical claim as: High / Medium / Low.
- If marketplace listings are used, state whether evidence is asking-price or sold-price and mark confidence accordingly.
- Never treat weak evidence as resolved fact; keep UNKNOWN where not verified.

Apply the following canonical instruction set exactly:

[BEGIN SHARED CORE]
(Use the full contents of scripts/prompt_templates/cross_platform_research_core.md verbatim.)
[END SHARED CORE]

Perplexity output controls:
- Keep output compact and schema-locked to A-F.
- Include evidence-strength annotations in A notes and C conflicts.
- Ensure dedup actions in F explicitly reference canonical key + material delta logic.

Return only sections A-F.
```
