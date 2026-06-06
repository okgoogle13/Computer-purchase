#!/usr/bin/env python3
"""
enrich_ebay_specs.py

Enriches parsed eBay watchlist candidates by scraping listing detail pages
via the Browserless API (with stealth mode enabled and no cookies) to extract 
structured specs (CPU, GPU, RAM, VRAM, Screen Size, Price).

Usage:
    python scripts/data_collection/enrich_ebay_specs.py [--csv path/to/parsed_watchlist.csv]
"""

import os
import sys
import re
import json
import csv
import urllib.request
from pathlib import Path
from html.parser import HTMLParser
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

class EbaySpecParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_tokens = []
        self.ignored_tags = {"script", "style", "head", "noscript", "iframe"}
        self.tag_stack = []
        
    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag.lower())
        
    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower in self.tag_stack:
            while self.tag_stack:
                popped = self.tag_stack.pop()
                if popped == tag_lower:
                    break
                    
    def handle_data(self, data):
        if any(ignored in self.tag_stack for ignored in self.ignored_tags):
            return
        clean_data = data.strip()
        if clean_data:
            self.text_tokens.append(clean_data)

def fetch_listing_html(url: str, api_key: str) -> str:
    print(f"Fetching listing details from: {url}")
    payload = {
        "url": url
    }
    # Note: We do NOT pass cookies to public item pages. 
    # Mismatch between Browserless server IP location and user cookies triggers CAPTCHA blocks.
    # Stealth mode is enabled to emulate normal browser environment.
    req_url = f"https://chrome.browserless.io/content?token={api_key}&stealth=true"
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
        print(f"Warning: Failed to fetch {url}: {e}", file=sys.stderr)
        return ""

def extract_specs_from_text(text: str, specs: dict) -> dict:
    """Helper to extract specs from text (like title) if they are still UNKNOWN."""
    # 1. CPU Model
    if specs["cpu_model"] == "UNKNOWN":
        cpu_match = re.search(r'\b(i[3579][-\s]\d{4,5}[a-zA-Z]*)\b', text, re.IGNORECASE)
        if not cpu_match:
            cpu_match = re.search(r'\b(ryzen\s*[3579]\s*\d{4}[a-zA-Z]*)\b', text, re.IGNORECASE)
        if not cpu_match:
            cpu_match = re.search(r'\b(ultra\s*[579]\s*\d{3}[a-zA-Z]*)\b', text, re.IGNORECASE)
        if not cpu_match:
            cpu_match = re.search(r'\b(xeon\s*[a-zA-Z0-9-]*)\b', text, re.IGNORECASE)
        if cpu_match:
            specs["cpu_model"] = cpu_match.group(1)
            
    # 2. GPU Model
    if specs["gpu_model"] == "UNKNOWN" or "about this item" in specs["gpu_model"].lower() or "refurbished" in specs["gpu_model"].lower():
        gpu_match = re.search(r'\b(rtx\s*\d{4}\s*(?:ti)?|rtx\s*(?:a)?\d{4}|rx\s*\d{4}[a-zA-Z]*|gtx\s*\d{4})\b', text, re.IGNORECASE)
        if gpu_match:
            specs["gpu_model"] = gpu_match.group(1)
            
    # 3. RAM capacity
    if specs["ram_gb"] == "UNKNOWN":
        ram_match = re.search(r'\b(\d+)\s*(?:gb|g)\s*(?:ddr\d|sdram)?\s*ram\b', text, re.IGNORECASE)
        if not ram_match:
            ram_match = re.search(r'\b(\d+)\s*(?:gb|g)\s*(?:ddr\d)\b', text, re.IGNORECASE)
        if ram_match:
            specs["ram_gb"] = ram_match.group(1)
            
    # 4. Storage capacity
    if specs["storage"] == "UNKNOWN":
        storage_match = re.search(r'(\d+)\s*(?:tb|gb)\s*(?:ssd|nvme|hdd)', text, re.IGNORECASE)
        if storage_match:
            specs["storage"] = storage_match.group(0)
            
    # 5. Screen Size
    if specs["screen_size_in"] == "UNKNOWN":
        screen_match = re.search(r'\b(1[345678](?:\.[0-9])?)\s*(?:”|"|inch|\-inch|in)\b', text, re.IGNORECASE)
        if screen_match:
            specs["screen_size_in"] = screen_match.group(1)
            
    return specs

