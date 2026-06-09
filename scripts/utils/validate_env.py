#!/usr/bin/env python3
"""
validate_env.py

Validates that all required environment variables are present and populated
with non-placeholder values.

Usage:
    python scripts/utils/validate_env.py
"""

import os
import sys
from pathlib import Path

REQUIRED_VARS = [
    "BROWSERLESS_API_KEY",
    "GEMINI_API_KEY",
    "GITHUB_TOKEN",
    "GITHUB_REPO",
]

OPTIONAL_VARS = [
    "OPENAI_API_KEY",
]

# Source URLs for documentation / help
OBTAIN_SOURCES = {
    "BROWSERLESS_API_KEY": "https://www.browserless.io/",
    "GEMINI_API_KEY": "https://aistudio.google.com/apikey",
    "OPENAI_API_KEY": "https://platform.openai.com/api-keys",
    "GITHUB_TOKEN": "https://github.com/settings/tokens",
    "GITHUB_REPO": "Repository path, e.g., okgoogle13/Computer-purchase",
}

def load_env_file(filepath: Path) -> dict[str, str]:
    """Manually parse .env file to avoid external dependency (python-dotenv)."""
    env_vars = {}
    if not filepath.exists():
        return env_vars
    
    with filepath.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue
            # Parse key-value pairs
            if "=" in line:
                key, val = line.split("=", 1)
                # Strip spaces, and quotes if any
                key = key.strip()
                val = val.strip().strip("'\"")
                env_vars[key] = val
    return env_vars

def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    env_path = repo_root / ".env"
    
    # Load env variables from .env file into os.environ if not already present
    env_vars = load_env_file(env_path)
    for k, v in env_vars.items():
        if k not in os.environ:
            os.environ[k] = v

    missing = []
    
    for var in REQUIRED_VARS:
        val = os.environ.get(var)
        # Check if missing, empty, or placeholder
        is_missing = not val
        is_placeholder = False
        if val:
            val_lower = val.lower()
            if "your_" in val_lower or "here" in val_lower:
                is_placeholder = True
        
        if is_missing or is_placeholder:
            missing.append((var, "missing" if is_missing else "placeholder"))

    if missing:
        print("Error: Missing or placeholder environment variables detected.", file=sys.stderr)
        for var, reason in missing:
            source = OBTAIN_SOURCES.get(var, "Unknown source")
            print(f"  ✗ {var} — {reason}.", file=sys.stderr)
            print(f"    → Obtain from: {source}", file=sys.stderr)
            print(f"    → Add to: .env at project root", file=sys.stderr)
        return 1

    # Print success output (without showing actual credentials)
    for var in REQUIRED_VARS:
        print(f"  ✓ {var} — present (value hidden)")
        
    for var in OPTIONAL_VARS:
        val = os.environ.get(var)
        is_missing = not val or "your_" in val.lower() or "here" in val.lower()
        if is_missing:
            print(f"  ? {var} — skipped (optional, using Gemini instead)")
        else:
            print(f"  ✓ {var} — present (value hidden, optional)")
            
    print("\nAll credentials validated. Safe to run pipeline.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
