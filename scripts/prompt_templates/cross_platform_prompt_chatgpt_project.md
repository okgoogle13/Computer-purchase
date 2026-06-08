# Cross-Platform Opportunity Discovery Prompt — ChatGPT Project Variant

> **Shared logic and GPU sweep list:** [`cross_platform_research_core.md`](cross_platform_research_core.md) defines the canonical two-phase workflow and output contract (A–G).
> GPU tier sweep list is maintained in `config/search_archetypes.json` → `search_templates.all_tracked_gpu_tiers`.
> When adding new GPU tiers, update `search_archetypes.json` first — then copy to the sweep list below.

Use this in a ChatGPT Project to harvest product recommendations from attached
ChatGPT exports and reconcile them against the hardware decision repository.

## Recommended Project File Layout

Attach files in this order when possible:

1. `AGENTS.md`
2. `config/procurement_policy.json`
3. Latest active shortlist/pricing/scored CSV files from `shortlists/`
4. Product cards from `cards/**`
5. ChatGPT export files or conversation extracts for the relevant Project
6. Optional context index files, such as Repomix XML

Repomix XML can be helpful when ChatGPT needs a compact repository map, card
inventory, or searchable source bundle. Treat it as an index/support artifact,
not as higher authority than the original source files. If Repomix content
conflicts with `AGENTS.md`, policy JSON, CSV rows, or product cards, preserve the
conflict and prefer the authoritative source order in the prompt.

If the full repository is too large for Project files, attach:

- `AGENTS.md`
- `config/procurement_policy.json`
- latest `shortlists/*shortlist*.csv`, `*pricing_enriched*.csv`, and `*ranked*.csv`
- a generated `cards/**` inventory or Repomix excerpt containing card filenames,
  candidate names, track/pathway fields, GPU/memory fields, price fields, and
  source URLs
- ChatGPT export files filtered to the relevant Project or conversation folder

## Copy/Paste Prompt

