import re
with open("/Users/okgoogle13/Projects/Computer purchase/AGENTS.md", "r") as f:
    text = f.read()

# 1. Add AMD Discrete Sub-section to Track 1 NVIDIA Path
amd_discrete = """
#### AMD Discrete GPU Laptops
AMD discrete GPU laptops evaluate under same rules as NVIDIA:
- HP OMEN Max (Ryzen AI 9 HX 375 + RTX 5070/5090)
- Tag as: architecture:discrete_gpu_amd, track_eligibility:track_1_nvidia_path
- Move cards from Strix_Halo_AMD/ to Gaming_Laptops_AMD_Discrete/
- Apply ≥16 GB VRAM floor, 16"+ screen size
"""
text = text.replace("#### Exclusions (Path 1A)", amd_discrete + "\n#### Exclusions (Path 1A)")

# 2. Track 1 Path 1B Screen size
old_screen = """#### Screen Size
- **No floor.** 13" and above are all in scope.
- 17–18" scoring bonus applies equally to this path."""
new_screen = """#### Screen Size
- **No minimum screen size.** 13-14" devices are valid Track 1 candidates BUT trigger immediate Track 2 urgency (portable device requires desktop companion for extended work).
- 17–18" scoring bonus applies equally to this path."""
text = text.replace(old_screen, new_screen)

# 3. Path 1B Brands and Families
old_brands = """#### Brands and Families in Scope
All brands — any laptop using a qualifying Strix Halo SoC is in scope. Confirmed candidates:
- ASUS TUF A16 (Strix Halo)
- ASUS ROG Zephyrus / Flow variants (Strix Halo)
- HP OMEN / Spectre AMD variants (Strix Halo) — AU availability UNKNOWN
- Any other 2024–2026 laptop with confirmed Strix Halo silicon

> **Excluded (no product):** Lenovo — no Strix Halo laptop exists in the Lenovo lineup.

#### Exclusions (Path 1B)
- Any AMD device with < 32 GB unified memory.
- Any AMD device using a non-unified architecture (discrete dGPU with standard Ryzen iGPU).
- Apple Silicon (separate category, currently deferred)."""

new_brands = """#### Brands and Families in Scope
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
- Any AMD device with < 32 GB unified memory.
- Any AMD device using a non-unified architecture (discrete dGPU with standard Ryzen iGPU).
- Apple Silicon (separate category, currently deferred)."""
text = text.replace(old_brands, new_brands)

# 4. Insert Track 1.5
track15 = """---

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
- Minimum 16 GB VRAM (same as Track 1 NVIDIA path)
- Target: RTX 3090 (24 GB), RTX 4080/4090, or equivalent

**Age Limit:** Maximum 6 years old (≥ 2020 manufacture date)

**Price Threshold (CRITICAL):**
Must beat equivalent Track 1 laptop on price/performance:
- [ ] Desktop ≤ 85% cost of comparable laptop (accounting for loss of portability)
- [ ] OR desktop offers ≥ 50% more VRAM at same price point

Example: Alienware R12 with RTX 3090 (24 GB) @ $2,500 AUD beats TUF A14 (32 GB unified ≈ 16 GB GPU-available) @ $3,499 AUD.

**Go/No-Go Gates:**
- [ ] Chassis ≥ 2020 (confirm manufacture date or CPU generation)
- [ ] GPU confirmed ≥ 16 GB VRAM
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
- Flag UNKNOWN for: exact manufacture date, PSU wattage, warranty terms
- Do NOT add new cards from web searches — use existing cards only

**Exclusions:**
- Custom/SI builds (those go to Track 2 Pathway A)
- Desktops with <16 GB VRAM
- Pre-2020 platforms (thermal/efficiency penalty too high)

"""
text = text.replace("## TRACK 2 — WORKSTATION", track15 + "## TRACK 2 — WORKSTATION")

# 5. Track 2 Pathway A Target updates
old_pathway_a = """**GPU Rules:**
- Minimum 16 GB VRAM per GPU.
- Any make/model: RTX 3090 (24 GB), RTX 4090 (24 GB used/new), Quadro RTX 6000 (24 GB),
  A4000 (16 GB), A5000 (24 GB), A6000 (48 GB), or equivalent.
- **Primary target:** RTX 3090 × 2 (48 GB total VRAM). Prefer NVLink-capable pairs where
  platform supports it.
- AU availability of RTX 3090 × 2 must be explicitly confirmed — do NOT assume.

**Agent Responsibilities:**"""
new_pathway_a = """**CPU Platform (LOCKED):**
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

**Agent Responsibilities:**"""
text = text.replace(old_pathway_a, new_pathway_a)

# 6. Track 2 Pathway B Review Flag
pb = """**Agent Responsibilities:**
- Existing cards in `Desktop_Towers_Refurbished/` are the primary candidates.
- For each card: verify age, PCIe slot spec, PSU spec, GPU compatibility. Flag UNKNOWN for any
  missing field.
- Flag for review: Dell Precision 5820 bundle ($3,558 includes ThinkPad T14s) — find unbundled tower-only price or mark "bundle only".
- Do NOT add new candidates from the internet."""
text = re.sub(r'\*\*Agent Responsibilities:\*\*\n- Existing cards in `Desktop_Towers_Refurbished/`.*?\n- Do NOT add new candidates from the internet\.', pb, text, flags=re.DOTALL)

# 7. Track 2 Pathway C Refurb Gates & Candidates
old_pc = """**Go/No-Go Gates (ALL must pass before any action is taken):**
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
- Any other 2024–2026 mini PC with confirmed Strix Halo / equivalent SoC"""

new_pc = """**Go/No-Go Gates (ALL must pass before any action is taken):**
- [ ] Device confirmed to use a unified-memory SoC (Strix Halo or equivalent — not a standard
      iGPU + discrete GPU combo).
- [ ] Unified memory ≥ 64 GB confirmed from spec sheet (not estimated).
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
- ASUS NUC 14 Pro AI (Intel Core Ultra, NOT Strix Halo)"""
text = text.replace(old_pc, new_pc)

with open("/Users/okgoogle13/Projects/Computer purchase/AGENTS.md", "w") as f:
    f.write(text)

