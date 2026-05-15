# P2 Candidate Verification and Shortlist Ingestion — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close out three eliminated P1 candidates from the discovery audit, verify four P2 candidates via live AU browser search, and ingest any confirmed-viable candidates into the active shortlist and product cards.

**Architecture:** Each task is self-contained: read the current card/shortlist state, run live verification via `agent-browser`, edit the card and shortlist row in place, validate with `pipeline_integrity_check.py`. No new pipeline scripts required — all changes go through existing CSV/card edit + pipeline validation pattern.

**Tech Stack:** agent-browser CLI, Python pipeline scripts (`pipeline_integrity_check.py`, `fill_shortlist_live_pricing.py`), CSV editing, Markdown card editing.

**Policy authority (highest to lowest):** `AGENTS.md` → `config/procurement_policy.json` → active shortlist CSVs → product cards.

**Active gates (from `config/procurement_policy.json`):**
- Budget cap: $5,000 AUD
- VRAM floor (discrete): 8 GB
- Screen size floor (Track 1A): ≥16 inches
- AU stock: must be confirmed from AU seller

**Active shortlist:** `shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv`
**Master ledger:** `shortlists/2026-05-13_shortlist.csv`

---

## File Map

| File | Action | Purpose |
|------|--------|---------|
| `cards/desktops/harvest-20260512-035_pioneer-dreambook-power-x370-rtx-4090.md` | Modify | Mark discontinued, add verification notes |
| `cards/desktops/harvest-20260512-029_hp-omen-transcend-16.md` | Modify | Mark not-AU-available, add verification notes |
| `cards/laptops/hp_omen_max.md` | Modify | Fill verified specs, price, stock |
| `shortlists/2026-05-13_shortlist.csv` | Modify | Update `hp_omen_max` row with verified price/VRAM/stock |
| `shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv` | Modify | Same — sync 1A-specific file |
| `cards/laptops/` (new card if needed) | Create | Product card for Legion Pro 5i or Zephyrus G16 if verified |
| `shortlists/2026-05-13_shortlist.csv` | Modify | Add new row for any verified P2 candidate |
| `shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv` | Modify | Add new row for any verified P2 candidate |

---

## Task 1 — Close Out Discarded P1 Candidates

**Files:**
- Modify: `cards/desktops/harvest-20260512-035_pioneer-dreambook-power-x370-rtx-4090.md`
- Modify: `cards/desktops/harvest-20260512-029_hp-omen-transcend-16.md`

No shortlist rows exist for these candidates — no CSV edits needed.

- [ ] **Step 1: Update Pioneer Dreambook X370 card**

Replace the entire `## Verification` section with:

```markdown
## Verification
- verification_status: Verified — DISCARDED
- policy_status: DISQUALIFIED
- policy_blockers: Product discontinued as of 2026-05-15. Pioneer Computers AU current lineup is X56/X58 (RTX 5090, from $6,468 AUD — over cap). X370 was last reviewed April 2023 and is not listed on pioneercomputers.com.au.
- verified_date: 2026-05-15
- verified_by: agent-browser (pioneercomputers.com.au)
- recommended_action: Do not pursue. No AU stock path exists.
```

- [ ] **Step 2: Confirm Pioneer card saved correctly**

```bash
grep "DISCARDED\|discontinued\|2026-05-15" "/Users/okgoogle13/Projects/Computer purchase/cards/desktops/harvest-20260512-035_pioneer-dreambook-power-x370-rtx-4090.md"
```

Expected output: 3 matching lines (DISCARDED, discontinued, 2026-05-15).

- [ ] **Step 3: Update HP Omen Transcend 16 card**

Replace the entire `## Verification` section with:

```markdown
## Verification
- verification_status: Verified — DISCARDED
- policy_status: DISQUALIFIED
- policy_blockers: Not sold in Australia as of 2026-05-15. Zero results across JB Hi-Fi, StaticIce, Harvey Norman, Scorptec, HP AU shop. HP Omen Transcend 16 is a US-market-only product. Do not confuse with HP Omen Max 16 (RTX 5080/5090), which IS available in AU.
- verified_date: 2026-05-15
- verified_by: agent-browser (hp.com/au, jbhifi.com.au, staticice.com.au, harveynorman.com.au)
- recommended_action: Do not pursue. The AU equivalent is hp_omen_max — verify that candidate separately.
```

