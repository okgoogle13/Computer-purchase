# TASKS.md — Hardware Procurement Pipeline

> **Model routing key:**
> - `[CLAUDE-HAIKU]` — grep, card reads, CSV search, policy filtering
> - `[CLAUDE-SONNET]` — MCDA scoring, price cross-checks, final recommendation, escalation
> - `[GEMINI-FLASH-LOW]` — mechanical matching tasks, no reasoning needed (thinkingBudget: 0)
> - `[GEMINI-FLASH-MEDIUM]` — moderate reasoning, edge-case classification (thinkingBudget: 1024)
> - `[GEMINI-FLASH-HIGH]` — complex multi-source analysis within Gemini (thinkingBudget: 8192)
>
> Current shortlist: `shortlists/2026-06-08_shortlist_pricing_enriched_live.csv`
> Current ranked output: `shortlists/2026-06-08_ranked_final.csv`

---

## Stage 1 — Active / Blocked

### [x] Phase 1 Card Coverage Audit
**Model:** `[GEMINI-FLASH-LOW]` (mechanical shortlist ↔ card cross-reference)
**Command:**
```bash
python scripts/run_gemini_card_audit.py \
  --shortlist shortlists/2026-06-08_shortlist_pricing_enriched_live.csv \
  --thinking low \
  --output output/card_audit_phase1.json
```
**Done when:** `output/card_audit_phase1.json` exists with `phase1_findings` array. Pass to Phase 2.

---

### [ ] Phase 2 Opportunity Discovery (Cross-Platform Prompt)
**Model:** `[CLAUDE-SONNET]` — uses Phase 1 JSON as input, no card reads
**Skill:** `gemini-card-audit` (intercepts Phase 1), then `cross_platform_prompt_claude.md` Phase 2
**Done when:** Sections A–G complete. New candidates listed in Section B.

---

### [ ] Live Pricing Verification — Top 10 Candidates
**Model:** `[GEMINI-FLASH-LOW]` via `fill_shortlist_live_pricing.py`
**Command:**
```bash
python scripts/fill_shortlist_live_pricing.py \
  shortlists/2026-06-08_shortlist_pricing_enriched.csv
```
**Done when:** `current_best_price_aud`, `in_stock_now`, `current_best_url` filled for top 10 rows (by Adjusted_MCDA_Total).

---

### [ ] Confirm MCDA Scores — Top 10 Candidates
**Model:** `[CLAUDE-SONNET]`
**Command:**
```bash
python scripts/scoring/rubric_weighting_engine.py \
  --csv shortlists/2026-06-08_shortlist_pricing_enriched_live.csv \
  --output-csv shortlists/2026-06-08_ranked_final.csv
```
**Done when:** All 5 MCDA factor scores filled for top 10 (by Adjusted_MCDA_Total); `MCDA_Total` computed for each.

---

### [ ] Final Purchase Recommendation
**Model:** `[CLAUDE-SONNET]`
**Prompt:** `scripts/prompt_templates/final_purchase_justification_prompt.md`
**Done when:** Recommendation includes all fields from CLAUDE.md Pre-Decision Checklist. Clear buy/wait/no verdict.

---

## Stage 2 — Secondary Market Sweep (if Stage 1 price misses)

### [ ] eBay / Facebook Secondary-Market Scan
**Model:** `[GEMINI-FLASH-MEDIUM]` via `run_gemini_card_audit.py --thinking medium`
**Skill:** `gaming-laptop-private-sale` or `refurb-workstation-au`
**Scope:** RTX 4090 16GB, RTX 3080 Ti 16GB, RTX 5000 Ada 16GB AU listings

---

### [ ] Opportunity Gap Analysis
**Model:** `[GEMINI-FLASH-MEDIUM]`
**Command:**
```bash
python scripts/run_gemini_card_audit.py \
  --shortlist shortlists/2026-06-08_shortlist_pricing_enriched_live.csv \
  --thinking medium \
  --output output/card_audit_gap_analysis.json
```
**Done when:** All P1/P2 items from Section B verified or dismissed with evidence.

---

## Stage 3 — Intake of New Candidates (if gap analysis surfaces new units)

### [ ] Normalize and Card New Candidates
**Model:** `[CLAUDE-HAIKU]`
**Commands:**
```bash
python scripts/normalize_intake.py NotebookLM_Workspaces/intake/raw/YYYY-MM-DD_batch.csv
python scripts/intake_to_cards.py NotebookLM_Workspaces/intake/processed/YYYY-MM-DD_batch_processed.csv --overwrite
```

### [ ] Rebuild Shortlist with New Cards
**Model:** `[CLAUDE-HAIKU]`
**Command:**
```bash
python scripts/build_shortlist.py
```

---

## Pipeline Integrity Checks (run after any shortlist/ranking change)

**Model:** `[CLAUDE-HAIKU]`
```bash
python scripts/policy_drift_check.py
python scripts/pipeline_integrity_check.py \
  --enriched shortlists/2026-06-08_shortlist_pricing_enriched_live.csv \
  --ranked shortlists/2026-06-08_ranked_final.csv
```

---

## Completed

- [x] Shortlist built: `2026-06-08_shortlist.csv` (64 rows)
- [x] Pricing scaffold: `2026-06-08_shortlist_pricing_enriched.csv`
- [x] MCDA gaps filled: `2026-06-08_shortlist_mcda_filled.csv`
- [x] Live pricing fill: `2026-06-08_shortlist_pricing_enriched_live.csv`
- [x] Ranked output: `2026-06-08_ranked_final.csv`
- [x] Gemini Flash card audit script: `scripts/run_gemini_card_audit.py`
- [x] Gemini card audit skill: `.claude/skills/gemini-card-audit/`
- [x] CLAUDE.md routing table updated with Gemini Flash tier
