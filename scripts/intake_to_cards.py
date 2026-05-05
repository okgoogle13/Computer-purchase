#!/usr/bin/env python3
"""
intake_to_cards.py — Convert normalized intake CSV into Markdown product cards.

Reads a *_processed.csv from NotebookLM_Workspaces/intake/processed/ and emits
one .md product card per row into the appropriate lane folder under
NotebookLM_Workspaces/.

Usage:
    python scripts/intake_to_cards.py NotebookLM_Workspaces/intake/processed/2026-05-05_notebooklm_batch1_processed.csv
    python scripts/intake_to_cards.py path/to/file.csv --dry-run
    python scripts/intake_to_cards.py path/to/file.csv --overwrite
    python scripts/intake_to_cards.py path/to/file.csv --skip-existing

Output folders (relative to repo root):
    Laptop            → 04_Laptops_Mainline/
    Desktop (New)     → 03_New_Desktop_Systems/
    Desktop (Refurb)  → 02_Refurbished_Desktop_Towers/
    Desktop (Gaming Refurb) → Desktop_Gaming_Refurbished/
    Mini PC / eGPU    → 06_Mini_PCs_and_eGPU/
    Component / GPU   → 09_Individual_Components/
    DIY Build         → 08_Custom_Builds/
    Apple Silicon     → 05_Apple_Silicon_Systems/
    Fallback          → 01_Research_Methods_and_Decision_System/

Behaviour on filename collision:
    Default  → skip and log (safe)
    --overwrite → replace existing
    --dry-run   → show what would be written, write nothing
"""

import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = REPO_ROOT / "NotebookLM_Workspaces"

# Category/condition → target folder mapping
# Evaluated in order; first match wins.
ROUTING_RULES: list[tuple[str, str, str, str]] = [
    # (category_pattern, condition_pattern, note, folder_name)
    ("mini pc|egpu",         r".*",           "Mini PC / eGPU",       "06_Mini_PCs_and_eGPU"),
    ("component|gpu",        r".*",           "Standalone component",  "09_Individual_Components"),
    ("diy build|custom",     r".*",           "DIY / Custom build",    "08_Custom_Builds"),
    ("apple",                r".*",           "Apple Silicon",         "05_Apple_Silicon_Systems"),
    # Laptop – all conditions to main lane (no separate refurb lane for laptops)
    ("laptop",               r".*",           "Laptop",                "04_Laptops_Mainline"),
    # Desktops – split on condition
    ("desktop",              r"refurb|used|open box", "Refurb desktop", "02_Refurbished_Desktop_Towers"),
    ("desktop",              r"new",          "New desktop",           "03_New_Desktop_Systems"),
    # Fallback desktop catch-all
    ("desktop",              r".*",           "Desktop (uncategorised)","03_New_Desktop_Systems"),
]

FALLBACK_FOLDER = "01_Research_Methods_and_Decision_System"

# Condition → condition tags
CONDITION_TAG_MAP = {
    "new":        "#New",
    "refurbished":"#Refurbished",
    "used":       "#Used",
    "open box":   "#OpenBox",
}

# Track → track tags
TRACK_TAG_MAP = {
    "track1a":  "#Track1A",
    "track1b":  "#Track1B",
    "track1.5": "#Track1-5",
    "track2a":  "#Track2A",
    "track2b":  "#Track2B",
    "track2c":  "#Track2C",
}

# VRAM threshold tags
def vram_tag(vram_str: str) -> str:
    try:
        v = float(vram_str)
        if v >= 48:
            return "#VRAM-48GB+"
        elif v >= 24:
            return "#VRAM-24GB"
        elif v >= 16:
            return "#VRAM-16GB"
        elif v >= 8:
            return "#VRAM-8GB"
        else:
            return "#VRAM-Unknown"
    except (ValueError, TypeError):
        return "#VRAM-Unknown"


# ---------------------------------------------------------------------------
# Routing
# ---------------------------------------------------------------------------

