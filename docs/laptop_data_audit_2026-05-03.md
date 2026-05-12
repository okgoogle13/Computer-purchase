# Laptop Data Audit — Sprint A
**File:** `Decision_System/laptop_data_audit_2026-05-03.md`
**Date:** 2026-05-03
**Scope:** `laptop_candidates.csv` ↔ `Laptops/*.md` cross-reference, field-level UNKNOWN flags, manual research checklist.
**Constraint:** Agent must not infer or guess missing values. UNKNOWN fields stay UNKNOWN until manually updated.

---

## Section 1 — CSV ↔ Card Cross-Reference

Budget status key: 🟢 Within sweet spot (≤ $3,500) · 🟡 Within cap, above sweet spot ($3,500–$4,000) · 🔴 Over cap (> $4,000) · ⬜ UNKNOWN (no price in repo)

| # | CSV `Machine` | CSV `Type` | Card file | Sync status | Budget_Status |
|---|---|---|---|---|---|
| 1 | `ASUS_ROG_Scar17_RTX4090_16GB` | Preferred | `22_asus-rog-strix-scar-17-rtx-4090.md` | ✅ Matched | 🔴 Over cap (~$5,099 old price) |
| 2 | `ASUS_ROG_Scar18_RTX4090_16GB` | Preferred | `23_asus-rog-strix-scar-18-rtx-4090.md` | ✅ Matched | 🔴 Over cap (~$6,899 old price) |
| 3 | `Lenovo_Legion_Pro7i_RTX4090_16GB` | Preferred | `21_lenovo-legion-pro-7i-rtx-4090.md` | ✅ Matched | 🟡/🔴 Split — low config ~$3,599 (🟡), high config ~$4,399 (🔴); needs current AU check |
| 4 | `MSI_Stealth16_RTX4090_16GB` | Borderline | `24_msi-stealth-16-ai-studio-rtx-4090.md` | ✅ Matched | 🔴 Over cap (~$6,599 old price) |
| 5 | `Dell_Alienware_m18_RTX4090_16GB` | OutOfScope | *(no card)* | ⛔ Out of scope — not a listed brand | — |
| 6 | `ASUS_ROG_Scar18_2025_RTX5090_24GB` | Target-UNVERIFIED | `30_asus-rog-strix-scar-18-rtx-5090-2025.md` | ⚠️ Shell only — all scores zeroed pending manual data | ⬜ UNKNOWN |
| 7 | `Lenovo_Legion_Pro9i_RTX5090_24GB` | Target-UNVERIFIED | `31_lenovo-legion-9i-18-rtx-5090.md` | ⚠️ Shell only — all scores zeroed pending manual data | ⬜ UNKNOWN |
| 8 | `MSI_Raider_A18_HX_RTX5090_24GB` | Target-UNVERIFIED | `32_msi-raider-a18-hx-rtx-5090.md` | ⚠️ Shell only — all scores zeroed pending manual data | ⬜ UNKNOWN |
| 9 | `MSI_Titan_GT77_RTX5090_24GB` | Target-UNVERIFIED | `33_msi-titan-rtx-5090.md` | ⚠️ Shell only — reclassified; Titan IS in scope per AGENTS.md | ⬜ UNKNOWN |

---

## Section 2 — Field-Level Audit: Existing 4090 Cards

### Card 21 — Lenovo Legion Pro 7i (RTX 4090, 16 GB)
**CSV row:** `Lenovo_Legion_Pro7i_RTX4090_16GB` | **File:** `21_lenovo-legion-pro-7i-rtx-4090.md`
**Track 1 status:** Fallback candidate (16 GB VRAM, not a locked chassis — Legion *9i* 18 is the locked family)

| Field | Value in card | Status |
|---|---|---|
| GPU / VRAM | RTX 4090 Laptop GPU, 16 GB GDDR6 | ✅ |
| CPU | Intel Core i9-14900HX | ✅ |
| RAM installed | 32 GB DDR5 | ✅ |
| RAM max supported | 64 GB (upgradeable) | ✅ spec stated, slot count UNKNOWN |
| Free RAM slots | Not listed | ⚠️ UNKNOWN |
| Storage installed | 2 TB SSD | ✅ |
| Free M.2 slots | Not listed | ⚠️ UNKNOWN |
| Display size | 16-inch | ✅ |
| Panel type | Not stated (2K 240 Hz only) | ⚠️ UNKNOWN (IPS / OLED / MiniLED?) |
| Weight | Not listed | ⚠️ UNKNOWN |
| Charger wattage | Not listed | ⚠️ UNKNOWN |
| Price (AUD) | ~$3,599–$4,399 | ⚠️ Approximate; needs current AU check |
| AU retailer (named) | "Mike PC / Lenovo AU / Amazon AU" | ⚠️ Vague — needs specific URL + stock confirmation |
| Warranty | Not listed | ⚠️ UNKNOWN |
| Sustained TGP | Not listed | ⚠️ UNKNOWN |
| Thermal notes | Not listed | ⚠️ UNKNOWN |

