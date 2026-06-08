# AUTONOMOUS EXECUTION PLAN — 2026-06-06
# CareerCopilot Hardware Procurement Pipeline
# Authority: AGENTS.md > config/procurement_policy.json > this document

<!--
  Generated: 2026-06-06T09:39:00Z
  Corrected: F1, F2, F3, F4, F5, F6, F7, F8, F9 applied.
  Upgraded:  U1, U2, U3, U4, U5 applied.
  Do NOT modify AGENTS.md or config/procurement_policy.json based on this document.
-->

---

# 1. CURRENT STATE ASSESSMENT

| Component | Status | Notes |
|-----------|--------|-------|
| **Pipeline scripts (existing, ready)** | ✅ | `build_shortlist.py`, `enrich_shortlist_pricing.py`, `fill_shortlist_live_pricing.py`, `rubric_weighting_engine.py`, `policy_drift_check.py`, `pipeline_integrity_check.py`, `validate_env.py`, `scripts/import/agent_browser_spec_gapfill.js`, `scripts/import/agent_browser_ebay_watchlist.js`, `scripts/data_collection/scrape_ebay_watchlist.py`, `scripts/data_collection/parse_ebay_watchlist.py`, `scripts/data_collection/enrich_ebay_specs.py`, `scripts/data_collection/map_ebay_to_intake.py` |
| **Scripts NEEDS CREATION** | ⚠️ | `scripts/data_collection/facebook_collect.py` — **BLOCKING for Stage B2**. `scripts/data_collection/gumtree_collect.py` — **BLOCKING for Stage B3**. `scripts/cards/update_cards_from_scored_shortlist.py` — **BLOCKING for Stage F**. `scripts/reports/generate_recommendations.py` — **BLOCKING for Stage G**. |
| **Credentials (.env)** | ✅ | All required vars present. `PARSEHUB_API_KEY`, `PARSEHUB_WATCHLIST_PROJECT_TOKEN`, `PARSEHUB_RETAILER_PROJECT_TOKEN`, `BROWSERLESS_API_KEY`, `VERCEL_BROWSER_AGENT_KEY`, `GEMINI_API_KEY`, `GITHUB_TOKEN`, `GITHUB_REPO` — all populated, no placeholders detected. `OPENAI_API_KEY` is a placeholder — optional, using Gemini fallback. |
| **7-factor scoring engine** | ✅ | `rubric_weighting_engine.py` implements `score_acquisition_risk`, `WEIGHT_ACQUISITION_RISK`, `score_battery`. Weights sum assertion present and passes. |
| **Shortlist data (existing)** | ✅ | `shortlists/2026-06-06_shortlist.csv`, `shortlists/2026-06-06_shortlist_pricing_enriched_live.csv`, `shortlists/2026-06-06_ranked.csv` all exist from prior run. |
| **Raw / processed data** | ✅ | `data/raw/ebay_watchlist/` and `data/processed/` contain 2026-06-06 eBay files. No Facebook or Gumtree raw data exists yet. |
| **Cards** | ✅ | `cards/laptops/` contains 66 cards from prior intake runs. |
| **Canonical schema** | ✅ | `config/shortlist_schema.json` valid — defines battery, seller, warranty, risk_adjusted_price fields. |
| **Policy thresholds** | ✅ | `budget_cap_aud = 5000.0`, `laptop_discrete_minimum_vram_gb = 8.0`, `laptop_unified_minimum_vram_gb = 16.0`. MCDA weights: Performance_Headroom=0.25, Price_Value=0.20, Future_Proof=0.20, Portability=0.20, Track2_Avoidance=0.15. **Note: config weights are the 5-factor AGENTS.md formula. The scoring engine uses the updated 7-factor weights (0.20/0.16/0.16/0.16/0.12/0.10/0.10). Record this drift if policy_drift_check.py reports it.** |
| **Estimated new listings** | 📊 | eBay AU: ~200 listings. Facebook Marketplace AU: ~150 listings. Gumtree AU: ~120 listings. |

---

# 2. PRE-FLIGHT CHECKLIST

All items must be true before Stage B begins. An autonomous agent must halt and report to the user if any item fails.

