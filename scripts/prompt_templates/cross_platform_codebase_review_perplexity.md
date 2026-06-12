# Codebase Review Prompt — Perplexity Variant

> **Scope:** Review of the procurement decision-system codebase, **not** market/opportunity discovery.
> For live AU market research, use [`cross_platform_prompt_perplexity.md`](cross_platform_prompt_perplexity.md) instead.
>
> Perplexity does not have repository access. The full code context is pasted from the
> repomix pack `scratch/procurement_context_pack.xml`, regenerated with:
>
> ```bash
> repomix --style xml --output scratch/procurement_context_pack.xml \
>   --include "AGENTS.md,CLAUDE.md,README.md,TASKS.md,config/*.json,scripts/build_shortlist*.py,scripts/scoring/*.py,scripts/policy_drift_check.py,scripts/pipeline_integrity_check.py,scripts/run_automated_pipeline.py,scripts/enrich_shortlist_pricing.py,scripts/fill_shortlist_live_pricing.py,scripts/fill_mcda_gaps.py,scripts/normalize_intake.py,scripts/intake_to_cards.py"
> ```

---

## Context (paste the repomix pack here)

```
<<< PASTE THE ENTIRE CONTENTS OF scratch/procurement_context_pack.xml HERE >>>
```

The pack contains 24 files (~54k tokens): the canonical policy docs (`AGENTS.md`,
`CLAUDE.md`, `README.md`, `TASKS.md`), all three config schemas (`config/*.json`), the
six `build_shortlist*` modules, the three `scoring/` modules (rubric engine, auto-scorer,
ranking feedback loop), and the integrity/pipeline scripts. Treat the pack as read-only
ground truth — do not invent files that are not present.

## Project Background

This is an AI-assisted hardware-procurement decision system. A 5-phase pipeline runs
**intake → shortlist → live pricing → manual MCDA scoring → ranked recommendation** to
select one Track 1 laptop (outcome-enabled, AU-available, ≤5,000 AUD, no disqualifying
thermal risk). Policy authority is strictly ordered:
`AGENTS.md` > `config/procurement_policy.json` > CSV ledger > cards > live sources.

## Review Task

Perform a rigorous engineering review of the included code. Organise findings into the
sections below. For every finding, cite the **exact file and the relevant
function/line region**, state severity, and give a concrete fix — not a vague suggestion.

### A. Policy & Config Consistency
- Do `procurement_policy.json`, `search_archetypes.json`, and `shortlist_schema.json`
  agree with each other and with the rules narrated in `AGENTS.md`/`CLAUDE.md`?
- Flag any budget cap, VRAM floor, track gate, or source-priority constant that is
  duplicated in code instead of read from config (drift risk).
- Does `policy_drift_check.py` actually detect the drift it claims to? Name any gap.

### B. Correctness of the Scoring Engine
- Audit `scripts/scoring/rubric_weighting_engine.py`: weight normalisation, missing-data
  handling, tie-breaking, and the MCDA formula. Do weights sum as intended? What happens
  on null/NaN criteria values?
- Cross-check `auto_score_cards.py` and `ranking_feedback_loop.py` for scoring logic that
  contradicts the rubric engine.

### C. Pipeline Integrity & Data Flow
- Trace a row from `normalize_intake.py` → `intake_to_cards.py` → `build_shortlist*.py`
  → `enrich_shortlist_pricing.py` → `fill_shortlist_live_pricing.py` → `fill_mcda_gaps.py`
  → scoring. Where can a column be silently dropped, renamed, or type-coerced wrongly?
- Does `pipeline_integrity_check.py` cover the failure modes you identify? List gaps.

### D. Robustness & Error Handling
- Unhandled exceptions, bare `except`, silent failures, missing-file / empty-CSV paths,
  and any place a live-pricing or web step can hang or corrupt the working CSV.
- `run_automated_pipeline.py` orchestration: does a mid-pipeline failure leave a coherent
  state, or a half-written shortlist?

### E. Maintainability & Duplication
- The six `build_shortlist*` modules — quantify shared logic that should be factored into
  a common helper. Note divergence between them that looks accidental rather than intended.

### F. Security & Data Hygiene
- Any secrets, tokens, cookies, or PII committed in config/code. Unsafe subprocess/shell
  use, unvalidated paths, or injection surfaces in the scraping/pricing steps.

## Output Contract

Return all sections **A–F**. Each finding: `severity (Critical/High/Medium/Low)` ·
`file:region` · `problem` · `fix`. End with a **prioritised top-5 action list**.
Tag each claim with confidence `High` / `Medium` / `Low`. If a section has no findings,
say so explicitly rather than omitting it. Do not propose changes to files absent from
the pack; if a fix depends on an unseen file, flag the dependency instead.
