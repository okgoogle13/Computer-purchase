# Track 2 — Pathway B Audit Report

**Generated:** 2026-05-04
**Auditor:** Antigravity agent (repo-only, no web access)
**Source cards:** `Desktop_Towers_Refurbished/*.md` (5 cards)

> All gate evaluations based solely on data present in existing card files.
> UNKNOWN = field not present or not confirmed in card. Manual web lookup required before gates can clear.

---

## Gate Definitions (from AGENTS.md)

| Gate | Requirement |
|---|---|
| G1 — Age | Chassis manufacture date ≥ 2018 |
| G2 — PCIe slots | PCIe slot count + lane allocation confirmed for target GPU config |
| G3 — PSU wattage | PSU confirmed sufficient for GPU(s), or upgrade confirmed possible + costed |
| G4 — GPU VRAM | GPU(s) ≥ 16 GB VRAM per card — pre-installed or confirmed available in AU used market |
| G5 — Budget | Total cost (unit + GPU additions) within AUD 0–4,000 |
| G6 — Thermal | No disqualifying thermal flag (inadequate airflow for dual-GPU sustained load) |
| G7 — ECC | No ECC-only memory constraint preventing standard GPU driver operation |

---

## Card-by-Card Gate Audit

---

### 1. HP Z4 G4 Workstation + RTX 3090 24 GB
**File:** `28_hp-z4-g4-rtx-3090-refurbished.md`

| Gate | Status | Evidence from card |
|---|---|---|
| G1 — Age ≥ 2018 | ⚠️ UNKNOWN | No manufacture date stated on card |
| G2 — PCIe slots | ⚠️ UNKNOWN | "Multiple M.2 and SATA slots" noted but PCIe x16 slot count not confirmed |
| G3 — PSU | ⚠️ NEEDS VERIFICATION | "HP Z4 G4 750W OEM PSU — VERIFY adequacy for RTX 3090 TDP" — card explicitly flags this |
| G4 — GPU VRAM | ✅ PARTIAL | RTX 3090 24 GB (added separately) — 24 GB confirms ≥ 16 GB; AU used market availability UNKNOWN |
| G5 — Budget | ✅ LIKELY | ~$2,800–$3,500 combined — within AUD 4,000 budget |
| G6 — Thermal | ⚠️ UNKNOWN | No thermal notes on card |
| G7 — ECC | ⚠️ RISK | Card notes "up to 128 GB ECC DDR4" — confirm standard GPU driver operation not blocked by ECC requirement |

**Gates cleared:** 1 partial (G4), 1 likely (G5)
**Gates blocking:** G1, G2, G3 (explicit flag), G6, G7
**Verdict:** ❌ NOT GATE-READY — 5 UNKNOWN / flagged gates. Priority: verify PSU adequacy, manufacture date, PCIe slot layout.

---

### 2. Dell Precision Tower 7910 + RTX 3090 24 GB
**File:** `29_dell-precision-tower-7910-rtx-3090.md`

| Gate | Status | Evidence from card |
|---|---|---|
| G1 — Age ≥ 2018 | ❌ LIKELY FAIL | Dell Precision 7910 = 2014–2016 generation (Xeon E5-2600 v3/v4). This platform predates 2018. **Age gate likely disqualified.** |
| G2 — PCIe slots | ⚠️ UNKNOWN | Dual-socket platform may have PCIe x16 slots — not confirmed on card |
| G3 — PSU | ✅ PARTIAL | "1300W Enterprise PSU (typically included in 7910)" — strong PSU headroom for dual GPU |
| G4 — GPU VRAM | ✅ PARTIAL | RTX 3090 24 GB — ≥ 16 GB confirmed; AU availability UNKNOWN |
| G5 — Budget | ⚠️ UNKNOWN | "Varies, used market" — no specific price on card |
| G6 — Thermal | ⚠️ UNKNOWN | No thermal notes |
| G7 — ECC | ⚠️ RISK | Enterprise dual-Xeon — ECC RAM standard; confirm GPU driver operation not impacted |

