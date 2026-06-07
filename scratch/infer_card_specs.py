#!/usr/bin/env python3
import re
from pathlib import Path

# Procurement policy thresholds
BUDGET_LAPTOP = 5000.0
BUDGET_TRACK2_A = 5000.0
BUDGET_TRACK2_B = 4000.0
BUDGET_TRACK2_C = 3500.0

LAPTOP_DISCRETE_VRAM_FLOOR = 8.0
LAPTOP_UNIFIED_MEM_FLOOR = 16.0
DESKTOP_VRAM_FLOOR = 16.0

def parse_float(val) -> float | None:
    if not val:
        return None
    text = str(val).strip().replace("$", "").replace(",", "").upper()
    if text in ("UNKNOWN", "N/A", "NONE", "-"):
        return None
    try:
        m = re.search(r"[-+]?\d*\.\d+|\d+", text)
        return float(m.group(0)) if m else None
    except Exception:
        return None

def parse_frontmatter(md_text: str) -> dict:
    match = re.search(r"^---\s*\n(.*?)\n---", md_text, re.DOTALL | re.MULTILINE)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        fm[key.strip()] = val.strip()
    return fm

def update_frontmatter(md_text: str, updates: dict) -> str:
    match = re.search(r"^---\s*\n(.*?)\n---", md_text, re.DOTALL | re.MULTILINE)
    if not match:
        return md_text
    
    fm_content = match.group(1)
    for key, val in updates.items():
        if re.search(rf"^{key}:", fm_content, re.MULTILINE):
            fm_content = re.sub(rf"^{key}:.*$", f"{key}: {val}", fm_content, flags=re.MULTILINE)
        else:
            fm_content = fm_content.rstrip() + f"\n{key}: {val}"
            
    return md_text[:match.start(1)] + fm_content + md_text[match.end(1):]

