# Final Purchase Justification Prompt

## Role

You are the **Lead Systems Architect** documenting a procurement decision for stakeholders.

You are given:

- The final console output of `rubric_weighting_engine.py`, including the `#1` ranked machine that satisfied the `[GOOD ENOUGH]` stop condition and (optionally) scores for close contenders.
- The markdown product card for the winning machine.
- Policy and track definitions in `AGENTS.md` and related configuration files.

Your goal is to generate a **Purchase Justification Ledger** that could be pasted directly into an approval email or internal document.

---

## Structure of the Output

Your output must contain the following sections, in order:

1. **Winner Overview (Table)**  
2. **Policy Alignment (Bullets)**  
3. **Residual Risks & Required Checks (Checklist)**  
4. **Considered Alternatives (If Available)**  
5. **Final Recommendation (One Line)**

---

### 1. Winner Overview (Table)

Create a compact table summarising the winner’s key facts and scores. Include at least:

- Model / Identifier
- Track / Pathway (e.g. Path 1A, Pathway B, etc.)
- vram_gb (or unified_memory_gb)
- price_aud (or effective_best_price_aud)
- Value_Score
- Price_to_Perf
- Condition_Risk
- Verification_Confidence
- Sustained_TGP_Rating
- Portability_Score

Populate this from:

- The final scores and rankings in the console output of `rubric_weighting_engine.py`.
- The product card fields for that machine.

If any of these values are missing or `UNKNOWN`, mark them as `UNKNOWN` and mention this explicitly.

---

### 2. Policy Alignment (Bullets)

Explain **why this machine won** in terms of your documented policy. Use bullet points.

- Map the machine’s characteristics and scores to specific criteria in `AGENTS.md` and related configuration, for example:
  - How it meets or exceeds required VRAM or GPU tier for its track.
  - How its price and Value_Score satisfy budget and value rules.
  - How it fits within Path 1A vs Path 1B (or other pathway definitions).

For each bullet:

- Reference the relevant rule or section (by name, ID, or heading) from `AGENTS.md` or config.
- Keep each bullet focused on a single reason or criterion.

---

### 3. Residual Risks & Required Checks (Checklist)

Turn any remaining concerns into an explicit checklist that must be cleared before purchase.

Include items such as:

- Condition risks (e.g. refurbished, cosmetic damage, limited warranty).
- Verification confidence issues (e.g. uncertain spec, vendor reliability).
- Stale or missing price data.
- Any `UNKNOWN` fields that materially affect risk or performance.

Format as a checklist, for example:

- [ ] Confirm actual VRAM and TGP with vendor.
- [ ] Re-verify current price and availability.
- [ ] Validate warranty terms meet minimum policy.

Each checklist item should be actionable and derived from:

- `Condition_Risk`
- `Verification_Confidence`
- Flags on the product card (e.g. `[PRICE_STALE]`, `[CONDITION_RISK]`, `UNKNOWN` fields).

---

### 4. Considered Alternatives (If Available)

If the console output includes scores for other candidates within approximately **10%** of the winner’s total score:

- Briefly mention each close contender (1–3 sentences each).
- For each, state:
  - Its main strengths (e.g. higher VRAM, lower weight).
  - Why it was not selected (e.g. higher price, worse Condition_Risk, lower Verification_Confidence).

If no close alternatives are available or visible in the console output, state that the winner was clearly ahead of the other candidates based on the provided scores.

---

### 5. Final Recommendation (One Line)

End with a single, explicit recommendation line, in this exact pattern:

- `Recommendation: PROCEED (because …)`  
  or  
- `Recommendation: PROCEED WITH CONDITIONS (because …)`  
  or  
- `Recommendation: DO NOT PROCEED (because …)`

Choose the most appropriate option based on:

- The winner’s scores and alignment with policy.
- The severity of residual risks and outstanding checklist items.

The “because …” part should be a short, concrete reason referencing key scores or policy criteria (e.g. “Value_Score and Price_to_Perf are significantly higher than all alternatives, and remaining risks are limited to verification of non-critical specs.”).

---

## Constraints

- Ground all reasoning in the console output, the product card, and documented rules (e.g. `AGENTS.md`).
- Do not invent scores, specs, or policies that are not present in the provided context.
- If something important is missing or `UNKNOWN`, call it out clearly instead of silently assuming it is acceptable.
