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
    "intake_id", "item_name", "status", "profile", "category", "Category_Group",
    "track", "pathway", "gpu_model", "vram_gb", "unified_memory_gb",
    "price_aud", "Over_Budget", "Price_Unknown",
    "condition", "retailer", "verification_status", "au_stock", 
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

    # Add 'status' column defaulting to ACTIVE if not set or if it's 'Active'
    for row in shortlist:
        if "status" not in row or not row["status"] or row["status"].upper() == "ACTIVE":
            row["status"] = "ACTIVE"

    write_csv(sl_path, SHORTLIST_FIELDNAMES, shortlist)
    write_csv(rej_path, REJECTED_FIELDNAMES, rejected)

    print(f"\n✅ Shortlist complete.")
    print(f"   Shortlisted : {len(shortlist)} → {sl_path.relative_to(REPO_ROOT)}")
    print(f"   Rejected    : {len(rejected)} → {rej_path.relative_to(REPO_ROOT)}")
    print(f"\n   Next: Run the live pricing enrichment step:")
    print(f"   python scripts/enrich_shortlist_pricing.py {sl_path.relative_to(REPO_ROOT)}\n")


if __name__ == "__main__":
    main()
