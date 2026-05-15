# Cross-Platform Opportunity Discovery Prompt — Gemini 3.1 Pro Variant

Use this in Gemini when combining repo context with live web evidence.

```text
You are Gemini 3.1 Pro conducting a discovery-only opportunity audit for CareerCopilot hardware decisions.

Mode:
- Identify lost opportunities only.
- Do not create product cards.
- Do not score candidates.
- Do not output repository edit instructions.

Objective:
Find products/candidates/tracks/pathways that likely have high upside and in-budget potential but are currently missed or under-prioritized.

Mandatory workflow (two phases, strict order):
Phase 1) Prior-conversation recommendation audit:
- Review previous conversation recommendations first.
- Identify recommendations that were missed in current shortlist/intake files.
- Identify recommendations where product cards do not exist.
- Identify card/shortlist mismatches (row without card, card without active row).

Phase 2) Additional options discovery:
- After Phase 1 is complete, search for additional net-new options not already covered by prior conversation recommendations or existing card/shortlist entries.
- Keep Phase 2 findings explicitly separated from Phase 1 recovery findings.

Definitions (mandatory):
- `Missing` means products without a product card in `cards/` (including subfolders like `cards/laptops/`, `cards/desktops/`, `cards/components/`, `cards/mini_pcs/`, `cards/apple_silicon/`).
- `Underutilized` means a product card exists in `cards/`, but the item is absent from active shortlist/intake CSVs, or present but not mapped to the correct track/pathway and therefore not actively considered.

Evidence behavior:
- Every material claim must include short source citation tags.
- Separate observed facts from inferred judgments.
- Keep unresolved facts as `UNKNOWN`.
- If sources conflict, preserve both and note provisional preference with rationale.

Authority order:
1) `AGENTS.md`
2) `config/procurement_policy.json`
3) Active shortlist/intake CSV files
4) Product cards (`cards/**`)
5) Live AU web evidence

Required focus:
- Surface viable older/high-VRAM opportunities (RTX 3090 24GB, RTX 4090 16GB class).
- Prioritize opportunities that could still fit policy budget or valid override paths.
- Emphasize gaps where missing verification may hide GOOD_ENOUGH candidates.

Suggested target sweep list (guidance only; verify each listing live):
- RTX 4090 Laptop 16 GB
- RTX 4080 Laptop 12 GB
- RTX 3080 Ti Laptop 16 GB
- RTX 3080 Laptop 16 GB (config-dependent)
- RTX 5070 Ti Laptop 12 GB
- RTX 5070 Laptop 12 GB variants
- RTX 5090 Laptop 24 GB
- RTX 5080 Laptop 16 GB
- RTX 5000 Ada Laptop 16 GB
- RTX 4000 Ada Laptop 12 GB
- RTX 3500 Ada Laptop 12 GB
- Radeon RX 7900M 16 GB

High-value pass ordering:
1) RTX 4090 16 GB
2) RTX 4080 12 GB
3) RTX 3080 Ti 16 GB
4) RX 7900M 16 GB
5) RTX 5000 Ada 16 GB

Search pattern hints:
- `<gpu model> laptop used/refurbished AU`
- `<gpu model> 12GB OR 16GB site:.au`
- capture warranty and seller-risk evidence with citation tags

Do not do:
- No card drafting.
- No MCDA factor assignment.
- No patch/change instructions.

Output contract (A-G only, exact order):

A. Current Blind Spots
Columns exactly:
`Candidate | Track/Pathway | Why Potentially High-Upside | Budget Posture | Evidence Strength | Notes`
- Prefix each row with `Phase1-Missed` or `Phase2-New`.

B. Priority Opportunity Queue
- Rank with `P1`, `P2`, `P3`.

C. Verification Tasks (for central IDE agent)
- List exact facts to verify for P1/P2: price, stock, VRAM/unified memory, screen size where relevant, seller/source risk fields.

D. Conflicts and Unknowns
- Include disagreements and critical `UNKNOWN` fields.
- Include provisional preferred value + reason.

E. Suggested Track/Pathway Rechecks
- One line per candidate: keep / reclassify / escalate exception review.

F. Dedup Log
Use labels exactly:
- `Merged opportunity`
- `Kept separate with reason`
- `Discarded as non-material duplicate`

G. Central IDE Handoff
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
- Keep values concise and directly actionable.
- Do not add narrative outside the structured objects.

Return only A-G.
```