- [ ] **Credential validation** — `python scripts/utils/validate_env.py` exits 0. If exit code ≠ 0, PAUSE and present missing-credential remediation.
- [ ] **ParseHub API key** — `PARSEHUB_API_KEY` present, not placeholder.
- [ ] **ParseHub project tokens** — `PARSEHUB_WATCHLIST_PROJECT_TOKEN` and `PARSEHUB_RETAILER_PROJECT_TOKEN` present and configured in ParseHub dashboard for eBay AU search queries.
- [ ] **Browserless token** — `BROWSERLESS_API_KEY` present, not placeholder, service reachable.
- [ ] **Vercel browser agent key** — `VERCEL_BROWSER_AGENT_KEY` present (format: `vck_...`).
- [ ] **Cookie file: eBay** — `data/agent_browser_cookies/ebay_cookies.json` exists and is < 30 days old.
- [ ] **Cookie file: Facebook** — `data/agent_browser_cookies/facebook_cookies.json` exists and is < 30 days old. *(Facebook is login-gated — this is mandatory for Stage B2.)*
- [ ] **Gumtree — no authentication required (public site). No cookie file needed.** Verify ParseHub project token covers Gumtree search URLs. *(F4 applied)*
- [ ] **Canonical schema** — `config/shortlist_schema.json` exists and is syntactically valid JSON (`python -c "import json; json.load(open('config/shortlist_schema.json'))"` exits 0).
- [ ] **7-factor engine check** — All three functions exist in scoring engine:
  ```bash
  grep -q "score_acquisition_risk" scripts/scoring/rubric_weighting_engine.py
  grep -q "WEIGHT_ACQUISITION_RISK" scripts/scoring/rubric_weighting_engine.py
  grep -q "score_battery" scripts/scoring/rubric_weighting_engine.py
  ```
- [ ] **Policy drift check** — `python scripts/policy_drift_check.py` exits 0 or PASS. If MISMATCH: follow AGENTS.md for all human-facing recommendations until config is updated.
- [ ] **Missing scripts scaffolded** — Confirm or scaffold:
  - `scripts/data_collection/facebook_collect.py` (**NEEDS CREATION** — see F3)
  - `scripts/data_collection/gumtree_collect.py` (**NEEDS CREATION** — see F3)
  - `scripts/cards/update_cards_from_scored_shortlist.py` (**NEEDS CREATION** — see F3)
  - `scripts/reports/generate_recommendations.py` (**NEEDS CREATION** — see F3)

---

# 3. STAGE-BY-STAGE EXECUTION PLAN

> **Note on naming convention**: the "source of truth" shortlist that Stage E reads is:
> `shortlists/shortlist_{YYYY-MM-DD}_pricing_enriched_live.csv`
> This is the single authoritative file. No other variant is read by the scoring engine.

---

## STAGE A — Credential and Environment Validation

**Goal:** Verify all required API keys and credentials are populated before any network calls.

**Input:** `.env`  
**Output:** None (validation result only)

**Commands:**
```bash
python scripts/utils/validate_env.py
```

**Decision logic:**
- IF exit code 0 → continue to Stage B (parallel dispatch)
- ELSE → PAUSE. Print the human-readable checklist from Section 2. Do not proceed until all required vars are resolved.

**Estimated duration:** < 1 minute  
**Human checkpoint:** YES — user must confirm any flagged missing credentials before pipeline proceeds.

---

## STAGE B1 — eBay AU Data Collection

**Goal:** Pull current laptop listings from eBay AU via ParseHub (primary) with Agent Browser fallback.

**Input:** ParseHub API / `data/raw/ebay_watchlist/`  
**Output:** `data/processed/ebay_watchlist_{date}.csv`

**SELF_HEAL (U2):**
- Attempt 1 — retry ParseHub run (transient API timeout)
- Attempt 2 — switch to Agent Browser fallback for same queries
- Attempt 3 — PAUSE_HUMAN: "eBay collection failed after 2 attempts. Check PARSEHUB_API_KEY and eBay search project config."

**Commands:**
```bash
python scripts/data_collection/scrape_ebay_watchlist.py
python scripts/data_collection/parse_ebay_watchlist.py \
  data/raw/ebay_watchlist/ebay_watchlist_raw.csv \
  data/processed/ebay_watchlist_$(date +%F).csv
python scripts/data_collection/map_ebay_to_intake.py \
  data/processed/ebay_watchlist_$(date +%F).csv \
  data/processed/ebay_watchlist_$(date +%F)_mapped.csv
```

**Decision logic:**
- IF output CSV has > 0 rows → continue
- ELSE → initiate SELF_HEAL Attempt 2 (Agent Browser fallback), then Attempt 3

**Estimated duration:** ~3 minutes  
**Human checkpoint:** No (automated retry handles failures)