**Gates cleared:** 1 partial (G3, G4)
**Gates blocking:** G1 (LIKELY FAIL — 2014-era platform), G2, G5, G6, G7
**Verdict:** ❌ LIKELY DISQUALIFIED — G1 (age) probable fail due to 2014-era Xeon E5-2600 platform. **Flag for manual confirmation before any action.** If manufacture date confirmed < 2018, remove from Pathway B shortlist.

---

### 3. Alienware Aurora R12 + RTX 3090 (Refurbished)
**File:** `09_alienware-aurora-r12-rtx-3090-refurbished.md`

| Gate | Status | Evidence from card |
|---|---|---|
| G1 — Age ≥ 2018 | ✅ LIKELY PASS | Alienware Aurora R12 = 2021 (Intel 11th gen / Rocket Lake). Confirm exact manufacture date. |
| G2 — PCIe slots | ⚠️ UNKNOWN | No PCIe slot info on card; OEM gaming chassis — likely single x16 only |
| G3 — PSU | ⚠️ UNKNOWN | No PSU spec on card |
| G4 — GPU VRAM | ✅ LIKELY | GPU listed as "24 GB" — RTX 3090 confirmed in title; meets ≥ 16 GB |
| G5 — Budget | ⚠️ BORDERLINE | Price listed as $3,090 AUD — within budget, but GPU may be separate; confirm total |
| G6 — Thermal | ⚠️ RISK | Alienware Aurora R12 uses proprietary OEM chassis and PSU; known thermal constraints under sustained GPU load |
| G7 — ECC | ✅ LIKELY PASS | Consumer gaming chassis — non-ECC RAM standard |

**Gates cleared:** G1 (likely), G4 (likely), G7 (likely)
**Gates blocking:** G2 (PCIe layout for dual GPU — OEM gaming chassis strongly suspected single-GPU only), G3 (PSU unknown), G5 (confirm total cost), G6 (thermal flag)
**Verdict:** ⚠️ SINGLE GPU ONLY — OEM Alienware chassis is almost certainly not dual-GPU capable. If Pathway B requires dual GPU potential, this is likely a poor fit. Suitable as **single 24 GB GPU** candidate only. Needs PCIe + PSU + thermal manual verification.

---

### 4. Recompute Dell Precision 5820 Tower + ThinkPad T14s Bundle
**File:** `18_recompute-dell-precision-5820-tower-act-thinkpad-t14s-pairing.md`

| Gate | Status | Evidence from card |
|---|---|---|
| G1 — Age ≥ 2018 | ✅ LIKELY PASS | Dell Precision 5820 = 2018–2021 era (Xeon W-2100/2200 series). Confirm exact model year. |
| G2 — PCIe slots | ⚠️ UNKNOWN | No PCIe slot info on card |
| G3 — PSU | ⚠️ UNKNOWN | No PSU spec on card |
| G4 — GPU VRAM | ✅ PARTIAL | GPU listed as "24 GB" — confirm exact GPU model |
| G5 — Budget | ⚠️ BORDERLINE | Price listed as $3,558 AUD — at upper range; includes laptop bundle (ThinkPad T14s) which may not be needed |
| G6 — Thermal | ⚠️ UNKNOWN | Enterprise workstation chassis — generally better thermal design than OEM gaming; unconfirmed |
| G7 — ECC | ⚠️ RISK | Xeon W platform — ECC RAM expected; confirm GPU driver compatibility |

**Gates cleared:** G1 (likely), G4 (partial)
**Gates blocking:** G2, G3, G5 (borderline — bundled laptop inflates cost), G6, G7
**Verdict:** ⚠️ CONDITIONAL — G1 likely passes (2018+ platform). Bundle includes ThinkPad T14s which may inflate cost beyond useful range if workstation alone is the target. Need unbundled price, PCIe layout, PSU spec, and ECC confirmation.

---

### 5. Acer Predator Orion 7000 — RTX 4080 (Refurbished)
**File:** `26_acer-predator-orion-7000-rtx-4080-super.md`

