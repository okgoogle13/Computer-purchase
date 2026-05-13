# Cross-Platform Research Core Prompt (Shared Logic)

Use this as the canonical instruction set for multi-LLM hardware research consolidation.

## Operating Goal
Produce a decision-safe, deduplicated shortlist for CareerCopilot procurement.

Late-phase priority:
- Surface older high-VRAM options (for example RTX 3090 24GB, RTX 4090 16GB) when still viable.
- Do not bury high-VRAM options behind newer lower-VRAM alternatives.
- Keep AU buy-path realism explicit.

Non-negotiables:
- No silent row drops.
- Keep unresolved facts as `UNKNOWN`.
- Distinguish observed facts from inference.

## Source Authority Order
Use sources in this order:
1. `AGENTS.md`
2. `config/procurement_policy.json`
3. Active shortlist/intake CSV files
4. Product cards (`cards/**`)
5. Live web evidence for AU price/stock/specs/warranty/thermal risk

Conflict handling:
- Preserve conflicting values side by side.
- Attribute each value to its source.
- Prefer most recent credible AU source for provisional ranking.
- Log all conflicts in section C.

## Candidate Extraction and Canonicalization
Canonical key:
- `brand + model_family + core_config (+ retailer when material)`

`core_config` includes:
- GPU tier + VRAM or unified-memory tier
- CPU class
- memory/storage variant when it changes purchase value

Create separate rows only for material deltas:
- config
- retailer/warranty path
- effective price
- availability
- condition

Otherwise merge into canonical row and record merge rationale in section F.

## Dedup and Exclusion Rules
- If item already exists in an equivalent canonical row, use:
  - `Excluded - already reflected in existing card`
- Never exclude without an explicit log entry.
- Every merge/exclusion decision must appear in section F.

## Unified Scoring and Normalization
Normalize all legacy scoring to 0-10 using:
- `Fit_for_needs` (30%)
- `Value_for_money` (20%)
- `Performance_quality` (25%)
- `Risk_uncertainty` (15%, reverse scored: lower risk -> higher score)
- `Recommendation_strength` (10%)

Formula:
- `Weighted_Total_0_to_10 = (Fit_for_needs*0.30) + (Value_for_money*0.20) + (Performance_quality*0.25) + (Risk_uncertainty*0.15) + (Recommendation_strength*0.10)`
- `Overall = Weighted_Total_0_to_10 / 10`

Rank tiers:
- `8.5-10.0`: Strong Buy Now
- `7.0-8.4`: Buy Candidate
- `5.5-6.9`: Conditional / Verify
- `<5.5`: Do Not Prioritize

Scoring safety:
- Penalize unresolved decision-critical unknowns through `Risk_uncertainty`.
- Do not auto-promote rows with unresolved price/stock/spec basics.
- Call out where older high-VRAM rows outperform newer low-VRAM rows.

## Required Output Contract (A-F, exact)
Return sections `A` to `F` only, in this exact order.

### A. Consolidated table
Columns exactly:
`Product | Category | Key specs | Price | Source/model | Original score | Normalized score | Confidence | Notes`

### B. Final shortlist
- Ranked best to worst.
- Include `Weighted_Total_0_to_10`, `Overall`, and rank tier.

### C. Conflicts/gaps requiring verification
- List conflicts and decision-critical `UNKNOWN` fields.
- For each conflict, name provisional preferred value and why.

### D. Final recommendation
- One winner with exactly 3 reasons.
- Include buy-path confidence and must-verify blocker.

### E. One-sentence tie-break rule
- One sentence comparing top 2.

### F. Dedup log
Use one of:
- `Merged`
- `Excluded - already reflected in existing card`
- `Kept separate with reason`

Each entry must include canonical key and rationale.

## Final Self-Check
- High-VRAM late-phase candidates were not suppressed.
- No silent exclusions.
- Every retained row has normalized score.
- Every merge/exclusion appears in F.
- Output includes only A-F.