- [ ] **Step 4: Confirm HP Omen Transcend card saved**

```bash
grep "DISCARDED\|US-market\|2026-05-15" "/Users/okgoogle13/Projects/Computer purchase/cards/desktops/harvest-20260512-029_hp-omen-transcend-16.md"
```

Expected: 3 matching lines.

- [ ] **Step 5: Commit**

```bash
git add "cards/desktops/harvest-20260512-035_pioneer-dreambook-power-x370-rtx-4090.md" \
        "cards/desktops/harvest-20260512-029_hp-omen-transcend-16.md"
git commit -m "chore: mark pioneer x370 and hp omen transcend as discarded (not AU-available)"
```

---

## Task 2 — Verify HP Omen Max 16 (P1 Promoted)

**Context:** `hp_omen_max` has status `ACTIVE` in master shortlist with `price_aud=UNKNOWN`, `au_stock=UNKNOWN`, `vram=24GB` (RTX 5090 per card). During the P1 browser sweep, a sponsored eBay listing confirmed: "HP OMEN MAX Gaming Laptop 16" WQXGA OLED Ultra 9 275HX 32GB 1TB SSD RTX 5080". Need to confirm: is the AU model RTX 5090 or RTX 5080? What is the current AU retail price?

**Files:**
- Modify: `cards/laptops/hp_omen_max.md`
- Modify: `shortlists/2026-05-13_shortlist.csv` (row: `hp_omen_max`)
- Modify: `shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv` (row: `hp_omen_max`)

- [ ] **Step 1: Open HP AU gaming laptops page**

```bash
agent-browser open "https://www.hp.com/au-en/gaming/omen/laptops.html"
agent-browser wait --load networkidle
agent-browser snapshot | grep -iE "(omen max|transcend|price|\$|rtx|5090|5080)"
```

If that URL 404s, try: `https://www.hp.com/au-en/shop/plp/laptops` then search for OMEN.

Expected: HP Omen Max 16 product listing with price.

- [ ] **Step 2: Navigate to HP Omen Max 16 product page**

Click the product link or open the direct PDP. Capture:
- Price (AUD, inc-GST)
- GPU model (RTX 5090 or RTX 5080 — AU SKU may differ from US)
- VRAM (24 GB for 5090, 16 GB for 5080)
- Screen size (confirm 16 inches)
- AU in-stock status
- Warranty (HP manufacturer warranty months)

```bash
agent-browser snapshot | grep -iE "(price|\$|aud|rtx|5090|5080|vram|gb|screen|inch|warranty|stock|in.stock|add to cart|available)"
```

- [ ] **Step 3: Cross-check on JB Hi-Fi and Harvey Norman**

```bash
agent-browser open "https://www.jbhifi.com.au/search?q=hp+omen+max+16"
agent-browser wait --load networkidle
agent-browser snapshot | grep -iE "(omen max|price|\$|rtx|5090|5080|in.stock|add to cart)"
```

Then check Harvey Norman:

```bash
agent-browser open "https://www.harveynorman.com.au/search.html?q=hp+omen+max+16"
agent-browser wait --load networkidle
agent-browser snapshot | grep -iE "(omen max|price|\$|rtx|5090|5080|in.stock)"
```

Record the lowest confirmed in-stock AU price. Per policy, use the lowest across all checked retailers.

- [ ] **Step 4: Close browser**

```bash
agent-browser close
```

- [ ] **Step 5: Update hp_omen_max card**

In `cards/laptops/hp_omen_max.md`, update the frontmatter with confirmed values:

```markdown
---
id: hp-omen-max-rtx-[5080|5090]
category: laptop
architecture: discrete_gpu_nvidia
track_eligibility: track_1A
name: HP OMEN Max 16 ([GPU confirmed])
gpu: NVIDIA GeForce RTX [5080|5090] Laptop GPU
vram: [16|24] GB
screen_size_in: 16
price_aud: [CONFIRMED PRICE]
retailer: [CONFIRMED RETAILER]
au_stock: [Yes|No]
warranty_months: [MONTHS]
verification_status: Verified
verified_date: 2026-05-15
Performance_Headroom: [keep existing or update]
Price_Value: [keep existing or update]
Future_Proof: [keep existing or update]
Portability: [keep existing or update]
Track2_Avoidance: [keep existing or update]
---
```

