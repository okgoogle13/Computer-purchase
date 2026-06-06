#!/usr/bin/env python3
"""
scrape_ebay_watchlist.py

Scrapes the eBay watchlist page using the Browserless API or ParseHub API.
Supports loading cookies from secrets/ebay_cookies.json for authenticating the request.

Usage:
    python scripts/data_collection/scrape_ebay_watchlist.py [--method browserless|parsehub]
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parents[2]

def load_env_file(filepath: Path) -> dict[str, str]:
    env_vars = {}
    if not filepath.exists():
        return env_vars
    with filepath.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, val = line.split("=", 1)
                env_vars[key.strip()] = val.strip().strip("'\"")
    return env_vars
def sanitize_cookies(cookies_list: list) -> list:
    sanitized = []
    allowed_keys = {"name", "value", "domain", "path", "secure", "httpOnly"}
    for cookie in cookies_list:
        if not isinstance(cookie, dict):
            continue
        clean_cookie = {}
        for k in allowed_keys:
            if k in cookie:
                clean_cookie[k] = cookie[k]
        
        # Map sameSite values to standard Puppeteer enums
        if "sameSite" in cookie:
            same_site = str(cookie["sameSite"]).lower()
            if same_site in {"strict", "lax", "none"}:
                clean_cookie["sameSite"] = same_site.capitalize()
            elif same_site == "no_restriction":
                clean_cookie["sameSite"] = "None"
        sanitized.append(clean_cookie)
    return sanitized

def fetch_watchlist_via_browserless(api_key: str) -> str:
    print("Fetching eBay Watchlist via Browserless /content API...")
    url = "https://www.ebay.com.au/myb/Watchlist"
    cookies_path = REPO_ROOT / "secrets" / "ebay_cookies.json"
    cookies = []
    if cookies_path.exists():
        try:
            data = json.loads(cookies_path.read_text(encoding="utf-8"))
            if isinstance(data, dict) and "cookies" in data:
                cookies = data["cookies"]
            elif isinstance(data, list):
                cookies = data
            else:
                print("Warning: Invalid cookie JSON format. Expected list or object with 'cookies' key.")
            
            # Sanitize cookies to prevent schema validation failures in Browserless
            cookies = sanitize_cookies(cookies)
            print(f"Loaded and sanitized {len(cookies)} cookies from secrets/ebay_cookies.json")
        except Exception as e:
            print(f"Warning: Failed to load cookies: {e}")
    else:
        print("Notice: secrets/ebay_cookies.json not found. Requesting page without login cookies.")
        print("If the request fails or redirects to login, please export your cookies to secrets/ebay_cookies.json first.")

    # Format POST request for Browserless
    payload = {
        "url": url
    }
    if cookies:
        payload["cookies"] = cookies
    
    req_url = f"https://chrome.browserless.io/content?token={api_key}"
    data = json.dumps(payload).encode("utf-8")
    
    req = urllib.request.Request(
        req_url,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=60) as res:
            return res.read().decode("utf-8")
    except Exception as e:
        print(f"Error calling Browserless: {e}", file=sys.stderr)
        sys.exit(1)

def trigger_parsehub_run(api_key: str, project_token: str) -> str:
    print("Triggering ParseHub run...")
    url = f"https://www.parsehub.com/api/v2/projects/{project_token}/run"
    data = urllib.parse.urlencode({
        "api_key": api_key
    }).encode("utf-8")
    
    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req) as res:
            res_data = json.loads(res.read().decode("utf-8"))
            print(f"Run triggered successfully: {res_data.get('run_token')}")
            return res_data.get("run_token")
    except Exception as e:
        print(f"Error calling ParseHub: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Scrape eBay watchlist candidates.")
    parser.add_argument("--method", choices=["browserless", "parsehub"], default="browserless",
                        help="Data collection method (default: browserless)")
    args = parser.parse_args()

    # Load environment variables
    env = load_env_file(REPO_ROOT / ".env")
    for k, v in env.items():
        if k not in os.environ:
            os.environ[k] = v

    today = datetime.today().strftime("%Y-%m-%d")
    
    if args.method == "browserless":
        api_key = os.environ.get("BROWSERLESS_API_KEY")
        if not api_key or "your_" in api_key.lower():
            print("Error: BROWSERLESS_API_KEY is missing or holds placeholder value.", file=sys.stderr)
            sys.exit(1)
            
        html = fetch_watchlist_via_browserless(api_key)
        
        # Save raw HTML to data/raw/ebay_watchlist/
        out_dir = REPO_ROOT / "data" / "raw" / "ebay_watchlist"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"watchlist_{today}.html"
        out_path.write_text(html, encoding="utf-8")
        print(f"Saved raw watchlist HTML to {out_path}")
        
    elif args.method == "parsehub":
        api_key = os.environ.get("PARSEHUB_API_KEY")
        project_token = os.environ.get("PARSEHUB_WATCHLIST_PROJECT_TOKEN")
        if not api_key or not project_token or "your_" in api_key.lower() or "your_" in project_token.lower():
            print("Error: PARSEHUB_API_KEY or PARSEHUB_WATCHLIST_PROJECT_TOKEN is missing or placeholder.", file=sys.stderr)
            sys.exit(1)
            
        trigger_parsehub_run(api_key, project_token)

if __name__ == "__main__":
    main()
