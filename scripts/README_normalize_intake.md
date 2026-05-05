# normalize_intake.py — Usage Guide

Script: `scripts/normalize_intake.py`
Project: `Computer purchase` hardware research repo

---

## What it does

Converts raw Gemini / NotebookLM hardware CSV output into a clean, normalized CSV
ready for routing into product cards or downstream scripts.

Handles:
- Code fences (` ```csv `) and wrapper text ("Code snippet", "Copy code", etc.)
- Datasets returned as one long line (splits on ISO date boundaries)
- Repeated header rows embedded in the output
- Rows with wrong column counts (collapses overflow, quarantines underflow)
- Null-like tokens (`None`, `null`, `n/a`, `—`) → `UNKNOWN`
- URL cleanup: markdown links, truncated `...` URLs
- Numeric cleaning: strips `$`, `AUD`, `GB`, commas
- Enum normalization with partial-match coercion and logging
- Cross-field sanity checks (logged as warnings, not blocking)
- Deduplication by URL first, then composite key

---

## Canonical 19-column schema

```
date_found, source_batch, track, pathway, category, item_name,
price_aud, gpu_model, vram_gb, unified_memory_gb, ram_gb, cpu_model,
condition, retailer, url, au_stock_confirmed, verification_status,
status, notes
```

---

## Enum allowed values

| Field | Allowed values |
|---|---|
| `track` | `Track1A`, `Track1B`, `Track1.5`, `Track2A`, `Track2B`, `Track2C`, `UNKNOWN` |
| `category` | `Laptop`, `Desktop`, `Component`, `DIY Build`, `Mini PC`, `eGPU`, `UNKNOWN` |
| `condition` | `New`, `Used`, `Refurbished`, `Open Box`, `UNKNOWN` |
| `au_stock_confirmed` | `Yes`, `No`, `UNKNOWN` |
| `verification_status` | `Unverified`, `Needs Verification`, `Verified` |
| `status` | `Active`, `Superseded`, `Out of Stock`, `Watchlist`, `UNKNOWN` |

---

## Usage

### Basic

```bash
python scripts/normalize_intake.py NotebookLM_Workspaces/intake/raw/2026-05-05_batch1_laptops.txt
```

### Custom output directory

```bash
python scripts/normalize_intake.py path/to/raw_file.txt --out-dir path/to/output/
```

---

## Output files

All outputs land in `NotebookLM_Workspaces/intake/processed/` by default (created if missing).

| File | Contents |
|---|---|
| `<stem>_processed.csv` | Clean, normalized rows — ready for card routing |
| `<stem>_manual_review.csv` | Rows that could not be parsed into 19 columns |
| `<stem>_normalization_log.json` | All warnings, coercions, counts, timestamps |

---

## Workflow

```
Gemini / NotebookLM
       ↓  (copy CSV output)
NotebookLM_Workspaces/intake/raw/<date>_<batch>.txt
       ↓  (run script)
python scripts/normalize_intake.py NotebookLM_Workspaces/intake/raw/<date>_<batch>.txt
       ↓
NotebookLM_Workspaces/intake/processed/
   ├── <stem>_processed.csv          ← clean rows
   ├── <stem>_manual_review.csv      ← rows needing manual fix
   └── <stem>_normalization_log.json ← full audit trail
```

---

## Raw file format

Paste the Gemini/NotebookLM output directly into a `.txt` or `.csv` file.
No cleanup required — the script handles code fences and wrapper text automatically.

Naming convention for raw files:
```
YYYY-MM-DD_<source>_<batch-label>.txt
```
Examples:
```
2026-05-05_notebooklm_batch1_laptops.txt
2026-05-05_gemini_track2_desktops.txt
```

---

## What this script does NOT do

- It does not create product card `.md` files (that is `intake_to_cards.py` — not yet built)
- It does not write to `laptop_candidates.csv` or any existing tracker
- It does not commit to git

This is a preprocessing layer only. Review the processed CSV before any further automation.

---

## Dependencies

Standard library only. No pip installs required. Python 3.10+.
