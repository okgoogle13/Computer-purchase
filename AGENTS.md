# AGENTS.md — Two-Track Hardware Decision System

**Role:** Hardware-research and organisation helper inside the Antigravity IDE.
Keep decisions simple. Do NOT design the perfect system.
Operate on repo files only. No web or browser searches.

---

## SCOPE

- **Track 1:** Active laptop purchase. One decision. GOOD ENOUGH → buy.
- **Track 2:** Active workstation/desktop research. Three pathways. Likely medium-term outcome — runs in parallel with Track 1. Do not delay Track 1 for Track 2 unless a unicorn deal is immediately available.

---

## GLOBAL CONSTRAINTS

- **No web or browser access.** Do NOT open retailer sites or search engines. Do NOT call any browsing / web-search tools.
- **Work ONLY with:** existing markdown product cards, CSVs, policy/spec docs, scripts and templates in this repo.
- **Unknown values:** Never guess or invent real-world specs or prices. Leave fields as `UNKNOWN` and flag them in audit/checklist output.
- **Responsibilities:**
  - Audit and sync product cards vs CSVs.
  - Create and normalise product card shells.
  - Generate and refine prompt files.
  - Rebuild the mega-bundle.
  - Apply documented patches to spec/policy docs.
  - Draft decision logs and checklists.
  - Never fetch new data from the internet.

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
- **Minimum:** 16 GB VRAM.
- **Preferred:** 24 GB VRAM.
- A 16 GB card at 17–18" = standard eligible candidate.
- A 16 GB card at < 15" = requires offsetting strengths (build quality, price, resale) to remain competitive.

#### Brands and Families in Scope

**LENOVO**
- Legion 9i
- Legion Pro 9i
- Legion Pro 7i (current high-end variants meeting VRAM and budget rules)

**ASUS**
- ROG Strix Scar 17
- ROG Strix Scar 18
- Any ROG model at 13"+ meeting the 16 GB VRAM floor

**MSI**
Any current 13"+ high-end RTX gaming/workstation model meeting VRAM and price constraints, including:
- MSI Raider 17/18
- MSI Titan 17/18
- MSI Stealth 16/17/18
- MSI Vector 16/17/18
- Other MSI 13"+ models with ≥ 16 GB VRAM

#### Exclusions (Path 1A)
- Any laptop with less than 13" screen size.
- Any laptop with less than 16 GB discrete VRAM.
- Any brand/model family outside the three listed above, unless explicitly expanded.

#### Lenovo Legion Pro 7i vs 9i / Pro 9i Value Rule
- At the same price or within < 300 AUD difference: **prefer Legion 9i / Pro 9i over Pro 7i.**
- **Prefer Pro 7i** if it is ≥ 300–500 AUD cheaper than a comparable 9i/Pro 9i, while still meeting
  VRAM requirements, decent thermals, and upgradeability targets (32–64 GB RAM, ≥ 2 TB SSD).
- Pro 7i = "discount premium" tier, not equal to 9i/Pro 9i at the same price.

---

### Path 1B — AMD Strix Halo Unified Memory Laptops

#### Screen Size
- **No floor.** 13" and above are all in scope.
- 17–18" scoring bonus applies equally to this path.

#### Unified Memory
- **Minimum:** 32 GB (≈ equivalent to 16 GB discrete VRAM in GPU-accessible terms, given ~60–75%
  allocation to GPU workloads).
- **Preferred:** 64 GB.
- **Optimal:** 96–128 GB.

#### SoC Requirement
- Must use AMD Strix Halo (Ryzen AI Max / Ryzen AI Max+) or architecturally equivalent
  unified-memory SoC.
- Standard Ryzen with discrete dGPU does NOT qualify for this path.

#### Brands and Families in Scope
All brands — any laptop using a qualifying Strix Halo SoC is in scope. Candidates include:
- ASUS TUF A16 (Strix Halo)
- ASUS ROG Zephyrus / Flow variants (Strix Halo)
- Lenovo Legion / ThinkPad AMD variants (Strix Halo)
- HP OMEN / Spectre AMD variants (Strix Halo)
- Any other 2024–2026 laptop with confirmed Strix Halo silicon

#### Exclusions (Path 1B)
- Any AMD device with < 32 GB unified memory.
- Any AMD device using a non-unified architecture (discrete dGPU with standard Ryzen iGPU).
- Apple Silicon (separate category, currently deferred).

---

### Track 1 — Price Band

- **Total budget range (AUD):** 0–4,000
- **Preferred sweet spot (AUD):** 2,500–3,500
- Only consider 3,500–4,000 AUD if: GPU/unified memory is top-tier, build quality and thermals are
  clearly superior, and there is a strong resale story.

### Track 1 — Scoring Bonuses and Flags

- **+Bonus:** Screen size 17–18" (applies to both Path 1A and 1B).
- **+Bonus:** Top-tier memory for path — 24 GB discrete (1A) or 96–128 GB unified (1B).
- **−Competitive penalty:** Screen size < 15" with no offsetting Track 2 plan resolved.
- **⚠ Flag:** Thermal concerns (sustained throttling under sustained GPU load).
- **⚠ Flag (Path 1B only):** Known ROCm software compatibility gaps for target workloads.

---

## TRACK 1 — AGENT RESPONSIBILITIES (REPO-ONLY)

- Audit `laptop_candidates.csv` against `Laptops/*.md`:
  - Map every CSV row to a card file (or flag "NO CARD EXISTS").
  - Map every card file to a CSV row (or flag "NOT IN CSV").
  - Flag UNKNOWN / placeholder fields.
