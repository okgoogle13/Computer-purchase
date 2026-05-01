#!/usr/bin/env bash
# sort_product_cards.sh
# Moves all 29 product cards from the archive into their designated workspace lanes.
# Run from the project root: bash sort_product_cards.sh

set -e

SRC="_Archive_Legacy_Data/product_cards"
WS="NotebookLM_Workspaces"

# ── Apple Silicon ──────────────────────────────────────────────
mv "$SRC/01_apple-mac-studio-m4-max-64gb.md"                        "$WS/Apple_Silicon/"
mv "$SRC/02_mac-studio-m4-max-64gb1tb-education-config.md"          "$WS/Apple_Silicon/"
mv "$SRC/03_mac-studio-m4-max-64gb-unified-memory-1tb-ssd.md"       "$WS/Apple_Silicon/"
mv "$SRC/04_refurb-mac-studio-m2-ultra-64gb.md"                     "$WS/Apple_Silicon/"
mv "$SRC/05_apple-macbook-pro-14-m4-pro-48gb.md"                    "$WS/Apple_Silicon/"
mv "$SRC/06_apple-macbook-pro-16-m3-max-48gb-open-box.md"           "$WS/Apple_Silicon/"
mv "$SRC/07_refurbished-macbook-pro-16-inch-m4-max-48gb1tb.md"      "$WS/Apple_Silicon/"
mv "$SRC/08_apple-mac-studio-m4-max-36gb.md"                        "$WS/Apple_Silicon/"

# ── Desktop Towers — Refurbished ─────────────────────────────
mv "$SRC/09_alienware-aurora-r12-rtx-3090-refurbished.md"           "$WS/Desktop_Towers_Refurbished/"
mv "$SRC/18_recompute-dell-precision-5820-tower-act-thinkpad-t14s-pairing.md" "$WS/Desktop_Towers_Refurbished/"
mv "$SRC/26_acer-predator-orion-7000-rtx-4080-super.md"             "$WS/Desktop_Towers_Refurbished/"
mv "$SRC/28_hp-z4-g4-rtx-3090-refurbished.md"                       "$WS/Desktop_Towers_Refurbished/"
mv "$SRC/29_dell-precision-tower-7910-rtx-3090.md"                  "$WS/Desktop_Towers_Refurbished/"

# ── Desktop Towers — New ─────────────────────────────────────
mv "$SRC/12_supertech-rtx-4090-gaming-pc.md"                        "$WS/Desktop_Towers_New/"
mv "$SRC/25_ple-ai-advanced-rtx-5070-ti.md"                         "$WS/Desktop_Towers_New/"
mv "$SRC/27_scorptec-eclipse-rtx-5070-ti.md"                        "$WS/Desktop_Towers_New/"

# ── Laptops ──────────────────────────────────────────────────
mv "$SRC/21_lenovo-legion-pro-7i-rtx-4090.md"                       "$WS/Laptops/"
mv "$SRC/22_asus-rog-strix-scar-17-rtx-4090.md"                     "$WS/Laptops/"
mv "$SRC/23_asus-rog-strix-scar-18-rtx-4090.md"                     "$WS/Laptops/"
mv "$SRC/24_msi-stealth-16-ai-studio-rtx-4090.md"                   "$WS/Laptops/"

# ── Mini PC and eGPU ─────────────────────────────────────────
mv "$SRC/16_minisforum-ms-01-deg1-oculink-rtx-3090-24gb.md"         "$WS/Mini_PC_and_eGPU/"

# ── Custom Builds ────────────────────────────────────────────
mv "$SRC/10_custom-rtx-3090-24gb-desktop-refurbished-thinkpad-bundle.md" "$WS/Custom_Builds/"
mv "$SRC/13_refurb-3090-tower-thin-client.md"                        "$WS/Custom_Builds/"
mv "$SRC/19_custom-rtx-3090-24gb-desktop-refurbished-thinkpad-class-laptop.md" "$WS/Custom_Builds/"

# ── Components ───────────────────────────────────────────────
mv "$SRC/11_mike-pc-msi-rtx-3090-aero-24gb-gpu-build-route.md"      "$WS/Components/"
mv "$SRC/14_msi-rtx-3090-aero-24gb-standalone-gpu.md"               "$WS/Components/"

# ── Research and Sources ─────────────────────────────────────
mv "$SRC/15_normal-laptop-remote-gpu-rental.md"                      "$WS/Research_and_Sources/"
mv "$SRC/20_used-enterprise-workstation-or-data-center-gpu-path.md"  "$WS/Research_and_Sources/"

# ── Decision System ───────────────────────────────────────────
mv "$SRC/17_system_ram_gb_or_unified_memory_gb.md"                   "$WS/Decision_System/"

echo "✅ All 29 cards sorted."
