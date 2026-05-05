# AGENTS.md — Two-Track Hardware Decision System

**Role:** Hardware-research and organisation helper inside the Antigravity IDE.
Keep decisions simple. Do NOT design the perfect system.
Browser access and web searches are permitted for verification and data gathering.

---

## SCOPE

- **Track 1:** Active laptop purchase. One decision. GOOD ENOUGH → buy.
- **Track 2:** Active workstation/desktop research. Three pathways. Likely medium-term outcome — runs in parallel with Track 1. Do not delay Track 1 for Track 2 unless a unicorn deal is immediately available.

---

## GLOBAL CONSTRAINTS

- **Browser access permitted.** Use the **Vercel Agent Browser (`agent-browser`)** CLI as the default for web research to ensure token utilization efficiency (via compact DOM snapshots). Use headless browser instances for all scraping and verification tasks to minimize overhead.
- **Work with:** existing markdown product cards, CSVs, policy/spec docs, scripts, templates in this repo, and external web sources.
- **Unknown values:** Use `agent-browser` to search for real-world specs or prices when they are unknown. Update fields dynamically.
- **Responsibilities:**
  - Audit and sync product cards vs CSVs.
  - Create and normalise product card shells.
  - Generate and refine prompt files.
  - Rebuild the mega-bundle.
  - Apply documented patches to spec/policy docs.
  - Draft decision logs and checklists.
  - Fetch new data from the internet to complete missing details.

---

## TRACK 1 — CHASSIS SCOPE AND BUDGET

Track 1 has **two hardware paths**: NVIDIA discrete GPU laptops and AMD unified-memory laptops.
Both paths are active simultaneously.

> **Principle:** The smaller the screen size, the more critical a Track 2 solution becomes.
> A 13" device at a strong price is a valid Track 1 candidate, but it explicitly increases
> urgency to resolve Track 2.

---

### Path 1A — NVIDIA Discrete GPU Laptops