Add a `## Verification Notes` section at the bottom:

```markdown
## Verification Notes
- Verified via agent-browser on [retailer URL], 2026-05-15
- GPU: RTX [5080|5090] Laptop GPU, [16|24] GB VRAM confirmed
- Price: AU $[X,XXX] at [retailer]
- AU stock: [Yes — in cart / No — out of stock]
- Warranty: [X] months HP manufacturer warranty
```

- [ ] **Step 6: Update hp_omen_max rows in both CSVs**

In `shortlists/2026-05-13_shortlist.csv`, find the `hp_omen_max` row and update these columns:
- `status`: `ACTIVE` → `BUY_CANDIDATE` (if passes all gates) or `NEEDS_REVIEW` (if any gate fails)
- `gpu_model`: fill confirmed GPU
- `vram_gb`: fill confirmed VRAM
- `price_aud`: fill confirmed price
- `Over_Budget`: `No` if ≤$5,000, else `Yes`
- `Price_Unknown`: clear if was `Yes`
- `retailer`: fill confirmed retailer
- `verification_status`: `Verified`
- `au_stock`: `Yes` or `No`
- `seller_class`: `MANUFACTURER_AU` (HP.com.au) or `MAJOR_RETAILER_AU` (JB/HN)

Apply the same edit to `shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv`.

- [ ] **Step 7: Run gate check**

```bash
cd "/Users/okgoogle13/Projects/Computer purchase"
python3 scripts/policy_drift_check.py
```

Expected: no new policy drift errors. If price is over $5,000, `Over_Budget` must be `Yes` — fix if needed.

- [ ] **Step 8: Commit**

```bash
git add cards/laptops/hp_omen_max.md \
        "shortlists/2026-05-13_shortlist.csv" \
        "shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv"
git commit -m "feat: verify hp omen max 16 — fill price, VRAM, AU stock"
```

---

## Task 3 — Verify Lenovo Legion Pro 5i RTX 5070 Ti (P2)

**Context:** `harvest-20260512-005` is a stub card with all UNKNOWN fields. The Legion Pro 5i is a 16-inch laptop (distinct from the 18-inch Legion Pro 7i). RTX 5070 Ti Laptop GPU = 12 GB VRAM. Needs: price AU, AU stock, screen size confirmation (target 16 in), thermal risk check, warranty.

**Files:**
- Modify: `cards/desktops/harvest-20260512-005_lenovo-legion-pro-5i-5070-ti.md`
- Create (if verified viable): `cards/laptops/harvest-20260512-005_lenovo-legion-pro-5i-5070-ti.md` (move to laptops subfolder)
- Modify (if viable): `shortlists/2026-05-13_shortlist.csv` (add new row)
- Modify (if viable): `shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv` (add new row)

- [ ] **Step 1: Search Lenovo AU for Legion Pro 5i Gen 10**

```bash
agent-browser open "https://www.lenovo.com/au/en/p/laptops/legion-laptops/legion-pro-5-series/lenovo-legion-pro-5i-gen-10-(16-inch-intel)/83dn"
agent-browser wait --load networkidle
agent-browser snapshot | grep -iE "(price|\$|aud|rtx|5070|5080|vram|gb|screen|inch|stock|add to cart|available|out.of.stock)"
```

If URL 404s, go to `https://www.lenovo.com/au/en/laptops/legion-laptops/` and search for "Legion Pro 5i".

- [ ] **Step 2: Confirm screen size and GPU**

The Legion Pro 5i Gen 10 is confirmed as a 16-inch laptop. Verify:
- GPU: RTX 5070 Ti Laptop GPU, 12 GB VRAM (check config options)
- Screen: 16 inches (this differentiates it from the 7i at 16 in / 9i at 18 in)
- Price range in AU
- Availability (in-stock vs out-of-stock vs preorder)

```bash
agent-browser snapshot | grep -iE "(5070 ti|5070ti|12gb|vram|16.?inch|16\"|screen|display|price|\$[0-9]|aud|add to cart|out of stock)"
```

- [ ] **Step 3: Cross-check JB Hi-Fi**

```bash
agent-browser open "https://www.jbhifi.com.au/search?q=lenovo+legion+pro+5i+rtx+5070+ti"
agent-browser wait --load networkidle
agent-browser snapshot | grep -iE "(legion pro 5i|5070|price|\$|aud|stock|add to cart)"
```