# Standard GPU mappings to normalized name and VRAM (in GB)
GPU_RULES = [
    # RTX 40 series
    (r"rtx\s*4090", "NVIDIA GeForce RTX 4090", {"laptop": 16.0, "desktop": 24.0}),
    (r"rtx\s*4080\s*super", "NVIDIA GeForce RTX 4080 SUPER", {"laptop": 12.0, "desktop": 16.0}),
    (r"rtx\s*4080", "NVIDIA GeForce RTX 4080", {"laptop": 12.0, "desktop": 16.0}),
    (r"rtx\s*4070\s*ti\s*super", "NVIDIA GeForce RTX 4070 Ti SUPER", {"laptop": 12.0, "desktop": 16.0}),
    (r"rtx\s*4070\s*ti", "NVIDIA GeForce RTX 4070 Ti", {"laptop": 8.0, "desktop": 12.0}),
    (r"rtx\s*4070", "NVIDIA GeForce RTX 4070", {"laptop": 8.0, "desktop": 12.0}),
    (r"rtx\s*4060\s*ti", "NVIDIA GeForce RTX 4060 Ti", {"laptop": 8.0, "desktop": 8.0}), # Default 8.0, 16.0 handled if specified
    (r"rtx\s*4060", "NVIDIA GeForce RTX 4060", {"laptop": 8.0, "desktop": 8.0}),
    # RTX 50 series (2025/2026 specs)
    (r"rtx\s*5090", "NVIDIA GeForce RTX 5090", {"laptop": 16.0, "desktop": 32.0}),
    (r"rtx\s*5080", "NVIDIA GeForce RTX 5080", {"laptop": 16.0, "desktop": 16.0}),
    (r"rtx\s*5070\s*ti", "NVIDIA GeForce RTX 5070 Ti", {"laptop": 12.0, "desktop": 16.0}),
    (r"rtx\s*5070", "NVIDIA GeForce RTX 5070", {"laptop": 12.0, "desktop": 12.0}),
    (r"rtx\s*5060", "NVIDIA GeForce RTX 5060", {"laptop": 8.0, "desktop": 8.0}),
    # RTX 30 series
    (r"rtx\s*3090", "NVIDIA GeForce RTX 3090", {"laptop": 24.0, "desktop": 24.0}),
    (r"rtx\s*3080\s*ti", "NVIDIA GeForce RTX 3080 Ti", {"laptop": 16.0, "desktop": 12.0}),
    (r"rtx\s*3080", "NVIDIA GeForce RTX 3080", {"laptop": 8.0, "desktop": 10.0}), # Default laptop/desktop
    (r"rtx\s*3070\s*ti", "NVIDIA GeForce RTX 3070 Ti", {"laptop": 8.0, "desktop": 8.0}),
    (r"rtx\s*3070", "NVIDIA GeForce RTX 3070", {"laptop": 8.0, "desktop": 8.0}),
    (r"rtx\s*3060\s*ti", "NVIDIA GeForce RTX 3060 Ti", {"laptop": 8.0, "desktop": 8.0}),
    (r"rtx\s*3060", "NVIDIA GeForce RTX 3060", {"laptop": 6.0, "desktop": 12.0}),
    (r"rtx\s*3050\s*ti", "NVIDIA GeForce RTX 3050 Ti", {"laptop": 4.0, "desktop": 4.0}),
    (r"rtx\s*3050", "NVIDIA GeForce RTX 3050", {"laptop": 4.0, "desktop": 8.0}),
    # RTX 20 series
    (r"rtx\s*2080\s*ti", "NVIDIA GeForce RTX 2080 Ti", {"laptop": 11.0, "desktop": 11.0}),
    (r"rtx\s*2080", "NVIDIA GeForce RTX 2080", {"laptop": 8.0, "desktop": 8.0}),
    (r"rtx\s*2070\s*super", "NVIDIA GeForce RTX 2070 SUPER", {"laptop": 8.0, "desktop": 8.0}),
    (r"rtx\s*2070", "NVIDIA GeForce RTX 2070", {"laptop": 8.0, "desktop": 8.0}),
    (r"rtx\s*2060\s*super", "NVIDIA GeForce RTX 2060 SUPER", {"laptop": 8.0, "desktop": 8.0}),
    (r"rtx\s*2060", "NVIDIA GeForce RTX 2060", {"laptop": 6.0, "desktop": 6.0}),
    # GTX series
    (r"gtx\s*1080\s*ti", "NVIDIA GeForce GTX 1080 Ti", {"laptop": 11.0, "desktop": 11.0}),
    (r"gtx\s*1080", "NVIDIA GeForce GTX 1080", {"laptop": 8.0, "desktop": 8.0}),
    (r"gtx\s*1070\s*ti", "NVIDIA GeForce GTX 1070 Ti", {"laptop": 8.0, "desktop": 8.0}),
    (r"gtx\s*1070", "NVIDIA GeForce GTX 1070", {"laptop": 8.0, "desktop": 8.0}),
    (r"gtx\s*1060", "NVIDIA GeForce GTX 1060", {"laptop": 6.0, "desktop": 6.0}),
    (r"gtx\s*1660\s*ti", "NVIDIA GeForce GTX 1660 Ti", {"laptop": 6.0, "desktop": 6.0}),
    (r"gtx\s*1660\s*super", "NVIDIA GeForce GTX 1660 SUPER", {"laptop": 6.0, "desktop": 6.0}),
    (r"gtx\s*1660", "NVIDIA GeForce GTX 1660", {"laptop": 6.0, "desktop": 6.0}),
    (r"gtx\s*1650", "NVIDIA GeForce GTX 1650", {"laptop": 4.0, "desktop": 4.0}),
    (r"gtx\s*970", "NVIDIA GeForce GTX 970", {"laptop": 3.5, "desktop": 4.0}),
    (r"gtx\s*980\s*ti", "NVIDIA GeForce GTX 980 Ti", {"laptop": 6.0, "desktop": 6.0}),
    (r"gtx\s*980", "NVIDIA GeForce GTX 980", {"laptop": 4.0, "desktop": 4.0}),
    (r"gtx\s*970m", "NVIDIA GeForce GTX 970M", {"laptop": 3.0, "desktop": 3.0}),
    # AMD Radeon RX series
    (r"rx\s*7900\s*xtx", "AMD Radeon RX 7900 XTX", {"laptop": 24.0, "desktop": 24.0}),
    (r"rx\s*7900\s*xt", "AMD Radeon RX 7900 XT", {"laptop": 20.0, "desktop": 20.0}),
    (r"rx\s*7800\s*xt", "AMD Radeon RX 7800 XT", {"laptop": 16.0, "desktop": 16.0}),
    (r"rx\s*7700\s*xt", "AMD Radeon RX 7700 XT", {"laptop": 12.0, "desktop": 12.0}),
    (r"rx\s*7600\s*xt", "AMD Radeon RX 7600 XT", {"laptop": 16.0, "desktop": 16.0}),
    (r"rx\s*7600", "AMD Radeon RX 7600", {"laptop": 8.0, "desktop": 8.0}),
    (r"rx\s*6900\s*xt", "AMD Radeon RX 6900 XT", {"laptop": 16.0, "desktop": 16.0}),
    (r"rx\s*6800\s*xt", "AMD Radeon RX 6800 XT", {"laptop": 16.0, "desktop": 16.0}),
    (r"rx\s*6800", "AMD Radeon RX 6800", {"laptop": 16.0, "desktop": 16.0}),
    (r"rx\s*6700\s*xt", "AMD Radeon RX 6700 XT", {"laptop": 12.0, "desktop": 12.0}),
    (r"rx\s*6600\s*xt", "AMD Radeon RX 6600 XT", {"laptop": 8.0, "desktop": 8.0}),
    (r"rx\s*6600", "AMD Radeon RX 6600", {"laptop": 8.0, "desktop": 8.0}),
    # Professional GPUs
    (r"rtx\s*6000\s*ada", "NVIDIA RTX 6000 Ada", {"laptop": 48.0, "desktop": 48.0}),
    (r"rtx\s*5000\s*ada", "NVIDIA RTX 5000 Ada", {"laptop": 32.0, "desktop": 32.0}),
    (r"rtx\s*4000\s*ada", "NVIDIA RTX 4000 Ada", {"laptop": 20.0, "desktop": 20.0}),
    (r"rtx\s*2000\s*ada", "NVIDIA RTX 2000 Ada", {"laptop": 16.0, "desktop": 16.0}),
    (r"a6000", "NVIDIA RTX A6000", {"laptop": 48.0, "desktop": 48.0}),
    (r"a5000", "NVIDIA RTX A5000", {"laptop": 24.0, "desktop": 24.0}),
    (r"a4000", "NVIDIA RTX A4000", {"laptop": 16.0, "desktop": 16.0}),
    (r"radeon\s*pro\s*w7900", "AMD Radeon Pro W7900", {"laptop": 48.0, "desktop": 48.0}),
    (r"arc\s*pro\s*b70", "Intel Arc Pro B70", {"laptop": 32.0, "desktop": 32.0}),
]

