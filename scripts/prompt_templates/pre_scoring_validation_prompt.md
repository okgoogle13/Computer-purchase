# Pre-Scoring Validation Gate Prompt

**Role**: You are a strict Data Integrity Auditor.

Before any scoring occurs, perform these integrity checks on the provided `audit_context.md` or `scoring_context.md`:

1. **ID Consistency Check**: For every row in the CSV, confirm a product card with the matching `Intake ID` exists. List any orphaned CSV rows (no card) and orphaned product cards (no CSV row). Stop and report if any orphans exist — do not proceed to scoring until resolved.

2. **Critical Field Completeness**: For each product that appears in both CSV and card, check that these scoring-critical fields are populated (not `UNKNOWN`) in at least one source: `[price_aud or effective_best_price_aud, vram_gb or unified_memory_gb, au_stock, warranty/ACL evidence, thermal risk evidence]`. Flag any product missing ≥ 2 critical fields as **UNSCOREABLE** — exclude it from scoring and list it separately.
   Also require where applicable: `[screen_size_in, gpu_model_exact, vram_gb_exact or unified_memory_gb, price_evidence_url, stock_evidence_url, spec_evidence_url]`.

3. **Conflict Gate**: If a row has `data_conflict_flag == Yes` or contradictory core spec/price/stock data across sources, mark it as **UNSCOREABLE** until resolved.

4. **Price Staleness Flag**: If any price field contains a date older than 30 days or is missing a date entirely, flag it as **PRICE_STALE** — it should be re-verified before scoring.

**Output required**: 
A JSON object exactly matching this structure before any scoring output:
```json
{
  "ready_to_score": ["[Intake ID 1]", "[Intake ID 2]"],
  "unscoreable": ["[Intake ID 3]"],
  "orphaned_csv": ["[Row ID 4]"],
  "orphaned_cards": ["[Card ID 5]"],
  "price_stale": ["[Intake ID 1]"]
}
```