- [ ] **Step 4: Close browser and assess gate status**

```bash
agent-browser close
```

Gate assessment (all must pass for Track 1A):
- [ ] Screen ≥ 16 inches: ___
- [ ] VRAM ≥ 8 GB (discrete): ___ (RTX 5070 Ti = 12 GB if confirmed)
- [ ] Price ≤ $5,000 AUD: ___
- [ ] AU stock confirmed: ___
- [ ] No disqualifying thermal risk: ___ (check notebookcheck if needed)

**If ANY gate fails → mark card as DISQUALIFIED, do NOT add shortlist row.**
**If ALL gates pass → continue to Step 5.**

- [ ] **Step 5: Update card with verified data (if viable)**

Update `cards/desktops/harvest-20260512-005_lenovo-legion-pro-5i-5070-ti.md`:

```markdown
# lenovo legion pro 5i gen 10 rtx 5070 ti

## Candidate Metadata
- intake_id: harvest-20260512-005
- item_name: Lenovo Legion Pro 5i Gen 10 (16-inch) RTX 5070 Ti
- track: 1
- pathway: 1A
- category: laptop
- gpu_model: NVIDIA GeForce RTX 5070 Ti Laptop GPU
- vram_gb: 12
- unified_memory_gb: N/A
- screen_size_in: 16
- price_aud: [CONFIRMED]
- retailer: [CONFIRMED — lenovo.com.au or JB Hi-Fi]
- au_stock: [Yes|No]
- warranty_months_confirmed: [MONTHS]

## Verification
- verification_status: Verified — [VIABLE|DISQUALIFIED]
- policy_status: [PASSES_GATES|DISQUALIFIED]
- policy_blockers: [None|list any failures]
- verified_date: 2026-05-15
- verified_by: agent-browser (lenovo.com.au, jbhifi.com.au)

## Provenance
- harvested_from: _Archive_Legacy_Data/comprehensive_llm_recommendation_log_notebooklm_optimized.md
- harvested_via: scripts/harvest_llm_recommendations.py
```

- [ ] **Step 6: Add shortlist row (only if VIABLE)**

Add the following row to BOTH `shortlists/2026-05-13_shortlist.csv` and `shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv`. Use the column order from the header row exactly:

```
harvest-20260512-005,Lenovo Legion Pro 5i Gen 10 (16-inch) RTX 5070 Ti,ACTIVE,Laptop,laptop,Complete_System,1,1A,NVIDIA GeForce RTX 5070 Ti Laptop GPU,12.0,,16.0,,<PRICE>,No,,New,<RETAILER>,Verified,Yes,<SELLER_CLASS>,MAJOR_RETAILER_AU,discovery_audit_2026-05-15,cards/desktops/harvest-20260512-005_lenovo-legion-pro-5i-5070-ti.md,,Passed gates — P2 discovery audit,,harvest-20260512-005,Candidate,,,,,,
```

Replace `<PRICE>`, `<RETAILER>`, `<SELLER_CLASS>` with confirmed values. `<SELLER_CLASS>` = `MANUFACTURER_AU` for lenovo.com.au, `MAJOR_RETAILER_AU` for JB Hi-Fi.

- [ ] **Step 7: Validate**

```bash
cd "/Users/okgoogle13/Projects/Computer purchase"
python3 scripts/policy_drift_check.py
```

Expected: no errors.

- [ ] **Step 8: Commit**

```bash
git add "cards/desktops/harvest-20260512-005_lenovo-legion-pro-5i-5070-ti.md" \
        "shortlists/2026-05-13_shortlist.csv" \
        "shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv"
git commit -m "feat: verify lenovo legion pro 5i rtx 5070 ti — [VIABLE|DISQUALIFIED]"
```

---

## Task 4 — Verify ASUS Zephyrus G16 RTX 5080 GU605 (P2)

**Context:** `harvest-20260512-004` is a stub. The ASUS Zephyrus G16 (GU605) with RTX 5080 is distinct from the Strix G16 (G614) already in the shortlist as `42_asus-rog-strix-g16-rtx-5080-2025`. GU605 = thinner chassis (1.65 kg), AMD CPU + NVIDIA dGPU config, 16-inch QHD+ panel. RTX 5080 Laptop = 16 GB VRAM.