**CSV scores (from updated laptop_candidates.csv):**
`VRAM=5, GPU_Compute=8, TGP=9, Thermal=7, RAM=10, Storage=8, AU_Retailer=9, Price=8, Display=5, Portability=7`
**Score source trustworthiness:** ⚠️ TGP=9 and AU_Retailer=9 are asserted without card evidence — flag for review when AU data arrives.

---

### Card 22 — ASUS ROG Strix Scar 17 (RTX 4090, 16 GB)
**CSV row:** `ASUS_ROG_Scar17_RTX4090_16GB` | **File:** `22_asus-rog-strix-scar-17-rtx-4090.md`
**Track 1 status:** Fallback candidate (16 GB VRAM; Scar 17 ≠ Scar 18 locked chassis)

| Field | Value in card | Status |
|---|---|---|
| GPU / VRAM | RTX 4090 Laptop GPU, 16 GB GDDR6 | ✅ |
| CPU | AMD Ryzen 9 7945HX | ✅ |
| RAM installed | 32 GB DDR5 | ✅ |
| RAM max supported | 64 GB (upgradeable) | ✅ spec stated, slot count UNKNOWN |
| Free RAM slots | Not listed | ⚠️ UNKNOWN |
| Storage installed | 1 TB NVMe | ✅ |
| Free M.2 slots | Not listed | ⚠️ UNKNOWN |
| Display size | 17.3-inch WQHD 240 Hz | ✅ |
| Panel type | Not stated | ⚠️ UNKNOWN |
| Weight | Not listed | ⚠️ UNKNOWN |
| Charger wattage | Not listed | ⚠️ UNKNOWN |
| Price (AUD) | ~$5,099 | ⚠️ Approximate; needs current AU check |
| AU retailer (named) | "Umart / Australian IT retailers" | ⚠️ Vague — needs specific URL + stock confirmation |
| Warranty | Not listed | ⚠️ UNKNOWN |
| Sustained TGP | Not listed | ⚠️ UNKNOWN |
| Thermal notes | "Strong sustained thermal performance" | ⚠️ Qualitative only — no wattage or source cited |

**CSV scores:** `VRAM=5, GPU_Compute=8, TGP=9, Thermal=9, RAM=10, Storage=7, AU_Retailer=8, Price=9, Display=8, Portability=6`
**Score source trustworthiness:** ⚠️ TGP=9 and Thermal=9 are asserted in the card without a numeric source — flag.

---

### Card 23 — ASUS ROG Strix Scar 18 (RTX 4090, 16 GB)
**CSV row:** `ASUS_ROG_Scar18_RTX4090_16GB` | **File:** `23_asus-rog-strix-scar-18-rtx-4090.md`
**Track 1 status:** ✅ Locked chassis family (Scar 18) — RTX 4090 fallback version

| Field | Value in card | Status |
|---|---|---|
| GPU / VRAM | RTX 4090 Laptop GPU, 16 GB GDDR6 | ✅ |
| CPU | Intel Core i9-14900HX | ✅ |
| RAM installed | 64 GB DDR5 | ✅ |
| RAM max supported | Not stated explicitly | ⚠️ Implied ≥ 64 GB; max and slot count UNKNOWN |
| Free RAM slots | Not listed | ⚠️ UNKNOWN |
| Storage installed | 2 TB (2× 1 TB NVMe) | ✅ |
| Free M.2 slots | 2 drives installed — free slots UNKNOWN | ⚠️ UNKNOWN |
| Display size | 18-inch QHD | ✅ |
| Panel type | Not stated | ⚠️ UNKNOWN |
| Weight | ~3.1 kg | ✅ |
| Charger wattage | Not listed | ⚠️ UNKNOWN |
| Price (AUD) | ~$6,899 | ⚠️ Approximate; needs current AU check |
| AU retailer (named) | "MSY / Umart-linked AU retail" | ⚠️ Vague — needs specific URL + stock confirmation |
| Warranty | Not listed | ⚠️ UNKNOWN |
| Sustained TGP | Not listed | ⚠️ UNKNOWN |
| Thermal notes | Not listed | ⚠️ UNKNOWN |

