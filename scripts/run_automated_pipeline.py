#!/usr/bin/env python3
"""
run_automated_pipeline.py — Orchestration harness for the hardware procurement system.
Uses dynamic, date-stamped file paths to run the pipeline phases.
"""

import argparse
import sys
import time
import subprocess
import re
import csv
from datetime import date
from pathlib import Path

# Identify repository root
REPO_ROOT = Path(__file__).resolve().parent.parent

# Preflight validation schemas
PHASE_INPUT_SCHEMA = {
    "Phase 3a: Enrich Shortlist Pricing": {
        "file_arg_index": 2,
        "required_columns": ["intake_id", "item_name", "gpu_model", "vram_gb"]
    },
    "Phase 3b: Fill Shortlist Live Pricing": {
        "file_arg_index": 2,
        "required_columns": ["intake_id", "item_name", "current_best_price_aud"]
    },
    "Phase 4: Fill MCDA Gaps": {
        "file_arg_index": 2,
        "required_columns": ["intake_id", "item_name", "in_stock_now"]
    },
    "Phase 5: Rubric Weighting Engine": {
        "file_arg_index": 3,
        "required_columns": ["intake_id", "MCDA_Total"]
    }
}

def validate_phase_input(step: dict) -> bool:
    name = step["name"]
    schema = PHASE_INPUT_SCHEMA.get(name)
    if not schema:
        return True
    
    cmd = step["cmd"]
    file_arg_index = schema["file_arg_index"]
    required_columns = schema["required_columns"]
    
    if len(cmd) <= file_arg_index:
        print(f"❌ Preflight Error: Command arguments list is too short for step '{name}' to extract file path at index {file_arg_index}.")
        return False
        
    file_path_str = cmd[file_arg_index]
    file_path = REPO_ROOT / file_path_str
    
    if not file_path.exists():
        print(f"❌ Preflight Error: Input file for step '{name}' does not exist: {file_path.resolve()}")
        return False
        
    try:
        with open(file_path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            if not headers:
                print(f"❌ Preflight Error: CSV file is empty or has no headers: {file_path_str}")
                return False
                
            # Read all rows to get count and validate
            rows = list(reader)
            row_count = len(rows)
            
        # Check required columns
        missing_cols = [col for col in required_columns if col not in headers]
        if missing_cols:
            print(f"❌ Preflight Error: CSV headers for step '{name}' are missing required columns: {missing_cols}")
            print(f"   Found headers: {headers}")
            return False
            
        if row_count == 0:
            print(f"❌ Preflight Error: CSV file for step '{name}' contains 0 data rows.")
            return False
            
        print(f"🔍 Preflight OK for '{name}': Verified file '{file_path_str}' ({row_count} rows, all required headers present).")
        return True
    except Exception as e:
        print(f"❌ Preflight Error: Failed to parse CSV file '{file_path_str}': {e}")
        return False

def run_command(cmd: list[str]) -> bool:
    print(f"\n>>> Running command: {' '.join(str(c) for c in cmd)}")
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            cwd=str(REPO_ROOT)
        )
        
        # Stream stdout/stderr live to terminal
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            if line:
                sys.stdout.write(line)
                sys.stdout.flush()
                
        returncode = process.poll()
        if returncode != 0:
            print(f"❌ Command failed with exit code {returncode}: {' '.join(str(c) for c in cmd)}")
            return False
        print("✅ Command completed successfully.")
        return True
    except Exception as e:
        print(f"❌ Exception occurred while running command: {e}")
        return False