**Files:**
- Modify: `cards/desktops/harvest-20260512-004_asus-zephyrus-g16-5080.md`
- Modify (if viable): `shortlists/2026-05-13_shortlist.csv` (add new row)
- Modify (if viable): `shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv` (add new row)

- [ ] **Step 1: Search ASUS AU for Zephyrus G16 RTX 5080**

```bash
agent-browser open "https://rog.asus.com/au/laptops/rog-zephyrus/rog-zephyrus-g16-2025/"
agent-browser wait --load networkidle
agent-browser snapshot | grep -iE "(5080|5090|rtx|price|\$|aud|vram|gb|stock|add to cart|out.of.stock|available)"
```

If that URL fails, try: `https://www.asus.com/au/laptops/for-gaming/zephyrus/` and navigate to G16 2025.

- [ ] **Step 2: Confirm GU605 model number and RTX 5080 config**

Verify:
- Model: GU605 (not G614 Strix)
- GPU: RTX 5080 Laptop, 16 GB VRAM (not 5090)
- Screen: 16 inches
- Price AU (with and without any current promotions)
- Stock availability

```bash
agent-browser snapshot | grep -iE "(GU605|G614|5080|16gb|screen|16\"|price|\$[0-9]|aud|add to cart|out of stock|model)"
```

- [ ] **Step 3: Cross-check Scorptec and MSY**

```bash
agent-browser open "https://www.scorptec.com.au/search?q=asus+zephyrus+g16+5080"
agent-browser wait --load networkidle
agent-browser snapshot | grep -iE "(zephyrus g16|5080|price|\$|aud|stock|add to cart)"
```

- [ ] **Step 4: Close browser and assess gates**

```bash
agent-browser close
```

Gate assessment:
- [ ] Screen ≥ 16 inches: ___ (GU605 = 16 in QHD+)
- [ ] VRAM ≥ 8 GB: ___ (RTX 5080 Laptop = 16 GB if confirmed)
- [ ] Price ≤ $5,000 AUD: ___
- [ ] AU stock confirmed: ___
- [ ] No disqualifying thermal risk: ___ (Zephyrus thin chassis — check notebookcheck GU605 if needed)

**If ANY gate fails → DISQUALIFIED. If ALL pass → continue.**

- [ ] **Step 5: Update card**

Update `cards/desktops/harvest-20260512-004_asus-zephyrus-g16-5080.md`:

```markdown
# asus rog zephyrus g16 2025 gu605 rtx 5080

## Candidate Metadata
- intake_id: harvest-20260512-004
- item_name: ASUS ROG Zephyrus G16 2025 (GU605) RTX 5080
- track: 1
- pathway: 1A
- category: laptop
- gpu_model: NVIDIA GeForce RTX 5080 Laptop GPU
- vram_gb: 16
- unified_memory_gb: N/A
- screen_size_in: 16
- price_aud: [CONFIRMED]
- retailer: [CONFIRMED]
- au_stock: [Yes|No]
- warranty_months_confirmed: [MONTHS]

## Verification
- verification_status: Verified — [VIABLE|DISQUALIFIED]
- policy_status: [PASSES_GATES|DISQUALIFIED]
- policy_blockers: [None|list any]
- note_distinct_from: 42_asus-rog-strix-g16-rtx-5080-2025 — GU605 Zephyrus chassis, not G614 Strix
- verified_date: 2026-05-15
- verified_by: agent-browser (rog.asus.com/au, scorptec.com.au)

## Provenance
- harvested_from: _Archive_Legacy_Data/comprehensive_llm_recommendation_log_notebooklm_optimized.md
- harvested_via: scripts/harvest_llm_recommendations.py
```

- [ ] **Step 6: Add shortlist row (only if VIABLE)**

Add to BOTH CSVs (same column order as Task 3 Step 6):

```
harvest-20260512-004,ASUS ROG Zephyrus G16 2025 (GU605) RTX 5080,ACTIVE,Laptop,laptop,Complete_System,1,1A,NVIDIA GeForce RTX 5080 Laptop GPU,16.0,,16.0,,<PRICE>,No,,New,<RETAILER>,Verified,Yes,<SELLER_CLASS>,<SOURCE_PLATFORM>,discovery_audit_2026-05-15,cards/desktops/harvest-20260512-004_asus-zephyrus-g16-5080.md,,Passed gates — P2 discovery audit; distinct from G614 Strix shortlist entry,,harvest-20260512-004,Candidate,,,,,,
```