---

## STAGE B2 — Facebook Marketplace AU Data Collection

**Goal:** Collect AU laptop listings from Facebook Marketplace via Agent Browser (login-gated, browser-only).

**Input:** `data/agent_browser_cookies/facebook_cookies.json`  
**Output:** `data/processed/facebook_marketplace_{date}.csv`

**⚠️ F3 GUARD — MUST PASS BEFORE RUNNING:**
```
IF NOT EXISTS scripts/data_collection/facebook_collect.py:
  HALT. Run scaffolding agent with Facebook collection prompt
  (reference: project prompts library) before invoking this stage.
```

**SELF_HEAL (U2):**
- Attempt 1 — retry with refreshed cookie injection
- Attempt 2 — reduce query count to top 2 queries only
- Attempt 3 — PAUSE_HUMAN: "Facebook cookies may be expired. Re-export from browser and update data/agent_browser_cookies/facebook_cookies.json"

**Commands:**
```bash
python scripts/data_collection/facebook_collect.py \
  --cookies data/agent_browser_cookies/facebook_cookies.json \
  --output data/processed/facebook_marketplace_$(date +%F).csv
```

**Decision logic:**
- IF output CSV has ≥ 100 rows → continue
- IF output CSV has 10–99 rows → PARTIAL: log PARTIAL_FACEBOOK_COLLECTION, continue
- IF 0 rows → initiate SELF_HEAL Attempt 1, then 2, then 3

**Estimated duration:** ~4 minutes (browser automation)  
**Human checkpoint:** Yes (cookie freshness must be verified in pre-flight)

---

## STAGE B3 — Gumtree AU Data Collection

**Goal:** Collect AU laptop listings from Gumtree via ParseHub (primary) with Agent Browser fallback.

**Input:** ParseHub API (Gumtree project token)  
**Output:** `data/processed/gumtree_{date}.csv`

**⚠️ F3 GUARD — MUST PASS BEFORE RUNNING:**
```
IF NOT EXISTS scripts/data_collection/gumtree_collect.py:
  HALT. Run scaffolding agent with Gumtree collection prompt
  (reference: project prompts library) before invoking this stage.
```

**⚠️ F8 — GUMTREE RISK FLAG (mandatory):**
All Gumtree rows must have `NO_FEEDBACK_SYSTEM` appended to `risk_flags`.
Gumtree has no verified seller feedback system — this flag is mandatory
for all rows regardless of `seller_class`.

**SELF_HEAL (U2):**
- Attempt 1 — retry ParseHub run
- Attempt 2 — Agent Browser fallback
- Attempt 3 — PARTIAL: continue without Gumtree, append GUMTREE_COLLECTION_FAILED to pipeline log

**Commands:**
```bash
python scripts/data_collection/gumtree_collect.py \
  --output data/processed/gumtree_$(date +%F).csv
```

**Decision logic:**
- IF output CSV has ≥ 80 rows → continue
- IF output CSV has 1–79 rows → PARTIAL: log PARTIAL_GUMTREE_COLLECTION, continue
- IF 0 rows → initiate SELF_HEAL Attempt 1, then 2, then PARTIAL (Attempt 3 — do NOT block pipeline)

**Estimated duration:** ~3 minutes  
**Human checkpoint:** No (Gumtree is public; no login required)

---

## STAGE B-MERGE — Consolidation

**Goal:** Merge all three platform CSVs, deduplicate against existing shortlists, apply policy pre-filters.

**Input:** `data/processed/ebay_watchlist_{date}_mapped.csv`, `data/processed/facebook_marketplace_{date}.csv`, `data/processed/gumtree_{date}.csv`  
**Output:** `shortlists/shortlist_{date}_raw.csv`

**Commands:**
```bash
python scripts/build_shortlist.py
```

**Decision logic:**
- IF merged shortlist has ≥ 50 rows after pre-filter → continue
- IF 10–49 rows → PARTIAL: log CANDIDATE_SHORTFALL, continue
- IF < 10 rows → PAUSE_HUMAN: "Fewer than 10 candidates survived policy pre-filter. Review keyword filters and budget cap."

**Estimated duration:** < 1 minute  
**Human checkpoint:** No

---

## STAGE C — Spec Gap-Filling

**Goal:** For all rows in shortlist_raw with empty spec fields (gpu_model, vram_gb, weight_kg, has_thunderbolt_5, etc.) — use Agent Browser to navigate to the product URL and extract missing specs.

