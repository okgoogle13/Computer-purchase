#!/usr/bin/env python3
"""
facebook_search_automator.py

Automates targeted product searches on Facebook Marketplace using an already-authenticated
Chrome browser session via the Chrome DevTools Protocol (CDP).

Requirements:
  pip install playwright

Usage:
  1. Close all existing Chrome instances.
  2. Launch Chrome with CDP enabled:
     /Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --remote-debugging-port=9222
  3. Run this script:
     python scripts/data_collection/facebook_search_automator.py --targets "RTX 4080, Legion Pro 7i"
"""

import argparse
import asyncio
import json
import urllib.parse
from pathlib import Path
from datetime import datetime

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Error: playwright is not installed. Run: pip install playwright")
    exit(1)

REPO_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_ROOT / "data" / "raw" / "facebook_marketplace"
RAW_DIR.mkdir(parents=True, exist_ok=True)

async def run_search(cdp_url: str, targets: list[str], max_scrolls: int, max_price: int | None = None, headless: bool = False):
    today = datetime.today().strftime("%Y-%m-%d")
    output_file = RAW_DIR / f"targeted_search_{today}.json"
    
    collected_responses = []

    async def handle_response(response):
        if "api/graphql" in response.url and response.request.method == "POST":
            try:
                post_data = response.request.post_data
                if post_data and "MarketplaceSearch" in post_data:
                    json_data = await response.json()
                    collected_responses.append({
                        "url": response.url,
                        "status": response.status,
                        "data": json_data
                    })
                    print(f"  [+] Intercepted GraphQL response ({len(json_data)} bytes)")
            except Exception as e:
                pass # Ignore parsing errors for irrelevant requests

    async with async_playwright() as p:
        try:
            print(f"Connecting to browser via CDP at {cdp_url}...")
            browser = await p.chromium.connect_over_cdp(cdp_url)
            context = browser.contexts[0]
            page = await context.new_page()
            
            page.on("response", handle_response)
            
            for target in targets:
                target = target.strip()
                if not target:
                    continue
                    
                print(f"\n[*] Searching for: '{target}'")
                query = urllib.parse.quote(target)
                url = f"https://www.facebook.com/marketplace/melbourne/search/?query={query}&exact=false"
                if max_price:
                    url += f"&maxPrice={max_price}"
                url += "&sortBy=creation_time_descend"
                
                print(f"  Navigating to {url}")
                await page.goto(url, wait_until="networkidle")
                await page.wait_for_timeout(3000) # Give it time to render the first batch
                
                print(f"  Scrolling {max_scrolls} times to load more results...")
                for i in range(max_scrolls):
                    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    await page.wait_for_timeout(2000) # Wait for network requests
                
                print(f"  Finished scrolling for '{target}'")
            
            await page.close()
            await browser.close()
            
        except Exception as e:
            print(f"\n[!] Error during automation: {e}")
            print("\nMake sure Chrome is running with --remote-debugging-port=9222")
            print("Command (Mac): /Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --remote-debugging-port=9222")

    if collected_responses:
        print(f"\n[+] Saving {len(collected_responses)} intercepted GraphQL responses to {output_file}")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(collected_responses, f, indent=2)
    else:
        print("\n[-] No relevant GraphQL responses were intercepted.")

def main():
    parser = argparse.ArgumentParser(description="Automate targeted Facebook Marketplace searches.")
    parser.add_argument("--targets", required=True, help="Comma-separated list of search targets (e.g., 'RTX 4080, Strix Halo')")
    parser.add_argument("--cdp-url", default="http://localhost:9222", help="CDP URL (default: http://localhost:9222)")
    parser.add_argument("--scrolls", type=int, default=5, help="Number of times to scroll down per search (default: 5)")
    parser.add_argument("--max-price", type=int, default=4500, help="Maximum price in AUD (default: 4500)")
    args = parser.parse_args()

    targets_list = [t.strip() for t in args.targets.split(",")]
    asyncio.run(run_search(args.cdp_url, targets_list, args.scrolls, args.max_price))

if __name__ == "__main__":
    main()
