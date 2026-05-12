# How to Maintain the MCDA Pipeline

## Active Scoring Model

The active model is the five-factor CareerCopilot MCDA rubric:

- `Performance_Headroom` - 25%
- `Price_Value` - 20%
- `Future_Proof` - 20%
- `Portability` - 20%
- `Track2_Avoidance` - 15%

Weights live in `config/procurement_policy.json`.

## Normal Flow

```bash
python scripts/build_shortlist.py
python scripts/enrich_shortlist_pricing.py NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist.csv
# Fill pricing fields and five MCDA factor columns.
python NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/rubric_weighting_engine.py \
  --csv NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist_pricing_enriched.csv
```

## Changing Weights

Edit only `config/procurement_policy.json`.

The five `mcda_weights` values must sum to `1.0`.

## Changing Gates

Edit `AGENTS.md` first, then align `config/procurement_policy.json`, then update scripts.

Do not leave script thresholds different from `AGENTS.md` unless the conflict is explicitly documented.

## Historical Files

The old expandable-workstation whitening rubric is no longer the active decision path. Treat workstation-specific CSVs and old rubric docs in this folder as reference data until the user reopens Track 2 implementation work.
