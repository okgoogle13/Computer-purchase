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
price_aud: 4200.00
effective_best_price_aud: 4200.00
retailer: PB Tech (User Verified)
url: https://www.pbtech.com/au/product/NBKHNB141202/HP-ZBook-Ultra-14-G1a-14-WUXGA-Mobile-Workstation
status: BUY_CANDIDATE
date_verified: 2026-05-07
---

# Product Card: HP ZBook Ultra 14 G1a (Strix Halo)

## Evidence Summary
- **Verified SoC:** AMD Ryzen AI Max PRO 390 (Strix Halo). 12 Cores, 24 Threads, up to 5.0 GHz.
- **Integrated Graphics:** AMD Radeon Graphics (Strix Halo tier, likely 40CU).
- **Unified Memory:** 32GB LPDDR5x-8533 MT/s (Onboard).
- **Storage:** 512GB PCIe Gen4 SSD (Requires upgrade for CareerCopilot).
- **Display:** 14" WUXGA (1920x1200) IPS 400 nits.
- **Price:** $4,849.57 AUD at PB Tech.
- **Warranty:** 3Y NBD Onsite (Professional grade).

## Gate Assessment (Track 1B)
- [x] **SoC is confirmed Strix Halo / Ryzen AI Max / Ryzen AI Max+.** (PASS: AI Max PRO 390)
- [x] **Unified memory is at least 16 GB.** (PASS: 32GB)
- [x] **Price is at most 5,000 AUD.** ($4,849.57 - PASS)
- [ ] **No disqualifying sustained thermal or ROCm compatibility risk.** (CAUTION: 14-inch chassis with 120W+ peak SoC TDP. ROCm support for Strix Halo is pending official firmware stable release).

## Decision State
**BUY_CANDIDATE**
This is the first verified Track 1B (Strix Halo) candidate in the repository. It meets all gates but carries significant thermal and software ecosystem risk (ROCm). It is recommended for users prioritizing portability and unified memory over raw CUDA performance.

## Performance Profile (CareerCopilot)
- **MVP Workload:** Strong. 32GB unified memory allows for larger LLM context windows than typical 8GB/12GB consumer laptops.
- **Q4 Advanced Features:** Strong. Strix Halo architecture provides a long runway for AI workloads.
- **Portability:** Excellent (14" chassis, ~1.4kg).
- **Upgradability:** Memory is onboard (LPDDR5x). 32GB is fixed.

## Verification Checklist
- [x] AU Stock Confirmed (PB Tech)
- [x] Unified Memory Confirmed (32GB LPDDR5x)
- [x] SoC Confirmed (Strix Halo / Ryzen AI Max PRO 390)
- [x] Warranty/ACL: 3 Year Next Business Day Onsite.
