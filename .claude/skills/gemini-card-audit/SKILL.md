---
name: gemini-card-audit
description: Phase 1 card coverage audit — delegates mechanical shortlist ↔ card cross-reference to Gemini 3.5 Flash instead of loading all 654 cards into Claude context. Use when asked to do a coverage audit, card inventory check, Phase 1 audit, or before running cross_platform_prompt_claude.md.
---

# Gemini Card Audit

## When to Use This Skill

Use this skill (not direct card reads) whenever the task is:
- "Run the Phase 1 coverage audit"
- "Which candidates are missing cards?"
- "Check which shortlist rows have no card"
- "Run the cross-platform discovery prompt" (intercept Phase 1 here first)
- Any card inventory cross-reference against the shortlist

Do NOT use this skill for MCDA scoring, final recommendations, or price checks — those stay in Claude.

## Steps

### Step 1 — Identify the active shortlist

Check which shortlist CSV is the most recent live-priced file:

```bash
ls -t shortlists/*_live.csv | head -3
```

Use `shortlists/shortlist_profile-laptop_pricing_enriched_live.csv` by default unless a more recent file exists.

### Step 2 — Run the Gemini audit script

```bash
python scripts/run_gemini_card_audit.py \
  --shortlist <active_shortlist_csv> \
  --cards-dir cards/ \
  --output output/card_audit_phase1.json
```

The script:
- Extracts frontmatter only from all `cards/**/*.md` (not full card bodies)
- Sends ~10–15k tokens to Gemini 3.5 Flash (vs ~65k for full card reads in Claude)
- Returns JSON with `Missing`, `Underutilized`, and `Orphan_Card` classifications

### Step 3 — Read the output

```bash
# Quick summary
python3 -c "
import json
d = json.load(open('output/card_audit_phase1.json'))
s = d.get('audit_summary', {})
print('Missing:', s.get('missing_count', '?'))
print('Underutilized:', s.get('underutilized_count', '?'))
f = d.get('phase1_findings', [])
for x in f:
    if x['classification'] in ('Missing', 'Underutilized'):
        print(f\"  [{x['classification']}] {x['candidate']} — {x['notes']}\")
"
```

### Step 4 — Use output as Phase 2 input

Pass `output/card_audit_phase1.json` findings as Phase 1 context when running Phase 2 (market discovery) in Claude. Do NOT re-read the card files — the audit output is sufficient for Phase 2 orientation.

## Completion Check

- `output/card_audit_phase1.json` exists and contains `phase1_findings` array
- At least one `Missing` or `Underutilized` finding is present (or summary confirms zero gaps)
- Pass findings to Phase 2 via conversation context, not by re-loading cards
- **Phase 2 handoff scope: top 10 shortlist candidates by `Adjusted_MCDA_Total`** (not top 3) — live pricing verification and MCDA confirmation must cover all 10
