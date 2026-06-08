#!/usr/bin/env python3
"""
build_shortlist.py — Phase 2 of the hardware procurement pipeline.

Scans all intake-*.md product cards, applies AGENTS.md hard-gate filters,
and emits two CSVs:

  shortlist.csv  — candidates that passed all gates, with blank MCDA columns
                   ready to be manually filled and fed into rubric_weighting_engine.py
  rejected.csv   — filtered-out rows with the reason for rejection

Usage:
    python scripts/build_shortlist.py
    python scripts/build_shortlist.py --dry-run
    python scripts/build_shortlist.py --batch 2026-05-05_notebooklm_batch1
    python scripts/build_shortlist.py --profile laptop
    python scripts/build_shortlist.py --track 1 --pathway 1A
    python scripts/build_shortlist.py --include-unknowns

Output folder: NotebookLM_Workspaces/intake/shortlist/

After filling in the MCDA columns (0-10), run:
    python NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/rubric_weighting_engine.py \\
        --csv NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist.csv
"""

import argparse
import csv
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Optional


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


def load_archetype(name: str) -> dict:
    """
    Load a named archetype from config/search_archetypes.json.

    Returns the archetype dict or exits with a helpful error listing valid names.
    Usage: loaded via --archetype <label> in main().
    """
    archetypes_path = REPO_ROOT / "config" / "search_archetypes.json"
    if not archetypes_path.exists():
        sys.exit(
            f"Error: search_archetypes.json not found at {archetypes_path}. "
            "Run Step 1 of the agent.md incremental plan to create it."
        )
    with open(archetypes_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    archetypes = {a["label"]: a for a in data.get("archetypes", [])}
    if name not in archetypes:
        valid = ", ".join(sorted(archetypes.keys()))
        sys.exit(
            f"Error: Unknown archetype '{name}'.\n"
            f"Valid archetype labels: {valid}"
        )
    return archetypes[name]

# Top-level card roots (scanner recurses into category subfolders).
INTAKE_LANES = [
    "cards",
]

# GPU model substrings that indicate professional/workstation-class cards
WORKSTATION_GPU_KEYWORDS = [
    "RTX PRO", "RTX 6000", "RTX 5000 ADA", "RTX 4000 ADA", "RTX 3000 ADA",
    "RTX 2000 ADA", "A6000", "A5000", "A4500", "A4000", "A2000",
    "QUADRO", "RADEON PRO W", "ARC PRO",
]

# MCDA score columns — filled manually after live pricing verification.
SCORE_COLUMNS = [
    "Performance_Headroom",  # 25%: local AI capacity/headroom for MVP + Q4
    "Price_Value",           # 20%: value against budget and alternatives
    "Future_Proof",          # 20%: Q4 runway and resale/useful life
    "Portability",           # 20%: laptop/field practicality; desktops score low unless Track 2 trigger applies
    "Track2_Avoidance",      # 15%: likelihood this purchase avoids/defer Track 2
    "MCDA_Total",            # computed by rubric_weighting_engine.py
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


def parse_screen_size(md_text: str, item_name: str) -> float | None:
    """Extract a likely laptop screen size in inches from card text."""
    patterns = [
        r"\*\*Display:\*\*[^\n]*?(\d{2}(?:\.\d)?)\s*(?:-|–)?\s*(?:inch|in\b|\")",
        r"\*\*Screen(?: Size)?:\*\*[^\n]*?(\d{2}(?:\.\d)?)\s*(?:-|–)?\s*(?:inch|in\b|\")",
        r"\b(\d{2}(?:\.\d)?)\s*(?:-|–)?\s*inch\b",
    ]
    haystack = f"{item_name}\n{md_text}"
    for pattern in patterns:
        match = re.search(pattern, haystack, re.IGNORECASE)
        if not match:
            continue
        value = float(match.group(1))
        if 10 <= value <= 20:
            return value
    return None


def parse_thermal_flag(md_text: str) -> str:
    """Return Disqualifying, Flagged, Clear, or UNKNOWN from card evidence."""
    text = md_text.lower()
    if "no disqualifying thermal" in text or "thermals clear" in text:
        return "Clear"
    if "disqualifying thermal" in text or "thermal flag: disqualifying" in text:
        return "Disqualifying"
    if "thermal concern" in text or "thermal flag" in text or "throttl" in text:
        return "Flagged"
    return "UNKNOWN"


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
    budget_cap        = config.get("budget_cap_aud", 5000.0)
    behavior          = config.get("shortlist_behavior", {})
    exc_vram          = config.get("exceptional_overrides", {}).get("vram_threshold_gb", 24.0)
    exc_max_budget    = config.get("exceptional_overrides", {}).get("max_override_budget_aud", 6000.0)
    bargain           = config.get("track1_bargain_exception", {})
    bargain_vram      = float(bargain.get("minimum_vram_gb", 12.0))
    bargain_price_cap = float(bargain.get("max_effective_price_aud", 3500.0))

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
            floor_dis = config.get("laptop_discrete_minimum_vram_gb", 16.0)
            floor_uni = config.get("laptop_unified_minimum_vram_gb", 16.0)
            effective_vram = vram_val or 0
            effective_unified = unified_val or 0
            
            # If both are known or partially known and fail:
            if vram_val is not None or unified_val is not None:
                if effective_vram < floor_dis and effective_unified < floor_uni:
                    if profile == "Laptop" and vram_val is not None and bargain_vram <= vram_val < floor_dis:
                        if price_val is None or price_val <= bargain_price_cap:
                            soft_penalty_notes.append(
                                f"Track 1A bargain exception candidate: {vram_val} GB VRAM below standard {floor_dis} GB floor; "
                                f"requires effective price ≤${bargain_price_cap:,.0f} AUD and Price_Value ≥8"
                            )
                            # Keep candidate visible for live pricing and MCDA.
                            pass
                        else:
                            msg = (
                                f"Below standard VRAM floor and not a bargain: {vram_val} GB discrete "
                                f"(need ≥{floor_dis} GB, or ≥{bargain_vram} GB at ≤${bargain_price_cap:,.0f} AUD)"
                            )
                            if behavior.get("below_vram_floor_action") == "hard_reject":
                                hard_reject_reason = msg
                                return {"hard_reject_reason": hard_reject_reason, "soft_penalty_notes": [], "exceptional_override": None, "shortlist_reason": "", "over_budget": False}
                            soft_penalty_notes.append(msg)
                        # Do not also apply the normal below-floor message.
                        continue_below_floor = False
                    else:
                        continue_below_floor = True
                    if not continue_below_floor:
                        pass
                    else:
                        msg = f"Below VRAM floor: vram={vram_val} GB, unified={effective_unified} GB (need ≥{floor_dis} GB discrete or ≥{floor_uni} GB unified)"
                        if behavior.get("below_vram_floor_action") == "hard_reject":
                            hard_reject_reason = msg
                            return {"hard_reject_reason": hard_reject_reason, "soft_penalty_notes": [], "exceptional_override": None, "shortlist_reason": "", "over_budget": False}
                        else:
                            soft_penalty_notes.append(msg)
        elif profile in ("Desktop",):
            floor_desk = config.get("desktop_minimum_vram_gb", 16.0)
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

def build_row(fm: dict, intake_info: dict, source_path: Path, md_text: str) -> dict:
    """Build a fully annotated shortlist row from a card's frontmatter."""

    # Raw field extraction
    item_name        = fm.get("name") or fm.get("item_name") or ""
    category         = fm.get("category", "UNKNOWN")
    gpu_model        = fm.get("gpu", "UNKNOWN")
    vram_raw         = str(fm.get("vram") or fm.get("vram_gb") or "UNKNOWN").replace("GB", "").strip()
    unified_raw      = str(fm.get("unified_memory") or fm.get("unified_memory_gb") or "UNKNOWN").replace("GB", "").strip()
    price_raw        = fm.get("price_aud", "UNKNOWN").replace("$", "").replace("AUD", "").strip()
    condition        = fm.get("condition", "UNKNOWN")
    retailer         = fm.get("retailer", "UNKNOWN")
    vstatus          = fm.get("verification", "UNKNOWN")
    au_stock         = fm.get("au_stock", "UNKNOWN")
    status           = fm.get("status", "Active")
    track            = fm.get("track", "UNKNOWN")
    pathway          = fm.get("pathway", "UNKNOWN")
    seller_class     = fm.get("seller_class", "UNKNOWN")
    source_platform  = fm.get("source_platform", "UNKNOWN")

    # Derived
    profile        = classify_profile(category)
    price_float, price_unknown = parse_price(price_raw)
    vram_float     = parse_vram(vram_raw)
    unified_float  = parse_vram(unified_raw)
    screen_raw     = str(fm.get("screen_size_in") or fm.get("screen_inches") or fm.get("screen_size") or "UNKNOWN").replace("in", "").strip()
    screen_size    = parse_vram(screen_raw)
    if screen_size is None:
        screen_size = parse_screen_size(md_text, item_name)
    thermal_flag   = parse_thermal_flag(md_text)
    cat_group      = classify_category_group(profile, gpu_model)

    # Intake ID from filename
    fname = source_path.name
    intake_id_match = re.match(r"([\w\d]+-\d+)", fname)
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
        "screen_size_in":       screen_size if screen_size is not None else "UNKNOWN",
        "thermal_flag":         thermal_flag,
        "price_aud":            price_float if price_float is not None else "UNKNOWN",
        "Price_Unknown":        "Yes" if price_unknown else "",
        "condition":            condition,
        "retailer":             retailer,
        "verification_status":  vstatus,
        "au_stock":             au_stock,
        "status":               status,
        "seller_class":         seller_class,
        "source_platform":      source_platform,
        # Engine metadata
        "Machine":              intake_id,   # rubric_weighting_engine.py expects this
        "Type":                 "Candidate", # default; user can change to Preferred/NeverBuy
        # Score columns — pull from frontmatter if present, else blank
        **{col: fm.get(col, "") for col in SCORE_COLUMNS},
        # Internal helpers (stripped before CSV output)
        "_price_float":         price_float,
        "_vram_float":          vram_float,
        "_unified_float":       unified_float,
    }
    return row


# ---------------------------------------------------------------------------
# Card scanner
# ---------------------------------------------------------------------------

def scan_intake_cards(
    batch_filter: str | None,
    profile_filter: str | None,
    track_filter: str | None,
    pathway_filter: str | None,
) -> list[dict]:
    """
    Walk all INTAKE_LANES and return a list of fully-built row dicts.
    """
    rows = []
    for lane in INTAKE_LANES:
        folder = REPO_ROOT / lane
        if not folder.exists():
            continue
        for md_path in sorted(folder.rglob("*.md")):
            text = md_path.read_text(encoding="utf-8", errors="replace")
            fm          = parse_frontmatter(text)
            intake_info = parse_tags_comment(text)

            if not fm:
                continue  # skip unparseable cards

            status = fm.get("status", "Active").strip().upper()
            if status in ("ARCHIVED", "REJECTED", "SOLD"):
                continue

            row = build_row(fm, intake_info, md_path, text)

            # Batch filter
            if batch_filter and batch_filter not in row["batch"]:
                continue

            # Profile filter
            if profile_filter and row["profile"].lower() != profile_filter.lower():
                continue

            # Track/pathway filters
            if track_filter and str(row["track"]).strip() != track_filter:
                continue
            if pathway_filter and str(row["pathway"]).strip().upper() != pathway_filter:
                continue

            rows.append(row)

    return rows


# ---------------------------------------------------------------------------
# CSV writers
# ---------------------------------------------------------------------------

SHORTLIST_FIELDNAMES = [
    "intake_id", "item_name", "status", "profile", "category", "Category_Group",
    "track", "pathway", "gpu_model", "vram_gb", "unified_memory_gb",
    "screen_size_in", "thermal_flag",
    "price_aud", "Over_Budget", "Price_Unknown",
    "condition", "retailer", "verification_status", "au_stock",
    "seller_class", "source_platform",
    "batch", "source_file", "exceptional_override", "shortlist_reason", "soft_penalty_notes",
    # Archetype transparency columns (Step 4)
    "archetype_used", "intent_notes",
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
  python scripts/build_shortlist.py --track 1 --pathway 1A

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
        "--track",
        default=None,
        choices=["1", "1.5", "2", "UNKNOWN"],
        help="Filter by track value (1, 1.5, 2, UNKNOWN)",
    )
    parser.add_argument(
        "--pathway",
        default=None,
        help="Filter by pathway value (1A, 1B, A, B, C, UNKNOWN)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview shortlist without writing any files",
    )
    parser.add_argument(
        "--spec-json",
        default=None,
        help="JSON string or file path containing SpecRequirements output from the Spec Clarifier Agent",
    )
    parser.add_argument(
        "--archetype",
        default=None,
        metavar="LABEL",
        help=(
            "Apply a named search archetype from config/search_archetypes.json. "
            "Example: --archetype gaming_laptop_private_sale. "
            "Overrides budget cap, VRAM floor, profile, track, and pathway filters "
            "from the archetype definition. "
            "Valid labels: gaming_laptop_private_sale, gaming_laptop_retailer, "
            "strix_halo_laptop, refurb_workstation_au"
        ),
    )
    args = parser.parse_args()

    # Load machine-readable config
    config = load_config()

    # ── Archetype override (--archetype) ────────────────────────────────────
    # Loaded BEFORE --spec-json so that spec-json can further narrow/override.
    archetype_label: Optional[str] = None
    if args.archetype:
        arch = load_archetype(args.archetype)
        archetype_label = arch["label"]

        price_ceil = arch.get("price", {}).get("hard_ceiling_aud")
        if price_ceil is not None:
            config["budget_cap_aud"] = float(price_ceil)

        spec = arch.get("spec", {})
        min_vram = spec.get("min_gpu_vram_gb")
        if min_vram is not None:
            config["laptop_discrete_minimum_vram_gb"] = float(min_vram)
        min_unified = spec.get("min_unified_memory_gb")
        if min_unified is not None:
            config["laptop_unified_minimum_vram_gb"] = float(min_unified)

        # Map track/pathway
        track_val = arch.get("track")
        pathway_val = arch.get("pathway")
        if track_val and args.track is None:
            args.track = str(track_val)
        if pathway_val and args.pathway is None:
            args.pathway = str(pathway_val)

        # Map profile from pathway
        if args.profile is None:
            pathway_lower = (pathway_val or "").lower()
            if pathway_lower in ("1a", "1b"):
                args.profile = "laptop"
            elif arch.get("track") == "1.5":
                args.profile = "desktop"

        print(f"✅ Loaded archetype '{archetype_label}': "
              f"budget_cap=${config['budget_cap_aud']:,.0f} AUD, "
              f"track={args.track}, pathway={args.pathway}, profile={args.profile}")

    if args.spec_json:
        try:
            if args.spec_json.strip().startswith("{"):
                spec = json.loads(args.spec_json)
            else:
                with open(args.spec_json, "r", encoding="utf-8") as f:
                    spec = json.load(f)
            
            # Apply spec overrides to config and filters dynamically
            if "budget_cap_aud" in spec:
                config["budget_cap_aud"] = spec["budget_cap_aud"]
            if "vram_floor_gb" in spec:
                config["laptop_discrete_minimum_vram_gb"] = spec["vram_floor_gb"]
                config["laptop_unified_minimum_vram_gb"] = spec["vram_floor_gb"]
                config["desktop_minimum_vram_gb"] = spec["vram_floor_gb"]
            if "track_preference" in spec and spec["track_preference"] != "Any":
                # Maps "1A" to track="1", pathway="1A"
                if spec["track_preference"] in ["1A", "1B"]:
                    args.track = "1"
                    args.pathway = spec["track_preference"]
                else:
                    args.track = spec["track_preference"]
            if "portability_requirement" in spec and spec["portability_requirement"] != "Any":
                args.profile = spec["portability_requirement"].lower()
                
            print(f"✅ Loaded overrides from --spec-json: {spec}")
        except Exception as e:
            print(f"⚠️ Failed to parse --spec-json: {e}")

    profile_filter = None if (args.profile in (None, "all")) else args.profile
    track_filter = None if args.track is None else args.track
    pathway_filter = None if args.pathway is None else args.pathway.strip().upper()

    print(f"\n🔍 Scanning intake cards in {WORKSPACE.relative_to(REPO_ROOT)} ...")
    all_rows = scan_intake_cards(args.batch, profile_filter, track_filter, pathway_filter)
    print(f"   Cards found: {len(all_rows)}")

    # Apply gates & policies
    shortlist = []
    rejected  = []

    for row in all_rows:
        eval_result = evaluate_policy(row, config)

        # ── Archetype transparency columns (Step 4) ──────────────────────
        row["archetype_used"] = archetype_label or ""
        if archetype_label:
            arch_data = load_archetype(archetype_label)
            row["intent_notes"] = arch_data.get("intent_notes_template", "")
        else:
            row["intent_notes"] = ""

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
    out_dir   = REPO_ROOT / "shortlists"
    suffix_parts = []
    if profile_filter:
        suffix_parts.append(f"profile-{profile_filter.replace(' ', '-')}")
    if track_filter:
        suffix_parts.append(f"track-{track_filter}")
    if pathway_filter:
        suffix_parts.append(f"pathway-{pathway_filter}")
    suffix = f"_{'_'.join(suffix_parts)}" if suffix_parts else ""

    sl_path   = out_dir / f"{today}_shortlist{suffix}.csv"
    rej_path  = out_dir / f"{today}_shortlist_rejected{suffix}.csv"

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
