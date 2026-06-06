import os
import json
import requests
import urllib.parse

api_key = os.environ.get("BROWSERLESS_API_KEY")

def fetch_url(url):
    req_url = f"https://chrome.browserless.io/content?token={api_key}&stealth=true"
    payload = {"url": url, "gotoOptions": {"waitUntil": "networkidle2"}}
    print(f"Fetching {url} via Browserless...")
    res = requests.post(req_url, json=payload, headers={"Cache-Control": "no-cache"})
    if res.status_code == 200:
        return res.text
    else:
        print(f"Error {res.status_code}: {res.text}")
        return None

# Dell Recompute (Search and fetch)
dell_html = fetch_url("https://www.recompute.com.au/search.php?search_query=5820+3090")
with open("scratch/dell_recompute.html", "w") as f:
    f.write(dell_html or "")

# ASUS Mwave or ASUS Store
asus_html = fetch_url("https://au.store.asus.com/rog/rog-strix-g16-2025-g615.html")
with open("scratch/asus_store.html", "w") as f:
    f.write(asus_html or "")

print("HTML fetched successfully")