- For missing candidates within allowed scope: create BLANK product card shells using
  `template_product_card_output.md` with all spec fields set to UNKNOWN.
- Produce a "data-ready checklist" — a markdown table of all fields requiring manual web lookup.
- Do NOT attempt to fill UNKNOWN fields from the internet.

---

## GOOD ENOUGH STOP CONDITION (Track 1)

Mark a candidate as **"GOOD ENOUGH — STOP SEARCHING"** when ALL of the following are confirmed:

**Path 1A (NVIDIA):**
- In stock in AU from a credible retailer.
- ≥ 16 GB VRAM (24 GB preferred; RTX 5090 24 GB optimal; RTX 4090 16 GB acceptable fallback).
- Supports at least 32–64 GB RAM (installed or clearly upgradable).
- At least 2 TB SSD (installed or clearly upgradable).
- Price within the 0–4,000 AUD budget.
- No disqualifying thermal flag.

**Path 1B (AMD Strix Halo):**
- In stock in AU from a credible retailer.
- Confirmed Strix Halo SoC.
- ≥ 32 GB unified memory (64 GB preferred).
- Price within the 0–4,000 AUD budget.
- No disqualifying thermal flag.
- No disqualifying ROCm software compatibility gap for target workloads.

Do NOT expand scope beyond the listed families/SoC requirements unless explicitly instructed.

---

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
- [ ] Confirmed build spec exists in repo at `Decision_System/track2_pathway_a_build_spec.md`
      (CPU, motherboard, RAM, PSU, GPU, case — all named, no UNKNOWN fields).
- [ ] Target GPU(s) availability in AU market confirmed (flag UNKNOWN until manually verified).
- [ ] Build spec confirmed to support target GPU(s): PCIe slots, lane allocation, PSU wattage,
      physical clearance.
- [ ] Total cost (build + GPUs) within AUD budget.

**GPU Rules:**
- Minimum 16 GB VRAM per GPU.
- Any make/model: RTX 3090 (24 GB), RTX 4090 (24 GB used/new), Quadro RTX 6000 (24 GB),
  A4000 (16 GB), A5000 (24 GB), A6000 (48 GB), or equivalent.
- **Primary target:** RTX 3090 × 2 (48 GB total VRAM). Prefer NVLink-capable pairs where
  platform supports it.
- AU availability of RTX 3090 × 2 must be explicitly confirmed — do NOT assume.

**Agent Responsibilities:**
- Maintain confirmed build spec at `Decision_System/track2_pathway_a_build_spec.md`.
- All UNKNOWN fields (prices, stock) must be flagged — never invented.
- Do NOT contact integrators or browse their websites.

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
- [ ] GPU(s) confirmed ≥ 16 GB VRAM per card — either pre-installed or separately available in
      AU used/refurbished market.
- [ ] Total cost (unit + any GPU additions) within AUD budget.
- [ ] No disqualifying thermal flag (inadequate airflow for dual-GPU sustained load).
- [ ] No ECC-only memory constraint that would prevent standard GPU driver operation.

**GPU Rules:** Same as Pathway A — 16 GB VRAM minimum per GPU, any make/model.

**Agent Responsibilities:**
- Existing cards in `Desktop_Towers_Refurbished/` are the primary candidates.
- For each card: verify age, PCIe slot spec, PSU spec, GPU compatibility. Flag UNKNOWN for any
  missing field.
- Do NOT add new candidates from the internet.

---

### Pathway C — Unified Memory Mini PC

**Definition:** A compact/mini PC using AMD Strix Halo (Ryzen AI Max / Ryzen AI Max+) or
architecturally equivalent high-bandwidth unified-memory SoC, where system RAM is simultaneously
GPU VRAM.

**Unified Memory Floor:** 64 GB minimum. 96–128 GB preferred.

**Go/No-Go Gates (ALL must pass before any action is taken):**
- [ ] Device confirmed to use a unified-memory SoC (Strix Halo or equivalent — not a standard
      iGPU + discrete GPU combo).
- [ ] Unified memory ≥ 64 GB confirmed from spec sheet (not estimated).
- [ ] AU stock confirmed at credible retailer.
- [ ] Price within AUD budget.
- [ ] No disqualifying thermal flag (passive-only or inadequate cooling for sustained inference
      workloads is a flag).
- [ ] No disqualifying ROCm software compatibility gap for target workloads.

**Candidate shells to create (UNKNOWN stock/price — manual verification required):**
- Minisforum AI X1 Pro (Ryzen AI Max+, up to 128 GB)
- ASUS NUC-class or equivalent Strix Halo mini PC (where released to AU market)
- Any other 2024–2026 mini PC with confirmed Strix Halo / equivalent SoC

**Agent Responsibilities:**
- Maintain candidate cards in `Mini_PC_and_eGPU/` (existing lane).
- For each candidate: confirm SoC model, unified memory config, AU availability. Flag all UNKNOWN.
- Do NOT add candidates from the internet.

---

## TRACK 2 — AGENT RESPONSIBILITIES (REPO-ONLY)

- **Pathway A:** Maintain and update `Decision_System/track2_pathway_a_build_spec.md`.
- **Pathway B:** Audit `Desktop_Towers_Refurbished/*.md` cards against all gate conditions.
- **Pathway C:** Audit and/or create candidate shells in `Mini_PC_and_eGPU/`.
- Produce a unified Track 2 data-ready checklist: a markdown table of all UNKNOWN fields across
  all three pathways requiring manual verification before gates can be cleared.
- Do NOT attempt to fill UNKNOWN fields from the internet.
