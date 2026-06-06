import os
import json
import urllib.parse
import requests
from dotenv import load_dotenv

load_dotenv()

BROWSERLESS_KEY = os.environ.get("BROWSERLESS_API_KEY")
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")

def test():
    print(f"Browserless: {BROWSERLESS_KEY[:5]}...")
    print(f"Gemini: {GEMINI_KEY[:5]}...")
    
test()
