# Track 1 Verification and Pricing Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** turn the current Track 1 candidate set into a live-verified shortlist with current AU stock, effective pricing, and enough evidence to make a reliable buy/no-buy decision.

**Architecture:** keep the work in three layers. First, triage the current repository evidence into a tight candidate queue. Second, verify live AU stock and effective price for those candidates. Third, score only the candidates that survive the gates and write the resulting shortlist back into the repo.

**Tech Stack:** repo CSVs and markdown cards, `scripts/enrich_shortlist_pricing.py`, `scripts/prompt_templates/browser_pricing_lookup.md`, `NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/rubric_weighting_engine.py`, live browser verification.

---

## Current Status

The repo now has a simplified Track 1 policy, a Track 1 focused shortlist, and a bargain exception for 12 GB discrete laptops. The current gap is not policy. The gap is live evidence:

- several cards still have `UNKNOWN` stock, warranty, or thermal data,
- some candidates are only present as older non-intake cards,
- one MSI Crosshair row has a repository conflict between older shortlist data and current card data,
- the 12 GB and 8 GB bargain lane needs live price verification before it can be treated as useful.

## Task 1: Lock the verification queue

**Files:**
- Modify: `NotebookLM_Workspaces/intake/shortlist/2026-05-07_track1_focused_shortlist.md`
- Modify: `NotebookLM_Workspaces/intake/shortlist/2026-05-07_track1_focused_shortlist.csv`

- [ ] **Step 1: Freeze the top verification order**

Use the current shortlist and keep the first five candidates as the live pricing queue:

1. Acer Predator Helios 18
2. Dell Alienware m18 R2 / Area-51
3. Lenovo Legion Pro 7i
4. Lenovo Legion 9i Gen 10 18 in RTX 5080
5. MSI Stealth A16 5080

- [ ] **Step 2: Mark the conflict rows explicitly**

Keep these rows visible in the focused shortlist, but label them as conflict or bargain-watchlist items instead of buy candidates:

- MSI Crosshair 18 HX AI
- MSI Raider A18 HX Remanufactured
- MSI Katana 17 HX
- MSI Vector A18 RTX 5070 Ti

- [ ] **Step 3: Preserve the parked rows**

Leave the clearly non-viable Track 1 items parked:

- ASUS ROG Strix Scar 18 RTX 4090
- MSI Raider 18 HX AI A2XWJG
- Razer Blade 18
- ASUS ROG Strix G18 2025 RTX 5070 Ti
- ASUS ROG Zephyrus G16 2025 RTX 5070

## Task 2: Verify live price and stock

**Files:**
- Modify: `NotebookLM_Workspaces/intake/shortlist/2026-05-07_track1_focused_shortlist.csv`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/intake-051_acer-predator-helios-18.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/intake-011_dell-alienware-m18-r2-area-51.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/intake-009_lenovo-legion-pro-7i.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/36_lenovo-legion-9i-18-rtx-5080-ebay.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/intake-045_msi-stealth-a16-5080.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/intake-013_msi-crosshair-18-hx-ai.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/22_asus-rog-strix-scar-17-rtx-4090.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/30_asus-rog-strix-scar-18-rtx-5090-2025.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/asus-tuf-a14.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/asus-proart-px13.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/asus-rog-flow-z13.md`

- [ ] **Step 1: Use the browser pricing template**

Run the browser lookup prompt for each queue item and collect:

- current best AU price,
- retailer,
- URL,
- in-stock status,
- student discount possibility,
- cashback possibility,
- price-match possibility,
- effective best price.

- [ ] **Step 2: Confirm seller credibility**

For each candidate, verify whether the seller is:

- a manufacturer AU store,
- a major AU retailer,
- a known refurb seller,
- or a weaker marketplace listing.

Treat marketplace items as higher risk unless the seller history and warranty are strong.

- [ ] **Step 3: Confirm the minimum spec fields**

For every buy-queue candidate, resolve these gaps before scoring:

- exact screen size,
- exact GPU model and VRAM,
- RAM installed and max supported,
- storage installed and expandability,
- warranty or ACL coverage,
- thermal reputation.

## Task 3: Resolve the bargain lane

**Files:**
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/intake-013_msi-crosshair-18-hx-ai.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/39_msi-raider-a18-hx-refurb.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/40_msi-katana-17-hx.md`
- Modify: `NotebookLM_Workspaces/04_Laptops_Mainline/41_asus-rog-strix-g18-rtx-5070ti-2025.md`
- Modify: `NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/ranking_feedback_loop.py`