**Input:** `shortlists/shortlist_{date}_raw.csv`  
**Output:** `shortlists/shortlist_{date}_filled.csv`

**SELF_HEAL (U2):**
- Attempt 1 — retry with extended timeout (+30s per URL)
- Attempt 2 — skip rows that fail after 3 URL attempts, mark `spec_source = "gap_fill_failed"` for those rows
- Attempt 3 — PARTIAL: proceed with available specs, flag incomplete rows as PENDING_SPEC_REVIEW

**Commands (F1 applied — correct Node invocation):**
```bash
node scripts/import/agent_browser_spec_gapfill.js \
  shortlists/shortlist_$(date +%F)_raw.csv \
  shortlists/shortlist_$(date +%F)_filled.csv
```

**Tag updated rows:** `spec_source = "agent_browser_gapfill"`  
**Tag failed rows:** `spec_source = "gap_fill_failed"`

**Decision logic:**
- IF > 60% of rows have gpu_model + vram_gb populated → continue
- IF ≤ 60% → log SPEC_GAP_FILL_INCOMPLETE, continue with PARTIAL data

**Estimated duration:** ~5 minutes (parallel browsing)  
**Human checkpoint:** No

---

## STAGE D — Pricing Enrichment

**Goal:** Add pricing metadata columns (Phase 3a scaffold) then fill with live AU pricing data (Phase 3b). Compute `risk_adjusted_price` for every row.

**Input:** `shortlists/shortlist_{date}_filled.csv`  
**Output:** `shortlists/shortlist_{date}_pricing_enriched_live.csv`

**Commands:**
```bash
python scripts/enrich_shortlist_pricing.py \
  shortlists/shortlist_$(date +%F)_filled.csv

python scripts/fill_shortlist_live_pricing.py \
  shortlists/shortlist_$(date +%F)_pricing_enriched.csv
```

**⚠️ F6 — risk_adjusted_price ASSERTION (mandatory after Stage D):**
```bash
python -c "
import pandas as pd, sys
df = pd.read_csv('shortlists/shortlist_$(date +%F)_pricing_enriched_live.csv')
nulls = df['risk_adjusted_price'].isnull().sum()
if nulls > 0:
    print(f'WARNING: {nulls} rows missing risk_adjusted_price. Using list_price_aud as fallback.')
    df.loc[df['risk_adjusted_price'].isnull(), 'risk_adjusted_price'] = df['list_price_aud']
    df.loc[df['risk_adjusted_price'].isnull(), 'risk_flags'] += ',PRICE_RISK_FALLBACK'
    df.to_csv('shortlists/shortlist_$(date +%F)_pricing_enriched_live.csv', index=False)
else:
    print('risk_adjusted_price validated. All rows populated.')
"
```

**ON FAIL:** Log warning, apply `list_price_aud` fallback, append `PRICE_RISK_FALLBACK` to `risk_flags` for affected rows, continue.

**Decision logic:**
- IF any `effective_best_price_aud` still UNKNOWN after live fill → log for manual review; continue
- IF `risk_adjusted_price` null count > 0 → apply F6 fallback assertion above

**Estimated duration:** ~3 minutes  
**Human checkpoint:** No

---

## STAGE E — 7-Factor MCDA Scoring

**Goal:** Run the 7-factor MCDA engine against the merged shortlist. Apply policy gates and risk multipliers. Output ranked CSV.

**Input (source of truth):** `shortlists/shortlist_{date}_pricing_enriched_live.csv`  
**Output:** `shortlists/scored_candidates_{date}.csv`

**⚠️ F7 — PRE-CHECK (BLOCKING — must pass before running scoring engine):**
```bash
grep -q "score_acquisition_risk" scripts/scoring/rubric_weighting_engine.py && \
grep -q "WEIGHT_ACQUISITION_RISK" scripts/scoring/rubric_weighting_engine.py && \
grep -q "score_battery" scripts/scoring/rubric_weighting_engine.py && \
echo "7-FACTOR ENGINE VERIFIED" || \
echo "HALT: scoring engine missing required functions — see F7"
```

IF any grep returns empty:
  HALT. The corrective scoring prompt has not been applied.
  Apply `docs/CORRECTIVE_PROMPT_ACQUISITION_RISK.md` before Stage E.
  Do not run scoring with the old 6-factor model — results will
  not penalise old/private-sale/battery-undisclosed listings.

IF all greps pass: continue.

