<!-- TAGS: #MiniPC #AMD #StrixHalo #UnifiedMemory #Track2-PathwayC #New #NeedsManualData #VRAM-Unified-64GB+ -->
---
id: minisforum-ai-x1-pro-strix-halo
category: mini-pc
pathway: Track2-C
name: Minisforum AI X1 Pro — AMD Ryzen AI Max+ (Strix Halo, up to 128 GB)
gpu: AMD Radeon integrated Strix Halo GPU (unified memory)
vram: UNKNOWN (unified — 64 GB / 96 GB / 128 GB configs; confirm SKU)
score: UNKNOWN — pending manual AU retailer data
---

# Minisforum AI X1 Pro — AMD Ryzen AI Max+ (Strix Halo)

> ⚠️ **BLANK SHELL — all fields require manual data entry from AU retailer research.**
> Agent must not infer or guess missing values. UNKNOWN fields stay UNKNOWN until manually updated.

## Track 2 Pathway C Status
- **Pathway:** C — Unified Memory Mini PC
- **SoC requirement:** AMD Ryzen AI Max+ (Strix Halo) ✅ — confirmed SoC family (verify exact model at purchase)
- **Unified memory floor:** 64 GB minimum required for Pathway C gate clearance
- **Gate status:** ALL gates UNKNOWN — manual verification required before any action

## Pathway C Go/No-Go Gate Checklist
- [ ] SoC confirmed as Strix Halo (Ryzen AI Max / AI Max+) — NOT standard Ryzen or Intel
- [ ] Unified memory ≥ 64 GB confirmed from spec sheet for this SKU
- [ ] AU stock confirmed at credible retailer (Scorptec, Mwave, Centre Com, or official AU distributor)
- [ ] Price within AUD budget (0–4,000 AUD)
- [ ] Thermal adequacy confirmed — active cooling present and sufficient for sustained LLM inference
- [ ] No disqualifying ROCm gap for target workloads

## Overview
- **Unified Memory Tier:** UNKNOWN — expected configs: 64 GB / 96 GB / 128 GB (confirm SKU)
- **Price (AUD):** UNKNOWN — requires AU retailer check
- **Vendor (AU):** UNKNOWN — check: official Minisforum AU distributor, Scorptec, Mwave, Centre Com
- **In stock in AU:** UNKNOWN ← **critical gate**

## Key Specs
- **SoC:** AMD Ryzen AI Max+ (Strix Halo) — confirm exact model variant (890M, 395+, or equivalent)
- **Unified Memory:** UNKNOWN GB LPDDR5X — confirm SKU (64 / 96 / 128 GB options expected)
- **GPU portion (estimated):** UNKNOWN — Strix Halo typically allocates 60–75% of unified memory to GPU; 128 GB config ≈ 96 GB GPU-accessible
- **CPU cores:** UNKNOWN
- **Storage:** UNKNOWN (M.2 slots — confirm count and size)
- **Ports:** UNKNOWN — confirm Thunderbolt / USB4 / display outputs
- **Cooling:** UNKNOWN — confirm active fan cooling (passive = ⚠️ flag for sustained inference)
- **Form factor:** Mini PC / compact desktop
- **Dimensions:** UNKNOWN
- **Power supply:** UNKNOWN W — confirm external adapter or internal PSU
- **Warranty (AU):** UNKNOWN

## Thermal Notes
- **Sustained TDP (SoC):** UNKNOWN W
- **Cooling system:** UNKNOWN — active cooling required; passive-only is a Pathway C disqualifying flag
- **Thermal reputation under sustained load:** UNKNOWN

## ROCm / Software Compatibility
- **ROCm version support:** UNKNOWN — flag any known gaps for llama.cpp, Ollama, VLLM workloads
- **HIP SDK:** UNKNOWN
- **Known compatibility issues:** UNKNOWN

## AI Capability Summary
UNKNOWN — to be completed after specs confirmed. At 128 GB unified memory: expect capability for 70B Q4 models fully in-memory; 405B Q4 with offloading. At 64 GB: 34B–70B Q4 range. This is the primary Pathway C candidate due to memory ceiling potential.

## Rubric Scores (Pathway C profile — all UNKNOWN)
- UnifiedMemory_Adequacy: UNKNOWN
- SoC_Compute_Tier: UNKNOWN
- Sustained_Thermal_Rating: UNKNOWN
- AU_Retailer_Confidence: UNKNOWN ← **gate-critical**
- Price_AUD_Competitiveness: UNKNOWN
- ROCm_Compatibility_Flag: UNKNOWN ← **disqualifying flag if severe gap**
- Cooling_Adequacy: UNKNOWN ← **disqualifying flag if passive-only**
- Connectivity_Score: UNKNOWN

## Verification Required Before Any Action
- [ ] Confirm AU stock from named retailer with URL and price
- [ ] Confirm SoC: Ryzen AI Max+ (Strix Halo)
- [ ] Confirm exact unified memory size for available AU SKU (64 / 96 / 128 GB)
- [ ] Confirm active cooling present (fan, heat pipe — not passive slab)
- [ ] Confirm M.2 slot count and storage config
- [ ] Confirm external PSU wattage
- [ ] Confirm all display/port outputs
- [ ] Confirm warranty and AU return policy
- [ ] Confirm ROCm compatibility for llama.cpp / Ollama — check community reports
