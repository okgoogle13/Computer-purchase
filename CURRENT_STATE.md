# Current State & Sprint Focus

**Last Updated:** 2026-05-04

## 1. Latest Completed Milestones
* **Structure:** Transitioned from a flat research folder into a strict 7-lane hardware evaluation workspace.
* **Automation:** Completed `tag_product_cards.py` and `sort_product_cards.sh` to automate classification of hardware candidates.
* **Policy Hardening:** Resolved all technical metric TODOs in the VRAM Architecture Spec.
* **Ingestion Assets:** Generated the `Complete_Hardware_Procurement_Knowledge_Base.md` mega-bundle as an experimental single-file NotebookLM ingestion method.
* **Strategy Refinement (2026-05-04):** Expanded Track 1 to include AMD Strix Halo unified-memory laptops (all brands, no screen floor, 32 GB minimum). Activated Track 2 as a parallel research track with three defined pathways. Relaxed NVIDIA screen size floor to 13"+.

## 2. Current Architecture Choice
**Status: LOCKED.** Proceeding with the **3-Notebook execution workflow** (Policy Brain + Desktop Arena + Mobile Arena). The filesystem lanes remain the source of truth. The mega-bundle is a secondary/fallback option. *We will not pursue both workflows simultaneously to prevent context drift.*

## 3. Active Tracks

### Track 1 — Laptop (PRIORITY — buy as soon as GOOD ENOUGH candidate confirmed)
Two active paths:
- **Path 1A (NVIDIA):** 13"+ screen floor, 16 GB VRAM minimum, 17–18" scoring bonus. Brands: Lenovo Legion, ASUS ROG, MSI.
- **Path 1B (AMD Strix Halo):** No screen floor, 32 GB unified memory minimum (64 GB preferred), all brands. ASUS TUF A16 and equivalents in scope.

### Track 2 — Workstation (ACTIVE — medium-term, parallel to Track 1)
Three pathways — do NOT delay Track 1 purchase for Track 2:
- **Pathway A:** AU system integrator custom/configurable build (Scorptec, Mwave, Centre.com). Requires confirmed build spec.
- **Pathway B:** Refurbished enterprise workstation (Dell Precision, HP Z-series, ThinkStation). ≥ 2018, ≥ 16 GB VRAM/GPU.
- **Pathway C:** Unified memory mini PC (Strix Halo, ≥ 64 GB unified). Minisforum AI X1 Pro and equivalents.

### Track 1.5 (Refurbished Gaming Desktop — Single GPU): ACTIVE
- Alienware Aurora R12 (RTX 3090) — price/performance leader
- Acer Predator Orion — under review (awaiting price/spec confirmation)
- Gate: Must beat Track 1 laptops on $/VRAM by ≥15% to justify loss of portability

## 4. Immediate Next Tasks (Current Sprint)
1. **Track 1 AMD audit:** Identify and create blank product card shells for AMD Strix Halo laptop candidates in `04_Laptops_Mainline/`.
2. **Track 2 Pathway C audit:** Create blank card shells for Strix Halo mini PC candidates in `06_Mini_PCs_and_eGPU/`.
3. **Track 2 Pathway A:** Populate `01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md` with a confirmed base build spec.
4. **Track 2 Pathway B audit:** Review `02_Refurbished_Desktop_Towers/` cards against new gate conditions (age, PCIe slots, PSU, GPU VRAM).
5. **Unified data-ready checklist:** Produce a markdown table of all UNKNOWN fields across Track 1 and Track 2 requiring manual lookup.

## 5. Deferred / Out of Scope
* **AMD Strix Halo unified-memory devices active across Track 1 (laptops) and Track 2 Pathway C (mini PCs). Track 2 all pathways now active in parallel with Track 1. Apple Silicon remains archived.**
* **AMD ROCm deep-dive:** General AMD viability noted; deep troubleshooting deferred until a specific AMD card reaches finals.
* **DIY self-build (parts sourcing):** Out of scope for Track 2. Track 2 Pathway A = AU system integrator only.