**CSV scores:** `VRAM=5, GPU_Compute=8, TGP=9, Thermal=9, RAM=10, Storage=10, AU_Retailer=7, Price=4, Display=10, Portability=3`
**Score source trustworthiness:** ⚠️ TGP=9 and Thermal=9 have no card evidence. Price=4 reflects the high ~$6,899 price — plausible but needs current AU confirmation.

---

### Card 24 — MSI Stealth 16 AI Studio (RTX 4090, 16 GB)
**CSV row:** `MSI_Stealth16_RTX4090_16GB` | **File:** `24_msi-stealth-16-ai-studio-rtx-4090.md`
**Track 1 status:** ✅ In scope per AGENTS.md (MSI Stealth 16/17/18 is a listed family). Marked Borderline due to 16 GB VRAM and thermal concerns. Budget status: 🔴 Over cap at ~$6,599 old price — needs current AU check.

| Field | Value in card | Status |
|---|---|---|
| GPU / VRAM | RTX 4090 Laptop GPU, 16 GB GDDR6 | ✅ |
| CPU | Intel Core Ultra 9 185H | ✅ |
| RAM installed | 32 GB DDR5 | ✅ |
| RAM max supported | "Soldered; verify upgrade path" | 🔴 UNVERIFIED — soldered RAM is a hard ceiling risk |
| Free RAM slots | Not listed | ⚠️ UNKNOWN |
| Storage installed | 2 TB SSD | ✅ |
| Free M.2 slots | Not listed | ⚠️ UNKNOWN |
| Display size | 16-inch creator-class | ✅ |
| Panel type | Not stated; resolution UNKNOWN | ⚠️ UNKNOWN |
| Weight | Not listed | ⚠️ UNKNOWN |
| Charger wattage | Not listed | ⚠️ UNKNOWN |
| Price (AUD) | ~$6,599 | ⚠️ Approximate; needs current AU check |
| AU retailer (named) | Umart | ✅ Named, but stock/URL not confirmed |
| Warranty | Not listed | ⚠️ UNKNOWN |
| Sustained TGP | Not listed | ⚠️ UNKNOWN |
| Thermal notes | "Thermal risk under sustained inference" | ⚠️ Qualitative flag only — no wattage cited |

**CSV scores:** `VRAM=5, GPU_Compute=6, TGP=5, Thermal=5, RAM=3, Storage=7, AU_Retailer=6, Price=4, Display=5, Portability=8`
**Score source trustworthiness:** ⚠️ RAM=3 correctly penalises soldered RAM, but upgrade path is marked UNVERIFIED in the card. Thermal=5 and TGP=5 have no numeric source.

---

## Section 3 — RTX 5090 Shell Cards (Track 1 Primary Targets)

All four are blank shells. All scores are zeroed. No field can be filled by the agent.

| Chassis | Card file | Fields populated | Fields UNKNOWN |
|---|---|---|---|
| ASUS ROG Strix Scar 18 (5090) | `30_asus-rog-strix-scar-18-rtx-5090-2025.md` | GPU class, VRAM class, chassis ID | All spec/price/retailer/thermal fields |
| Lenovo Legion 9i 18 (5090) | `31_lenovo-legion-9i-18-rtx-5090.md` | GPU class, VRAM class, chassis ID | All spec/price/retailer/thermal fields |
| MSI Raider A18 HX (5090) | `32_msi-raider-a18-hx-rtx-5090.md` | GPU class, VRAM class, chassis ID | All spec/price/retailer/thermal fields |
| MSI Titan (5090) | `33_msi-titan-rtx-5090.md` | GPU class, VRAM class, chassis family | Model variant UNKNOWN; all spec/price/retailer/thermal fields UNKNOWN |

---

## Section 4 — Manual Web Research Checklist

Collect these fields for each of the 4 RTX 5090 target chassis from AU retailer pages.
Return the data here and the agent will fill the card shells and update CSV scores.

**Priority order:** AU_Retailer_Confidence → Sustained_TGP_Rating → VRAM_Adequacy (already known) → rest.
AU_Retailer_Confidence is the single hardest gate for the GOOD ENOUGH stop condition.