**SELF_HEAL (U2):**
- Attempt 1 — verify input CSV exists and has required columns
- Attempt 2 — if column missing: add empty column with default value (e.g. `Upgrade_Ceiling = ""`)
- Attempt 3 — ABORT if `WEIGHT_ACQUISITION_RISK` not found in engine

**Commands:**
```bash
python scripts/scoring/rubric_weighting_engine.py \
  --csv shortlists/shortlist_$(date +%F)_pricing_enriched_live.csv \
  --output-csv shortlists/scored_candidates_$(date +%F).csv
```

**Decision logic:**  *(F2 applied — Policy_Status = PASS, not GOOD_ENOUGH)*
- IF any row has `Policy_Status = PASS` → proceed to Stage F
- IF no row has `Policy_Status = PASS` → PAUSE_HUMAN: "No candidate cleared policy gates. Apply Track Escalation Rule per AGENTS.md."

**Estimated duration:** < 1 minute  
**Human checkpoint:** No (automated decision logic handles escalation trigger)

---

## STAGE F — Card and Documentation Update

**Goal:** Create or update `cards/laptops/{id}.md` for each scored candidate. Write MCDA fields to YAML front-matter. Log this run to `docs/HYBRID_PIPELINE.md`.

**Input:** `shortlists/scored_candidates_{date}.csv`  
**Output:** `cards/laptops/*.md` (new/updated), `docs/HYBRID_PIPELINE.md` (appended)

**⚠️ F3 GUARD — MUST PASS BEFORE RUNNING:**
```
IF NOT EXISTS scripts/cards/update_cards_from_scored_shortlist.py:
  HALT. Scaffold the card update script before invoking Stage F.
```

**Commands:**
```bash
python scripts/cards/update_cards_from_scored_shortlist.py \
  --input shortlists/scored_candidates_$(date +%F).csv \
  --cards-dir cards/laptops
```

**Safety rules:**
- Script MUST only write YAML front-matter fields.
- Script MUST NOT overwrite any `## Battery Health`, `## Acquisition Risk`, `## Evidence`, `## Notes`, or any other manually-authored body section.
- For new cards: create the full file with front-matter + `## Battery Health` and `## Acquisition Risk` stubs only.
- If a card body section would be overwritten: ABORT card update for that row and log CARD_MANUAL_SECTION_CONFLICT.

**Decision logic:**
- IF all scored candidates have updated cards → continue
- IF any card raises CARD_MANUAL_SECTION_CONFLICT → log conflict, skip that card, continue

**Estimated duration:** < 2 minutes  
**Human checkpoint:** No

---

## STAGE G — Human-Readable Recommendations Report

**Goal:** Generate `reports/recommendations_{date}.md` containing all seven required report sections.

**Input:** `shortlists/scored_candidates_{date}.csv`  
**Output:** `reports/recommendations_{date}.md`

**⚠️ F3 GUARD — MUST PASS BEFORE RUNNING:**
```
IF NOT EXISTS scripts/reports/generate_recommendations.py:
  HALT. Scaffold the report generator before invoking Stage G.
```

**Commands:**
```bash
python scripts/reports/generate_recommendations.py \
  --input shortlists/scored_candidates_$(date +%F).csv \
  --output reports/recommendations_$(date +%F).md
```

**Required report sections:**
1. Executive summary — top 3 ranked candidates, key differentiators, pipeline health metrics (U5)
2. Full ranked table — all PASS candidates, all 7 factor scores
3. Risk heat map — table of all risk_flags per candidate
4. Battery health transparency summary — which listings disclosed, which did not, scores
5. Platform comparison — how eBay vs Facebook vs Gumtree performed as sources
6. Policy failures log — all POLICY_FAIL/NEEDS_REVIEW rows with reasons
7. Recommended next action per top candidate (e.g. "Request battery report", "Verify TB5 on OEM page", "Check seller warranty terms before bidding")

**Decision logic:**
- IF report generated without errors → SUCCESS
- ELSE → PAUSE_HUMAN: show exact error, stage, and what file or data is needed to unblock

**Estimated duration:** < 1 minute  
**Human checkpoint:** No

---

## STAGE H — Log Completion

**Goal:** Append run summary and pipeline health metrics to dated log.

**Commands:**
```bash
echo "Pipeline completed at $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> logs/pipeline_$(date +%F).log
```

All scripts throughout the pipeline log to stdout. Redirect all stage output to the log file during orchestrated runs:
```bash
python scripts/scoring/rubric_weighting_engine.py \
  --csv ... \
  --output-csv ... 2>&1 | tee -a logs/pipeline_$(date +%F).log
```

