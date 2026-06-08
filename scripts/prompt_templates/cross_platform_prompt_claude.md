# Cross-Platform Opportunity Discovery Prompt — Claude Variant

> **Canonical logic lives in [`cross_platform_research_core.md`](cross_platform_research_core.md).**
> This file is a thin platform-specific wrapper only.
> When the GPU sweep list or source rules change, update `config/search_archetypes.json` — not this file.

---

## Platform-Specific Note: Claude

- Claude has access to the project files directly via the conversation context.
- No export/attachment inventory step is required (unlike the ChatGPT Project variant).
- Use the `agent-browser` skill for any live AU price/stock lookups.
- Context window is large enough for full card inventory; load `cards/laptops/` directly.

## Inputs

- Active shortlist: `shortlists/shortlist_profile-laptop_pricing_enriched_live.csv`
- Cards: `cards/laptops/`, `cards/desktops/`, `cards/apple_silicon/`, `cards/components/`, `cards/mini_pcs/`
- GPU sweep list: see `config/search_archetypes.json` → `search_templates.all_tracked_gpu_tiers`

## Prompt

Follow `cross_platform_research_core.md` exactly.

GPU tier sweep guidance (from `search_archetypes.json` → `search_templates.all_tracked_gpu_tiers`):
- RTX 5090 Laptop 24 GB
- RTX 5080 Laptop 16 GB
- RTX 5070 Ti Laptop 12 GB
- RTX 5070 Laptop 12 GB
- RTX 4090 Laptop 16 GB
- RTX 4080 Laptop 12 GB
- RTX 3080 Ti Laptop 16 GB
- RTX 3080 Laptop 16 GB
- RTX 4070 Ti Laptop 12 GB
- RTX 5000 Ada Laptop 16 GB
- RTX A5500 Laptop 16 GB
- RTX 4000 Ada Laptop 12 GB
- RTX 3500 Ada Laptop 12 GB
- Radeon RX 7900M 16 GB
- Ryzen AI Max Strix Halo Laptop 32 GB+
- RTX 3090 24 GB Desktop Refurb

High-value pass ordering (Track 1A priority):
1. RTX 4090 16 GB
2. RTX 5080 16 GB
3. RTX 3080 Ti 16 GB
4. RTX 5000 Ada 16 GB
5. RTX A5500 16 GB
6. RTX 4000 Ada 12 GB
7. RX 7900M 16 GB

## Completion Check

Output must contain all sections A–G as defined in `cross_platform_research_core.md`. If any section is missing, flag it explicitly.