INTEGRATED_SIGNALS = [
    "intel hd", "intel iris", "iris xe", "radeon 780m", "radeon 680m", "radeon 760m",
    "integrated graphics", "graphics card 2gb", "integrated intel", "radeon graphics",
    "uhd graphics"
]

def scan_for_gpu_and_vram(title: str, body: str, is_laptop: bool) -> tuple[str | None, float | None, bool]:
    full_text = (title + " " + body).lower()
    
    # 1. Check for discrete GPUs
    for pattern, normalized, vram_map in GPU_RULES:
        if re.search(pattern, full_text):
            # Check for explicit VRAM count in text near GPU or title
            vram = None
            vram_match = re.search(r"(\d+)\s*(gb|g)\s*(vram|gddr|gpu\s*memory|graphics)", full_text)
            if vram_match:
                vram = float(vram_match.group(1))
            else:
                profile_key = "laptop" if is_laptop else "desktop"
                vram = vram_map.get(profile_key)
            return normalized, vram, False

    # 2. Check for integrated graphics signals
    for signal in INTEGRATED_SIGNALS:
        if signal in full_text:
            return "Integrated Graphics", 0.0, True
            
    return None, None, False

def extract_screen_size(title: str, body: str) -> float | None:
    haystack = (title + " " + body).lower()
    
    # Model regex mappings with word boundaries
    model_regexes = [
        (r"\bpx13\b", 13.3),
        (r"\bz13\b", 13.4),
        (r"\ba14\b", 14.0),
        (r"\bblade\s+14\b", 14.0),
        (r"\bpx14\b", 14.0),
        (r"\bzenbook\s+14\b", 14.0),
        (r"\bg14\b", 14.0),
        (r"\ba16\b", 16.0),
        (r"\bg16\b", 16.0),
        (r"\bmax\s+16\b", 16.0),
        (r"\bhelios\s+neo\s+16\b", 16.0),
        (r"\bomen\s+16\b", 16.0),
        (r"\blegion\s+slim\s+5\s+14\b", 14.0),
        (r"\blegion\s+16\b", 16.0),
        (r"\blegion\s+pro\s+7i\s+16\b", 16.0),
        (r"\blegion\s+pro\s+7i\b", 16.0),
        (r"\balienware\s+16\b", 16.0),
        (r"\balienware\s+x16\b", 16.0),
        (r"\bkatana\s+17\b", 17.3),
        (r"\bvector\s+17\b", 17.0),
        (r"\braider\s+ge78\b", 17.0),
        (r"\bhelios\s+18\b", 18.0),
        (r"\btitan\s+18\b", 18.0),
        (r"\braider\s+18\b", 18.0),
        (r"\bblade\s+18\b", 18.0),
        (r"\balienware\s+18\b", 18.0),
        (r"\balienware\s+m18\b", 18.0),
        (r"\barea-51\s+18\b", 18.0),
    ]
    
    for pattern, val in model_regexes:
        if re.search(pattern, haystack):
            return val
            
    patterns = [
        r"(\d{2}(?:\.\d)?)\s*(?:inch|in\b|\")",
        r"\b(\d{2}(?:\.\d)?)\s*screen\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, haystack)
        if match:
            val = float(match.group(1))
            if 10 <= val <= 21:
                return val
    return None

def main():
    cards_dir = Path("cards")
    all_cards = list(cards_dir.rglob("*.md"))
    
    updated_count = 0
    archived_count = 0
    
    for path in all_cards:
        text = path.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        if not fm:
            continue
            
        status = fm.get("status", "").strip().upper()
        if status in ("ARCHIVED", "REJECTED", "SOLD"):
            continue
            
        category = fm.get("category", "").strip().lower()
        is_laptop = "laptop" in category or fm.get("track") == "1"
        is_fb = path.name.startswith("fb-") or fm.get("source_platform") == "FB_MARKETPLACE"
        
        # Get body text
        body = text
        fm_match = re.search(r"^---\s*\n.*?\n---\s*\n", text, re.DOTALL | re.MULTILINE)
        if fm_match:
            body = text[fm_match.end():]
            
        title = fm.get("name") or path.stem.replace("-", " ")
        
        # Check current frontmatter specs
        current_gpu = fm.get("gpu", "").strip().upper()
        current_vram = parse_float(fm.get("vram"))
        current_unified = parse_float(fm.get("unified_memory"))
        current_screen = parse_float(fm.get("screen_size_in"))
        
        updates = {}
        reasons = []
        
        # 1. Infer GPU and VRAM if UNKNOWN
        if current_gpu == "UNKNOWN" or not current_gpu or current_vram is None:
            lookup_text = body
            if current_gpu and current_gpu != "UNKNOWN":
                lookup_text = current_gpu + " " + lookup_text
            inferred_gpu, inferred_vram, is_integrated = scan_for_gpu_and_vram(title, lookup_text, is_laptop)
            if inferred_gpu:
                if current_gpu == "UNKNOWN" or not current_gpu:
                    updates["gpu"] = inferred_gpu
                    current_gpu = inferred_gpu.upper()
                if inferred_vram is not None and current_vram is None:
                    updates["vram"] = f"{inferred_vram} GB"
                    current_vram = inferred_vram
                print(f"[{path.name}] Inferred GPU specs: {current_gpu} ({current_vram} GB VRAM)")
        
        # 2. Infer screen size if UNKNOWN
        if (current_screen is None or current_screen == 0) and is_laptop:
            inferred_screen = extract_screen_size(title, body)
            if inferred_screen:
                updates["screen_size_in"] = str(inferred_screen)
                current_screen = inferred_screen
                print(f"[{path.name}] Inferred screen size: {inferred_screen} in")

        # 3. Apply procurement thresholds and policy gates
        price = parse_float(fm.get("price_aud") or fm.get("list_price_aud"))
        track = str(fm.get("track", "")).strip()
        pathway = str(fm.get("pathway", "")).strip().upper()
        
        # Laptop path constraints
        if is_laptop:
            if price is not None and price > BUDGET_LAPTOP:
                reasons.append(f"Price {price} > laptop budget cap {BUDGET_LAPTOP}")
            
            # Check discrete laptop rules
            if pathway in ("1A", "A", "UNKNOWN"):
                if current_screen is not None and current_screen < 16.0:
                    reasons.append(f"Screen size {current_screen} < 16.0 in floor")
                if current_vram is not None and current_vram < LAPTOP_DISCRETE_VRAM_FLOOR:
                    reasons.append(f"Discrete VRAM {current_vram} GB < floor {LAPTOP_DISCRETE_VRAM_FLOOR} GB")
                    
            # Check unified laptop rules
            elif pathway == "1B":
                if current_unified is not None and current_unified < LAPTOP_UNIFIED_MEM_FLOOR:
                    reasons.append(f"Unified memory {current_unified} GB < floor {LAPTOP_UNIFIED_MEM_FLOOR} GB")
                # Check SoC
                soc_ok = any(sig in (fm.get("gpu", "") + " " + title + " " + body).lower() 
                            for sig in ("strix halo", "ryzen ai max"))
                if not soc_ok:
                    reasons.append("SoC is not Strix Halo / Ryzen AI Max")

        # Desktop constraints
        elif category == "desktop" or track == "1.5" or track == "2":
            # Budget caps for Track 2
            if track == "2":
                cap = BUDGET_TRACK2_A if pathway == "A" else (BUDGET_TRACK2_B if pathway == "B" else BUDGET_TRACK2_C)
                if price is not None and price > cap:
                    reasons.append(f"Price {price} > Track 2{pathway} budget cap {cap}")
            
            # Desktop VRAM floor
            if current_vram is not None and current_vram < DESKTOP_VRAM_FLOOR:
                reasons.append(f"Desktop VRAM {current_vram} GB < floor {DESKTOP_VRAM_FLOOR} GB")

        # Archive if it's an Facebook Marketplace listing with unknown specs
        if is_fb:
            if current_gpu == "UNKNOWN" or not current_gpu or "INTEGRATED" in current_gpu:
                reasons.append("Facebook Marketplace listing with UNKNOWN or integrated GPU specs")
            elif current_vram is None and current_unified is None:
                reasons.append("Facebook Marketplace listing with UNKNOWN VRAM/memory specs")

        # Archive if any gating policies failed
        if reasons:
            updates["status"] = "ARCHIVED"
            archived_count += 1
            print(f"[{path.name}] Archived: {'; '.join(reasons)}")
        
        if updates:
            new_text = update_frontmatter(text, updates)
            path.write_text(new_text, encoding="utf-8")
            updated_count += 1
            
    print(f"\nScan complete: updated {updated_count} cards, archived {archived_count} non-viable cards.")

if __name__ == "__main__":
    main()
