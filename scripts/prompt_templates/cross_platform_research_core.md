# Cross-Platform Opportunity Discovery Core Prompt (Shared Logic)

Use this as the canonical instruction set for multi-LLM opportunity discovery.

## Operating Goal
Identify lost opportunities only:
- products/candidates/tracks/pathways that were missed, deprioritized, or excluded
- but appear likely to be high-upside and within policy budget

This is discovery-only work. Do not create product cards. Do not score candidates.

## Mandatory Two-Phase Workflow
Run in this exact order:

### Phase 1: Prior-Conversation Coverage Audit
Review prior conversation artifacts and recommendation logs first. Identify:
- recommendations that were previously made but are missing from active shortlist/intake CSVs
- recommendations that exist in shortlist rows but have no corresponding product card
- product cards that exist but are detached from active shortlist rows

Phase 1 output must produce an explicit "missed or untracked recommendation set" before any new market discovery.

### Phase 2: Additional Market Discovery
Only after Phase 1, search for net-new additional options not already covered by:
- prior conversation recommendations
- active shortlist/intake rows
- existing product cards

Phase 2 must clearly separate genuinely new options from Phase 1 recovery items.

## Non-Negotiables
- No silent drops.
- Keep unresolved facts as `UNKNOWN`.
- Distinguish observed facts from inference.
- Do not propose editing repository files.
- Do not compute or assign new MCDA factor values.

## Source Authority Order
Use sources in this order:
1. `AGENTS.md`
2. `config/procurement_policy.json`
3. Active shortlist/intake CSV files
4. Product cards (`cards/**`)
5. Live web AU evidence for freshness

Conflict handling:
- Preserve conflicting values with source attribution.
- Prefer most recent credible AU source provisionally.
- Log unresolved conflicts in section D.

## Opportunity Identification Rules
Focus on candidates that satisfy all or most:
- likely policy-compliant budget posture (`<= 5,000 AUD` Track 1 cap, or explicit valid override case)
- likely strong compute headroom (for example high VRAM tiers)
- likely AU-available from credible seller paths
- likely improvement over currently selected shortlist rows

## Definitions (Mandatory)
Use these exact definitions when classifying opportunities:

- `Missing`:
  - A product/recommendation is `Missing` when no corresponding product card exists in `cards/` (including subfolders such as `cards/laptops/`, `cards/desktops/`, `cards/components/`, `cards/mini_pcs/`, `cards/apple_silicon/`).
  - Shorthand rule for prompts: "products without a product card in `cards/`".

- `Underutilized`:
  - A product/recommendation is `Underutilized` when a product card exists in `cards/` but the item is absent from active shortlist/intake CSVs, or present but not mapped to the correct track/pathway and therefore not being actively considered.

Late-phase priority:
- surface viable older/high-VRAM options (for example RTX 3090 24GB, RTX 4090 16GB)
- do not bury them behind newer lower-VRAM rows

## Dedup and Canonicalization
Canonical key:
- `brand + model_family + core_config (+ retailer when material)`

Treat as separate opportunities only when there is a material delta:
- config tier
- effective price
- stock status
- warranty/seller risk path

Otherwise merge into one opportunity and note merge rationale in section F.

## Output Contract (A-G, exact)
Return sections `A` through `G` only, in this order.

### A. Current Blind Spots
Columns exactly:
`Candidate | Track/Pathway | Why Potentially High-Upside | Budget Posture | Evidence Strength | Notes`
- Prefix each row with `Phase1-Missed` or `Phase2-New`.

### B. Priority Opportunity Queue
- Ranked highest-to-lowest opportunity to investigate next.
- Include `Priority` label: `P1`, `P2`, `P3`.

### C. Verification Tasks (for central IDE agent)
- For each P1/P2 opportunity, list exact facts to verify:
  - price
  - stock
  - VRAM/unified memory
  - screen size (if pathway-relevant)
  - seller/source risk fields

### D. Conflicts and Unknowns
- List source disagreements and decision-critical `UNKNOWN` fields.
- Include provisional preferred value and reason.

### E. Suggested Track/Pathway Rechecks
- One-line recommendation per opportunity:
  - keep current track/pathway
  - reclassify track/pathway
  - escalate to track exception review

### F. Dedup Log
Use labels exactly:
- `Merged opportunity`
- `Kept separate with reason`
- `Discarded as non-material duplicate`

### G. Central IDE Handoff
- Output as compact JSON or JSONL.
- One object per opportunity.
- Use stable keys only:
  - `candidate`
  - `track_pathway`
  - `priority`
  - `why_high_upside`
  - `budget_posture`
  - `evidence_strength`
  - `verification_tasks`
  - `conflicts`
  - `recommended_action`
- Keep values concise and actionable.
- Do not add narrative outside the structured objects.

## Final Self-Check
- Output is discovery-only.
- No card creation instructions.
- No MCDA scoring instructions.
- No file-edit instructions.
- A-G sections complete and ordered.
