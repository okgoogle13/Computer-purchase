import os
import json
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

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
        if "sameSite" in cookie:
            same_site = str(cookie["sameSite"]).lower()
            if same_site in {"strict", "lax", "none"}:
                clean_cookie["sameSite"] = same_site.capitalize()
            elif same_site == "no_restriction":
                clean_cookie["sameSite"] = "None"
        sanitized.append(clean_cookie)
    return sanitized

def main():
    env = load_env_file(REPO_ROOT / ".env")
    api_key = env.get("BROWSERLESS_API_KEY")
    if not api_key:
        print("Error: BROWSERLESS_API_KEY not found.")
        return

    # Load cookies
    cookies_path = REPO_ROOT / "secrets" / "ebay_cookies.json"
    cookies = []
    if cookies_path.exists():
        try:
            data = json.loads(cookies_path.read_text(encoding="utf-8"))
            if isinstance(data, dict) and "cookies" in data:
                cookies = data["cookies"]
            elif isinstance(data, list):
                cookies = data
            cookies = sanitize_cookies(cookies)
            print(f"Loaded and sanitized {len(cookies)} cookies.")
        except Exception as e:
            print(f"Failed to load cookies: {e}")

    url = "https://www.ebay.com.au/itm/137317465327"
    print(f"Fetching: {url}")
    
    req_url = f"https://chrome.browserless.io/content?token={api_key}&stealth=true"
    payload = {"url": url}
    if cookies:
        payload["cookies"] = cookies
        
    data = json.dumps(payload).encode("utf-8")
    
    req = urllib.request.Request(
        req_url,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=60) as res:
            html = res.read().decode("utf-8")
            print(f"Fetched {len(html)} bytes.")
            
            # Save to scratch/test_page.html
            out_path = REPO_ROOT / "scratch" / "test_page.html"
            out_path.parent.mkdir(exist_ok=True)
            out_path.write_text(html, encoding="utf-8")
            print(f"Saved to {out_path}")
            
            # Print first 1000 characters to check if it's a captcha block
            print("\nFirst 1000 characters of HTML:")
            print(html[:1000])
            
            # Check if CAPTCHA keywords are present
            keywords = ["captcha", "pardon our interruption", "distil", "robot", "block", "security check"]
            print("\nBlock checks:")
            for kw in keywords:
                if kw in html.lower():
                    print(f"  Found keyword: '{kw}'")
                else:
                    print(f"  Not found: '{kw}'")
                    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
