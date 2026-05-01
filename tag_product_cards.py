#!/usr/bin/env python3
"""
tag_product_cards.py
Prepends a <!-- TAGS: ... --> block to every product card that doesn't already have one.
Run from the project root: python3 tag_product_cards.py
"""

import os

WS = "NotebookLM_Workspaces"

# Map: relative file path → tag string
TAGS = {
    # ── Apple Silicon ──────────────────────────────────────────────────────────
    "Apple_Silicon/01_apple-mac-studio-m4-max-64gb.md":
        "#AppleSilicon #UnifiedMemory #VRAM-64GB #New #PrimaryWorkstation #AgenticAI #ImageGeneration #Shortlist",
    "Apple_Silicon/02_mac-studio-m4-max-64gb1tb-education-config.md":
        "#AppleSilicon #UnifiedMemory #VRAM-64GB #New #EducationConfig #PrimaryWorkstation #AgenticAI #Shortlist",
    "Apple_Silicon/03_mac-studio-m4-max-64gb-unified-memory-1tb-ssd.md":
        "#AppleSilicon #UnifiedMemory #VRAM-64GB #New #PrimaryWorkstation #AgenticAI #NeedsReview",
    "Apple_Silicon/04_refurb-mac-studio-m2-ultra-64gb.md":
        "#AppleSilicon #UnifiedMemory #VRAM-64GB #Refurbished #PrimaryWorkstation #AgenticAI #NeedsReview",
    "Apple_Silicon/05_apple-macbook-pro-14-m4-pro-48gb.md":
        "#AppleSilicon #UnifiedMemory #VRAM-48GB #Laptop #New #Travel #SecondaryLaptop #Coding #NonUpgradeable",
    "Apple_Silicon/06_apple-macbook-pro-16-m3-max-48gb-open-box.md":
        "#AppleSilicon #UnifiedMemory #VRAM-48GB #Laptop #OpenBox #Travel #SecondaryLaptop #Coding #NonUpgradeable",
    "Apple_Silicon/07_refurbished-macbook-pro-16-inch-m4-max-48gb1tb.md":
        "#AppleSilicon #UnifiedMemory #VRAM-48GB #Laptop #Refurbished #Travel #SecondaryLaptop #Coding #NonUpgradeable",
    "Apple_Silicon/08_apple-mac-studio-m4-max-36gb.md":
        "#AppleSilicon #UnifiedMemory #VRAM-36GB #New #PrimaryWorkstation #AgenticAI #NeedsReview",

    # ── Desktop Towers — Refurbished ──────────────────────────────────────────
    "Desktop_Towers_Refurbished/09_alienware-aurora-r12-rtx-3090-refurbished.md":
        "#DesktopTower #NVIDIA #VRAM-24GB #Refurbished #SingleGPU #PrimaryWorkstation #AgenticAI #ImageGeneration #Shortlist",
    "Desktop_Towers_Refurbished/18_recompute-dell-precision-5820-tower-act-thinkpad-t14s-pairing.md":
        "#Workstation #NVIDIA #VRAM-24GB #Refurbished #Bundle #Expandable #PCIe-x16x16 #PrimaryWorkstation #SecondaryLaptop #AgenticAI #Shortlist",
    "Desktop_Towers_Refurbished/26_acer-predator-orion-7000-rtx-4080-super.md":
        "#DesktopTower #NVIDIA #VRAM-16GB #Refurbished #SingleGPU #PrimaryWorkstation #NeedsReview",
    "Desktop_Towers_Refurbished/28_hp-z4-g4-rtx-3090-refurbished.md":
        "#Workstation #NVIDIA #VRAM-24GB #Refurbished #Used #Expandable #PCIe-x16x16 #PrimaryWorkstation #AgenticAI #Shortlist",
    "Desktop_Towers_Refurbished/29_dell-precision-tower-7910-rtx-3090.md":
        "#Workstation #NVIDIA #VRAM-24GB #Refurbished #Used #Expandable #PCIe-x16x16 #PrimaryWorkstation #AgenticAI #Shortlist",

    # ── Desktop Towers — New ──────────────────────────────────────────────────
    "Desktop_Towers_New/12_supertech-rtx-4090-gaming-pc.md":
        "#DesktopTower #NVIDIA #VRAM-24GB #New #SingleGPU #PrimaryWorkstation #AgenticAI #ImageGeneration #NeedsReview",
    "Desktop_Towers_New/25_ple-ai-advanced-rtx-5070-ti.md":
        "#DesktopTower #NVIDIA #VRAM-16GB #New #SingleGPU #PrimaryWorkstation #Coding #NeedsReview",
    "Desktop_Towers_New/27_scorptec-eclipse-rtx-5070-ti.md":
        "#DesktopTower #NVIDIA #VRAM-16GB #New #SingleGPU #PrimaryWorkstation #NeedsReview",

    # ── Laptops ───────────────────────────────────────────────────────────────
    "Laptops/21_lenovo-legion-pro-7i-rtx-4090.md":
        "#Laptop #NVIDIA #VRAM-16GB #New #SingleGPU #AgenticAI #Coding #NonUpgradeable #NeedsReview",
    "Laptops/22_asus-rog-strix-scar-17-rtx-4090.md":
        "#Laptop #NVIDIA #VRAM-16GB #New #SingleGPU #AgenticAI #Coding #NonUpgradeable #NeedsReview",
    "Laptops/23_asus-rog-strix-scar-18-rtx-4090.md":
        "#Laptop #NVIDIA #VRAM-16GB #New #SingleGPU #AgenticAI #Coding #NonUpgradeable #NeedsReview",
    "Laptops/24_msi-stealth-16-ai-studio-rtx-4090.md":
        "#Laptop #NVIDIA #VRAM-16GB #New #SingleGPU #AgenticAI #Coding #Travel #NonUpgradeable #NeedsReview",

    # ── Mini PC and eGPU ─────────────────────────────────────────────────────
    "Mini_PC_and_eGPU/16_minisforum-ms-01-deg1-oculink-rtx-3090-24gb.md":
        "#MiniPC #OCuLink #eGPU #NVIDIA #VRAM-24GB #New #Expandable #AgenticAI #ConditionalBuy",

    # ── Custom Builds ─────────────────────────────────────────────────────────
    "Custom_Builds/13_refurb-3090-tower-thin-client.md":
        "#CustomBuild #DesktopTower #NVIDIA #VRAM-24GB #Refurbished #Bundle #Expandable #PrimaryWorkstation #SecondaryLaptop #AgenticAI #Shortlist",

    # ── Components ───────────────────────────────────────────────────────────
    "Components/11_mike-pc-msi-rtx-3090-aero-24gb-gpu-build-route.md":
        "#Component #NVIDIA #VRAM-24GB #Used #CustomBuild #NeedsReview",
    "Components/14_msi-rtx-3090-aero-24gb-standalone-gpu.md":
        "#Component #NVIDIA #VRAM-24GB #Used #NeedsReview",

    # ── Research and Sources ─────────────────────────────────────────────────
    "Research_and_Sources/15_normal-laptop-remote-gpu-rental.md":
        "#Strategy #Cloud_First #Remote_GPU #Laptop #NeedsReview",
    "Research_and_Sources/20_used-enterprise-workstation-or-data-center-gpu-path.md":
        "#Strategy #Workstation #NVIDIA #VRAM-24GB #Used #NeedsReview",

    # ── Decision System ───────────────────────────────────────────────────────
    "Decision_System/17_system_ram_gb_or_unified_memory_gb.md":
        "#DecisionAxis #RAM #UnifiedMemory #VRAM-Reference",
}

TAG_MARKER = "<!-- TAGS:"
tag_line = lambda tags: f"<!-- TAGS: {tags} -->\n"

applied = []
skipped = []

for rel_path, tags in TAGS.items():
    full_path = os.path.join(WS, rel_path)
    if not os.path.exists(full_path):
        print(f"⚠️  MISSING: {full_path}")
        continue
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    if TAG_MARKER in content:
        skipped.append(rel_path)
        continue
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(tag_line(tags) + content)
    applied.append(rel_path)

print(f"\n✅ Tags applied to {len(applied)} cards:")
for p in applied:
    print(f"   + {p}")

if skipped:
    print(f"\n⏭️  Skipped {len(skipped)} (already tagged):")
    for p in skipped:
        print(f"   · {p}")