def parse_specs_from_tokens(tokens: list[str], title: str = "") -> dict:
    specs = {
        "price_aud": "UNKNOWN",
        "cpu_model": "UNKNOWN",
        "gpu_model": "UNKNOWN",
        "ram_gb": "UNKNOWN",
        "vram_gb": "UNKNOWN",
        "screen_size_in": "UNKNOWN",
        "storage": "UNKNOWN"
    }
    
    # 0. Extract specs from the title first (most reliable source of candidate identity)
    if title:
        specs = extract_specs_from_text(title, specs)
    
    # Locate keys in flat token list
    for i, token in enumerate(tokens):
        token_lower = token.lower()
        
        # 1. Price search
        # Look for AU $1,234.56 or $1,234.56 in the token
        price_match = re.search(r'(?:AU\s*)?\$([0-9,]+\.[0-9]{2})', token)
        if price_match and specs["price_aud"] == "UNKNOWN":
            specs["price_aud"] = price_match.group(1).replace(",", "")
        elif not price_match:
            price_match_no_cents = re.search(r'(?:AU\s*)?\$([0-9,]+)', token)
            if price_match_no_cents:
                val = price_match_no_cents.group(1).replace(",", "")
                if val.isdigit() and 100 <= int(val) <= 15000:
                    if specs["price_aud"] == "UNKNOWN":
                        specs["price_aud"] = val

        # 2. Specifics table key-value pairs (usually Label token followed by Value token)
        if i + 1 < len(tokens):
            next_token = tokens[i+1]
            if "processor" in token_lower or token_lower == "cpu":
                if specs["cpu_model"] == "UNKNOWN":
                    specs["cpu_model"] = next_token
            elif "ram size" in token_lower or token_lower == "memory" or "installed size" in token_lower:
                if specs["ram_gb"] == "UNKNOWN":
                    specs["ram_gb"] = next_token
            elif "gpu" in token_lower or "graphics card" in token_lower or "video card" in token_lower or "graphics controller" in token_lower:
                if specs["gpu_model"] == "UNKNOWN":
                    specs["gpu_model"] = next_token
            elif "screen size" in token_lower:
                if specs["screen_size_in"] == "UNKNOWN":
                    specs["screen_size_in"] = next_token
            elif "storage capacity" in token_lower or "hard drive capacity" in token_lower or "ssd capacity" in token_lower:
                if specs["storage"] == "UNKNOWN":
                    specs["storage"] = next_token

    # Fallback to scanning title or first 300 tokens for missing specs
    limited_text = " ".join(tokens[:300])
    specs = extract_specs_from_text(limited_text, specs)
    if title:
        specs = extract_specs_from_text(title, specs)

    # 3. Post-parsing Validation & Cleanups
    
    # Clean up GPU model if it got set to price or other garbage
    gpu_clean = specs["gpu_model"].lower()
    gpu_invalid_keywords = ["$", "about", "refurbished", "select", "condition", "year", "seller", ","]
    if (specs["gpu_model"] == "UNKNOWN" or 
        any(x in gpu_clean for x in gpu_invalid_keywords) or
        len(specs["gpu_model"].strip()) < 3):
        # Force a fresh search on limited text
        gpu_match = re.search(r'\b(rtx\s*\d{4}\s*(?:ti)?|rtx\s*(?:a)?\d{4}|rx\s*\d{4}[a-zA-Z]*|gtx\s*\d{4})\b', limited_text, re.IGNORECASE)
        if not gpu_match and title:
            gpu_match = re.search(r'\b(rtx\s*\d{4}\s*(?:ti)?|rtx\s*(?:a)?\d{4}|rx\s*\d{4}[a-zA-Z]*|gtx\s*\d{4})\b', title, re.IGNORECASE)
        if gpu_match:
            specs["gpu_model"] = gpu_match.group(1)
        else:
            specs["gpu_model"] = "UNKNOWN"

    # Clean up CPU model if it got set to price or other garbage
    cpu_clean = specs["cpu_model"].lower()
    cpu_keywords = ["intel", "amd", "ryzen", "xeon", "threadripper", "i3", "i5", "i7", "i9", "ultra", "gold", "processor", "core"]
    if (specs["cpu_model"] == "UNKNOWN" or 
        any(x in cpu_clean for x in ["$", "notebook", "laptop", "pc", "computer", "select", "condition", "year"]) or
        not any(kw in cpu_clean for kw in cpu_keywords) or
        len(specs["cpu_model"].strip()) < 3):
        # Force a fresh search on limited text or title
        cpu_match = re.search(r'\b(i[3579][-\s]\d{4,5}[a-zA-Z]*)\b', limited_text, re.IGNORECASE)
        if not cpu_match:
            cpu_match = re.search(r'\b(ryzen\s*[3579]\s*\d{4}[a-zA-Z]*)\b', limited_text, re.IGNORECASE)
        if not cpu_match:
            cpu_match = re.search(r'\b(ultra\s*[579]\s*\d{3}[a-zA-Z]*)\b', limited_text, re.IGNORECASE)
        if not cpu_match:
            cpu_match = re.search(r'\b(xeon\s*[a-zA-Z0-9-]*)\b', limited_text, re.IGNORECASE)
        if not cpu_match:
            cpu_match = re.search(r'\b(ryzen\s*[3579])\b', limited_text, re.IGNORECASE)
        
        # Try title if still not found
        if not cpu_match and title:
            cpu_match = re.search(r'\b(i[3579][-\s]\d{4,5}[a-zA-Z]*)\b', title, re.IGNORECASE)
            if not cpu_match:
                cpu_match = re.search(r'\b(ryzen\s*[3579]\s*\d{4}[a-zA-Z]*)\b', title, re.IGNORECASE)
            if not cpu_match:
                cpu_match = re.search(r'\b(ultra\s*[579]\s*\d{3}[a-zA-Z]*)\b', title, re.IGNORECASE)
            if not cpu_match:
                cpu_match = re.search(r'\b(xeon\s*[a-zA-Z0-9-]*)\b', title, re.IGNORECASE)
            if not cpu_match:
                cpu_match = re.search(r'\b(ryzen\s*[3579])\b', title, re.IGNORECASE)

        if cpu_match:
            specs["cpu_model"] = cpu_match.group(1)
        else:
            specs["cpu_model"] = "UNKNOWN"

    # Standardize screen size (extract float)
    if specs["screen_size_in"] != "UNKNOWN":
        match = re.search(r'([0-9.]+)', specs["screen_size_in"])
        if match:
            specs["screen_size_in"] = match.group(1)

    # Standardize RAM (extract integer GB)
    if specs["ram_gb"] != "UNKNOWN":
        match = re.search(r'(\d+)\s*(?:GB|gb|G|g)', specs["ram_gb"])
        if match:
            specs["ram_gb"] = match.group(1)

    # Determine if candidate is a laptop for VRAM heuristics
    title_lower = title.lower()
    is_laptop = any(x in title_lower for x in ["laptop", "notebook", "book", "portable", "precision"]) or \
                (any(x in title_lower for x in ["strix", "scar", "legion", "blade", "proart", "zephyrus", "aorus", "predator", "vivobook"]) and \
                 not any(x in title_lower for x in ["desktop", "tower", "pc", "aio", "all-in-one"]))

    # Heuristic for discrete GPU VRAM if GPU model is found
    if specs["gpu_model"] != "UNKNOWN":
        gpu = specs["gpu_model"].lower()
        if "4090" in gpu:
            specs["vram_gb"] = "16" if (is_laptop or any(x in gpu for x in ["laptop", "mobile", "rtx", "notebook"])) else "24"
        elif "4080" in gpu:
            specs["vram_gb"] = "12" if (is_laptop or any(x in gpu for x in ["laptop", "mobile", "rtx", "notebook"])) else "16"
        elif "4070" in gpu:
            specs["vram_gb"] = "8"
        elif "3090" in gpu:
            specs["vram_gb"] = "24"
        elif "3080 ti" in gpu or "3080ti" in gpu:
            specs["vram_gb"] = "16" if (is_laptop or any(x in gpu for x in ["laptop", "mobile", "notebook"])) else "12"
        elif "3080" in gpu:
            specs["vram_gb"] = "8" if (is_laptop or any(x in gpu for x in ["laptop", "mobile", "notebook"])) else "10"
        elif "3070 ti" in gpu or "3070ti" in gpu:
            specs["vram_gb"] = "8"
        elif "3070" in gpu:
            specs["vram_gb"] = "8"
        elif "5080" in gpu:
            specs["vram_gb"] = "16"
        elif "5090" in gpu:
            specs["vram_gb"] = "32" if any(x in gpu for x in ["desktop", "workstation"]) else "16"
        elif "rtx 5000" in gpu or "rtx5000" in gpu:
            specs["vram_gb"] = "16"
        elif "rtx a4000" in gpu or "rtxa4000" in gpu:
            specs["vram_gb"] = "8" if (is_laptop or any(x in gpu for x in ["mobile", "laptop", "notebook"])) else "16"
        elif "rtx a3000" in gpu or "rtxa3000" in gpu:
            specs["vram_gb"] = "6"

    # Also scan limited_text or title for direct VRAM specifications
    vram_match = re.search(r'(\d+)\s*(?:gb|g)\s*(?:vram|gpu|graphics|video|card|discrete)', limited_text, re.IGNORECASE)
    if not vram_match and title:
        vram_match = re.search(r'(\d+)\s*(?:gb|g)\s*(?:vram|gpu|graphics|video|card|discrete)', title, re.IGNORECASE)
    if vram_match and specs["vram_gb"] == "UNKNOWN":
        specs["vram_gb"] = vram_match.group(1)

    return specs

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Enrich eBay candidates with specs.")
    parser.add_argument("--csv", type=str, default=None, help="Path to parsed watchlist CSV")
    args = parser.parse_args()

    # Load environment variables
    env = load_env_file(REPO_ROOT / ".env")
    for k, v in env.items():
        if k not in os.environ:
            os.environ[k] = v

    api_key = os.environ.get("BROWSERLESS_API_KEY")
    if not api_key or "your_" in api_key.lower():
        print("Error: BROWSERLESS_API_KEY is missing or holds placeholder value.", file=sys.stderr)
        sys.exit(1)

    # Find the latest parsed watchlist CSV
    csv_path = None
    if args.csv:
        csv_path = Path(args.csv)
    else:
        processed_dir = REPO_ROOT / "data" / "processed"
        if processed_dir.exists():
            csv_files = sorted(processed_dir.glob("parsed_watchlist_*.csv"))
            if csv_files:
                csv_path = csv_files[-1]

    if not csv_path or not csv_path.exists():
        print("Error: No parsed watchlist CSV found.", file=sys.stderr)
        sys.exit(1)

    print(f"Reading candidates from: {csv_path}")
    candidates = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        candidates = list(reader)

    enriched_candidates = []
    
    for row in candidates:
        url = row["url"]
        print(f"\nProcessing candidate: {row['title']}")
        html = fetch_listing_html(url, api_key)
        
        # Initialize default specs for merging
        specs = {
            "price_aud": "UNKNOWN",
            "cpu_model": "UNKNOWN",
            "gpu_model": "UNKNOWN",
            "ram_gb": "UNKNOWN",
            "vram_gb": "UNKNOWN",
            "screen_size_in": "UNKNOWN",
            "storage": "UNKNOWN"
        }
        
        if not html:
            print("Warning: HTML detail page could not be fetched (blocked/offline). Extracting specs from title only.")
            specs = parse_specs_from_tokens([], title=row["title"])
        else:
            parser = EbaySpecParser()
            parser.feed(html)
            specs = parse_specs_from_tokens(parser.text_tokens, title=row["title"])
            
        # Fallback price_aud to pre-parsed price_raw if price_aud was not found
        if (specs["price_aud"] == "UNKNOWN" or specs["price_aud"] == "") and row.get("price_raw") != "UNKNOWN":
            specs["price_aud"] = row["price_raw"]
            
        print("Extracted Specs:")
        for k, v in specs.items():
            print(f"  {k}: {v}")
            
        # Merge specifications back to the candidate row
        row.update(specs)
        enriched_candidates.append(row)

    # Save enriched candidates to a new file
    today = datetime.today().strftime("%Y-%m-%d")
    out_dir = REPO_ROOT / "data" / "processed"
    out_path = out_dir / f"enriched_watchlist_{today}.csv"
    
    fieldnames = ["listing_id", "title", "url", "price_raw", "price_aud", "retailer", "condition", 
                  "cpu_model", "gpu_model", "ram_gb", "vram_gb", "screen_size_in", "storage"]
                  
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(enriched_candidates)
        
    print(f"\nSaved enriched candidates to: {out_path}")

if __name__ == "__main__":
    main()
