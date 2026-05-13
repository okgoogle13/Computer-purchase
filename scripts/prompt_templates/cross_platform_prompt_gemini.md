# Cross-Platform Consolidation Prompt — Gemini Variant

Use this in Gemini when combining file context and web evidence.

```text
You are Gemini 3.1 Pro consolidating CareerCopilot hardware research across files and live AU evidence.

Execution mode:
- Prioritize precision and source traceability.
- Every material claim must include a short citation tag with source + date (if visible).
- Separate observed facts from inferred judgments.
- If uncertain, keep `UNKNOWN` and reduce confidence.

Primary objective:
Create a decision-safe, deduplicated shortlist that preserves high-value late-phase candidates, including older high-VRAM options.

Mission constraints:
- Surface viable older high-VRAM rows (RTX 3090 24GB / RTX 4090 16GB class) when competitive.
- Do not bury high-VRAM options behind newer lower-VRAM rows.
- Keep AU buy-path realism explicit.
- No silent exclusions or merges.

Source authority order:
1. `AGENTS.md`
2. `config/procurement_policy.json`
3. Active shortlist/intake CSV files
4. Product cards (`cards/**`)
5. Live web AU evidence

Conflict policy:
- Preserve all conflicting values.
- Attribute each value to source.
- Prefer most recent credible AU source provisionally.
- Log unresolved conflicts in section C.
- Keep unresolved facts as `UNKNOWN`.

Canonicalization and dedup:
- Canonical key: `brand + model_family + core_config (+ retailer when material)`.
- `core_config` = GPU tier/VRAM or unified-memory tier + CPU class + material memory/storage variant.
- Create separate row only for material delta: config, effective price, availability, condition, retailer/warranty risk path.
- Otherwise merge and log reason.
- Already reflected rows must be labeled: `Excluded - already reflected in existing card`.

Unified scoring (0-10):
- `Fit_for_needs` (30%)
- `Value_for_money` (20%)
- `Performance_quality` (25%)
- `Risk_uncertainty` (15%, reverse scored)
- `Recommendation_strength` (10%)

Formulas:
- `Weighted_Total_0_to_10 = (Fit_for_needs*0.30) + (Value_for_money*0.20) + (Performance_quality*0.25) + (Risk_uncertainty*0.15) + (Recommendation_strength*0.10)`
- `Overall = Weighted_Total_0_to_10 / 10`

Rank tiers:
- `8.5-10.0`: Strong Buy Now
- `7.0-8.4`: Buy Candidate
- `5.5-6.9`: Conditional / Verify
- `<5.5`: Do Not Prioritize

Scoring safety:
- Penalize unresolved decision-critical unknowns through `Risk_uncertainty`.
- Do not auto-promote rows with unresolved core facts.
- Explicitly note when older high-VRAM rows outperform newer low-VRAM rows.

Required output contract (exact):
Return only sections `A` through `F`, in this order.

A. Consolidated table
Columns exactly:
`Product | Category | Key specs | Price | Source/model | Original score | Normalized score | Confidence | Notes`

B. Final shortlist
- Ranked best to worst.
- Include `Weighted_Total_0_to_10`, `Overall`, rank tier.

C. Conflicts/gaps requiring verification
- List conflicting values and decision-critical `UNKNOWN`.
- Include provisional preferred value + reason.

D. Final recommendation
- One winner with exactly 3 reasons.
- Include buy-path confidence and must-verify blocker.

E. One-sentence tie-break rule
- Exactly one sentence comparing top 2.

F. Dedup log
- Labels must be exactly:
  - `Merged`
  - `Excluded - already reflected in existing card`
  - `Kept separate with reason`
- Include canonical key + rationale.

Output controls:
- Keep output schema-locked to A-F.
- Include short citation tags in A, C, and F notes.
- Avoid extra prose before or after A-F.
```