- [ ] **Step 7: Validate and commit**

```bash
cd "/Users/okgoogle13/Projects/Computer purchase"
python3 scripts/policy_drift_check.py
git add "cards/desktops/harvest-20260512-004_asus-zephyrus-g16-5080.md" \
        "shortlists/2026-05-13_shortlist.csv" \
        "shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv"
git commit -m "feat: verify asus zephyrus g16 gu605 rtx 5080 — [VIABLE|DISQUALIFIED]"
```

---

## Task 5 — Verify Dell Outlet Alienware M18 R2 (P2)

**Context:** `harvest-20260512-001` is a stub for the Dell Outlet AU channel specifically. The shortlist already has `laptop4134_alienware_m18_r2` (RTX 4090, $3,899 AU from Dell Outlet, verified). This task checks whether Dell Outlet AU currently has additional M18 R2 configs at better price/warranty terms. If it's the same listing, merge; if a different config exists, create a new row.

**Files:**
- Modify: `cards/desktops/harvest-20260512-001_dell-outlet-alienware-m18-r2.md`
- Modify (if new config found): `shortlists/2026-05-13_shortlist.csv`
- Modify (if new config found): `shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv`

- [ ] **Step 1: Open Dell Outlet AU and filter to Alienware**

```bash
agent-browser open "https://www.dell.com/en-au/shop/dell-outlet/cp/outlet"
agent-browser wait --load networkidle
agent-browser snapshot -i | grep -iE "(alienware|m18|laptop|filter|category|link)" | head -20
```

Navigate to the Alienware / Gaming Laptops section.

- [ ] **Step 2: Check available M18 R2 configs**

```bash
agent-browser snapshot | grep -iE "(m18|alienware|rtx|4090|4080|5080|5090|price|\$|aud|stock|add to cart|config|gb)"
```

Record all distinct configurations available (GPU, VRAM, RAM, price).

- [ ] **Step 3: Compare against existing shortlist entry**

The existing `laptop4134_alienware_m18_r2` shortlist row shows:
- GPU: NVIDIA GeForce RTX 4090 Laptop GPU
- Price: $3,899.10 AUD
- Condition: Refurbished
- Retailer: Dell Outlet Australia
- Status: BUY_CANDIDATE

Check if the current Dell Outlet listing for that model number matches OR if there are additional distinct configs (e.g., RTX 4080, different RAM, newer Alienware M18 R2 variant).

- [ ] **Step 4: Close browser and decide**

```bash
agent-browser close
```

Decision tree:
- If same config as `laptop4134` → mark harvest-20260512-001 as **Merged opportunity** into laptop4134. Update card. No new shortlist row.
- If different config (better GPU, lower price, or different RAM) → continue to Step 5 for a new card/row.
- If no M18 R2 available → mark as **Discarded — out of stock at time of check**.

- [ ] **Step 5: Update card with outcome**

Update `cards/desktops/harvest-20260512-001_dell-outlet-alienware-m18-r2.md`:

**Case A — Merged into laptop4134:**
```markdown
## Verification
- verification_status: Verified — MERGED
- policy_status: MERGED_OPPORTUNITY
- merged_into: laptop4134_alienware_m18_r2
- merge_reason: Same retailer (Dell Outlet AU), same GPU config (RTX 4090). No distinct config found on 2026-05-15.
- verified_date: 2026-05-15
- verified_by: agent-browser (dell.com/en-au/shop/dell-outlet)
```

**Case B — New config found:**
```markdown
## Verification
- verification_status: Verified — VIABLE
- policy_status: PASSES_GATES
- policy_blockers: None
- note: Distinct from laptop4134 — [explain difference e.g. RTX 4080 at lower price]
- price_aud: [CONFIRMED]
- gpu_model: [CONFIRMED GPU]
- vram_gb: [CONFIRMED VRAM]
- verified_date: 2026-05-15
- verified_by: agent-browser (dell.com/en-au/shop/dell-outlet)
```

**Case C — Out of stock:**
```markdown
## Verification
- verification_status: Verified — DISCARDED
- policy_status: DISQUALIFIED
- policy_blockers: No Alienware M18 R2 stock at Dell Outlet AU as of 2026-05-15.
- verified_date: 2026-05-15
```

