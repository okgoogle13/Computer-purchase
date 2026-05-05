#!/usr/bin/env python3
"""
normalize_intake.py
-------------------
Preprocessing layer for raw Gemini / NotebookLM hardware CSV output.

Handles malformed input: one-line CSVs, repeated headers, code fences,
wrapper text, truncated URLs, bad enums, and column count mismatches.

Usage:
    python scripts/normalize_intake.py path/to/raw_file.txt
    python scripts/normalize_intake.py path/to/raw_file.txt --out-dir path/to/output/

Outputs (default: NotebookLM_Workspaces/intake/processed/):
    <stem>_processed.csv          — clean, normalized rows
    <stem>_manual_review.csv      — rows that could not be reliably parsed
    <stem>_normalization_log.json — all warnings, coercions, counts
"""

import argparse
import csv
import io
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

CANONICAL_HEADER = [
    "date_found", "source_batch", "track", "pathway", "category",
    "item_name", "price_aud", "gpu_model", "vram_gb", "unified_memory_gb",
    "ram_gb", "cpu_model", "condition", "retailer", "url",
    "au_stock_confirmed", "verification_status", "status", "notes",
]
NUM_COLS = len(CANONICAL_HEADER)  # 19

# ---------------------------------------------------------------------------
# Enum allowed values (lowercase keys → display values)
# ---------------------------------------------------------------------------

ENUM_TRACK = {
    "track1a": "Track1A",
    "track1b": "Track1B",
    "track1.5": "Track1.5",
    "track2a": "Track2A",
    "track2b": "Track2B",
    "track2c": "Track2C",
}

ENUM_CATEGORY = {
    "laptop": "Laptop",
    "desktop": "Desktop",
    "component": "Component",
    "diy build": "DIY Build",
    "mini pc": "Mini PC",
    "egpu": "eGPU",
}

ENUM_CONDITION = {
    "new": "New",
    "used": "Used",
    "refurbished": "Refurbished",
    "open box": "Open Box",
}

ENUM_AU_STOCK = {
    "yes": "Yes",
    "no": "No",
}

ENUM_VERIFICATION = {
    "unverified": "Unverified",
    "needs verification": "Needs Verification",
    "verified": "Verified",
}

ENUM_STATUS = {
    "active": "Active",
    "superseded": "Superseded",
    "out of stock": "Out of Stock",
    "watchlist": "Watchlist",
}

# Tokens that should be treated as missing/unknown
NULL_TOKENS = {"", "none", "null", "n/a", "na", "unknown", "-", "—", "–"}


# ---------------------------------------------------------------------------
# Basic field helpers
# ---------------------------------------------------------------------------

def is_null(val: str) -> bool:
    """Return True if val is a null-like token."""
    return val.strip().lower() in NULL_TOKENS


def normalize_null(val: str) -> str:
    """Replace null-like values with UNKNOWN; otherwise strip whitespace."""
    return "UNKNOWN" if is_null(val) else val.strip()


def collapse_whitespace(val: str) -> str:
    """Collapse runs of whitespace to a single space."""
    return re.sub(r"\s+", " ", val).strip()


# ---------------------------------------------------------------------------
# Input cleaning — strip Gemini wrapper artifacts
# ---------------------------------------------------------------------------

def strip_code_fences(text: str) -> str:
    """Remove markdown code fences (```csv, ```, etc.)."""
    text = re.sub(r"^```[a-z]*\s*$", "", text, flags=re.MULTILINE)
    return text


def strip_wrapper_text(text: str) -> str:
    """Remove common Gemini/NotebookLM UI chrome that precedes the CSV."""
    # Match lines that are purely wrapper phrases
    wrapper_pattern = re.compile(
        r"^(Code snippet|Download code|Copy code|Here is the CSV[:\s]*"
        r"|Output[:\s]*|Result[:\s]*|Here are the results[:\s]*)\s*$",
        flags=re.IGNORECASE | re.MULTILINE,
    )
    text = wrapper_pattern.sub("", text)
    return text


# ---------------------------------------------------------------------------
# URL normalization
# ---------------------------------------------------------------------------

