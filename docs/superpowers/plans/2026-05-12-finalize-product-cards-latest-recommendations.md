# Finalize Product Cards From Latest Recommendation Search Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ingest all unique machine recommendations from legacy LLM logs into canonical `cards/` and shortlist CSVs with deterministic dedupe, AGENTS.md-compliant gating, and reproducible validation output.

**Architecture:** Add one deterministic harvest script that parses legacy logs and current shortlist, emits a machine inventory with actions (`skip_existing`, `update_partial`, `append_new`), and generates card-ready field mappings without inventing unknowns. Keep live pricing verification as a separate manual/agent checkpoint (no fake automation), then run existing enrichment/ranking validators. Treat source hierarchy explicitly so `EBAY_AU` is fallback for Track 1 recommendations.

**Tech Stack:** Python 3 (`csv`, `re`, `pathlib`, `json`), existing repo scripts in `scripts/`, markdown cards in `cards/`, shortlist CSVs in `shortlists/`.

---

## File Structure

- Create: `scripts/harvest_llm_recommendations.py`
- Create: `tests/test_harvest_llm_recommendations.py`
- Create: `logs/harvest_recommendations_latest.json`
- Modify: `scripts/README_pipeline.md`
- Modify: `scripts/prompt_templates/pre_scoring_validation_prompt.md`
- Modify: `scripts/prompt_templates/final_purchase_justification_prompt.md`
- Modify: `shortlists/2026-05-12_shortlist_ranked_final.csv` (or latest shortlist snapshot selected at execution time)
- Modify/Create: `cards/intake-XXX_<slug>.md` for newly harvested machines

### Task 1: Build Deterministic Harvest Engine

**Files:**
- Create: `scripts/harvest_llm_recommendations.py`
- Test: `tests/test_harvest_llm_recommendations.py`

- [ ] **Step 1: Write the failing parser/dedupe tests**

```python
# tests/test_harvest_llm_recommendations.py
from scripts.harvest_llm_recommendations import (
    normalize_item_name,
    extract_candidates_from_log,
    decide_action,
)


def test_normalize_item_name_removes_noise_tokens():
    assert normalize_item_name('Lenovo Legion 9i Gen 10 18" RTX 5080 (eBay)') == 'lenovo legion 9i gen 10 18 rtx 5080'


def test_extract_candidates_from_log_finds_machine_lines():
    text = """
### [82 / 100] — ASUS ROG Zephyrus Duo 16 RTX 4080
- **GPU**: NVIDIA RTX 4080 12GB
- **Price (AUD)**: $3000
"""
    rows = extract_candidates_from_log(text)
    assert len(rows) == 1
    assert rows[0]["item_name"] == "ASUS ROG Zephyrus Duo 16 RTX 4080"
    assert rows[0]["vram_gb"] == "12"


def test_decide_action_skip_existing_when_scored_and_priced():
    shortlist_row = {
        "MCDA_Total": "6.850",
        "effective_best_price_aud": "3000",
        "current_best_url": "https://example.com",
    }
    assert decide_action(shortlist_row) == "skip_existing"
```

- [ ] **Step 2: Run tests to verify failure**

Run: `pytest tests/test_harvest_llm_recommendations.py -q`
Expected: FAIL with `ModuleNotFoundError` or missing function errors.

- [ ] **Step 3: Write minimal harvest implementation**

