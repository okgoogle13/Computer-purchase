---
name: opportunity-audit
description: Run the two-phase lost-opportunity audit (prior-conversation gap check then net-new discovery) against the current shortlist and cards. Follows the canonical prompt in scripts/prompt_templates/cross_platform_research_core.md exactly. Platform-specific wrappers (claude/gemini/perplexity/chatgpt) delegate back to that core.
---

# Opportunity Audit

1. Read `scripts/prompt_templates/cross_platform_prompt_claude.md` for Claude-specific notes.
2. That file delegates to `scripts/prompt_templates/cross_platform_research_core.md` for canonical workflow and output contract (A–G).
3. GPU sweep list is in `config/search_archetypes.json` → `search_templates.all_tracked_gpu_tiers`.

Current inputs:
- Active shortlist: `shortlists/shortlist_profile-laptop_pricing_enriched_live.csv`
- Cards: `cards/laptops/`, `cards/desktops/`, `cards/apple_silicon/`, `cards/components/`, `cards/mini_pcs/`

Completion check: output must contain all sections A–G as defined in `cross_platform_research_core.md`. If any section is missing, flag it explicitly.