def route_row(row: dict) -> tuple[Path, str]:
    """Return (target_folder_path, routing_note)."""
    cat   = (row.get("category") or "").strip().lower()
    cond  = (row.get("condition") or "").strip().lower()

    for cat_pat, cond_pat, note, folder in ROUTING_RULES:
        if re.search(cat_pat, cat) and re.search(cond_pat, cond, re.IGNORECASE):
            return WORKSPACE / folder, note

    return WORKSPACE / FALLBACK_FOLDER, "Fallback — unrecognised category/condition"


# ---------------------------------------------------------------------------
# Slug generation
# ---------------------------------------------------------------------------

def slugify(text: str, maxlen: int = 60) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text.strip())
    text = re.sub(r"-{2,}", "-", text)
    return text[:maxlen].rstrip("-")


def make_filename(row: dict, index: int) -> str:
    name  = row.get("item_name") or "unknown-item"
    slug  = slugify(name)
    return f"intake-{index:03d}_{slug}.md"


# ---------------------------------------------------------------------------
# Tag assembly
# ---------------------------------------------------------------------------

def build_tags(row: dict) -> str:
    tags: list[str] = []

    cat = (row.get("category") or "").strip().lower()
    if "laptop"    in cat: tags.append("#Laptop")
    elif "desktop" in cat: tags.append("#Desktop")
    elif "mini pc" in cat: tags.append("#MiniPC")
    elif "egpu"    in cat: tags.append("#eGPU")
    elif "component" in cat or "gpu" in cat: tags.append("#Component")
    elif "diy"     in cat or "custom" in cat: tags.append("#CustomBuild")
    elif "apple"   in cat: tags.append("#AppleSilicon")

    gpu = (row.get("gpu_model") or "").upper()
    if "RTX" in gpu or "NVIDIA" in gpu: tags.append("#NVIDIA")
    elif "RX " in gpu or "RADEON" in gpu or "AMD" in gpu: tags.append("#AMD")
    elif "ARC" in gpu: tags.append("#Intel")

    tags.append(vram_tag(row.get("vram_gb") or "0"))

    cond = (row.get("condition") or "").strip().lower()
    tags.append(CONDITION_TAG_MAP.get(cond, "#ConditionUnknown"))

    track_key = (row.get("track") or "").strip().lower()
    tags.append(TRACK_TAG_MAP.get(track_key, "#TrackUnknown"))

    vstatus = (row.get("verification_status") or "").strip()
    if vstatus == "Verified":        tags.append("#Verified")
    elif vstatus == "Needs Verification": tags.append("#NeedsVerification")
    else:                            tags.append("#Unverified")

    au = (row.get("au_stock_confirmed") or "").strip()
    if au == "Yes":  tags.append("#AUStock-Confirmed")
    elif au == "No": tags.append("#AUStock-No")
    else:            tags.append("#AUStock-Unknown")

    return " ".join(tags)


# ---------------------------------------------------------------------------
# Card rendering
# ---------------------------------------------------------------------------

def fmt(val: str | None, fallback: str = "UNKNOWN") -> str:
    v = (val or "").strip()
    return v if v and v.upper() not in ("UNKNOWN", "N/A", "NONE", "") else fallback


def url_md(url: str | None) -> str:
    u = fmt(url)
    if u == "UNKNOWN":
        return "UNKNOWN"
    return f"[{u}]({u})"


def checkbox(label: str, done: bool = False) -> str:
    mark = "x" if done else " "
    return f"- [{mark}] {label}"