def normalize_url(url: str, warnings: list, row_id: str) -> str:
    """
    Normalize the url field:
      - Expand markdown links [label](url) -> url
      - Accept plain http/https URLs
      - Truncated URLs (ending '...' or '…') -> UNKNOWN
      - Non-http values -> UNKNOWN (logged)
    """
    url = url.strip()

    if is_null(url):
        return "UNKNOWN"

    # Expand markdown link: [any text](https://...)
    md_match = re.match(r"\[.*?\]\((https?://[^\)]+)\)", url)
    if md_match:
        url = md_match.group(1).strip()

    # Truncated URL
    if url.endswith("...") or url.endswith("…"):
        warnings.append({
            "type": "truncated_url",
            "row": row_id,
            "original": url,
        })
        return "UNKNOWN"

    # Must start with http:// or https://
    if not re.match(r"^https?://", url):
        warnings.append({
            "type": "invalid_url",
            "row": row_id,
            "original": url,
        })
        return "UNKNOWN"

    return url


# ---------------------------------------------------------------------------
# Numeric normalization
# ---------------------------------------------------------------------------

def normalize_numeric(val: str, field: str, warnings: list, row_id: str) -> str:
    """
    Strip currency symbols ($, AUD), trailing 'GB', commas, and whitespace.
    Coerce to a clean numeric string. On failure, return UNKNOWN.
    """
    val = val.strip()

    if is_null(val):
        return "UNKNOWN"

    cleaned = val.upper()
    cleaned = re.sub(r"AUD", "", cleaned)      # strip AUD text
    cleaned = re.sub(r"[$\s]", "", cleaned)    # strip $ and whitespace
    cleaned = re.sub(r"GB$", "", cleaned)       # strip trailing GB
    cleaned = cleaned.replace(",", "")          # strip thousands commas

    # Handle ranges like "2,500-3,000" — take the lower bound
    range_match = re.match(r"^(\d+\.?\d*)-(\d+\.?\d*)$", cleaned)
    if range_match:
        cleaned = range_match.group(1)
        warnings.append({
            "type": "numeric_range_lowered",
            "field": field,
            "row": row_id,
            "original": val,
            "used": cleaned,
        })

    try:
        float(cleaned)
        return cleaned
    except ValueError:
        warnings.append({
            "type": "invalid_numeric",
            "field": field,
            "row": row_id,
            "original": val,
        })
        return "UNKNOWN"


# ---------------------------------------------------------------------------
# Enum normalization
# ---------------------------------------------------------------------------

def normalize_enum(
    val: str,
    display_map: dict,
    field: str,
    warnings: list,
    row_id: str,
    fallback: str = "UNKNOWN",
) -> str:
    """
    Normalize an enum field via exact lowercase match, then partial match.
    Returns the display-cased value or fallback.
    """
    val = val.strip()

    if is_null(val):
        return fallback

    key = val.lower()

    # Exact match
    if key in display_map:
        return display_map[key]

    # Partial / substring match (e.g. "track 1a" -> "Track1A")
    for allowed_key, display_val in display_map.items():
        if allowed_key in key or key in allowed_key:
            warnings.append({
                "type": "enum_coerced",
                "field": field,
                "row": row_id,
                "original": val,
                "coerced_to": display_val,
            })
            return display_val

    warnings.append({
        "type": "enum_invalid",
        "field": field,
        "row": row_id,
        "original": val,
    })
    return fallback


# ---------------------------------------------------------------------------
# Header detection
# ---------------------------------------------------------------------------

def find_header_line(lines: list) -> int:
    """
    Find the index of the canonical header row.
    Requires the line to contain 'date_found' and at least 5 canonical fields.
    Returns -1 if not found.
    """
    for i, line in enumerate(lines):
        lower = line.lower()
        if "date_found" not in lower:
            continue
        hits = sum(1 for col in CANONICAL_HEADER if col in lower)
        if hits >= 5:
            return i
    return -1


def is_repeated_header(line: str) -> bool:
    """Return True if this line looks like a repeated header row."""
    lower = line.lower()
    return "date_found" in lower and sum(
        1 for col in CANONICAL_HEADER if col in lower
    ) >= 5


# ---------------------------------------------------------------------------
# One-line CSV recovery
# ---------------------------------------------------------------------------

def recover_one_line_csv(text: str) -> list:
    """
    If the entire dataset was returned as one long line, split on boundaries
    that look like the start of a new row: a comma followed by an ISO date.

    Uses a lookahead so the date is preserved on each recovered fragment.
    """
    # Boundary: comma immediately before a 4-digit year (20xx)
    pattern = re.compile(r",(?=20\d{2}-\d{2})")
    parts = pattern.split(text)

    if len(parts) > 1:
        return parts  # first part is the first row; rest start with a date

    return [text]