| Field to collect | Scar 18 RTX 5090 | Legion 9i 18 RTX 5090 | Raider A18 HX RTX 5090 | MSI Titan RTX 5090 |
|---|---|---|---|---|
| AU retailer name | ☐ | ☐ | ☐ | ☐ |
| AU retailer URL (direct product page) | ☐ | ☐ | ☐ | ☐ |
| In stock now? (Y/N) | ☐ | ☐ | ☐ | ☐ |
| Price (AUD, inc. GST) | ☐ | ☐ | ☐ | ☐ |
| Exact model name / SKU | — | — | — | ☐ (confirm Titan variant) |
| GPU confirmed (RTX 5090 / GDDR7 / 24 GB) | ☐ | ☐ | ☐ | ☐ |
| CPU model | ☐ | ☐ | ☐ | ☐ |
| RAM installed (GB) | ☐ | ☐ | ☐ | ☐ |
| RAM max supported (GB) | ☐ | ☐ | ☐ | ☐ |
| Free RAM slots (count) | ☐ | ☐ | ☐ | ☐ |
| SSD installed (TB) | ☐ | ☐ | ☐ | ☐ |
| Free M.2 slots (count) | ☐ | ☐ | ☐ | ☐ |
| Charger wattage (W) | ☐ | ☐ | ☐ | ☐ |
| Weight (kg) | ☐ | ☐ | ☐ | ☐ |
| Warranty — term (e.g. 2 yr) | ☐ | ☐ | ☐ | ☐ |
| Warranty — type (onsite / carry-in / depot) | ☐ | ☐ | ☐ | ☐ |
| Sustained TGP (W, from spec sheet or review) | ☐ | ☐ | ☐ | ☐ |
| Thermal flag (runs hot / throttles / good) | ☐ | ☐ | ☐ | ☐ |
| Panel type (IPS / OLED / MiniLED) | ☐ | ☐ | ☐ | ☐ |

**Suggested AU retailers to check:**
- ASUS Scar 18: rog.asus.com/au, JB Hi-Fi, Scorptec, Centre Com
- Legion 9i 18: lenovo.com/au, JB Hi-Fi, Centre Com, Scorptec
- Raider A18 HX: au.msi.com, JB Hi-Fi, PLE, Centre Com, Scorptec
- MSI Titan: au.msi.com, JB Hi-Fi, PLE, Centre Com, Scorptec (confirm model variant first)

---

## Section 5 — GOOD ENOUGH Gate Reminder

A candidate triggers the stop condition when ALL of the following are confirmed:

| Criterion | Minimum | Score threshold in rubric |
|---|---|---|
| AU stock from named credible retailer | Confirmed in stock | `AU_Retailer_Confidence ≥ 8` |
| VRAM | 24 GB (RTX 5090) preferred; 16 GB (RTX 4090) fallback | `VRAM_Adequacy ≥ 5` |
| RAM | 32–64 GB installed or clearly upgradable | `RAM_Ceiling ≥ 5` |
| Storage | 2 TB installed or clearly upgradable | `Storage_Expandability ≥ 5` |
| Sustained thermal | No "throttles badly" signal | `Sustained_TGP_Rating ≥ 6` |
| Composite score | ≥ 72.0 / 100 after whitened rubric | `rubric_weighting_engine.py --profile laptop` |

**The engine will not produce a trustworthy score until AU_Retailer_Confidence is filled with real data for at least one candidate.**

---

## Section 6 — Status Summary

| Task | Owner | Status |
|---|---|---|
| CSV ↔ card cross-reference table | Agent | ✅ Done (this doc) |
| Blank card shells for 4 RTX 5090 targets | Agent | ✅ Done (files 30, 31, 32, 33) |
| MSI Titan reclassified to Target-UNVERIFIED in CSV | Agent | ✅ Done |
| Budget_Status column added to audit table | Agent | ✅ Done |
| CSV rows zeroed for unverified 5090 targets | Agent | ✅ Done |
| Out-of-scope rows labelled in CSV | Agent | ✅ Done |
| Manual web research for 5090 chassis | **You** | ☐ Pending |
| Fill card shells with collected data | Agent (after you collect data) | ☐ Blocked on manual research |
| Update CSV scores from filled cards | Agent (after you collect data) | ☐ Blocked on manual research |
| Run `rubric_weighting_engine.py --profile laptop` | Agent | ☐ Blocked on score data |
| Check GOOD ENOUGH threshold (72.0) | Agent | ☐ Blocked on score data |