- [ ] **Step 6: Add shortlist row only for Case B**

If Case B, add new row to both CSVs with confirmed data (same pattern as Task 3 Step 6, but with `dell.com/en-au/shop/dell-outlet` as retailer, `MANUFACTURER_AU` as seller_class).

- [ ] **Step 7: Validate and commit**

```bash
cd "/Users/okgoogle13/Projects/Computer purchase"
python3 scripts/policy_drift_check.py
git add "cards/desktops/harvest-20260512-001_dell-outlet-alienware-m18-r2.md" \
        "shortlists/2026-05-13_shortlist.csv" \
        "shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv"
git commit -m "chore: verify dell outlet alienware m18 r2 — [merged|new-config|discarded]"
```

---

## Task 6 — Pipeline Integrity Check and Session Summary

**Files:** Read-only — no edits.

- [ ] **Step 1: Run full pipeline integrity check**

```bash
cd "/Users/okgoogle13/Projects/Computer purchase"
python3 scripts/pipeline_integrity_check.py \
  --enriched "shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv" \
  --ranked "shortlists/2026-05-13_shortlist_ranked_latest.csv"
```

Expected: no integrity errors. If errors appear, fix the relevant CSV row before continuing.

- [ ] **Step 2: Run policy drift check**

```bash
python3 scripts/policy_drift_check.py
```

Expected: no drift. If drift is reported, check that `config/procurement_policy.json` values match `AGENTS.md` thresholds.

- [ ] **Step 3: Count active BUY_CANDIDATE rows in 1A shortlist**

```bash
grep "BUY_CANDIDATE\|GOOD ENOUGH" "/Users/okgoogle13/Projects/Computer purchase/shortlists/2026-05-13_shortlist_track-1_pathway-1A.csv" | wc -l
```

Expected: ≥4 rows (the pre-existing BUY_CANDIDATE entries: `aa182502898_alienware_18_area_51`, `laptop4134_alienware_m18_r2`, `lenovo-legion-pro-7-5080-centrecom`, `mikepc_msi_raider_ge68_rtx4090`, `36_lenovo-legion-9i-18-rtx-5080-ebay`, `052_alienware-m18-r2-rtx-4080` [GOOD ENOUGH], `054_alienware-m18-r2-rtx-4090` [GOOD ENOUGH]) plus any newly ingested P2 candidates.

- [ ] **Step 4: Produce session handoff note**

Print or record:
1. Which P2 candidates were verified VIABLE and added to shortlist
2. Which were DISCARDED and why
3. Which require a follow-up browser pass (e.g., Radeon RX 7900M laptop)
4. Whether `hp_omen_max` is now a BUY_CANDIDATE — if so, whether it should trigger the pre-decision checklist in AGENTS.md

---

## Verification Checklist (Audit Complete When)

- [ ] Pioneer X370 card → status `DISCARDED` with verification notes
- [ ] HP Omen Transcend 16 card → status `DISCARDED` with verification notes
- [ ] `hp_omen_max` card → all fields filled, verification_status = `Verified`
- [ ] `hp_omen_max` shortlist rows → `price_aud`, `vram_gb`, `au_stock`, `retailer` all non-UNKNOWN
- [ ] Legion Pro 5i card → status `VIABLE` or `DISQUALIFIED` with verification notes
- [ ] Zephyrus G16 GU605 card → status `VIABLE` or `DISQUALIFIED` with verification notes
- [ ] Dell Outlet M18 R2 card → status `MERGED`, `VIABLE`, or `DISCARDED`
- [ ] `policy_drift_check.py` → passes with no errors
- [ ] `pipeline_integrity_check.py` → passes with no errors
- [ ] All changes committed to git

---

## Remaining P3 Work (out of scope for this plan)

- Radeon RX 7900M 16 GB Laptop — no AU stock found during P1 pass; needs a dedicated eBay AU sweep
- RTX 4000 Ada / RTX 5000 Ada Laptop — workstation-class; single search pass on hp.com.au ZBook and lenovo.com.au ThinkPad P
- harvest-20260512-030–033 Legion Pro 7i RTX 4090 variants — check if any is a distinct seller from `21_lenovo-legion-pro-7i-rtx-4090`
