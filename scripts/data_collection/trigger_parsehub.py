#!/usr/bin/env python3
"""
trigger_parsehub.py

A script to trigger a ParseHub run for a specific project, wait for it to complete,
and download the resulting JSON data to the local data/raw directory.

Usage:
    python trigger_parsehub.py --project-token <TOKEN> --api-key <KEY>

Ensure you have your ParseHub API key and Project Token ready.
"""

import argparse
import requests
import time
import json
import os
from datetime import datetime

PARSEHUB_API_BASE = "https://www.parsehub.com/api/v2"

def main():
    parser = argparse.ArgumentParser(description="Trigger and download ParseHub runs.")
    parser.add_argument("--api-key", required=True, help="ParseHub API Key")
    parser.add_argument("--project-token", required=True, help="ParseHub Project Token")
    parser.add_argument("--output-dir", default="data/raw/facebook_marketplace", help="Directory to save the results")
    args = parser.parse_args()

    # 1. Trigger the run
    print(f"Triggering run for project {args.project_token}...")
    run_url = f"{PARSEHUB_API_BASE}/projects/{args.project_token}/run"
    resp = requests.post(run_url, data={"api_key": args.api_key})
    
    if not resp.ok:
        print(f"Error triggering run: {resp.status_code} {resp.text}")
        return

    run_data = resp.json()
    run_token = run_data.get("run_token")
    print(f"Run triggered successfully. Run Token: {run_token}")

    # 2. Poll for completion
    status_url = f"{PARSEHUB_API_BASE}/runs/{run_token}"
    
    while True:
        status_resp = requests.get(status_url, params={"api_key": args.api_key})
        if not status_resp.ok:
            print(f"Error checking status: {status_resp.status_code} {status_resp.text}")
            return
            
        status_info = status_resp.json()
        status = status_info.get("status")
        pages = status_info.get("pages", 0)
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Status: {status} | Pages scraped: {pages}")
        
        if status == "complete":
            break
        elif status in ["error", "cancelled"]:
            print(f"Run ended with status: {status}. Exiting.")
            return
            
        time.sleep(30) # Poll every 30 seconds

    # 3. Download the data
    print("Run complete! Downloading data...")
    data_url = f"{PARSEHUB_API_BASE}/runs/{run_token}/data"
    data_resp = requests.get(data_url, params={"api_key": args.api_key, "format": "json"})
    
    if not data_resp.ok:
        print(f"Error downloading data: {data_resp.status_code} {data_resp.text}")
        return

    # Ensure output dir exists
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Save the file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"parsehub_run_{run_token}_{timestamp}.json"
    filepath = os.path.join(args.output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(data_resp.text)
        
    print(f"Data saved successfully to: {filepath}")

if __name__ == "__main__":
    main()