# ---------------------------------------------------------------------------
# Row parsing
# ---------------------------------------------------------------------------

def parse_csv_line(line: str) -> list | None:
    """
    Parse a single CSV line into a list of fields.
    Returns None on CSV parse error.
    """
    try:
        reader = csv.reader(io.StringIO(line))
        return next(reader)
    except Exception:
        return None


def fit_row_to_schema(fields: list, raw_line: str, warnings: list) -> list | None:
    """
    Attempt to fit a parsed row to exactly NUM_COLS columns.

    - Exact: return as-is.
    - Too many cols: collapse extras into the last (notes) field.
    - Too few: return None (send to manual review).
    """
    n = len(fields)

    if n == NUM_COLS:
        return fields

    if n > NUM_COLS:
        # Overflow columns get folded into the notes field
        fitted = fields[: NUM_COLS - 1] + ["; ".join(fields[NUM_COLS - 1 :])]
        warnings.append({
            "type": "row_overflow_collapsed",
            "expected": NUM_COLS,
            "got": n,
            "raw": raw_line[:120],
        })
        return fitted

    # Too few columns — cannot safely assign fields
    return None


# ---------------------------------------------------------------------------
# Main parse pipeline
# ---------------------------------------------------------------------------

def parse_raw_text(raw: str, warnings: list) -> tuple:
    """
    Full input parsing pipeline.

    Returns:
        (good_rows, bad_rows)
        good_rows: list of lists (each list is NUM_COLS fields)
        bad_rows:  list of str  (raw lines that could not be parsed)

    Raises SystemExit on fatal error (no header found).
    """
    text = strip_code_fences(raw)
    text = strip_wrapper_text(text)

    lines = text.splitlines()

    header_idx = find_header_line(lines)
    if header_idx == -1:
        return None, lines  # caller handles fatal

    # Discard everything before the header
    data_lines = lines[header_idx + 1 :]

    # Remove blanks and repeated headers
    clean_lines = []
    for line in data_lines:
        stripped = line.strip()
        if not stripped:
            continue
        if is_repeated_header(stripped):
            warnings.append({"type": "repeated_header_removed", "line": stripped[:80]})
            continue
        clean_lines.append(stripped)

    # One-line CSV recovery: if only one (very long) line, try to split it
    if len(clean_lines) == 1 and len(clean_lines[0]) > 300:
        recovered = recover_one_line_csv(clean_lines[0])
        if len(recovered) > 1:
            warnings.append({
                "type": "one_line_csv_recovered",
                "fragments": len(recovered),
            })
            clean_lines = recovered

    good_rows = []
    bad_rows = []

    for line in clean_lines:
        fields = parse_csv_line(line)

        if fields is None:
            bad_rows.append(line)
            continue

        fitted = fit_row_to_schema(fields, line, warnings)
        if fitted is None:
            bad_rows.append(line)
            warnings.append({
                "type": "row_too_few_columns",
                "expected": NUM_COLS,
                "got": len(fields),
                "raw": line[:120],
            })
            continue

        good_rows.append(fitted)

    return good_rows, bad_rows


# ---------------------------------------------------------------------------
# Row normalization
# ---------------------------------------------------------------------------

def normalize_row(fields: list, warnings: list) -> dict:
    """
    Normalize a single parsed row (list of NUM_COLS values) into a dict.
    Applies null normalization, URL cleanup, numeric cleaning, and enum validation.
    """
    d = dict(zip(CANONICAL_HEADER, fields))
    row_id = collapse_whitespace(d.get("item_name", "?") or "?")

    # Step 1: collapse whitespace on all fields
    for k in d:
        d[k] = collapse_whitespace(d[k])

    # Step 2: null-normalize all non-URL fields
    for k in d:
        if k != "url":
            d[k] = normalize_null(d[k])

    # Step 3: URL
    d["url"] = normalize_url(d["url"], warnings, row_id)

    # Step 4: numeric fields
    for field in ("price_aud", "vram_gb", "unified_memory_gb", "ram_gb"):
        d[field] = normalize_numeric(d[field], field, warnings, row_id)

    # Step 5: enum fields
    d["track"] = normalize_enum(
        d["track"], ENUM_TRACK, "track", warnings, row_id
    )
    d["category"] = normalize_enum(
        d["category"], ENUM_CATEGORY, "category", warnings, row_id
    )
    d["condition"] = normalize_enum(
        d["condition"], ENUM_CONDITION, "condition", warnings, row_id
    )
    d["au_stock_confirmed"] = normalize_enum(
        d["au_stock_confirmed"], ENUM_AU_STOCK, "au_stock_confirmed", warnings, row_id
    )
    d["verification_status"] = normalize_enum(
        d["verification_status"],
        ENUM_VERIFICATION,
        "verification_status",
        warnings,
        row_id,
        fallback="Unverified",  # default for verification is Unverified, not UNKNOWN
    )
    d["status"] = normalize_enum(
        d["status"], ENUM_STATUS, "status", warnings, row_id
    )

    return d