#### Screen Size
- **Floor:** 13" minimum.
- **Primary target:** 17–18" (scoring bonus applies — see Scoring section).
- **Intermediate sizes (14–16"):** In scope; evaluated on VRAM, build quality, and resale value.

#### VRAM
- **Minimum:** 8 GB VRAM.
- **Preferred:** 12 GB or higher (16 GB - 24 GB optimal for larger LLMs).
- A 12 GB+ card at 17–18" = standard eligible candidate.
- An 8 GB card = requires significant offsetting strengths (build quality, price, resale) to remain competitive for LLM workloads.

#### Brands and Families in Scope

**LENOVO**
- Legion 9i
- Legion Pro 9i
- Legion Pro 7i (current high-end variants meeting VRAM and budget rules)

**ASUS**
- ROG Strix Scar 17
- ROG Strix Scar 18
- Any ROG model at 13"+ meeting the 8 GB VRAM floor

**MSI**
Any current 13"+ high-end RTX gaming/workstation model meeting VRAM and price constraints, including:
- MSI Raider 17/18
- MSI Titan 17/18
- MSI Stealth 16/17/18
- MSI Vector 16/17/18
- Other MSI 13"+ models with ≥ 8 GB VRAM


#### AMD Discrete GPU Laptops
AMD discrete GPU laptops evaluate under same rules as NVIDIA:
- HP OMEN Max (Ryzen AI 9 HX 375 + RTX 5070/5090)
- Tag as: architecture:discrete_gpu_amd, track_eligibility:track_1_nvidia_path
- Move cards from Strix_Halo_AMD/ to Gaming_Laptops_AMD_Discrete/
- Apply ≥8 GB VRAM floor, 16"+ screen size

#### Exclusions (Path 1A)
- Any laptop with less than 13" screen size.
- Any laptop with less than 8 GB discrete VRAM.
- Any brand/model family outside the three listed above, unless explicitly expanded.

#### Lenovo Legion Pro 7i vs 9i / Pro 9i Value Rule
- At the same price or within < 300 AUD difference: **prefer Legion 9i / Pro 9i over Pro 7i.**
- **Prefer Pro 7i** if it is ≥ 300–500 AUD cheaper than a comparable 9i/Pro 9i, while still meeting
  VRAM requirements, decent thermals, and upgradeability targets (32–64 GB RAM, ≥ 2 TB SSD).
- Pro 7i = "discount premium" tier, not equal to 9i/Pro 9i at the same price.

---

### Path 1B — AMD Strix Halo Unified Memory Laptops

#### Screen Size
- **No minimum screen size.** 13-14" devices are valid Track 1 candidates BUT trigger immediate Track 2 urgency (portable device requires desktop companion for extended work).
- 17–18" scoring bonus applies equally to this path.

#### Unified Memory
- **Minimum:** 16 GB (≈ equivalent to 8 GB discrete VRAM in GPU-accessible terms, given ~60–75%
  allocation to GPU workloads).
- **Preferred:** 64 GB.
- **Optimal:** 96–128 GB.

#### SoC Requirement
- Must use AMD Strix Halo (Ryzen AI Max / Ryzen AI Max+) or architecturally equivalent
  unified-memory SoC.
- Standard Ryzen with discrete dGPU does NOT qualify for this path.

#### Brands and Families in Scope
AMD Strix Halo laptops (any brand):
- ASUS TUF Gaming A14 (2026) FA401EA — 32 GB unified, 14"
- ASUS ProArt PX13 (Strix Halo variant) — 128 GB unified, 13.3"
- ASUS ROG Flow Z13 GZ302EA — check unified memory config, 13.4"
- Lenovo Legion 7a Gen 11 — if AU stock confirmed (not yet available)

> **ProArt PX13 Note:** ProArt PX13 retail (~$6,000 AUD) exceeds budget. ONLY pursue if refurbished/open-box/sale pricing ≤$4,500 AUD. Check: Officeworks, Harvey Norman, JB Hi-Fi, ASUS AU Outlet.

#### Exclusions (Path 1B)
- ASUS TUF A16: NO Strix Halo variant exists (discrete GPU only)
- ASUS ROG Zephyrus G16: NO Strix Halo variant exists (discrete GPU only)
- HP OMEN Max: Uses Strix Point (discrete GPU), NOT Strix Halo
- Any AMD device with < 16 GB unified memory.
- Any AMD device using a non-unified architecture (discrete dGPU with standard Ryzen iGPU).
- Apple Silicon (separate category, currently deferred).

---

### Track 1 — Price Band

- **Total budget range (AUD):** 0–4,500
- **Preferred sweet spot (AUD):** 2,500–4,000
- Only consider 4,000–4,500 AUD if: GPU/unified memory is top-tier, build quality and thermals are
  clearly superior, and there is a strong resale story.

### Track 1 — Scoring Bonuses and Flags

- **+Bonus:** Screen size 17–18" (applies to both Path 1A and 1B).
- **+Bonus:** Top-tier memory for path — 24 GB discrete (1A) or 96–128 GB unified (1B).
- **−Competitive penalty:** Screen size < 15" with no offsetting Track 2 plan resolved.
- **⚠ Flag:** Thermal concerns (sustained throttling under sustained GPU load).
- **⚠ Flag (Path 1B only):** Known ROCm software compatibility gaps for target workloads.

---

## TRACK 1 — AGENT RESPONSIBILITIES (REPO-ONLY)

- Audit `laptop_candidates.csv` against `04_Laptops_Mainline/*.md`:
  - Map every CSV row to a card file (or flag "NO CARD EXISTS").
  - Map every card file to a CSV row (or flag "NOT IN CSV").
  - Flag UNKNOWN / placeholder fields.
- For missing candidates within allowed scope: create BLANK product card shells using
  `template_product_card_output.md` with all spec fields set to UNKNOWN.
- Produce a "data-ready checklist" — a markdown table of all fields requiring web lookup, and use the browser agent to fill them.
- Actively attempt to fill UNKNOWN fields using the internet.

---

## GOOD ENOUGH STOP CONDITION (Track 1)

Mark a candidate as **"GOOD ENOUGH — STOP SEARCHING"** when ALL of the following are confirmed:

**Path 1A (NVIDIA):**
- In stock in AU from a credible retailer.
- ≥ 8 GB VRAM (12 GB+ preferred; RTX 4080/4090/5080/5090 optimal).
- Supports at least 32–64 GB RAM (installed or clearly upgradable).
- At least 2 TB SSD (installed or clearly upgradable).
- Price within the 0–4,000 AUD budget.
- No disqualifying thermal flag.

**Path 1B (AMD Strix Halo):**
- In stock in AU from a credible retailer.
- Confirmed Strix Halo SoC.
- ≥ 16 GB unified memory (32 GB+ preferred).
- Price within the 0–4,000 AUD budget.
- No disqualifying thermal flag.
- No disqualifying ROCm software compatibility gap for target workloads.

Do NOT expand scope beyond the listed families/SoC requirements unless explicitly instructed.

---

---

## TRACK 1.5 — REFURBISHED GAMING DESKTOP (SINGLE GPU)

**Definition:** Refurbished or open-box gaming desktops (OEM chassis) with single high-VRAM GPU. Evaluated as laptop alternatives when price/performance ratio is compelling.

**Scope:** Pre-built gaming towers from major OEMs. NOT custom builds (see Track 2 Pathway A).

**Brands in scope:**
- Alienware Aurora (R11, R12, R13, R14, R15, R16 series)
- Acer Predator Orion
- HP OMEN 45L/40L/30L
- ASUS ROG Strix GA15/GA35
- Lenovo Legion Tower (5i/7i series)

**GPU Requirements:**
- Minimum 8 GB VRAM (same as Track 1 NVIDIA path)
- Target: RTX 3090 (24 GB), RTX 4080/4090, or equivalent

**Age Limit:** Maximum 6 years old (≥ 2020 manufacture date)

**Price Threshold (CRITICAL):**
Must beat equivalent Track 1 laptop on price/performance:
- [ ] Desktop ≤ 85% cost of comparable laptop (accounting for loss of portability)
- [ ] OR desktop offers ≥ 50% more VRAM at same price point

Example: Alienware R12 with RTX 3090 (24 GB) @ $2,500 AUD beats TUF A14 (32 GB unified ≈ 16 GB GPU-available) @ $3,499 AUD.

**Go/No-Go Gates:**
- [ ] Chassis ≥ 2020 (confirm manufacture date or CPU generation)
- [ ] GPU confirmed ≥ 8 GB VRAM
- [ ] PSU wattage confirmed sufficient for installed GPU (or upgradable)
- [ ] Price threshold test passed (see above)
- [ ] AU stock/listing confirmed at credible seller
- [ ] Warranty ≥ 3 months (refurb) or ACL coverage (retailer sold)
- [ ] No disqualifying proprietary parts flag (Dell/Alienware: check PSU/mobo upgradeability)

**Candidate Prioritization:**
1. RTX 3090 chassis (best VRAM/$)
2. RTX 4090 chassis (if steep discount)
3. Multi-GPU capable (even if sold with single GPU — future Track 2 Pathway B conversion)

**Agent Responsibilities:**
- Maintain cards in `Desktop_Gaming_Refurbished/` folder
- For each card: confirm age, GPU VRAM, PSU spec, price/performance vs Track 1
- Use web searches to resolve UNKNOWN fields for: exact manufacture date, PSU wattage, warranty terms
- You may add new cards from web searches if they meet the criteria

**Exclusions:**
- Custom/SI builds (those go to Track 2 Pathway A)
- Desktops with <8 GB VRAM
- Pre-2020 platforms (thermal/efficiency penalty too high)

## TRACK 2 — WORKSTATION (ACTIVE — THREE PATHWAYS)

Track 2 is **active now** and runs in parallel with Track 1.
It is likely a **medium-term** outcome.

> **Do not delay Track 1 for Track 2.** Unless a Pathway A, B, or C candidate with immediate
> AU availability and strong pricing is identified, Track 1 remains the priority purchase.
> Track 2 resolves on its own timeline.

---

### Pathway A — AU System Integrator Custom/Configurable Build

**Definition:** A system ordered from an AU-based system integrator in a custom or
"ready-to-run" configuration. Examples: Scorptec, Mwave, Centre.com. This is NOT a
DIY self-sourced parts build.

**Go/No-Go Gates (ALL must pass before any action is taken):**
- [ ] Confirmed build spec exists in repo at `01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md`
      (CPU, motherboard, RAM, PSU, GPU, case — all named, no UNKNOWN fields).
- [ ] Target GPU(s) availability in AU market confirmed (flag UNKNOWN until manually verified).
- [ ] Build spec confirmed to support target GPU(s): PCIe slots, lane allocation, PSU wattage,
      physical clearance.
- [ ] Total cost (build + GPUs) within AUD budget.

**CPU Platform (LOCKED):**
AMD Threadripper PRO 5000WX (WRX80 chipset)
- 128 PCIe Gen 4 lanes (supports RTX 3090 × 2 + NVMe without bottleneck)
- Better AU availability than Intel Xeon W-3400
- Compatible motherboards: ASUS Pro WS WRX80E-SAGE, ASRock WRX80 Creator

**GPU Target:**
RTX 3090 × 2 (24 GB VRAM each = 48 GB total)
- AU used market estimate: $1,500-1,800 AUD per card (Gumtree, eBay AU)
- Flag as UNKNOWN until manual verification at time of build decision

**Next Steps:**
Create `track2_pathway_a_build_spec.md` with confirmed components:
- CPU: Threadripper PRO 5955WX or 5975WX
- Motherboard: (specific model TBD)
- RAM: 128 GB DDR4 ECC (minimum)
- PSU: 1600W+ 80+ Platinum (dual GPU headroom)
- Case: (TBD — must fit dual 3-slot GPUs)

**Agent Responsibilities:**
- Maintain confirmed build spec at `01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md`.
- Use the browser agent to look up UNKNOWN fields (prices, stock) from integrator websites.
- You may browse integrator websites to confirm specs and prices.

---

### Pathway B — Refurbished Enterprise Workstation

**Definition:** A pre-owned enterprise-class tower or rack workstation (e.g., Dell Precision,
HP Z-series, Lenovo ThinkStation) that arrives with 1× or 2× compatible GPU already installed,
or has confirmed empty PCIe slot(s) and PSU headroom to accept target GPU(s).

**Age Limit:** Maximum 8 years old (manufactured ≥ 2018).

**Go/No-Go Gates (ALL must pass before any action is taken):**
- [ ] Chassis manufacture date confirmed ≥ 2018 (flag UNKNOWN if not stated on card).
- [ ] PCIe slot count and lane allocation confirmed for target GPU configuration.
- [ ] PSU wattage confirmed sufficient for GPU(s), or PSU upgrade confirmed possible and costed.
- [ ] GPU(s) confirmed ≥ 8 GB VRAM per card — either pre-installed or separately available in
      AU used/refurbished market.
- [ ] Total cost (unit + any GPU additions) within AUD budget.
- [ ] No disqualifying thermal flag (inadequate airflow for dual-GPU sustained load).
- [ ] No ECC-only memory constraint that would prevent standard GPU driver operation.

**GPU Rules:** Same as Pathway A — 8 GB VRAM minimum per GPU, any make/model.

**Agent Responsibilities:**
- Existing cards in `02_Refurbished_Desktop_Towers/` are the primary candidates.
- For each card: verify age, PCIe slot spec, PSU spec, GPU compatibility. Flag UNKNOWN for any
  missing field.
- Flag for review: Dell Precision 5820 bundle ($3,558 includes ThinkPad T14s) — find unbundled tower-only price or mark "bundle only".
- You may add new candidates from the internet.

---

### Pathway C — Unified Memory Mini PC

**Definition:** A compact/mini PC using AMD Strix Halo (Ryzen AI Max / Ryzen AI Max+) or
architecturally equivalent high-bandwidth unified-memory SoC, where system RAM is simultaneously
GPU VRAM.

**Unified Memory Floor:** 32 GB minimum. 64–128 GB preferred.

**Go/No-Go Gates (ALL must pass before any action is taken):**
- [ ] Device confirmed to use a unified-memory SoC (Strix Halo or equivalent — not a standard
      iGPU + discrete GPU combo).
- [ ] Unified memory ≥ 32 GB confirmed from spec sheet (not estimated).
- [ ] AU stock confirmed at credible retailer.
- [ ] Price within AUD budget.
- [ ] No disqualifying thermal flag (passive-only or inadequate cooling for sustained inference
      workloads is a flag).
- [ ] No disqualifying ROCm software compatibility gap for target workloads.
- [ ] If refurbished/open-box: Minimum 3-month seller warranty or ACL coverage confirmed
- [ ] If refurbished/open-box: Condition grade disclosed (Grade A/B acceptable; C/D flagged for manual review)

**Confirmed AU Stock Candidates:**
- Minisforum AI X1 Pro (Ryzen AI Max+ 370/470, up to 128 GB unified)
  - AU retailers: au.minisforum.com, MegaTechStore AU
  - Pricing: Quote required
  - Status: ✅ Confirmed in stock

**Priority Research Targets (UNKNOWN — manual verification required):**
- HP Z2 Mini G1a (Strix Halo variant, if exists)
- HP Elite Mini 800 G11 AI (Strix Halo variant, if exists)
- Any HP workstation mini PC with Ryzen AI Max/Max+
- Prioritize refurbished/open-box from: HP AU Refurbished Store, Scorptec, Mwave, eBay AU enterprise sellers

**Excluded:**
- ASUS NUC 14 Pro AI (Intel Core Ultra, NOT Strix Halo)

**Agent Responsibilities:**
- Maintain candidate cards in `06_Mini_PCs_and_eGPU/` (existing lane).
- For each candidate: confirm SoC model, unified memory config, AU availability. Use the internet to resolve UNKNOWN fields.
- You may add new candidates from the internet.

---

## TRACK 2 — AGENT RESPONSIBILITIES (REPO-ONLY)

- **Pathway A:** Maintain and update `01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md`.
- **Pathway B:** Audit `02_Refurbished_Desktop_Towers/*.md` cards against all gate conditions.
- **Pathway C:** Audit and/or create candidate shells in `06_Mini_PCs_and_eGPU/`.
- Produce a unified Track 2 data-ready checklist: a markdown table of all UNKNOWN fields across
  all three pathways requiring verification, and use the browser to fill them before gates can be cleared.
- Actively use the internet to resolve and fill UNKNOWN fields.
