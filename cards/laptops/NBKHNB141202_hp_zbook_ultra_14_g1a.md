---
id: NBKHNB141202
category: laptop
track: 1B
pathway: 1B
item_name: HP ZBook Ultra 14 G1a (Ryzen AI Max PRO 390)
machine: HP ZBook Ultra 14 G1a
soc: AMD Ryzen AI Max PRO 390
unified_memory_gb: 32
ram_gb: 32
ssd_gb: 512
screen_inches: 14.0
price_aud: 3899.00
effective_best_price_aud: 3899.00
retailer: JW Computers
url: https://www.jw.com.au/product/hp-zb-ultra-14-g1a-14-ai-max-390-32g-512g-w11p
status: BUY_CANDIDATE
date_verified: 2026-06-06
Performance_Headroom: 3
Price_Value: 5
Future_Proof: 3
Portability: 8
Track2_Avoidance: 5
gpu: Integrated Graphics
vram: 0.0 GB
screen_size_in: 16.0
source_platform: MAJOR_RETAILER_AU
seller_class: MAJOR_RETAILER_AU
---

# Product Card: HP ZBook Ultra 14 G1a (Strix Halo)

## Evidence Summary
- **Verified SoC:** AMD Ryzen AI Max PRO 390 (Strix Halo). 12 Cores, 24 Threads, up to 5.0 GHz.
- **Integrated Graphics:** AMD Radeon Graphics (Strix Halo tier, likely 40CU).
- **Unified Memory:** 32GB LPDDR5x-8533 MT/s (Onboard).
- **Storage:** 512GB PCIe Gen4 SSD (Requires upgrade for CareerCopilot).
- **Display:** 14" WUXGA (1920x1200) IPS 400 nits.
- **Price:** $3,899.00 AUD at JW Computers (lowest confirmed AU, 2026-06-06). Also listed: Mwave ~$4,861, Landmark Computers, 7Stores.au.
- **Stock:** JW Computers — dispatch 1–2 business days (confirmed 2026-06-06).
- **Warranty:** 3Y NBD Onsite (Professional grade — confirmed AU stock).

## Gate Assessment (Track 1B)
- [x] **SoC is confirmed Strix Halo / Ryzen AI Max / Ryzen AI Max+.** (PASS: AI Max PRO 390)
- [x] **Unified memory is at least 16 GB.** (PASS: 32GB)
- [x] **Price is at most 5,000 AUD.** ($3,899.00 at JW Computers — PASS)
- [x] **No disqualifying sustained thermal or ROCm compatibility risk.** (PASS: ROCm 7.2 confirmed STABLE on Strix Halo gfx1151 via AMD Adrenalin 26.2.2, Linux kernel ≥6.18.4 or WSL. Thermal risk in 14" chassis remains a scoring caution but is not disqualifying.)

## Decision State
**BUY_CANDIDATE**
All Track 1B gates now pass. ROCm 7.2 confirmed stable on Strix Halo (gfx1151) as of AMD Adrenalin 26.2.2 — software ecosystem blocker resolved. Track2_Avoidance revised to 5 per AGENTS.md (32GB unified memory cap). Thermal caution in 14" chassis applies as a scoring modifier only, not a disqualifier. No viable Track 1A candidate remains under $5,000 cap after cross-check (Legion Pro 7i Gen 10 outlet now $5,999). **This is currently the only confirmed GOOD ENOUGH candidate.**

## Performance Profile (CareerCopilot)
- **MVP Workload:** Strong. 32GB unified memory allows for larger LLM context windows than typical 8GB/12GB consumer laptops.
- **Q4 Advanced Features:** Moderate to strong. 32GB unified memory helps, but runway is below 64GB/128GB tiers.
- **Portability:** Excellent (14" chassis, ~1.4kg).
- **Upgradability:** Memory is onboard (LPDDR5x). 32GB is fixed.

## Verification Checklist
- [x] AU Stock Confirmed — JW Computers (1–2 day dispatch), Mwave, Landmark Computers (2026-06-06)
- [x] Price Confirmed — $3,899 AUD (JW Computers, lowest confirmed AU)
- [x] Unified Memory Confirmed (32GB LPDDR5x)
- [x] SoC Confirmed (Strix Halo / Ryzen AI Max PRO 390)
- [x] Warranty/ACL: 3 Year Next Business Day Onsite (AU stock confirmed).
- [x] ROCm / Strix Halo: STABLE — ROCm 7.2 + AMD Adrenalin 26.2.2, Linux kernel ≥6.18.4. Firmware ≥2026 required; avoid 2025 linux-firmware regression. (verified 2026-06-06)
- [x] Thermal: CAUTION (scoring modifier, not disqualifying) — 14" chassis, 120W+ TDP; recommend balanced power profile in CareerCopilot workloads.