def run_command_with_retry(cmd: list[str], max_retries: int = 3, backoff_seconds: int = 30) -> bool:
    """
    Run a command and retry on failure with exponential/progressive backoff.
    """
    for attempt in range(1, max_retries + 1):
        success = run_command(cmd)
        if success:
            return True
        if attempt < max_retries:
            sleep_time = backoff_seconds * attempt
            print(f"⚠️ Command failed. Retrying (attempt {attempt + 1}/{max_retries}) in {sleep_time} seconds...")
            time.sleep(sleep_time)
    return False

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Orchestrate the hardware procurement pipeline using dynamic date-stamped files."
    )
    parser.add_argument(
        "--batch",
        default=None,
        help="Optional batch filter for build_shortlist.py"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Skip live pricing Phase 3b; use existing pricing data for MCDA/ranking tests"
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Maximum retries for failing steps (specifically Phase 3b)"
    )
    args = parser.parse_args()

    # Dynamic date-stamped paths
    today = date.today().isoformat()
    shortlist_base = f"shortlists/{today}_shortlist_profile-laptop.csv"
    shortlist_enriched = f"shortlists/{today}_shortlist_profile-laptop_pricing_enriched.csv"
    shortlist_live = f"shortlists/{today}_shortlist_profile-laptop_pricing_enriched_live.csv"
    shortlist_ranked = f"shortlists/{today}_shortlist_profile-laptop_ranked.csv"

    # Define warnings to print
    high_context_warning = (
        "⚠️ HIGH CONTEXT OPERATION APPROACHING. Please ensure you have run "
        "/compact or /clear if running this within an interactive Claude session "
        "window to avoid token bloat."
    )

    # 1. Build Shortlist command
    build_cmd = [sys.executable, "scripts/build_shortlist.py", "--profile", "laptop"]
    if args.batch:
        build_cmd += ["--batch", args.batch]

    # 2. Define Phased Execution Steps
    steps = [
        # Phase 2: Shortlist Building
        {
            "name": "Phase 2: Build Shortlist",
            "cmd": build_cmd
        },
        
        # Phase 3: Pricing Scaffold & Fill
        {
            "name": "Phase 3a: Enrich Shortlist Pricing",
            "cmd": [sys.executable, "scripts/enrich_shortlist_pricing.py", shortlist_base, "--force"]
        },
        {
            "name": "Phase 3b: Fill Shortlist Live Pricing",
            "cmd": [sys.executable, "scripts/fill_shortlist_live_pricing.py", shortlist_enriched],
            "warning": high_context_warning,
            "skip_in_dry_run": True
        },
        
        # Phase 4: MCDA Scopes (Overwrites shortlist_live in place)
        {
            "name": "Phase 4: Fill MCDA Gaps",
            "cmd": [sys.executable, "scripts/fill_mcda_gaps.py", shortlist_live, "--output", shortlist_live]
        },
        
        # Phase 5: Scoring, Weighting & Verification
        {
            "name": "Phase 5: Rubric Weighting Engine",
            "cmd": [
                sys.executable,
                "scripts/scoring/rubric_weighting_engine.py",
                "--csv", shortlist_live,
                "--output-csv", shortlist_ranked
            ],
            "warning": high_context_warning
        },
        {
            "name": "Phase 5: Pipeline Integrity Check",
            "cmd": [
                sys.executable,
                "scripts/pipeline_integrity_check.py",
                "--enriched", shortlist_live,
                "--ranked", shortlist_ranked
            ]
        },
        
        # Card Audit Check (Runs on the final live shortlist compared to card inventory)
        {
            "name": "Audit: Run Gemini Card Audit",
            "cmd": [sys.executable, "scripts/run_gemini_card_audit.py", "--shortlist", shortlist_live]
        }
    ]

    print(f"Starting automated hardware procurement pipeline for date: {today}...")
    
    for step in steps:
        print(f"\n========================================\nExecuting step: {step['name']}")
        
        # Print warning if applicable, unless --dry-run is True
        if "warning" in step and not args.dry_run:
            print(f"\n{step['warning']}\n")
            
        # Check for dry-run skipping
        if args.dry_run and step.get("skip_in_dry_run"):
            print(f"[dry-run] Skipping: {step['name']}")
            continue
            
        # Preflight validation
        if not validate_phase_input(step):
            sys.exit(1)
            
        if step["name"] == "Phase 3b: Fill Shortlist Live Pricing":
            success = run_command_with_retry(step["cmd"], max_retries=args.max_retries)
        else:
            success = run_command(step["cmd"])
            
        if not success:
            print(f"\n❌ Pipeline execution halted due to failure in step: {step['name']}")
            sys.exit(1)

    print("\n🎉 All pipeline phases completed successfully!")

if __name__ == "__main__":
    main()