---

# 4. DEPENDENCY MAP *(U1 applied — parallel orchestration)*

```
STAGE A (credentials)
  │
  ├─── PARALLEL BLOCK 1 (dispatch simultaneously) ──────────────────────────
  │      SA-EBAY     → B1: eBay AU collection
  │      SA-FACEBOOK → B2: Facebook Marketplace collection
  │      SA-GUMTREE  → B3: Gumtree AU collection
  │
  │    AWAIT_ALL([SA-EBAY, SA-FACEBOOK, SA-GUMTREE], timeout=600s)
  │      → ON PARTIAL SUCCESS (≥1 platform returned data): continue to B-MERGE
  │      → ON TOTAL FAILURE (all 3 returned 0 rows): PAUSE_HUMAN
  │
  ├─── B-MERGE: MERGE_OUTPUTS([B1, B2, B3]) → shortlists/merged_{date}.csv
  │
  ├─── PARALLEL BLOCK 2 (dispatch simultaneously) ──────────────────────────
  │      SA-GAPFILL → C: Spec gap-filling
  │      SA-PRICER  → D: Pricing enrichment + risk_adjusted_price
  │
  │    AWAIT_ALL([SA-GAPFILL, SA-PRICER], timeout=600s)
  │      → merge gap-filled specs + enriched pricing into single CSV
  │      → ASSERT: risk_adjusted_price non-null (F6 assertion)
  │
  └─── SEQUENTIAL ──────────────────────────────────────────────────────────
         E (MCDA scoring) → F (card update) → G (report) → H (log)
```

**Note — True parallel execution:**
True parallel execution requires `run_pipeline.js` to use `Promise.all()` for B1–B3, and Python `multiprocessing` or `asyncio` for C+D. Shell implementation uses `&` + `wait` as minimum viable parallelism:

```bash
# Parallel B1-B3
python scripts/data_collection/scrape_ebay_watchlist.py &
python scripts/data_collection/facebook_collect.py &
python scripts/data_collection/gumtree_collect.py &
wait  # AWAIT_ALL

# Parallel C+D (note: merge required before Stage E)
node scripts/import/agent_browser_spec_gapfill.js \
  shortlists/shortlist_$(date +%F)_raw.csv \
  shortlists/shortlist_$(date +%F)_filled.csv &
python scripts/enrich_shortlist_pricing.py \
  shortlists/shortlist_$(date +%F)_raw.csv &
wait  # AWAIT_ALL
# then merge gap-filled specs + pricing columns before Stage E
```

**Stages that can run in parallel:** B1, B2, B3 (Block 1). C, D (Block 2).  
**Stages that are strictly sequential:** A → B-MERGE → E → F → G → H.

---

# 5. ROLLBACK AND SAFETY RULES

## GLOBAL RECOVERY LADDER *(U4 applied — applies to all stages)*

```
Level 1 — RETRY:   Re-run with identical parameters (max 2x).
Level 2 — RELAX:   Re-run with relaxed parameters
                   (extend timeout, reduce required field count,
                    broaden keyword filter, use fallback data source).
Level 3 — PARTIAL: Proceed with available data.
                   Log gap with PARTIAL_DATA flag, continue pipeline.
Level 4 — PAUSE_HUMAN: Surface specific blocker with exact remediation
                   steps — not a vague error message.
Level 5 — ABORT:   Only for credential failures, policy file unreadable,
                   or engine missing core functions.
```

**Rule:** The orchestrator MUST NOT jump to Level 4 or 5 without first attempting Levels 1–3.  
Every PAUSE_HUMAN must include:
- Which stage failed
- What was attempted (levels tried)
- Exact file or credential needed to unblock
- Estimated time to fix

---

## Per-Stage Rollback Rules