| Gate | Status | Evidence from card |
|---|---|---|
| G1 — Age ≥ 2018 | ✅ PASS | Acer Predator Orion 7000 = 2022 (Intel i9-14900K confirmed on card). Well within 2018 cutoff. |
| G2 — PCIe slots | ⚠️ UNKNOWN | OEM gaming chassis — likely single x16 primary slot; dual GPU support unclear |
| G3 — PSU | ⚠️ UNKNOWN | No PSU spec on card; OEM Acer PSU may be limiting |
| G4 — GPU VRAM | ✅ PARTIAL | RTX 4080 16 GB (Ada Lovelace) confirmed — meets ≥ 16 GB floor |
| G5 — Budget | ❌ OVER BUDGET | Price listed as ~$3,699 AUD — already at budget ceiling before any GPU addition |
| G6 — Thermal | ⚠️ FLAG | Card notes: "Loud under sustained AI load." Active flag on card. |
| G7 — ECC | ✅ PASS | Consumer gaming chassis — non-ECC DDR5 (32 GB DDR5 confirmed on card) |

**Gates cleared:** G1 ✅, G4 ✅ (single GPU), G7 ✅
**Gates blocking:** G2 (dual GPU unclear), G3 (PSU unknown), G5 (budget tight — no headroom for GPU additions), G6 (thermal flag active)
**Verdict:** ❌ WEAK CANDIDATE FOR PATHWAY B — Single GPU already installed (16 GB, meets floor). But: budget headroom is minimal, dual GPU path not viable in OEM chassis, thermal flag raised. Best evaluated as a **single 16 GB GPU ready-to-run** option only, not a growth platform.

---

## Summary Table

| Card | G1 Age | G2 PCIe | G3 PSU | G4 VRAM | G5 Budget | G6 Thermal | G7 ECC | Verdict |
|---|---|---|---|---|---|---|---|---|
| HP Z4 G4 | UNKNOWN | UNKNOWN | ⚠️ FLAGGED | ✅ 24 GB | ✅ likely | UNKNOWN | ⚠️ risk | Not gate-ready |
| Dell 7910 | ❌ likely fail | UNKNOWN | ✅ 1300W | ✅ 24 GB | UNKNOWN | UNKNOWN | ⚠️ risk | Likely disqualified (age) |
| Alienware R12 | ✅ 2021 | ⚠️ OEM limit | UNKNOWN | ✅ 24 GB | ✅ $3,090 | ⚠️ flag | ✅ | Single GPU only |
| Dell 5820 Bundle | ✅ likely | UNKNOWN | UNKNOWN | ✅ 24 GB | ⚠️ $3,558 | UNKNOWN | ⚠️ risk | Conditional — needs unbundled price |
| Acer Orion 7000 | ✅ 2022 | ⚠️ OEM limit | UNKNOWN | ✅ 16 GB | ❌ $3,699 | ⚠️ flagged | ✅ | Weak — no headroom |

---

## Priority Manual Lookup Actions (Pathway B)

| Priority | Card | Field to Verify |
|---|---|---|
| 🔴 HIGH | Dell Precision 7910 | Manufacture year — confirm whether pre-2018 → DISQUALIFY |
| 🔴 HIGH | HP Z4 G4 | PSU model + wattage — card explicitly flags this as unverified |
| 🔴 HIGH | HP Z4 G4 | Manufacture date — confirm ≥ 2018 |
| 🟡 MED | All 5 cards | PCIe x16 slot count — confirm dual GPU capability (except Alienware R12 and Acer Orion which are OEM gaming, likely single-GPU only) |
| 🟡 MED | HP Z4 G4, Dell 5820 | ECC RAM — confirm GPU driver operation not blocked |
| 🟡 MED | Dell 5820 | Unbundled price (workstation only, without ThinkPad) |
| 🟢 LOW | Alienware R12 | PSU model + wattage |
| 🟢 LOW | Acer Orion 7000 | PSU model + wattage (informational — already weak candidate) |