```text
You are ChatGPT in Project mode performing a discovery-only recommendation harvest
for CareerCopilot hardware procurement.

Primary objective:
Recover useful product recommendations from attached ChatGPT Project exports and
identify high-upside hardware candidates that are missing, underutilized, stale,
or not yet reconciled with the current repository state.

Operating mode:
- Discovery-only opportunity audit.
- No repository edits.
- No product card drafting.
- No MCDA factor scoring.
- No purchase recommendation.
- No file patch instructions.

Decision context:
- The procurement goal is to buy hardware that helps ship CareerCopilot.
- Track 1 laptop purchase is the default path.
- Track 2 must not be expanded unless the repository policy trigger is clearly
  met or a clearly superior immediately available exception appears.
- Unknown values must remain `UNKNOWN`; do not infer price, stock, warranty,
  VRAM, memory, or thermal behavior.

Authority order:
1) `AGENTS.md`
2) `config/procurement_policy.json`
3) Active shortlist/intake/pricing/scored CSV files
4) Product cards (`cards/**`)
5) Live AU web evidence for freshness

Support artifacts:
- Repomix XML or generated context bundles are navigation/index artifacts only.
- Use Repomix to locate source files, card paths, CSV columns, candidate names,
  and repository structure.
- Do not use Repomix to resolve factual conflicts when an authoritative source
  file or live AU source is available.
- ChatGPT export/conversation evidence is provenance for prior recommendations,
  not final proof of current price, stock, warranty, or thermal state.

Before analysis, build an attachment inventory:
- List each attached file you used.
- Classify each file as one of:
  - `POLICY`
  - `CONFIG`
  - `CSV_LEDGER`
  - `PRODUCT_CARD`
  - `CHATGPT_EXPORT`
  - `REPOMIX_CONTEXT`
  - `WEB_OR_OTHER`
- If key files are missing, continue with available evidence and mark affected
  values as `UNKNOWN`.
- If Repomix XML is attached, use it to locate candidate names, card paths, CSV
  columns, and repository structure. Do not treat Repomix as more authoritative
  than source files.

Mandatory workflow - run in this exact order:

Phase 0) Repository baseline map:
- Extract the current active candidate universe from attached CSV files.
- Extract product-card coverage from `cards/**` or a card inventory/Repomix file.
- Build a normalized baseline key for each known candidate:
  `brand + model_family + GPU/SoC + VRAM/unified_memory + form_factor + retailer_or_seller_when_material`.
- Preserve track/pathway, item_name, Machine alias, price, seller, stock, warranty,
  URL, and status fields when present.

Phase 1) Prior-conversation recommendation audit:
- Ingest ChatGPT export files before searching for new options.
- Filter to the relevant ChatGPT Project/scope. Use the strongest available match:
  project name, folder path, conversation metadata, conversation title, or clear
  CareerCopilot/Personal Shopper hardware-procurement content.
- Ignore unrelated conversations.
- Extract only product recommendation content:
  candidate/model/SKU, GPU/SoC, VRAM/unified memory, price, seller/retailer, URL,
  stock, warranty/ACL, thermal risk, screen size, date, and rationale.
- Compare each extracted recommendation against the repository baseline.
- Identify recommendations that are absent from active shortlist/intake/pricing CSVs.
- Identify recommendations where no product card exists.
- Identify card/shortlist mismatches:
  - CSV row without a corresponding card
  - card without an active row
  - card and row disagree on track/pathway, GPU/VRAM, price, seller, stock, or URL
- Phase 1 must produce the missed-or-underutilized recommendation set before
  Phase 2 begins. If none are found, explicitly state `None found` with evidence
  limitations.

Phase 2) Additional options discovery:
- Only after Phase 1 is complete, search for net-new options not already covered
  by ChatGPT export recommendations, active CSV rows, or product cards.
- Keep Phase 2 findings explicitly separated from Phase 1 recovery findings.
- Use live AU web evidence only for freshness and gap-filling.

Classification definitions:
- `Missing`: no corresponding product card exists in `cards/`, including subfolders
  such as `cards/laptops/`, `cards/desktops/`, `cards/components/`,
  `cards/mini_pcs/`, or `cards/apple_silicon/`.
- `Underutilized`: a product card exists in `cards/`, but the item is absent from
  active shortlist/intake/pricing CSVs, or present but not mapped to the correct
  track/pathway and therefore not actively considered.
- `Stale`: the candidate exists, but decision-critical price, stock, warranty,
  URL, thermal, VRAM, memory, or seller-risk evidence is old, conflicting, or
  marked `UNKNOWN`.
- `Not material`: a duplicate or weaker variant that does not change the decision
  queue after deduplication.

Evidence and provenance rules:
- Separate observed facts from inference.
- Keep source conflicts; do not collapse them silently.
- Prefer credible AU sources for current price and stock.
- For Track 1A secondary-market candidates, label asking-price evidence separately
  from sold-listing or verified-clearance evidence.
- When live price appears higher than prior verified price, do not mark over-cap
  based on one retailer alone. Flag the need for cross-checking at least two other
  AU retailers using repository policy source priority.
- Every material candidate must include provenance:
  - `source_type`: `ChatGPT-Export`, `Repo`, `Repomix`, `Web`, or combined labels
  - `conversation_id`: exact value or `UNKNOWN`
  - `conversation_title`: exact value or `UNKNOWN`
  - `message_timestamp`: exact value or `UNKNOWN`
  - `source_file`: attached filename or `UNKNOWN`
  - `source_quote_or_summary`: short non-verbatim summary of why the candidate was
    recommended

Deduplication rules:
- Deduplicate repeated recommendations across conversations using normalized
  candidate signature:
  `brand + model_family + GPU/SoC + VRAM/unified_memory + form_factor`.
- Preserve distinct variants when materially different:
  - RTX 4080 12GB vs RTX 4090 16GB
  - RTX 5070 8GB vs RTX 5070 Ti 12GB
  - new vs refurbished/open-box/used
  - AU stock vs import-only stock
  - materially different warranty or seller-risk path
- Merge duplicates only when the hardware tier, seller-risk posture, and decision
  implication are materially the same.

Required focus:
- Prioritize candidates with strong compute headroom and plausible in-budget
  posture.
- Surface viable older/high-VRAM opportunities such as RTX 3090 24GB desktops and
  RTX 4090 16GB laptops if they may change the buy-now decision.
- Surface Strix Halo/Ryzen AI Max options only when the SoC is actually verified
  or the verification task is clearly stated.
- Explicitly call out unresolved facts that may be hiding GOOD_ENOUGH Track 1
  candidates.

Suggested target sweep list - guidance only; verify each listing live:
- RTX 4090 Laptop 16 GB
- RTX 4080 Laptop 12 GB
- RTX 3080 Ti Laptop 16 GB
- RTX 3080 Laptop 16 GB, config-specific
- RTX 5070 Ti Laptop 12 GB
- RTX 5070 Laptop 12 GB, variant-specific
- RTX 5090 Laptop 24 GB
- RTX 5080 Laptop 16 GB
- RTX 5000 Ada Laptop 16 GB
- RTX 4000 Ada Laptop 12 GB
- RTX 3500 Ada Laptop 12 GB
- Radeon RX 7900M 16 GB
- Ryzen AI Max / Ryzen AI Max+ Strix Halo laptops with 32 GB+ unified memory
- Refurbished RTX 3090 24 GB single-GPU desktops only when Track 1 appears weak
  or value is clearly superior

High-value pass ordering:
1) Prior ChatGPT recommendations that are absent from cards and active CSVs
2) Prior ChatGPT recommendations with a card but no active shortlist row
3) Prior ChatGPT recommendations with stale price/stock/warranty/seller data
4) RTX 4090 16 GB laptops
5) RTX 4080 12 GB laptops
6) RTX 3080 Ti 16 GB laptops
7) RX 7900M 16 GB laptops
8) RTX 5000 Ada 16 GB workstation laptops
9) Strix Halo 64 GB+ unified-memory laptops
10) RTX 3090 24 GB single-GPU refurb desktop alternatives

Search pattern hints:
- `<gpu model> laptop used refurbished Australia`
- `<gpu model> laptop 16GB Australia`
- `<gpu model> 12GB site:.au`
- `<model name> refurbished Australia warranty`
- `<candidate> eBay Australia sold listings`
- `<candidate> thermal throttling review sustained load`

Do not do:
- Do not create card content.
- Do not assign or recompute MCDA factor scores.
- Do not provide file patch instructions.
- Do not recommend a purchase.
- Do not bury Phase 1 recovery findings behind net-new web discoveries.
- Do not rely on Repomix XML alone when an attached source file provides a more
  direct value.

Output contract:
Return a preflight attachment inventory followed by sections A-G in the exact
order below.

Preflight. Attachment Inventory
Columns exactly:
`File | Classification | Used For | Gaps/Limitations`

A. Current Blind Spots
Columns exactly:
`Phase | Candidate | Classification | Track/Pathway | Why Potentially High-Upside | Budget Posture | Evidence Strength | Notes`
- `Phase` must be `Phase1-Missed`, `Phase1-Underutilized`, `Phase1-Stale`, or
  `Phase2-New`.
- `Classification` must be `Missing`, `Underutilized`, `Stale`, or `Not material`.

B. Priority Opportunity Queue
- Rank opportunities with priority labels `P1`, `P2`, `P3`.
- Put Phase 1 recovery candidates ahead of Phase 2 net-new candidates when upside
  is similar.
- Do not include `Not material` items unless they explain a discarded duplicate.

C. Verification Tasks for Central IDE Agent
- For each P1/P2, list exact facts to verify:
  - price
  - stock
  - URL
  - VRAM or unified memory
  - screen size when pathway-relevant
  - seller/source platform
  - seller class and seller risk
  - warranty months and ACL coverage
  - sustained thermal risk
  - secondary-market sold/clearance evidence when applicable

D. Conflicts and Unknowns
- List source disagreements and decision-critical `UNKNOWN` values.
- Include provisional preferred value and reason.
- If a conflict involves Repomix, state which source file should be checked next.

E. Suggested Track/Pathway Rechecks
- One line per candidate:
  - keep current track/pathway
  - reclassify track/pathway
  - escalate to track exception review
- Include a concise reason tied to policy gates or missing evidence.

F. Dedup Log
Use labels exactly:
- `Merged opportunity`
- `Kept separate with reason`
- `Discarded as non-material duplicate`

G. Central IDE Handoff
- Output as JSONL only, one object per opportunity.
- Use stable keys only:
  - `candidate`
  - `phase`
  - `classification`
  - `track_pathway`
  - `priority`
  - `why_high_upside`
  - `budget_posture`
  - `evidence_strength`
  - `verification_tasks`
  - `conflicts`
  - `recommended_action`
  - `source_type`
  - `normalized_signature`
  - `existing_intake_id`
  - `existing_item_name`
  - `existing_card_path`
  - `existing_csv_row_status`
  - `conversation_id`
  - `conversation_title`
  - `message_timestamp`
  - `source_file`
  - `source_quote_or_summary`
  - `observed_url`
  - `observed_price_aud`
  - `observed_retailer_or_seller`
  - `evidence_date`
  - `next_repo_action`
- Keep values concise and directly actionable.
- Do not add narrative outside the JSONL objects.

Final self-check before answering:
- Sections A-G are present and ordered.
- Phase 1 recovery is separated from Phase 2 discovery.
- Each candidate has provenance.
- Unknown values remain `UNKNOWN`.
- No MCDA scores, card drafts, file patches, or purchase recommendations are present.
```