- [ ] **Step 1: Resolve the MSI Crosshair contradiction**

The repo currently contains two different stories for the Crosshair 18 HX AI:

- one older shortlist says 12 GB, about 3,385 AUD, AU stock yes,
- the current card says 16 GB and price unknown.

Resolve this before allowing the row to influence ranking.

- [ ] **Step 2: Decide the bargain watchlist fate**

Classify each of these as one of the following:

- live bargain candidate,
- parked bargain reference,
- rejected under current policy.

The classification should reflect the bargain exception rule:

- 12 GB can compete if the effective price is genuinely low,
- below 12 GB cannot become GOOD_ENOUGH,
- 8 GB should remain a cheap fallback only, not a winner.

- [ ] **Step 3: Update the bargain notes**

Make sure the bargain cards state the practical tradeoff plainly:

- cheap enough to be worth keeping visible,
- but not so strong on headroom that they masquerade as the top answer.

## Task 4: Fill MCDA and rank

**Files:**
- Modify: `NotebookLM_Workspaces/intake/shortlist/2026-05-07_shortlist_pricing_enriched.csv`
- Modify: `NotebookLM_Workspaces/intake/shortlist/2026-05-07_track1_focused_shortlist.csv`
- Modify: `NotebookLM_Workspaces/intake/shortlist/2026-05-07_track1_focused_shortlist.md`

- [ ] **Step 1: Populate the pricing-enriched CSV**

After browser verification, fill the live pricing fields and the MCDA columns only for candidates that still make sense under Track 1.

- [ ] **Step 2: Score the live candidates**

Use the current rubric rules:

- `Price_Value` can be high for a real bargain,
- `Performance_Headroom`, `Future_Proof`, and `Track2_Avoidance` must drop when VRAM is weak,
- anything below 12 GB discrete VRAM stays out of `GOOD_ENOUGH`.

- [ ] **Step 3: Rank with the engine**

Run:

```bash
python3 NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/rubric_weighting_engine.py \
  --csv NotebookLM_Workspaces/intake/shortlist/2026-05-07_shortlist_pricing_enriched.csv \
  --output-csv /private/tmp/track1_ranked.csv
```

Expected result:

- top candidates sort by MCDA,
- `GOOD_ENOUGH` only appears when the live evidence is complete,
- bargain candidates never outrank stronger 16 GB or 24 GB options just because they are cheap.

## Task 5: Final shortlist cleanup

**Files:**
- Modify: `NotebookLM_Workspaces/intake/shortlist/2026-05-07_track1_focused_shortlist.md`
- Modify: `NotebookLM_Workspaces/intake/shortlist/2026-05-07_track1_focused_shortlist.csv`

- [ ] **Step 1: Remove stale ambiguity**

Anything still marked as a buy candidate but missing current AU stock, current price, or warranty should be downgraded to verify-next.

- [ ] **Step 2: Keep the shortlist meaningful**

The final Track 1 shortlist should be small enough to act on:

- 1 or 2 buy candidates,
- a short verify-next queue,
- a bargain watchlist,
- a parked section for items that are no longer sensible.

- [ ] **Step 3: Commit the evidence trail**

Leave the repo with a current markdown summary, a current CSV, and a clear note of any unresolved gaps that still prevent a safe buy.

## Exit Criteria

The Track 1 shortlist is good enough when:

- the top candidates have live AU stock and price evidence,
- effective prices are known,
- warranty and thermal risks are resolved,
- the bargain lane is explicit and not confused with the main buy path,
- the ranking engine can produce a believable top item without unresolved `UNKNOWN`s in the key gates.