# ---------------------------------------------------------------------------
# Cross-field checks
# ---------------------------------------------------------------------------

def cross_field_checks(d: dict, warnings: list) -> None:
    """
    Add warnings for suspicious field combinations.
    These do not block output — they are informational flags.
    """
    row_id = d.get("item_name", "?")

    # Verified but no real evidence
    if d["verification_status"] == "Verified":
        weak_count = sum([
            d["url"] == "UNKNOWN",
            d["retailer"] == "UNKNOWN",
            d["price_aud"] == "UNKNOWN",
        ])
        if weak_count >= 2:
            warnings.append({
                "type": "suspicious_verified_no_evidence",
                "row": row_id,
                "msg": "verification_status=Verified but url/retailer/price mostly UNKNOWN",
            })

    # Out of Stock contradicts au_stock_confirmed=Yes
    if d["status"] == "Out of Stock" and d["au_stock_confirmed"] == "Yes":
        warnings.append({
            "type": "suspicious_stock_conflict",
            "row": row_id,
            "msg": "status=Out of Stock but au_stock_confirmed=Yes",
        })

    # Apple/unified-memory device — may need category review
    name_lower = d["item_name"].lower()
    if any(kw in name_lower for kw in ("apple", "mac studio", "macbook", " m4 ", " m3 ", " m2 ")):
        warnings.append({
            "type": "apple_device_detected",
            "row": row_id,
            "msg": "Apple product — verify category and unified_memory_gb vs vram_gb mapping",
        })

    # Mini PC with what looks like a discrete GPU
    if d["category"] == "Mini PC" and d["gpu_model"] not in ("UNKNOWN", ""):
        if any(kw in d["gpu_model"].upper() for kw in ("RTX ", "GTX ", " RX ")):
            warnings.append({
                "type": "mini_pc_discrete_gpu_flag",
                "row": row_id,
                "msg": "Mini PC with apparent discrete GPU — confirm if unified-memory device",
            })

    # Track1B (AMD Strix Halo) but vram_gb populated and unified_memory_gb UNKNOWN
    if d["track"] == "Track1B" and d["unified_memory_gb"] == "UNKNOWN" and d["vram_gb"] != "UNKNOWN":
        warnings.append({
            "type": "track1b_missing_unified_memory",
            "row": row_id,
            "msg": "Track1B (Strix Halo) row has vram_gb but not unified_memory_gb — check field mapping",
        })


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def dedup_rows(rows: list, warnings: list) -> list:
    """
    Deduplicate normalized rows using:
      1. URL (when valid and not UNKNOWN)
      2. Fallback: composite key of item_name + retailer + gpu_model + price_aud

    Keeps the first occurrence of each key; logs removed duplicates.
    """
    seen_urls: dict = {}
    seen_composite: dict = {}
    out = []

    for d in rows:
        url_key = d["url"] if d["url"] != "UNKNOWN" else None
        composite = (
            f'{d["item_name"].lower()}|{d["retailer"].lower()}'
            f'|{d["gpu_model"].lower()}|{d["price_aud"]}'
        )

        if url_key and url_key in seen_urls:
            warnings.append({
                "type": "duplicate_removed",
                "row": d["item_name"],
                "key_type": "url",
                "key": url_key,
            })
            continue

        if composite in seen_composite:
            warnings.append({
                "type": "duplicate_removed",
                "row": d["item_name"],
                "key_type": "composite",
                "key": composite,
            })
            continue

        if url_key:
            seen_urls[url_key] = True
        seen_composite[composite] = True
        out.append(d)

    return out


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------

