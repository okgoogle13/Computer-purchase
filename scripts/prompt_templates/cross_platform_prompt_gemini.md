# Cross-Platform Consolidation Prompt — Gemini Variant

Use this in Gemini when combining file context and web evidence.

```text
You are consolidating hardware product research for CareerCopilot.

Gemini-specific evidence rules:
- Every material claim must include source citation context inline (source name + date if visible).
- Distinguish observed facts vs inferred judgments.
- When uncertain, say UNKNOWN and lower confidence explicitly.
- If two sources disagree, include both values, note confidence for each, and prefer the most recent credible AU source provisionally.

Apply the following canonical instruction set exactly:

[BEGIN SHARED CORE]
(Use the full contents of scripts/prompt_templates/cross_platform_research_core.md verbatim.)
[END SHARED CORE]

Gemini output controls:
- Avoid narrative expansion outside A-F.
- Include short citation tags in A, C, and F notes.
- Keep scoring normalization explicit for each retained row.

Return only sections A-F.
```