```python
# scripts/harvest_llm_recommendations.py
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

MISSING = {"", "UNKNOWN", "N/A", "NONE", "-"}


def normalize_item_name(value: str) -> str:
    v = re.sub(r"\(.*?\)", "", value or "")
    v = re.sub(r"[^A-Za-z0-9\s]", " ", v)
    v = re.sub(r"\s+", " ", v).strip().lower()
    return v


def parse_money_aud(line: str) -> str:
    m = re.search(r"\$\s*([0-9][0-9,]*(?:\.[0-9]{1,2})?)", line)
    return m.group(1).replace(",", "") if m else "UNKNOWN"


def parse_vram_gb(line: str) -> str:
    m = re.search(r"([0-9]{1,3})\s*GB", line, flags=re.I)
    return m.group(1) if m else "UNKNOWN"


def extract_candidates_from_log(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for raw in text.splitlines():
        line = raw.strip()
        head = re.match(r"^###\s*(?:\[[^\]]+\]\s*[—-]\s*)?(.+)$", line)
        if head:
            if current:
                rows.append(current)
            current = {
                "item_name": head.group(1).strip(),
                "price_aud": "UNKNOWN",
                "vram_gb": "UNKNOWN",
                "source_note": "legacy_llm_log",
            }
            continue
        if not current:
            continue
        if "Price (AUD)" in line:
            current["price_aud"] = parse_money_aud(line)
        if "GPU" in line and "GB" in line:
            current["vram_gb"] = parse_vram_gb(line)
    if current:
        rows.append(current)
    return rows


def is_populated(v: str) -> bool:
    return (v or "").strip().upper() not in MISSING


def decide_action(shortlist_row: dict[str, str] | None) -> str:
    if not shortlist_row:
        return "append_new"
    if all(
        is_populated(shortlist_row.get(k, ""))
        for k in ("MCDA_Total", "effective_best_price_aud", "current_best_url")
    ):
        return "skip_existing"
    return "update_partial"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", required=True)
    ap.add_argument("--shortlist", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    log_text = Path(args.log).read_text(encoding="utf-8")
    extracted = extract_candidates_from_log(log_text)

    shortlist = list(csv.DictReader(Path(args.shortlist).open(encoding="utf-8")))
    by_key = {normalize_item_name(r.get("item_name", "")): r for r in shortlist}

    actions = []
    seen = set()
    for row in extracted:
        key = normalize_item_name(row["item_name"])
        if key in seen:
            continue
        seen.add(key)
        match = by_key.get(key)
        actions.append({**row, "normalized_key": key, "action": decide_action(match)})

    out = {
        "source_log": args.log,
        "shortlist": args.shortlist,
        "total_extracted": len(extracted),
        "unique_candidates": len(actions),
        "actions": actions,
    }
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"Wrote harvest report: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Re-run tests to verify pass**

Run: `pytest tests/test_harvest_llm_recommendations.py -q`
Expected: PASS (3 passed).

- [ ] **Step 5: Commit**

```bash
git add tests/test_harvest_llm_recommendations.py scripts/harvest_llm_recommendations.py
git commit -m "feat: add deterministic legacy recommendation harvest engine"
```

### Task 2: Produce Harvest Report and Build Card/CSV Work Queue

**Files:**
- Create: `logs/harvest_recommendations_latest.json`
- Modify: `shortlists/2026-05-12_shortlist_ranked_final.csv`
- Modify/Create: `cards/intake-XXX_<slug>.md`

- [ ] **Step 1: Run harvest report generation**

Run:

```bash
python3 scripts/harvest_llm_recommendations.py \
  --log _Archive_Legacy_Data/comprehensive_llm_recommendation_log_notebooklm_optimized.md \
  --shortlist shortlists/2026-05-12_shortlist_ranked_final.csv \
  --out logs/harvest_recommendations_latest.json
```

Expected: `Wrote harvest report: logs/harvest_recommendations_latest.json`.

- [ ] **Step 2: Verify report categories and counts**

Run:

```bash
python3 - <<'PY'
import json
p='logs/harvest_recommendations_latest.json'
r=json.load(open(p))
counts={}
for a in r['actions']:
    counts[a['action']]=counts.get(a['action'],0)+1
