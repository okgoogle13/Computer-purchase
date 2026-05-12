#!/usr/bin/env python3
"""Deterministic harvest of candidate recommendations from markdown logs."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")
VRAM_RE = re.compile(r"(?i)\b(?:gpu|vram)\b[^\d]*(\d{1,3})\s*gb\b")
PRICE_RE = re.compile(
    r"(?i)(?:A\$|AU\$)\s*([0-9][0-9,]*(?:\.[0-9]{1,2})?)|AUD\s*\$?\s*([0-9][0-9,]*(?:\.[0-9]{1,2})?)"
)
PRODUCT_HEADING_RE = re.compile(
    r"(?i)\b("
    r"rtx|rx|radeon|geforce|legion|rog|alienware|thinkstation|zephyrus|"
    r"predator|titan|raider|omen|proart|strix|ryzen ai max|threadripper|quadro"
    r")\b"
)
AUD_CONTEXT_RE = re.compile(r"(?i)\bAUD\b|A\$\s*\d|AU\$\s*\d")


def normalize_item_name(value: str) -> str:
    """Lowercase and remove parenthetical noise and punctuation."""
    no_paren = re.sub(r"\([^)]*\)", " ", value)
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", " ", no_paren).lower()
    return " ".join(cleaned.split())


def _parse_number(value: str) -> float:
    return float(value.replace(",", ""))


def extract_candidates_from_log(log_text: str) -> list[dict[str, Any]]:
    """Parse markdown headings and attach explicit price/VRAM evidence lines."""
    rows: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for raw_line in log_text.splitlines():
        line = raw_line.strip()

        m_heading = HEADING_RE.match(raw_line)
        if m_heading:
            if current:
                rows.append(current)
            heading_text = m_heading.group(1)
            if not PRODUCT_HEADING_RE.search(heading_text):
                current = None
                continue
            current = {"item_name": normalize_item_name(heading_text)}
            continue

        if not current:
            continue

        m_vram = VRAM_RE.search(line)
        if m_vram:
            vram = int(m_vram.group(1))
            if 1 <= vram <= 96:
                current["vram_gb"] = vram

        m_price = PRICE_RE.search(line)
        if m_price and AUD_CONTEXT_RE.search(line):
            amount = m_price.group(1) or m_price.group(2)
            current["price_aud"] = _parse_number(amount)

    if current:
        rows.append(current)

    return rows


def _is_populated(value: Any) -> bool:
    if value is None:
        return False
    text = str(value).strip()
    return text != "" and text.upper() != "UNKNOWN"


def decide_action(shortlist_row: dict[str, Any] | None) -> str:
    """Choose deterministic action for a candidate vs shortlist row."""
    if not shortlist_row:
        return "append_new"

    required = (
        "MCDA_Total",
        "effective_best_price_aud",
        "current_best_url",
        "in_stock_now",
        "seller_class",
        "source_platform",
    )
    if all(_is_populated(shortlist_row.get(key)) for key in required):
        return "skip_existing"

    return "update_partial"


def dedupe_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Merge duplicate item names, preferring populated fields from newer entries."""
    merged_candidates: dict[str, dict[str, Any]] = {}
    for candidate in candidates:
        item_name = candidate["item_name"]
        if item_name not in merged_candidates:
            merged_candidates[item_name] = dict(candidate)
            continue
        existing = merged_candidates[item_name]
        for key, value in candidate.items():
            if key == "item_name":
                continue
            if _is_populated(value):
                existing[key] = value
    return list(merged_candidates.values())


def _load_shortlist(path: Path) -> list[dict[str, Any]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def _canonical_item_key(value: str) -> str:
    key = normalize_item_name(value)
    stopwords = {
        "refurb",
        "refurbished",
        "renewed",
        "used",
        "listing",
        "ebay",
        "outlet",
        "open",
        "box",
    }
    parts = [p for p in key.split() if p not in stopwords]
    return " ".join(parts)


def _match_shortlist_row(
    shortlist_rows: list[dict[str, Any]], candidate_item_name: str
) -> dict[str, Any] | None:
    candidate_key = _canonical_item_key(candidate_item_name)
    for row in shortlist_rows:
        source_name = row.get("item_name") or row.get("Machine") or ""
        if normalize_item_name(source_name) == candidate_item_name:
            return row
        if _canonical_item_key(source_name) == candidate_key:
            return row
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Harvest LLM recommendations deterministically")
    parser.add_argument("--log", required=True, help="Path to markdown log")
    parser.add_argument("--shortlist", required=True, help="Path to shortlist CSV")
    parser.add_argument("--out", required=True, help="Path to output JSON report")
    args = parser.parse_args()

    log_text = Path(args.log).read_text(encoding="utf-8")
    candidates = extract_candidates_from_log(log_text)
    unique_candidates = dedupe_candidates(candidates)

    shortlist_rows = _load_shortlist(Path(args.shortlist))

    actions: list[dict[str, Any]] = []
    counts = {"skip_existing": 0, "append_new": 0, "update_partial": 0}

    for candidate in unique_candidates:
        shortlist_row = _match_shortlist_row(shortlist_rows, candidate["item_name"])
        action = decide_action(shortlist_row=shortlist_row)
        counts[action] += 1
        actions.append({"item_name": candidate["item_name"], "action": action})

    report = {
        "counts": {"total_candidates": len(unique_candidates), **counts},
        "actions": actions,
    }

    out_path = Path(args.out)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
