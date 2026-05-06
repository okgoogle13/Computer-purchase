This file is a merged representation of a subset of the codebase, containing specifically included files, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: NotebookLM_Workspaces/intake/shortlist/test_shortlist.csv, NotebookLM_Workspaces/**/intake-011*.md, NotebookLM_Workspaces/**/intake-009*.md, NotebookLM_Workspaces/**/intake-052*.md, NotebookLM_Workspaces/**/intake-010*.md, AGENTS.md, config/*.json, scripts/*.py
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
config/
  procurement_policy.json
NotebookLM_Workspaces/
  04_Laptops_Mainline/
    intake-009_lenovo-legion-pro-7i.md
    intake-010_msi-raider-18-hx-ai-a2xwjg.md
    intake-011_dell-alienware-m18-r2-area-51.md
    intake-052_acer-predator-helios-neo-16s-ai-rtx-5060.md
  intake/
    shortlist/
      test_shortlist.csv
scripts/
  build_shortlist.py
  enrich_shortlist_pricing.py
  intake_to_cards.py
  normalize_intake.py
AGENTS.md
```

# Files

## File: config/procurement_policy.json
````json
{
  "budget_cap_aud": 4500.0,
  "desktop_minimum_vram_gb": 8.0,
  "laptop_discrete_minimum_vram_gb": 8.0,
  "laptop_unified_minimum_vram_gb": 16.0,
  "exceptional_overrides": {
    "vram_threshold_gb": 24.0,
    "gpu_tier_threshold": 8.0,
    "max_override_budget_aud": 6000.0
  },
  "shortlist_behavior": {
    "over_budget_action": "soft_penalty",
    "unknown_price_action": "soft_penalty",
    "out_of_stock_action": "hard_reject",
    "below_vram_floor_action": "hard_reject"
  }
}
````

## File: NotebookLM_Workspaces/intake/shortlist/test_shortlist.csv
````
intake_id,item_name,profile,category,Category_Group,track,pathway,gpu_model,vram_gb,unified_memory_gb,price_aud,Over_Budget,Price_Unknown,condition,retailer,verification_status,au_stock,status,batch,source_file,exceptional_override,shortlist_reason,soft_penalty_notes,Machine,Type,VRAM_Adequacy,GPU_Compute_Tier,Value_Score,Price_to_Perf,Condition_Risk,Verification_Confidence,Sustained_TGP_Rating,Portability_Score
intake-009,Lenovo Legion Pro 7i,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 4090 Mobile,16.0,UNKNOWN,4575.0,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-009_lenovo-legion-pro-7i.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $4,575.00); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-009,Candidate,,,,,,,,
intake-010,MSI Raider 18 HX AI A2XWJG,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090 Mobile,24.0,UNKNOWN,8488.0,Yes,,New,UNKNOWN,Verified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-010_msi-raider-18-hx-ai-a2xwjg.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $8,488.00); AU stock: UNKNOWN",intake-010,Candidate,,,,,,,,
intake-011,Dell Alienware m18 R2 / Area-51,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090 Mobile,24.0,UNKNOWN,4499.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-011_dell-alienware-m18-r2-area-51.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-011,Candidate,,,,,,,,
intake-052,Acer Predator Helios Neo 16S AI RTX 5060,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5060,8.0,UNKNOWN,2399.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-052_acer-predator-helios-neo-16s-ai-rtx-5060.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-052,Candidate,,,,,,,,
````

## File: scripts/build_shortlist.py
````python
#!/usr/bin/env python3
"""
build_shortlist.py — Phase 2 of the hardware procurement pipeline.

Scans all intake-*.md product cards, applies AGENTS.md hard-gate filters,
and emits two CSVs:

  shortlist.csv  — candidates that passed all gates, with blank score columns
                   ready to be manually filled and fed into rubric_weighting_engine.py
  rejected.csv   — filtered-out rows with the reason for rejection

Usage:
    python scripts/build_shortlist.py
    python scripts/build_shortlist.py --dry-run
    python scripts/build_shortlist.py --batch 2026-05-05_notebooklm_batch1
    python scripts/build_shortlist.py --profile laptop
    python scripts/build_shortlist.py --include-unknowns

Output folder: NotebookLM_Workspaces/intake/shortlist/

After filling in the score columns (0-10), run:
    python scripts/rubric_weighting_engine.py --profile merged \\
        --csv NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist.csv
"""

import argparse
import csv
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPO_ROOT  = Path(__file__).resolve().parent.parent
WORKSPACE  = REPO_ROOT / "NotebookLM_Workspaces"

# Loads config
def load_config() -> dict:
    config_path = REPO_ROOT / "config" / "procurement_policy.json"
    if not config_path.exists():
        sys.exit(f"Error: Config file not found at {config_path}. Please create it.")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Lanes that contain intake cards
INTAKE_LANES = [
    "02_Refurbished_Desktop_Towers",
    "03_New_Desktop_Systems",
    "04_Laptops_Mainline",
    "06_Mini_PCs_and_eGPU",
    "08_Custom_Builds",
    "09_Individual_Components",
    "05_Apple_Silicon_Systems",
    "01_Research_Methods_and_Decision_System",
]

# GPU model substrings that indicate professional/workstation-class cards
WORKSTATION_GPU_KEYWORDS = [
    "RTX PRO", "RTX 6000", "RTX 5000 ADA", "RTX 4000 ADA", "RTX 3000 ADA",
    "RTX 2000 ADA", "A6000", "A5000", "A4500", "A4000", "A2000",
    "QUADRO", "RADEON PRO W", "ARC PRO",
]

# Merged score columns — filled manually after shortlisting
SCORE_COLUMNS = [
    "VRAM_Adequacy",          # 10=48GB+/128GB unified, 8=24GB, 5=16GB, 2=8GB, 0=<8GB
    "GPU_Compute_Tier",       # 10=RTX5090/4090 Pro, 8=RTX3090/4090M/5080, 6=RTX5070Ti/4080
    "Value_Score",            # 10=exceptional price/VRAM ratio, 5=average, 0=poor
    "Price_to_Perf",          # 10=best-in-class overall value, 5=fair, 0=overpriced
    "Condition_Risk",         # 10=New+warranty, 8=OpenBox, 6=Refurb+warranty, 4=Used, 0=Unknown
    "Verification_Confidence",# 10=AU stock+URL confirmed, 5=needs verification, 2=unverified
    "Sustained_TGP_Rating",   # 10=>=175W, 8=150W, 6=120W, 0=N/A (desktop/component)
    "Portability_Score",      # 10=<2kg, 7=2-2.5kg, 4=2.5-3kg, 1=3kg+, 0=N/A (non-mobile)
]


# ---------------------------------------------------------------------------
# Frontmatter parser
# ---------------------------------------------------------------------------

def parse_frontmatter(md_text: str) -> dict:
    """
    Extract YAML frontmatter from a markdown file (between first pair of ---).
    Returns a dict of key: value pairs (all strings).
    """
    match = re.search(r"---\s*\n(.*?)\n---", md_text, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        fm[key.strip()] = val.strip()
    return fm


def parse_tags_comment(md_text: str) -> dict:
    """
    Extract batch name from the INTAKE comment line if present.
    <!-- INTAKE: batch=X date=Y route=Z -->
    """
    match = re.search(r"<!-- INTAKE: batch=(\S+)", md_text)
    return {"batch": match.group(1)} if match else {}


# ---------------------------------------------------------------------------
# Classification helpers
# ---------------------------------------------------------------------------

def classify_profile(category: str) -> str:
    """Map category string to a human-readable profile label."""
    cat = category.lower()
    if "laptop" in cat:
        return "Laptop"
    if "mini pc" in cat or "egpu" in cat:
        return "Mini PC"
    if "component" in cat or "gpu" in cat:
        return "Component"
    if "apple" in cat:
        return "Apple Silicon"
    # desktop / diy build / everything else
    return "Desktop"


def classify_category_group(profile: str, gpu_model: str) -> str:
    """Classify into Complete_System / Standalone_GPU / Workstation_GPU."""
    if profile == "Component":
        gpu_upper = gpu_model.upper()
        if any(kw in gpu_upper for kw in WORKSTATION_GPU_KEYWORDS):
            return "Workstation_GPU"
        return "Standalone_GPU"
    return "Complete_System"


# ---------------------------------------------------------------------------
# Numeric helpers
# ---------------------------------------------------------------------------

def parse_price(price_str: str) -> tuple[float | None, bool]:
    """
    Return (price_float_or_None, is_unknown).
    Strips $, AUD, commas, GB suffixes.
    """
    cleaned = price_str.strip().upper()
    if not cleaned or cleaned in ("UNKNOWN", "N/A", "NONE", "-"):
        return None, True
    cleaned = re.sub(r"[AUD$\s]", "", cleaned).replace(",", "")
    try:
        return float(cleaned), False
    except ValueError:
        return None, True


def parse_vram(vram_str: str) -> float | None:
    """Return numeric VRAM GB or None if unknown."""
    cleaned = re.sub(r"[^0-9.]", "", vram_str.strip())
    try:
        return float(cleaned) if cleaned else None
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Policy Evaluator
# ---------------------------------------------------------------------------

def evaluate_policy(row: dict, config: dict) -> dict:
    """
    Evaluate against config rules (Hard Rejects vs Soft Penalties).
    Returns dict:
      hard_reject_reason: str | None
      soft_penalty_notes: list
      exceptional_override: str | None
      shortlist_reason: str
      over_budget: bool
    """
    profile        = row["profile"]
    status         = row["status"].lower()
    price_unknown  = row["Price_Unknown"] == "Yes"
    price_val      = row["_price_float"]
    vram_val       = row["_vram_float"]
    unified_val    = row["_unified_float"]

    # Load thresholds from config
    budget_cap        = config.get("budget_cap_aud", 4500.0)
    behavior          = config.get("shortlist_behavior", {})
    exc_vram          = config.get("exceptional_overrides", {}).get("vram_threshold_gb", 24.0)
    exc_max_budget    = config.get("exceptional_overrides", {}).get("max_override_budget_aud", 6000.0)

    hard_reject_reason = None
    soft_penalty_notes = []
    exceptional_override = None
    is_over_budget = False

    # Gate 1: Out of Stock
    if "out of stock" in status:
        if behavior.get("out_of_stock_action") == "hard_reject":
            hard_reject_reason = "Out of Stock"
            return {"hard_reject_reason": hard_reject_reason, "soft_penalty_notes": [], "exceptional_override": None, "shortlist_reason": "", "over_budget": False}

    # Gate 2: VRAM floor (Complete Systems only)
    if row["Category_Group"] == "Complete_System":
        if profile in ("Laptop", "Mini PC", "Apple Silicon"):
            floor_dis = config.get("laptop_discrete_minimum_vram_gb", 8.0)
            floor_uni = config.get("laptop_unified_minimum_vram_gb", 16.0)
            effective_vram = vram_val or 0
            effective_unified = unified_val or 0
            
            # If both are known or partially known and fail:
            if vram_val is not None or unified_val is not None:
                if effective_vram < floor_dis and effective_unified < floor_uni:
                    msg = f"Below VRAM floor: vram={vram_val} GB, unified={effective_unified} GB (need ≥{floor_dis} GB discrete or ≥{floor_uni} GB unified)"
                    if behavior.get("below_vram_floor_action") == "hard_reject":
                        hard_reject_reason = msg
                        return {"hard_reject_reason": hard_reject_reason, "soft_penalty_notes": [], "exceptional_override": None, "shortlist_reason": "", "over_budget": False}
                    else:
                        soft_penalty_notes.append(msg)
        elif profile in ("Desktop",):
            floor_desk = config.get("desktop_minimum_vram_gb", 8.0)
            if vram_val is not None and vram_val < floor_desk:
                msg = f"Below VRAM floor: {vram_val} GB discrete (need ≥{floor_desk} GB)"
                if behavior.get("below_vram_floor_action") == "hard_reject":
                    hard_reject_reason = msg
                    return {"hard_reject_reason": hard_reject_reason, "soft_penalty_notes": [], "exceptional_override": None, "shortlist_reason": "", "over_budget": False}
                else:
                    soft_penalty_notes.append(msg)

    # Soft Penalties & Overrides
    if price_unknown:
        soft_penalty_notes.append("Price UNKNOWN — research required")

    if not price_unknown and price_val is not None and price_val > budget_cap:
        is_over_budget = True
        msg = f"Exceeds ${budget_cap:,.0f} AUD budget (price: ${price_val:,.2f})"
        
        # Check if exceptional override applies
        vram_check = vram_val if vram_val is not None else 0
        uni_check = unified_val if unified_val is not None else 0
        max_vram = max(vram_check, uni_check)
        
        if max_vram >= exc_vram and price_val <= exc_max_budget:
            exceptional_override = f"≥ {exc_vram}GB VRAM allows budget stretch to ${exc_max_budget}"
            soft_penalty_notes.append(f"{msg} [ALLOWED: {exceptional_override}]")
        elif "5090" in row["gpu_model"].upper() and price_val <= exc_max_budget:
            exceptional_override = f"RTX 5090 Tier allows budget stretch to ${exc_max_budget}"
            soft_penalty_notes.append(f"{msg} [ALLOWED: {exceptional_override}]")
        else:
            # Over budget and not exceptional
            if behavior.get("over_budget_action") == "hard_reject":
                hard_reject_reason = msg
                return {"hard_reject_reason": hard_reject_reason, "soft_penalty_notes": [], "exceptional_override": None, "shortlist_reason": "", "over_budget": True}
            else:
                soft_penalty_notes.append(msg)
                
    if row["verification_status"] in ("Unverified", "UNKNOWN"):
        soft_penalty_notes.append("Unverified — confirm specs before scoring")
        
    if row["au_stock"] in ("UNKNOWN", "No"):
        soft_penalty_notes.append(f"AU stock: {row['au_stock']}")

    return {
        "hard_reject_reason": hard_reject_reason,
        "soft_penalty_notes": soft_penalty_notes,
        "exceptional_override": exceptional_override,
        "shortlist_reason": "Passed gates" if not exceptional_override else "Passed via exceptional override",
        "over_budget": is_over_budget
    }


# ---------------------------------------------------------------------------
# Row builder
# ---------------------------------------------------------------------------

def build_row(fm: dict, intake_info: dict, source_path: Path) -> dict:
    """Build a fully annotated shortlist row from a card's frontmatter."""

    # Raw field extraction
    item_name        = fm.get("name", "")
    category         = fm.get("category", "UNKNOWN")
    gpu_model        = fm.get("gpu", "UNKNOWN")
    vram_raw         = fm.get("vram", "UNKNOWN").replace("GB", "").strip()
    unified_raw      = fm.get("unified_memory", "UNKNOWN").replace("GB", "").strip()
    price_raw        = fm.get("price_aud", "UNKNOWN").replace("$", "").replace("AUD", "").strip()
    condition        = fm.get("condition", "UNKNOWN")
    retailer         = fm.get("retailer", "UNKNOWN")
    vstatus          = fm.get("verification", "UNKNOWN")
    au_stock         = fm.get("au_stock", "UNKNOWN")
    status           = fm.get("status", "Active")
    track            = fm.get("track", "UNKNOWN")
    pathway          = fm.get("pathway", "UNKNOWN")

    # Derived
    profile        = classify_profile(category)
    price_float, price_unknown = parse_price(price_raw)
    vram_float     = parse_vram(vram_raw)
    unified_float  = parse_vram(unified_raw)
    cat_group      = classify_category_group(profile, gpu_model)

    # Intake ID from filename
    fname = source_path.name
    intake_id_match = re.match(r"(intake-\d+)", fname)
    intake_id = intake_id_match.group(1) if intake_id_match else fname.replace(".md", "")

    row = {
        # Identity
        "intake_id":            intake_id,
        "item_name":            item_name,
        "source_file":          str(source_path.relative_to(REPO_ROOT)),
        "batch":                intake_info.get("batch", "UNKNOWN"),
        # Classification
        "profile":              profile,
        "category":             category,
        "Category_Group":       cat_group,
        "track":                track,
        "pathway":              pathway,
        # Specs
        "gpu_model":            gpu_model,
        "vram_gb":              vram_float if vram_float is not None else "UNKNOWN",
        "unified_memory_gb":    unified_float if unified_float is not None else "UNKNOWN",
        "price_aud":            price_float if price_float is not None else "UNKNOWN",
        "Price_Unknown":        "Yes" if price_unknown else "",
        "condition":            condition,
        "retailer":             retailer,
        "verification_status":  vstatus,
        "au_stock":             au_stock,
        "status":               status,
        # Engine metadata
        "Machine":              intake_id,   # rubric_weighting_engine.py expects this
        "Type":                 "Candidate", # default; user can change to Preferred/NeverBuy
        # Score columns — all blank for manual completion
        **{col: "" for col in SCORE_COLUMNS},
        # Internal helpers (stripped before CSV output)
        "_price_float":         price_float,
        "_vram_float":          vram_float,
        "_unified_float":       unified_float,
    }
    return row


# ---------------------------------------------------------------------------
# Card scanner
# ---------------------------------------------------------------------------

def scan_intake_cards(batch_filter: str | None, profile_filter: str | None) -> list[dict]:
    """
    Walk all INTAKE_LANES and return a list of fully-built row dicts.
    """
    rows = []
    for lane in INTAKE_LANES:
        folder = WORKSPACE / lane
        if not folder.exists():
            continue
        for md_path in sorted(folder.glob("intake-*.md")):
            text = md_path.read_text(encoding="utf-8", errors="replace")
            fm          = parse_frontmatter(text)
            intake_info = parse_tags_comment(text)

            if not fm:
                continue  # skip unparseable cards

            row = build_row(fm, intake_info, md_path)

            # Batch filter
            if batch_filter and batch_filter not in row["batch"]:
                continue

            # Profile filter
            if profile_filter and row["profile"].lower() != profile_filter.lower():
                continue

            rows.append(row)

    return rows


# ---------------------------------------------------------------------------
# CSV writers
# ---------------------------------------------------------------------------

SHORTLIST_FIELDNAMES = [
    "intake_id", "item_name", "profile", "category", "Category_Group",
    "track", "pathway", "gpu_model", "vram_gb", "unified_memory_gb",
    "price_aud", "Over_Budget", "Price_Unknown",
    "condition", "retailer", "verification_status", "au_stock", "status",
    "batch", "source_file", "exceptional_override", "shortlist_reason", "soft_penalty_notes",
    # Engine columns
    "Machine", "Type",
    # Score columns
    *SCORE_COLUMNS,
]

REJECTED_FIELDNAMES = [col for col in SHORTLIST_FIELDNAMES if col not in ("Machine", "Type", *SCORE_COLUMNS)] + ["rejection_reason"]


def strip_internals(row: dict) -> dict:
    return {k: v for k, v in row.items() if not k.startswith("_")}


def write_csv(path: Path, fieldnames: list, rows: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows([strip_internals(r) for r in rows])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Phase 2 of the hardware procurement pipeline.\n\n"
            "Scans intake-*.md cards, applies policy from config/procurement_policy.json\n"
            "(handling hard rejects vs soft penalties), and emits a CSV ready for scoring."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/build_shortlist.py
  python scripts/build_shortlist.py --dry-run
  python scripts/build_shortlist.py --profile laptop

After generating the shortlist, run the pricing enrichment step:
  python scripts/enrich_shortlist_pricing.py
        """,
    )
    parser.add_argument(
        "--batch", default=None, metavar="STEM",
        help="Filter to a specific intake batch stem",
    )
    parser.add_argument(
        "--profile", default=None,
        choices=["laptop", "desktop", "mini pc", "component", "apple silicon", "all"],
        help="Filter by device profile (default: all profiles)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview shortlist without writing any files",
    )
    args = parser.parse_args()

    # Load machine-readable config
    config = load_config()

    profile_filter = None if (args.profile in (None, "all")) else args.profile

    print(f"\n🔍 Scanning intake cards in {WORKSPACE.relative_to(REPO_ROOT)} ...")
    all_rows = scan_intake_cards(args.batch, profile_filter)
    print(f"   Cards found: {len(all_rows)}")

    # Apply gates & policies
    shortlist = []
    rejected  = []

    for row in all_rows:
        eval_result = evaluate_policy(row, config)
        
        if eval_result["hard_reject_reason"]:
            row["rejection_reason"] = eval_result["hard_reject_reason"]
            rejected.append(row)
        else:
            row["Over_Budget"] = "Yes" if eval_result["over_budget"] else "No"
            row["exceptional_override"] = eval_result["exceptional_override"] or ""
            row["shortlist_reason"] = eval_result["shortlist_reason"]
            row["soft_penalty_notes"] = "; ".join(eval_result["soft_penalty_notes"])
            shortlist.append(row)

    # Sort: Complete_System first, then Standalone_GPU, then Workstation_GPU
    group_order = {"Complete_System": 0, "Standalone_GPU": 1, "Workstation_GPU": 2}
    shortlist.sort(key=lambda r: (
        group_order.get(r["Category_Group"], 9),
        r["profile"],
        str(r["vram_gb"]) if r["vram_gb"] != "UNKNOWN" else "0",
    ), reverse=False)

    # Print preview
    print(f"\n{'─'*70}")
    print(f"  SHORTLIST ({len(shortlist)} candidates):")
    print(f"{'─'*70}")
    for r in shortlist:
        flags = []
        if r["Price_Unknown"] == "Yes": flags.append("[PRICE UNKNOWN]")
        if r["Over_Budget"] == "Yes": flags.append("[OVER BUDGET]")
        if r["exceptional_override"]: flags.append("[EXCEPTIONAL]")
        flag_str = " ".join(flags)
        
        print(f"  {r['intake_id']:12s}  {r['profile']:12s}  {r['Category_Group']:18s}  "
              f"{str(r['vram_gb']):>6} GB  ${str(r['price_aud']):>8} {flag_str}  "
              f"{r['item_name'][:30]}")

    print(f"\n{'─'*70}")
    print(f"  REJECTED ({len(rejected)} candidates):")
    print(f"{'─'*70}")
    for r in rejected:
        print(f"  {r['intake_id']:12s}  {r['profile']:12s}  {r['item_name'][:40]:40s}  "
              f"→ {r.get('rejection_reason', '?')}")

    if args.dry_run:
        print(f"\n  [DRY RUN] — no files written.\n")
        return

    # Write outputs
    today     = date.today().isoformat()
    out_dir   = WORKSPACE / "intake" / "shortlist"
    sl_path   = out_dir / f"{today}_shortlist.csv"
    rej_path  = out_dir / f"{today}_shortlist_rejected.csv"

    write_csv(sl_path, SHORTLIST_FIELDNAMES, shortlist)
    write_csv(rej_path, REJECTED_FIELDNAMES, rejected)

    print(f"\n✅ Shortlist complete.")
    print(f"   Shortlisted : {len(shortlist)} → {sl_path.relative_to(REPO_ROOT)}")
    print(f"   Rejected    : {len(rejected)} → {rej_path.relative_to(REPO_ROOT)}")
    print(f"\n   Next: Run the live pricing enrichment step:")
    print(f"   python scripts/enrich_shortlist_pricing.py {sl_path.relative_to(REPO_ROOT)}\n")


if __name__ == "__main__":
    main()
````

## File: scripts/enrich_shortlist_pricing.py
````python
#!/usr/bin/env python3
"""
enrich_shortlist_pricing.py — Phase 2b of the hardware procurement pipeline.

Takes a shortlist CSV generated by build_shortlist.py and outputs an enriched
version with empty columns for live pricing intelligence (cashback, student discounts,
stackable coupons, etc.).

Usage:
    python scripts/enrich_shortlist_pricing.py NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist.csv
"""

import argparse
import csv
import sys
from pathlib import Path

PRICING_COLUMNS = [
    "current_best_price_aud",
    "current_best_retailer",
    "current_best_url",
    "in_stock_now",
    "student_discount_possible",
    "cashback_possible",
    "cashback_source",
    "stackable_coupons_confirmed",
    "price_match_possible",
    "price_beat_possible",
    "effective_best_price_aud",
    "promo_notes",
    "pricing_checked_at"
]

def main():
    parser = argparse.ArgumentParser(description="Add pricing enrichment columns to a shortlist CSV.")
    parser.add_argument("csv_path", type=str, help="Path to the input shortlist CSV")
    args = parser.parse_args()

    input_path = Path(args.csv_path)
    if not input_path.exists():
        sys.exit(f"Error: Input file {input_path} does not exist.")

    output_path = input_path.parent / f"{input_path.stem}_pricing_enriched.csv"

    with open(input_path, "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)
        fieldnames = reader.fieldnames
        if not fieldnames:
            sys.exit("Error: Input CSV has no headers.")
            
        # Avoid duplicating columns if ran twice
        new_fieldnames = list(fieldnames)
        for col in PRICING_COLUMNS:
            if col not in new_fieldnames:
                new_fieldnames.append(col)

        rows = list(reader)

    # Initialize new columns to blank
    for row in rows:
        for col in PRICING_COLUMNS:
            if col not in row:
                row[col] = ""

    with open(output_path, "w", newline="", encoding="utf-8") as fout:
        writer = csv.DictWriter(fout, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n✅ Pricing enrichment scaffold created successfully!")
    print(f"   Output: {output_path}")
    print(f"\n   Next Steps:")
    print(f"   1. Use the prompt template in `scripts/prompt_templates/browser_pricing_lookup.md`")
    print(f"      to instruct your Vercel Browser Agent to look up live prices.")
    print(f"   2. Fill in the new pricing columns in the enriched CSV.")
    print(f"   3. Score the candidates and run `rubric_weighting_engine.py --profile merged`")

if __name__ == "__main__":
    main()
````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-009_lenovo-legion-pro-7i.md
````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: lenovo-legion-pro-7i
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Lenovo Legion Pro 7i
gpu: RTX 4090 Mobile
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $4575 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Lenovo Legion Pro 7i

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $4575 AUD
- **Retailer:** Mike PC / Lenovo
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4090 Mobile
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** i9-14900HX
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
The best emotional-but-defensible one-machine route

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-010_msi-raider-18-hx-ai-a2xwjg.md
````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-24GB #New #TrackUnknown #Verified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: msi-raider-18-hx-ai-a2xwjg
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: MSI Raider 18 HX AI A2XWJG
gpu: RTX 5090 Mobile
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $8488 AUD
condition: New
au_stock: UNKNOWN
verification: Verified
status: Active
score: UNKNOWN — pending manual review
---

# MSI Raider 18 HX AI A2XWJG

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $8488 AUD
- **Retailer:** Scorptec / JW Computers
- **URL:** [https://www.scorptec.com.au/product/ready-to-run-pcs/gaming-pc/124318-r2r10638](https://www.scorptec.com.au/product/ready-to-run-pcs/gaming-pc/124318-r2r10638)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090 Mobile
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 285HX
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Massive desktop replacement that overcomes traditional laptop VRAM limits

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-011_dell-alienware-m18-r2-area-51.md
````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: dell-alienware-m18-r2-area-51
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Dell Alienware m18 R2 / Area-51
gpu: RTX 5090 Mobile
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $4499 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Dell Alienware m18 R2 / Area-51

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $4499 AUD
- **Retailer:** Dell Outlet / Best Buy
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090 Mobile
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 275HX
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
18-inch desktop replacement offering 24GB of mobile VRAM

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-052_acer-predator-helios-neo-16s-ai-rtx-5060.md
````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-8GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: acer-predator-helios-neo-16s-ai-rtx-5060
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Acer Predator Helios Neo 16S AI RTX 5060
gpu: RTX 5060
vram: 8 GB
unified_memory: UNKNOWN
price_aud: $2399 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Acer Predator Helios Neo 16S AI RTX 5060

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2399 AUD
- **Retailer:** Acer AU Clearance
- **URL:** [https://store.acer.com/en-au/](https://store.acer.com/en-au/)
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5060
- **VRAM:** 8 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 275HX
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Refurbished entry level laptop

## AI Capability Summary
Baseline — 8 GB VRAM sufficient for 7B Q4; larger models require significant offload.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
````

## File: scripts/intake_to_cards.py
````python
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
````

## File: scripts/normalize_intake.py
````python
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
    "pre-owned": "Refurbished",
    "ex-demo": "Open Box",
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
````

## File: AGENTS.md
````markdown
# AGENTS.md — Two-Track Hardware Decision System

**Role:** Hardware-research and organisation helper inside the Antigravity IDE.
Keep decisions simple. Do NOT design the perfect system.
Browser access and web searches are permitted for verification and data gathering.

---

## TERMINOLOGY

### Tracks and Paths / Pathways
- `track` (CSV) is the high-level decision rail, usually a small integer (e.g. 1, 2).  
- `pathway` (CSV) is the specific branch within a track (e.g. "1A", "1B", "2A").  
- In prose we refer to these as “Path 1A”, “Path 1B”, etc.  
- When you see or say “Track 1A” or “Track 2B”, interpret that as:  
  - `track = 1` and `pathway = "1A"`, or  
  - `track = 2` and `pathway = "2B"`, respectively.  
- The **Track** concept is always the broader category; **Path / Pathway** is the specific branch within that Track.

### Machine vs item_name
- `item_name` is the canonical identifier in the intake and shortlist CSVs.  
- Some processing steps and reports also use a derived `Machine` label; this should always be consistent with `item_name` (optionally plus extra context, such as retailer or config suffix).  
- When referring to a “machine” in prompts or conversations, assume it refers to the underlying `item_name`, and treat `Machine` as a reporting/alias field tied back to that `item_name`.

---

## SCOPE

- **Track 1:** Active laptop purchase. One decision. GOOD ENOUGH → buy.
- **Track 2:** Active workstation/desktop research. Three pathways. Likely medium-term outcome — runs in parallel with Track 1. Do not delay Track 1 for Track 2 unless a unicorn deal is immediately available.

---

## GLOBAL CONSTRAINTS

- **Browser access permitted.** Use the **Vercel Agent Browser (`agent-browser`)** CLI as the default for web research to ensure token utilization efficiency (via compact DOM snapshots). Use headless browser instances for all scraping and verification tasks to minimize overhead.
- **Work with:** existing markdown product cards, CSVs, policy/spec docs, scripts, templates in this repo, and external web sources.
- **Unknown values:** Use `agent-browser` to search for real-world specs or prices when they are unknown. Update fields dynamically.
- **Responsibilities:**
  - Audit and sync product cards vs CSVs.
  - Create and normalise product card shells.
  - Generate and refine prompt files.
  - Rebuild the mega-bundle.
  - Apply documented patches to spec/policy docs.
  - Draft decision logs and checklists.
  - Fetch new data from the internet to complete missing details.

---

## PIPELINE AND POLICY (5-PHASE WORKFLOW)

This repository enforces a strict 5-phase execution path to go from raw web data to a mathematical purchase decision. 

**Policy Source of Truth:**
All scripts read hardware constraints (budgets, VRAM floors, soft penalty behaviors) from the machine-readable config: `config/procurement_policy.json`. Do not hard-code these limits in scripts.

1. **Phase 1: Intake & Verification** (`normalize_intake.py` + `intake_to_cards.py`)
   - Clean raw AI exports and generate markdown product cards.
2. **Phase 2: Shortlist** (`build_shortlist.py`)
   - Filter out junk (out of stock, under VRAM floor). Applies soft-penalties to over-budget items unless they qualify for an `exceptional_override`.
3. **Phase 3: Live Pricing Enrichment** (`enrich_shortlist_pricing.py`)
   - Scaffold the CSV for live pricing checks. 
   - *Agent action:* Use `scripts/prompt_templates/browser_pricing_lookup.md` in the Vercel Browser Agent to hunt down stackable coupons, student discounts, and cashback.
4. **Phase 4: Manual Scoring**
   - *Agent action:* Fill in the 0–10 score columns in the enriched CSV based on the newly discovered `effective_best_price_aud`.
5. **Phase 5: Score & Rank** (`rubric_weighting_engine.py`)
   - Run the engine with `--profile merged`. Buy the candidate that ranks #1 and hits `[GOOD ENOUGH]`.

---

## TRACK 1 — CHASSIS SCOPE AND BUDGET

Track 1 has **two hardware paths**: NVIDIA discrete GPU laptops and AMD unified-memory laptops.
Both paths are active simultaneously.

> **Principle:** The smaller the screen size, the more critical a Track 2 solution becomes.
> A 13" device at a strong price is a valid Track 1 candidate, but it explicitly increases
> urgency to resolve Track 2.

---

### Path 1A — NVIDIA Discrete GPU Laptops

#### Screen Size
- **Floor:** 13" minimum.
- **Primary target:** 17–18" (scoring bonus applies — see Scoring section).
- **Intermediate sizes (14–16"):** In scope; evaluated on VRAM, build quality, and resale value.

#### VRAM
- **Minimum:** 8 GB VRAM.
- **Preferred:** 12 GB or higher (16 GB - 24 GB optimal for larger LLMs).
- A 12 GB+ card at 17–18" = standard eligible candidate.
- An 8 GB card = requires significant offsetting strengths (build quality, price, resale) to remain competitive for LLM workloads.

#### Brands and Families in Scope

**LENOVO**
- Legion 9i
- Legion Pro 9i
- Legion Pro 7i (current high-end variants meeting VRAM and budget rules)

**ASUS**
- ROG Strix Scar 17
- ROG Strix Scar 18
- Any ROG model at 13"+ meeting the 8 GB VRAM floor

**MSI**
Any current 13"+ high-end RTX gaming/workstation model meeting VRAM and price constraints, including:
- MSI Raider 17/18
- MSI Titan 17/18
- MSI Stealth 16/17/18
- MSI Vector 16/17/18
- Other MSI 13"+ models with ≥ 8 GB VRAM


#### AMD Discrete GPU Laptops
AMD discrete GPU laptops evaluate under same rules as NVIDIA:
- HP OMEN Max (Ryzen AI 9 HX 375 + RTX 5070/5090)
- Tag as: architecture:discrete_gpu_amd, track_eligibility:track_1_nvidia_path
- Move cards from Strix_Halo_AMD/ to Gaming_Laptops_AMD_Discrete/
- Apply ≥8 GB VRAM floor, 16"+ screen size

#### Exclusions (Path 1A)
- Any laptop with less than 13" screen size.
- Any laptop with less than 8 GB discrete VRAM.
- Any brand/model family outside the three listed above, unless explicitly expanded.

#### Lenovo Legion Pro 7i vs 9i / Pro 9i Value Rule
- At the same price or within < 300 AUD difference: **prefer Legion 9i / Pro 9i over Pro 7i.**
- **Prefer Pro 7i** if it is ≥ 300–500 AUD cheaper than a comparable 9i/Pro 9i, while still meeting
  VRAM requirements, decent thermals, and upgradeability targets (32–64 GB RAM, ≥ 2 TB SSD).
- Pro 7i = "discount premium" tier, not equal to 9i/Pro 9i at the same price.

---

### Path 1B — AMD Strix Halo Unified Memory Laptops

#### Screen Size
- **No minimum screen size.** 13-14" devices are valid Track 1 candidates BUT trigger immediate Track 2 urgency (portable device requires desktop companion for extended work).
- 17–18" scoring bonus applies equally to this path.

#### Unified Memory
- **Minimum:** 16 GB (≈ equivalent to 8 GB discrete VRAM in GPU-accessible terms, given ~60–75%
  allocation to GPU workloads).
- **Preferred:** 64 GB.
- **Optimal:** 96–128 GB.

#### SoC Requirement
- Must use AMD Strix Halo (Ryzen AI Max / Ryzen AI Max+) or architecturally equivalent
  unified-memory SoC.
- Standard Ryzen with discrete dGPU does NOT qualify for this path.

#### Brands and Families in Scope
AMD Strix Halo laptops (any brand):
- ASUS TUF Gaming A14 (2026) FA401EA — 32 GB unified, 14"
- ASUS ProArt PX13 (Strix Halo variant) — 128 GB unified, 13.3"
- ASUS ROG Flow Z13 GZ302EA — check unified memory config, 13.4"
- Lenovo Legion 7a Gen 11 — if AU stock confirmed (not yet available)

> **ProArt PX13 Note:** ProArt PX13 retail (~$6,000 AUD) exceeds budget. ONLY pursue if refurbished/open-box/sale pricing ≤$4,500 AUD. Check: Officeworks, Harvey Norman, JB Hi-Fi, ASUS AU Outlet.

#### Exclusions (Path 1B)
- ASUS TUF A16: NO Strix Halo variant exists (discrete GPU only)
- ASUS ROG Zephyrus G16: NO Strix Halo variant exists (discrete GPU only)
- HP OMEN Max: Uses Strix Point (discrete GPU), NOT Strix Halo
- Any AMD device with < 16 GB unified memory.
- Any AMD device using a non-unified architecture (discrete dGPU with standard Ryzen iGPU).
- Apple Silicon (separate category, currently deferred).

---

### Track 1 — Price Band

- **Total budget range (AUD):** 0–4,500
- **Preferred sweet spot (AUD):** 2,500–4,000
- Only consider 4,000–4,500 AUD if: GPU/unified memory is top-tier, build quality and thermals are
  clearly superior, and there is a strong resale story.

### Track 1 — Scoring Bonuses and Flags

- **+Bonus:** Screen size 17–18" (applies to both Path 1A and 1B).
- **+Bonus:** Top-tier memory for path — 24 GB discrete (1A) or 96–128 GB unified (1B).
- **−Competitive penalty:** Screen size < 15" with no offsetting Track 2 plan resolved.
- **⚠ Flag:** Thermal concerns (sustained throttling under sustained GPU load).
- **⚠ Flag (Path 1B only):** Known ROCm software compatibility gaps for target workloads.

---

## TRACK 1 — AGENT RESPONSIBILITIES (REPO-ONLY)

- Audit `laptop_candidates.csv` against `04_Laptops_Mainline/*.md`:
  - Map every CSV row to a card file (or flag "NO CARD EXISTS").
  - Map every card file to a CSV row (or flag "NOT IN CSV").
  - Flag UNKNOWN / placeholder fields.
- For missing candidates within allowed scope: create BLANK product card shells using
  `template_product_card_output.md` with all spec fields set to UNKNOWN.
- Produce a "data-ready checklist" — a markdown table of all fields requiring web lookup, and use the browser agent to fill them.
- Actively attempt to fill UNKNOWN fields using the internet.

---

## GOOD ENOUGH STOP CONDITION (Track 1)

Mark a candidate as **"GOOD ENOUGH — STOP SEARCHING"** when ALL of the following are confirmed:

**Path 1A (NVIDIA):**
- In stock in AU from a credible retailer.
- ≥ 8 GB VRAM (12 GB+ preferred; RTX 4080/4090/5080/5090 optimal).
- Supports at least 32–64 GB RAM (installed or clearly upgradable).
- At least 2 TB SSD (installed or clearly upgradable).
- Price within the 0–4,000 AUD budget.
- No disqualifying thermal flag.

**Path 1B (AMD Strix Halo):**
- In stock in AU from a credible retailer.
- Confirmed Strix Halo SoC.
- ≥ 16 GB unified memory (32 GB+ preferred).
- Price within the 0–4,000 AUD budget.
- No disqualifying thermal flag.
- No disqualifying ROCm software compatibility gap for target workloads.

Do NOT expand scope beyond the listed families/SoC requirements unless explicitly instructed.

---

---

## TRACK 1.5 — REFURBISHED GAMING DESKTOP (SINGLE GPU)

**Definition:** Refurbished or open-box gaming desktops (OEM chassis) with single high-VRAM GPU. Evaluated as laptop alternatives when price/performance ratio is compelling.

**Scope:** Pre-built gaming towers from major OEMs. NOT custom builds (see Track 2 Pathway A).

**Brands in scope:**
- Alienware Aurora (R11, R12, R13, R14, R15, R16 series)
- Acer Predator Orion
- HP OMEN 45L/40L/30L
- ASUS ROG Strix GA15/GA35
- Lenovo Legion Tower (5i/7i series)

**GPU Requirements:**
- Minimum 8 GB VRAM (same as Track 1 NVIDIA path)
- Target: RTX 3090 (24 GB), RTX 4080/4090, or equivalent

**Age Limit:** Maximum 6 years old (≥ 2020 manufacture date)

**Price Threshold (CRITICAL):**
Must beat equivalent Track 1 laptop on price/performance:
- [ ] Desktop ≤ 85% cost of comparable laptop (accounting for loss of portability)
- [ ] OR desktop offers ≥ 50% more VRAM at same price point

Example: Alienware R12 with RTX 3090 (24 GB) @ $2,500 AUD beats TUF A14 (32 GB unified ≈ 16 GB GPU-available) @ $3,499 AUD.

**Go/No-Go Gates:**
- [ ] Chassis ≥ 2020 (confirm manufacture date or CPU generation)
- [ ] GPU confirmed ≥ 8 GB VRAM
- [ ] PSU wattage confirmed sufficient for installed GPU (or upgradable)
- [ ] Price threshold test passed (see above)
- [ ] AU stock/listing confirmed at credible seller
- [ ] Warranty ≥ 3 months (refurb) or ACL coverage (retailer sold)
- [ ] No disqualifying proprietary parts flag (Dell/Alienware: check PSU/mobo upgradeability)

**Candidate Prioritization:**
1. RTX 3090 chassis (best VRAM/$)
2. RTX 4090 chassis (if steep discount)
3. Multi-GPU capable (even if sold with single GPU — future Track 2 Pathway B conversion)

**Agent Responsibilities:**
- Maintain cards in `Desktop_Gaming_Refurbished/` folder
- For each card: confirm age, GPU VRAM, PSU spec, price/performance vs Track 1
- Use web searches to resolve UNKNOWN fields for: exact manufacture date, PSU wattage, warranty terms
- You may add new cards from web searches if they meet the criteria

**Exclusions:**
- Custom/SI builds (those go to Track 2 Pathway A)
- Desktops with <8 GB VRAM
- Pre-2020 platforms (thermal/efficiency penalty too high)

## TRACK 2 — WORKSTATION (ACTIVE — THREE PATHWAYS)

Track 2 is **active now** and runs in parallel with Track 1.
It is likely a **medium-term** outcome.

> **Do not delay Track 1 for Track 2.** Unless a Pathway A, B, or C candidate with immediate
> AU availability and strong pricing is identified, Track 1 remains the priority purchase.
> Track 2 resolves on its own timeline.

---

### Pathway A — AU System Integrator Custom/Configurable Build

**Definition:** A system ordered from an AU-based system integrator in a custom or
"ready-to-run" configuration. Examples: Scorptec, Mwave, Centre.com. This is NOT a
DIY self-sourced parts build.

**Go/No-Go Gates (ALL must pass before any action is taken):**
- [ ] Confirmed build spec exists in repo at `01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md`
      (CPU, motherboard, RAM, PSU, GPU, case — all named, no UNKNOWN fields).
- [ ] Target GPU(s) availability in AU market confirmed (flag UNKNOWN until manually verified).
- [ ] Build spec confirmed to support target GPU(s): PCIe slots, lane allocation, PSU wattage,
      physical clearance.
- [ ] Total cost (build + GPUs) within AUD budget.

**CPU Platform (LOCKED):**
AMD Threadripper PRO 5000WX (WRX80 chipset)
- 128 PCIe Gen 4 lanes (supports RTX 3090 × 2 + NVMe without bottleneck)
- Better AU availability than Intel Xeon W-3400
- Compatible motherboards: ASUS Pro WS WRX80E-SAGE, ASRock WRX80 Creator

**GPU Target:**
RTX 3090 × 2 (24 GB VRAM each = 48 GB total)
- AU used market estimate: $1,500-1,800 AUD per card (Gumtree, eBay AU)
- Flag as UNKNOWN until manual verification at time of build decision

**Next Steps:**
Create `track2_pathway_a_build_spec.md` with confirmed components:
- CPU: Threadripper PRO 5955WX or 5975WX
- Motherboard: (specific model TBD)
- RAM: 128 GB DDR4 ECC (minimum)
- PSU: 1600W+ 80+ Platinum (dual GPU headroom)
- Case: (TBD — must fit dual 3-slot GPUs)

**Agent Responsibilities:**
- Maintain confirmed build spec at `01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md`.
- Use the browser agent to look up UNKNOWN fields (prices, stock) from integrator websites.
- You may browse integrator websites to confirm specs and prices.

---

### Pathway B — Refurbished Enterprise Workstation

**Definition:** A pre-owned enterprise-class tower or rack workstation (e.g., Dell Precision,
HP Z-series, Lenovo ThinkStation) that arrives with 1× or 2× compatible GPU already installed,
or has confirmed empty PCIe slot(s) and PSU headroom to accept target GPU(s).

**Age Limit:** Maximum 8 years old (manufactured ≥ 2018).

**Go/No-Go Gates (ALL must pass before any action is taken):**
- [ ] Chassis manufacture date confirmed ≥ 2018 (flag UNKNOWN if not stated on card).
- [ ] PCIe slot count and lane allocation confirmed for target GPU configuration.
- [ ] PSU wattage confirmed sufficient for GPU(s), or PSU upgrade confirmed possible and costed.
- [ ] GPU(s) confirmed ≥ 8 GB VRAM per card — either pre-installed or separately available in
      AU used/refurbished market.
- [ ] Total cost (unit + any GPU additions) within AUD budget.
- [ ] No disqualifying thermal flag (inadequate airflow for dual-GPU sustained load).
- [ ] No ECC-only memory constraint that would prevent standard GPU driver operation.

**GPU Rules:** Same as Pathway A — 8 GB VRAM minimum per GPU, any make/model.

**Agent Responsibilities:**
- Existing cards in `02_Refurbished_Desktop_Towers/` are the primary candidates.
- For each card: verify age, PCIe slot spec, PSU spec, GPU compatibility. Flag UNKNOWN for any
  missing field.
- Flag for review: Dell Precision 5820 bundle ($3,558 includes ThinkPad T14s) — find unbundled tower-only price or mark "bundle only".
- You may add new candidates from the internet.

---

### Pathway C — Unified Memory Mini PC

**Definition:** A compact/mini PC using AMD Strix Halo (Ryzen AI Max / Ryzen AI Max+) or
architecturally equivalent high-bandwidth unified-memory SoC, where system RAM is simultaneously
GPU VRAM.

**Unified Memory Floor:** 32 GB minimum. 64–128 GB preferred.

**Go/No-Go Gates (ALL must pass before any action is taken):**
- [ ] Device confirmed to use a unified-memory SoC (Strix Halo or equivalent — not a standard
      iGPU + discrete GPU combo).
- [ ] Unified memory ≥ 32 GB confirmed from spec sheet (not estimated).
- [ ] AU stock confirmed at credible retailer.
- [ ] Price within AUD budget.
- [ ] No disqualifying thermal flag (passive-only or inadequate cooling for sustained inference
      workloads is a flag).
- [ ] No disqualifying ROCm software compatibility gap for target workloads.
- [ ] If refurbished/open-box: Minimum 3-month seller warranty or ACL coverage confirmed
- [ ] If refurbished/open-box: Condition grade disclosed (Grade A/B acceptable; C/D flagged for manual review)

**Confirmed AU Stock Candidates:**
- Minisforum AI X1 Pro (Ryzen AI Max+ 370/470, up to 128 GB unified)
  - AU retailers: au.minisforum.com, MegaTechStore AU
  - Pricing: Quote required
  - Status: ✅ Confirmed in stock

**Priority Research Targets (UNKNOWN — manual verification required):**
- HP Z2 Mini G1a (Strix Halo variant, if exists)
- HP Elite Mini 800 G11 AI (Strix Halo variant, if exists)
- Any HP workstation mini PC with Ryzen AI Max/Max+
- Prioritize refurbished/open-box from: HP AU Refurbished Store, Scorptec, Mwave, eBay AU enterprise sellers

**Excluded:**
- ASUS NUC 14 Pro AI (Intel Core Ultra, NOT Strix Halo)

**Agent Responsibilities:**
- Maintain candidate cards in `06_Mini_PCs_and_eGPU/` (existing lane).
- For each candidate: confirm SoC model, unified memory config, AU availability. Use the internet to resolve UNKNOWN fields.
- You may add new candidates from the internet.

---

## TRACK 2 — AGENT RESPONSIBILITIES (REPO-ONLY)

- **Pathway A:** Maintain and update `01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md`.
- **Pathway B:** Audit `02_Refurbished_Desktop_Towers/*.md` cards against all gate conditions.
- **Pathway C:** Audit and/or create candidate shells in `06_Mini_PCs_and_eGPU/`.
- Produce a unified Track 2 data-ready checklist: a markdown table of all UNKNOWN fields across
  all three pathways requiring verification, and use the browser to fill them before gates can be cleared.
- Actively use the internet to resolve and fill UNKNOWN fields.

---

## SCORING RUBRIC CHEATSHEET (VRAM, PRICE/PERF, ETC.)

**VRAM_Adequacy (0–10)**  
- 0 = Below hard minimum VRAM for the target workload in this Track/Path.  
- 5 = Meets the minimum VRAM requirement, but with little headroom.  
- 10 = Meets or exceeds the “ideal” VRAM tier defined for this Track/Path (comfortable headroom).  
- Example:  
  - For a Track 1A GPU workload where the minimum is 16 GB and the ideal is 24 GB:  
    - 8 GB → 0  
    - 16 GB → ~5  
    - 24 GB or more → 9–10

**Price_to_Perf (0–10)**  
- 0 = Clearly poor value for money vs alternatives in the same Track/Path.  
- 5 = Acceptable value (roughly average) for this segment.  
- 10 = Excellent value (significantly better price/performance than typical options for this Track/Path).  
- Use the same formula or comparison logic implemented in `rubric_weighting_engine.py`, but this section documents the intent in plain language.

**Value_Score (0–10)**  
- Aggregated view of cost vs capability for the intended workload.  
- 0 = Fails either capability or cost constraints badly.  
- 5 = Meets both capability and cost constraints at baseline.  
- 10 = Strongly meets or exceeds capability while staying comfortably within budget.

**Condition_Risk (0–10)**  
- 0 = Extremely high risk (e.g. unknown vendor, no warranty, poor condition).  
- 5 = Acceptable risk (standard refurb or used, clear but limited warranty).  
- 10 = Minimal risk (new or near-new from trusted vendor, strong warranty).

**Verification_Confidence (0–10)**  
- 0 = Almost nothing verified; key specs uncertain.  
- 5 = Most important specs have at least one independent verification.  
- 10 = All critical specs and price are cross-verified and documented.

**Sustained_TGP_Rating (0–10)**  
- 0 = Clear thermal/Power-limit issues vs workload expectations.  
- 5 = Meets baseline TGP and thermal headroom for the expected workloads.  
- 10 = Excellent sustained TGP/thermals for long-running workloads in this Track/Path.

**Portability_Score (0–10)**  
- 0 = Not reasonably portable for the intended use (very heavy, bulky, low battery if relevant).  
- 5 = Acceptably portable (within stated thresholds for weight, size, battery).  
- 10 = Very portable while still meeting capability requirements.

These are **interpretive guardrails** for humans and LLMs. The exact formulas and thresholds live in `rubric_weighting_engine.py`, but this section documents the intent, so scorers apply the rubric consistently.
````
