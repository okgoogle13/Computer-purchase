# Unified Data-Ready Checklist — All Tracks

**Generated:** 2026-05-04
**Source:** Repo card audit (no web access — all values from existing .md files only)
**Purpose:** Master list of all UNKNOWN fields requiring manual web/retailer lookup before
scoring, gate clearance, or purchase decisions can proceed.

> 🔴 = Blocks a go/no-go gate or GOOD ENOUGH condition
> 🟡 = Required for accurate rubric scoring
> 🟢 = Informational / secondary

---

## TRACK 1 — NVIDIA Laptops (Path 1A)

### Existing Cards (4 NVIDIA + 4 RTX 5090 cards)

| Card | Field | Priority | Notes |
|---|---|---|---|
| All 8 NVIDIA cards | AU stock confirmed at named retailer + URL | 🔴 | GOOD ENOUGH gate-critical |
| All 8 NVIDIA cards | Price in AUD (confirmed, not estimated) | 🔴 | Budget gate |
| 30_asus-rog-strix-scar-18-rtx-5090 | CPU model | 🟡 | |
| 30_asus-rog-strix-scar-18-rtx-5090 | RAM installed + max + free slots | 🟡 | |
| 30_asus-rog-strix-scar-18-rtx-5090 | Charger wattage | 🟡 | |
| 30_asus-rog-strix-scar-18-rtx-5090 | Weight | 🟢 | |
| 30_asus-rog-strix-scar-18-rtx-5090 | Sustained TGP from review | 🟡 | |
| 31_lenovo-legion-9i-18-rtx-5090 | CPU model | 🟡 | |
| 31_lenovo-legion-9i-18-rtx-5090 | RAM installed + max + free slots | 🟡 | |
| 31_lenovo-legion-9i-18-rtx-5090 | Charger wattage | 🟡 | |
| 31_lenovo-legion-9i-18-rtx-5090 | Weight | 🟢 | |
| 31_lenovo-legion-9i-18-rtx-5090 | Sustained TGP from review | 🟡 | |
| 32_msi-raider-a18-hx-rtx-5090 | CPU model | 🟡 | |
| 32_msi-raider-a18-hx-rtx-5090 | RAM installed + max + free slots | 🟡 | |
| 32_msi-raider-a18-hx-rtx-5090 | Charger wattage | 🟡 | |
| 33_msi-titan-rtx-5090 | CPU model | 🟡 | |
| 33_msi-titan-rtx-5090 | RAM installed + max + free slots | 🟡 | |
| 33_msi-titan-rtx-5090 | Charger wattage | 🟡 | |
| 21–24 (RTX 4090 cards) | All key specs | 🟡 | Legacy cards; lower priority vs RTX 5090 tier |

---

## TRACK 1 — AMD Strix Halo Laptops (Path 1B)

### New Card Shells (created 2026-05-04 — all fields UNKNOWN)

