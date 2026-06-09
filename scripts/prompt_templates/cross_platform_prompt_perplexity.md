# Cross-Platform Opportunity Discovery Prompt — Perplexity Sonar Deep Research Variant

> **Canonical logic lives in [`cross_platform_research_core.md`](cross_platform_research_core.md).**
> This file is a thin platform-specific wrapper only.
> When the GPU sweep list or source rules change, update `config/search_archetypes.json` — not this file.

---

## Platform-Specific Note: Perplexity Sonar Deep Research

- Perplexity excels at real-time AU web search. Use it primarily for Phase 2 live market discovery.
- Tag each critical claim with confidence level: `High`, `Medium`, `Low`.
- For marketplace pricing, explicitly distinguish ask vs sold vs verified clearance evidence.
- Perplexity does not have access to repository files — paste relevant context from:
  - `AGENTS.md` (track gates, budget caps, source priority)
  - Top 5–10 rows of the current active shortlist CSV
  - `config/search_archetypes.json` → `search_templates.all_tracked_gpu_tiers`

## Inputs (paste as context)

- Budget cap: $5,000 AUD (Track 1), $3,500 AUD (private-sale archetype)
- GPU sweep list: see `config/search_archetypes.json` → `search_templates.all_tracked_gpu_tiers`
- Source priority: MANUFACTURER_AU > MAJOR_RETAILER_AU > AMAZON_AU > EBAY_AU > GUMTREE_AU/FB_MARKETPLACE > GRAY_IMPORT

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
- RTX 4000 Ada Laptop 12 GB
- RTX 3500 Ada Laptop 12 GB
- Radeon RX 7900M 16 GB
- Ryzen AI Max Strix Halo Laptop 32 GB+
- RTX Spark Laptop 32 GB+
- RTX 3090 24 GB Desktop Refurb

High-value pass ordering (Track 1A priority):
1. RTX 4090 16 GB
2. RTX 4080 12 GB
3. RTX 3080 Ti 16 GB
4. RX 7900M 16 GB
5. RTX 5000 Ada 16 GB

## Completion Check

Output must contain all sections A–G as defined in `cross_platform_research_core.md`. If any section is missing, flag it explicitly.