| Stage | Failure Action | Safe to Delete & Regenerate | Must Preserve |
|-------|---------------|------------------------------|---------------|
| **A** | Re-run validator after fixing env | N/A | `.env` |
| **B1–B3** | Re-run individual collector after fixing cookies / ParseHub token | `data/raw/*`, `data/processed/*` (all are derived outputs — safe to regenerate) | `cards/*.md` manual sections and `.env` only. **Never delete shortlists/ files that have already been scored.** *(F5 applied)* |
| **B-MERGE** | Delete `shortlists/shortlist_*_raw.csv`, re-run `build_shortlist.py` | `shortlists/*_raw.csv` | Existing scored shortlists |
| **C** | Delete `shortlists/shortlist_*_filled.csv`, re-run spec-gap script | `shortlists/*_filled.csv` | No manual edits exist at this stage |
| **D** | Delete `*_pricing_enriched*.csv`, re-run both pricing scripts | `*_pricing_enriched.csv`, `*_pricing_enriched_live.csv` | Any manual price overrides added by user |
| **E** | Delete `scored_candidates_*.csv`, re-run scoring engine | `shortlists/scored_candidates_*.csv` | None |
| **F** | **CRITICAL**: Never overwrite manual sections in card markdown files. If conflict detected (CARD_MANUAL_SECTION_CONFLICT), skip that card, log, and continue. | Only card front-matter YAML may be rewritten | `## Battery Health`, `## Acquisition Risk`, `## Evidence`, `## Notes`, and all body text below the front-matter |
| **G** | Delete report, re-run report generator | `reports/recommendations_*.md` | None |
| **H** | Log file can be appended or recreated per run | Old log files | None |

---

# 6. INVOCATION INSTRUCTIONS

All commands assume execution from the repository root:
```
/Users/okgoogle13/Projects/Computer purchase/
```

## Resume from a specific stage

```bash
# Resume from Stage C (spec gap-filling), skipping collection
node scripts/import/agent_browser_spec_gapfill.js \
  shortlists/shortlist_2026-06-06_raw.csv \
  shortlists/shortlist_2026-06-06_filled.csv

# Resume from Stage D (pricing enrichment)
python scripts/enrich_shortlist_pricing.py shortlists/shortlist_2026-06-06_filled.csv
python scripts/fill_shortlist_live_pricing.py shortlists/shortlist_2026-06-06_pricing_enriched.csv

# Resume from Stage E (scoring only)
python scripts/scoring/rubric_weighting_engine.py \
  --csv shortlists/shortlist_2026-06-06_pricing_enriched_live.csv \
  --output-csv shortlists/scored_candidates_2026-06-06.csv

# Resume from Stage G (report only)
python scripts/reports/generate_recommendations.py \
  --input shortlists/scored_candidates_2026-06-06.csv \
  --output reports/recommendations_2026-06-06.md
```

## Re-run a single platform search without re-running all

```bash
# eBay only
python scripts/data_collection/scrape_ebay_watchlist.py
python scripts/data_collection/parse_ebay_watchlist.py \
  data/raw/ebay_watchlist/ebay_watchlist_raw.csv \
  data/processed/ebay_watchlist_$(date +%F).csv

# Facebook only (after refreshing cookies)
python scripts/data_collection/facebook_collect.py \
  --cookies data/agent_browser_cookies/facebook_cookies.json \
  --output data/processed/facebook_marketplace_$(date +%F).csv

# Gumtree only
python scripts/data_collection/gumtree_collect.py \
  --output data/processed/gumtree_$(date +%F).csv
```

## Re-score without re-collecting

```bash
python scripts/scoring/rubric_weighting_engine.py \
  --csv shortlists/shortlist_$(date +%F)_pricing_enriched_live.csv \
  --output-csv shortlists/scored_candidates_$(date +%F).csv
```

## Regenerate report only

```bash
python scripts/reports/generate_recommendations.py \
  --input shortlists/scored_candidates_$(date +%F).csv \
  --output reports/recommendations_$(date +%F).md
```

## Run integrity check after pipeline

```bash
python scripts/pipeline_integrity_check.py \
  --enriched shortlists/shortlist_$(date +%F)_pricing_enriched_live.csv \
  --ranked shortlists/scored_candidates_$(date +%F).csv
```

---

## SUBAGENT DISPATCH INVOCATIONS *(U3 applied — for follow-up Antigravity session)*

```
# Run all collection agents in parallel:
DISPATCH_SUBAGENT(id:SA-EBAY,     task:"Run Stage B1")
DISPATCH_SUBAGENT(id:SA-FACEBOOK, task:"Run Stage B2")
DISPATCH_SUBAGENT(id:SA-GUMTREE,  task:"Run Stage B3")
AWAIT_ALL([SA-EBAY, SA-FACEBOOK, SA-GUMTREE])

# Run gap-fill and pricing enrichment in parallel:
DISPATCH_SUBAGENT(id:SA-GAPFILL, task:"Run Stage C")
DISPATCH_SUBAGENT(id:SA-PRICER,  task:"Run Stage D")
AWAIT_ALL([SA-GAPFILL, SA-PRICER])
# then merge outputs before Stage E

# Invoke scoring only (skip collection):
DISPATCH_SUBAGENT(id:SA-SCORER, task:"Run Stage E only.
  Input: most recent shortlist_{date}_pricing_enriched_live.csv.
  Assert 7-factor model active before running.")

# Invoke report only:
DISPATCH_SUBAGENT(id:SA-REPORTER, task:"Run Stage G only.
  Input: most recent scored_candidates_{date}.csv.")
```