| Card | Field | Priority | Notes |
|---|---|---|---|
| 34_asus-tuf-gaming-a16-strix-halo | SoC model (confirm Strix Halo — not standard Ryzen) | 🔴 | Gate: Path 1B eligibility |
| 34_asus-tuf-gaming-a16-strix-halo | Unified memory size in AU SKU (32 / 64 / 96 GB?) | 🔴 | Gate: ≥ 32 GB required |
| 34_asus-tuf-gaming-a16-strix-halo | AU stock + named retailer + URL | 🔴 | GOOD ENOUGH gate |
| 34_asus-tuf-gaming-a16-strix-halo | Price in AUD | 🔴 | Budget gate |
| 34_asus-tuf-gaming-a16-strix-halo | ROCm / llama.cpp compatibility | 🔴 | Disqualifying flag if severe gap |
| 34_asus-tuf-gaming-a16-strix-halo | Sustained TDP under load | 🟡 | Thermal scoring |
| 34_asus-tuf-gaming-a16-strix-halo | Storage + free M.2 slots | 🟡 | |
| 34_asus-tuf-gaming-a16-strix-halo | Weight + charger wattage | 🟢 | |
| 35_asus-rog-zephyrus-g16-strix-halo | SoC model (confirm Strix Halo) | 🔴 | Gate: Path 1B eligibility |
| 35_asus-rog-zephyrus-g16-strix-halo | Unified memory size in AU SKU | 🔴 | Gate: ≥ 32 GB required |
| 35_asus-rog-zephyrus-g16-strix-halo | AU stock + named retailer + URL | 🔴 | GOOD ENOUGH gate |
| 35_asus-rog-zephyrus-g16-strix-halo | Price in AUD | 🔴 | Budget gate |
| 35_asus-rog-zephyrus-g16-strix-halo | ROCm / llama.cpp compatibility | 🔴 | Disqualifying flag if severe gap |
| 35_asus-rog-zephyrus-g16-strix-halo | Sustained TDP under load | 🟡 | |
| 36_lenovo-amd-strix-halo-laptop | Exact model name + SKU carrying Strix Halo | 🔴 | Card shell uses placeholder name |
| 36_lenovo-amd-strix-halo-laptop | SoC model (confirm Strix Halo) | 🔴 | Gate: Path 1B eligibility |
| 36_lenovo-amd-strix-halo-laptop | Unified memory size in AU SKU | 🔴 | Gate: ≥ 32 GB required |
| 36_lenovo-amd-strix-halo-laptop | AU stock + named retailer + URL | 🔴 | GOOD ENOUGH gate |
| 36_lenovo-amd-strix-halo-laptop | Price in AUD | 🔴 | Budget gate |
| 36_lenovo-amd-strix-halo-laptop | Screen size (determines scoring bonus/penalty) | 🔴 | Bonus at 17–18"; penalty < 15" |
| 36_lenovo-amd-strix-halo-laptop | ROCm / llama.cpp compatibility | 🔴 | Disqualifying flag if severe gap |

---

## TRACK 2 — Pathway A (AU System Integrator Build)

| Field | Priority | Notes |
|---|---|---|
| CPU — model and generation | 🔴 | No build spec yet; all fields UNKNOWN |
| Motherboard — model, chipset, PCIe x16 slot count and lane allocation | 🔴 | Gate: must support target GPU config |
| RAM — capacity, type, speed | 🟡 | |
| PSU — model, wattage, efficiency, connector count | 🔴 | Gate: must support dual GPU (≥ 1000W recommended for dual RTX 3090) |
| Case — model, GPU clearance, fan layout | 🟡 | |
| Storage — SSD model + capacity | 🟢 | |
| GPU — RTX 3090 × 2: AU used/refurb market availability | 🔴 | Gate: must be explicitly confirmed, not assumed |
| GPU — RTX 3090 × 2: price per unit in AU market | 🔴 | Budget gate |
| NVLink support — platform compatibility for RTX 3090 pair | 🟡 | Determines pooled VRAM (48 GB) |
| Total build cost at target integrator (Scorptec / Mwave / Centre.com) | 🔴 | Budget gate |

---

## TRACK 2 — Pathway B (Refurbished Enterprise Workstation)

| Card | Field | Priority | Notes |
|---|---|---|---|
| 28_hp-z4-g4 | Manufacture date (confirm ≥ 2018) | 🔴 | Age gate |
| 28_hp-z4-g4 | PSU model + wattage | 🔴 | Card explicitly flags "VERIFY adequacy" |
| 28_hp-z4-g4 | PCIe x16 slot count + lane allocation | 🔴 | Gate: dual GPU support |
| 28_hp-z4-g4 | ECC RAM — confirm GPU driver compatibility | 🟡 | Risk flag |
| 29_dell-precision-7910 | Manufacture date — URGENT (likely < 2018) | 🔴 | Probable age disqualification |
| 29_dell-precision-7910 | Current AU used market price | 🟡 | For budget gate if age clears |
| 09_alienware-aurora-r12 | PSU model + wattage | 🔴 | Gate: adequate for RTX 3090 |
| 09_alienware-aurora-r12 | PCIe x16 slot count | 🔴 | OEM chassis likely single GPU only |
| 09_alienware-aurora-r12 | Manufacture date (confirm 2021) | 🟡 | Likely passes; confirm |
| 18_dell-precision-5820-bundle | Unbundled price (workstation only, no ThinkPad) | 🔴 | Budget gate — bundle at $3,558 inflated |
| 18_dell-precision-5820-bundle | PSU model + wattage | 🔴 | Gate |
| 18_dell-precision-5820-bundle | PCIe x16 slot count + lane allocation | 🔴 | Gate |
| 18_dell-precision-5820-bundle | ECC RAM — confirm GPU driver compatibility | 🟡 | Risk flag |
| 26_acer-orion-7000 | PSU model + wattage | 🟡 | Low priority — already weak candidate |

