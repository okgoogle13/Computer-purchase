#!/usr/bin/env python3
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def fix_card(filename: str, old_str: str, new_str: str):
    card_path = REPO_ROOT / "cards" / filename
    if not card_path.exists():
        print(f"Error: {filename} not found.")
        return
    content = card_path.read_text(encoding="utf-8")
    content = content.replace(old_str, new_str)
    card_path.write_text(content, encoding="utf-8")
    print(f"Updated {filename}: replaced '{old_str}' with '{new_str}'")

def main():
    # Fix Razer Blade 18 (intake-002) -> seller_class: MANUFACTURER_AU
    fix_card(
        "intake-002_razer-blade-18-qhd-240hz-i9-13950hx-rtx4090-2tb-32gb-w11h-ga.md",
        "seller_class: EBAY_AU",
        "seller_class: MANUFACTURER_AU"
    )
    
    # Fix Lenovo Legion 9i (intake-004) -> seller_class: MAJOR_RETAILER_AU
    fix_card(
        "intake-004_lenovo-legion-9i-18-wquxga-intel-ultra-9-240hz-2tb-64gb-rtx5.md",
        "seller_class: EBAY_AU",
        "seller_class: MAJOR_RETAILER_AU"
    )
    
    # Re-run pipeline steps
    print("\nRe-running build_shortlist.py...")
    subprocess.run(["python", "scripts/build_shortlist.py", "--batch", "ebay_watchlist_2026-06-07_processed"], cwd=REPO_ROOT, check=True)
    
    print("\nRe-running enrich_shortlist_pricing.py...")
    subprocess.run(["python", "scripts/enrich_shortlist_pricing.py", "shortlists/2026-06-07_shortlist.csv", "--force"], cwd=REPO_ROOT, check=True)
    
    print("\nRe-running fill_mcda_gaps.py...")
    subprocess.run(["python", "scripts/fill_mcda_gaps.py", "shortlists/2026-06-07_shortlist_pricing_enriched.csv", "--output", "shortlists/2026-06-07_shortlist_pricing_enriched_live.csv"], cwd=REPO_ROOT, check=True)
    
    print("\nRe-running rubric_weighting_engine.py...")
    subprocess.run(["python", "scripts/scoring/rubric_weighting_engine.py", "--csv", "shortlists/2026-06-07_shortlist_pricing_enriched_live.csv", "--output-csv", "shortlists/2026-06-07_ranked_final.csv"], cwd=REPO_ROOT, check=True)

if __name__ == "__main__":
    main()