---

# 7. SUCCESS CRITERIA

**Minimum candidates:** *(F9 applied)*  
≥ 10 scored PASS candidates appear in `shortlists/scored_candidates_{date}.csv`,
or as configured by `min_candidates_threshold` in `procurement_policy.json`.
If fewer than 10 PASS candidates result, log `CANDIDATE_SHORTFALL` and
trigger **SELF_HEAL: relax policy thresholds by one tier and re-score.**

**Cards:**  
Every row with `Policy_Status = PASS` has a corresponding markdown card in `cards/laptops/` whose front-matter includes all derived fields: `risk_adjusted_price`, `risk_flags`, all 7 MCDA factor scores, `battery_score`, `battery_disclosure_level`, `score_acquisition_risk`, `manufacture_year`.

**Report:**  
`reports/recommendations_{date}.md` exists, renders without Markdown errors, and contains all 7 required sections (see Stage G above).

**Policy failures:**  
No rows in the ranked CSV have `Policy_Status = NEEDS_REVIEW` or `Policy_Status = POLICY_FAIL` without an explanatory entry in `Policy_Blockers`.

**Log:**  
`logs/pipeline_{date}.log` exists, contains no lines prefixed with `ERROR:`, and records timestamps for each completed stage.

---

## PIPELINE HEALTH METRICS *(U5 applied — logged to logs/pipeline_{date}.log and included in Stage G executive summary)*

| Metric | Target | Warning Threshold | Log Flag |
|--------|--------|-------------------|----------|
| **Collection rate** | > 80% of estimated listings per platform | Any platform < 50% | `LOW_COLLECTION_RATE_{PLATFORM}` |
| **Filter survival rate** | > 20% of collected rows pass pre-filter | < 20% | `FILTER_TOO_AGGRESSIVE` |
| **Policy pass rate** | > 10% of scored rows are PASS | < 10% | `POLICY_OVERLY_RESTRICTIVE` (suggest relaxing one threshold in `procurement_policy.json`) |
| **Battery disclosure rate** | > 30% of rows have `battery_disclosure_level != "none"` | < 30% | `LOW_BATTERY_DISCLOSURE_RATE` |
| **Spec completeness rate** | > 60% of rows have `gpu_model` + `vram_gb` populated | < 60% | `SPEC_GAP_FILL_INCOMPLETE` |
| **Acquisition risk distribution** | Log count per tier | — | `HIGH_RISK (0–3)`, `MEDIUM_RISK (4–6)`, `LOW_RISK (7–10)` — count of rows per tier |

These metrics are:
1. Printed in the executive summary section of the Stage G report.
2. Appended to `logs/pipeline_{date}.log` after Stage G completes.

---

# APPENDIX — SCRIPTS NEEDS CREATION REGISTRY

The following scripts are referenced in this plan but do not yet exist.
They must be scaffolded before the relevant stage can run.

| Script | Required For | Priority | Notes |
|--------|-------------|----------|-------|
| `scripts/data_collection/facebook_collect.py` | Stage B2 | BLOCKING | Must use Browserless API + cookie injection. Login-gated. |
| `scripts/data_collection/gumtree_collect.py` | Stage B3 | BLOCKING | May use ParseHub (primary) or Browserless (fallback). Public site, no login. All rows get `NO_FEEDBACK_SYSTEM` risk flag. |
| `scripts/cards/update_cards_from_scored_shortlist.py` | Stage F | BLOCKING | Must write front-matter only. Must never overwrite body sections. |
| `scripts/reports/generate_recommendations.py` | Stage G | BLOCKING | Must produce all 7 report sections + pipeline health metrics. |

---

*This document is self-contained. An autonomous agent reading it can execute every stage in order, pause only at documented PAUSE_HUMAN checkpoints, apply SELF_HEAL logic before escalating to human, and produce a complete, auditable hardware-procurement pipeline run without additional context.*

*Authority order: AGENTS.md > config/procurement_policy.json > this document.*