---

## TRACK 2 — Pathway C (Unified Memory Mini PC)

| Card | Field | Priority | Notes |
|---|---|---|---|
| 40_minisforum-ai-x1-pro | AU stock at named retailer + URL | 🔴 | Gate-critical |
| 40_minisforum-ai-x1-pro | Price in AUD | 🔴 | Budget gate |
| 40_minisforum-ai-x1-pro | Exact SoC model (confirm Strix Halo) | 🔴 | Gate eligibility |
| 40_minisforum-ai-x1-pro | Unified memory size in AU SKU (64 / 96 / 128 GB?) | 🔴 | Gate: ≥ 64 GB required |
| 40_minisforum-ai-x1-pro | Active cooling confirmed (not passive) | 🔴 | Disqualifying flag if passive |
| 40_minisforum-ai-x1-pro | ROCm / llama.cpp compatibility | 🔴 | Disqualifying flag if severe gap |
| 40_minisforum-ai-x1-pro | External PSU wattage | 🟡 | |
| 40_minisforum-ai-x1-pro | M.2 slot count + storage options | 🟢 | |
| 41_asus-nuc-strix-halo | Exact model name carrying Strix Halo SoC | 🔴 | Shell uses placeholder |
| 41_asus-nuc-strix-halo | AU stock at named retailer + URL | 🔴 | Gate-critical |
| 41_asus-nuc-strix-halo | Price in AUD | 🔴 | Budget gate |
| 41_asus-nuc-strix-halo | Unified memory size in AU SKU | 🔴 | Gate: ≥ 64 GB required |
| 41_asus-nuc-strix-halo | Active cooling confirmed | 🔴 | Disqualifying flag if passive |
| 41_asus-nuc-strix-halo | ROCm / llama.cpp compatibility | 🔴 | Disqualifying flag if severe gap |

---

## Summary — Count of Red-Priority UNKNOWN Fields

| Track / Pathway | 🔴 Red fields blocking gates |
|---|---|
| Track 1 — NVIDIA (Path 1A) | 8 (AU stock × 8 cards) + all key specs on new 5090 shells |
| Track 1 — AMD (Path 1B) | 21 across 3 new shells |
| Track 2 — Pathway A | 7 (entire build spec UNKNOWN) |
| Track 2 — Pathway B | 11 across 5 cards |
| Track 2 — Pathway C | 12 across 2 new shells |
| **TOTAL blocking** | **~59 red-priority fields** |

---

## Recommended Lookup Sequence

1. **Immediate (Track 1 priority):** AMD Strix Halo laptop AU availability — confirm ASUS TUF A16, Zephyrus G16, and any Lenovo Strix Halo are actually stocked in AU before investing further research time.
2. **Immediate (Track 2 Pathway C):** Minisforum AI X1 Pro AU availability + price — this is the highest-potential Pathway C candidate with 128 GB ceiling.
3. **Track 2 Pathway B triage:** Confirm Dell Precision 7910 manufacture date — likely disqualification will clean up the shortlist immediately.
4. **Track 2 Pathway A:** Fill build spec with a single credible SI config before doing GPU availability checks.
5. **Track 1 NVIDIA:** Confirm AU stock for RTX 5090 chassis — these are the priority purchase candidates under current strategy.
