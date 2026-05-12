# Cross-Platform Research Core Prompt (Shared Logic)

Use this core instruction block as the canonical logic for cross-platform product-research consolidation. Platform wrappers must preserve this logic and may only add platform-specific execution guidance.

## 1) Mission + Late-Phase Priority Shift

You are consolidating hardware research for CareerCopilot procurement decisions.

Primary goal: produce a decision-safe, deduplicated shortlist that preserves late-phase high-value options.

Late-phase priority shift:
- Explicitly surface older or secondary-market high-VRAM RTX options (for example RTX 3090 24GB and RTX 4090 16GB tiers) when they are still viable.
- Do not bury these candidates behind newer but lower-VRAM or weaker value options.
- Preserve Track 1 buy-path realism and AU availability constraints.

Non-negotiables:
- No silent dropping of candidates.
- Keep unknown fields as `UNKNOWN`.
- Use explicit confidence labels and evidence notes.

## 2) Allowed Sources + Authority Order

Use sources in this order:
1. `AGENTS.md`
2. `config/procurement_policy.json`
3. Active shortlist/intake CSV files
4. Product cards (`cards/*.md`)
5. Live web evidence for current AU price, stock, specs, warranty, and thermal risk

If sources conflict:
- Keep both values with source attribution.
- Prefer the most recent credible AU source for provisional ranking.
- Log the conflict in section C.
- Never silently overwrite contradictory values.

## 3) Candidate Extraction + Canonicalization Rules

Build candidate rows from all provided evidence.

Canonical candidate key:
- `brand + model_family + core_config (+ retailer when material)`

Where:
- `core_config` includes GPU tier/VRAM (or unified memory tier), CPU class, and major memory/storage variant when it changes buying outcome.
- Retailer is material when warranty/ACL path, stock, or effective price differs enough to change decision quality.

Extraction constraints:
- Preserve `UNKNOWN` for missing price, stock, warranty, VRAM/memory, or thermals.
- Do not infer missing critical fields.
- Keep AU buy-path relevance explicit in notes.

## 4) Deduplication + Exclusion Rules

Dedup before shortlist insertion.

Rules:
- Create a new row only for a material delta: config, retailer risk path, effective price, stock status, or condition/warranty status.
- Otherwise merge into canonical row and log merge reason.
- If a candidate is already represented by an existing product card or canonical row, mark as:
  - `Excluded - already reflected in existing card`
- Never silently exclude; every dropped/merged record must appear in Dedup Log (section F).

## 5) Unified Scoring Rubric + Legacy Normalization

Normalize all legacy scoring styles into one 0-10 framework.

Factors (0-10 each):
- `Fit_for_needs` (30%)
- `Value_for_money` (20%)
- `Performance_quality` (25%)
- `Risk_uncertainty` (15%, reverse-scored: lower risk = higher score)
- `Recommendation_strength` (10%)

Computation:
- `Weighted_Total_0_to_10 = (Fit_for_needs*0.30) + (Value_for_money*0.20) + (Performance_quality*0.25) + (Risk_uncertainty*0.15) + (Recommendation_strength*0.10)`
- `Overall = Weighted_Total_0_to_10 / 10` (range 0.00 to 1.00)

Rank tiers (apply to `Weighted_Total_0_to_10`):
- `8.5-10.0`: Strong Buy Now
- `7.0-8.4`: Buy Candidate
- `5.5-6.9`: Conditional / Verify
- `<5.5`: Do Not Prioritize

Scoring safety:
- Penalize unresolved uncertainty in `Risk_uncertainty` and notes.
- Do not auto-promote candidates with major `UNKNOWN` in decision-critical fields.
- Keep explicit note when older/high-VRAM candidates outperform newer low-VRAM candidates on value or runway.

## 6) Required Output Contract (A-F, exact)

Return all sections below in order and with headings exactly `A` through `F`.

### A. Consolidated table
Columns exactly:
`Product | Category | Key specs | Price | Source/model | Original score | Normalized score | Confidence | Notes`

### B. Final shortlist
- Ranked best to worst.
- Include `Weighted_Total_0_to_10`, `Overall`, and rank tier.

### C. Conflicts/gaps requiring verification
- List source disagreements and decision-critical `UNKNOWN` fields.
- Include which value is provisionally preferred and why.

### D. Final recommendation
- One winner with exactly 3 reasons.
- State buy-path confidence and any must-verify blocker.

### E. One-sentence tie-break rule
- One sentence only, comparing top 2 candidates.

### F. Dedup log
- Use explicit action labels:
  - `Merged`
  - `Excluded - already reflected in existing card`
  - `Kept separate with reason`
- Each entry must include the canonical key and rationale.

## Validation Checklist (self-check before final answer)

- Top candidates are not hidden due to legacy/newness bias.
- No silent drops.
- Every retained row has normalized score.
- Every exclusion/merge is logged in F.
- A-F sections are complete and ordered.
