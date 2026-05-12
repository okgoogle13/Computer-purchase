# CareerCopilot Hardware Prompt-Chain and Superpowers Orchestration

## Superpowers Execution Order
1. `superpowers:using-superpowers`
2. `superpowers:writing-plans`
3. `superpowers:dispatching-parallel-agents`
4. `superpowers:subagent-driven-development`
5. `superpowers:verification-before-completion`
6. Optional: `superpowers:systematic-debugging`

## Parallel Agent Split
- Agent A: audit + pre-scoring validation (`audit_checklist_prompt.md`, `pre_scoring_validation_prompt.md`)
- Agent B: pricing lookups + source/seller risk evidence (`browser_pricing_lookup.md`)
- Agent C: scoring prep consistency checks (no score generation before gate pass)

## Deterministic Prompt Chain
1. `scripts/prompt_templates/notebooklm_system_prompt.md`
2. `scripts/prompt_templates/audit_checklist_prompt.md`
3. `scripts/prompt_templates/pre_scoring_validation_prompt.md`
4. `scripts/prompt_templates/browser_pricing_lookup.md`
5. `scripts/prompt_templates/track1_card_shortlist_sync_prompt.md`
6. `scripts/prompt_templates/ai_scoring_execution_prompt.md`
7. `scripts/prompt_templates/final_purchase_justification_prompt.md`

## Script Chain
1. `python scripts/policy_drift_check.py`
2. `python scripts/build_shortlist.py`
3. `python scripts/enrich_shortlist_pricing.py <shortlist.csv>`
4. Fill live pricing from browser-agent outputs (`UNKNOWN` when unresolved)
5. Fill the five MCDA factor columns only
6. `python scripts/scoring/rubric_weighting_engine.py --csv <..._pricing_enriched_live.csv> --output-csv <..._ranked.csv>`
7. Generate final decision memo with `final_purchase_justification_prompt.md`

## Guardrails
- Never infer price/stock/warranty/VRAM/thermals.
- Keep unresolved values as `UNKNOWN`.
- Enforce AU source/seller enums exactly as prompt contracts specify.
- Respect Strix Halo score caps unless benchmark evidence exists.
- If Track 2 overrides Track 1, cite escalation exception explicitly.