print('unique',r['unique_candidates'])
print('counts',counts)
PY
```

Expected: non-zero `append_new` or `update_partial` set, no crash.

- [ ] **Step 3: Create/Update product cards only for actionable rows**

```markdown
For each action in {append_new, update_partial}:
1) Create `cards/intake-XXX_<slug>.md` if missing.
2) Copy schema style from existing cards and keep UNKNOWN where unverified.
3) Fill only data present in legacy logs (item_name, indicative price_aud, gpu_model/vram when explicit).
4) Add provenance note: source file + extraction date.
```

- [ ] **Step 4: Update shortlist rows deterministically**

```csv
Required fields when appending/updating:
intake_id,item_name,status,track,pathway,gpu_model,vram_gb,price_aud,source_file,verification_status,Policy_Status,Policy_Blockers
```

Set policy-safe defaults:
- `status=NEEDS_REVIEW`
- `verification_status=Needs Verification`
- `Policy_Status=NEEDS_REVIEW`
- `Policy_Blockers` includes `AU stock not confirmed` and any gate failures that can be proven.

- [ ] **Step 5: Commit**

```bash
git add logs/harvest_recommendations_latest.json cards shortlists/2026-05-12_shortlist_ranked_final.csv
git commit -m "chore: sync legacy recommendation harvest into cards and shortlist"
```

### Task 3: Enforce AGENTS.md Gate Alignment and Prompt Safety

**Files:**
- Modify: `scripts/prompt_templates/pre_scoring_validation_prompt.md`
- Modify: `scripts/prompt_templates/final_purchase_justification_prompt.md`
- Modify: `scripts/README_pipeline.md`

- [ ] **Step 1: Add explicit AGENTS-aligned floors to pre-scoring prompt**

```markdown
Track 1A eligibility floor: discrete VRAM >= 8 GB.
Track 1A discovery preference: 12 GB+, stronger at 16 GB+ and 24 GB.
Track 1.5 desktop gate: VRAM >= 16 GB (24 GB preferred value tier, not hard gate).
Do not mark GOOD_ENOUGH without confirmed AU stock, price <= cap, and ACL/warranty path.
```

- [ ] **Step 2: Add source hierarchy rule to final justification prompt**

```markdown
Track 1 source priority: MANUFACTURER_AU > MAJOR_RETAILER_AU > AMAZON_AU > EBAY_AU > GUMTREE/FB > GRAY_IMPORT.
If winner is EBAY_AU, recommendation must include fallback justification and explicit warranty/return risk statement.
```

- [ ] **Step 3: Document non-automation constraint in pipeline README**

```markdown
`fill_shortlist_live_pricing.py` is scaffolding and does not perform live web lookups by default.
Live pricing remains a manual/agent checkpoint before final ranking.
```

- [ ] **Step 4: Run prompt/policy validators**

Run:

```bash
python3 scripts/validate_prompt_templates.py
python3 scripts/policy_drift_check.py
```

Expected:
- `Prompt contract validation PASSED`
- `Policy drift check: PASS`

- [ ] **Step 5: Commit**

```bash
git add scripts/prompt_templates/pre_scoring_validation_prompt.md scripts/prompt_templates/final_purchase_justification_prompt.md scripts/README_pipeline.md
git commit -m "docs: align prompt-chain gates with AGENTS policy and source hierarchy"
```

### Task 4: Final Validation and Decision Handoff

**Files:**
- Modify: `shortlists/2026-05-12_shortlist_ranked_final.csv` (or generated ranked output)
- Modify: `logs/harvest_recommendations_latest.json` (if regenerated)

- [ ] **Step 1: Re-run shortlist enrichment/ranking chain on updated shortlist**

Run:

```bash
python3 scripts/enrich_shortlist_pricing.py shortlists/2026-05-12_shortlist_ranked_final.csv --force
python3 scripts/scoring/rubric_weighting_engine.py \
  --csv shortlists/2026-05-12_shortlist_ranked_final_pricing_enriched.csv \
  --output-csv shortlists/2026-05-12_shortlist_ranked_final_ranked.csv
python3 scripts/pipeline_integrity_check.py \
  --enriched shortlists/2026-05-12_shortlist_ranked_final_pricing_enriched.csv \
  --ranked shortlists/2026-05-12_shortlist_ranked_final_ranked.csv
```

Expected: integrity check passes.

- [ ] **Step 2: Generate decision summary artifact**

```markdown
Include:
- harvested new items count
- updated partial items count
- remaining UNKNOWN decision-critical fields
- top Track 1 candidate(s) meeting GOOD_ENOUGH
- whether escalation exception is triggered
```

- [ ] **Step 3: Final QA sanity checks**

Run:

```bash
python3 - <<'PY'
import csv
p='shortlists/2026-05-12_shortlist_ranked_final_ranked.csv'
rows=list(csv.DictReader(open(p)))
assert any((r.get('item_name') or '').strip() for r in rows)
assert all('Policy_Status' in r for r in rows)
print('qa-ok rows',len(rows))
PY
```

Expected: `qa-ok rows <N>`.

- [ ] **Step 4: Commit**

```bash
git add shortlists/2026-05-12_shortlist_ranked_final_pricing_enriched.csv shortlists/2026-05-12_shortlist_ranked_final_ranked.csv
git commit -m "chore: finalize harvested shortlist and ranked output"
```

## Self-Review

- Spec coverage: covers extraction/dedupe, card generation, shortlist sync, AGENTS gating, and final ranking verification.
- Placeholder scan: no TBD/TODO placeholders; each task has executable commands and concrete outputs.
- Type consistency: uses existing CSV headers (`MCDA_Total`, `Policy_Status`, `Policy_Blockers`, `source_file`) and AGENTS-compatible statuses.