def render_card(row: dict, tags: str, routing_note: str, source_batch: str) -> str:
    name     = fmt(row.get("item_name"), "Unnamed Item")
    slug_id  = slugify(name)
    cat      = fmt(row.get("category"))
    track    = fmt(row.get("track"))
    pathway  = fmt(row.get("pathway"))
    gpu      = fmt(row.get("gpu_model"))
    vram     = fmt(row.get("vram_gb"))
    unified  = fmt(row.get("unified_memory_gb"))
    ram      = fmt(row.get("ram_gb"))
    cpu      = fmt(row.get("cpu_model"))
    cond     = fmt(row.get("condition"))
    price    = fmt(row.get("price_aud"))
    retailer = fmt(row.get("retailer"))
    url      = url_md(row.get("url"))
    au_stock = fmt(row.get("au_stock_confirmed"))
    vstatus  = fmt(row.get("verification_status"))
    status   = fmt(row.get("status"))
    notes    = fmt(row.get("notes"), "No notes.")
    date_f   = fmt(row.get("date_found"))

    price_str = f"${price} AUD" if price != "UNKNOWN" else "UNKNOWN"
    vram_str  = f"{vram} GB" if vram != "UNKNOWN" else "UNKNOWN"
    unified_str = f"{unified} GB" if unified != "UNKNOWN" else "UNKNOWN"
    ram_str   = f"{ram} GB" if ram != "UNKNOWN" else "UNKNOWN"

    # --- Frontmatter + tag comment ---
    lines = [
        f"<!-- TAGS: {tags} -->",
        f"<!-- INTAKE: batch={source_batch} date={date_f} route={routing_note} -->",
        "---",
        f"id: {slug_id}",
        f"category: {cat.lower()}",
        f"track: {track}",
        f"pathway: {pathway}",
        f"name: {name}",
        f"gpu: {gpu}",
        f"vram: {vram_str}",
        f"unified_memory: {unified_str}",
        f"price_aud: {price_str}",
        f"condition: {cond}",
        f"au_stock: {au_stock}",
        f"verification: {vstatus}",
        f"status: {status}",
        "score: UNKNOWN — pending manual review",
        "---",
        "",
        f"# {name}",
        "",
    ]

    # Warn banner if unverified
    if vstatus in ("UNKNOWN", "Unverified"):
        lines += [
            "> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**",
            "> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.",
            "",
        ]

    # --- Track status block ---
    lines += [
        "## Track Status",
        f"- **Track:** {track}",
        f"- **Pathway:** {pathway}",
        f"- **Status:** {status}",
        f"- **AU Stock Confirmed:** {au_stock}",
        f"- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below",
        "",
    ]

    # --- Overview ---
    lines += [
        "## Overview",
        f"- **Price (AUD):** {price_str}",
        f"- **Retailer:** {retailer}",
        f"- **URL:** {url}",
        f"- **Condition:** {cond}",
        f"- **Source batch:** {source_batch} (ingested {date_f})",
        "",
    ]

    # --- Key Specs ---
    lines += [
        "## Key Specs",
        f"- **GPU:** {gpu}",
        f"- **VRAM:** {vram_str}",
        f"- **Unified Memory:** {unified_str}",
        f"- **CPU:** {cpu}",
        f"- **RAM:** {ram_str}",
        "- **Storage:** UNKNOWN",
        "- **PSU / Charger:** UNKNOWN",
        "- **Warranty (AU):** UNKNOWN",
        "",
    ]

    # --- Notes from batch ---
    lines += [
        "## Source Notes",
        notes,
        "",
    ]

    # --- AI capability stub ---
    ai_cap = "UNKNOWN — to be completed after manual spec verification."
    if vram != "UNKNOWN":
        try:
            v = float(vram)
            if v >= 48:
                ai_cap = "Exceptional — 48 GB+ VRAM supports 70B+ models fully in VRAM at Q4."
            elif v >= 24:
                ai_cap = "Strong — 24 GB VRAM handles 30B–34B Q4 models natively."
            elif v >= 16:
                ai_cap = "Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading."
            elif v >= 8:
                ai_cap = "Baseline — 8 GB VRAM sufficient for 7B Q4; larger models require significant offload."
        except ValueError:
            pass

    lines += [
        "## AI Capability Summary",
        ai_cap,
        "",
    ]

    # --- Verification checklist ---
    au_confirmed  = au_stock == "Yes"
    price_known   = price != "UNKNOWN"
    gpu_known     = gpu != "UNKNOWN"
    cpu_known     = cpu != "UNKNOWN"
    ram_known     = ram != "UNKNOWN"

    lines += [
        "## Verification Checklist",
        checkbox("Confirm AU stock from named retailer with URL", au_confirmed),
        checkbox("Confirm price in AUD",                         price_known),
        checkbox("Confirm GPU model and VRAM",                   gpu_known),
        checkbox("Confirm CPU model",                            cpu_known),
        checkbox("Confirm RAM installed and max supported",      ram_known),
        checkbox("Confirm storage installed and free M.2 slots", False),
        checkbox("Confirm PSU / charger wattage",                False),
        checkbox("Confirm warranty term and type (AU)",          False),
        checkbox("Check thermal reputation (reviews)",           False),
        checkbox("Confirm AGENTS.md GOOD ENOUGH gate cleared",   False),
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Convert normalized intake CSV to Markdown product cards.")
    parser.add_argument("input_csv", help="Path to *_processed.csv")
    parser.add_argument("--dry-run",       action="store_true", help="Preview output; do not write files")
    parser.add_argument("--overwrite",     action="store_true", help="Overwrite existing card files")
    parser.add_argument("--skip-existing", action="store_true", help="Skip (default) rows whose card file already exists")
    args = parser.parse_args()

    input_path = Path(args.input_csv).resolve()
    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    source_batch = input_path.stem  # e.g. 2026-05-05_notebooklm_batch1_processed

    rows = []
    with open(input_path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            rows.append(row)

    print(f"\n📋 Processing: {input_path.name}")
    print(f"   Rows found: {len(rows)}")
    if args.dry_run:
        print("   [DRY RUN] — no files will be written\n")

    log: list[dict] = []
    written = skipped = errored = 0

    for idx, row in enumerate(rows, start=1):
        item_name = row.get("item_name") or f"row-{idx}"
        try:
            folder, routing_note = route_row(row)
            tags     = build_tags(row)
            filename = make_filename(row, idx)
            out_path = folder / filename

            card = render_card(row, tags, routing_note, source_batch)

            if args.dry_run:
                print(f"  [{idx:03d}] DRY-RUN → {out_path.relative_to(REPO_ROOT)}")
                print(f"          route: {routing_note}")
                written += 1
                log.append({"index": idx, "item": item_name, "action": "dry-run", "path": str(out_path)})
                continue

            if out_path.exists() and not args.overwrite:
                print(f"  [{idx:03d}] SKIP (exists) → {out_path.relative_to(REPO_ROOT)}")
                skipped += 1
                log.append({"index": idx, "item": item_name, "action": "skipped", "path": str(out_path)})
                continue

            folder.mkdir(parents=True, exist_ok=True)
            out_path.write_text(card, encoding="utf-8")
            action = "overwrite" if out_path.exists() else "written"
            print(f"  [{idx:03d}] ✅ {action.upper()} → {out_path.relative_to(REPO_ROOT)}")
            written += 1
            log.append({"index": idx, "item": item_name, "action": action, "path": str(out_path), "route": routing_note})

        except Exception as exc:  # noqa: BLE001
            print(f"  [{idx:03d}] ❌ ERROR — {item_name}: {exc}", file=sys.stderr)
            errored += 1
            log.append({"index": idx, "item": item_name, "action": "error", "error": str(exc)})

    # --- Write run log ---
    log_dir = input_path.parent
    log_stem = input_path.stem.replace("_processed", "")
    log_path = log_dir / f"{log_stem}_cards_log.json"
    if not args.dry_run:
        log_path.write_text(json.dumps({
            "run_timestamp": datetime.now().isoformat(),
            "input_file": str(input_path),
            "counts": {
                "total_rows": len(rows),
                "written":    written,
                "skipped":    skipped,
                "errored":    errored,
            },
            "entries": log,
        }, indent=2), encoding="utf-8")

    # --- Summary ---
    print(f"""
✅ Card generation complete.
   Written  : {written}
   Skipped  : {skipped}
   Errors   : {errored}
""")
    if not args.dry_run:
        print(f"   Run log  → {log_path.relative_to(REPO_ROOT)}\n")


if __name__ == "__main__":
    main()