def write_processed_csv(path: Path, rows: list) -> None:
    """Write normalized rows to a clean CSV."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CANONICAL_HEADER)
        writer.writeheader()
        writer.writerows(rows)


def write_manual_review_csv(path: Path, bad_rows: list) -> None:
    """Write unparseable raw lines to a manual-review CSV."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["raw_line"])
        for line in bad_rows:
            writer.writerow([line])


def write_log(path: Path, log: dict) -> None:
    """Write the normalization log as JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Normalize raw Gemini/NotebookLM hardware CSV output.\n\n"
            "Handles malformed one-line CSV, code fences, repeated headers,\n"
            "bad enums, truncated URLs, and column mismatches."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "input_file",
        help="Path to raw input file (plain text or CSV from Gemini/NotebookLM)",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        metavar="DIR",
        help=(
            "Output directory for processed files. "
            "Defaults to NotebookLM_Workspaces/intake/processed/ "
            "relative to the project root."
        ),
    )
    return parser


def resolve_out_dir(args_out_dir: str | None) -> Path:
    """Resolve the output directory, creating it if necessary."""
    if args_out_dir:
        out_dir = Path(args_out_dir).resolve()
    else:
        # Script lives at <project_root>/scripts/normalize_intake.py
        project_root = Path(__file__).parent.parent
        out_dir = project_root / "NotebookLM_Workspaces" / "intake" / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def print_summary(counts: dict, warnings: list, paths: dict) -> None:
    """Print a human-readable summary to stdout."""
    print("\n✅ Normalization complete.")
    print(f"   Input rows parsed    : {counts['parsed_good']}")
    print(f"   Sent to manual review: {counts['manual_review']}")
    print(f"   After deduplication  : {counts['after_dedup']}")
    print(f"   Duplicates removed   : {counts['duplicates_removed']}")
    print(f"   Warnings logged      : {counts['warnings_total']}")

    if warnings:
        # Summarize warning types
        type_counts: dict = {}
        for w in warnings:
            t = w.get("type", "other")
            type_counts[t] = type_counts.get(t, 0) + 1
        print("\n   Warning breakdown:")
        for wtype, cnt in sorted(type_counts.items()):
            print(f"     {cnt:3d}  {wtype}")

    print(f"\n   Processed CSV   → {paths['processed']}")
    print(f"   Manual review   → {paths['review']}")
    print(f"   Normalization log → {paths['log']}")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    input_path = Path(args.input_file).resolve()
    if not input_path.exists():
        print(f"❌  Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    out_dir = resolve_out_dir(args.out_dir)
    stem = input_path.stem

    processed_path = out_dir / f"{stem}_processed.csv"
    review_path    = out_dir / f"{stem}_manual_review.csv"
    log_path       = out_dir / f"{stem}_normalization_log.json"

    # Read
    print(f"📥 Reading: {input_path}")
    raw = input_path.read_text(encoding="utf-8", errors="replace")

    warnings: list = []

    # Parse
    good_rows, bad_rows = parse_raw_text(raw, warnings)

    if good_rows is None:
        print(
            "❌  FATAL: Could not find the canonical header in the input file.",
            file=sys.stderr,
        )
        print(
            f"   Expected a line containing: {CANONICAL_HEADER[0]},{CANONICAL_HEADER[1]},...",
            file=sys.stderr,
        )
        sys.exit(2)

    print(f"   Parsed: {len(good_rows)} rows OK, {len(bad_rows)} sent to manual review.")

    # Normalize
    normalized = []
    for row in good_rows:
        d = normalize_row(row, warnings)
        cross_field_checks(d, warnings)
        normalized.append(d)

    # Deduplicate
    before = len(normalized)
    normalized = dedup_rows(normalized, warnings)
    after = len(normalized)

    # Build counts for log
    counts = {
        "parsed_good": len(good_rows),
        "manual_review": len(bad_rows),
        "after_dedup": after,
        "duplicates_removed": before - after,
        "warnings_total": len(warnings),
    }

    # Write outputs
    write_processed_csv(processed_path, normalized)
    write_manual_review_csv(review_path, bad_rows)

    log = {
        "run_timestamp": datetime.now().isoformat(),
        "input_file": str(input_path),
        "counts": counts,
        "warnings": warnings,
    }
    write_log(log_path, log)

    print_summary(
        counts,
        warnings,
        {"processed": processed_path, "review": review_path, "log": log_path},
    )


if __name__ == "__main__":
    main()
