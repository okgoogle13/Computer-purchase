This file is a merged representation of a subset of the codebase, containing specifically included files and files not matching ignore patterns, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: NotebookLM_Workspaces/intake/shortlist/*.csv, NotebookLM_Workspaces/**/*.md
- Files matching these patterns are excluded: **/raw/**, NotebookLM_Workspaces/MegaBundle_*.md, NotebookLM_Workspaces/*_context.md
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
NotebookLM_Workspaces/
  01_Research_Methods_and_Decision_System/
    Policy_Pack/
      expandable_workstation_scoring_policy_pack/
        HOW_TO_MAINTAIN_RUBRIC.md
        policy_expandable_workstation_scoring.md
        prompt_notebooklm_executor.md
        prompt_synergy_config_advisor.md
        README.md
        rubric_component_synergy_matrix.md
        template_product_card_output.md
    17_system_ram_gb_or_unified_memory_gb.md
    chatgpt_agent_research_prompt.md
    data_ready_checklist_2026-05-04.md
    laptop_data_audit_2026-05-03.md
    notebook_manifest.md
    tagging_taxonomy.md
    track2_pathway_a_build_spec.md
    track2_pathway_b_audit_2026-05-04.md
    vram_agent_spec.md
    vram_architecture_spec_v1.md
    vram_orchestrator_notes.md
    vram_spec_patch_suggestions.md
    vram_spec_validation_report.md
  02_Refurbished_Desktop_Towers/
    10_lenovo-thinkstation-p620-refurb.md
    18_recompute-dell-precision-5820-tower-act-thinkpad-t14s-pairing.md
    28_hp-z4-g4-rtx-3090-refurbished.md
    intake-003_dell-precision-5820-tower-bundle.md
    intake-004_hp-z4-g4-workstation-refurbished-base.md
    intake-005_dell-precision-t7910-refurbished-base.md
    intake-006_alienware-aurora-r12-refurbished.md
    intake-023_gaming-pc-jonsbo-mod-5-asrock-x570-aqua.md
    intake-034_lenovo-thinkstation-p330-tiny-desktop.md
    intake-035_specialized-evga-3090-custom-build.md
    intake-040_recompute-dell-precision-5820-tower-act-thinkpad.md
    intake-041_act-dell-3650-a4000.md
    intake-042_hp-z4-g4-used-3090.md
    intake-046_acer-predator-orion-7000-rtx-4080-refurbished.md
    intake-047_alienware-aurora-r12-rtx-3090-refurbished.md
    intake-050_ple-sidekick-rtx-4070-super-ex-demo.md
    intake-065_dell-optiplex-5060-sff.md
    intake-066_dell-precision-5820-tower-workstation-32gb-ram.md
  03_New_Desktop_Systems/
    01_lenovo-thinkstation-basic.md
    12_supertech-rtx-4090-gaming-pc.md
    25_ple-ai-advanced-rtx-5070-ti.md
    27_scorptec-eclipse-rtx-5070-ti.md
    intake-001_dual-rtx-3090-24gb-gpu-pro-workstation-pure-501-black.md
    intake-002_supertech-computers-rtx-4090-gaming-pc.md
    intake-007_ple-ai-advanced-rtx-5070-ti-desktop.md
    intake-008_evatech-y40k-rtx-4080-super-gaming-pc.md
    intake-016_okinos-studio-pro-rtx-5070-ti3090.md
    intake-022_gaming-pc-intel-i9-12th-gen-nvidia-rtx-3090.md
    intake-023_gaming-pc-jonsbo-mod-5-asrock-x570-aqua.md
    intake-024_skytech-prism-4-gaming-pc.md
    intake-025_hp-omen-45l-gt22-3090-gaming-pc.md
    intake-026_clx-horus-gaming-desktop.md
    intake-028_dual-rtx-4090-24gb-gpu-pro-workstation.md
    intake-029_dual-rtx-5090-32gb-gpu-pro-workstation.md
    intake-032_topaz-snow-pc.md
    intake-033_vision-onyx-pc.md
    intake-035_specialized-evga-3090-custom-build.md
    intake-037_thermaltake-horizon-xtreme-tower-x1-carbon.md
    intake-043_ple-pixel-5070-ti.md
    intake-044_scorptec-eclipse-rtx-5070-ti-gaming-pc.md
    intake-048_metrocom-custom-5700x-rtx-4070-super.md
    intake-049_nebula-pc-titan-ryzen-7-7800x3d-rtx-5070.md
    intake-050_ple-sidekick-rtx-4070-super-ex-demo.md
    intake-054_constellar-onyx-pc-rtx-4080-super.md
    intake-055_scorptec-32-core-compute-platform.md
    intake-056_scorptec-blackwell-pro-workstation.md
    intake-059_hp-z8-fury-g5-workstation.md
    intake-062_allied-moab-a-rtx-5090-32gb-gaming-pc.md
    intake-063_scorptec-vengeance-rtx-5090-gaming-pc.md
    intake-064_aether-lvl-10-ice-max-rtx-5090-desktop-pc.md
  04_Laptops_Mainline/
    21_lenovo-legion-pro-7i-rtx-4090.md
    22_asus-rog-strix-scar-17-rtx-4090.md
    23_asus-rog-strix-scar-18-rtx-4090.md
    24_msi-stealth-16-ai-studio-rtx-4090.md
    30_asus-rog-strix-scar-18-rtx-5090-2025.md
    31_lenovo-legion-9i-18-rtx-5090.md
    32_msi-raider-a18-hx-rtx-5090.md
    33_msi-titan-rtx-5090.md
    34_asus-tuf-gaming-a16-strix-halo.md
    35_asus-rog-zephyrus-g16-strix-halo.md
    36_lenovo-legion-9i-18-rtx-5080-ebay.md
    37_lenovo-legion-9i-gen10-direct.md
    39_msi-raider-a18-hx-refurb.md
    40_msi-katana-17-hx.md
    41_asus-rog-strix-g18-rtx-5070ti-2025.md
    42_asus-rog-strix-g16-rtx-5080-2025.md
    43_asus-rog-zephyrus-g16-rtx-5070-2025.md
    44_asus-rog-strix-g16-rtx-5070ti-2025.md
    45_asus-rog-zephyrus-g16-intel-rtx-5070ti-2025.md
    46_asus-rog-zephyrus-g16-intel-rtx-5090-2025.md
    47_asus-rog-strix-g18-2024-rtx4080.md
    48_asus-rog-zephyrus-g16-2024-rtx4080.md
    asus-proart-px13.md
    asus-rog-flow-z13.md
    asus-tuf-a14.md
    asus-zenbook-duo-ux8406.md
    hp-zbook-ultra-14-g1a.md
    intake-009_lenovo-legion-pro-7i.md
    intake-010_msi-raider-18-hx-ai-a2xwjg.md
    intake-011_dell-alienware-m18-r2-area-51.md
    intake-012_razer-blade-18.md
    intake-013_msi-crosshair-18-hx-ai.md
    intake-014_lenovo-thinkpad-t14-t14s-refurbished.md
    intake-015_dell-latitude-7330-2-in-1-refurbished.md
    intake-036_alienware-16-area-51-new-config.md
    intake-045_msi-stealth-a16-5080.md
    intake-051_acer-predator-helios-18-rtx-4090-refurbished.md
    intake-052_acer-predator-helios-neo-16s-ai-rtx-5060.md
    intake-053_erazer-major-x20-rtx-4070.md
    intake-072_hp-zbook-ultra-14-g1a.md
  05_Apple_Silicon_Systems/
    01_apple-mac-studio-m4-max-64gb.md
    02_mac-studio-m4-max-64gb1tb-education-config.md
    03_mac-studio-m4-max-64gb-unified-memory-1tb-ssd.md
    04_refurb-mac-studio-m2-ultra-64gb.md
    05_apple-macbook-pro-14-m4-pro-48gb.md
    06_apple-macbook-pro-16-m3-max-48gb-open-box.md
    07_refurbished-macbook-pro-16-inch-m4-max-48gb1tb.md
    08_apple-mac-studio-m4-max-36gb.md
  06_Mini_PCs_and_eGPU/
    16_minisforum-ms-01-deg1-oculink-rtx-3090-24gb.md
    40_minisforum-ai-x1-pro-strix-halo.md
    hp_mini_pc_placeholder.md
    hp-z2-mini-g1a-strix-halo.md
    intake-038_minisforum-ai-x1-pro-deg2-rtx-5070-ti.md
    intake-039_minisforum-x1-lite-deg1-rtx-5070-ti.md
    intake-071_gpd-win-5.md
  08_Custom_Builds/
    10_custom-rtx-3090-24gb-desktop-refurbished-thinkpad-bundle.md
    13_refurb-3090-tower-thin-client.md
    intake-017_budget-build.md
    intake-018_mid-range-build.md
    intake-019_pro-build.md
  09_Individual_Components/
    11_mike-pc-msi-rtx-3090-aero-24gb-gpu-build-route.md
    14_msi-rtx-3090-aero-24gb-standalone-gpu.md
    intake-020_asus-rog-strix-geforce-rtx-3090-oc-24gb-gddr6x.md
    intake-021_nvidia-geforce-rtx-3090-24gb-2slot-turbo-blower.md
    intake-027_gigabyte-radeon-rx-9070-xt-gaming-oc-ice-16g.md
    intake-030_gigabyte-aorus-geforce-rtx-5090-master-ice-32g.md
    intake-031_zotac-gaming-geforce-rtx-5090-solid-oc.md
    intake-057_asrock-radeon-rx-7900-xtx-phantom-gaming-24gb-oc.md
    intake-058_nvidia-rtx-pro-6000.md
    intake-060_nvidia-rtx-6000-96gb-gddr7-professional-video-card.md
    intake-061_amd-radeon-pro-w7900-48gb-ecc-gddr6.md
    intake-067_evga-ftw3-ultra-rtx-3090.md
    intake-068_intel-arc-pro-b70.md
    intake-069_nvidia-rtx-5000-ada-32gb.md
    intake-070_nvidia-rtx-2000-ada-16gb.md
  Desktop_Gaming_Refurbished/
    09_alienware-aurora-r12-rtx-3090-refurbished.md
    10_alienware-aurora-r11-rtx-3090-refurbished.md
  Gaming_Laptops_AMD_Discrete/
    hp_omen_max.md
  intake/
    shortlist/
      2026-05-06_shortlist_rejected.csv
      2026-05-06_shortlist.csv
      test_shortlist_scored.csv
      test_shortlist.csv
  Research_and_Sources/
    15_normal-laptop-remote-gpu-rental.md
    20_used-enterprise-workstation-or-data-center-gpu-path.md
  final_justification_TEST.md
  scoring_context_TEST.md
  workspace_redesign_proposal.md
```

# Files

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-023_gaming-pc-jonsbo-mod-5-asrock-x570-aqua.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: gaming-pc-jonsbo-mod-5-asrock-x570-aqua
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Gaming PC Jonsbo MOD 5 ASRock x570 Aqua
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $3898.30 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Gaming PC Jonsbo MOD 5 ASRock x570 Aqua

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3898.30 AUD
- **Retailer:** ale_deconno
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 9 5950X
- **RAM:** 128 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
eBay custom build

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-035_specialized-evga-3090-custom-build.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: specialized-evga-3090-custom-build
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Specialized EVGA 3090 Custom Build
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $2953 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Specialized EVGA 3090 Custom Build

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2953 AUD
- **Retailer:** Tech Junction
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core i9-12900K
- **RAM:** 16 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Custom built using EVGA 3090

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-050_ple-sidekick-rtx-4070-super-ex-demo.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-8GB #OpenBox #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: ple-sidekick-rtx-4070-super-ex-demo
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: PLE Sidekick RTX 4070 Super EX-DEMO
gpu: RTX 4070 Super
vram: 12 GB
unified_memory: UNKNOWN
price_aud: $3079 AUD
condition: Open Box
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# PLE Sidekick RTX 4070 Super EX-DEMO

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3079 AUD
- **Retailer:** PLE Computers
- **URL:** [https://www.ple.com.au/products/684114/ex-demo-ple-sidekick-rtx-4070-super-prebuilt-ready-to-go-gaming-pc-co-demo](https://www.ple.com.au/products/684114/ex-demo-ple-sidekick-rtx-4070-super-prebuilt-ready-to-go-gaming-pc-co-demo)
- **Condition:** Open Box
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4070 Super
- **VRAM:** 12 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core i5-14400
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Low stock

## AI Capability Summary
Baseline — 8 GB VRAM sufficient for 7B Q4; larger models require significant offload.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/intake/shortlist/2026-05-06_shortlist_rejected.csv
`````
intake_id,item_name,profile,category,Category_Group,track,pathway,gpu_model,vram_gb,unified_memory_gb,price_aud,Over_Budget,Price_Unknown,condition,retailer,verification_status,au_stock,status,batch,source_file,exceptional_override,shortlist_reason,soft_penalty_notes,rejection_reason
intake-059,HP Z8 FURY G5 Workstation,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 6000 Ada,48.0,UNKNOWN,44205.95,,,New,UNKNOWN,Unverified,UNKNOWN,Out of Stock,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-059_hp-z8-fury-g5-workstation.md,,,,Out of Stock
intake-058,NVIDIA RTX PRO 6000,Component,component,Workstation_GPU,UNKNOWN,UNKNOWN,RTX PRO 6000,96.0,UNKNOWN,15999.0,,,New,UNKNOWN,Unverified,UNKNOWN,Out of Stock,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-058_nvidia-rtx-pro-6000.md,,,,Out of Stock
intake-060,NVIDIA RTX 6000 96GB GDDR7 Professional Video Card,Component,component,Workstation_GPU,UNKNOWN,UNKNOWN,RTX 6000,96.0,UNKNOWN,15499.0,,,New,UNKNOWN,Unverified,UNKNOWN,Out of Stock,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-060_nvidia-rtx-6000-96gb-gddr7-professional-video-card.md,,,,Out of Stock
`````

## File: NotebookLM_Workspaces/intake/shortlist/2026-05-06_shortlist.csv
`````
intake_id,item_name,profile,category,Category_Group,track,pathway,gpu_model,vram_gb,unified_memory_gb,price_aud,Over_Budget,Price_Unknown,condition,retailer,verification_status,au_stock,status,batch,source_file,exceptional_override,shortlist_reason,soft_penalty_notes,Machine,Type,VRAM_Adequacy,GPU_Compute_Tier,Value_Score,Price_to_Perf,Condition_Risk,Verification_Confidence,Sustained_TGP_Rating,Portability_Score
intake-034,Lenovo ThinkStation P330 Tiny Desktop,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,469.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-034_lenovo-thinkstation-p330-tiny-desktop.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-034,Candidate,,,,,,,,
intake-065,Dell OptiPlex 5060 SFF,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,238.99,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-065_dell-optiplex-5060-sff.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-065,Candidate,,,,,,,,
intake-050,PLE Sidekick RTX 4070 Super EX-DEMO,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 4070 Super,12.0,UNKNOWN,3079.0,No,,Open Box,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-050_ple-sidekick-rtx-4070-super-ex-demo.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-050,Candidate,,,,,,,,
intake-048,Metrocom Custom 5700X RTX 4070 Super,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 4070 Super,12.0,UNKNOWN,2350.0,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-048_metrocom-custom-5700x-rtx-4070-super.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-048,Candidate,,,,,,,,
intake-049,Nebula PC Titan Ryzen 7 7800X3D RTX 5070,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5070,12.0,UNKNOWN,2238.0,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-049_nebula-pc-titan-ryzen-7-7800x3d-rtx-5070.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-049,Candidate,,,,,,,,
intake-050,PLE Sidekick RTX 4070 Super EX-DEMO,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 4070 Super,12.0,UNKNOWN,3079.0,No,,UNKNOWN,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-050_ple-sidekick-rtx-4070-super-ex-demo.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-050,Candidate,,,,,,,,
intake-018,Mid-range build,Desktop,diy build,Complete_System,UNKNOWN,UNKNOWN,RTX 4070 Super,12.0,UNKNOWN,1599.0,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/08_Custom_Builds/intake-018_mid-range-build.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-018,Candidate,,,,,,,,
intake-041,ACT Dell 3650 + A4000,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX A4000,16.0,UNKNOWN,1800.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-041_act-dell-3650-a4000.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-041,Candidate,,,,,,,,
intake-046,Acer Predator Orion 7000 RTX 4080 refurbished,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 4080,16.0,UNKNOWN,3699.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-046_acer-predator-orion-7000-rtx-4080-refurbished.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-046,Candidate,,,,,,,,
intake-007,PLE AI Advanced RTX 5070 Ti Desktop,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5070 Ti,16.0,UNKNOWN,3907.0,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-007_ple-ai-advanced-rtx-5070-ti-desktop.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-007,Candidate,,,,,,,,
intake-008,Evatech Y40K RTX 4080 Super Gaming PC,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 4080 Super,16.0,UNKNOWN,UNKNOWN,No,Yes,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-008_evatech-y40k-rtx-4080-super-gaming-pc.md,,Passed gates,Price UNKNOWN — research required; Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-008,Candidate,,,,,,,,
intake-016,OKINOS Studio Pro - RTX 5070 Ti/3090,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5070 Ti,16.0,UNKNOWN,3599.0,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-016_okinos-studio-pro-rtx-5070-ti3090.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-016,Candidate,,,,,,,,
intake-032,TOPAZ SNOW PC,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5070 Ti,16.0,UNKNOWN,2699.0,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-032_topaz-snow-pc.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-032,Candidate,,,,,,,,
intake-033,VISION ONYX PC,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5080,16.0,UNKNOWN,3999.0,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-033_vision-onyx-pc.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-033,Candidate,,,,,,,,
intake-037,Thermaltake Horizon Xtreme tower + X1 Carbon,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 4080 Super,16.0,UNKNOWN,4543.0,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-037_thermaltake-horizon-xtreme-tower-x1-carbon.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $4,543.00); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-037,Candidate,,,,,,,,
intake-043,PLE Pixel 5070 Ti,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5070 Ti,16.0,UNKNOWN,3799.0,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-043_ple-pixel-5070-ti.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-043,Candidate,,,,,,,,
intake-044,Scorptec Eclipse RTX 5070 Ti Gaming PC,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5070 Ti,16.0,UNKNOWN,3399.0,No,,New,UNKNOWN,Verified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-044_scorptec-eclipse-rtx-5070-ti-gaming-pc.md,,Passed gates,AU stock: UNKNOWN,intake-044,Candidate,,,,,,,,
intake-054,CONSTELLAR ONYX PC — RTX 4080 SUPER,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 4080 Super,16.0,UNKNOWN,4099.0,No,,UNKNOWN,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-054_constellar-onyx-pc-rtx-4080-super.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-054,Candidate,,,,,,,,
intake-055,Scorptec 32-Core Compute Platform,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX PRO 4000,16.0,UNKNOWN,UNKNOWN,No,Yes,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-055_scorptec-32-core-compute-platform.md,,Passed gates,Price UNKNOWN — research required; Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-055,Candidate,,,,,,,,
intake-017,Budget build,Desktop,diy build,Complete_System,UNKNOWN,UNKNOWN,RTX 4060 Ti,16.0,UNKNOWN,899.0,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/08_Custom_Builds/intake-017_budget-build.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-017,Candidate,,,,,,,,
intake-003,Dell Precision 5820 Tower Bundle,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,3558.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-003_dell-precision-5820-tower-bundle.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-003,Candidate,,,,,,,,
intake-004,HP Z4 G4 Workstation (Refurbished Base),Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,3500.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-004_hp-z4-g4-workstation-refurbished-base.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-004,Candidate,,,,,,,,
intake-005,Dell Precision T7910 (Refurbished Base),Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,1875.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-005_dell-precision-t7910-refurbished-base.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-005,Candidate,,,,,,,,
intake-006,Alienware Aurora R12 (Refurbished),Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,3884.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-006_alienware-aurora-r12-refurbished.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-006,Candidate,,,,,,,,
intake-023,Gaming PC Jonsbo MOD 5 ASRock x570 Aqua,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,3898.3,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-023_gaming-pc-jonsbo-mod-5-asrock-x570-aqua.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-023,Candidate,,,,,,,,
intake-035,Specialized EVGA 3090 Custom Build,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,2953.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-035_specialized-evga-3090-custom-build.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-035,Candidate,,,,,,,,
intake-040,Recompute Dell Precision 5820 Tower + ACT ThinkPad,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,3558.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-040_recompute-dell-precision-5820-tower-act-thinkpad.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-040,Candidate,,,,,,,,
intake-042,HP Z4 G4 + used 3090,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,2800.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-042_hp-z4-g4-used-3090.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-042,Candidate,,,,,,,,
intake-047,Alienware Aurora R12 RTX 3090 refurbished,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,3884.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-047_alienware-aurora-r12-rtx-3090-refurbished.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-047,Candidate,,,,,,,,
intake-066,Dell Precision 5820 Tower Workstation (32GB RAM),Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,2399.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-066_dell-precision-5820-tower-workstation-32gb-ram.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-066,Candidate,,,,,,,,
intake-002,Supertech Computers RTX 4090 Gaming PC,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 4090,24.0,UNKNOWN,5799.0,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-002_supertech-computers-rtx-4090-gaming-pc.md,≥ 24.0GB VRAM allows budget stretch to $6000.0,Passed via exceptional override,"Exceeds $4,500 AUD budget (price: $5,799.00) [ALLOWED: ≥ 24.0GB VRAM allows budget stretch to $6000.0]; Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-002,Candidate,,,,,,,,
intake-022,Gaming PC Intel i9-12th Gen NVIDIA RTX 3090,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,5271.98,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-022_gaming-pc-intel-i9-12th-gen-nvidia-rtx-3090.md,≥ 24.0GB VRAM allows budget stretch to $6000.0,Passed via exceptional override,"Exceeds $4,500 AUD budget (price: $5,271.98) [ALLOWED: ≥ 24.0GB VRAM allows budget stretch to $6000.0]; Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-022,Candidate,,,,,,,,
intake-023,Gaming PC Jonsbo MOD 5 ASRock x570 Aqua,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,3898.3,No,,UNKNOWN,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-023_gaming-pc-jonsbo-mod-5-asrock-x570-aqua.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-023,Candidate,,,,,,,,
intake-035,Specialized EVGA 3090 Custom Build,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,2953.0,No,,UNKNOWN,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-035_specialized-evga-3090-custom-build.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-035,Candidate,,,,,,,,
intake-019,Pro build,Desktop,diy build,Complete_System,UNKNOWN,UNKNOWN,RTX 4090,24.0,UNKNOWN,2899.0,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/08_Custom_Builds/intake-019_pro-build.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-019,Candidate,,,,,,,,
intake-024,Skytech Prism 4 Gaming PC,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090,32.0,UNKNOWN,6599.98,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-024_skytech-prism-4-gaming-pc.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $6,599.98); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-024,Candidate,,,,,,,,
intake-025,HP OMEN 45L GT22-3090 Gaming PC,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090,32.0,UNKNOWN,7499.98,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-025_hp-omen-45l-gt22-3090-gaming-pc.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $7,499.98); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-025,Candidate,,,,,,,,
intake-026,CLX Horus Gaming Desktop,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090,32.0,UNKNOWN,9899.98,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-026_clx-horus-gaming-desktop.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $9,899.98); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-026,Candidate,,,,,,,,
intake-062,Allied M.O.A.B-A: RTX 5090 32GB Gaming PC,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090,32.0,UNKNOWN,UNKNOWN,No,Yes,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-062_allied-moab-a-rtx-5090-32gb-gaming-pc.md,,Passed gates,Price UNKNOWN — research required; Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-062,Candidate,,,,,,,,
intake-063,Scorptec Vengeance RTX 5090 Gaming PC,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090,32.0,UNKNOWN,UNKNOWN,No,Yes,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-063_scorptec-vengeance-rtx-5090-gaming-pc.md,,Passed gates,Price UNKNOWN — research required; Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-063,Candidate,,,,,,,,
intake-064,AETHER : LVL 10 ICE MAX RTX 5090 Desktop PC,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090,32.0,UNKNOWN,UNKNOWN,No,Yes,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-064_aether-lvl-10-ice-max-rtx-5090-desktop-pc.md,,Passed gates,Price UNKNOWN — research required; Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-064,Candidate,,,,,,,,
intake-001,Dual RTX 3090 24GB GPU Pro Workstation (Pure 501 Black),Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 3090,48.0,UNKNOWN,5998.5,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-001_dual-rtx-3090-24gb-gpu-pro-workstation-pure-501-black.md,≥ 24.0GB VRAM allows budget stretch to $6000.0,Passed via exceptional override,"Exceeds $4,500 AUD budget (price: $5,998.50) [ALLOWED: ≥ 24.0GB VRAM allows budget stretch to $6000.0]; Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-001,Candidate,,,,,,,,
intake-028,Dual RTX 4090 24GB GPU Pro Workstation,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 4090,48.0,UNKNOWN,11998.5,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-028_dual-rtx-4090-24gb-gpu-pro-workstation.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $11,998.50); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-028,Candidate,,,,,,,,
intake-056,Scorptec Blackwell PRO Workstation,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX PRO 5000 Blackwell,48.0,UNKNOWN,UNKNOWN,No,Yes,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-056_scorptec-blackwell-pro-workstation.md,,Passed gates,Price UNKNOWN — research required; Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-056,Candidate,,,,,,,,
intake-029,Dual RTX 5090 32GB GPU Pro Workstation,Desktop,desktop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090,64.0,UNKNOWN,14998.5,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/03_New_Desktop_Systems/intake-029_dual-rtx-5090-32gb-gpu-pro-workstation.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $14,998.50); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-029,Candidate,,,,,,,,
intake-014,Lenovo ThinkPad T14 / T14s (Refurbished),Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,800.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-014_lenovo-thinkpad-t14-t14s-refurbished.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-014,Candidate,,,,,,,,
intake-015,Dell Latitude 7330 2-in-1 (Refurbished),Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,UNKNOWN,1254.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-015_dell-latitude-7330-2-in-1-refurbished.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-015,Candidate,,,,,,,,
intake-072,HP ZBook Ultra 14 G1a,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,Radeon 8060S,UNKNOWN,UNKNOWN,UNKNOWN,No,Yes,New,UNKNOWN,Needs Verification,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-072_hp-zbook-ultra-14-g1a.md,,Passed gates,Price UNKNOWN — research required; AU stock: UNKNOWN,intake-072,Candidate,,,,,,,,
intake-009,Lenovo Legion Pro 7i,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 4090 Mobile,16.0,UNKNOWN,4575.0,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-009_lenovo-legion-pro-7i.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $4,575.00); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-009,Candidate,,,,,,,,
intake-013,MSI Crosshair 18 HX AI,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5070 Mobile,16.0,UNKNOWN,UNKNOWN,No,Yes,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-013_msi-crosshair-18-hx-ai.md,,Passed gates,Price UNKNOWN — research required; Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-013,Candidate,,,,,,,,
intake-036,Alienware 16 Area-51 new config,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5070 Ti Mobile,16.0,UNKNOWN,4198.7,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-036_alienware-16-area-51-new-config.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-036,Candidate,,,,,,,,
intake-045,MSI Stealth A16 5080,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5080 Mobile,16.0,UNKNOWN,4999.0,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-045_msi-stealth-a16-5080.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $4,999.00); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-045,Candidate,,,,,,,,
intake-051,Acer Predator Helios 18 RTX 4090 refurbished,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 4090 Mobile,16.0,UNKNOWN,4449.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-051_acer-predator-helios-18-rtx-4090-refurbished.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-051,Candidate,,,,,,,,
intake-010,MSI Raider 18 HX AI A2XWJG,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090 Mobile,24.0,UNKNOWN,8488.0,Yes,,New,UNKNOWN,Verified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-010_msi-raider-18-hx-ai-a2xwjg.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $8,488.00); AU stock: UNKNOWN",intake-010,Candidate,,,,,,,,
intake-011,Dell Alienware m18 R2 / Area-51,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090 Mobile,24.0,UNKNOWN,4499.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-011_dell-alienware-m18-r2-area-51.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-011,Candidate,,,,,,,,
intake-012,Razer Blade 18,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090 Mobile,24.0,UNKNOWN,7400.0,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-012_razer-blade-18.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $7,400.00); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-012,Candidate,,,,,,,,
intake-052,Acer Predator Helios Neo 16S AI RTX 5060,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5060,8.0,UNKNOWN,2399.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-052_acer-predator-helios-neo-16s-ai-rtx-5060.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-052,Candidate,,,,,,,,
intake-053,ERAZER Major X20 RTX 4070,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 4070,8.0,UNKNOWN,2999.0,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-053_erazer-major-x20-rtx-4070.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-053,Candidate,,,,,,,,
intake-071,GPD WIN 5,Mini PC,mini pc,Complete_System,UNKNOWN,UNKNOWN,Radeon 8060S,UNKNOWN,UNKNOWN,UNKNOWN,No,Yes,New,UNKNOWN,Needs Verification,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/intake-071_gpd-win-5.md,,Passed gates,Price UNKNOWN — research required; AU stock: UNKNOWN,intake-071,Candidate,,,,,,,,
intake-038,Minisforum AI X1 Pro + DEG2 + RTX 5070 Ti,Mini PC,mini pc,Complete_System,UNKNOWN,UNKNOWN,RTX 5070 Ti,16.0,UNKNOWN,3633.19,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/intake-038_minisforum-ai-x1-pro-deg2-rtx-5070-ti.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-038,Candidate,,,,,,,,
intake-039,Minisforum X1 Lite + DEG1 + RTX 5070 Ti,Mini PC,mini pc,Complete_System,UNKNOWN,UNKNOWN,RTX 5070 Ti,16.0,UNKNOWN,2851.98,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/intake-039_minisforum-x1-lite-deg1-rtx-5070-ti.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-039,Candidate,,,,,,,,
intake-027,Gigabyte Radeon RX 9070 XT Gaming OC Ice 16G,Component,component,Standalone_GPU,UNKNOWN,UNKNOWN,RX 9070 XT,16.0,UNKNOWN,1235.4,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-027_gigabyte-radeon-rx-9070-xt-gaming-oc-ice-16g.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-027,Candidate,,,,,,,,
intake-020,ASUS ROG Strix GeForce RTX 3090 OC 24GB GDDR6X,Component,component,Standalone_GPU,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,1591.98,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-020_asus-rog-strix-geforce-rtx-3090-oc-24gb-gddr6x.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-020,Candidate,,,,,,,,
intake-021,NVIDIA GeForce RTX 3090 24GB 2SLOT Turbo Blower,Component,component,Standalone_GPU,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,1739.49,No,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-021_nvidia-geforce-rtx-3090-24gb-2slot-turbo-blower.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-021,Candidate,,,,,,,,
intake-057,ASRock Radeon RX 7900 XTX Phantom Gaming 24GB OC,Component,component,Standalone_GPU,UNKNOWN,UNKNOWN,RX 7900 XTX,24.0,UNKNOWN,1229.0,No,,New,UNKNOWN,Verified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-057_asrock-radeon-rx-7900-xtx-phantom-gaming-24gb-oc.md,,Passed gates,AU stock: UNKNOWN,intake-057,Candidate,,,,,,,,
intake-067,EVGA FTW3 Ultra RTX 3090,Component,component,Standalone_GPU,UNKNOWN,UNKNOWN,RTX 3090,24.0,UNKNOWN,1318.0,No,,Refurbished,UNKNOWN,Needs Verification,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-067_evga-ftw3-ultra-rtx-3090.md,,Passed gates,AU stock: UNKNOWN,intake-067,Candidate,,,,,,,,
intake-030,GIGABYTE AORUS GeForce RTX 5090 Master Ice 32G,Component,component,Standalone_GPU,UNKNOWN,UNKNOWN,RTX 5090,32.0,UNKNOWN,6499.0,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-030_gigabyte-aorus-geforce-rtx-5090-master-ice-32g.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $6,499.00); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-030,Candidate,,,,,,,,
intake-031,ZOTAC Gaming GeForce RTX 5090 Solid OC,Component,component,Standalone_GPU,UNKNOWN,UNKNOWN,RTX 5090,32.0,UNKNOWN,6569.95,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-031_zotac-gaming-geforce-rtx-5090-solid-oc.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $6,569.95); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-031,Candidate,,,,,,,,
intake-070,NVIDIA RTX 2000 Ada 16GB,Component,component,Workstation_GPU,UNKNOWN,UNKNOWN,RTX 2000 Ada,16.0,UNKNOWN,1233.0,No,,New,UNKNOWN,Verified,Yes,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-070_nvidia-rtx-2000-ada-16gb.md,,Passed gates,,intake-070,Candidate,,,,,,,,
intake-068,Intel Arc Pro B70,Component,component,Workstation_GPU,UNKNOWN,UNKNOWN,Arc Pro B70,32.0,UNKNOWN,1423.0,No,,New,UNKNOWN,Needs Verification,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-068_intel-arc-pro-b70.md,,Passed gates,AU stock: UNKNOWN,intake-068,Candidate,,,,,,,,
intake-069,NVIDIA RTX 5000 Ada 32GB,Component,component,Workstation_GPU,UNKNOWN,UNKNOWN,RTX 5000 Ada,32.0,UNKNOWN,6368.0,Yes,,New,UNKNOWN,Verified,Yes,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-069_nvidia-rtx-5000-ada-32gb.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $6,368.00)",intake-069,Candidate,,,,,,,,
intake-061,AMD Radeon Pro W7900 48GB ECC GDDR6,Component,component,Workstation_GPU,UNKNOWN,UNKNOWN,Radeon Pro W7900,48.0,UNKNOWN,UNKNOWN,No,Yes,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/09_Individual_Components/intake-061_amd-radeon-pro-w7900-48gb-ecc-gddr6.md,,Passed gates,Price UNKNOWN — research required; Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-061,Candidate,,,,,,,,
`````

## File: NotebookLM_Workspaces/intake/shortlist/test_shortlist_scored.csv
`````
Machine,Type,VRAM_Adequacy,GPU_Compute_Tier,Value_Score,Price_to_Perf,Condition_Risk,Verification_Confidence,Sustained_TGP_Rating,Portability_Score
intake-009,Candidate,5,8,4,4,10,2,0,0
intake-010,Candidate,8,10,2,3,10,8,0,0
intake-011,Candidate,8,10,9,9,6,2,0,0
intake-052,Candidate,2,4,7,6,6,2,0,0
`````

## File: NotebookLM_Workspaces/intake/shortlist/test_shortlist.csv
`````
intake_id,item_name,profile,category,Category_Group,track,pathway,gpu_model,vram_gb,unified_memory_gb,price_aud,Over_Budget,Price_Unknown,condition,retailer,verification_status,au_stock,status,batch,source_file,exceptional_override,shortlist_reason,soft_penalty_notes,Machine,Type,VRAM_Adequacy,GPU_Compute_Tier,Value_Score,Price_to_Perf,Condition_Risk,Verification_Confidence,Sustained_TGP_Rating,Portability_Score
intake-009,Lenovo Legion Pro 7i,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 4090 Mobile,16.0,UNKNOWN,4575.0,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-009_lenovo-legion-pro-7i.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $4,575.00); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-009,Candidate,,,,,,,,
intake-010,MSI Raider 18 HX AI A2XWJG,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090 Mobile,24.0,UNKNOWN,8488.0,Yes,,New,UNKNOWN,Verified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-010_msi-raider-18-hx-ai-a2xwjg.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $8,488.00); AU stock: UNKNOWN",intake-010,Candidate,,,,,,,,
intake-011,Dell Alienware m18 R2 / Area-51,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090 Mobile,24.0,UNKNOWN,4499.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-011_dell-alienware-m18-r2-area-51.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-011,Candidate,,,,,,,,
intake-052,Acer Predator Helios Neo 16S AI RTX 5060,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5060,8.0,UNKNOWN,2399.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-052_acer-predator-helios-neo-16s-ai-rtx-5060.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-052,Candidate,,,,,,,,
`````

## File: NotebookLM_Workspaces/final_justification_TEST.md
`````markdown
# Purchase Justification Ledger (Dry Run)

## 1. Winner Overview (Table)

| Metric | Value |
|---|---|
| **Model / Identifier** | Dell Alienware m18 R2 / Area-51 (intake-011) |
| **Track / Pathway** | Track 1, Pathway 1A |
| **vram_gb** | 24.0 GB |
| **price_aud** | $4,499.00 AUD |
| **Value_Score** | 9 |
| **Price_to_Perf** | 9 |
| **Condition_Risk** | 6 (Refurbished) |
| **Verification_Confidence** | 2 (Unverified) |
| **Sustained_TGP_Rating** | UNKNOWN (0) |
| **Portability_Score** | UNKNOWN (0) |
| **Final Score** | 50.9 / 100 |

*Note: The sustained TGP and portability scores were UNKNOWN at the time of scoring.*

## 2. Policy Alignment

* **VRAM Adequacy:** At 24GB of VRAM (RTX 5090 Mobile), this machine comfortably exceeds the 16GB ideal tier for Track 1A, allowing it to handle 30B–34B Q4 models natively.
* **Budget & Value:** The price of $4,499 AUD falls just inside the strict $4,500 AUD budget cap defined in `AGENTS.md`. Its Value_Score and Price_to_Perf are very strong (9/10), making it an exceptional deal for 24GB VRAM.
* **Track Suitability:** It perfectly fits the Path 1A parameters (NVIDIA Discrete GPU Laptop with large screen and high VRAM), offering desktop-replacement levels of performance.

## 3. Residual Risks & Required Checks

* [ ] **Unmet Good-Enough Threshold:** The engine scored this machine at 50.9/100, which falls below the 70.0/100 threshold required to automatically stop searching.
* [ ] **Verification Confidence:** The verification score is extremely low (2/10). You must confirm AU stock from the named retailer (Dell Outlet / Best Buy) and acquire the specific URL.
* [ ] **Condition Risk:** As a refurbished unit (score 6/10), the warranty term and type (AU) must be manually verified to ensure it meets minimum ACL or seller warranty guidelines.
* [ ] **Missing Specs:** Storage (installed and free M.2 slots), PSU wattage, and Unified Memory are currently UNKNOWN.
* [ ] **Thermal Reputation:** Check reviews to confirm thermal performance and sustained TGP rating.

## 4. Considered Alternatives

* **MSI Raider 18 HX AI A2XWJG (intake-010) — Score: 47.3**
  * *Strengths:* Also features 24GB VRAM and is a brand new unit with high Verification_Confidence (10/10).
  * *Why it lost:* Severely overpriced at $8,488 AUD, completely destroying its Value_Score (2/10) and violating the hard budget cap.

## 5. Final Recommendation

**Recommendation: DO NOT PROCEED (because while it presents exceptional value on paper, the verification confidence is too low and it has not cleared the GOOD ENOUGH threshold of 70.0).**
`````

## File: NotebookLM_Workspaces/scoring_context_TEST.md
`````markdown
This file is a merged representation of a subset of the codebase, containing specifically included files, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: NotebookLM_Workspaces/intake/shortlist/test_shortlist.csv, NotebookLM_Workspaces/**/intake-011*.md, NotebookLM_Workspaces/**/intake-009*.md, NotebookLM_Workspaces/**/intake-052*.md, NotebookLM_Workspaces/**/intake-010*.md, AGENTS.md, config/*.json, scripts/*.py
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
config/
  procurement_policy.json
NotebookLM_Workspaces/
  04_Laptops_Mainline/
    intake-009_lenovo-legion-pro-7i.md
    intake-010_msi-raider-18-hx-ai-a2xwjg.md
    intake-011_dell-alienware-m18-r2-area-51.md
    intake-052_acer-predator-helios-neo-16s-ai-rtx-5060.md
  intake/
    shortlist/
      test_shortlist.csv
scripts/
  build_shortlist.py
  enrich_shortlist_pricing.py
  intake_to_cards.py
  normalize_intake.py
AGENTS.md
```

# Files

## File: config/procurement_policy.json
````json
{
  "budget_cap_aud": 4500.0,
  "desktop_minimum_vram_gb": 8.0,
  "laptop_discrete_minimum_vram_gb": 8.0,
  "laptop_unified_minimum_vram_gb": 16.0,
  "exceptional_overrides": {
    "vram_threshold_gb": 24.0,
    "gpu_tier_threshold": 8.0,
    "max_override_budget_aud": 6000.0
  },
  "shortlist_behavior": {
    "over_budget_action": "soft_penalty",
    "unknown_price_action": "soft_penalty",
    "out_of_stock_action": "hard_reject",
    "below_vram_floor_action": "hard_reject"
  }
}
````

## File: NotebookLM_Workspaces/intake/shortlist/test_shortlist.csv
````
intake_id,item_name,profile,category,Category_Group,track,pathway,gpu_model,vram_gb,unified_memory_gb,price_aud,Over_Budget,Price_Unknown,condition,retailer,verification_status,au_stock,status,batch,source_file,exceptional_override,shortlist_reason,soft_penalty_notes,Machine,Type,VRAM_Adequacy,GPU_Compute_Tier,Value_Score,Price_to_Perf,Condition_Risk,Verification_Confidence,Sustained_TGP_Rating,Portability_Score
intake-009,Lenovo Legion Pro 7i,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 4090 Mobile,16.0,UNKNOWN,4575.0,Yes,,New,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-009_lenovo-legion-pro-7i.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $4,575.00); Unverified — confirm specs before scoring; AU stock: UNKNOWN",intake-009,Candidate,,,,,,,,
intake-010,MSI Raider 18 HX AI A2XWJG,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090 Mobile,24.0,UNKNOWN,8488.0,Yes,,New,UNKNOWN,Verified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-010_msi-raider-18-hx-ai-a2xwjg.md,,Passed gates,"Exceeds $4,500 AUD budget (price: $8,488.00); AU stock: UNKNOWN",intake-010,Candidate,,,,,,,,
intake-011,Dell Alienware m18 R2 / Area-51,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5090 Mobile,24.0,UNKNOWN,4499.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-011_dell-alienware-m18-r2-area-51.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-011,Candidate,,,,,,,,
intake-052,Acer Predator Helios Neo 16S AI RTX 5060,Laptop,laptop,Complete_System,UNKNOWN,UNKNOWN,RTX 5060,8.0,UNKNOWN,2399.0,No,,Refurbished,UNKNOWN,Unverified,UNKNOWN,Active,2026-05-05_notebooklm_batch1_processed,NotebookLM_Workspaces/04_Laptops_Mainline/intake-052_acer-predator-helios-neo-16s-ai-rtx-5060.md,,Passed gates,Unverified — confirm specs before scoring; AU stock: UNKNOWN,intake-052,Candidate,,,,,,,,
````

## File: scripts/build_shortlist.py
````python
#!/usr/bin/env python3
"""
build_shortlist.py — Phase 2 of the hardware procurement pipeline.

Scans all intake-*.md product cards, applies AGENTS.md hard-gate filters,
and emits two CSVs:

  shortlist.csv  — candidates that passed all gates, with blank score columns
                   ready to be manually filled and fed into rubric_weighting_engine.py
  rejected.csv   — filtered-out rows with the reason for rejection

Usage:
    python scripts/build_shortlist.py
    python scripts/build_shortlist.py --dry-run
    python scripts/build_shortlist.py --batch 2026-05-05_notebooklm_batch1
    python scripts/build_shortlist.py --profile laptop
    python scripts/build_shortlist.py --include-unknowns

Output folder: NotebookLM_Workspaces/intake/shortlist/

After filling in the score columns (0-10), run:
    python scripts/rubric_weighting_engine.py --profile merged \\
        --csv NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist.csv
"""

import argparse
import csv
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPO_ROOT  = Path(__file__).resolve().parent.parent
WORKSPACE  = REPO_ROOT / "NotebookLM_Workspaces"

# Loads config
def load_config() -> dict:
    config_path = REPO_ROOT / "config" / "procurement_policy.json"
    if not config_path.exists():
        sys.exit(f"Error: Config file not found at {config_path}. Please create it.")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Lanes that contain intake cards
INTAKE_LANES = [
    "02_Refurbished_Desktop_Towers",
    "03_New_Desktop_Systems",
    "04_Laptops_Mainline",
    "06_Mini_PCs_and_eGPU",
    "08_Custom_Builds",
    "09_Individual_Components",
    "05_Apple_Silicon_Systems",
    "01_Research_Methods_and_Decision_System",
]

# GPU model substrings that indicate professional/workstation-class cards
WORKSTATION_GPU_KEYWORDS = [
    "RTX PRO", "RTX 6000", "RTX 5000 ADA", "RTX 4000 ADA", "RTX 3000 ADA",
    "RTX 2000 ADA", "A6000", "A5000", "A4500", "A4000", "A2000",
    "QUADRO", "RADEON PRO W", "ARC PRO",
]

# Merged score columns — filled manually after shortlisting
SCORE_COLUMNS = [
    "VRAM_Adequacy",          # 10=48GB+/128GB unified, 8=24GB, 5=16GB, 2=8GB, 0=<8GB
    "GPU_Compute_Tier",       # 10=RTX5090/4090 Pro, 8=RTX3090/4090M/5080, 6=RTX5070Ti/4080
    "Value_Score",            # 10=exceptional price/VRAM ratio, 5=average, 0=poor
    "Price_to_Perf",          # 10=best-in-class overall value, 5=fair, 0=overpriced
    "Condition_Risk",         # 10=New+warranty, 8=OpenBox, 6=Refurb+warranty, 4=Used, 0=Unknown
    "Verification_Confidence",# 10=AU stock+URL confirmed, 5=needs verification, 2=unverified
    "Sustained_TGP_Rating",   # 10=>=175W, 8=150W, 6=120W, 0=N/A (desktop/component)
    "Portability_Score",      # 10=<2kg, 7=2-2.5kg, 4=2.5-3kg, 1=3kg+, 0=N/A (non-mobile)
]


# ---------------------------------------------------------------------------
# Frontmatter parser
# ---------------------------------------------------------------------------

def parse_frontmatter(md_text: str) -> dict:
    """
    Extract YAML frontmatter from a markdown file (between first pair of ---).
    Returns a dict of key: value pairs (all strings).
    """
    match = re.search(r"---\s*\n(.*?)\n---", md_text, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        fm[key.strip()] = val.strip()
    return fm


def parse_tags_comment(md_text: str) -> dict:
    """
    Extract batch name from the INTAKE comment line if present.
    <!-- INTAKE: batch=X date=Y route=Z -->
    """
    match = re.search(r"<!-- INTAKE: batch=(\S+)", md_text)
    return {"batch": match.group(1)} if match else {}


# ---------------------------------------------------------------------------
# Classification helpers
# ---------------------------------------------------------------------------

def classify_profile(category: str) -> str:
    """Map category string to a human-readable profile label."""
    cat = category.lower()
    if "laptop" in cat:
        return "Laptop"
    if "mini pc" in cat or "egpu" in cat:
        return "Mini PC"
    if "component" in cat or "gpu" in cat:
        return "Component"
    if "apple" in cat:
        return "Apple Silicon"
    # desktop / diy build / everything else
    return "Desktop"


def classify_category_group(profile: str, gpu_model: str) -> str:
    """Classify into Complete_System / Standalone_GPU / Workstation_GPU."""
    if profile == "Component":
        gpu_upper = gpu_model.upper()
        if any(kw in gpu_upper for kw in WORKSTATION_GPU_KEYWORDS):
            return "Workstation_GPU"
        return "Standalone_GPU"
    return "Complete_System"


# ---------------------------------------------------------------------------
# Numeric helpers
# ---------------------------------------------------------------------------

def parse_price(price_str: str) -> tuple[float | None, bool]:
    """
    Return (price_float_or_None, is_unknown).
    Strips $, AUD, commas, GB suffixes.
    """
    cleaned = price_str.strip().upper()
    if not cleaned or cleaned in ("UNKNOWN", "N/A", "NONE", "-"):
        return None, True
    cleaned = re.sub(r"[AUD$\s]", "", cleaned).replace(",", "")
    try:
        return float(cleaned), False
    except ValueError:
        return None, True


def parse_vram(vram_str: str) -> float | None:
    """Return numeric VRAM GB or None if unknown."""
    cleaned = re.sub(r"[^0-9.]", "", vram_str.strip())
    try:
        return float(cleaned) if cleaned else None
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Policy Evaluator
# ---------------------------------------------------------------------------

def evaluate_policy(row: dict, config: dict) -> dict:
    """
    Evaluate against config rules (Hard Rejects vs Soft Penalties).
    Returns dict:
      hard_reject_reason: str | None
      soft_penalty_notes: list
      exceptional_override: str | None
      shortlist_reason: str
      over_budget: bool
    """
    profile        = row["profile"]
    status         = row["status"].lower()
    price_unknown  = row["Price_Unknown"] == "Yes"
    price_val      = row["_price_float"]
    vram_val       = row["_vram_float"]
    unified_val    = row["_unified_float"]

    # Load thresholds from config
    budget_cap        = config.get("budget_cap_aud", 4500.0)
    behavior          = config.get("shortlist_behavior", {})
    exc_vram          = config.get("exceptional_overrides", {}).get("vram_threshold_gb", 24.0)
    exc_max_budget    = config.get("exceptional_overrides", {}).get("max_override_budget_aud", 6000.0)

    hard_reject_reason = None
    soft_penalty_notes = []
    exceptional_override = None
    is_over_budget = False

    # Gate 1: Out of Stock
    if "out of stock" in status:
        if behavior.get("out_of_stock_action") == "hard_reject":
            hard_reject_reason = "Out of Stock"
            return {"hard_reject_reason": hard_reject_reason, "soft_penalty_notes": [], "exceptional_override": None, "shortlist_reason": "", "over_budget": False}

    # Gate 2: VRAM floor (Complete Systems only)
    if row["Category_Group"] == "Complete_System":
        if profile in ("Laptop", "Mini PC", "Apple Silicon"):
            floor_dis = config.get("laptop_discrete_minimum_vram_gb", 8.0)
            floor_uni = config.get("laptop_unified_minimum_vram_gb", 16.0)
            effective_vram = vram_val or 0
            effective_unified = unified_val or 0
            
            # If both are known or partially known and fail:
            if vram_val is not None or unified_val is not None:
                if effective_vram < floor_dis and effective_unified < floor_uni:
                    msg = f"Below VRAM floor: vram={vram_val} GB, unified={effective_unified} GB (need ≥{floor_dis} GB discrete or ≥{floor_uni} GB unified)"
                    if behavior.get("below_vram_floor_action") == "hard_reject":
                        hard_reject_reason = msg
                        return {"hard_reject_reason": hard_reject_reason, "soft_penalty_notes": [], "exceptional_override": None, "shortlist_reason": "", "over_budget": False}
                    else:
                        soft_penalty_notes.append(msg)
        elif profile in ("Desktop",):
            floor_desk = config.get("desktop_minimum_vram_gb", 8.0)
            if vram_val is not None and vram_val < floor_desk:
                msg = f"Below VRAM floor: {vram_val} GB discrete (need ≥{floor_desk} GB)"
                if behavior.get("below_vram_floor_action") == "hard_reject":
                    hard_reject_reason = msg
                    return {"hard_reject_reason": hard_reject_reason, "soft_penalty_notes": [], "exceptional_override": None, "shortlist_reason": "", "over_budget": False}
                else:
                    soft_penalty_notes.append(msg)

    # Soft Penalties & Overrides
    if price_unknown:
        soft_penalty_notes.append("Price UNKNOWN — research required")

    if not price_unknown and price_val is not None and price_val > budget_cap:
        is_over_budget = True
        msg = f"Exceeds ${budget_cap:,.0f} AUD budget (price: ${price_val:,.2f})"
        
        # Check if exceptional override applies
        vram_check = vram_val if vram_val is not None else 0
        uni_check = unified_val if unified_val is not None else 0
        max_vram = max(vram_check, uni_check)
        
        if max_vram >= exc_vram and price_val <= exc_max_budget:
            exceptional_override = f"≥ {exc_vram}GB VRAM allows budget stretch to ${exc_max_budget}"
            soft_penalty_notes.append(f"{msg} [ALLOWED: {exceptional_override}]")
        elif "5090" in row["gpu_model"].upper() and price_val <= exc_max_budget:
            exceptional_override = f"RTX 5090 Tier allows budget stretch to ${exc_max_budget}"
            soft_penalty_notes.append(f"{msg} [ALLOWED: {exceptional_override}]")
        else:
            # Over budget and not exceptional
            if behavior.get("over_budget_action") == "hard_reject":
                hard_reject_reason = msg
                return {"hard_reject_reason": hard_reject_reason, "soft_penalty_notes": [], "exceptional_override": None, "shortlist_reason": "", "over_budget": True}
            else:
                soft_penalty_notes.append(msg)
                
    if row["verification_status"] in ("Unverified", "UNKNOWN"):
        soft_penalty_notes.append("Unverified — confirm specs before scoring")
        
    if row["au_stock"] in ("UNKNOWN", "No"):
        soft_penalty_notes.append(f"AU stock: {row['au_stock']}")

    return {
        "hard_reject_reason": hard_reject_reason,
        "soft_penalty_notes": soft_penalty_notes,
        "exceptional_override": exceptional_override,
        "shortlist_reason": "Passed gates" if not exceptional_override else "Passed via exceptional override",
        "over_budget": is_over_budget
    }


# ---------------------------------------------------------------------------
# Row builder
# ---------------------------------------------------------------------------

def build_row(fm: dict, intake_info: dict, source_path: Path) -> dict:
    """Build a fully annotated shortlist row from a card's frontmatter."""

    # Raw field extraction
    item_name        = fm.get("name", "")
    category         = fm.get("category", "UNKNOWN")
    gpu_model        = fm.get("gpu", "UNKNOWN")
    vram_raw         = fm.get("vram", "UNKNOWN").replace("GB", "").strip()
    unified_raw      = fm.get("unified_memory", "UNKNOWN").replace("GB", "").strip()
    price_raw        = fm.get("price_aud", "UNKNOWN").replace("$", "").replace("AUD", "").strip()
    condition        = fm.get("condition", "UNKNOWN")
    retailer         = fm.get("retailer", "UNKNOWN")
    vstatus          = fm.get("verification", "UNKNOWN")
    au_stock         = fm.get("au_stock", "UNKNOWN")
    status           = fm.get("status", "Active")
    track            = fm.get("track", "UNKNOWN")
    pathway          = fm.get("pathway", "UNKNOWN")

    # Derived
    profile        = classify_profile(category)
    price_float, price_unknown = parse_price(price_raw)
    vram_float     = parse_vram(vram_raw)
    unified_float  = parse_vram(unified_raw)
    cat_group      = classify_category_group(profile, gpu_model)

    # Intake ID from filename
    fname = source_path.name
    intake_id_match = re.match(r"(intake-\d+)", fname)
    intake_id = intake_id_match.group(1) if intake_id_match else fname.replace(".md", "")

    row = {
        # Identity
        "intake_id":            intake_id,
        "item_name":            item_name,
        "source_file":          str(source_path.relative_to(REPO_ROOT)),
        "batch":                intake_info.get("batch", "UNKNOWN"),
        # Classification
        "profile":              profile,
        "category":             category,
        "Category_Group":       cat_group,
        "track":                track,
        "pathway":              pathway,
        # Specs
        "gpu_model":            gpu_model,
        "vram_gb":              vram_float if vram_float is not None else "UNKNOWN",
        "unified_memory_gb":    unified_float if unified_float is not None else "UNKNOWN",
        "price_aud":            price_float if price_float is not None else "UNKNOWN",
        "Price_Unknown":        "Yes" if price_unknown else "",
        "condition":            condition,
        "retailer":             retailer,
        "verification_status":  vstatus,
        "au_stock":             au_stock,
        "status":               status,
        # Engine metadata
        "Machine":              intake_id,   # rubric_weighting_engine.py expects this
        "Type":                 "Candidate", # default; user can change to Preferred/NeverBuy
        # Score columns — all blank for manual completion
        **{col: "" for col in SCORE_COLUMNS},
        # Internal helpers (stripped before CSV output)
        "_price_float":         price_float,
        "_vram_float":          vram_float,
        "_unified_float":       unified_float,
    }
    return row


# ---------------------------------------------------------------------------
# Card scanner
# ---------------------------------------------------------------------------

def scan_intake_cards(batch_filter: str | None, profile_filter: str | None) -> list[dict]:
    """
    Walk all INTAKE_LANES and return a list of fully-built row dicts.
    """
    rows = []
    for lane in INTAKE_LANES:
        folder = WORKSPACE / lane
        if not folder.exists():
            continue
        for md_path in sorted(folder.glob("intake-*.md")):
            text = md_path.read_text(encoding="utf-8", errors="replace")
            fm          = parse_frontmatter(text)
            intake_info = parse_tags_comment(text)

            if not fm:
                continue  # skip unparseable cards

            row = build_row(fm, intake_info, md_path)

            # Batch filter
            if batch_filter and batch_filter not in row["batch"]:
                continue

            # Profile filter
            if profile_filter and row["profile"].lower() != profile_filter.lower():
                continue

            rows.append(row)

    return rows


# ---------------------------------------------------------------------------
# CSV writers
# ---------------------------------------------------------------------------

SHORTLIST_FIELDNAMES = [
    "intake_id", "item_name", "profile", "category", "Category_Group",
    "track", "pathway", "gpu_model", "vram_gb", "unified_memory_gb",
    "price_aud", "Over_Budget", "Price_Unknown",
    "condition", "retailer", "verification_status", "au_stock", "status",
    "batch", "source_file", "exceptional_override", "shortlist_reason", "soft_penalty_notes",
    # Engine columns
    "Machine", "Type",
    # Score columns
    *SCORE_COLUMNS,
]

REJECTED_FIELDNAMES = [col for col in SHORTLIST_FIELDNAMES if col not in ("Machine", "Type", *SCORE_COLUMNS)] + ["rejection_reason"]


def strip_internals(row: dict) -> dict:
    return {k: v for k, v in row.items() if not k.startswith("_")}


def write_csv(path: Path, fieldnames: list, rows: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows([strip_internals(r) for r in rows])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Phase 2 of the hardware procurement pipeline.\n\n"
            "Scans intake-*.md cards, applies policy from config/procurement_policy.json\n"
            "(handling hard rejects vs soft penalties), and emits a CSV ready for scoring."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/build_shortlist.py
  python scripts/build_shortlist.py --dry-run
  python scripts/build_shortlist.py --profile laptop

After generating the shortlist, run the pricing enrichment step:
  python scripts/enrich_shortlist_pricing.py
        """,
    )
    parser.add_argument(
        "--batch", default=None, metavar="STEM",
        help="Filter to a specific intake batch stem",
    )
    parser.add_argument(
        "--profile", default=None,
        choices=["laptop", "desktop", "mini pc", "component", "apple silicon", "all"],
        help="Filter by device profile (default: all profiles)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview shortlist without writing any files",
    )
    args = parser.parse_args()

    # Load machine-readable config
    config = load_config()

    profile_filter = None if (args.profile in (None, "all")) else args.profile

    print(f"\n🔍 Scanning intake cards in {WORKSPACE.relative_to(REPO_ROOT)} ...")
    all_rows = scan_intake_cards(args.batch, profile_filter)
    print(f"   Cards found: {len(all_rows)}")

    # Apply gates & policies
    shortlist = []
    rejected  = []

    for row in all_rows:
        eval_result = evaluate_policy(row, config)
        
        if eval_result["hard_reject_reason"]:
            row["rejection_reason"] = eval_result["hard_reject_reason"]
            rejected.append(row)
        else:
            row["Over_Budget"] = "Yes" if eval_result["over_budget"] else "No"
            row["exceptional_override"] = eval_result["exceptional_override"] or ""
            row["shortlist_reason"] = eval_result["shortlist_reason"]
            row["soft_penalty_notes"] = "; ".join(eval_result["soft_penalty_notes"])
            shortlist.append(row)

    # Sort: Complete_System first, then Standalone_GPU, then Workstation_GPU
    group_order = {"Complete_System": 0, "Standalone_GPU": 1, "Workstation_GPU": 2}
    shortlist.sort(key=lambda r: (
        group_order.get(r["Category_Group"], 9),
        r["profile"],
        str(r["vram_gb"]) if r["vram_gb"] != "UNKNOWN" else "0",
    ), reverse=False)

    # Print preview
    print(f"\n{'─'*70}")
    print(f"  SHORTLIST ({len(shortlist)} candidates):")
    print(f"{'─'*70}")
    for r in shortlist:
        flags = []
        if r["Price_Unknown"] == "Yes": flags.append("[PRICE UNKNOWN]")
        if r["Over_Budget"] == "Yes": flags.append("[OVER BUDGET]")
        if r["exceptional_override"]: flags.append("[EXCEPTIONAL]")
        flag_str = " ".join(flags)
        
        print(f"  {r['intake_id']:12s}  {r['profile']:12s}  {r['Category_Group']:18s}  "
              f"{str(r['vram_gb']):>6} GB  ${str(r['price_aud']):>8} {flag_str}  "
              f"{r['item_name'][:30]}")

    print(f"\n{'─'*70}")
    print(f"  REJECTED ({len(rejected)} candidates):")
    print(f"{'─'*70}")
    for r in rejected:
        print(f"  {r['intake_id']:12s}  {r['profile']:12s}  {r['item_name'][:40]:40s}  "
              f"→ {r.get('rejection_reason', '?')}")

    if args.dry_run:
        print(f"\n  [DRY RUN] — no files written.\n")
        return

    # Write outputs
    today     = date.today().isoformat()
    out_dir   = WORKSPACE / "intake" / "shortlist"
    sl_path   = out_dir / f"{today}_shortlist.csv"
    rej_path  = out_dir / f"{today}_shortlist_rejected.csv"

    write_csv(sl_path, SHORTLIST_FIELDNAMES, shortlist)
    write_csv(rej_path, REJECTED_FIELDNAMES, rejected)

    print(f"\n✅ Shortlist complete.")
    print(f"   Shortlisted : {len(shortlist)} → {sl_path.relative_to(REPO_ROOT)}")
    print(f"   Rejected    : {len(rejected)} → {rej_path.relative_to(REPO_ROOT)}")
    print(f"\n   Next: Run the live pricing enrichment step:")
    print(f"   python scripts/enrich_shortlist_pricing.py {sl_path.relative_to(REPO_ROOT)}\n")


if __name__ == "__main__":
    main()
````

## File: scripts/enrich_shortlist_pricing.py
````python
#!/usr/bin/env python3
"""
enrich_shortlist_pricing.py — Phase 2b of the hardware procurement pipeline.

Takes a shortlist CSV generated by build_shortlist.py and outputs an enriched
version with empty columns for live pricing intelligence (cashback, student discounts,
stackable coupons, etc.).

Usage:
    python scripts/enrich_shortlist_pricing.py NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist.csv
"""

import argparse
import csv
import sys
from pathlib import Path

PRICING_COLUMNS = [
    "current_best_price_aud",
    "current_best_retailer",
    "current_best_url",
    "in_stock_now",
    "student_discount_possible",
    "cashback_possible",
    "cashback_source",
    "stackable_coupons_confirmed",
    "price_match_possible",
    "price_beat_possible",
    "effective_best_price_aud",
    "promo_notes",
    "pricing_checked_at"
]

def main():
    parser = argparse.ArgumentParser(description="Add pricing enrichment columns to a shortlist CSV.")
    parser.add_argument("csv_path", type=str, help="Path to the input shortlist CSV")
    args = parser.parse_args()

    input_path = Path(args.csv_path)
    if not input_path.exists():
        sys.exit(f"Error: Input file {input_path} does not exist.")

    output_path = input_path.parent / f"{input_path.stem}_pricing_enriched.csv"

    with open(input_path, "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)
        fieldnames = reader.fieldnames
        if not fieldnames:
            sys.exit("Error: Input CSV has no headers.")
            
        # Avoid duplicating columns if ran twice
        new_fieldnames = list(fieldnames)
        for col in PRICING_COLUMNS:
            if col not in new_fieldnames:
                new_fieldnames.append(col)

        rows = list(reader)

    # Initialize new columns to blank
    for row in rows:
        for col in PRICING_COLUMNS:
            if col not in row:
                row[col] = ""

    with open(output_path, "w", newline="", encoding="utf-8") as fout:
        writer = csv.DictWriter(fout, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n✅ Pricing enrichment scaffold created successfully!")
    print(f"   Output: {output_path}")
    print(f"\n   Next Steps:")
    print(f"   1. Use the prompt template in `scripts/prompt_templates/browser_pricing_lookup.md`")
    print(f"      to instruct your Vercel Browser Agent to look up live prices.")
    print(f"   2. Fill in the new pricing columns in the enriched CSV.")
    print(f"   3. Score the candidates and run `rubric_weighting_engine.py --profile merged`")

if __name__ == "__main__":
    main()
````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-009_lenovo-legion-pro-7i.md
````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: lenovo-legion-pro-7i
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Lenovo Legion Pro 7i
gpu: RTX 4090 Mobile
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $4575 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Lenovo Legion Pro 7i

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $4575 AUD
- **Retailer:** Mike PC / Lenovo
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4090 Mobile
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** i9-14900HX
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
The best emotional-but-defensible one-machine route

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-010_msi-raider-18-hx-ai-a2xwjg.md
````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-24GB #New #TrackUnknown #Verified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: msi-raider-18-hx-ai-a2xwjg
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: MSI Raider 18 HX AI A2XWJG
gpu: RTX 5090 Mobile
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $8488 AUD
condition: New
au_stock: UNKNOWN
verification: Verified
status: Active
score: UNKNOWN — pending manual review
---

# MSI Raider 18 HX AI A2XWJG

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $8488 AUD
- **Retailer:** Scorptec / JW Computers
- **URL:** [https://www.scorptec.com.au/product/ready-to-run-pcs/gaming-pc/124318-r2r10638](https://www.scorptec.com.au/product/ready-to-run-pcs/gaming-pc/124318-r2r10638)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090 Mobile
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 285HX
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Massive desktop replacement that overcomes traditional laptop VRAM limits

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-011_dell-alienware-m18-r2-area-51.md
````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: dell-alienware-m18-r2-area-51
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Dell Alienware m18 R2 / Area-51
gpu: RTX 5090 Mobile
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $4499 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Dell Alienware m18 R2 / Area-51

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $4499 AUD
- **Retailer:** Dell Outlet / Best Buy
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090 Mobile
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 275HX
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
18-inch desktop replacement offering 24GB of mobile VRAM

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-052_acer-predator-helios-neo-16s-ai-rtx-5060.md
````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-8GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: acer-predator-helios-neo-16s-ai-rtx-5060
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Acer Predator Helios Neo 16S AI RTX 5060
gpu: RTX 5060
vram: 8 GB
unified_memory: UNKNOWN
price_aud: $2399 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Acer Predator Helios Neo 16S AI RTX 5060

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2399 AUD
- **Retailer:** Acer AU Clearance
- **URL:** [https://store.acer.com/en-au/](https://store.acer.com/en-au/)
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5060
- **VRAM:** 8 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 275HX
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Refurbished entry level laptop

## AI Capability Summary
Baseline — 8 GB VRAM sufficient for 7B Q4; larger models require significant offload.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
````

## File: scripts/intake_to_cards.py
````python
#!/usr/bin/env python3
"""
intake_to_cards.py — Convert normalized intake CSV into Markdown product cards.

Reads a *_processed.csv from NotebookLM_Workspaces/intake/processed/ and emits
one .md product card per row into the appropriate lane folder under
NotebookLM_Workspaces/.

Usage:
    python scripts/intake_to_cards.py NotebookLM_Workspaces/intake/processed/2026-05-05_notebooklm_batch1_processed.csv
    python scripts/intake_to_cards.py path/to/file.csv --dry-run
    python scripts/intake_to_cards.py path/to/file.csv --overwrite
    python scripts/intake_to_cards.py path/to/file.csv --skip-existing

Output folders (relative to repo root):
    Laptop            → 04_Laptops_Mainline/
    Desktop (New)     → 03_New_Desktop_Systems/
    Desktop (Refurb)  → 02_Refurbished_Desktop_Towers/
    Desktop (Gaming Refurb) → Desktop_Gaming_Refurbished/
    Mini PC / eGPU    → 06_Mini_PCs_and_eGPU/
    Component / GPU   → 09_Individual_Components/
    DIY Build         → 08_Custom_Builds/
    Apple Silicon     → 05_Apple_Silicon_Systems/
    Fallback          → 01_Research_Methods_and_Decision_System/

Behaviour on filename collision:
    Default  → skip and log (safe)
    --overwrite → replace existing
    --dry-run   → show what would be written, write nothing
"""

import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = REPO_ROOT / "NotebookLM_Workspaces"

# Category/condition → target folder mapping
# Evaluated in order; first match wins.
ROUTING_RULES: list[tuple[str, str, str, str]] = [
    # (category_pattern, condition_pattern, note, folder_name)
    ("mini pc|egpu",         r".*",           "Mini PC / eGPU",       "06_Mini_PCs_and_eGPU"),
    ("component|gpu",        r".*",           "Standalone component",  "09_Individual_Components"),
    ("diy build|custom",     r".*",           "DIY / Custom build",    "08_Custom_Builds"),
    ("apple",                r".*",           "Apple Silicon",         "05_Apple_Silicon_Systems"),
    # Laptop – all conditions to main lane (no separate refurb lane for laptops)
    ("laptop",               r".*",           "Laptop",                "04_Laptops_Mainline"),
    # Desktops – split on condition
    ("desktop",              r"refurb|used|open box", "Refurb desktop", "02_Refurbished_Desktop_Towers"),
    ("desktop",              r"new",          "New desktop",           "03_New_Desktop_Systems"),
    # Fallback desktop catch-all
    ("desktop",              r".*",           "Desktop (uncategorised)","03_New_Desktop_Systems"),
]

FALLBACK_FOLDER = "01_Research_Methods_and_Decision_System"

# Condition → condition tags
CONDITION_TAG_MAP = {
    "new":        "#New",
    "refurbished":"#Refurbished",
    "used":       "#Used",
    "open box":   "#OpenBox",
}

# Track → track tags
TRACK_TAG_MAP = {
    "track1a":  "#Track1A",
    "track1b":  "#Track1B",
    "track1.5": "#Track1-5",
    "track2a":  "#Track2A",
    "track2b":  "#Track2B",
    "track2c":  "#Track2C",
}

# VRAM threshold tags
def vram_tag(vram_str: str) -> str:
    try:
        v = float(vram_str)
        if v >= 48:
            return "#VRAM-48GB+"
        elif v >= 24:
            return "#VRAM-24GB"
        elif v >= 16:
            return "#VRAM-16GB"
        elif v >= 8:
            return "#VRAM-8GB"
        else:
            return "#VRAM-Unknown"
    except (ValueError, TypeError):
        return "#VRAM-Unknown"


# ---------------------------------------------------------------------------
# Routing
# ---------------------------------------------------------------------------

def route_row(row: dict) -> tuple[Path, str]:
    """Return (target_folder_path, routing_note)."""
    cat   = (row.get("category") or "").strip().lower()
    cond  = (row.get("condition") or "").strip().lower()

    for cat_pat, cond_pat, note, folder in ROUTING_RULES:
        if re.search(cat_pat, cat) and re.search(cond_pat, cond, re.IGNORECASE):
            return WORKSPACE / folder, note

    return WORKSPACE / FALLBACK_FOLDER, "Fallback — unrecognised category/condition"


# ---------------------------------------------------------------------------
# Slug generation
# ---------------------------------------------------------------------------

def slugify(text: str, maxlen: int = 60) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text.strip())
    text = re.sub(r"-{2,}", "-", text)
    return text[:maxlen].rstrip("-")


def make_filename(row: dict, index: int) -> str:
    name  = row.get("item_name") or "unknown-item"
    slug  = slugify(name)
    return f"intake-{index:03d}_{slug}.md"


# ---------------------------------------------------------------------------
# Tag assembly
# ---------------------------------------------------------------------------

def build_tags(row: dict) -> str:
    tags: list[str] = []

    cat = (row.get("category") or "").strip().lower()
    if "laptop"    in cat: tags.append("#Laptop")
    elif "desktop" in cat: tags.append("#Desktop")
    elif "mini pc" in cat: tags.append("#MiniPC")
    elif "egpu"    in cat: tags.append("#eGPU")
    elif "component" in cat or "gpu" in cat: tags.append("#Component")
    elif "diy"     in cat or "custom" in cat: tags.append("#CustomBuild")
    elif "apple"   in cat: tags.append("#AppleSilicon")

    gpu = (row.get("gpu_model") or "").upper()
    if "RTX" in gpu or "NVIDIA" in gpu: tags.append("#NVIDIA")
    elif "RX " in gpu or "RADEON" in gpu or "AMD" in gpu: tags.append("#AMD")
    elif "ARC" in gpu: tags.append("#Intel")

    tags.append(vram_tag(row.get("vram_gb") or "0"))

    cond = (row.get("condition") or "").strip().lower()
    tags.append(CONDITION_TAG_MAP.get(cond, "#ConditionUnknown"))

    track_key = (row.get("track") or "").strip().lower()
    tags.append(TRACK_TAG_MAP.get(track_key, "#TrackUnknown"))

    vstatus = (row.get("verification_status") or "").strip()
    if vstatus == "Verified":        tags.append("#Verified")
    elif vstatus == "Needs Verification": tags.append("#NeedsVerification")
    else:                            tags.append("#Unverified")

    au = (row.get("au_stock_confirmed") or "").strip()
    if au == "Yes":  tags.append("#AUStock-Confirmed")
    elif au == "No": tags.append("#AUStock-No")
    else:            tags.append("#AUStock-Unknown")

    return " ".join(tags)


# ---------------------------------------------------------------------------
# Card rendering
# ---------------------------------------------------------------------------

def fmt(val: str | None, fallback: str = "UNKNOWN") -> str:
    v = (val or "").strip()
    return v if v and v.upper() not in ("UNKNOWN", "N/A", "NONE", "") else fallback


def url_md(url: str | None) -> str:
    u = fmt(url)
    if u == "UNKNOWN":
        return "UNKNOWN"
    return f"[{u}]({u})"


def checkbox(label: str, done: bool = False) -> str:
    mark = "x" if done else " "
    return f"- [{mark}] {label}"


def render_card(row: dict, tags: str, routing_note: str, source_batch: str) -> str:
    name     = fmt(row.get("item_name"), "Unnamed Item")
    slug_id  = slugify(name)
    cat      = fmt(row.get("category"))
    track    = fmt(row.get("track"))
    pathway  = fmt(row.get("pathway"))
    gpu      = fmt(row.get("gpu_model"))
    vram     = fmt(row.get("vram_gb"))
    unified  = fmt(row.get("unified_memory_gb"))
    ram      = fmt(row.get("ram_gb"))
    cpu      = fmt(row.get("cpu_model"))
    cond     = fmt(row.get("condition"))
    price    = fmt(row.get("price_aud"))
    retailer = fmt(row.get("retailer"))
    url      = url_md(row.get("url"))
    au_stock = fmt(row.get("au_stock_confirmed"))
    vstatus  = fmt(row.get("verification_status"))
    status   = fmt(row.get("status"))
    notes    = fmt(row.get("notes"), "No notes.")
    date_f   = fmt(row.get("date_found"))

    price_str = f"${price} AUD" if price != "UNKNOWN" else "UNKNOWN"
    vram_str  = f"{vram} GB" if vram != "UNKNOWN" else "UNKNOWN"
    unified_str = f"{unified} GB" if unified != "UNKNOWN" else "UNKNOWN"
    ram_str   = f"{ram} GB" if ram != "UNKNOWN" else "UNKNOWN"

    # --- Frontmatter + tag comment ---
    lines = [
        f"<!-- TAGS: {tags} -->",
        f"<!-- INTAKE: batch={source_batch} date={date_f} route={routing_note} -->",
        "---",
        f"id: {slug_id}",
        f"category: {cat.lower()}",
        f"track: {track}",
        f"pathway: {pathway}",
        f"name: {name}",
        f"gpu: {gpu}",
        f"vram: {vram_str}",
        f"unified_memory: {unified_str}",
        f"price_aud: {price_str}",
        f"condition: {cond}",
        f"au_stock: {au_stock}",
        f"verification: {vstatus}",
        f"status: {status}",
        "score: UNKNOWN — pending manual review",
        "---",
        "",
        f"# {name}",
        "",
    ]

    # Warn banner if unverified
    if vstatus in ("UNKNOWN", "Unverified"):
        lines += [
            "> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**",
            "> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.",
            "",
        ]

    # --- Track status block ---
    lines += [
        "## Track Status",
        f"- **Track:** {track}",
        f"- **Pathway:** {pathway}",
        f"- **Status:** {status}",
        f"- **AU Stock Confirmed:** {au_stock}",
        f"- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below",
        "",
    ]

    # --- Overview ---
    lines += [
        "## Overview",
        f"- **Price (AUD):** {price_str}",
        f"- **Retailer:** {retailer}",
        f"- **URL:** {url}",
        f"- **Condition:** {cond}",
        f"- **Source batch:** {source_batch} (ingested {date_f})",
        "",
    ]

    # --- Key Specs ---
    lines += [
        "## Key Specs",
        f"- **GPU:** {gpu}",
        f"- **VRAM:** {vram_str}",
        f"- **Unified Memory:** {unified_str}",
        f"- **CPU:** {cpu}",
        f"- **RAM:** {ram_str}",
        "- **Storage:** UNKNOWN",
        "- **PSU / Charger:** UNKNOWN",
        "- **Warranty (AU):** UNKNOWN",
        "",
    ]

    # --- Notes from batch ---
    lines += [
        "## Source Notes",
        notes,
        "",
    ]

    # --- AI capability stub ---
    ai_cap = "UNKNOWN — to be completed after manual spec verification."
    if vram != "UNKNOWN":
        try:
            v = float(vram)
            if v >= 48:
                ai_cap = "Exceptional — 48 GB+ VRAM supports 70B+ models fully in VRAM at Q4."
            elif v >= 24:
                ai_cap = "Strong — 24 GB VRAM handles 30B–34B Q4 models natively."
            elif v >= 16:
                ai_cap = "Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading."
            elif v >= 8:
                ai_cap = "Baseline — 8 GB VRAM sufficient for 7B Q4; larger models require significant offload."
        except ValueError:
            pass

    lines += [
        "## AI Capability Summary",
        ai_cap,
        "",
    ]

    # --- Verification checklist ---
    au_confirmed  = au_stock == "Yes"
    price_known   = price != "UNKNOWN"
    gpu_known     = gpu != "UNKNOWN"
    cpu_known     = cpu != "UNKNOWN"
    ram_known     = ram != "UNKNOWN"

    lines += [
        "## Verification Checklist",
        checkbox("Confirm AU stock from named retailer with URL", au_confirmed),
        checkbox("Confirm price in AUD",                         price_known),
        checkbox("Confirm GPU model and VRAM",                   gpu_known),
        checkbox("Confirm CPU model",                            cpu_known),
        checkbox("Confirm RAM installed and max supported",      ram_known),
        checkbox("Confirm storage installed and free M.2 slots", False),
        checkbox("Confirm PSU / charger wattage",                False),
        checkbox("Confirm warranty term and type (AU)",          False),
        checkbox("Check thermal reputation (reviews)",           False),
        checkbox("Confirm AGENTS.md GOOD ENOUGH gate cleared",   False),
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Convert normalized intake CSV to Markdown product cards.")
    parser.add_argument("input_csv", help="Path to *_processed.csv")
    parser.add_argument("--dry-run",       action="store_true", help="Preview output; do not write files")
    parser.add_argument("--overwrite",     action="store_true", help="Overwrite existing card files")
    parser.add_argument("--skip-existing", action="store_true", help="Skip (default) rows whose card file already exists")
    args = parser.parse_args()

    input_path = Path(args.input_csv).resolve()
    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    source_batch = input_path.stem  # e.g. 2026-05-05_notebooklm_batch1_processed

    rows = []
    with open(input_path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            rows.append(row)

    print(f"\n📋 Processing: {input_path.name}")
    print(f"   Rows found: {len(rows)}")
    if args.dry_run:
        print("   [DRY RUN] — no files will be written\n")

    log: list[dict] = []
    written = skipped = errored = 0

    for idx, row in enumerate(rows, start=1):
        item_name = row.get("item_name") or f"row-{idx}"
        try:
            folder, routing_note = route_row(row)
            tags     = build_tags(row)
            filename = make_filename(row, idx)
            out_path = folder / filename

            card = render_card(row, tags, routing_note, source_batch)

            if args.dry_run:
                print(f"  [{idx:03d}] DRY-RUN → {out_path.relative_to(REPO_ROOT)}")
                print(f"          route: {routing_note}")
                written += 1
                log.append({"index": idx, "item": item_name, "action": "dry-run", "path": str(out_path)})
                continue

            if out_path.exists() and not args.overwrite:
                print(f"  [{idx:03d}] SKIP (exists) → {out_path.relative_to(REPO_ROOT)}")
                skipped += 1
                log.append({"index": idx, "item": item_name, "action": "skipped", "path": str(out_path)})
                continue

            folder.mkdir(parents=True, exist_ok=True)
            out_path.write_text(card, encoding="utf-8")
            action = "overwrite" if out_path.exists() else "written"
            print(f"  [{idx:03d}] ✅ {action.upper()} → {out_path.relative_to(REPO_ROOT)}")
            written += 1
            log.append({"index": idx, "item": item_name, "action": action, "path": str(out_path), "route": routing_note})

        except Exception as exc:  # noqa: BLE001
            print(f"  [{idx:03d}] ❌ ERROR — {item_name}: {exc}", file=sys.stderr)
            errored += 1
            log.append({"index": idx, "item": item_name, "action": "error", "error": str(exc)})

    # --- Write run log ---
    log_dir = input_path.parent
    log_stem = input_path.stem.replace("_processed", "")
    log_path = log_dir / f"{log_stem}_cards_log.json"
    if not args.dry_run:
        log_path.write_text(json.dumps({
            "run_timestamp": datetime.now().isoformat(),
            "input_file": str(input_path),
            "counts": {
                "total_rows": len(rows),
                "written":    written,
                "skipped":    skipped,
                "errored":    errored,
            },
            "entries": log,
        }, indent=2), encoding="utf-8")

    # --- Summary ---
    print(f"""
✅ Card generation complete.
   Written  : {written}
   Skipped  : {skipped}
   Errors   : {errored}
""")
    if not args.dry_run:
        print(f"   Run log  → {log_path.relative_to(REPO_ROOT)}\n")


if __name__ == "__main__":
    main()
````

## File: scripts/normalize_intake.py
````python
#!/usr/bin/env python3
"""
normalize_intake.py
-------------------
Preprocessing layer for raw Gemini / NotebookLM hardware CSV output.

Handles malformed input: one-line CSVs, repeated headers, code fences,
wrapper text, truncated URLs, bad enums, and column count mismatches.

Usage:
    python scripts/normalize_intake.py path/to/raw_file.txt
    python scripts/normalize_intake.py path/to/raw_file.txt --out-dir path/to/output/

Outputs (default: NotebookLM_Workspaces/intake/processed/):
    <stem>_processed.csv          — clean, normalized rows
    <stem>_manual_review.csv      — rows that could not be reliably parsed
    <stem>_normalization_log.json — all warnings, coercions, counts
"""

import argparse
import csv
import io
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

CANONICAL_HEADER = [
    "date_found", "source_batch", "track", "pathway", "category",
    "item_name", "price_aud", "gpu_model", "vram_gb", "unified_memory_gb",
    "ram_gb", "cpu_model", "condition", "retailer", "url",
    "au_stock_confirmed", "verification_status", "status", "notes",
]
NUM_COLS = len(CANONICAL_HEADER)  # 19

# ---------------------------------------------------------------------------
# Enum allowed values (lowercase keys → display values)
# ---------------------------------------------------------------------------

ENUM_TRACK = {
    "track1a": "Track1A",
    "track1b": "Track1B",
    "track1.5": "Track1.5",
    "track2a": "Track2A",
    "track2b": "Track2B",
    "track2c": "Track2C",
}

ENUM_CATEGORY = {
    "laptop": "Laptop",
    "desktop": "Desktop",
    "component": "Component",
    "diy build": "DIY Build",
    "mini pc": "Mini PC",
    "egpu": "eGPU",
}

ENUM_CONDITION = {
    "new": "New",
    "used": "Used",
    "refurbished": "Refurbished",
    "open box": "Open Box",
    "pre-owned": "Refurbished",
    "ex-demo": "Open Box",
}

ENUM_AU_STOCK = {
    "yes": "Yes",
    "no": "No",
}

ENUM_VERIFICATION = {
    "unverified": "Unverified",
    "needs verification": "Needs Verification",
    "verified": "Verified",
}

ENUM_STATUS = {
    "active": "Active",
    "superseded": "Superseded",
    "out of stock": "Out of Stock",
    "watchlist": "Watchlist",
}

# Tokens that should be treated as missing/unknown
NULL_TOKENS = {"", "none", "null", "n/a", "na", "unknown", "-", "—", "–"}


# ---------------------------------------------------------------------------
# Basic field helpers
# ---------------------------------------------------------------------------

def is_null(val: str) -> bool:
    """Return True if val is a null-like token."""
    return val.strip().lower() in NULL_TOKENS


def normalize_null(val: str) -> str:
    """Replace null-like values with UNKNOWN; otherwise strip whitespace."""
    return "UNKNOWN" if is_null(val) else val.strip()


def collapse_whitespace(val: str) -> str:
    """Collapse runs of whitespace to a single space."""
    return re.sub(r"\s+", " ", val).strip()


# ---------------------------------------------------------------------------
# Input cleaning — strip Gemini wrapper artifacts
# ---------------------------------------------------------------------------

def strip_code_fences(text: str) -> str:
    """Remove markdown code fences (```csv, ```, etc.)."""
    text = re.sub(r"^```[a-z]*\s*$", "", text, flags=re.MULTILINE)
    return text


def strip_wrapper_text(text: str) -> str:
    """Remove common Gemini/NotebookLM UI chrome that precedes the CSV."""
    # Match lines that are purely wrapper phrases
    wrapper_pattern = re.compile(
        r"^(Code snippet|Download code|Copy code|Here is the CSV[:\s]*"
        r"|Output[:\s]*|Result[:\s]*|Here are the results[:\s]*)\s*$",
        flags=re.IGNORECASE | re.MULTILINE,
    )
    text = wrapper_pattern.sub("", text)
    return text


# ---------------------------------------------------------------------------
# URL normalization
# ---------------------------------------------------------------------------

def normalize_url(url: str, warnings: list, row_id: str) -> str:
    """
    Normalize the url field:
      - Expand markdown links [label](url) -> url
      - Accept plain http/https URLs
      - Truncated URLs (ending '...' or '…') -> UNKNOWN
      - Non-http values -> UNKNOWN (logged)
    """
    url = url.strip()

    if is_null(url):
        return "UNKNOWN"

    # Expand markdown link: [any text](https://...)
    md_match = re.match(r"\[.*?\]\((https?://[^\)]+)\)", url)
    if md_match:
        url = md_match.group(1).strip()

    # Truncated URL
    if url.endswith("...") or url.endswith("…"):
        warnings.append({
            "type": "truncated_url",
            "row": row_id,
            "original": url,
        })
        return "UNKNOWN"

    # Must start with http:// or https://
    if not re.match(r"^https?://", url):
        warnings.append({
            "type": "invalid_url",
            "row": row_id,
            "original": url,
        })
        return "UNKNOWN"

    return url


# ---------------------------------------------------------------------------
# Numeric normalization
# ---------------------------------------------------------------------------

def normalize_numeric(val: str, field: str, warnings: list, row_id: str) -> str:
    """
    Strip currency symbols ($, AUD), trailing 'GB', commas, and whitespace.
    Coerce to a clean numeric string. On failure, return UNKNOWN.
    """
    val = val.strip()

    if is_null(val):
        return "UNKNOWN"

    cleaned = val.upper()
    cleaned = re.sub(r"AUD", "", cleaned)      # strip AUD text
    cleaned = re.sub(r"[$\s]", "", cleaned)    # strip $ and whitespace
    cleaned = re.sub(r"GB$", "", cleaned)       # strip trailing GB
    cleaned = cleaned.replace(",", "")          # strip thousands commas

    # Handle ranges like "2,500-3,000" — take the lower bound
    range_match = re.match(r"^(\d+\.?\d*)-(\d+\.?\d*)$", cleaned)
    if range_match:
        cleaned = range_match.group(1)
        warnings.append({
            "type": "numeric_range_lowered",
            "field": field,
            "row": row_id,
            "original": val,
            "used": cleaned,
        })

    try:
        float(cleaned)
        return cleaned
    except ValueError:
        warnings.append({
            "type": "invalid_numeric",
            "field": field,
            "row": row_id,
            "original": val,
        })
        return "UNKNOWN"


# ---------------------------------------------------------------------------
# Enum normalization
# ---------------------------------------------------------------------------

def normalize_enum(
    val: str,
    display_map: dict,
    field: str,
    warnings: list,
    row_id: str,
    fallback: str = "UNKNOWN",
) -> str:
    """
    Normalize an enum field via exact lowercase match, then partial match.
    Returns the display-cased value or fallback.
    """
    val = val.strip()

    if is_null(val):
        return fallback

    key = val.lower()

    # Exact match
    if key in display_map:
        return display_map[key]

    # Partial / substring match (e.g. "track 1a" -> "Track1A")
    for allowed_key, display_val in display_map.items():
        if allowed_key in key or key in allowed_key:
            warnings.append({
                "type": "enum_coerced",
                "field": field,
                "row": row_id,
                "original": val,
                "coerced_to": display_val,
            })
            return display_val

    warnings.append({
        "type": "enum_invalid",
        "field": field,
        "row": row_id,
        "original": val,
    })
    return fallback


# ---------------------------------------------------------------------------
# Header detection
# ---------------------------------------------------------------------------

def find_header_line(lines: list) -> int:
    """
    Find the index of the canonical header row.
    Requires the line to contain 'date_found' and at least 5 canonical fields.
    Returns -1 if not found.
    """
    for i, line in enumerate(lines):
        lower = line.lower()
        if "date_found" not in lower:
            continue
        hits = sum(1 for col in CANONICAL_HEADER if col in lower)
        if hits >= 5:
            return i
    return -1


def is_repeated_header(line: str) -> bool:
    """Return True if this line looks like a repeated header row."""
    lower = line.lower()
    return "date_found" in lower and sum(
        1 for col in CANONICAL_HEADER if col in lower
    ) >= 5


# ---------------------------------------------------------------------------
# One-line CSV recovery
# ---------------------------------------------------------------------------

def recover_one_line_csv(text: str) -> list:
    """
    If the entire dataset was returned as one long line, split on boundaries
    that look like the start of a new row: a comma followed by an ISO date.

    Uses a lookahead so the date is preserved on each recovered fragment.
    """
    # Boundary: comma immediately before a 4-digit year (20xx)
    pattern = re.compile(r",(?=20\d{2}-\d{2})")
    parts = pattern.split(text)

    if len(parts) > 1:
        return parts  # first part is the first row; rest start with a date

    return [text]


# ---------------------------------------------------------------------------
# Row parsing
# ---------------------------------------------------------------------------

def parse_csv_line(line: str) -> list | None:
    """
    Parse a single CSV line into a list of fields.
    Returns None on CSV parse error.
    """
    try:
        reader = csv.reader(io.StringIO(line))
        return next(reader)
    except Exception:
        return None


def fit_row_to_schema(fields: list, raw_line: str, warnings: list) -> list | None:
    """
    Attempt to fit a parsed row to exactly NUM_COLS columns.

    - Exact: return as-is.
    - Too many cols: collapse extras into the last (notes) field.
    - Too few: return None (send to manual review).
    """
    n = len(fields)

    if n == NUM_COLS:
        return fields

    if n > NUM_COLS:
        # Overflow columns get folded into the notes field
        fitted = fields[: NUM_COLS - 1] + ["; ".join(fields[NUM_COLS - 1 :])]
        warnings.append({
            "type": "row_overflow_collapsed",
            "expected": NUM_COLS,
            "got": n,
            "raw": raw_line[:120],
        })
        return fitted

    # Too few columns — cannot safely assign fields
    return None


# ---------------------------------------------------------------------------
# Main parse pipeline
# ---------------------------------------------------------------------------

def parse_raw_text(raw: str, warnings: list) -> tuple:
    """
    Full input parsing pipeline.

    Returns:
        (good_rows, bad_rows)
        good_rows: list of lists (each list is NUM_COLS fields)
        bad_rows:  list of str  (raw lines that could not be parsed)

    Raises SystemExit on fatal error (no header found).
    """
    text = strip_code_fences(raw)
    text = strip_wrapper_text(text)

    lines = text.splitlines()

    header_idx = find_header_line(lines)
    if header_idx == -1:
        return None, lines  # caller handles fatal

    # Discard everything before the header
    data_lines = lines[header_idx + 1 :]

    # Remove blanks and repeated headers
    clean_lines = []
    for line in data_lines:
        stripped = line.strip()
        if not stripped:
            continue
        if is_repeated_header(stripped):
            warnings.append({"type": "repeated_header_removed", "line": stripped[:80]})
            continue
        clean_lines.append(stripped)

    # One-line CSV recovery: if only one (very long) line, try to split it
    if len(clean_lines) == 1 and len(clean_lines[0]) > 300:
        recovered = recover_one_line_csv(clean_lines[0])
        if len(recovered) > 1:
            warnings.append({
                "type": "one_line_csv_recovered",
                "fragments": len(recovered),
            })
            clean_lines = recovered

    good_rows = []
    bad_rows = []

    for line in clean_lines:
        fields = parse_csv_line(line)

        if fields is None:
            bad_rows.append(line)
            continue

        fitted = fit_row_to_schema(fields, line, warnings)
        if fitted is None:
            bad_rows.append(line)
            warnings.append({
                "type": "row_too_few_columns",
                "expected": NUM_COLS,
                "got": len(fields),
                "raw": line[:120],
            })
            continue

        good_rows.append(fitted)

    return good_rows, bad_rows


# ---------------------------------------------------------------------------
# Row normalization
# ---------------------------------------------------------------------------

def normalize_row(fields: list, warnings: list) -> dict:
    """
    Normalize a single parsed row (list of NUM_COLS values) into a dict.
    Applies null normalization, URL cleanup, numeric cleaning, and enum validation.
    """
    d = dict(zip(CANONICAL_HEADER, fields))
    row_id = collapse_whitespace(d.get("item_name", "?") or "?")

    # Step 1: collapse whitespace on all fields
    for k in d:
        d[k] = collapse_whitespace(d[k])

    # Step 2: null-normalize all non-URL fields
    for k in d:
        if k != "url":
            d[k] = normalize_null(d[k])

    # Step 3: URL
    d["url"] = normalize_url(d["url"], warnings, row_id)

    # Step 4: numeric fields
    for field in ("price_aud", "vram_gb", "unified_memory_gb", "ram_gb"):
        d[field] = normalize_numeric(d[field], field, warnings, row_id)

    # Step 5: enum fields
    d["track"] = normalize_enum(
        d["track"], ENUM_TRACK, "track", warnings, row_id
    )
    d["category"] = normalize_enum(
        d["category"], ENUM_CATEGORY, "category", warnings, row_id
    )
    d["condition"] = normalize_enum(
        d["condition"], ENUM_CONDITION, "condition", warnings, row_id
    )
    d["au_stock_confirmed"] = normalize_enum(
        d["au_stock_confirmed"], ENUM_AU_STOCK, "au_stock_confirmed", warnings, row_id
    )
    d["verification_status"] = normalize_enum(
        d["verification_status"],
        ENUM_VERIFICATION,
        "verification_status",
        warnings,
        row_id,
        fallback="Unverified",  # default for verification is Unverified, not UNKNOWN
    )
    d["status"] = normalize_enum(
        d["status"], ENUM_STATUS, "status", warnings, row_id
    )

    return d


# ---------------------------------------------------------------------------
# Cross-field checks
# ---------------------------------------------------------------------------

def cross_field_checks(d: dict, warnings: list) -> None:
    """
    Add warnings for suspicious field combinations.
    These do not block output — they are informational flags.
    """
    row_id = d.get("item_name", "?")

    # Verified but no real evidence
    if d["verification_status"] == "Verified":
        weak_count = sum([
            d["url"] == "UNKNOWN",
            d["retailer"] == "UNKNOWN",
            d["price_aud"] == "UNKNOWN",
        ])
        if weak_count >= 2:
            warnings.append({
                "type": "suspicious_verified_no_evidence",
                "row": row_id,
                "msg": "verification_status=Verified but url/retailer/price mostly UNKNOWN",
            })

    # Out of Stock contradicts au_stock_confirmed=Yes
    if d["status"] == "Out of Stock" and d["au_stock_confirmed"] == "Yes":
        warnings.append({
            "type": "suspicious_stock_conflict",
            "row": row_id,
            "msg": "status=Out of Stock but au_stock_confirmed=Yes",
        })

    # Apple/unified-memory device — may need category review
    name_lower = d["item_name"].lower()
    if any(kw in name_lower for kw in ("apple", "mac studio", "macbook", " m4 ", " m3 ", " m2 ")):
        warnings.append({
            "type": "apple_device_detected",
            "row": row_id,
            "msg": "Apple product — verify category and unified_memory_gb vs vram_gb mapping",
        })

    # Mini PC with what looks like a discrete GPU
    if d["category"] == "Mini PC" and d["gpu_model"] not in ("UNKNOWN", ""):
        if any(kw in d["gpu_model"].upper() for kw in ("RTX ", "GTX ", " RX ")):
            warnings.append({
                "type": "mini_pc_discrete_gpu_flag",
                "row": row_id,
                "msg": "Mini PC with apparent discrete GPU — confirm if unified-memory device",
            })

    # Track1B (AMD Strix Halo) but vram_gb populated and unified_memory_gb UNKNOWN
    if d["track"] == "Track1B" and d["unified_memory_gb"] == "UNKNOWN" and d["vram_gb"] != "UNKNOWN":
        warnings.append({
            "type": "track1b_missing_unified_memory",
            "row": row_id,
            "msg": "Track1B (Strix Halo) row has vram_gb but not unified_memory_gb — check field mapping",
        })


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def dedup_rows(rows: list, warnings: list) -> list:
    """
    Deduplicate normalized rows using:
      1. URL (when valid and not UNKNOWN)
      2. Fallback: composite key of item_name + retailer + gpu_model + price_aud

    Keeps the first occurrence of each key; logs removed duplicates.
    """
    seen_urls: dict = {}
    seen_composite: dict = {}
    out = []

    for d in rows:
        url_key = d["url"] if d["url"] != "UNKNOWN" else None
        composite = (
            f'{d["item_name"].lower()}|{d["retailer"].lower()}'
            f'|{d["gpu_model"].lower()}|{d["price_aud"]}'
        )

        if url_key and url_key in seen_urls:
            warnings.append({
                "type": "duplicate_removed",
                "row": d["item_name"],
                "key_type": "url",
                "key": url_key,
            })
            continue

        if composite in seen_composite:
            warnings.append({
                "type": "duplicate_removed",
                "row": d["item_name"],
                "key_type": "composite",
                "key": composite,
            })
            continue

        if url_key:
            seen_urls[url_key] = True
        seen_composite[composite] = True
        out.append(d)

    return out


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------

def write_processed_csv(path: Path, rows: list) -> None:
    """Write normalized rows to a clean CSV."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CANONICAL_HEADER)
        writer.writeheader()
        writer.writerows(rows)


def write_manual_review_csv(path: Path, bad_rows: list) -> None:
    """Write unparseable raw lines to a manual-review CSV."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["raw_line"])
        for line in bad_rows:
            writer.writerow([line])


def write_log(path: Path, log: dict) -> None:
    """Write the normalization log as JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Normalize raw Gemini/NotebookLM hardware CSV output.\n\n"
            "Handles malformed one-line CSV, code fences, repeated headers,\n"
            "bad enums, truncated URLs, and column mismatches."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "input_file",
        help="Path to raw input file (plain text or CSV from Gemini/NotebookLM)",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        metavar="DIR",
        help=(
            "Output directory for processed files. "
            "Defaults to NotebookLM_Workspaces/intake/processed/ "
            "relative to the project root."
        ),
    )
    return parser


def resolve_out_dir(args_out_dir: str | None) -> Path:
    """Resolve the output directory, creating it if necessary."""
    if args_out_dir:
        out_dir = Path(args_out_dir).resolve()
    else:
        # Script lives at <project_root>/scripts/normalize_intake.py
        project_root = Path(__file__).parent.parent
        out_dir = project_root / "NotebookLM_Workspaces" / "intake" / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def print_summary(counts: dict, warnings: list, paths: dict) -> None:
    """Print a human-readable summary to stdout."""
    print("\n✅ Normalization complete.")
    print(f"   Input rows parsed    : {counts['parsed_good']}")
    print(f"   Sent to manual review: {counts['manual_review']}")
    print(f"   After deduplication  : {counts['after_dedup']}")
    print(f"   Duplicates removed   : {counts['duplicates_removed']}")
    print(f"   Warnings logged      : {counts['warnings_total']}")

    if warnings:
        # Summarize warning types
        type_counts: dict = {}
        for w in warnings:
            t = w.get("type", "other")
            type_counts[t] = type_counts.get(t, 0) + 1
        print("\n   Warning breakdown:")
        for wtype, cnt in sorted(type_counts.items()):
            print(f"     {cnt:3d}  {wtype}")

    print(f"\n   Processed CSV   → {paths['processed']}")
    print(f"   Manual review   → {paths['review']}")
    print(f"   Normalization log → {paths['log']}")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    input_path = Path(args.input_file).resolve()
    if not input_path.exists():
        print(f"❌  Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    out_dir = resolve_out_dir(args.out_dir)
    stem = input_path.stem

    processed_path = out_dir / f"{stem}_processed.csv"
    review_path    = out_dir / f"{stem}_manual_review.csv"
    log_path       = out_dir / f"{stem}_normalization_log.json"

    # Read
    print(f"📥 Reading: {input_path}")
    raw = input_path.read_text(encoding="utf-8", errors="replace")

    warnings: list = []

    # Parse
    good_rows, bad_rows = parse_raw_text(raw, warnings)

    if good_rows is None:
        print(
            "❌  FATAL: Could not find the canonical header in the input file.",
            file=sys.stderr,
        )
        print(
            f"   Expected a line containing: {CANONICAL_HEADER[0]},{CANONICAL_HEADER[1]},...",
            file=sys.stderr,
        )
        sys.exit(2)

    print(f"   Parsed: {len(good_rows)} rows OK, {len(bad_rows)} sent to manual review.")

    # Normalize
    normalized = []
    for row in good_rows:
        d = normalize_row(row, warnings)
        cross_field_checks(d, warnings)
        normalized.append(d)

    # Deduplicate
    before = len(normalized)
    normalized = dedup_rows(normalized, warnings)
    after = len(normalized)

    # Build counts for log
    counts = {
        "parsed_good": len(good_rows),
        "manual_review": len(bad_rows),
        "after_dedup": after,
        "duplicates_removed": before - after,
        "warnings_total": len(warnings),
    }

    # Write outputs
    write_processed_csv(processed_path, normalized)
    write_manual_review_csv(review_path, bad_rows)

    log = {
        "run_timestamp": datetime.now().isoformat(),
        "input_file": str(input_path),
        "counts": counts,
        "warnings": warnings,
    }
    write_log(log_path, log)

    print_summary(
        counts,
        warnings,
        {"processed": processed_path, "review": review_path, "log": log_path},
    )


if __name__ == "__main__":
    main()
````

## File: AGENTS.md
````markdown
# AGENTS.md — Two-Track Hardware Decision System

**Role:** Hardware-research and organisation helper inside the Antigravity IDE.
Keep decisions simple. Do NOT design the perfect system.
Browser access and web searches are permitted for verification and data gathering.

---

## TERMINOLOGY

### Tracks and Paths / Pathways
- `track` (CSV) is the high-level decision rail, usually a small integer (e.g. 1, 2).  
- `pathway` (CSV) is the specific branch within a track (e.g. "1A", "1B", "2A").  
- In prose we refer to these as “Path 1A”, “Path 1B”, etc.  
- When you see or say “Track 1A” or “Track 2B”, interpret that as:  
  - `track = 1` and `pathway = "1A"`, or  
  - `track = 2` and `pathway = "2B"`, respectively.  
- The **Track** concept is always the broader category; **Path / Pathway** is the specific branch within that Track.

### Machine vs item_name
- `item_name` is the canonical identifier in the intake and shortlist CSVs.  
- Some processing steps and reports also use a derived `Machine` label; this should always be consistent with `item_name` (optionally plus extra context, such as retailer or config suffix).  
- When referring to a “machine” in prompts or conversations, assume it refers to the underlying `item_name`, and treat `Machine` as a reporting/alias field tied back to that `item_name`.

---

## SCOPE

- **Track 1:** Active laptop purchase. One decision. GOOD ENOUGH → buy.
- **Track 2:** Active workstation/desktop research. Three pathways. Likely medium-term outcome — runs in parallel with Track 1. Do not delay Track 1 for Track 2 unless a unicorn deal is immediately available.

---

## GLOBAL CONSTRAINTS

- **Browser access permitted.** Use the **Vercel Agent Browser (`agent-browser`)** CLI as the default for web research to ensure token utilization efficiency (via compact DOM snapshots). Use headless browser instances for all scraping and verification tasks to minimize overhead.
- **Work with:** existing markdown product cards, CSVs, policy/spec docs, scripts, templates in this repo, and external web sources.
- **Unknown values:** Use `agent-browser` to search for real-world specs or prices when they are unknown. Update fields dynamically.
- **Responsibilities:**
  - Audit and sync product cards vs CSVs.
  - Create and normalise product card shells.
  - Generate and refine prompt files.
  - Rebuild the mega-bundle.
  - Apply documented patches to spec/policy docs.
  - Draft decision logs and checklists.
  - Fetch new data from the internet to complete missing details.

---

## PIPELINE AND POLICY (5-PHASE WORKFLOW)

This repository enforces a strict 5-phase execution path to go from raw web data to a mathematical purchase decision. 

**Policy Source of Truth:**
All scripts read hardware constraints (budgets, VRAM floors, soft penalty behaviors) from the machine-readable config: `config/procurement_policy.json`. Do not hard-code these limits in scripts.

1. **Phase 1: Intake & Verification** (`normalize_intake.py` + `intake_to_cards.py`)
   - Clean raw AI exports and generate markdown product cards.
2. **Phase 2: Shortlist** (`build_shortlist.py`)
   - Filter out junk (out of stock, under VRAM floor). Applies soft-penalties to over-budget items unless they qualify for an `exceptional_override`.
3. **Phase 3: Live Pricing Enrichment** (`enrich_shortlist_pricing.py`)
   - Scaffold the CSV for live pricing checks. 
   - *Agent action:* Use `scripts/prompt_templates/browser_pricing_lookup.md` in the Vercel Browser Agent to hunt down stackable coupons, student discounts, and cashback.
4. **Phase 4: Manual Scoring**
   - *Agent action:* Fill in the 0–10 score columns in the enriched CSV based on the newly discovered `effective_best_price_aud`.
5. **Phase 5: Score & Rank** (`rubric_weighting_engine.py`)
   - Run the engine with `--profile merged`. Buy the candidate that ranks #1 and hits `[GOOD ENOUGH]`.

---

## TRACK 1 — CHASSIS SCOPE AND BUDGET

Track 1 has **two hardware paths**: NVIDIA discrete GPU laptops and AMD unified-memory laptops.
Both paths are active simultaneously.

> **Principle:** The smaller the screen size, the more critical a Track 2 solution becomes.
> A 13" device at a strong price is a valid Track 1 candidate, but it explicitly increases
> urgency to resolve Track 2.

---

### Path 1A — NVIDIA Discrete GPU Laptops

#### Screen Size
- **Floor:** 13" minimum.
- **Primary target:** 17–18" (scoring bonus applies — see Scoring section).
- **Intermediate sizes (14–16"):** In scope; evaluated on VRAM, build quality, and resale value.

#### VRAM
- **Minimum:** 8 GB VRAM.
- **Preferred:** 12 GB or higher (16 GB - 24 GB optimal for larger LLMs).
- A 12 GB+ card at 17–18" = standard eligible candidate.
- An 8 GB card = requires significant offsetting strengths (build quality, price, resale) to remain competitive for LLM workloads.

#### Brands and Families in Scope

**LENOVO**
- Legion 9i
- Legion Pro 9i
- Legion Pro 7i (current high-end variants meeting VRAM and budget rules)

**ASUS**
- ROG Strix Scar 17
- ROG Strix Scar 18
- Any ROG model at 13"+ meeting the 8 GB VRAM floor

**MSI**
Any current 13"+ high-end RTX gaming/workstation model meeting VRAM and price constraints, including:
- MSI Raider 17/18
- MSI Titan 17/18
- MSI Stealth 16/17/18
- MSI Vector 16/17/18
- Other MSI 13"+ models with ≥ 8 GB VRAM


#### AMD Discrete GPU Laptops
AMD discrete GPU laptops evaluate under same rules as NVIDIA:
- HP OMEN Max (Ryzen AI 9 HX 375 + RTX 5070/5090)
- Tag as: architecture:discrete_gpu_amd, track_eligibility:track_1_nvidia_path
- Move cards from Strix_Halo_AMD/ to Gaming_Laptops_AMD_Discrete/
- Apply ≥8 GB VRAM floor, 16"+ screen size

#### Exclusions (Path 1A)
- Any laptop with less than 13" screen size.
- Any laptop with less than 8 GB discrete VRAM.
- Any brand/model family outside the three listed above, unless explicitly expanded.

#### Lenovo Legion Pro 7i vs 9i / Pro 9i Value Rule
- At the same price or within < 300 AUD difference: **prefer Legion 9i / Pro 9i over Pro 7i.**
- **Prefer Pro 7i** if it is ≥ 300–500 AUD cheaper than a comparable 9i/Pro 9i, while still meeting
  VRAM requirements, decent thermals, and upgradeability targets (32–64 GB RAM, ≥ 2 TB SSD).
- Pro 7i = "discount premium" tier, not equal to 9i/Pro 9i at the same price.

---

### Path 1B — AMD Strix Halo Unified Memory Laptops

#### Screen Size
- **No minimum screen size.** 13-14" devices are valid Track 1 candidates BUT trigger immediate Track 2 urgency (portable device requires desktop companion for extended work).
- 17–18" scoring bonus applies equally to this path.

#### Unified Memory
- **Minimum:** 16 GB (≈ equivalent to 8 GB discrete VRAM in GPU-accessible terms, given ~60–75%
  allocation to GPU workloads).
- **Preferred:** 64 GB.
- **Optimal:** 96–128 GB.

#### SoC Requirement
- Must use AMD Strix Halo (Ryzen AI Max / Ryzen AI Max+) or architecturally equivalent
  unified-memory SoC.
- Standard Ryzen with discrete dGPU does NOT qualify for this path.

#### Brands and Families in Scope
AMD Strix Halo laptops (any brand):
- ASUS TUF Gaming A14 (2026) FA401EA — 32 GB unified, 14"
- ASUS ProArt PX13 (Strix Halo variant) — 128 GB unified, 13.3"
- ASUS ROG Flow Z13 GZ302EA — check unified memory config, 13.4"
- Lenovo Legion 7a Gen 11 — if AU stock confirmed (not yet available)

> **ProArt PX13 Note:** ProArt PX13 retail (~$6,000 AUD) exceeds budget. ONLY pursue if refurbished/open-box/sale pricing ≤$4,500 AUD. Check: Officeworks, Harvey Norman, JB Hi-Fi, ASUS AU Outlet.

#### Exclusions (Path 1B)
- ASUS TUF A16: NO Strix Halo variant exists (discrete GPU only)
- ASUS ROG Zephyrus G16: NO Strix Halo variant exists (discrete GPU only)
- HP OMEN Max: Uses Strix Point (discrete GPU), NOT Strix Halo
- Any AMD device with < 16 GB unified memory.
- Any AMD device using a non-unified architecture (discrete dGPU with standard Ryzen iGPU).
- Apple Silicon (separate category, currently deferred).

---

### Track 1 — Price Band

- **Total budget range (AUD):** 0–4,500
- **Preferred sweet spot (AUD):** 2,500–4,000
- Only consider 4,000–4,500 AUD if: GPU/unified memory is top-tier, build quality and thermals are
  clearly superior, and there is a strong resale story.

### Track 1 — Scoring Bonuses and Flags

- **+Bonus:** Screen size 17–18" (applies to both Path 1A and 1B).
- **+Bonus:** Top-tier memory for path — 24 GB discrete (1A) or 96–128 GB unified (1B).
- **−Competitive penalty:** Screen size < 15" with no offsetting Track 2 plan resolved.
- **⚠ Flag:** Thermal concerns (sustained throttling under sustained GPU load).
- **⚠ Flag (Path 1B only):** Known ROCm software compatibility gaps for target workloads.

---

## TRACK 1 — AGENT RESPONSIBILITIES (REPO-ONLY)

- Audit `laptop_candidates.csv` against `04_Laptops_Mainline/*.md`:
  - Map every CSV row to a card file (or flag "NO CARD EXISTS").
  - Map every card file to a CSV row (or flag "NOT IN CSV").
  - Flag UNKNOWN / placeholder fields.
- For missing candidates within allowed scope: create BLANK product card shells using
  `template_product_card_output.md` with all spec fields set to UNKNOWN.
- Produce a "data-ready checklist" — a markdown table of all fields requiring web lookup, and use the browser agent to fill them.
- Actively attempt to fill UNKNOWN fields using the internet.

---

## GOOD ENOUGH STOP CONDITION (Track 1)

Mark a candidate as **"GOOD ENOUGH — STOP SEARCHING"** when ALL of the following are confirmed:

**Path 1A (NVIDIA):**
- In stock in AU from a credible retailer.
- ≥ 8 GB VRAM (12 GB+ preferred; RTX 4080/4090/5080/5090 optimal).
- Supports at least 32–64 GB RAM (installed or clearly upgradable).
- At least 2 TB SSD (installed or clearly upgradable).
- Price within the 0–4,000 AUD budget.
- No disqualifying thermal flag.

**Path 1B (AMD Strix Halo):**
- In stock in AU from a credible retailer.
- Confirmed Strix Halo SoC.
- ≥ 16 GB unified memory (32 GB+ preferred).
- Price within the 0–4,000 AUD budget.
- No disqualifying thermal flag.
- No disqualifying ROCm software compatibility gap for target workloads.

Do NOT expand scope beyond the listed families/SoC requirements unless explicitly instructed.

---

---

## TRACK 1.5 — REFURBISHED GAMING DESKTOP (SINGLE GPU)

**Definition:** Refurbished or open-box gaming desktops (OEM chassis) with single high-VRAM GPU. Evaluated as laptop alternatives when price/performance ratio is compelling.

**Scope:** Pre-built gaming towers from major OEMs. NOT custom builds (see Track 2 Pathway A).

**Brands in scope:**
- Alienware Aurora (R11, R12, R13, R14, R15, R16 series)
- Acer Predator Orion
- HP OMEN 45L/40L/30L
- ASUS ROG Strix GA15/GA35
- Lenovo Legion Tower (5i/7i series)

**GPU Requirements:**
- Minimum 8 GB VRAM (same as Track 1 NVIDIA path)
- Target: RTX 3090 (24 GB), RTX 4080/4090, or equivalent

**Age Limit:** Maximum 6 years old (≥ 2020 manufacture date)

**Price Threshold (CRITICAL):**
Must beat equivalent Track 1 laptop on price/performance:
- [ ] Desktop ≤ 85% cost of comparable laptop (accounting for loss of portability)
- [ ] OR desktop offers ≥ 50% more VRAM at same price point

Example: Alienware R12 with RTX 3090 (24 GB) @ $2,500 AUD beats TUF A14 (32 GB unified ≈ 16 GB GPU-available) @ $3,499 AUD.

**Go/No-Go Gates:**
- [ ] Chassis ≥ 2020 (confirm manufacture date or CPU generation)
- [ ] GPU confirmed ≥ 8 GB VRAM
- [ ] PSU wattage confirmed sufficient for installed GPU (or upgradable)
- [ ] Price threshold test passed (see above)
- [ ] AU stock/listing confirmed at credible seller
- [ ] Warranty ≥ 3 months (refurb) or ACL coverage (retailer sold)
- [ ] No disqualifying proprietary parts flag (Dell/Alienware: check PSU/mobo upgradeability)

**Candidate Prioritization:**
1. RTX 3090 chassis (best VRAM/$)
2. RTX 4090 chassis (if steep discount)
3. Multi-GPU capable (even if sold with single GPU — future Track 2 Pathway B conversion)

**Agent Responsibilities:**
- Maintain cards in `Desktop_Gaming_Refurbished/` folder
- For each card: confirm age, GPU VRAM, PSU spec, price/performance vs Track 1
- Use web searches to resolve UNKNOWN fields for: exact manufacture date, PSU wattage, warranty terms
- You may add new cards from web searches if they meet the criteria

**Exclusions:**
- Custom/SI builds (those go to Track 2 Pathway A)
- Desktops with <8 GB VRAM
- Pre-2020 platforms (thermal/efficiency penalty too high)

## TRACK 2 — WORKSTATION (ACTIVE — THREE PATHWAYS)

Track 2 is **active now** and runs in parallel with Track 1.
It is likely a **medium-term** outcome.

> **Do not delay Track 1 for Track 2.** Unless a Pathway A, B, or C candidate with immediate
> AU availability and strong pricing is identified, Track 1 remains the priority purchase.
> Track 2 resolves on its own timeline.

---

### Pathway A — AU System Integrator Custom/Configurable Build

**Definition:** A system ordered from an AU-based system integrator in a custom or
"ready-to-run" configuration. Examples: Scorptec, Mwave, Centre.com. This is NOT a
DIY self-sourced parts build.

**Go/No-Go Gates (ALL must pass before any action is taken):**
- [ ] Confirmed build spec exists in repo at `01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md`
      (CPU, motherboard, RAM, PSU, GPU, case — all named, no UNKNOWN fields).
- [ ] Target GPU(s) availability in AU market confirmed (flag UNKNOWN until manually verified).
- [ ] Build spec confirmed to support target GPU(s): PCIe slots, lane allocation, PSU wattage,
      physical clearance.
- [ ] Total cost (build + GPUs) within AUD budget.

**CPU Platform (LOCKED):**
AMD Threadripper PRO 5000WX (WRX80 chipset)
- 128 PCIe Gen 4 lanes (supports RTX 3090 × 2 + NVMe without bottleneck)
- Better AU availability than Intel Xeon W-3400
- Compatible motherboards: ASUS Pro WS WRX80E-SAGE, ASRock WRX80 Creator

**GPU Target:**
RTX 3090 × 2 (24 GB VRAM each = 48 GB total)
- AU used market estimate: $1,500-1,800 AUD per card (Gumtree, eBay AU)
- Flag as UNKNOWN until manual verification at time of build decision

**Next Steps:**
Create `track2_pathway_a_build_spec.md` with confirmed components:
- CPU: Threadripper PRO 5955WX or 5975WX
- Motherboard: (specific model TBD)
- RAM: 128 GB DDR4 ECC (minimum)
- PSU: 1600W+ 80+ Platinum (dual GPU headroom)
- Case: (TBD — must fit dual 3-slot GPUs)

**Agent Responsibilities:**
- Maintain confirmed build spec at `01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md`.
- Use the browser agent to look up UNKNOWN fields (prices, stock) from integrator websites.
- You may browse integrator websites to confirm specs and prices.

---

### Pathway B — Refurbished Enterprise Workstation

**Definition:** A pre-owned enterprise-class tower or rack workstation (e.g., Dell Precision,
HP Z-series, Lenovo ThinkStation) that arrives with 1× or 2× compatible GPU already installed,
or has confirmed empty PCIe slot(s) and PSU headroom to accept target GPU(s).

**Age Limit:** Maximum 8 years old (manufactured ≥ 2018).

**Go/No-Go Gates (ALL must pass before any action is taken):**
- [ ] Chassis manufacture date confirmed ≥ 2018 (flag UNKNOWN if not stated on card).
- [ ] PCIe slot count and lane allocation confirmed for target GPU configuration.
- [ ] PSU wattage confirmed sufficient for GPU(s), or PSU upgrade confirmed possible and costed.
- [ ] GPU(s) confirmed ≥ 8 GB VRAM per card — either pre-installed or separately available in
      AU used/refurbished market.
- [ ] Total cost (unit + any GPU additions) within AUD budget.
- [ ] No disqualifying thermal flag (inadequate airflow for dual-GPU sustained load).
- [ ] No ECC-only memory constraint that would prevent standard GPU driver operation.

**GPU Rules:** Same as Pathway A — 8 GB VRAM minimum per GPU, any make/model.

**Agent Responsibilities:**
- Existing cards in `02_Refurbished_Desktop_Towers/` are the primary candidates.
- For each card: verify age, PCIe slot spec, PSU spec, GPU compatibility. Flag UNKNOWN for any
  missing field.
- Flag for review: Dell Precision 5820 bundle ($3,558 includes ThinkPad T14s) — find unbundled tower-only price or mark "bundle only".
- You may add new candidates from the internet.

---

### Pathway C — Unified Memory Mini PC

**Definition:** A compact/mini PC using AMD Strix Halo (Ryzen AI Max / Ryzen AI Max+) or
architecturally equivalent high-bandwidth unified-memory SoC, where system RAM is simultaneously
GPU VRAM.

**Unified Memory Floor:** 32 GB minimum. 64–128 GB preferred.

**Go/No-Go Gates (ALL must pass before any action is taken):**
- [ ] Device confirmed to use a unified-memory SoC (Strix Halo or equivalent — not a standard
      iGPU + discrete GPU combo).
- [ ] Unified memory ≥ 32 GB confirmed from spec sheet (not estimated).
- [ ] AU stock confirmed at credible retailer.
- [ ] Price within AUD budget.
- [ ] No disqualifying thermal flag (passive-only or inadequate cooling for sustained inference
      workloads is a flag).
- [ ] No disqualifying ROCm software compatibility gap for target workloads.
- [ ] If refurbished/open-box: Minimum 3-month seller warranty or ACL coverage confirmed
- [ ] If refurbished/open-box: Condition grade disclosed (Grade A/B acceptable; C/D flagged for manual review)

**Confirmed AU Stock Candidates:**
- Minisforum AI X1 Pro (Ryzen AI Max+ 370/470, up to 128 GB unified)
  - AU retailers: au.minisforum.com, MegaTechStore AU
  - Pricing: Quote required
  - Status: ✅ Confirmed in stock

**Priority Research Targets (UNKNOWN — manual verification required):**
- HP Z2 Mini G1a (Strix Halo variant, if exists)
- HP Elite Mini 800 G11 AI (Strix Halo variant, if exists)
- Any HP workstation mini PC with Ryzen AI Max/Max+
- Prioritize refurbished/open-box from: HP AU Refurbished Store, Scorptec, Mwave, eBay AU enterprise sellers

**Excluded:**
- ASUS NUC 14 Pro AI (Intel Core Ultra, NOT Strix Halo)

**Agent Responsibilities:**
- Maintain candidate cards in `06_Mini_PCs_and_eGPU/` (existing lane).
- For each candidate: confirm SoC model, unified memory config, AU availability. Use the internet to resolve UNKNOWN fields.
- You may add new candidates from the internet.

---

## TRACK 2 — AGENT RESPONSIBILITIES (REPO-ONLY)

- **Pathway A:** Maintain and update `01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md`.
- **Pathway B:** Audit `02_Refurbished_Desktop_Towers/*.md` cards against all gate conditions.
- **Pathway C:** Audit and/or create candidate shells in `06_Mini_PCs_and_eGPU/`.
- Produce a unified Track 2 data-ready checklist: a markdown table of all UNKNOWN fields across
  all three pathways requiring verification, and use the browser to fill them before gates can be cleared.
- Actively use the internet to resolve and fill UNKNOWN fields.

---

## SCORING RUBRIC CHEATSHEET (VRAM, PRICE/PERF, ETC.)

**VRAM_Adequacy (0–10)**  
- 0 = Below hard minimum VRAM for the target workload in this Track/Path.  
- 5 = Meets the minimum VRAM requirement, but with little headroom.  
- 10 = Meets or exceeds the “ideal” VRAM tier defined for this Track/Path (comfortable headroom).  
- Example:  
  - For a Track 1A GPU workload where the minimum is 16 GB and the ideal is 24 GB:  
    - 8 GB → 0  
    - 16 GB → ~5  
    - 24 GB or more → 9–10

**Price_to_Perf (0–10)**  
- 0 = Clearly poor value for money vs alternatives in the same Track/Path.  
- 5 = Acceptable value (roughly average) for this segment.  
- 10 = Excellent value (significantly better price/performance than typical options for this Track/Path).  
- Use the same formula or comparison logic implemented in `rubric_weighting_engine.py`, but this section documents the intent in plain language.

**Value_Score (0–10)**  
- Aggregated view of cost vs capability for the intended workload.  
- 0 = Fails either capability or cost constraints badly.  
- 5 = Meets both capability and cost constraints at baseline.  
- 10 = Strongly meets or exceeds capability while staying comfortably within budget.

**Condition_Risk (0–10)**  
- 0 = Extremely high risk (e.g. unknown vendor, no warranty, poor condition).  
- 5 = Acceptable risk (standard refurb or used, clear but limited warranty).  
- 10 = Minimal risk (new or near-new from trusted vendor, strong warranty).

**Verification_Confidence (0–10)**  
- 0 = Almost nothing verified; key specs uncertain.  
- 5 = Most important specs have at least one independent verification.  
- 10 = All critical specs and price are cross-verified and documented.

**Sustained_TGP_Rating (0–10)**  
- 0 = Clear thermal/Power-limit issues vs workload expectations.  
- 5 = Meets baseline TGP and thermal headroom for the expected workloads.  
- 10 = Excellent sustained TGP/thermals for long-running workloads in this Track/Path.

**Portability_Score (0–10)**  
- 0 = Not reasonably portable for the intended use (very heavy, bulky, low battery if relevant).  
- 5 = Acceptably portable (within stated thresholds for weight, size, battery).  
- 10 = Very portable while still meeting capability requirements.

These are **interpretive guardrails** for humans and LLMs. The exact formulas and thresholds live in `rubric_weighting_engine.py`, but this section documents the intent, so scorers apply the rubric consistently.
````
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/HOW_TO_MAINTAIN_RUBRIC.md
`````markdown
# How to Maintain the Rubric Pipeline

This guide is for "future you" — written assuming you haven't touched this in weeks.

---

## Quick-start commands

```bash
# From: NotebookLM_Workspaces/Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/

# Full ranking run with whitening details, gate results, and old-vs-new diff:
python3 rubric_weighting_engine.py

# Interactive pairwise review + redundancy check:
python3 ranking_feedback_loop.py
```

---

## How the scoring pipeline works (top to bottom)

```
candidates_scores.csv
        ↓
[1] HARD-FAIL GATE     Second_x16_Usability == 0  →  [HARD FAIL] flag, score capped at 38/100
        ↓
[2] SOFT EXPANSION GATE  avg(Second_x16, Chassis_2nd_GPU, PSU_Wattage_Ceiling) < 6.0
                         →  zero Price_per_GB_VRAM, Warranty_Coverage, Enterprise_Pedigree
        ↓
[3] WHITENING          Sigma estimated on ELIGIBLE rows only
                       (gate PASS + not NeverBuy)
        ↓
[4] MANUAL OVERRIDES   VRAM ≥ 18%, Second_x16 ≥ 8%, PSU_Ceiling ≥ 5%
        ↓
[5] SCORING
        Old_Score    = equal weights × raw scores  (baseline)
        PreGate_Score = final weights × raw scores  (weight effect only)
        PostGate_Score = final weights × gated scores + hard-fail cap  (actual rank)
        Gate_Cost    = PostGate - PreGate  (negative = gate penalty)
```

---

## Key design decisions (what changed and why)

| What | How it works |
|---|---|
| **Expandability gate** | If a machine's avg(`Second_x16_Usability`, `Chassis_2nd_GPU`, `PSU_Wattage_Ceiling`) < 6.0, its `Price_per_GB_VRAM`, `Warranty_Coverage`, and `Enterprise_Pedigree` scores are **zeroed before scoring**. A great deal on a non-expandable machine can't rescue its rank. |
| **Whitening method** | Follows RRD paper §4: standardise columns → estimate Σ → regularise Σ_λ = Σ + λI → compute Σ_λ^{-1/2} via eigen-decomp → weights ∝ row sums of Σ_λ^{-1/2}. This down-weights clusters of correlated metrics so they don't dominate collectively. |
| **Manual overrides** | Applied **before** whitening distributes the remainder. VRAM ≥ 18%, `Second_x16_Usability` ≥ 8%, `PSU_Wattage_Ceiling` ≥ 5%. These represent your non-negotiable buying priorities. |
| **Misalignment filter** | Pairwise NeverBuy-vs-Preferred per criterion. Only flags SUSPECT (> 50% of pairs go the wrong way). Does not auto-invert — you decide. |
| **Contribution math** | Points shown in the diff are `raw_score × final_weight × 10` so they sum to the displayed New_Score. |

---

## 1. Adding a new "Never Buy" example

Open `rubric_weighting_engine.py`, find `NEVER_BUY_MACHINES`, add the machine name exactly as it appears in `candidates_scores.csv`:

```python
NEVER_BUY_MACHINES = [
    "PLE_RTX5070Ti_16GB_Desktop",
    "My_New_Bad_Machine",   # <-- add here
]
```

Then re-run: `python3 rubric_weighting_engine.py`

---

## 2. Adding a new candidate machine

Add a row to `candidates_scores.csv`. Score each criterion 0–10 using the scale in `policy_expandable_workstation_scoring.md`. Set `Type` to `Preferred`, `NeverBuy`, `Borderline`, or `Special`.

```
NewMachine,Preferred,8,8,7,8,8,8,7,8,8,8,9,9,8,9,5,2
```

Re-run `python3 rubric_weighting_engine.py`. The covariance matrix will be re-estimated with the new data point.

---

## 3. Reviewing SUSPECT vs CONFIRMED misalignment

The engine prints two buckets at the start of every run:

- **SUSPECT** — criterion rewards NeverBuy machines more than Preferred > 50% of the time. **Do not auto-invert.** Ask: "Is this criterion just overweighted, or genuinely measuring the wrong thing?"
  - If **overweighted**: leave it, rely on whitening + manual overrides to dampen it.
  - If **genuinely wrong**: edit the 0–10 scale in the policy markdown, or delete it from the CSV entirely.
- **CONFIRMED** — you've already decided to suppress it. Add it to `CONFIRMED_MISALIGNED_COLS` in the script (currently none).

---

## 4. Adjusting manual weight overrides

Edit `MANUAL_MIN_WEIGHTS` in `rubric_weighting_engine.py`:

```python
MANUAL_MIN_WEIGHTS = {
    "VRAM_Adequacy":        0.25,   # bump from 18% → 25%
    "Second_x16_Usability": 0.10,   # bump from 8% → 10%
    "PSU_Wattage_Ceiling":  0.05,
}
```

The remaining weight pool (1 − sum of overrides) is automatically redistributed via whitening. Re-run to see the new weight vector and ranking diff.

---

## 5. Adjusting the expandability gate

Edit two constants in `rubric_weighting_engine.py`:

```python
EXPANSION_GROUP_COLS      = ["Second_x16_Usability", "Chassis_2nd_GPU", "PSU_Wattage_Ceiling"]
EXPANSION_FLOOR_THRESHOLD = 6.0   # raise to 7.0 to be stricter
GATED_BEHIND_EXPANSION    = ["Price_per_GB_VRAM", "Warranty_Coverage", "Enterprise_Pedigree"]
```

Raising the threshold makes the gate stricter (more machines fail). Lowering it relaxes it. You can also add/remove criteria from `GATED_BEHIND_EXPANSION`.

---

## 6. Adding or removing a rubric criterion

1. Edit the table in `policy_expandable_workstation_scoring.md` (add the new row with its 0–10 scale).
2. Add the same column name to every row in `candidates_scores.csv`.
3. Update `template_product_card_output.md` so NotebookLM extracts the new score.
4. Re-run `python3 rubric_weighting_engine.py`.

**Before adding**: run `python3 ranking_feedback_loop.py` first — it will warn you if a new criterion would be > 0.9 correlated with an existing one. If so, adjust weights instead.

---

## 7. Understanding the whitening parameters

| Parameter | Location | Effect |
|---|---|---|
| `LAMBDA_REG = 0.1` | `rubric_weighting_engine.py` | Regularisation strength. Increase (e.g. 0.3) if weights look noisy or if eigenvalues are very small. |
| `MIN_SAMPLE_SIZE = 8` | `rubric_weighting_engine.py` | Below this, the engine skips whitening and uses equal weights. Add more candidate rows to unlock. |

The eigenvalues printed during each run tell you how spread out the variance is. A large dominant eigenvalue (e.g. 9.4 vs 0.1) means one dimension dominates the raw scores — whitening pulls that dimension's weight back down.
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/policy_expandable_workstation_scoring.md
`````markdown
# Policy – Expandable Workstation Scoring

## Goal

Identify refurbished desktops, workstation towers, and selected boutique prebuilts that make excellent expandable AI / GPU workstations, not just good single-GPU gaming PCs.

The primary target is:

> **24GB+ usable NVIDIA VRAM now, or a tower/workstation platform that can grow toward multiple GPUs and 48GB+ total VRAM.**

16GB VRAM systems are not the central target. They may be scored only as discounted value exceptions, temporary compromise systems, or comparative benchmarks.

## Non-Negotiable Filters

### Form Factor

Prefer:
- Full tower, mid tower, full ATX, E-ATX, enterprise tower, workstation tower.
- Dell Precision tower-class systems.
- HP Z-series tower-class systems.
- Threadripper, Xeon, Ryzen 9, Core i9, workstation-class platforms.

Reject or heavily penalise:
- SFF / USDT / mini desktops unless they clearly support full-length GPUs and adequate PSU.
- Compact proprietary gaming cases with poor airflow unless price is unusually strong.
- Towers with no clear GPU clearance or no PSU details.

### PSU

Minimum baseline:
- 850W only for single 24GB GPU systems.
- 1000W–1300W preferred for future dual-GPU growth.
- 80+ Gold or better preferred.
- Must have enough safe PCIe power connectors for the current GPU and plausible future GPU.

For dual-GPU growth:
- Estimate CPU + GPU sustained load.
- Add transient-spike allowance.
- Aim for at least 30% headroom over worst-case sustained draw.
- Penalise unknown PSU brand/model/wattage.
- Penalise proprietary PSUs unless replacement modules and GPU cables are available.

### PCIe Slots and Lanes

Minimum:
- At least one full-length x16 physical slot.

Preferred:
- Two full-length PCIe x16 physical slots.
- x8/x8 electrical support or better for dual GPU.
- Slot spacing suitable for two 2-slot blower cards or two modern 3-slot cards.
- Additional PCIe slots for NIC, capture card, HBA, RAID, or future expansion.

Penalise:
- Unknown motherboard layout.
- Second slot physically blocked by GPU, PSU shroud, drive cage, or case layout.
- Consumer boards where second x16 slot is only x4 and shares lanes in unclear ways.
- No documentation of PCIe slot layout.

### Power Connectors

Verify:
- 8-pin / dual 8-pin / triple 8-pin / 12VHPWR / 12V-2x6 support.
- Native connectors are preferred.
- Safe manufacturer-approved adapters are acceptable only if PSU quality and connector load are credible.
- Avoid questionable daisy-chain PCIe power cabling for high-power GPUs.

### Cooling

Minimum:
- Clear front-to-back airflow path.
- At least two intake and one exhaust fan positions for high-power GPU use.
- CPU cooler adequate for target CPU sustained power.
- GPU intake/exhaust not blocked by solid panels or drive cages.

Preferred:
- Enterprise high-static-pressure airflow.
- Blower-style GPUs for dense dual-GPU setups.
- Large mesh front or workstation ducting.
- Clear thermal path for second GPU.

Penalise:
- Glass-box aesthetics with weak intake.
- Compact cases with one high-power open-air GPU already heat-soaked.
- Unknown fan layout.
- Laptop-style or proprietary cooling in desktop cases.

### Case Clearance

Minimum:
- Must fit modern full-length GPU.
- Target GPU clearance: 320mm+ preferred.
- For future cards, prefer clearance for 3-slot GPUs unless explicitly using blower/workstation 2-slot cards.

Penalise:
- Unknown clearance.
- Drive cages blocking GPU length.
- Case only suitable for one large GPU.
- No room between GPUs for airflow.

### RAM

Minimum:
- 32GB installed for serious use.
- 64GB preferred.
- Must support at least 128GB for growth-platform scoring.
- ECC support is a bonus for enterprise/workstation platforms.

Penalise:
- 16GB RAM on a high-end GPU system unless upgrade is cheap and straightforward.
- Soldered or limited RAM.
- Unknown RAM slot count.

### Storage

Minimum:
- At least one NVMe SSD.
- 1TB minimum; 2TB preferred.

Preferred:
- Two or more M.2 slots.
- SATA bays for bulk model/data storage.
- Easy drive access.

Penalise:
- Unknown storage expansion.
- Single small SSD with no expansion details.

### Reliability

Reward:
- Enterprise/workstation platforms.
- Known OEM workstation families.
- ECC RAM support.
- Local warranty.
- Refurbishers with clear return policies.
- Mature platforms with stable BIOS/chipset support.

Penalise:
- Unknown motherboard.
- Unknown PSU.
- No warranty.
- Seller avoids basic technical questions.
- Non-transferable warranty.

## Synergy Rules

### CPU ↔ GPU Balance

Avoid pairing ultra-high-end GPUs with very weak CPUs unless the workload is clearly GPU-bound inference and the price is compelling.

Score higher when:
- CPU has enough cores/threads for data prep, dev workloads, multitasking, and model serving.
- Platform has enough PCIe lanes for GPU + NVMe + expansion.
- CPU generation is not so old that platform stability, driver support, or general responsiveness suffers.

### PSU ↔ GPU(s) ↔ CPU

Always estimate:
- CPU sustained power.
- GPU sustained power.
- Future second-GPU power.
- Transient spike risk.
- Connector availability.

Score lower if a build technically works today but needs a PSU replacement before the intended second GPU.

### Cooling ↔ Case ↔ Workload

AI inference/image generation can run sustained high GPU load.

Score higher for:
- Airflow-first cases.
- Workstation ducts.
- Blower cards in dense multi-GPU platforms.
- Conservative thermals over RGB aesthetics.

Score lower for:
- Compact cases.
- Poor intake.
- Hot-running open-air GPUs stacked together.
- Unknown fan layout.

### Platform ↔ Upgrade Path

Reward systems that can accept:
- More RAM.
- More NVMe/SATA storage.
- Second GPU.
- Higher-TDP CPU.
- Standard ATX PSU replacement.
- Standard case/fan upgrades.

Penalise systems that require a total rebuild to reach the stated target.

## Scoring Rubric (Atomic Dimensions)

Evaluate each candidate on the following atomic dimensions. Score each out of 10 points based on the facts provided in the listing.

| Category / UX Grouping | Subcriterion | Scale (0-10) Guidelines |
|---|---|---|
| **Workload Fit** | `VRAM Adequacy` | 10: 48GB+, 8: 24GB, 5: 16GB, 0: <16GB |
| | `GPU Compute Tier` | 10: RTX 4090/A6000, 8: RTX 3090, 6: RTX 4080/5070Ti |
| | `CPU Multi-core Sustained` | 10: High-end Threadripper/Xeon W, 8: Modern i9/R9, 5: i7/R7 |
| | `System RAM Capacity` | 10: 128GB+, 8: 64GB, 5: 32GB, 0: <32GB |
| **Component Synergy** | `PSU Headroom for Current GPU` | 10: 30%+ headroom over spikes, 5: adequate, 0: unsafe/unknown |
| | `CPU/GPU PCIe Bottleneck Risk` | 10: Full x16 Gen4+, 5: Shared lanes/older Gen, 0: Severe bottleneck |
| **Compatibility** | `PCIe Slot Layout Clarity` | 10: Full motherboard diagram/specs, 5: Text description only, 0: Unknown |
| | `PSU Connector Availability` | 10: Native cables listed, 5: Adapters needed, 0: Unknown cables |
| **Thermals/Noise** | `Intake Airflow Volume` | 10: High static pressure/mesh, 5: Standard airflow, 0: Solid glass/blocked |
| | `Sustained Thermal Stability` | 10: Blower/workstation layout, 5: Standard open-air, 0: Compact case |
| **Upgrade Path** | `Second PCIe x16 Slot Usability` | 10: True x16/x8 clear, 5: Shared x4/partially blocked, 0: None/blocked |
| | `Chassis Clearance for 2nd GPU` | 10: 320mm+ with spacing, 5: Tight but possible, 0: No room |
| | `PSU Wattage Ceiling` | 10: 1200W+ (Multi-GPU ready), 8: 1000W, 5: 850W, 0: Proprietary <800W |
| **Value/Reliability** | `Price per GB VRAM` | 10: Excellent value (<$150/GB), 5: Average, 0: Very expensive |
| | `Enterprise Pedigree` | 10: Dell Precision/HP Z, 5: Quality custom, 0: Unknown OEM/cheap prebuilt |
| | `Warranty Coverage` | 10: 3yr+ Onsite, 8: 1yr Return, 0: No warranty |

*Note: Final weighting will be handled by external correlation-aware aggregation.*

## Hard Scoring Rules

- Never score a machine as **Strong buy** if PSU model, motherboard layout, or case clearance are completely unknown.
- If PSU wattage is unknown, compatibility confidence is capped at 7/15.
- If motherboard PCIe layout is unknown, upgrade path is capped at 5/10.
- If case clearance is unknown, thermals/noise is capped at 6/10.
- If GPU VRAM is below 24GB, workload fit is capped unless the listing is a value exception.
- If the system cannot plausibly support a future second GPU, it cannot be classified as a Growth Platform.
- If a listing hides too many technical details, use **Conditional buy** or **Not recommended**, not **Strong buy**.

## Recommendation Labels

Use exactly one:

- **Strong buy**: Strong current capability, clear specs, strong value, and no critical unknowns.
- **Conditional buy (if X)**: Good candidate but depends on verifying PSU, motherboard, warranty, clearance, or price.
- **Niche buy**: Useful for a specific scenario but not broadly recommended.
- **Not recommended for expandable AI workstation**: Fails expansion, value, thermals, or critical-spec confidence.
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/prompt_notebooklm_executor.md
`````markdown
# Prompt – NotebookLM Executor for Product Listings

Use this prompt inside a NotebookLM notebook after uploading:

- `Policy – Expandable Workstation Scoring`
- `Template – Product Card Output`
- Product listing sources

```text
Using the sources “Policy – Expandable Workstation Scoring” and “Template – Product Card Output” plus the product listing sources in this notebook:

1. For each candidate desktop, extract all available spec details relevant to PSU, motherboard, RAM, storage, case, cooling, and GPU support.
2. Apply the policy scoring rubric exactly as written, explicitly penalising uncertainty where the listing hides or omits critical facts.
3. Produce one product card per candidate using the exact Markdown structure from the template source. Do not add extra sections. Do not omit headings.
4. In “Rejected or risky points”, clearly state any reasons this machine is a bad fit for multi-GPU or high-TDP workloads, even if it looks good as a normal gaming PC.
5. If a listing lacks enough information to score safely, say so in the compatibility confidence line and avoid “Strong buy”. Use “Conditional buy” or “Not recommended for expandable AI workstation”.
6. Prioritise 24GB+ usable NVIDIA VRAM now, or platforms that can grow toward multiple GPUs and 48GB+ total VRAM. Do not over-rank 16GB VRAM systems unless price is unusually compelling.
7. Penalise builds that technically work now but leave no PSU, PCIe, storage, cooling, or chassis room for future GPU expansion.

Start with these listings:
[Paste listing names / source names / URLs here]

When finished, briefly compare the cards and label the single best candidate for expandable AI workstation use, not generic gaming.
```
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/prompt_synergy_config_advisor.md
`````markdown
# Prompt – Cohesive Spec Configuration Advisor

Use this prompt when you want NotebookLM to suggest a better target configuration rather than merely score listings.

```text
Using the uploaded policy, product cards, and listing sources, propose the most cohesive target configuration for an expandable AI workstation.

Do not simply choose the highest GPU model. Design the system around component synergy.

Target:
- 24GB+ usable NVIDIA VRAM now.
- Future path toward multiple GPUs and 48GB+ total VRAM.
- Stable long-running local LLM and image-generation workloads.
- Australian availability and realistic refurb/prebuilt purchasing.

For the recommended configuration, specify:
1. GPU target:
   - Current GPU
   - Future second GPU path
   - Preferred blower/open-air type
2. CPU target:
   - Minimum acceptable CPU
   - Preferred CPU class
   - Why it balances the GPU workload
3. Motherboard/platform:
   - Required PCIe slots
   - Electrical lane requirements
   - RAM ceiling
   - Storage expansion
4. PSU:
   - Minimum wattage
   - Preferred wattage
   - Connector requirements
   - Headroom calculation
5. Case/cooling:
   - Minimum GPU clearance
   - Intake/exhaust requirement
   - Cooling risks
6. RAM/storage:
   - Minimum and preferred RAM
   - Minimum and preferred NVMe/SATA layout
7. Purchase rule:
   - What specs are non-negotiable
   - What can be upgraded later
   - What unknowns make a listing unsafe
8. Shortlist impact:
   - Which current candidates match this target
   - Which candidates should be rejected despite attractive GPU or price

Return the answer as:
- Target configuration table
- Minimum viable configuration
- Preferred configuration
- Red flags checklist
- Candidate ranking impact
```
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/README.md
`````markdown
# Expandable Workstation Scoring Policy Pack

Generated: 2026-04-29

## Purpose

This pack upgrades the scoring system so NotebookLM evaluates desktops as cohesive expandable AI workstations, not just as isolated CPU/GPU spec lists.

## Files

1. `policy_expandable_workstation_scoring.md`
2. `template_product_card_output.md`
3. `prompt_notebooklm_executor.md`
4. `prompt_synergy_config_advisor.md`
5. `rubric_component_synergy_matrix.md`

## Recommended NotebookLM Use

Upload all five files into the relevant NotebookLM notebook:

- `02 — Expandable Workstations`
- optionally also `01 — Master Hardware Strategy + Ledger`

Then upload product listing sources and run the executor prompt.
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/rubric_component_synergy_matrix.md
`````markdown
# Component Synergy Matrix – Expandable AI Workstations

Use this as a checklist when evaluating whether a machine is cohesive.

## GPU ↔ PSU

| GPU setup | Minimum PSU | Preferred PSU | Notes |
|---|---:|---:|---|
| 1× RTX 3090 24GB | 850W | 1000W | 3090 transient spikes matter. |
| 2× RTX 3090 24GB | 1200W | 1300W+ | Prefer blower cards, strong airflow. |
| 1× RTX 4090 24GB | 850W | 1000W | Native 12VHPWR / safe cabling important. |
| 2× RTX 4090 24GB | 1300W | 1600W | Usually impractical in normal consumer cases. |
| 1× RTX A5000 24GB | 750W | 850W | Lower power, workstation-friendly. |
| 2× RTX A5000 24GB | 1000W | 1200W | Strong multi-GPU workstation route. |
| 1× RTX A6000 48GB | 850W | 1000W | Expensive but excellent capacity. |

## GPU ↔ Case

| Case trait | Score impact |
|---|---|
| 320mm+ GPU clearance | Positive |
| 3-slot GPU support | Positive |
| Two 2-slot blower GPUs supported | Strong positive |
| Drive cage blocks long GPU | Negative |
| Solid front panel with weak intake | Negative |
| Unknown clearance | Reduce compatibility confidence |

## CPU ↔ Workload

| CPU class | Fit |
|---|---|
| Xeon W / Threadripper / Threadripper Pro | Strong workstation fit |
| Ryzen 9 / Core i9 | Strong consumer creator fit |
| Ryzen 7 / Core i7 | Usually adequate for GPU-bound inference |
| Old low-core Xeon | Acceptable only if GPU value is excellent |
| Weak SFF CPU | Penalise for high-end GPU pairing |

## RAM ↔ Workload

| RAM | Fit |
|---:|---|
| 32GB | Minimum serious baseline |
| 64GB | Preferred current target |
| 128GB | Strong growth-platform target |
| 256GB+ | Enterprise bonus if price is reasonable |

## Storage ↔ Workload

| Storage setup | Fit |
|---|---|
| 1TB NVMe only | Minimum, likely needs upgrade |
| 2TB NVMe | Preferred baseline |
| 2× NVMe + SATA bays | Strong |
| No NVMe / HDD-only | Reject or upgrade immediately |

## Atomic Dimension Score Caps

| Missing detail | Cap |
|---|---:|
| PSU wattage unknown | `PSU Headroom` capped at 0/10 |
| Motherboard model / slot layout unknown | `PCIe Slot Layout Clarity` capped at 0/10, `Second PCIe x16 Slot Usability` max 5/10 |
| Case GPU clearance unknown | `Chassis Clearance for 2nd GPU` max 5/10, `Sustained Thermal Stability` max 5/10 |
| GPU VRAM unclear | `VRAM Adequacy` capped at 5/10 |
| Warranty unclear | `Warranty Coverage` capped at 0/10 |
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/template_product_card_output.md
`````markdown
# Template – Product Card Output

Use this exact Markdown structure for each candidate.

```markdown
<!-- PRODUCT CARD START: [Machine name or short label] -->
### [Machine name or short label]

**Headline verdict:** [1–2 lines. Example: “Strong single-GPU refurb, weak multi-GPU future.”]

**Score (Atomic Dimensions - Unweighted):**
- VRAM Adequacy: [X] / 10
- GPU Compute Tier: [X] / 10
- CPU Multi-core Sustained: [X] / 10
- System RAM Capacity: [X] / 10
- PSU Headroom for Current GPU: [X] / 10
- CPU/GPU PCIe Bottleneck Risk: [X] / 10
- PCIe Slot Layout Clarity: [X] / 10
- PSU Connector Availability: [X] / 10
- Intake Airflow Volume: [X] / 10
- Sustained Thermal Stability: [X] / 10
- Second PCIe x16 Slot Usability: [X] / 10
- Chassis Clearance for 2nd GPU: [X] / 10
- PSU Wattage Ceiling: [X] / 10
- Price per GB VRAM: [X] / 10
- Enterprise Pedigree: [X] / 10
- Warranty Coverage: [X] / 10

**Classification**
- Expansion class: [Growth Platform / Single-24GB-GPU Candidate / Single-GPU Value Exception / Portable Value Exception / Unified-Memory Exception / Modular Exception / Rejected Benchmark]
- VRAM strategy fit: [48GB+ Growth Target / Single 24GB Target / 16GB Compromise / Rejected]
- Recommendation: [Strong buy / Conditional buy (if X) / Niche buy / Not recommended for expandable AI workstation]

**Key specs (from listing)**
- CPU:
- RAM (capacity, type, slots used/free):
- Storage (NVMe, SATA, total bays):
- GPU (if included, else “not included”):
- Motherboard notes (chipset, slots, PCIe layout if known):
- PSU (model, wattage, efficiency, connectors if known):
- Case / form factor (size, GPU clearance, fan positions if known):
- Warranty / seller terms:

**Synergy analysis**
- CPU ↔ GPU balance:
- PSU ↔ GPU(s) / CPU headroom:
- Cooling ↔ workload:
- Case ↔ GPU length / airflow:
- Platform ↔ upgrade path:

**Best-fit use case**
[Short paragraph describing who this is actually good for and at what budget/performance tradeoff.]

**Rejected or risky points**
- [Bottleneck, imbalance, or risk]
- [Unknown that meaningfully affects scoring]
- [Platform limitation for future dual-GPU or high-TDP upgrades]

**Overall recommendation**
[Strong buy / Conditional buy (if X) / Niche buy / Not recommended for expandable AI workstation]

**Verification required before purchase**
- [PSU model / wattage / connectors]
- [Motherboard PCIe slot layout]
- [Case GPU clearance]
- [Warranty / return policy]
<!-- PRODUCT CARD END: [Machine name or short label] -->
```
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/17_system_ram_gb_or_unified_memory_gb.md
`````markdown
<!-- TAGS: #DecisionAxis #RAM #UnifiedMemory #VRAM-Reference -->
<!-- PRODUCT CARD START: System_RAM_GB_or_Unified_Memory_GB -->
### [90 / 100] — System_RAM_GB_or_Unified_Memory_GB

- **Category**: Apple Mac
- **Condition**: UNKNOWN
- **Price (AUD)**: $UNKNOWN
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: 24GB
- **CPU**: UNKNOWN
- **RAM**: Target ≥32GB system RAM for Windows; ≥64GB unified memory for Apple to rival a 24GB NVIDIA setup in capacity.
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 90 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 90 / 110 (81%)

#### AI Capability Summary
Capable of running models suitable for 24GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 24GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: System_RAM_GB_or_Unified_Memory_GB -->
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/chatgpt_agent_research_prompt.md
`````markdown
# ChatGPT Agent Mode — AU Laptop Research Prompt
# Purpose: Use browser control to collect AU retailer data for the 4 RTX 5090 laptop targets.
# Output will be pasted directly into the repo card shells and CSV by the local agent.
# Generated: 2026-05-03

---

## PROMPT (paste this into ChatGPT Agent Mode / Computer Use)

```
You are a hardware research agent with browser control.

Your job is to collect Australian retailer data for 4 specific laptop models and return it in a structured format I can paste directly into my repo files.

---

## TASK

Search Australian retailer websites for each of the 4 laptops below.
For each laptop, visit at least 2 AU retailer pages and collect the exact fields listed.

Do NOT guess or infer values. If a field is not listed on the retailer page, write UNKNOWN.

---

## LAPTOPS TO RESEARCH

1. ASUS ROG Strix Scar 18 (2025) with RTX 5090 Laptop GPU
2. Lenovo Legion 9i Gen 10 18" with RTX 5090 Laptop GPU
3. MSI Raider A18 HX with RTX 5090 Laptop GPU
4. MSI Titan (any 2025 18" variant) with RTX 5090 Laptop GPU
   - Note: confirm exact model name (e.g. Titan GT77 HX, Titan 18 HX, etc.)

---

## AU RETAILERS TO CHECK (in order of preference)

- JB Hi-Fi: https://www.jbhifi.com.au
- Centre Com: https://www.centrecom.com.au
- Scorptec: https://www.scorptec.com.au
- Affordable Laptops: https://www.affordablelaptops.com.au
- PLE Computers: https://www.ple.com.au
- ASUS AU store: https://rog.asus.com/au/laptops/
- Lenovo AU store: https://www.lenovo.com/au/en/laptops/legion-laptops/
- MSI AU store: https://au.msi.com/Laptops

---

## FIELDS TO COLLECT FOR EACH LAPTOP

For each laptop, collect ALL of the following. Write UNKNOWN if not found on the page.

1.  Retailer name
2.  Retailer URL (direct product page URL)
3.  In stock right now? (Yes / No / Check store)
4.  Price (AUD, inc. GST — exact listed price)
5.  Exact model name / SKU as shown on the retailer page
6.  GPU confirmed (e.g. "RTX 5090 Laptop GPU, 24 GB GDDR7")
7.  CPU model (e.g. "Intel Core i9-14900HX")
8.  RAM installed (e.g. "32 GB DDR5")
9.  RAM max supported (e.g. "64 GB")
10. Free RAM slots (count — how many slots are empty)
11. SSD installed (e.g. "2 TB NVMe")
12. Free M.2 slots (count — how many are empty)
13. Charger / PSU wattage (e.g. "330 W")
14. Weight (kg)
15. Warranty — term (e.g. "2 years")
16. Warranty — type (e.g. "carry-in", "onsite", "depot")
17. Panel type (e.g. "QHD IPS 240 Hz", "OLED", "MiniLED")
18. Sustained TGP in watts — check the product spec sheet or any linked review. If listed as a range (e.g. "150 W – 175 W"), capture both values.
19. Thermal flag — note any mention of "runs hot", "throttles", "excellent thermals", etc. from the retailer page or a pinned review link.

---

## OUTPUT FORMAT

Return a separate block for each laptop using exactly this format.
Use the field names exactly as shown — they map directly to my repo files.

---

### LAPTOP 1: ASUS ROG Strix Scar 18 (2025) RTX 5090
<!-- Maps to: NotebookLM_Workspaces/Laptops/30_asus-rog-strix-scar-18-rtx-5090-2025.md -->
<!-- CSV row: ASUS_ROG_Scar18_2025_RTX5090_24GB in laptop_candidates.csv -->

- Retailer name: 
- Retailer URL: 
- In stock: 
- Price (AUD): 
- Exact model name / SKU: 
- GPU confirmed: 
- CPU: 
- RAM installed: 
- RAM max supported: 
- Free RAM slots: 
- SSD installed: 
- Free M.2 slots: 
- Charger wattage: 
- Weight: 
- Warranty term: 
- Warranty type: 
- Panel type: 
- Sustained TGP: 
- Thermal flag: 

---

### LAPTOP 2: Lenovo Legion 9i Gen 10 18" RTX 5090
<!-- Maps to: NotebookLM_Workspaces/Laptops/31_lenovo-legion-9i-18-rtx-5090.md -->
<!-- CSV row: Lenovo_Legion_Pro9i_RTX5090_24GB in laptop_candidates.csv -->

- Retailer name: 
- Retailer URL: 
- In stock: 
- Price (AUD): 
- Exact model name / SKU: 
- GPU confirmed: 
- CPU: 
- RAM installed: 
- RAM max supported: 
- Free RAM slots: 
- SSD installed: 
- Free M.2 slots: 
- Charger wattage: 
- Weight: 
- Warranty term: 
- Warranty type: 
- Panel type: 
- Sustained TGP: 
- Thermal flag: 

---

### LAPTOP 3: MSI Raider A18 HX RTX 5090
<!-- Maps to: NotebookLM_Workspaces/Laptops/32_msi-raider-a18-hx-rtx-5090.md -->
<!-- CSV row: MSI_Raider_A18_HX_RTX5090_24GB in laptop_candidates.csv -->

- Retailer name: 
- Retailer URL: 
- In stock: 
- Price (AUD): 
- Exact model name / SKU: 
- GPU confirmed: 
- CPU: 
- RAM installed: 
- RAM max supported: 
- Free RAM slots: 
- SSD installed: 
- Free M.2 slots: 
- Charger wattage: 
- Weight: 
- Warranty term: 
- Warranty type: 
- Panel type: 
- Sustained TGP: 
- Thermal flag: 

---

### LAPTOP 4: MSI Titan (2025, 18") RTX 5090
<!-- Maps to: NotebookLM_Workspaces/Laptops/33_msi-titan-rtx-5090.md -->
<!-- CSV row: MSI_Titan_GT77_RTX5090_24GB in laptop_candidates.csv -->

- Retailer name: 
- Retailer URL: 
- In stock: 
- Price (AUD): 
- Exact model name / SKU:          ← IMPORTANT: confirm exact Titan variant name here
- GPU confirmed: 
- CPU: 
- RAM installed: 
- RAM max supported: 
- Free RAM slots: 
- SSD installed: 
- Free M.2 slots: 
- Charger wattage: 
- Weight: 
- Warranty term: 
- Warranty type: 
- Panel type: 
- Sustained TGP: 
- Thermal flag: 

---

## ADDITIONAL NOTES

- Budget cap for this purchase is AUD 4,000. Flag with "⚠️ OVER BUDGET" if price exceeds this.
- Preferred sweet spot is AUD 2,500–3,500. Flag with "✅ IN SWEET SPOT" if in this range.
- If any laptop is completely unavailable in AU (no stock, no listing), write: "NOT LISTED IN AU — checked [retailer names]"
- If you find multiple configurations for the same chassis (e.g. 32 GB vs 64 GB RAM), return BOTH rows using the same format, labelled as CONFIG A and CONFIG B.
- Do not return summaries or recommendations — raw field data only. The local scoring engine handles ranking.

---

## AFTER COLLECTING ALL DATA

At the end, add a one-line stock summary:

STOCK SUMMARY:
- ASUS Scar 18 5090: [In stock at X / Not listed / Price only]
- Legion 9i 18 5090: [In stock at X / Not listed / Price only]
- MSI Raider A18 HX 5090: [In stock at X / Not listed / Price only]
- MSI Titan 5090: [In stock at X / Not listed / Price only — confirm model name]
```
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/data_ready_checklist_2026-05-04.md
`````markdown
# Unified Data-Ready Checklist — All Tracks

**Generated:** 2026-05-04
**Source:** Repo card audit (no web access — all values from existing .md files only)
**Purpose:** Master list of all UNKNOWN fields requiring manual web/retailer lookup before
scoring, gate clearance, or purchase decisions can proceed.

> 🔴 = Blocks a go/no-go gate or GOOD ENOUGH condition
> 🟡 = Required for accurate rubric scoring
> 🟢 = Informational / secondary

---

## TRACK 1 — NVIDIA Laptops (Path 1A)

### Existing Cards (4 NVIDIA + 4 RTX 5090 cards)

| Card | Field | Priority | Notes |
|---|---|---|---|
| All 8 NVIDIA cards | AU stock confirmed at named retailer + URL | 🔴 | GOOD ENOUGH gate-critical |
| All 8 NVIDIA cards | Price in AUD (confirmed, not estimated) | 🔴 | Budget gate |
| 30_asus-rog-strix-scar-18-rtx-5090 | CPU model | 🟡 | |
| 30_asus-rog-strix-scar-18-rtx-5090 | RAM installed + max + free slots | 🟡 | |
| 30_asus-rog-strix-scar-18-rtx-5090 | Charger wattage | 🟡 | |
| 30_asus-rog-strix-scar-18-rtx-5090 | Weight | 🟢 | |
| 30_asus-rog-strix-scar-18-rtx-5090 | Sustained TGP from review | 🟡 | |
| 31_lenovo-legion-9i-18-rtx-5090 | CPU model | 🟡 | |
| 31_lenovo-legion-9i-18-rtx-5090 | RAM installed + max + free slots | 🟡 | |
| 31_lenovo-legion-9i-18-rtx-5090 | Charger wattage | 🟡 | |
| 31_lenovo-legion-9i-18-rtx-5090 | Weight | 🟢 | |
| 31_lenovo-legion-9i-18-rtx-5090 | Sustained TGP from review | 🟡 | |
| 32_msi-raider-a18-hx-rtx-5090 | CPU model | 🟡 | |
| 32_msi-raider-a18-hx-rtx-5090 | RAM installed + max + free slots | 🟡 | |
| 32_msi-raider-a18-hx-rtx-5090 | Charger wattage | 🟡 | |
| 33_msi-titan-rtx-5090 | CPU model | 🟡 | |
| 33_msi-titan-rtx-5090 | RAM installed + max + free slots | 🟡 | |
| 33_msi-titan-rtx-5090 | Charger wattage | 🟡 | |
| 21–24 (RTX 4090 cards) | All key specs | 🟡 | Legacy cards; lower priority vs RTX 5090 tier |

---

## TRACK 1 — AMD Strix Halo Laptops (Path 1B)

### New Card Shells (created 2026-05-04 — all fields UNKNOWN)

| Card | Field | Priority | Notes |
|---|---|---|---|
| 34_asus-tuf-gaming-a16-strix-halo | SoC model (confirm Strix Halo — not standard Ryzen) | 🔴 | Gate: Path 1B eligibility |
| 34_asus-tuf-gaming-a16-strix-halo | Unified memory size in AU SKU (32 / 64 / 96 GB?) | 🔴 | Gate: ≥ 32 GB required |
| 34_asus-tuf-gaming-a16-strix-halo | AU stock + named retailer + URL | 🔴 | GOOD ENOUGH gate |
| 34_asus-tuf-gaming-a16-strix-halo | Price in AUD | 🔴 | Budget gate |
| 34_asus-tuf-gaming-a16-strix-halo | ROCm / llama.cpp compatibility | 🔴 | Disqualifying flag if severe gap |
| 34_asus-tuf-gaming-a16-strix-halo | Sustained TDP under load | 🟡 | Thermal scoring |
| 34_asus-tuf-gaming-a16-strix-halo | Storage + free M.2 slots | 🟡 | |
| 34_asus-tuf-gaming-a16-strix-halo | Weight + charger wattage | 🟢 | |
| 35_asus-rog-zephyrus-g16-strix-halo | SoC model (confirm Strix Halo) | 🔴 | Gate: Path 1B eligibility |
| 35_asus-rog-zephyrus-g16-strix-halo | Unified memory size in AU SKU | 🔴 | Gate: ≥ 32 GB required |
| 35_asus-rog-zephyrus-g16-strix-halo | AU stock + named retailer + URL | 🔴 | GOOD ENOUGH gate |
| 35_asus-rog-zephyrus-g16-strix-halo | Price in AUD | 🔴 | Budget gate |
| 35_asus-rog-zephyrus-g16-strix-halo | ROCm / llama.cpp compatibility | 🔴 | Disqualifying flag if severe gap |
| 35_asus-rog-zephyrus-g16-strix-halo | Sustained TDP under load | 🟡 | |
| 36_lenovo-amd-strix-halo-laptop | Exact model name + SKU carrying Strix Halo | 🔴 | Card shell uses placeholder name |
| 36_lenovo-amd-strix-halo-laptop | SoC model (confirm Strix Halo) | 🔴 | Gate: Path 1B eligibility |
| 36_lenovo-amd-strix-halo-laptop | Unified memory size in AU SKU | 🔴 | Gate: ≥ 32 GB required |
| 36_lenovo-amd-strix-halo-laptop | AU stock + named retailer + URL | 🔴 | GOOD ENOUGH gate |
| 36_lenovo-amd-strix-halo-laptop | Price in AUD | 🔴 | Budget gate |
| 36_lenovo-amd-strix-halo-laptop | Screen size (determines scoring bonus/penalty) | 🔴 | Bonus at 17–18"; penalty < 15" |
| 36_lenovo-amd-strix-halo-laptop | ROCm / llama.cpp compatibility | 🔴 | Disqualifying flag if severe gap |

---

## TRACK 2 — Pathway A (AU System Integrator Build)

| Field | Priority | Notes |
|---|---|---|
| CPU — model and generation | 🔴 | No build spec yet; all fields UNKNOWN |
| Motherboard — model, chipset, PCIe x16 slot count and lane allocation | 🔴 | Gate: must support target GPU config |
| RAM — capacity, type, speed | 🟡 | |
| PSU — model, wattage, efficiency, connector count | 🔴 | Gate: must support dual GPU (≥ 1000W recommended for dual RTX 3090) |
| Case — model, GPU clearance, fan layout | 🟡 | |
| Storage — SSD model + capacity | 🟢 | |
| GPU — RTX 3090 × 2: AU used/refurb market availability | 🔴 | Gate: must be explicitly confirmed, not assumed |
| GPU — RTX 3090 × 2: price per unit in AU market | 🔴 | Budget gate |
| NVLink support — platform compatibility for RTX 3090 pair | 🟡 | Determines pooled VRAM (48 GB) |
| Total build cost at target integrator (Scorptec / Mwave / Centre.com) | 🔴 | Budget gate |

---

## TRACK 2 — Pathway B (Refurbished Enterprise Workstation)

| Card | Field | Priority | Notes |
|---|---|---|---|
| 28_hp-z4-g4 | Manufacture date (confirm ≥ 2018) | 🔴 | Age gate |
| 28_hp-z4-g4 | PSU model + wattage | 🔴 | Card explicitly flags "VERIFY adequacy" |
| 28_hp-z4-g4 | PCIe x16 slot count + lane allocation | 🔴 | Gate: dual GPU support |
| 28_hp-z4-g4 | ECC RAM — confirm GPU driver compatibility | 🟡 | Risk flag |
| 29_dell-precision-7910 | Manufacture date — URGENT (likely < 2018) | 🔴 | Probable age disqualification |
| 29_dell-precision-7910 | Current AU used market price | 🟡 | For budget gate if age clears |
| 09_alienware-aurora-r12 | PSU model + wattage | 🔴 | Gate: adequate for RTX 3090 |
| 09_alienware-aurora-r12 | PCIe x16 slot count | 🔴 | OEM chassis likely single GPU only |
| 09_alienware-aurora-r12 | Manufacture date (confirm 2021) | 🟡 | Likely passes; confirm |
| 18_dell-precision-5820-bundle | Unbundled price (workstation only, no ThinkPad) | 🔴 | Budget gate — bundle at $3,558 inflated |
| 18_dell-precision-5820-bundle | PSU model + wattage | 🔴 | Gate |
| 18_dell-precision-5820-bundle | PCIe x16 slot count + lane allocation | 🔴 | Gate |
| 18_dell-precision-5820-bundle | ECC RAM — confirm GPU driver compatibility | 🟡 | Risk flag |
| 26_acer-orion-7000 | PSU model + wattage | 🟡 | Low priority — already weak candidate |

---

## TRACK 2 — Pathway C (Unified Memory Mini PC)

| Card | Field | Priority | Notes |
|---|---|---|---|
| 40_minisforum-ai-x1-pro | AU stock at named retailer + URL | 🔴 | Gate-critical |
| 40_minisforum-ai-x1-pro | Price in AUD | 🔴 | Budget gate |
| 40_minisforum-ai-x1-pro | Exact SoC model (confirm Strix Halo) | 🔴 | Gate eligibility |
| 40_minisforum-ai-x1-pro | Unified memory size in AU SKU (64 / 96 / 128 GB?) | 🔴 | Gate: ≥ 64 GB required |
| 40_minisforum-ai-x1-pro | Active cooling confirmed (not passive) | 🔴 | Disqualifying flag if passive |
| 40_minisforum-ai-x1-pro | ROCm / llama.cpp compatibility | 🔴 | Disqualifying flag if severe gap |
| 40_minisforum-ai-x1-pro | External PSU wattage | 🟡 | |
| 40_minisforum-ai-x1-pro | M.2 slot count + storage options | 🟢 | |
| 41_asus-nuc-strix-halo | Exact model name carrying Strix Halo SoC | 🔴 | Shell uses placeholder |
| 41_asus-nuc-strix-halo | AU stock at named retailer + URL | 🔴 | Gate-critical |
| 41_asus-nuc-strix-halo | Price in AUD | 🔴 | Budget gate |
| 41_asus-nuc-strix-halo | Unified memory size in AU SKU | 🔴 | Gate: ≥ 64 GB required |
| 41_asus-nuc-strix-halo | Active cooling confirmed | 🔴 | Disqualifying flag if passive |
| 41_asus-nuc-strix-halo | ROCm / llama.cpp compatibility | 🔴 | Disqualifying flag if severe gap |

---

## Summary — Count of Red-Priority UNKNOWN Fields

| Track / Pathway | 🔴 Red fields blocking gates |
|---|---|
| Track 1 — NVIDIA (Path 1A) | 8 (AU stock × 8 cards) + all key specs on new 5090 shells |
| Track 1 — AMD (Path 1B) | 21 across 3 new shells |
| Track 2 — Pathway A | 7 (entire build spec UNKNOWN) |
| Track 2 — Pathway B | 11 across 5 cards |
| Track 2 — Pathway C | 12 across 2 new shells |
| **TOTAL blocking** | **~59 red-priority fields** |

---

## Recommended Lookup Sequence

1. **Immediate (Track 1 priority):** AMD Strix Halo laptop AU availability — confirm ASUS TUF A16, Zephyrus G16, and any Lenovo Strix Halo are actually stocked in AU before investing further research time.
2. **Immediate (Track 2 Pathway C):** Minisforum AI X1 Pro AU availability + price — this is the highest-potential Pathway C candidate with 128 GB ceiling.
3. **Track 2 Pathway B triage:** Confirm Dell Precision 7910 manufacture date — likely disqualification will clean up the shortlist immediately.
4. **Track 2 Pathway A:** Fill build spec with a single credible SI config before doing GPU availability checks.
5. **Track 1 NVIDIA:** Confirm AU stock for RTX 5090 chassis — these are the priority purchase candidates under current strategy.
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/laptop_data_audit_2026-05-03.md
`````markdown
# Laptop Data Audit — Sprint A
**File:** `Decision_System/laptop_data_audit_2026-05-03.md`
**Date:** 2026-05-03
**Scope:** `laptop_candidates.csv` ↔ `Laptops/*.md` cross-reference, field-level UNKNOWN flags, manual research checklist.
**Constraint:** Agent must not infer or guess missing values. UNKNOWN fields stay UNKNOWN until manually updated.

---

## Section 1 — CSV ↔ Card Cross-Reference

Budget status key: 🟢 Within sweet spot (≤ $3,500) · 🟡 Within cap, above sweet spot ($3,500–$4,000) · 🔴 Over cap (> $4,000) · ⬜ UNKNOWN (no price in repo)

| # | CSV `Machine` | CSV `Type` | Card file | Sync status | Budget_Status |
|---|---|---|---|---|---|
| 1 | `ASUS_ROG_Scar17_RTX4090_16GB` | Preferred | `22_asus-rog-strix-scar-17-rtx-4090.md` | ✅ Matched | 🔴 Over cap (~$5,099 old price) |
| 2 | `ASUS_ROG_Scar18_RTX4090_16GB` | Preferred | `23_asus-rog-strix-scar-18-rtx-4090.md` | ✅ Matched | 🔴 Over cap (~$6,899 old price) |
| 3 | `Lenovo_Legion_Pro7i_RTX4090_16GB` | Preferred | `21_lenovo-legion-pro-7i-rtx-4090.md` | ✅ Matched | 🟡/🔴 Split — low config ~$3,599 (🟡), high config ~$4,399 (🔴); needs current AU check |
| 4 | `MSI_Stealth16_RTX4090_16GB` | Borderline | `24_msi-stealth-16-ai-studio-rtx-4090.md` | ✅ Matched | 🔴 Over cap (~$6,599 old price) |
| 5 | `Dell_Alienware_m18_RTX4090_16GB` | OutOfScope | *(no card)* | ⛔ Out of scope — not a listed brand | — |
| 6 | `ASUS_ROG_Scar18_2025_RTX5090_24GB` | Target-UNVERIFIED | `30_asus-rog-strix-scar-18-rtx-5090-2025.md` | ⚠️ Shell only — all scores zeroed pending manual data | ⬜ UNKNOWN |
| 7 | `Lenovo_Legion_Pro9i_RTX5090_24GB` | Target-UNVERIFIED | `31_lenovo-legion-9i-18-rtx-5090.md` | ⚠️ Shell only — all scores zeroed pending manual data | ⬜ UNKNOWN |
| 8 | `MSI_Raider_A18_HX_RTX5090_24GB` | Target-UNVERIFIED | `32_msi-raider-a18-hx-rtx-5090.md` | ⚠️ Shell only — all scores zeroed pending manual data | ⬜ UNKNOWN |
| 9 | `MSI_Titan_GT77_RTX5090_24GB` | Target-UNVERIFIED | `33_msi-titan-rtx-5090.md` | ⚠️ Shell only — reclassified; Titan IS in scope per AGENTS.md | ⬜ UNKNOWN |

---

## Section 2 — Field-Level Audit: Existing 4090 Cards

### Card 21 — Lenovo Legion Pro 7i (RTX 4090, 16 GB)
**CSV row:** `Lenovo_Legion_Pro7i_RTX4090_16GB` | **File:** `21_lenovo-legion-pro-7i-rtx-4090.md`
**Track 1 status:** Fallback candidate (16 GB VRAM, not a locked chassis — Legion *9i* 18 is the locked family)

| Field | Value in card | Status |
|---|---|---|
| GPU / VRAM | RTX 4090 Laptop GPU, 16 GB GDDR6 | ✅ |
| CPU | Intel Core i9-14900HX | ✅ |
| RAM installed | 32 GB DDR5 | ✅ |
| RAM max supported | 64 GB (upgradeable) | ✅ spec stated, slot count UNKNOWN |
| Free RAM slots | Not listed | ⚠️ UNKNOWN |
| Storage installed | 2 TB SSD | ✅ |
| Free M.2 slots | Not listed | ⚠️ UNKNOWN |
| Display size | 16-inch | ✅ |
| Panel type | Not stated (2K 240 Hz only) | ⚠️ UNKNOWN (IPS / OLED / MiniLED?) |
| Weight | Not listed | ⚠️ UNKNOWN |
| Charger wattage | Not listed | ⚠️ UNKNOWN |
| Price (AUD) | ~$3,599–$4,399 | ⚠️ Approximate; needs current AU check |
| AU retailer (named) | "Mike PC / Lenovo AU / Amazon AU" | ⚠️ Vague — needs specific URL + stock confirmation |
| Warranty | Not listed | ⚠️ UNKNOWN |
| Sustained TGP | Not listed | ⚠️ UNKNOWN |
| Thermal notes | Not listed | ⚠️ UNKNOWN |

**CSV scores (from updated laptop_candidates.csv):**
`VRAM=5, GPU_Compute=8, TGP=9, Thermal=7, RAM=10, Storage=8, AU_Retailer=9, Price=8, Display=5, Portability=7`
**Score source trustworthiness:** ⚠️ TGP=9 and AU_Retailer=9 are asserted without card evidence — flag for review when AU data arrives.

---

### Card 22 — ASUS ROG Strix Scar 17 (RTX 4090, 16 GB)
**CSV row:** `ASUS_ROG_Scar17_RTX4090_16GB` | **File:** `22_asus-rog-strix-scar-17-rtx-4090.md`
**Track 1 status:** Fallback candidate (16 GB VRAM; Scar 17 ≠ Scar 18 locked chassis)

| Field | Value in card | Status |
|---|---|---|
| GPU / VRAM | RTX 4090 Laptop GPU, 16 GB GDDR6 | ✅ |
| CPU | AMD Ryzen 9 7945HX | ✅ |
| RAM installed | 32 GB DDR5 | ✅ |
| RAM max supported | 64 GB (upgradeable) | ✅ spec stated, slot count UNKNOWN |
| Free RAM slots | Not listed | ⚠️ UNKNOWN |
| Storage installed | 1 TB NVMe | ✅ |
| Free M.2 slots | Not listed | ⚠️ UNKNOWN |
| Display size | 17.3-inch WQHD 240 Hz | ✅ |
| Panel type | Not stated | ⚠️ UNKNOWN |
| Weight | Not listed | ⚠️ UNKNOWN |
| Charger wattage | Not listed | ⚠️ UNKNOWN |
| Price (AUD) | ~$5,099 | ⚠️ Approximate; needs current AU check |
| AU retailer (named) | "Umart / Australian IT retailers" | ⚠️ Vague — needs specific URL + stock confirmation |
| Warranty | Not listed | ⚠️ UNKNOWN |
| Sustained TGP | Not listed | ⚠️ UNKNOWN |
| Thermal notes | "Strong sustained thermal performance" | ⚠️ Qualitative only — no wattage or source cited |

**CSV scores:** `VRAM=5, GPU_Compute=8, TGP=9, Thermal=9, RAM=10, Storage=7, AU_Retailer=8, Price=9, Display=8, Portability=6`
**Score source trustworthiness:** ⚠️ TGP=9 and Thermal=9 are asserted in the card without a numeric source — flag.

---

### Card 23 — ASUS ROG Strix Scar 18 (RTX 4090, 16 GB)
**CSV row:** `ASUS_ROG_Scar18_RTX4090_16GB` | **File:** `23_asus-rog-strix-scar-18-rtx-4090.md`
**Track 1 status:** ✅ Locked chassis family (Scar 18) — RTX 4090 fallback version

| Field | Value in card | Status |
|---|---|---|
| GPU / VRAM | RTX 4090 Laptop GPU, 16 GB GDDR6 | ✅ |
| CPU | Intel Core i9-14900HX | ✅ |
| RAM installed | 64 GB DDR5 | ✅ |
| RAM max supported | Not stated explicitly | ⚠️ Implied ≥ 64 GB; max and slot count UNKNOWN |
| Free RAM slots | Not listed | ⚠️ UNKNOWN |
| Storage installed | 2 TB (2× 1 TB NVMe) | ✅ |
| Free M.2 slots | 2 drives installed — free slots UNKNOWN | ⚠️ UNKNOWN |
| Display size | 18-inch QHD | ✅ |
| Panel type | Not stated | ⚠️ UNKNOWN |
| Weight | ~3.1 kg | ✅ |
| Charger wattage | Not listed | ⚠️ UNKNOWN |
| Price (AUD) | ~$6,899 | ⚠️ Approximate; needs current AU check |
| AU retailer (named) | "MSY / Umart-linked AU retail" | ⚠️ Vague — needs specific URL + stock confirmation |
| Warranty | Not listed | ⚠️ UNKNOWN |
| Sustained TGP | Not listed | ⚠️ UNKNOWN |
| Thermal notes | Not listed | ⚠️ UNKNOWN |

**CSV scores:** `VRAM=5, GPU_Compute=8, TGP=9, Thermal=9, RAM=10, Storage=10, AU_Retailer=7, Price=4, Display=10, Portability=3`
**Score source trustworthiness:** ⚠️ TGP=9 and Thermal=9 have no card evidence. Price=4 reflects the high ~$6,899 price — plausible but needs current AU confirmation.

---

### Card 24 — MSI Stealth 16 AI Studio (RTX 4090, 16 GB)
**CSV row:** `MSI_Stealth16_RTX4090_16GB` | **File:** `24_msi-stealth-16-ai-studio-rtx-4090.md`
**Track 1 status:** ✅ In scope per AGENTS.md (MSI Stealth 16/17/18 is a listed family). Marked Borderline due to 16 GB VRAM and thermal concerns. Budget status: 🔴 Over cap at ~$6,599 old price — needs current AU check.

| Field | Value in card | Status |
|---|---|---|
| GPU / VRAM | RTX 4090 Laptop GPU, 16 GB GDDR6 | ✅ |
| CPU | Intel Core Ultra 9 185H | ✅ |
| RAM installed | 32 GB DDR5 | ✅ |
| RAM max supported | "Soldered; verify upgrade path" | 🔴 UNVERIFIED — soldered RAM is a hard ceiling risk |
| Free RAM slots | Not listed | ⚠️ UNKNOWN |
| Storage installed | 2 TB SSD | ✅ |
| Free M.2 slots | Not listed | ⚠️ UNKNOWN |
| Display size | 16-inch creator-class | ✅ |
| Panel type | Not stated; resolution UNKNOWN | ⚠️ UNKNOWN |
| Weight | Not listed | ⚠️ UNKNOWN |
| Charger wattage | Not listed | ⚠️ UNKNOWN |
| Price (AUD) | ~$6,599 | ⚠️ Approximate; needs current AU check |
| AU retailer (named) | Umart | ✅ Named, but stock/URL not confirmed |
| Warranty | Not listed | ⚠️ UNKNOWN |
| Sustained TGP | Not listed | ⚠️ UNKNOWN |
| Thermal notes | "Thermal risk under sustained inference" | ⚠️ Qualitative flag only — no wattage cited |

**CSV scores:** `VRAM=5, GPU_Compute=6, TGP=5, Thermal=5, RAM=3, Storage=7, AU_Retailer=6, Price=4, Display=5, Portability=8`
**Score source trustworthiness:** ⚠️ RAM=3 correctly penalises soldered RAM, but upgrade path is marked UNVERIFIED in the card. Thermal=5 and TGP=5 have no numeric source.

---

## Section 3 — RTX 5090 Shell Cards (Track 1 Primary Targets)

All four are blank shells. All scores are zeroed. No field can be filled by the agent.

| Chassis | Card file | Fields populated | Fields UNKNOWN |
|---|---|---|---|
| ASUS ROG Strix Scar 18 (5090) | `30_asus-rog-strix-scar-18-rtx-5090-2025.md` | GPU class, VRAM class, chassis ID | All spec/price/retailer/thermal fields |
| Lenovo Legion 9i 18 (5090) | `31_lenovo-legion-9i-18-rtx-5090.md` | GPU class, VRAM class, chassis ID | All spec/price/retailer/thermal fields |
| MSI Raider A18 HX (5090) | `32_msi-raider-a18-hx-rtx-5090.md` | GPU class, VRAM class, chassis ID | All spec/price/retailer/thermal fields |
| MSI Titan (5090) | `33_msi-titan-rtx-5090.md` | GPU class, VRAM class, chassis family | Model variant UNKNOWN; all spec/price/retailer/thermal fields UNKNOWN |

---

## Section 4 — Manual Web Research Checklist

Collect these fields for each of the 4 RTX 5090 target chassis from AU retailer pages.
Return the data here and the agent will fill the card shells and update CSV scores.

**Priority order:** AU_Retailer_Confidence → Sustained_TGP_Rating → VRAM_Adequacy (already known) → rest.
AU_Retailer_Confidence is the single hardest gate for the GOOD ENOUGH stop condition.

| Field to collect | Scar 18 RTX 5090 | Legion 9i 18 RTX 5090 | Raider A18 HX RTX 5090 | MSI Titan RTX 5090 |
|---|---|---|---|---|
| AU retailer name | ☐ | ☐ | ☐ | ☐ |
| AU retailer URL (direct product page) | ☐ | ☐ | ☐ | ☐ |
| In stock now? (Y/N) | ☐ | ☐ | ☐ | ☐ |
| Price (AUD, inc. GST) | ☐ | ☐ | ☐ | ☐ |
| Exact model name / SKU | — | — | — | ☐ (confirm Titan variant) |
| GPU confirmed (RTX 5090 / GDDR7 / 24 GB) | ☐ | ☐ | ☐ | ☐ |
| CPU model | ☐ | ☐ | ☐ | ☐ |
| RAM installed (GB) | ☐ | ☐ | ☐ | ☐ |
| RAM max supported (GB) | ☐ | ☐ | ☐ | ☐ |
| Free RAM slots (count) | ☐ | ☐ | ☐ | ☐ |
| SSD installed (TB) | ☐ | ☐ | ☐ | ☐ |
| Free M.2 slots (count) | ☐ | ☐ | ☐ | ☐ |
| Charger wattage (W) | ☐ | ☐ | ☐ | ☐ |
| Weight (kg) | ☐ | ☐ | ☐ | ☐ |
| Warranty — term (e.g. 2 yr) | ☐ | ☐ | ☐ | ☐ |
| Warranty — type (onsite / carry-in / depot) | ☐ | ☐ | ☐ | ☐ |
| Sustained TGP (W, from spec sheet or review) | ☐ | ☐ | ☐ | ☐ |
| Thermal flag (runs hot / throttles / good) | ☐ | ☐ | ☐ | ☐ |
| Panel type (IPS / OLED / MiniLED) | ☐ | ☐ | ☐ | ☐ |

**Suggested AU retailers to check:**
- ASUS Scar 18: rog.asus.com/au, JB Hi-Fi, Scorptec, Centre Com
- Legion 9i 18: lenovo.com/au, JB Hi-Fi, Centre Com, Scorptec
- Raider A18 HX: au.msi.com, JB Hi-Fi, PLE, Centre Com, Scorptec
- MSI Titan: au.msi.com, JB Hi-Fi, PLE, Centre Com, Scorptec (confirm model variant first)

---

## Section 5 — GOOD ENOUGH Gate Reminder

A candidate triggers the stop condition when ALL of the following are confirmed:

| Criterion | Minimum | Score threshold in rubric |
|---|---|---|
| AU stock from named credible retailer | Confirmed in stock | `AU_Retailer_Confidence ≥ 8` |
| VRAM | 24 GB (RTX 5090) preferred; 16 GB (RTX 4090) fallback | `VRAM_Adequacy ≥ 5` |
| RAM | 32–64 GB installed or clearly upgradable | `RAM_Ceiling ≥ 5` |
| Storage | 2 TB installed or clearly upgradable | `Storage_Expandability ≥ 5` |
| Sustained thermal | No "throttles badly" signal | `Sustained_TGP_Rating ≥ 6` |
| Composite score | ≥ 72.0 / 100 after whitened rubric | `rubric_weighting_engine.py --profile laptop` |

**The engine will not produce a trustworthy score until AU_Retailer_Confidence is filled with real data for at least one candidate.**

---

## Section 6 — Status Summary

| Task | Owner | Status |
|---|---|---|
| CSV ↔ card cross-reference table | Agent | ✅ Done (this doc) |
| Blank card shells for 4 RTX 5090 targets | Agent | ✅ Done (files 30, 31, 32, 33) |
| MSI Titan reclassified to Target-UNVERIFIED in CSV | Agent | ✅ Done |
| Budget_Status column added to audit table | Agent | ✅ Done |
| CSV rows zeroed for unverified 5090 targets | Agent | ✅ Done |
| Out-of-scope rows labelled in CSV | Agent | ✅ Done |
| Manual web research for 5090 chassis | **You** | ☐ Pending |
| Fill card shells with collected data | Agent (after you collect data) | ☐ Blocked on manual research |
| Update CSV scores from filled cards | Agent (after you collect data) | ☐ Blocked on manual research |
| Run `rubric_weighting_engine.py --profile laptop` | Agent | ☐ Blocked on score data |
| Check GOOD ENOUGH threshold (72.0) | Agent | ☐ Blocked on score data |
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/notebook_manifest.md
`````markdown
# Notebook Manifest (v2)

## Notebook 1 – Research Methods & Decision System
- Location: 01_Research_Methods_and_Decision_System/
- Contents:
  - Policy documents and scoring rubrics (Policy_Pack/)
  - vram_architecture_spec_vX.md
  - tagging_taxonomy.md
  - prompts.md
  - notebook_manifest.md
  - Cross‑lane summary and comparison notes (outputs from Notebooks 2–9)

## Notebook 2 – Refurbished Desktop Towers
- Location: 02_Refurbished_Desktop_Towers/
- Typical contents:
  - product_cards tagged #Refurbished AND #DesktopTower
  - OEM and vendor sheets for refurbished towers
  - Notes on warranty, refurb quality, and prior repairs

## Notebook 3 – New Desktop Systems
- Location: 03_New_Desktop_Systems/
- Typical contents:
  - product_cards tagged #New AND #DesktopTower
  - Standard desktop reviews and retailer specs

## Notebook 4 – Laptops (Mainline)
- Location: 04_Laptops_Mainline/
- Typical contents:
  - product_cards tagged #Laptop AND #PrimaryWorkstation
  - Thermals, battery, and performance reports

## Notebook 5 – Apple Silicon Systems
- Location: 05_Apple_Silicon_Systems/
- Typical contents:
  - product_cards tagged #AppleSilicon
  - Unified memory deep‑dives, M‑series benchmarks, VRAM equivalence notes

## Notebook 6 – Mini PCs & eGPU
- Location: 06_Mini_PCs_and_eGPU/
- Typical contents:
  - product_cards tagged #MiniPC OR #eGPU
  - OCuLink / TB eGPU benchmarks and stability notes

## Notebook 7 – Secondary Laptops & Ergonomics
- Location: 07_Secondary_Laptops_and_Ergonomics/
- Typical contents:
  - product_cards tagged #SecondaryLaptop OR #Ergonomics
  - Input device reviews, posture/ergonomics notes

## Notebook 8 – Custom Builds
- Location: 08_Custom_Builds/
- Typical contents:
  - Part‑list builds tagged #CustomBuild
  - Build‑vs‑buy comparisons and cost breakdowns
  - Case/mobo/PSU compatibility notes

## Notebook 9 – Individual Components
- Location: 09_Individual_Components/
- Typical contents:
  - Individual GPUs, CPUs, motherboards, RAM, SSDs, PSUs, coolers, cases
  - Each product_card tagged #Component plus more specific tags (e.g. #GPU, #Motherboard)
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/tagging_taxonomy.md
`````markdown
# Tagging Taxonomy (v2)

## 1. VRAM / Capacity Tags
- #VRAM-12GB
- #VRAM-16GB
- #VRAM-24GB
- #VRAM-32GB
- #VRAM-48GBPlus

## 2. Acquisition Tags
- #New          — Factory new
- #Refurbished  — Vendor or OEM refurb
- #Used         — Private sale / second‑hand
- #OpenBox      — Return / display model

## 3. Form Factor Tags
- #DesktopTower
- #Laptop
- #MiniPC
- #SmallFormFactor
- #CustomBuild   — Complete DIY build or part list
- #Component     — Individual part, not a full system

## 4. Architecture & Topology Tags
- #NVIDIA
- #AMD
- #AppleSilicon
- #IntelArc
- #SingleGPU
- #MultiGPU
- #eGPU
- #IntegratedGPU

## 5. Upgradeability & Platform Tags
- #Expandable       — Room for future GPU/RAM/drive upgrades
- #NonUpgradeable   — Soldered RAM or tightly constrained platform
- #PCIeRich         — Multiple x16/x8 slots, good lane layout
- #SolderedRAM
- #ECCSupport
- #OCuLinkSupport
- #Thunderbolt4

## 6. Use‑Case / Role Tags
- #PrimaryWorkstation
- #SecondaryLaptop
- #TravelFriendly
- #DeskBound
- #AgenticAI
- #Coding
- #ContentCreation
- #MixedUse

## 7. Status & Review Tags
- #Verified      — Specs and pricing checked against source
- #NeedsReview   — Partially checked; revisit before purchase
- #Rejected      — Eliminated for clear reasons
- #Shortlist     — Strong contender
- #Archived      — Historical reference only

## 8. Example Tag Combinations

- Refurbished 24GB expandable tower candidate:  
  `#Refurbished #DesktopTower #Expandable #SingleGPU #NVIDIA #VRAM-24GB #PrimaryWorkstation`

- New 16GB SFF coding box:  
  `#New #SmallFormFactor #DesktopTower #SingleGPU #VRAM-16GB #Coding #TravelFriendly`

- Apple‑first laptop:  
  `#AppleSilicon #Laptop #PrimaryWorkstation #VRAM-24GB #PortableValue`
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/track2_pathway_a_build_spec.md
`````markdown
# Track 2 — Pathway A Build Spec

## Target Configuration

- **CPU:** Threadripper PRO 5955WX or 5975WX (WRX80 chipset)
- **Motherboard:** (specific model TBD, e.g. ASUS Pro WS WRX80E-SAGE)
- **RAM:** 128 GB DDR4 ECC (minimum)
- **PSU:** 1600W+ 80+ Platinum
- **Case:** (TBD — must fit dual 3-slot GPUs)
- **Primary GPU:** RTX 3090 × 2 (24 GB VRAM each)
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/track2_pathway_b_audit_2026-05-04.md
`````markdown
# Track 2 — Pathway B Audit Report

**Generated:** 2026-05-04
**Auditor:** Antigravity agent (repo-only, no web access)
**Source cards:** `Desktop_Towers_Refurbished/*.md` (5 cards)

> All gate evaluations based solely on data present in existing card files.
> UNKNOWN = field not present or not confirmed in card. Manual web lookup required before gates can clear.

---

## Gate Definitions (from AGENTS.md)

| Gate | Requirement |
|---|---|
| G1 — Age | Chassis manufacture date ≥ 2018 |
| G2 — PCIe slots | PCIe slot count + lane allocation confirmed for target GPU config |
| G3 — PSU wattage | PSU confirmed sufficient for GPU(s), or upgrade confirmed possible + costed |
| G4 — GPU VRAM | GPU(s) ≥ 16 GB VRAM per card — pre-installed or confirmed available in AU used market |
| G5 — Budget | Total cost (unit + GPU additions) within AUD 0–4,000 |
| G6 — Thermal | No disqualifying thermal flag (inadequate airflow for dual-GPU sustained load) |
| G7 — ECC | No ECC-only memory constraint preventing standard GPU driver operation |

---

## Card-by-Card Gate Audit

---

### 1. HP Z4 G4 Workstation + RTX 3090 24 GB
**File:** `28_hp-z4-g4-rtx-3090-refurbished.md`

| Gate | Status | Evidence from card |
|---|---|---|
| G1 — Age ≥ 2018 | ⚠️ UNKNOWN | No manufacture date stated on card |
| G2 — PCIe slots | ⚠️ UNKNOWN | "Multiple M.2 and SATA slots" noted but PCIe x16 slot count not confirmed |
| G3 — PSU | ⚠️ NEEDS VERIFICATION | "HP Z4 G4 750W OEM PSU — VERIFY adequacy for RTX 3090 TDP" — card explicitly flags this |
| G4 — GPU VRAM | ✅ PARTIAL | RTX 3090 24 GB (added separately) — 24 GB confirms ≥ 16 GB; AU used market availability UNKNOWN |
| G5 — Budget | ✅ LIKELY | ~$2,800–$3,500 combined — within AUD 4,000 budget |
| G6 — Thermal | ⚠️ UNKNOWN | No thermal notes on card |
| G7 — ECC | ⚠️ RISK | Card notes "up to 128 GB ECC DDR4" — confirm standard GPU driver operation not blocked by ECC requirement |

**Gates cleared:** 1 partial (G4), 1 likely (G5)
**Gates blocking:** G1, G2, G3 (explicit flag), G6, G7
**Verdict:** ❌ NOT GATE-READY — 5 UNKNOWN / flagged gates. Priority: verify PSU adequacy, manufacture date, PCIe slot layout.

---

### 2. Dell Precision Tower 7910 + RTX 3090 24 GB
**File:** `29_dell-precision-tower-7910-rtx-3090.md`

| Gate | Status | Evidence from card |
|---|---|---|
| G1 — Age ≥ 2018 | ❌ LIKELY FAIL | Dell Precision 7910 = 2014–2016 generation (Xeon E5-2600 v3/v4). This platform predates 2018. **Age gate likely disqualified.** |
| G2 — PCIe slots | ⚠️ UNKNOWN | Dual-socket platform may have PCIe x16 slots — not confirmed on card |
| G3 — PSU | ✅ PARTIAL | "1300W Enterprise PSU (typically included in 7910)" — strong PSU headroom for dual GPU |
| G4 — GPU VRAM | ✅ PARTIAL | RTX 3090 24 GB — ≥ 16 GB confirmed; AU availability UNKNOWN |
| G5 — Budget | ⚠️ UNKNOWN | "Varies, used market" — no specific price on card |
| G6 — Thermal | ⚠️ UNKNOWN | No thermal notes |
| G7 — ECC | ⚠️ RISK | Enterprise dual-Xeon — ECC RAM standard; confirm GPU driver operation not impacted |

**Gates cleared:** 1 partial (G3, G4)
**Gates blocking:** G1 (LIKELY FAIL — 2014-era platform), G2, G5, G6, G7
**Verdict:** ❌ LIKELY DISQUALIFIED — G1 (age) probable fail due to 2014-era Xeon E5-2600 platform. **Flag for manual confirmation before any action.** If manufacture date confirmed < 2018, remove from Pathway B shortlist.

---

### 3. Alienware Aurora R12 + RTX 3090 (Refurbished)
**File:** `09_alienware-aurora-r12-rtx-3090-refurbished.md`

| Gate | Status | Evidence from card |
|---|---|---|
| G1 — Age ≥ 2018 | ✅ LIKELY PASS | Alienware Aurora R12 = 2021 (Intel 11th gen / Rocket Lake). Confirm exact manufacture date. |
| G2 — PCIe slots | ⚠️ UNKNOWN | No PCIe slot info on card; OEM gaming chassis — likely single x16 only |
| G3 — PSU | ⚠️ UNKNOWN | No PSU spec on card |
| G4 — GPU VRAM | ✅ LIKELY | GPU listed as "24 GB" — RTX 3090 confirmed in title; meets ≥ 16 GB |
| G5 — Budget | ⚠️ BORDERLINE | Price listed as $3,090 AUD — within budget, but GPU may be separate; confirm total |
| G6 — Thermal | ⚠️ RISK | Alienware Aurora R12 uses proprietary OEM chassis and PSU; known thermal constraints under sustained GPU load |
| G7 — ECC | ✅ LIKELY PASS | Consumer gaming chassis — non-ECC RAM standard |

**Gates cleared:** G1 (likely), G4 (likely), G7 (likely)
**Gates blocking:** G2 (PCIe layout for dual GPU — OEM gaming chassis strongly suspected single-GPU only), G3 (PSU unknown), G5 (confirm total cost), G6 (thermal flag)
**Verdict:** ⚠️ SINGLE GPU ONLY — OEM Alienware chassis is almost certainly not dual-GPU capable. If Pathway B requires dual GPU potential, this is likely a poor fit. Suitable as **single 24 GB GPU** candidate only. Needs PCIe + PSU + thermal manual verification.

---

### 4. Recompute Dell Precision 5820 Tower + ThinkPad T14s Bundle
**File:** `18_recompute-dell-precision-5820-tower-act-thinkpad-t14s-pairing.md`

| Gate | Status | Evidence from card |
|---|---|---|
| G1 — Age ≥ 2018 | ✅ LIKELY PASS | Dell Precision 5820 = 2018–2021 era (Xeon W-2100/2200 series). Confirm exact model year. |
| G2 — PCIe slots | ⚠️ UNKNOWN | No PCIe slot info on card |
| G3 — PSU | ⚠️ UNKNOWN | No PSU spec on card |
| G4 — GPU VRAM | ✅ PARTIAL | GPU listed as "24 GB" — confirm exact GPU model |
| G5 — Budget | ⚠️ BORDERLINE | Price listed as $3,558 AUD — at upper range; includes laptop bundle (ThinkPad T14s) which may not be needed |
| G6 — Thermal | ⚠️ UNKNOWN | Enterprise workstation chassis — generally better thermal design than OEM gaming; unconfirmed |
| G7 — ECC | ⚠️ RISK | Xeon W platform — ECC RAM expected; confirm GPU driver compatibility |

**Gates cleared:** G1 (likely), G4 (partial)
**Gates blocking:** G2, G3, G5 (borderline — bundled laptop inflates cost), G6, G7
**Verdict:** ⚠️ CONDITIONAL — G1 likely passes (2018+ platform). Bundle includes ThinkPad T14s which may inflate cost beyond useful range if workstation alone is the target. Need unbundled price, PCIe layout, PSU spec, and ECC confirmation.

---

### 5. Acer Predator Orion 7000 — RTX 4080 (Refurbished)
**File:** `26_acer-predator-orion-7000-rtx-4080-super.md`

| Gate | Status | Evidence from card |
|---|---|---|
| G1 — Age ≥ 2018 | ✅ PASS | Acer Predator Orion 7000 = 2022 (Intel i9-14900K confirmed on card). Well within 2018 cutoff. |
| G2 — PCIe slots | ⚠️ UNKNOWN | OEM gaming chassis — likely single x16 primary slot; dual GPU support unclear |
| G3 — PSU | ⚠️ UNKNOWN | No PSU spec on card; OEM Acer PSU may be limiting |
| G4 — GPU VRAM | ✅ PARTIAL | RTX 4080 16 GB (Ada Lovelace) confirmed — meets ≥ 16 GB floor |
| G5 — Budget | ❌ OVER BUDGET | Price listed as ~$3,699 AUD — already at budget ceiling before any GPU addition |
| G6 — Thermal | ⚠️ FLAG | Card notes: "Loud under sustained AI load." Active flag on card. |
| G7 — ECC | ✅ PASS | Consumer gaming chassis — non-ECC DDR5 (32 GB DDR5 confirmed on card) |

**Gates cleared:** G1 ✅, G4 ✅ (single GPU), G7 ✅
**Gates blocking:** G2 (dual GPU unclear), G3 (PSU unknown), G5 (budget tight — no headroom for GPU additions), G6 (thermal flag active)
**Verdict:** ❌ WEAK CANDIDATE FOR PATHWAY B — Single GPU already installed (16 GB, meets floor). But: budget headroom is minimal, dual GPU path not viable in OEM chassis, thermal flag raised. Best evaluated as a **single 16 GB GPU ready-to-run** option only, not a growth platform.

---

## Summary Table

| Card | G1 Age | G2 PCIe | G3 PSU | G4 VRAM | G5 Budget | G6 Thermal | G7 ECC | Verdict |
|---|---|---|---|---|---|---|---|---|
| HP Z4 G4 | UNKNOWN | UNKNOWN | ⚠️ FLAGGED | ✅ 24 GB | ✅ likely | UNKNOWN | ⚠️ risk | Not gate-ready |
| Dell 7910 | ❌ likely fail | UNKNOWN | ✅ 1300W | ✅ 24 GB | UNKNOWN | UNKNOWN | ⚠️ risk | Likely disqualified (age) |
| Alienware R12 | ✅ 2021 | ⚠️ OEM limit | UNKNOWN | ✅ 24 GB | ✅ $3,090 | ⚠️ flag | ✅ | Single GPU only |
| Dell 5820 Bundle | ✅ likely | UNKNOWN | UNKNOWN | ✅ 24 GB | ⚠️ $3,558 | UNKNOWN | ⚠️ risk | Conditional — needs unbundled price |
| Acer Orion 7000 | ✅ 2022 | ⚠️ OEM limit | UNKNOWN | ✅ 16 GB | ❌ $3,699 | ⚠️ flagged | ✅ | Weak — no headroom |

---

## Priority Manual Lookup Actions (Pathway B)

| Priority | Card | Field to Verify |
|---|---|---|
| 🔴 HIGH | Dell Precision 7910 | Manufacture year — confirm whether pre-2018 → DISQUALIFY |
| 🔴 HIGH | HP Z4 G4 | PSU model + wattage — card explicitly flags this as unverified |
| 🔴 HIGH | HP Z4 G4 | Manufacture date — confirm ≥ 2018 |
| 🟡 MED | All 5 cards | PCIe x16 slot count — confirm dual GPU capability (except Alienware R12 and Acer Orion which are OEM gaming, likely single-GPU only) |
| 🟡 MED | HP Z4 G4, Dell 5820 | ECC RAM — confirm GPU driver operation not blocked |
| 🟡 MED | Dell 5820 | Unbundled price (workstation only, without ThinkPad) |
| 🟢 LOW | Alienware R12 | PSU model + wattage |
| 🟢 LOW | Acer Orion 7000 | PSU model + wattage (informational — already weak candidate) |
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/vram_agent_spec.md
`````markdown
# VRAM Architecture Spec Agent – Design Notes

## Purpose

This agent rewrites `Local LLM GPU VRAM Analysis` into a rigorous, versioned system-architecture specification for local AI deployments, safe for NotebookLM ingestion and long-term maintenance.

## Superpowers

- **STRUCTURE_REWRITE**  
  Reorder and normalize the document into the canonical section sequence used across the hardware project.

- **SPEC_EXTRACTION**  
  Extract only hardware and workload facts found in:
  - `NotebookLM_Workspaces/**`
  - `Policy_Pack/**`
  - `product_cards/**` and other explicit spec sheets  

  When a required metric is missing, the agent must emit:  
  `TODO: REQUIRED_METRIC_MISSING - <short description>`  
  and must not invent values.

- **FORMAL_DECISION_LOGIC**  
  Translate prose guidance into:
  - IF/THEN rules (boolean logic)
  - Tabular thresholds (e.g., VRAM tier vs workload type)
  - Deployment checklists

- **TRACEABILITY**  
  Every section and table includes a `Sources:` line listing filenames and headings, enabling human review and future regeneration.

- **VERSIONING**  
  The agent must:
  - Never overwrite the original VRAM document.
  - Write to `vram_architecture_spec_v1.md` (or increment `_v2`, `_v3` if later instructed).
  - Assume humans or other agents will diff versions in git.

## Required Sections

The output spec must include:

1. **Workload Definitions**  
   - Distinguish chat vs autonomous/agentic runs.  
   - Map workloads to approximate concurrency, context length, and I/O characteristics.

2. **Hardware Constraints**  
   - VRAM, memory bandwidth, PCIe, system RAM, PSU, NPU/accelerators.  
   - KV-cache scaling formula with clear variables and units.  
   - TODO markers wherever concrete numbers are not yet available.

3. **Hardware Tier Evaluation (12 / 16 / 24+ GB)**  
   - Describe supported workloads per tier.  
   - Note explicit limitations (context length, batch size, latency).  
   - Anchor statements to specific product_cards and policies when possible.

4. **Compatible Model Ecosystems**  
   - Local model families, quantization schemes, runtimes/toolchains.  
   - Apple unified memory vs NVIDIA CUDA, based only on documented sources.

5. **Total Cost of Ownership (TCO)**  
   - Table capturing GPU, CPU, RAM, SSD, cooling, PSU, and estimated energy.  
   - Explicit assumptions block at the top of the section.

6. **Deployment Logistics & Orchestration**  
   - Single-node vs multi-GPU considerations.  
   - Orchestration frameworks present in the repo (e.g., MCP servers, Genkit).  
   - Clear TODO items for anything referenced in the plan but not yet documented.

7. **Decision Logic & Checklists**  
   - IF/THEN rules for picking tiers and platforms (e.g., 16GB vs 24GB).  
   - A stepwise deployment checklist aligned to the 7 NotebookLM lanes.  
   - Optional: a small decision table matching workloads to recommended lanes.

## Safety and Hallucination Guards

- Use **only** the allowed sources; no outside knowledge.
- Never infer hardware specs from model names alone.
- Prefer TODO markers over guesses.
- Keep assumptions explicit in a dedicated “Assumptions” subsection early in the doc.

## Integration Notes

- The XML system prompt is the “machine-facing” contract.
- This markdown file is the “human-facing” design reference.
- Both should live alongside the generated `vram_architecture_spec_v1.md` in:
  `NotebookLM_Workspaces/01_Master_Hardware_Strategy_Ledger/`.
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/vram_architecture_spec_v1.md
`````markdown
# VRAM Architecture Specification for Local AI (v1)

## Project Goal & Rationale

**The Overarching Goal**: The user requires a new computer. 
**The Project Purpose**: To collate and synthesize extensive hardware research into a coherent, cohesive, comprehensive analysis and a structured, logical decision-making framework.
**The Rationale**: This thorough analysis stage is necessary to mitigate post-purchase cognitive dissonance. It empowers the user to confidently shortlist the best-value product propositions for their needs and lock in a purchase soon.

---

## 1. Workload Definitions

This section defines the computational and memory characteristics of local AI workloads in 2026.

| Workload Type | Characteristics | Concurrency | Context Requirements |
| :--- | :--- | :--- | :--- |
| **Chat / Assistant** | High responsiveness, single-turn or short multi-turn interaction. | Low (1-2 users) | 4K - 16K tokens |
| **Autonomous Agent** | Multi-step reasoning, tool use (terminal, browser), self-correction. | Moderate (1 agent) | 32K - 128K tokens |
| **Project Research** | Large document ingestion (PDFs, codebases), cross-referencing. | Low | 64K - 256K+ tokens |
| **Agentic Coding** | Codebase-wide analysis, autonomous debugging, multi-file edits. | Moderate | 64K - 128K tokens |

**Note on Agentic Reliability**: In agentic workflows, reliability (instruction following and tool use) is prioritized over raw speed. The "reasoning gap" between local and cloud models begins to close at the 24GB VRAM threshold.

**Sources**: `Local LLM GPU VRAM Analysis.md` §2.2, §5.2.

---

## 2. Hardware Constraints

### 2.1 Memory-Bandwidth Bottleneck
In the 2026 paradigm, LLM inference is primarily memory-bandwidth-bound. Generation speed is directly proportional to the GPU's memory bandwidth.

### 2.2 The VRAM Equation
The total VRAM footprint ($V_{total}$) is calculated as:
$$V_{total} = V_{weights} + V_{KV\_cache} + V_{overhead}$$

*   **$V_{weights}$**: Model parameters at specific quantization.
    *   Example (30B Model at Q4): ~18.0 - 20.0 GB.
*   **$V_{KV\_cache}$**: Stored attention states.
    *   32K-64K context: ~1.5 - 4.0 GB.
*   **$V_{overhead}$**: Backend/Runtime (CUDA, drivers, runtime graphs).
    *   Typical: ~0.75 - 1.0 GB.

### 2.3 Component Baseline Requirements
| Component | Minimum Requirement | Preferred for Growth |
| :--- | :--- | :--- |
| **VRAM** | 12GB (Entry), 16GB (Developer) | 24GB+ (Standard) |
| **Bandwidth** | 936 GB/s (3090) / 1008 GB/s (4090) | >1500 GB/s (5090) / Target >1000 GB/s |
| **System RAM** | 32GB | 64GB - 128GB (for weights offloading) |
| **PSU** | 850W (Single GPU) | 1000W - 1300W (Dual GPU growth) |
| **PCIe** | One x16 Slot | Dual x16 (x8/x8 electrical) |
| **NPU/TTFT** | < 500ms (30B models) | < 250ms (Reasoning/Thinking models) |

**Sources**: `Local LLM GPU VRAM Analysis.md` §1.1, `policy_expandable_workstation_scoring.md` §2.

---

## 3. Hardware Tier Evaluation

### 3.1 12GB Tier: Entry-Level Constraint
*   **Supported Workloads**: Short-context chat, basic code snippets, email drafting.
*   **Model Range**: 7B to 9B parameters.
*   **Limitations**: "Context cliff" occurs quickly; unusable for long-form research or complex agentic multi-turn runs.

### 3.2 16GB Tier: Developer’s Compromise
*   **Supported Workloads**: Multi-turn technical writing, professional coding (single-file), small-agent tasks.
*   **Model Range**: 14B to 20B parameters comfortably; 30B with aggressive quantization (Q2/Q3).
*   **Highlight**: **GPT-OSS 20B** (MXFP4) – 42 t/s on 16GB hardware.
*   **Limitations**: "VRAM envy"; unable to run 70B+ class frontier models effectively.

### 3.3 24GB Tier: Standard for Local Autonomy
*   **Supported Workloads**: Full project ingestion, autonomous agentic coding, massive RAG databases.
*   **Model Range**: 30B to 35B at high-quality quantization (Q5/Q6) with 64K+ context.
*   **Highlight**: **Llama 4 Scout** (109B MoE) at INT4 quantization – the gold standard for early 2026.
*   **Sources**: `Local LLM GPU VRAM Analysis.md` §3.1-3.3.

---

## 4. Compatible Model Ecosystems

| Model Family | Target Tier | Logic |
| :--- | :--- | :--- |
| **Gemma 4 (E2B/E4B)** | 8GB - 12GB | Optimized for edge/mobile via PLE architecture. |
| **Gemma 4 (26B A4B MoE)** | 16GB - 24GB | High "intelligence-per-GB" via Mixture-of-Experts. |
| **Gemma 4 (31B Dense)** | 24GB+ | Claude surrogate; 256K context window support. |
| **Qwen 3.5 (32B Coder)** | 24GB | Best-in-class coding for 24GB VRAM. |
| **Llama 4 Scout** | 24GB (MoE) | Top local LLM in early 2026 using INT4. |

**Architecture Comparison**:
*   **NVIDIA CUDA**: Standard for local LLM inference; high performance on INT4/MXFP4.
*   **Apple Unified Memory**: Separate "quiet" route; 64GB+ unified memory allows running larger models that exceed 24GB consumer GPU limits. **Bandwidth Comparison**: M4 Max (546 GB/s) vs. RTX 4090 (1008 GB/s). M5 estimated to improve TTFT by 3.3–4× via GPU-integrated Neural Accelerators.

**Sources**: `Local LLM GPU VRAM Analysis.md` §2, §5.

---

## 5. Total Cost of Ownership (TCO)

**Assumptions**: 3-year horizon. AUD pricing. used/refurbished vs. new. *Note: The used RTX 3090 CapEx split ($1,100 base + $1,100 GPU) is an estimate; the source (`Local LLM GPU VRAM Analysis.md`) only explicitly confirms the $2,200 total.*

| Component | Used RTX 3090 Build | New RTX 4090 Build | New RTX 5090 Build |
| :--- | :--- | :--- | :--- |
| **Base System (CPU/MB/RAM/PSU)** | ~$1,100 | ~$1,800 | ~$2,500 |
| **GPU** | ~$1,100 | ~$2,400 | ~$5,000 |
| **Cooling (Mod/Active Backplate)** | ~$200 | ~$0 (Stock) | ~$0 (Stock) |
| **Est. Power (Monthly)** | ~$15 | ~$25 | ~$40 |
| **Total CapEx (Upfront)** | **~$2,200** | **~$4,200** | **~$7,500** |
| **Break-even vs $100/mo Cloud** | **~15 Months** | **~29 Months** | **~52 Months** |

**Sources**: `Local LLM GPU VRAM Analysis.md` §4.2, `rubric_component_synergy_matrix.md`.

---

## 6. Deployment Logistics & Orchestration

### 6.1 Multi-GPU Considerations
*   **Single-Node**: Consumer setups (3090/4090) are limited by PCIe lane distribution.
*   **Enterprise/Workstation**: Dell Precision / HP Z-series allow for dual-GPU growth with proper x8/x8 or x16/x16 lane separation.
*   **Cooling**: Blower-style cards are preferred for multi-GPU density. RTX 3090 specifically requires VRAM thermal management (active backplate/waterblock).

### 6.2 Frameworks
*   **Ollama + OpenCode**: Low-friction developer setup for 16GB.
*   **OpenClaw + OpenCode**: Dual-agent setup for 24GB (mimicking Claude Code).
*   **Genkit / MCP Servers**: Orchestration pattern for autonomous tool execution; allows local agents (Gemma 4 / Qwen 3.5) to interact with local filesystems and browser-based tools securely.

**Sources**: `Local LLM GPU VRAM Analysis.md` §5.2, §6.1.

---

## 7. Decision Logic & Checklists

### 7.1 Platform Selection IF/THEN
*   **IF** ultimate goal is multi-year growth and multi-GPU (48GB+ VRAM) **THEN** choose **Expandable Workstation** (Xeon/Threadripper) with 1000W+ PSU.
*   **IF** budget is <$2,500 AUD and immediate 24GB VRAM is needed **THEN** choose **Used RTX 3090 Tower**.
*   **IF** mobility is critical and AI is secondary **THEN** choose **Apple 64GB Unified Memory** (MacBook/Studio).
*   **IF** desk space is limited but modularity is desired **THEN** choose **Mini PC + OCuLink eGPU**.

### 7.2 Deployment Checklist
1. [ ] **Verify PSU**: 850W minimum for single 3090/4090; 1000W+ for growth.
2. [ ] **Confirm PCIe Layout**: At least one x16 slot; dual slots for growth.
3. [ ] **Check Case Clearance**: 320mm+ for modern high-end GPUs.
4. [ ] **Ensure Airflow**: Mesh front or workstation ducting.
5. [ ] **VRAM Thermal Management**: Check backplate temps for 3090; consider active cooling.

**Sources**: `policy_expandable_workstation_scoring.md`, `rubric_component_synergy_matrix.md`, `Local LLM GPU VRAM Analysis.md` §7.
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/vram_orchestrator_notes.md
`````markdown
# VRAM Spec Orchestrator – Runbook

## Pipeline

1. **Architecture Spec Agent (Builder)**
   - System prompt: `vram_architecture_agent_system_prompt.xml`
   - Input: original VRAM doc + local sources
   - Output: `vram_architecture_spec_v1.md`

2. **Validator Agent**
   - System prompt: `vram_validator_agent_system_prompt.xml`
   - Inputs: `vram_architecture_spec_v1.md`, original VRAM doc, local sources
   - Outputs:
     - `vram_spec_validation_report.md`
     - `vram_spec_patch_suggestions.md`

3. **Human Review**
   - Read validation report summary.
   - Inspect patch suggestions.
   - Apply edits to produce `vram_architecture_spec_v2.md` (if needed).

4. **NotebookLM Integration**
   - Add latest `vram_architecture_spec_vX.md` to Notebook 1.
   - Reference it in `notebook_manifest.md` and `prompts.md`.

## Typical Usage

- When in doubt, ask the Orchestrator agent:
  - “Which step should I run next?”
  - “How do I run the validator on the latest spec?”
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/vram_spec_patch_suggestions.md
`````markdown
# VRAM Spec Patch Suggestions

Apply these manual edits to `vram_architecture_spec_v1.md` to resolve the issues identified in the validation report.

## Patch 1: Fix Vague TODO in Hardware Constraints
**Location**: Section 2.3 Component Baseline Requirements (Table)
**Issue**: The "Preferred for Growth" Bandwidth column has a vague TODO marker.
**Action**: Replace the cell contents.
```diff
- | **Bandwidth** | TODO: REQUIRED_METRIC_MISSING - Specify GB/s for 3090/4090/5090 | TODO: REQUIRED_METRIC_MISSING |
+ | **Bandwidth** | TODO: REQUIRED_METRIC_MISSING - Specify GB/s for 3090/4090/5090 | TODO: REQUIRED_METRIC_MISSING - Specify target GB/s memory bandwidth for future-proofing. |
```

## Patch 2: Add Missing Source Evidence for Apple vs NVIDIA
**Location**: Section 4 Compatible Model Ecosystems (Architecture Comparison)
**Issue**: The comparison makes claims about Apple unified memory exceeding 24GB limits without explicit spec backing from the product cards.
**Action**: Insert a TODO marker to force spec extraction.
```diff
- *   **Apple Unified Memory**: Separate "quiet" route; 64GB+ unified memory allows running larger models that exceed 24GB consumer GPU limits, but with potentially different memory-bandwidth characteristics.
+ *   **Apple Unified Memory**: Separate "quiet" route; 64GB+ unified memory allows running larger models that exceed 24GB consumer GPU limits. TODO: REQUIRED_METRIC_MISSING - Extract memory bandwidth specifications from Apple product cards to compare directly with NVIDIA CUDA performance.
```

## Patch 3: Clarify Inconclusive TCO Split
**Location**: Section 5 Total Cost of Ownership (TCO)
**Issue**: The $1,100 / $1,100 split for Base System / GPU is an estimation not explicitly found in the source text, which only specifies the $2,200 total and $950-$1,100 marketplace price.
**Action**: Add a disclaimer to the Assumptions block.
```diff
- **Assumptions**: 3-year horizon. AUD pricing. used/refurbished vs. new.
+ **Assumptions**: 3-year horizon. AUD pricing. used/refurbished vs. new. *Note: The used RTX 3090 CapEx split ($1,100 base + $1,100 GPU) is an estimate; the source (`Local LLM GPU VRAM Analysis.md`) only explicitly confirms the $2,200 total.*
```
`````

## File: NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/vram_spec_validation_report.md
`````markdown
# VRAM Architecture Spec Validation Report

## 1. Summary
**Status**: CONDITIONAL PASS
**Top 3 Issues**:
1. **Inconclusive Fact/TCO Split**: The TCO table breaks the $2,200 AUD RTX 3090 build into a $1,100 Base System and $1,100 GPU. While the total matches the source, the exact 50/50 split is not explicitly stated in `Local LLM GPU VRAM Analysis.md`.
2. **Missing Source Evidence for Apple vs NVIDIA**: The comparison relies on high-level strategy rather than explicit spec extraction from the `product_cards` regarding memory-bandwidth differences.
3. **Vague TODO Marker**: There is a blank `TODO: REQUIRED_METRIC_MISSING` in the bandwidth column that lacks instruction on what specific metric to find.

## 2. Structural Findings
*   **Section 1: Workload Definitions**: Present and populated.
*   **Section 2: Hardware Constraints**: Present and populated.
*   **Section 3: Hardware Tier Evaluation**: Present and populated.
*   **Section 4: Compatible Model Ecosystems**: Present and populated.
*   **Section 5: Total Cost of Ownership**: Present and populated.
*   **Section 6: Deployment Logistics & Orchestration**: Present and populated.
*   **Section 7: Decision Logic & Checklists**: Present and populated.
*   **Order**: Correct.
*   **Empty Sections**: None.

## 3. Fact Check Findings

| Claim / Metric | Source | Status |
| :--- | :--- | :--- |
| KV Cache size (~1.5-4GB for 32K-64K) | `Local LLM GPU VRAM Analysis.md` | CONFIRMED |
| GPT-OSS 20B at 42 t/s | `Local LLM GPU VRAM Analysis.md` | CONFIRMED |
| Llama 4 Scout 109B requires 24GB | `Local LLM GPU VRAM Analysis.md` | CONFIRMED |
| Break-even vs $100/mo Cloud | `Local LLM GPU VRAM Analysis.md` | CONFIRMED |
| RTX 3090 Total CapEx ~$2,200 | `Local LLM GPU VRAM Analysis.md` | CONFIRMED |
| RTX 3090 GPU cost ~$1,100 | `Local LLM GPU VRAM Analysis.md` | INCONCLUSIVE |
| Apple unified memory allows larger models | Strategy Ledger | INCONCLUSIVE (Needs explicit spec extraction) |

## 4. TODO Audit Findings

| Current TODO Marker | Rating | Suggested Rewrite |
| :--- | :--- | :--- |
| `TODO: REQUIRED_METRIC_MISSING - Specify GB/s for 3090/4090/5090` | CLEAR | Keep as is. |
| `TODO: REQUIRED_METRIC_MISSING` (Preferred Bandwidth) | VAGUE | `TODO: REQUIRED_METRIC_MISSING - Specify target GB/s memory bandwidth for future-proofing.` |
| `TODO: REQUIRED_METRIC_MISSING - Baseline TTFT for 2026 models` | CLEAR | Keep as is. |
| `TODO: REQUIRED_METRIC_MISSING - Describe specific orchestration patterns present in repo.` | CLEAR | Keep as is. |

## 5. Decision Logic Findings
*   The IF/THEN rules for platform selection accurately reflect the "Goal" and "Non-Negotiable Filters" outlined in `policy_expandable_workstation_scoring.md`.
*   The 850W minimum PSU and 320mm clearance checks directly map to the `rubric_component_synergy_matrix.md`.

## 6. Recommended Patches
See `vram_spec_patch_suggestions.md` for the concrete text edits to resolve the Top 3 Issues.
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/10_lenovo-thinkstation-p620-refurb.md
`````markdown
<!-- TAGS: #Desktop #Lenovo #ThinkStation #Refurbished #Track2-Candidate #NeedsVRAMVerification -->
---
id: lenovo-thinkstation-p620-refurb
category: desktop_towers_refurbished
name: Lenovo ThinkStation P620
gpu: NVIDIA Quadro P2000 (5GB GDDR5)
vram: 5 GB
price_aud: 1779
score: 7.5 (Requires GPU Upgrade)
---

# Lenovo ThinkStation P620 — eBay Refurbished

> ⚠️ **LLM VIABILITY ALERT:** This workstation comes with a **Quadro P2000 (5GB VRAM)**, which fails the 8GB VRAM floor out of the box. However, because the base system is incredibly well-priced ($1,779), it leaves massive budget headroom to purchase and drop in a used RTX 3090 (24GB) or RTX 4090.

## Track 2 Status
- **Pathway:** Pathway B (Refurbished Enterprise Workstation)
- **GOOD ENOUGH check:** ✅ **PASSED AS BAREBONE** — Must purchase secondary GPU.

## Overview
- **Price (AUD):** $1,779.00
- **Vendor (AU):** eBay AU
- **URL:** `https://www.ebay.com.au/itm/267617299269?var=567431065928`

## Key Specs
- **GPU:** NVIDIA Quadro P2000 5GB (Requires upgrade)
- **CPU:** AMD Ryzen Threadripper PRO 3945WX (12 Core / 24 Thread)
- **RAM:** 32 GB or 64 GB
- **Storage:** 1 TB SSD
- **Condition:** Refurbished

## Conclusion
The ThinkStation P620 is a powerhouse chassis that fully supports massive PCIe expansion and high-wattage dual GPU setups. If the price is low enough to allow you to purchase a used RTX 3090 (or two) within the $4,500 budget, this is a top-tier Pathway B candidate. If it already includes an 8 GB+ GPU, it must be evaluated on total value.
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/18_recompute-dell-precision-5820-tower-act-thinkpad-t14s-pairing.md
`````markdown
<!-- TAGS: #Workstation #NVIDIA #VRAM-24GB #Refurbished #Bundle #Expandable #PCIe-x16x16 #PrimaryWorkstation #SecondaryLaptop #AgenticAI #Shortlist -->
<!-- PRODUCT CARD START: Recompute Dell Precision 5820 Tower + ACT ThinkPad T14s pairing -->
### [90 / 100] — Recompute Dell Precision 5820 Tower + ACT ThinkPad T14s pairing

- **Category**: Workstation / Secondary Laptop
- **Condition**: UNKNOWN
- **Price (AUD)**: $3,558 (⚠️ FLAG FOR REVIEW: Includes ThinkPad T14s. Find unbundled tower-only price or mark "bundle only")
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: 24GB
- **CPU**: UNKNOWN
- **RAM**: 24GB
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 90 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 90 / 110 (81%)

#### AI Capability Summary
Capable of running models suitable for 24GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 24GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Recompute Dell Precision 5820 Tower + ACT ThinkPad T14s pairing -->
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/28_hp-z4-g4-rtx-3090-refurbished.md
`````markdown
<!-- TAGS: #Workstation #NVIDIA #VRAM-24GB #Refurbished #Used #Expandable #PCIe-x16x16 #PrimaryWorkstation #AgenticAI #Shortlist -->
---
id: hp-z4-g4-rtx-3090-refurbished
category: desktop
name: HP Z4 G4 Workstation + Used RTX 3090 24 GB
gpu: NVIDIA GeForce RTX 3090 (24 GB)
vram: 24 GB
score: 92
---

# HP Z4 G4 Workstation + Used RTX 3090 24 GB

## Overview
- **VRAM Tier:** Priority 1 — 24 GB
- **Adjusted Score:** 92 / 110
- **Price (AUD):** ~$2,800–$3,500 combined (refurb unit + used GPU)
- **Condition:** Refurbished workstation + used/refurb GPU

## Key Specs
- **GPU:** NVIDIA GeForce RTX 3090 24 GB (added separately)
- **CPU:** Intel Xeon W-class (HP Z4 G4 platform)
- **RAM:** Up to 128 GB ECC DDR4
- **Storage:** Multiple M.2 and SATA slots
- **PSU:** HP Z4 G4 750 W OEM PSU — VERIFY adequacy for RTX 3090 TDP
- **Form factor:** Enterprise workstation tower

## AI Capability Summary
Enterprise-grade RAM headroom (up to 128 GB ECC DDR4) makes this a compelling CPU-offload platform. Useful for running oversized models by offloading layers to system RAM. 24 GB VRAM handles 30B/34B Q4 natively.
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-003_dell-precision-5820-tower-bundle.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: dell-precision-5820-tower-bundle
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Dell Precision 5820 Tower Bundle
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $3558 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Dell Precision 5820 Tower Bundle

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3558 AUD
- **Retailer:** Recompute / Australian Computer Traders
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Xeon W-2235
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Older workstation platform but provides a complete out-of-the-box dual-device ecosystem

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-004_hp-z4-g4-workstation-refurbished-base.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: hp-z4-g4-workstation-refurbished-base
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: HP Z4 G4 Workstation (Refurbished Base)
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $3500 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# HP Z4 G4 Workstation (Refurbished Base)

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3500 AUD
- **Retailer:** Refurbishers / eBay
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Xeon
- **RAM:** 128 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Highly affordable foundational build that supplies the massive power and space requirements needed for a 24GB GPU

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-005_dell-precision-t7910-refurbished-base.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: dell-precision-t7910-refurbished-base
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Dell Precision T7910 (Refurbished Base)
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $1875 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Dell Precision T7910 (Refurbished Base)

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $1875 AUD
- **Retailer:** System Liquidation / eBay
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Dual Xeon E5-2680 v4
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
The absolute cheapest foundational workstation; featuring a factory-installed 1300W PSU

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-006_alienware-aurora-r12-refurbished.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: alienware-aurora-r12-refurbished
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Alienware Aurora R12 (Refurbished)
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $3884 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Alienware Aurora R12 (Refurbished)

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3884 AUD
- **Retailer:** Dick Smith / UN Tech
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** i9-11900K
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Solid consumer-oriented pre-built option to secure 24GB of VRAM

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-034_lenovo-thinkstation-p330-tiny-desktop.md
`````markdown
<!-- TAGS: #Desktop #VRAM-Unknown #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: lenovo-thinkstation-p330-tiny-desktop
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Lenovo ThinkStation P330 Tiny Desktop
gpu: UNKNOWN
vram: UNKNOWN
unified_memory: UNKNOWN
price_aud: $469.00 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Lenovo ThinkStation P330 Tiny Desktop

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $469.00 AUD
- **Retailer:** Recompute
- **URL:** [https://www.recompute.com.au/lenovo-thinkstation-p330-tiny-desktop-intel-core-i7-8700-16gb-ram-256gb-ssd/](https://www.recompute.com.au/lenovo-thinkstation-p330-tiny-desktop-intel-core-i7-8700-16gb-ram-256gb-ssd/)
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** UNKNOWN
- **VRAM:** UNKNOWN
- **Unified Memory:** UNKNOWN
- **CPU:** Core i7-8700
- **RAM:** 16 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Tiny desktop for basic tasks

## AI Capability Summary
UNKNOWN — to be completed after manual spec verification.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [ ] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-040_recompute-dell-precision-5820-tower-act-thinkpad.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: recompute-dell-precision-5820-tower-act-thinkpad
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Recompute Dell Precision 5820 Tower + ACT ThinkPad
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $3558 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Recompute Dell Precision 5820 Tower + ACT ThinkPad

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3558 AUD
- **Retailer:** Recompute + Australian Computer Traders
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Xeon W-2235
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Older workstation platform; not pretty or especially quiet

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-041_act-dell-3650-a4000.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: act-dell-3650-a4000
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: ACT Dell 3650 + A4000
gpu: RTX A4000
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $1800 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# ACT Dell 3650 + A4000

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $1800 AUD
- **Retailer:** UNKNOWN
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX A4000
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** 128 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Moderate performance

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-042_hp-z4-g4-used-3090.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: hp-z4-g4-used-3090
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: HP Z4 G4 + used 3090
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $2800 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# HP Z4 G4 + used 3090

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2800 AUD
- **Retailer:** UNKNOWN
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** 128 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Strong FP16 performance

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-046_acer-predator-orion-7000-rtx-4080-refurbished.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: acer-predator-orion-7000-rtx-4080-refurbished
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Acer Predator Orion 7000 RTX 4080 refurbished
gpu: RTX 4080
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $3699 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Acer Predator Orion 7000 RTX 4080 refurbished

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3699 AUD
- **Retailer:** Acer AU Clearance
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4080
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** i9-14900K
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Refurbished prebuilt

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-047_alienware-aurora-r12-rtx-3090-refurbished.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: alienware-aurora-r12-rtx-3090-refurbished
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Alienware Aurora R12 RTX 3090 refurbished
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $3884 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Alienware Aurora R12 RTX 3090 refurbished

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3884 AUD
- **Retailer:** Dick Smith / UN Tech
- **URL:** [https://www.dicksmith.com.au/](https://www.dicksmith.com.au/)
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** i9-11900K
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Solid consumer-oriented pre-built option to secure 24GB of VRAM

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-065_dell-optiplex-5060-sff.md
`````markdown
<!-- TAGS: #Desktop #VRAM-Unknown #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: dell-optiplex-5060-sff
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Dell OptiPlex 5060 SFF
gpu: UNKNOWN
vram: UNKNOWN
unified_memory: UNKNOWN
price_aud: $238.99 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Dell OptiPlex 5060 SFF

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $238.99 AUD
- **Retailer:** ReUse Computers
- **URL:** [https://reusecomputers.com/products/dell-optiplex-5060-sff](https://reusecomputers.com/products/dell-optiplex-5060-sff)
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** UNKNOWN
- **VRAM:** UNKNOWN
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Desktop

## AI Capability Summary
UNKNOWN — to be completed after manual spec verification.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [ ] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/02_Refurbished_Desktop_Towers/intake-066_dell-precision-5820-tower-workstation-32gb-ram.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Refurb desktop -->
---
id: dell-precision-5820-tower-workstation-32gb-ram
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Dell Precision 5820 Tower Workstation (32GB RAM)
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $2399.00 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Dell Precision 5820 Tower Workstation (32GB RAM)

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2399.00 AUD
- **Retailer:** Recompute
- **URL:** [https://www.recompute.com.au/dell-precision-5820-tower-workstation-intel-xeon-w-2235-32gb-ram-1tb-ssd-2tb-ssd-nvidia-geforce-rtx-3090/](https://www.recompute.com.au/dell-precision-5820-tower-workstation-intel-xeon-w-2235-32gb-ram-1tb-ssd-2tb-ssd-nvidia-geforce-rtx-3090/)
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Xeon W-2235
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Tower Workstation

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/01_lenovo-thinkstation-basic.md
`````markdown
<!-- TAGS: #Desktop #Lenovo #ThinkStation #Track2-Candidate #NeedsVRAMVerification -->
---
id: lenovo-thinkstation-basic-student
category: desktop_tower_new
name: Lenovo ThinkStation (Basic Config)
gpu: UNKNOWN
vram: UNKNOWN
price_aud: 3350
score: UNKNOWN — Pending Specs
---

# Lenovo ThinkStation (Basic Config) — Student Pricing

> ⚠️ **LLM VIABILITY ALERT:** This workstation is currently priced at **$3,350 AUD** via student discount. However, we must strictly verify the GPU configuration. It **MUST** meet the new 8 GB VRAM minimum rule to be viable for local LLM workloads (though 12GB+ is strongly preferred).

## Track 2 Status
- **Pathway:** Pathway A or C equivalent (Pre-built New)
- **GOOD ENOUGH check:** PENDING — Awaiting exact GPU and VRAM specs.

## Overview
- **Price (AUD):** $3,350 (Student Price)
- **Vendor (AU):** Lenovo Australia (Education Store)
- **In stock in AU:** Yes (Custom to order)

## Evaluation for Local LLMs
At $3,350, a basic ThinkStation chassis is an excellent foundation (often offering superior PCIe lane expansion and PSU headroom). 
**However**, if the "Basic Config" only includes an entry-level professional GPU (e.g., an RTX A2000 with less than 8 GB), it will fail our strict requirements. 

**Recommendation:** Before purchasing, ensure the configurator is upgraded to at least an 8 GB card (e.g., RTX 4060 Ti, A4000, or equivalent). If that pushes the price over budget, consider buying the chassis with the lowest-tier GPU and sourcing a used 24 GB RTX 3090 locally to maximize its potential.
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/12_supertech-rtx-4090-gaming-pc.md
`````markdown
<!-- TAGS: #DesktopTower #NVIDIA #VRAM-24GB #New #SingleGPU #PrimaryWorkstation #AgenticAI #ImageGeneration #NeedsReview -->
<!-- PRODUCT CARD START: Supertech RTX 4090 Gaming PC -->
### [92 / 100] — Supertech RTX 4090 Gaming PC

- **Category**: Windows Tower / Desktop
- **Condition**: UNKNOWN
- **Price (AUD)**: $5,799 sale; new
- **Vendor**: UNKNOWN
- **URL**: https://supertechcomputers.com.au/product/rtx4090-gaming-pc/

#### Hardware Profile
- **GPU**: 24GB
- **CPU**: UNKNOWN
- **RAM**: Highest raw local-AI capability in previous report, but beyond preferred budget and likely overkill unless 24GB VRAM is non-negotiable.
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 14/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 92 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 92 / 110 (83%)

#### AI Capability Summary
Capable of running models suitable for 24GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 24GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Supertech RTX 4090 Gaming PC -->
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/25_ple-ai-advanced-rtx-5070-ti.md
`````markdown
<!-- TAGS: #DesktopTower #NVIDIA #VRAM-16GB #New #SingleGPU #PrimaryWorkstation #Coding #NeedsReview -->
---
id: ple-ai-advanced-rtx-5070-ti
category: desktop
name: PLE AI Advanced RTX 5070 Ti 16 GB Desktop
gpu: NVIDIA GeForce RTX 5070 Ti (16 GB)
vram: 16 GB
score: 90
---

# PLE AI Advanced RTX 5070 Ti 16 GB Desktop

## Overview
- **VRAM Tier:** Priority 3 — 16 GB
- **Adjusted Score:** 90 / 110
- **Price (AUD):** ~$3,907 built to order
- **Vendor:** PLE Computers AU

## Key Specs
- **GPU:** NVIDIA GeForce RTX 5070 Ti 16 GB (Blackwell)
- **CPU:** AMD Ryzen 7 9700X
- **RAM:** 32 GB DDR5-6000 (upgrade to 64 GB recommended)
- **Storage:** 2 TB NVMe SSD
- **PSU:** Built-to-order specification; verify wattage
- **Form factor:** Gaming tower

## AI Capability Summary
Best clean-warranty AU retail desktop path for 7B–14B models and strong SDXL/FLUX image generation. 16 GB is adequate for current mainstream local LLM use but is below the 24 GB target for serious 30B/34B model work.
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/27_scorptec-eclipse-rtx-5070-ti.md
`````markdown
<!-- TAGS: #DesktopTower #NVIDIA #VRAM-16GB #New #SingleGPU #PrimaryWorkstation #NeedsReview -->
---
id: scorptec-eclipse-rtx-5070-ti
category: desktop
name: Scorptec Eclipse RTX 5070 Ti
gpu: NVIDIA GeForce RTX 5070 Ti (16 GB)
vram: 16 GB
score: 88
---

# Scorptec Eclipse RTX 5070 Ti

## Overview
- **VRAM Tier:** Priority 3 — 16 GB
- **Adjusted Score:** 88 / 110
- **Price (AUD):** ~$3,399
- **Vendor:** Scorptec Computers AU

## Key Specs
- **GPU:** NVIDIA GeForce RTX 5070 Ti 16 GB (Blackwell)
- **CPU:** Ryzen 7 / Intel i7-class
- **RAM:** 32 GB DDR5 typical
- **Storage:** 1–2 TB NVMe
- **PSU:** 750–850 W typical
- **Form factor:** Gaming tower

## AI Capability Summary
Strong entry-level local AI desktop. Quiet under inference compared to gaming use. 16 GB VRAM covers mainstream 7B–14B local model work confidently.
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-001_dual-rtx-3090-24gb-gpu-pro-workstation-pure-501-black.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-48GB+ #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: dual-rtx-3090-24gb-gpu-pro-workstation-pure-501-black
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Dual RTX 3090 24GB GPU Pro Workstation (Pure 501 Black)
gpu: RTX 3090
vram: 48 GB
unified_memory: UNKNOWN
price_aud: $5998.50 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Dual RTX 3090 24GB GPU Pro Workstation (Pure 501 Black)

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $5998.50 AUD
- **Retailer:** Green Beast Gaming
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 48 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ultra 7 265K
- **RAM:** 128 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Incredible pre-built value for running massive 70B+ unquantized models utilizing dual 3090s

## AI Capability Summary
Exceptional — 48 GB+ VRAM supports 70B+ models fully in VRAM at Q4.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-002_supertech-computers-rtx-4090-gaming-pc.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: supertech-computers-rtx-4090-gaming-pc
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Supertech Computers RTX 4090 Gaming PC
gpu: RTX 4090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $5799 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Supertech Computers RTX 4090 Gaming PC

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $5799 AUD
- **Retailer:** Supertech Computers
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** i7-14700K
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Offers the highest raw local-AI capability in a brand-new retail build

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-007_ple-ai-advanced-rtx-5070-ti-desktop.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: ple-ai-advanced-rtx-5070-ti-desktop
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: PLE AI Advanced RTX 5070 Ti Desktop
gpu: RTX 5070 Ti
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $3907 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# PLE AI Advanced RTX 5070 Ti Desktop

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3907 AUD
- **Retailer:** PLE Computers
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5070 Ti
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 7 9700X
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Clean fully warrantied local Australian retail path under $4k

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-008_evatech-y40k-rtx-4080-super-gaming-pc.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: evatech-y40k-rtx-4080-super-gaming-pc
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Evatech Y40K RTX 4080 Super Gaming PC
gpu: RTX 4080 Super
vram: 16 GB
unified_memory: UNKNOWN
price_aud: UNKNOWN
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Evatech Y40K RTX 4080 Super Gaming PC

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** UNKNOWN
- **Retailer:** Evatech Australia
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4080 Super
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** i9-14900KF
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Powerful tier-down compromise option offering excellent compute speed

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-016_okinos-studio-pro-rtx-5070-ti3090.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: okinos-studio-pro-rtx-5070-ti3090
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: OKINOS Studio Pro - RTX 5070 Ti/3090
gpu: RTX 5070 Ti
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $3599 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# OKINOS Studio Pro - RTX 5070 Ti/3090

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3599 AUD
- **Retailer:** Mike PC AU
- **URL:** [https://mikepc.com.au/products/okinos-studio-pro-rtx-5070-ti-intel-i9-14900kf?variant=43641754124366](https://mikepc.com.au/products/okinos-studio-pro-rtx-5070-ti-intel-i9-14900kf?variant=43641754124366)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5070 Ti
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Intel i9-14900KF
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Topaz Snow PC equivalent prebuilt

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-022_gaming-pc-intel-i9-12th-gen-nvidia-rtx-3090.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: gaming-pc-intel-i9-12th-gen-nvidia-rtx-3090
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Gaming PC Intel i9-12th Gen NVIDIA RTX 3090
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $5271.98 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Gaming PC Intel i9-12th Gen NVIDIA RTX 3090

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $5271.98 AUD
- **Retailer:** sukkdawod-0
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** i9-12th Gen
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
eBay prebuilt

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-023_gaming-pc-jonsbo-mod-5-asrock-x570-aqua.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #ConditionUnknown #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Desktop (uncategorised) -->
---
id: gaming-pc-jonsbo-mod-5-asrock-x570-aqua
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Gaming PC Jonsbo MOD 5 ASRock x570 Aqua
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $3898.30 AUD
condition: UNKNOWN
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Gaming PC Jonsbo MOD 5 ASRock x570 Aqua

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3898.30 AUD
- **Retailer:** ale_deconno
- **URL:** UNKNOWN
- **Condition:** UNKNOWN
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 9 5950X
- **RAM:** 128 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
eBay custom build

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-024_skytech-prism-4-gaming-pc.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: skytech-prism-4-gaming-pc
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Skytech Prism 4 Gaming PC
gpu: RTX 5090
vram: 32 GB
unified_memory: UNKNOWN
price_aud: $6599.98 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Skytech Prism 4 Gaming PC

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $6599.98 AUD
- **Retailer:** Newegg
- **URL:** [https://www.newegg.com/skytech-gaming-desktop-pcs-geforce-rtx-5090-amd-ryzen-7-9800x3d-32gb-ddr5-2tb-nvme-ssd-st-prism4-1793-b-al-black/p/3D5-000Z-002D9](https://www.newegg.com/skytech-gaming-desktop-pcs-geforce-rtx-5090-amd-ryzen-7-9800x3d-32gb-ddr5-2tb-nvme-ssd-st-prism4-1793-b-al-black/p/3D5-000Z-002D9)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090
- **VRAM:** 32 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 7 9800X3D
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
High-end 5090 prebuilt

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-025_hp-omen-45l-gt22-3090-gaming-pc.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: hp-omen-45l-gt22-3090-gaming-pc
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: HP OMEN 45L GT22-3090 Gaming PC
gpu: RTX 5090
vram: 32 GB
unified_memory: UNKNOWN
price_aud: $7499.98 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# HP OMEN 45L GT22-3090 Gaming PC

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $7499.98 AUD
- **Retailer:** Newegg
- **URL:** [https://www.newegg.com/hp-gaming-desktop-pcs-nvidia-geforce-rtx-5090-32gb-gddr7-intel-core-ultra-9-285k-64gb-ddr5-2tb-nvme-ssd-omen-45l-black/p/3D5-0005-03SF5](https://www.newegg.com/hp-gaming-desktop-pcs-nvidia-geforce-rtx-5090-32gb-gddr7-intel-core-ultra-9-285k-64gb-ddr5-2tb-nvme-ssd-omen-45l-black/p/3D5-0005-03SF5)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090
- **VRAM:** 32 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 285K
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
OEM high-end 5090 prebuilt

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-026_clx-horus-gaming-desktop.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: clx-horus-gaming-desktop
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: CLX Horus Gaming Desktop
gpu: RTX 5090
vram: 32 GB
unified_memory: UNKNOWN
price_aud: $9899.98 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# CLX Horus Gaming Desktop

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $9899.98 AUD
- **Retailer:** Newegg
- **URL:** [https://www.newegg.com/clx-horus-gaming-desktop-pcs-nvidia-geforce-rtx-5090-amd-ryzen-9-9950x3d-96gb-ddr5-2-tb-ssd-8tb-hdd-tgmhorrtz5305bm-black/p/3D5-000B-00312](https://www.newegg.com/clx-horus-gaming-desktop-pcs-nvidia-geforce-rtx-5090-amd-ryzen-9-9950x3d-96gb-ddr5-2-tb-ssd-8tb-hdd-tgmhorrtz5305bm-black/p/3D5-000B-00312)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090
- **VRAM:** 32 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 9 9950X3D
- **RAM:** 96 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Extreme tier 5090 desktop

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-028_dual-rtx-4090-24gb-gpu-pro-workstation.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-48GB+ #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: dual-rtx-4090-24gb-gpu-pro-workstation
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Dual RTX 4090 24GB GPU Pro Workstation
gpu: RTX 4090
vram: 48 GB
unified_memory: UNKNOWN
price_aud: $11998.50 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Dual RTX 4090 24GB GPU Pro Workstation

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $11998.50 AUD
- **Retailer:** Green Beast Gaming
- **URL:** [https://greenbeastgaming.com/products/dual-rtx-4090-24gb-gpu-pro-workstation-intel-pure-501-black](https://greenbeastgaming.com/products/dual-rtx-4090-24gb-gpu-pro-workstation-intel-pure-501-black)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4090
- **VRAM:** 48 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Dual 4090 workstation

## AI Capability Summary
Exceptional — 48 GB+ VRAM supports 70B+ models fully in VRAM at Q4.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-029_dual-rtx-5090-32gb-gpu-pro-workstation.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-48GB+ #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: dual-rtx-5090-32gb-gpu-pro-workstation
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Dual RTX 5090 32GB GPU Pro Workstation
gpu: RTX 5090
vram: 64 GB
unified_memory: UNKNOWN
price_aud: $14998.50 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Dual RTX 5090 32GB GPU Pro Workstation

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $14998.50 AUD
- **Retailer:** Green Beast Gaming
- **URL:** [https://greenbeastgaming.com/products/dual-rtx-5090-32gb-gpu-pro-workstation-intel-pure-501-black](https://greenbeastgaming.com/products/dual-rtx-5090-32gb-gpu-pro-workstation-intel-pure-501-black)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090
- **VRAM:** 64 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Dual 5090 workstation

## AI Capability Summary
Exceptional — 48 GB+ VRAM supports 70B+ models fully in VRAM at Q4.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-032_topaz-snow-pc.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: topaz-snow-pc
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: TOPAZ SNOW PC
gpu: RTX 5070 Ti
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $2699.00 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# TOPAZ SNOW PC

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2699.00 AUD
- **Retailer:** Mike PC AU
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5070 Ti
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 7 7700
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Prebuilt desktop

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-033_vision-onyx-pc.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: vision-onyx-pc
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: VISION ONYX PC
gpu: RTX 5080
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $3999.00 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# VISION ONYX PC

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3999.00 AUD
- **Retailer:** Mike PC AU
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5080
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 7 9800X3D
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Prebuilt desktop

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-035_specialized-evga-3090-custom-build.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #ConditionUnknown #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Desktop (uncategorised) -->
---
id: specialized-evga-3090-custom-build
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Specialized EVGA 3090 Custom Build
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $2953 AUD
condition: UNKNOWN
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Specialized EVGA 3090 Custom Build

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2953 AUD
- **Retailer:** Tech Junction
- **URL:** UNKNOWN
- **Condition:** UNKNOWN
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core i9-12900K
- **RAM:** 16 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Custom built using EVGA 3090

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-037_thermaltake-horizon-xtreme-tower-x1-carbon.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: thermaltake-horizon-xtreme-tower-x1-carbon
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Thermaltake Horizon Xtreme tower + X1 Carbon
gpu: RTX 4080 Super
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $4543 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Thermaltake Horizon Xtreme tower + X1 Carbon

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $4543 AUD
- **Retailer:** Umart + Australian Computer Traders
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4080 Super
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 7 7800X3D
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
16GB VRAM limits 32B local coding models; pairing slightly over budget

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-043_ple-pixel-5070-ti.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: ple-pixel-5070-ti
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: PLE Pixel 5070 Ti
gpu: RTX 5070 Ti
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $3799 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# PLE Pixel 5070 Ti

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3799 AUD
- **Retailer:** PLE Computers
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5070 Ti
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Strong quiet build

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-044_scorptec-eclipse-rtx-5070-ti-gaming-pc.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #New #TrackUnknown #Verified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: scorptec-eclipse-rtx-5070-ti-gaming-pc
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Scorptec Eclipse RTX 5070 Ti Gaming PC
gpu: RTX 5070 Ti
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $3399 AUD
condition: New
au_stock: UNKNOWN
verification: Verified
status: Active
score: UNKNOWN — pending manual review
---

# Scorptec Eclipse RTX 5070 Ti Gaming PC

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3399 AUD
- **Retailer:** Scorptec
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5070 Ti
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 7 265K
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Tier-down option

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-048_metrocom-custom-5700x-rtx-4070-super.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-8GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: metrocom-custom-5700x-rtx-4070-super
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Metrocom Custom 5700X RTX 4070 Super
gpu: RTX 4070 Super
vram: 12 GB
unified_memory: UNKNOWN
price_aud: $2350 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Metrocom Custom 5700X RTX 4070 Super

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2350 AUD
- **Retailer:** Metrocom
- **URL:** [https://metrocom.com.au/best-gaming-pcs-australia-2025/](https://metrocom.com.au/best-gaming-pcs-australia-2025/)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4070 Super
- **VRAM:** 12 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 7 5700X
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Custom gaming PC

## AI Capability Summary
Baseline — 8 GB VRAM sufficient for 7B Q4; larger models require significant offload.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-049_nebula-pc-titan-ryzen-7-7800x3d-rtx-5070.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-8GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: nebula-pc-titan-ryzen-7-7800x3d-rtx-5070
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Nebula PC Titan Ryzen 7 7800X3D RTX 5070
gpu: RTX 5070
vram: 12 GB
unified_memory: UNKNOWN
price_aud: $2238 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Nebula PC Titan Ryzen 7 7800X3D RTX 5070

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2238 AUD
- **Retailer:** Nebula PC via OzBargain
- **URL:** [https://www.ozbargain.com.au/node/900497](https://www.ozbargain.com.au/node/900497)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5070
- **VRAM:** 12 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 7 7800X3D
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Gaming PC via OzBargain

## AI Capability Summary
Baseline — 8 GB VRAM sufficient for 7B Q4; larger models require significant offload.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-050_ple-sidekick-rtx-4070-super-ex-demo.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-8GB #ConditionUnknown #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Desktop (uncategorised) -->
---
id: ple-sidekick-rtx-4070-super-ex-demo
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: PLE Sidekick RTX 4070 Super EX-DEMO
gpu: RTX 4070 Super
vram: 12 GB
unified_memory: UNKNOWN
price_aud: $3079 AUD
condition: UNKNOWN
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# PLE Sidekick RTX 4070 Super EX-DEMO

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3079 AUD
- **Retailer:** PLE Computers
- **URL:** [https://www.ple.com.au/products/684114/ex-demo-ple-sidekick-rtx-4070-super-prebuilt-ready-to-go-gaming-pc-co-demo](https://www.ple.com.au/products/684114/ex-demo-ple-sidekick-rtx-4070-super-prebuilt-ready-to-go-gaming-pc-co-demo)
- **Condition:** UNKNOWN
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4070 Super
- **VRAM:** 12 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core i5-14400
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Low stock

## AI Capability Summary
Baseline — 8 GB VRAM sufficient for 7B Q4; larger models require significant offload.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-054_constellar-onyx-pc-rtx-4080-super.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #ConditionUnknown #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Desktop (uncategorised) -->
---
id: constellar-onyx-pc-rtx-4080-super
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: CONSTELLAR ONYX PC — RTX 4080 SUPER
gpu: RTX 4080 Super
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $4099 AUD
condition: UNKNOWN
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# CONSTELLAR ONYX PC — RTX 4080 SUPER

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $4099 AUD
- **Retailer:** Mike PC AU
- **URL:** UNKNOWN
- **Condition:** UNKNOWN
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4080 Super
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Watchlist candidate

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-055_scorptec-32-core-compute-platform.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: scorptec-32-core-compute-platform
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Scorptec 32-Core Compute Platform
gpu: RTX PRO 4000
vram: 16 GB
unified_memory: UNKNOWN
price_aud: UNKNOWN
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Scorptec 32-Core Compute Platform

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** UNKNOWN
- **Retailer:** Scorptec
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX PRO 4000
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Threadripper 9970X
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Professional workstation

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-056_scorptec-blackwell-pro-workstation.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-48GB+ #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: scorptec-blackwell-pro-workstation
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Scorptec Blackwell PRO Workstation
gpu: RTX PRO 5000 Blackwell
vram: 48 GB
unified_memory: UNKNOWN
price_aud: UNKNOWN
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Scorptec Blackwell PRO Workstation

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** UNKNOWN
- **Retailer:** Scorptec
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX PRO 5000 Blackwell
- **VRAM:** 48 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Professional workstation supported by ECC memory

## AI Capability Summary
Exceptional — 48 GB+ VRAM supports 70B+ models fully in VRAM at Q4.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-059_hp-z8-fury-g5-workstation.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-48GB+ #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: hp-z8-fury-g5-workstation
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: HP Z8 FURY G5 Workstation
gpu: RTX 6000 Ada
vram: 48 GB
unified_memory: UNKNOWN
price_aud: $44205.95 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Out of Stock
score: UNKNOWN — pending manual review
---

# HP Z8 FURY G5 Workstation

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Out of Stock
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $44205.95 AUD
- **Retailer:** Mwave
- **URL:** [https://www.mwave.com.au/product/hp-z8-fury-g5-workstation-xeon-w93475x-128gb-6tb-rtx-6000-ada-w11p-ac81318](https://www.mwave.com.au/product/hp-z8-fury-g5-workstation-xeon-w93475x-128gb-6tb-rtx-6000-ada-w11p-ac81318)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 6000 Ada
- **VRAM:** 48 GB
- **Unified Memory:** UNKNOWN
- **CPU:** XEON W9-3475X
- **RAM:** 128 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
High end fury workstation

## AI Capability Summary
Exceptional — 48 GB+ VRAM supports 70B+ models fully in VRAM at Q4.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-062_allied-moab-a-rtx-5090-32gb-gaming-pc.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: allied-moab-a-rtx-5090-32gb-gaming-pc
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Allied M.O.A.B-A: RTX 5090 32GB Gaming PC
gpu: RTX 5090
vram: 32 GB
unified_memory: UNKNOWN
price_aud: UNKNOWN
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Allied M.O.A.B-A: RTX 5090 32GB Gaming PC

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** UNKNOWN
- **Retailer:** Allied Gaming
- **URL:** [https://www.alliedgamingpc.com.au/allied-moab-a-ready-to-ship-gaming-pc-ryzen-7-9800X3D-rtx-5090-32gb/](https://www.alliedgamingpc.com.au/allied-moab-a-ready-to-ship-gaming-pc-ryzen-7-9800X3D-rtx-5090-32gb/)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090
- **VRAM:** 32 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 7 9800X3D
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Prebuilt

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-063_scorptec-vengeance-rtx-5090-gaming-pc.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: scorptec-vengeance-rtx-5090-gaming-pc
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: Scorptec Vengeance RTX 5090 Gaming PC
gpu: RTX 5090
vram: 32 GB
unified_memory: UNKNOWN
price_aud: UNKNOWN
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Scorptec Vengeance RTX 5090 Gaming PC

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** UNKNOWN
- **Retailer:** Scorptec
- **URL:** [https://www.scorptec.com.au/product/ready-to-run-pcs/gaming-pc/121620-r2r10544](https://www.scorptec.com.au/product/ready-to-run-pcs/gaming-pc/121620-r2r10544)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090
- **VRAM:** 32 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Prebuilt

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/03_New_Desktop_Systems/intake-064_aether-lvl-10-ice-max-rtx-5090-desktop-pc.md
`````markdown
<!-- TAGS: #Desktop #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=New desktop -->
---
id: aether-lvl-10-ice-max-rtx-5090-desktop-pc
category: desktop
track: UNKNOWN
pathway: UNKNOWN
name: AETHER : LVL 10 ICE MAX RTX 5090 Desktop PC
gpu: RTX 5090
vram: 32 GB
unified_memory: UNKNOWN
price_aud: UNKNOWN
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# AETHER : LVL 10 ICE MAX RTX 5090 Desktop PC

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** UNKNOWN
- **Retailer:** Aftershock PC
- **URL:** [https://aftershockpc.com.au/products/aether-lvl-10-ice-max-r9-9950x3d-rtx-5090-1](https://aftershockpc.com.au/products/aether-lvl-10-ice-max-r9-9950x3d-rtx-5090-1)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090
- **VRAM:** 32 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 9 9950X3D
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Prebuilt

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/21_lenovo-legion-pro-7i-rtx-4090.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #New #SingleGPU #AgenticAI #Coding #NonUpgradeable #NeedsReview -->
---
id: lenovo-legion-pro-7i-rtx-4090
category: laptop
name: Lenovo Legion Pro 7i
gpu: NVIDIA RTX 4090 Laptop GPU (16 GB)
vram: 16 GB
score: 84
---

# Lenovo Legion Pro 7i — RTX 4090 Laptop GPU 16 GB

## Overview
- **VRAM Tier:** Priority 3 — 16 GB RTX 4090 Laptop GPU
- **Adjusted Score:** 84 / 110
- **Price (AUD):** ~$3,599–$4,399 depending on configuration
- **Vendor:** Mike PC / Lenovo AU / Amazon AU

## Key Specs
- **GPU:** NVIDIA RTX 4090 Laptop GPU, 16 GB GDDR6 (TGP varies by config; verify)
- **CPU:** Intel Core i9-14900HX
- **RAM:** 32 GB DDR5 (upgradeable to 64 GB via SODIMM slots)
- **Storage:** 2 TB SSD
- **Display:** 16-inch 2K 240 Hz
- **Form factor:** 16-inch performance laptop

## AI Capability Summary
Best emotional compromise one-device setup. Powerful Windows laptop for CUDA workflows, SDXL, FLUX, and 7B–14B local LLMs. RAM upgradeable to 64 GB which helps with CPU offloading for larger models. Cannot run 30B/34B Q4 in VRAM alone (16 GB ceiling).

## Rubric Breakdown
- **VRAM & GPU Generation:** 22/35
- **Ecosystem & Software:** 25/25
- **Value for Money:** 18/25
- **Design & Expandability:** 11/15
- **Purchase Safety & Risk:** 8/10
- **Raw Score:** 84 / 110
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/22_asus-rog-strix-scar-17-rtx-4090.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #New #SingleGPU #AgenticAI #Coding #NonUpgradeable #NeedsReview -->
---
id: asus-rog-strix-scar-17-rtx-4090
category: laptop
name: Asus ROG Strix Scar 17 G733PY-LL021W
gpu: NVIDIA RTX 4090 Laptop GPU (16 GB)
vram: 16 GB
score: 87
---

# Asus ROG Strix Scar 17 G733PY-LL021W — RTX 4090 Laptop GPU 16 GB

## Overview
- **VRAM Tier:** Priority 3 — 16 GB RTX 4090 Laptop GPU
- **Adjusted Score:** 87 / 110
- **Price (AUD):** ~$5,099
- **Vendor:** Umart / Australian IT retailers

## Key Specs
- **GPU:** NVIDIA RTX 4090 Laptop GPU, 16 GB GDDR6
- **CPU:** AMD Ryzen 9 7945HX
- **RAM:** 32 GB DDR5, upgradeable to 64 GB
- **Storage:** 1 TB NVMe SSD
- **Display:** 17.3-inch WQHD 240 Hz
- **Form factor:** 17-inch desktop replacement laptop

## AI Capability Summary
Best NVIDIA laptop candidate in the scored set. Strong sustained thermal performance for extended local inference runs. RAM upgrade to 64 GB is practical and affordable.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/23_asus-rog-strix-scar-18-rtx-4090.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #New #SingleGPU #AgenticAI #Coding #NonUpgradeable #NeedsReview -->
---
id: asus-rog-strix-scar-18-rtx-4090
category: laptop
name: Asus ROG Strix Scar 18 G834JYR-R6037W
gpu: NVIDIA RTX 4090 Laptop GPU (16 GB)
vram: 16 GB
score: 84
---

# Asus ROG Strix Scar 18 G834JYR-R6037W — RTX 4090 Laptop GPU 16 GB

## Overview
- **VRAM Tier:** Priority 3 — 16 GB RTX 4090 Laptop GPU
- **Adjusted Score:** 84 / 110
- **Price (AUD):** ~$6,899
- **Vendor:** MSY / Umart-linked AU retail

## Key Specs
- **GPU:** NVIDIA RTX 4090 Laptop GPU, 16 GB GDDR6
- **CPU:** Intel Core i9-14900HX
- **RAM:** 64 GB DDR5 (out of box)
- **Storage:** 2 TB total NVMe (2x 1 TB)
- **Display:** 18-inch QHD
- **Form factor:** 18-inch desktop replacement laptop (~3.1 kg)

## AI Capability Summary
Strong 18-inch desktop-replacement laptop. Better out-of-box RAM than Scar 17, but the price premium is high for the same 16 GB VRAM ceiling.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/24_msi-stealth-16-ai-studio-rtx-4090.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #New #SingleGPU #AgenticAI #Coding #Travel #NonUpgradeable #NeedsReview -->
---
id: msi-stealth-16-ai-studio-rtx-4090
category: laptop
name: MSI Stealth 16 AI Studio A1VIG
gpu: NVIDIA RTX 4090 Laptop GPU (16 GB)
vram: 16 GB
score: 82
---

# MSI Stealth 16 AI Studio A1VIG — RTX 4090 Laptop GPU 16 GB

## Overview
- **VRAM Tier:** Priority 3 — 16 GB RTX 4090 Laptop GPU
- **Adjusted Score:** 82 / 110
- **Price (AUD):** ~$6,599
- **Vendor:** Umart

## Key Specs
- **GPU:** NVIDIA RTX 4090 Laptop GPU, 16 GB GDDR6
- **CPU:** Intel Core Ultra 9 185H
- **RAM:** 32 GB DDR5 (soldered; verify upgrade path)
- **Storage:** 2 TB SSD
- **Display:** 16-inch creator-class
- **Form factor:** Thin 16-inch creator laptop

## AI Capability Summary
RTX 4090 16 GB in a thinner chassis. Capable but the thin design creates thermal risk under sustained local inference. Not recommended over the Scar 17/18 for AI-first use.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/30_asus-rog-strix-scar-18-rtx-5090-2025.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-24GB #New #SingleGPU #AgenticAI #Coding #Track1-Target #NeedsManualData -->
---
id: asus-rog-strix-scar-18-rtx-5090-2025
category: laptop
name: ASUS ROG Strix Scar 18 (2025) RTX 5090
gpu: NVIDIA RTX 5090 Laptop GPU (24 GB)
vram: 24 GB
score: UNKNOWN — pending manual AU retailer data
---

# ASUS ROG Strix Scar 18 (2025) — RTX 5090 Laptop GPU 24 GB

> ⚠️ **BLANK SHELL — all fields require manual data entry from AU retailer research.**
> Agent must not infer or guess missing values. UNKNOWN fields stay UNKNOWN until manually updated.

## Track 1 Status
- **Chassis family:** ASUS ROG Strix Scar 18 ✅ (locked chassis)
- **Target GPU:** RTX 5090 Laptop GPU 24 GB ✅ (preferred tier)
- **GOOD ENOUGH check:** PENDING — requires AU stock confirmation + specs below

## Overview
- **VRAM Tier:** Priority 1 — 24 GB RTX 5090 Laptop GPU (preferred)
- **Price (AUD):** UNKNOWN — requires AU retailer check
- **Vendor (AU):** UNKNOWN — requires AU retailer check (check: JB Hi-Fi, Centre Com, Scorptec, Affordable Laptops, ASUS AU store)
- **In stock in AU:** UNKNOWN

## Key Specs
- **GPU:** NVIDIA RTX 5090 Laptop GPU, 24 GB GDDR7 (confirm; may vary by config)
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN installed / UNKNOWN max supported
- **Free RAM slots:** UNKNOWN
- **Storage:** UNKNOWN installed
- **Free M.2 slots:** UNKNOWN
- **Display:** 18-inch — panel type UNKNOWN (IPS / OLED / MiniLED?)
- **Weight:** UNKNOWN kg
- **Charger / PSU wattage:** UNKNOWN W
- **Warranty (AU):** UNKNOWN — term and type (onsite / carry-in?)

## Thermal Notes
- **Sustained TGP:** UNKNOWN W
- **Thermal reputation:** UNKNOWN — check major reviews (Notebookcheck, LaptorMedia, Hardware Unboxed)
- **Review signals:** UNKNOWN

## AI Capability Summary
UNKNOWN — to be completed after specs are filled in. Expected: capable of running 30B+ Q4 models locally in VRAM with 24 GB ceiling.

## Rubric Scores (laptop profile — all UNKNOWN until data collected)
- VRAM_Adequacy: UNKNOWN (expected 8 if 24 GB confirmed)
- GPU_Compute_Tier: UNKNOWN
- Sustained_TGP_Rating: UNKNOWN
- Thermal_Reputation: UNKNOWN
- RAM_Ceiling: UNKNOWN
- Storage_Expandability: UNKNOWN
- AU_Retailer_Confidence: UNKNOWN ← **critical gate for GOOD ENOUGH condition**
- Price_AUD_Competitiveness: UNKNOWN
- Display_Usability: UNKNOWN
- Portability_Penalty: UNKNOWN

## Verification Required Before Scoring
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [ ] Confirm GPU: RTX 5090 Laptop GPU 24 GB GDDR7
- [ ] RAM installed amount and max supported
- [ ] Number of free M.2 slots
- [ ] Charger wattage
- [ ] Weight
- [ ] Warranty term and type
- [ ] Sustained TGP from review or spec sheet
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/31_lenovo-legion-9i-18-rtx-5090.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-24GB #New #SingleGPU #AgenticAI #Coding #Track1-Target #NeedsManualData -->
---
id: lenovo-legion-9i-18-rtx-5090
category: laptop
name: Lenovo Legion 9i Gen 10 18" RTX 5090
gpu: NVIDIA RTX 5090 Laptop GPU (24 GB)
vram: 24 GB
score: UNKNOWN — pending manual AU retailer data
---

# Lenovo Legion 9i Gen 10 18" — RTX 5090 Laptop GPU 24 GB

> ⚠️ **BLANK SHELL — all fields require manual data entry from AU retailer research.**
> Agent must not infer or guess missing values. UNKNOWN fields stay UNKNOWN until manually updated.

## Track 1 Status
- **Chassis family:** Lenovo Legion 9i 18 ✅ (locked chassis)
- **Target GPU:** RTX 5090 Laptop GPU 24 GB ✅ (preferred tier)
- **GOOD ENOUGH check:** PENDING — requires AU stock confirmation + specs below

## Overview
- **VRAM Tier:** Priority 1 — 24 GB RTX 5090 Laptop GPU (preferred)
- **Price (AUD):** UNKNOWN — requires AU retailer check
- **Vendor (AU):** UNKNOWN — requires AU retailer check (check: Lenovo AU store, JB Hi-Fi, Centre Com, Scorptec)
- **In stock in AU:** UNKNOWN

## Key Specs
- **GPU:** NVIDIA RTX 5090 Laptop GPU, 24 GB GDDR7 (confirm; may vary by config)
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN installed / UNKNOWN max supported
- **Free RAM slots:** UNKNOWN
- **Storage:** UNKNOWN installed
- **Free M.2 slots:** UNKNOWN
- **Display:** 18-inch — panel type UNKNOWN (IPS / OLED / MiniLED?)
- **Weight:** UNKNOWN kg
- **Charger / PSU wattage:** UNKNOWN W
- **Warranty (AU):** UNKNOWN — term and type (onsite / carry-in?)

## Thermal Notes
- **Sustained TGP:** UNKNOWN W
- **Thermal reputation:** UNKNOWN — check major reviews (Notebookcheck, LaptorMedia, Hardware Unboxed)
- **Review signals:** UNKNOWN

## AI Capability Summary
UNKNOWN — to be completed after specs are filled in. Expected: capable of running 30B+ Q4 models locally in VRAM with 24 GB ceiling.

## Rubric Scores (laptop profile — all UNKNOWN until data collected)
- VRAM_Adequacy: UNKNOWN (expected 8 if 24 GB confirmed)
- GPU_Compute_Tier: UNKNOWN
- Sustained_TGP_Rating: UNKNOWN
- Thermal_Reputation: UNKNOWN
- RAM_Ceiling: UNKNOWN
- Storage_Expandability: UNKNOWN
- AU_Retailer_Confidence: UNKNOWN ← **critical gate for GOOD ENOUGH condition**
- Price_AUD_Competitiveness: UNKNOWN
- Display_Usability: UNKNOWN
- Portability_Penalty: UNKNOWN

## Verification Required Before Scoring
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [ ] Confirm GPU: RTX 5090 Laptop GPU 24 GB GDDR7
- [ ] RAM installed amount and max supported
- [ ] Number of free M.2 slots
- [ ] Charger wattage
- [ ] Weight
- [ ] Warranty term and type
- [ ] Sustained TGP from review or spec sheet
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/32_msi-raider-a18-hx-rtx-5090.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-24GB #New #SingleGPU #AgenticAI #Coding #Track1-Target #NeedsManualData -->
---
id: msi-raider-a18-hx-rtx-5090
category: laptop
name: MSI Raider A18 HX RTX 5090
gpu: NVIDIA RTX 5090 Laptop GPU (24 GB)
vram: 24 GB
score: UNKNOWN — pending manual AU retailer data
---

# MSI Raider A18 HX — RTX 5090 Laptop GPU 24 GB

> ⚠️ **BLANK SHELL — all fields require manual data entry from AU retailer research.**
> Agent must not infer or guess missing values. UNKNOWN fields stay UNKNOWN until manually updated.

## Track 1 Status
- **Chassis family:** MSI Raider A18 HX ✅ (locked chassis)
- **Target GPU:** RTX 5090 Laptop GPU 24 GB ✅ (preferred tier)
- **GOOD ENOUGH check:** PENDING — requires AU stock confirmation + specs below

## Overview
- **VRAM Tier:** Priority 1 — 24 GB RTX 5090 Laptop GPU (preferred)
- **Price (AUD):** UNKNOWN — requires AU retailer check
- **Vendor (AU):** UNKNOWN — requires AU retailer check (check: JB Hi-Fi, Centre Com, Scorptec, MSI AU store, PLE)
- **In stock in AU:** UNKNOWN

## Key Specs
- **GPU:** NVIDIA RTX 5090 Laptop GPU, 24 GB GDDR7 (confirm; may vary by config)
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN installed / UNKNOWN max supported
- **Free RAM slots:** UNKNOWN
- **Storage:** UNKNOWN installed
- **Free M.2 slots:** UNKNOWN
- **Display:** 18-inch — panel type UNKNOWN (IPS / OLED / MiniLED?)
- **Weight:** UNKNOWN kg
- **Charger / PSU wattage:** UNKNOWN W
- **Warranty (AU):** UNKNOWN — term and type (onsite / carry-in?)

## Thermal Notes
- **Sustained TGP:** UNKNOWN W
- **Thermal reputation:** UNKNOWN — check major reviews (Notebookcheck, LaptorMedia, Hardware Unboxed)
- **Review signals:** UNKNOWN

## AI Capability Summary
UNKNOWN — to be completed after specs are filled in. Expected: capable of running 30B+ Q4 models locally in VRAM with 24 GB ceiling.

## Rubric Scores (laptop profile — all UNKNOWN until data collected)
- VRAM_Adequacy: UNKNOWN (expected 8 if 24 GB confirmed)
- GPU_Compute_Tier: UNKNOWN
- Sustained_TGP_Rating: UNKNOWN
- Thermal_Reputation: UNKNOWN
- RAM_Ceiling: UNKNOWN
- Storage_Expandability: UNKNOWN
- AU_Retailer_Confidence: UNKNOWN ← **critical gate for GOOD ENOUGH condition**
- Price_AUD_Competitiveness: UNKNOWN
- Display_Usability: UNKNOWN
- Portability_Penalty: UNKNOWN

## Verification Required Before Scoring
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [ ] Confirm GPU: RTX 5090 Laptop GPU 24 GB GDDR7
- [ ] RAM installed amount and max supported
- [ ] Number of free M.2 slots
- [ ] Charger wattage
- [ ] Weight
- [ ] Warranty term and type
- [ ] Sustained TGP from review or spec sheet
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/33_msi-titan-rtx-5090.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-24GB #New #SingleGPU #AgenticAI #Coding #Track1-Target #NeedsManualData -->
---
id: msi-titan-rtx-5090
category: laptop
name: MSI Titan (RTX 5090) — model variant UNKNOWN
gpu: NVIDIA RTX 5090 Laptop GPU (24 GB)
vram: 24 GB
score: UNKNOWN — pending manual AU retailer data
---

# MSI Titan — RTX 5090 Laptop GPU 24 GB

> ⚠️ **BLANK SHELL — all real-world spec fields are UNKNOWN.**
> Agent must not infer or guess missing values. UNKNOWN fields stay UNKNOWN until manually updated by the user.
> Specific model variant (e.g. Titan GT77, Titan 18 HX) to be confirmed from AU retailer listing.

## Track 1 Status
- **Chassis family:** MSI Titan 17/18 ✅ (in scope per AGENTS.md)
- **Target GPU:** RTX 5090 Laptop GPU 24 GB ✅ (preferred tier)
- **Budget band:** UNKNOWN — needs AU price confirmation. Cap: 4,000 AUD. Sweet spot: 2,500–3,500 AUD.
- **GOOD ENOUGH check:** PENDING — requires AU stock confirmation + all specs below

## Overview
- **Model variant:** UNKNOWN — confirm exact model name (e.g. MSI Titan GT77, Titan 18 HX, etc.)
- **VRAM Tier:** Priority 1 — 24 GB RTX 5090 Laptop GPU (preferred)
- **Price (AUD):** UNKNOWN — requires AU retailer check
- **Vendor (AU):** UNKNOWN — check: JB Hi-Fi, Centre Com, Scorptec, PLE, MSI AU store
- **In stock in AU:** UNKNOWN

## Key Specs
- **GPU:** NVIDIA RTX 5090 Laptop GPU, 24 GB GDDR7 — confirm VRAM and GPU variant
- **CPU:** UNKNOWN
- **RAM installed:** UNKNOWN GB
- **RAM max supported:** UNKNOWN GB
- **Free RAM slots:** UNKNOWN
- **Storage installed:** UNKNOWN TB
- **Free M.2 slots:** UNKNOWN
- **Screen size:** UNKNOWN inches (expect 17" or 18")
- **Panel type:** UNKNOWN (IPS / OLED / MiniLED?)
- **Weight:** UNKNOWN kg
- **Charger / PSU wattage:** UNKNOWN W
- **Warranty (AU):** UNKNOWN — term and type (onsite / carry-in / depot?)

## Thermal Notes
- **Sustained TGP:** UNKNOWN W
- **Thermal reputation:** UNKNOWN — check Notebookcheck, LaptorMedia, Hardware Unboxed
- **Review signals:** UNKNOWN

## AI Capability Summary
UNKNOWN — to be completed after specs are filled in.

## Rubric Scores (laptop profile — all UNKNOWN until data collected)
- VRAM_Adequacy: UNKNOWN
- GPU_Compute_Tier: UNKNOWN
- Sustained_TGP_Rating: UNKNOWN
- Thermal_Reputation: UNKNOWN
- RAM_Ceiling: UNKNOWN
- Storage_Expandability: UNKNOWN
- AU_Retailer_Confidence: UNKNOWN ← **critical gate for GOOD ENOUGH condition**
- Price_AUD_Competitiveness: UNKNOWN
- Display_Usability: UNKNOWN
- Portability_Penalty: UNKNOWN

## Verification Required Before Scoring
- [ ] Confirm exact model name and screen size
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD (within 4,000 AUD cap?)
- [ ] Confirm GPU: RTX 5090 Laptop GPU 24 GB GDDR7
- [ ] CPU model
- [ ] RAM installed amount and max supported
- [ ] Number of free M.2 slots
- [ ] Charger wattage
- [ ] Weight
- [ ] Warranty term and type
- [ ] Sustained TGP from review or spec sheet
- [ ] Thermal flag from review (throttles / runs hot / acceptable?)
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/34_asus-tuf-gaming-a16-strix-halo.md
`````markdown
<!-- TAGS: #Laptop #AMD #StrixHalo #UnifiedMemory #Track1-1B #New #NeedsManualData #VRAM-Unified -->
---
id: asus-tuf-gaming-a16-strix-halo
category: laptop
path: 1B
name: ASUS TUF Gaming A16 — AMD Strix Halo (Ryzen AI Max)
gpu: AMD Radeon 890M / integrated Strix Halo GPU (unified)
vram: UNKNOWN (unified — 32–64 GB from shared system RAM, config dependent)
score: UNKNOWN — pending manual AU retailer data
---

# ASUS TUF Gaming A16 — AMD Strix Halo (Ryzen AI Max)

> ⚠️ **BLANK SHELL — all fields require manual data entry from AU retailer research.**
> Agent must not infer or guess missing values. UNKNOWN fields stay UNKNOWN until manually updated.

## Track 1 Status
- **Path:** 1B — AMD Strix Halo Unified Memory
- **Chassis family:** ASUS TUF Gaming A16 ✅ (in scope — all brands on 1B)
- **SoC requirement:** Must confirm Strix Halo (Ryzen AI Max or Ryzen AI Max+) — NOT standard Ryzen
- **GOOD ENOUGH check:** PENDING — requires AU stock + unified memory ≥ 32 GB confirmed

## Overview
- **Unified Memory Tier:** UNKNOWN — confirm 32 GB / 64 GB / 96 GB config at time of purchase
- **Price (AUD):** UNKNOWN — requires AU retailer check
- **Vendor (AU):** UNKNOWN — check: Scorptec, Centre Com, JB Hi-Fi, ASUS AU Store
- **In stock in AU:** UNKNOWN

## Key Specs
- **SoC:** UNKNOWN — confirm Ryzen AI Max or Ryzen AI Max+ (Strix Halo architecture required)
- **Unified Memory:** UNKNOWN GB LPDDR5X (shared CPU + GPU — confirm config; min 32 GB for Track 1 eligibility)
- **GPU portion (estimated):** UNKNOWN — typically 60–75% of unified memory available to GPU
- **CPU cores:** UNKNOWN
- **Storage:** UNKNOWN installed
- **Free M.2 slots:** UNKNOWN
- **Display:** 16" — panel type UNKNOWN (IPS / OLED / MiniLED?)
- **Weight:** UNKNOWN kg
- **Charger / PSU wattage:** UNKNOWN W
- **Warranty (AU):** UNKNOWN — term and type (onsite / carry-in?)

## Screen Size Note
- **16" screen:** No scoring bonus (17–18" bonus not triggered). No penalty unless < 15". Evaluate on value + SoC.

## Thermal Notes
- **Sustained TDP (SoC):** UNKNOWN W
- **Thermal reputation:** UNKNOWN — check reviews (Notebookcheck, Hardware Unboxed)
- **Fan noise under sustained load:** UNKNOWN

## ROCm / Software Compatibility
- **ROCm version support:** UNKNOWN — flag any known gaps for LLM inference (llama.cpp, Ollama, etc.)
- **HIP SDK:** UNKNOWN

## AI Capability Summary
UNKNOWN — to be completed after specs are filled in. Expected: with ≥ 64 GB unified memory, capable of running 34B–70B Q4 models fully in-memory. At 32 GB, expect 13B–20B Q4 range before offloading required.

## Rubric Scores (Path 1B profile — all UNKNOWN until data collected)
- UnifiedMemory_Adequacy: UNKNOWN
- SoC_Compute_Tier: UNKNOWN
- Sustained_TDP_Rating: UNKNOWN
- Thermal_Reputation: UNKNOWN
- Storage_Expandability: UNKNOWN
- AU_Retailer_Confidence: UNKNOWN ← **critical gate for GOOD ENOUGH condition**
- Price_AUD_Competitiveness: UNKNOWN
- Display_Usability: UNKNOWN
- ROCm_Compatibility_Flag: UNKNOWN ← **disqualifying flag if severe gap confirmed**
- Screen_Size_Bonus: 0 (16" — no bonus; bonus triggers at 17–18")

## Track 2 Urgency Note
- **16" screen:** Moderate Track 2 urgency. A 13" Strix Halo would raise this to HIGH.

## Verification Required Before Scoring
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [ ] Confirm SoC: Ryzen AI Max or Ryzen AI Max+ (Strix Halo — NOT standard Ryzen)
- [ ] Confirm unified memory size in this specific SKU (32 / 64 / 96 GB?)
- [ ] Confirm CPU core count and clock
- [ ] Storage installed and free M.2 slot count
- [ ] Charger wattage
- [ ] Weight
- [ ] Warranty term and type (AU)
- [ ] Sustained TDP from review or spec sheet
- [ ] ROCm / llama.cpp compatibility confirmed or flagged
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/35_asus-rog-zephyrus-g16-strix-halo.md
`````markdown
<!-- TAGS: #Laptop #AMD #StrixHalo #UnifiedMemory #Track1-1B #New #NeedsManualData #VRAM-Unified #SmallScreen #Track2-Urgency-High -->
---
id: asus-rog-zephyrus-g16-strix-halo
category: laptop
path: 1B
name: ASUS ROG Zephyrus G16 — AMD Strix Halo (Ryzen AI Max)
gpu: AMD Radeon integrated Strix Halo GPU (unified)
vram: UNKNOWN (unified — 32–96 GB from shared system RAM, config dependent)
score: UNKNOWN — pending manual AU retailer data
---

# ASUS ROG Zephyrus G16 — AMD Strix Halo (Ryzen AI Max)

> ⚠️ **BLANK SHELL — all fields require manual data entry from AU retailer research.**
> Agent must not infer or guess missing values. UNKNOWN fields stay UNKNOWN until manually updated.

## Track 1 Status
- **Path:** 1B — AMD Strix Halo Unified Memory
- **Chassis family:** ASUS ROG Zephyrus G16 ✅ (in scope — all brands on 1B)
- **SoC requirement:** Must confirm Strix Halo (Ryzen AI Max or Ryzen AI Max+) — NOT standard Ryzen
- **GOOD ENOUGH check:** PENDING — requires AU stock + unified memory ≥ 32 GB confirmed

## Overview
- **Unified Memory Tier:** UNKNOWN — confirm 32 GB / 64 GB / 96 GB config at time of purchase
- **Price (AUD):** UNKNOWN — requires AU retailer check
- **Vendor (AU):** UNKNOWN — check: Scorptec, Centre Com, JB Hi-Fi, ASUS AU Store
- **In stock in AU:** UNKNOWN

## Key Specs
- **SoC:** UNKNOWN — confirm Ryzen AI Max or Ryzen AI Max+ (Strix Halo architecture required)
- **Unified Memory:** UNKNOWN GB LPDDR5X (shared CPU + GPU — confirm config; min 32 GB for Track 1 eligibility)
- **GPU portion (estimated):** UNKNOWN — typically 60–75% of unified memory available to GPU
- **CPU cores:** UNKNOWN
- **Storage:** UNKNOWN installed
- **Free M.2 slots:** UNKNOWN
- **Display:** 16" — panel type UNKNOWN (OLED / MiniLED?)
- **Weight:** UNKNOWN kg
- **Charger / PSU wattage:** UNKNOWN W
- **Warranty (AU):** UNKNOWN — term and type

## Screen Size Note
- **16" screen:** No scoring bonus (17–18" bonus not triggered). No penalty unless < 15". Evaluate on value + SoC + build quality.

## Thermal Notes
- **Sustained TDP (SoC):** UNKNOWN W
- **Thermal reputation:** UNKNOWN — Zephyrus line historically has better thermals than TUF; confirm under sustained load
- **Fan noise under sustained load:** UNKNOWN

## ROCm / Software Compatibility
- **ROCm version support:** UNKNOWN — flag any known gaps for LLM inference
- **HIP SDK:** UNKNOWN

## AI Capability Summary
UNKNOWN — to be completed after specs are filled in. Zephyrus chassis typically carries better build quality and thermals than TUF, making it a stronger Track 1 candidate at equivalent specs. Expected: with ≥ 64 GB unified memory, capable of 34B–70B Q4 range.

## Rubric Scores (Path 1B profile — all UNKNOWN until data collected)
- UnifiedMemory_Adequacy: UNKNOWN
- SoC_Compute_Tier: UNKNOWN
- Sustained_TDP_Rating: UNKNOWN
- Thermal_Reputation: UNKNOWN
- Storage_Expandability: UNKNOWN
- AU_Retailer_Confidence: UNKNOWN ← **critical gate for GOOD ENOUGH condition**
- Price_AUD_Competitiveness: UNKNOWN
- Display_Usability: UNKNOWN
- ROCm_Compatibility_Flag: UNKNOWN ← **disqualifying flag if severe gap confirmed**
- Screen_Size_Bonus: 0 (16" — no bonus; bonus triggers at 17–18")

## Track 2 Urgency Note
- **16" screen:** Moderate Track 2 urgency. If 16" confirmed at high price, consider whether Track 2 Pathway C mini PC closes the gap more cost-effectively.

## Verification Required Before Scoring
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [ ] Confirm SoC: Ryzen AI Max or Ryzen AI Max+ (Strix Halo — NOT standard Ryzen)
- [ ] Confirm unified memory size in this specific SKU (32 / 64 / 96 GB?)
- [ ] Confirm CPU core count and clock
- [ ] Storage installed and free M.2 slot count
- [ ] Charger wattage
- [ ] Weight
- [ ] Warranty term and type (AU)
- [ ] Sustained TDP from review or spec sheet
- [ ] ROCm / llama.cpp compatibility confirmed or flagged
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/36_lenovo-legion-9i-18-rtx-5080-ebay.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #New #SingleGPU #AgenticAI #Coding #Track1-Candidate #ExceedsBudget -->
---
id: lenovo-legion-9i-18-rtx-5080-ebay
category: laptop
name: Lenovo Legion 9i Gen 10 18" RTX 5080 (eBay)
gpu: NVIDIA RTX 5080 Laptop GPU (16 GB)
vram: 16 GB
price_aud: 4635
score: 7.5 (Marginally Over Budget)
---

# Lenovo Legion 9i Gen 10 18" — RTX 5080 Laptop GPU 16 GB

> ⚠️ **BUDGET ALERT:** This candidate is priced at **$4,635 AUD**, which is **$135 over** the updated $4,500 ceiling.

## Track 1 Status
- **Chassis family:** Lenovo Legion 9i 18 ✅ (locked chassis)
- **Target GPU:** RTX 5080 Laptop GPU 16 GB ✅ (meets Path 1A floor)
- **GOOD ENOUGH check:** ⚠️ **BORDERLINE** — Price ($4,635) is 3% over the $4,500 limit.

## Overview
- **VRAM Tier:** Priority 2 — 16 GB RTX 5080 Laptop GPU
- **Price (AUD):** $4,635 (After discounts)
- **Vendor (AU):** eBay Australia (Item: 168263146829)
- **In stock in AU:** Yes

## Key Specs
- **GPU:** NVIDIA RTX 5080 Laptop GPU, 16 GB GDDR7
- **CPU:** Intel Core Ultra 9 275HX
- **RAM:** 64 GB DDR5 (Confirmed via listing)
- **Storage:** 2 TB PCIe Gen 5 SSD
- **Display:** 18-inch WQUXGA (3840 x 2400), 240Hz
- **Weight:** ~3.1 kg
- **Charger / PSU wattage:** 330W GaN
- **Warranty (AU):** Likely 1-year standard; verify if eBay seller is authorized for Lenovo AU warranty.

## Thermal Notes
- **Sustained TGP:** Up to 175W (Typical for 5080 class in this chassis)
- **Thermal reputation:** Excellent (Internal liquid cooling + Vapor chamber)

## AI Capability Summary
Highly capable for coding and local inference. 16 GB VRAM allows for 14B models (e.g., Mistral-Small, Qwen2.5-Coder) at high precision, or 30B+ models at 4-bit quantization with some offloading/tight fit.

## Rubric Scores (laptop profile)
- VRAM_Adequacy: 6 (16 GB is the floor)
- GPU_Compute_Tier: 9 (RTX 5080 is bleeding edge)
- Sustained_TGP_Rating: 9
- Thermal_Reputation: 9
- RAM_Ceiling: 10 (64 GB pre-installed)
- Storage_Expandability: 8 (2 TB pre-installed, extra slot likely)
- AU_Retailer_Confidence: 7 (eBay retailer; needs warranty verification)
- Price_AUD_Competitiveness: 4 (Exceeds $4,000 limit)
- Display_Usability: 10 (18" 4K 240Hz)
- Portability_Penalty: 3 (Very heavy 18" chassis)

## Verification Required Before Scoring
- [x] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD ($4,635)
- [x] Confirm GPU: RTX 5080 Laptop GPU 16 GB GDDR7
- [x] RAM installed amount (64 GB)
- [ ] Confirm warranty type (Consumer Law vs Manufacturer)
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/37_lenovo-legion-9i-gen10-direct.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #VRAM-24GB #New #SingleGPU #AgenticAI #Coding #Track1-Candidate -->
---
id: lenovo-legion-9i-gen10-direct
category: laptop
name: Lenovo Legion 9i Gen 10 18" (Lenovo Direct)
gpu: NVIDIA RTX 5080 (16 GB) or RTX 5090 (24 GB) Laptop GPU
vram: 16 GB / 24 GB
price_aud: UNKNOWN (Estimate: High, but mitigated by cashback)
score: UNKNOWN — Pending Price
---

# Lenovo Legion 9i Gen 10 18" — Lenovo Direct (EDU/Pro)

> ⚠️ **VERIFIED CONFIGURATION:** Bundle ID `83EYCTO1WWAU3` refers to the **Legion 9i Gen 10 18-inch**, starting with an RTX 5080 (16 GB) or 5090 (24 GB). This is a highly capable machine that meets and exceeds our VRAM requirements.

## Track 1 Status
- **Chassis family:** Lenovo Legion 9i 18 ✅ (locked chassis)
- **Target GPU:** RTX 5080 (16 GB) or RTX 5090 (24 GB) ✅ (meets Path 1A floor)
- **GOOD ENOUGH check:** PENDING — Requires final price verification after discounts.

## Overview
- **VRAM Tier:** Priority 1/2 — 16 GB or 24 GB options available
- **Price (AUD):** UNKNOWN (Needs manual check on EDU/Pro portal)
- **Discount Potential:** Highly compelling due to **16% TopCashback** and/or **Lenovo Student/Pro account discounts**.
- **Vendor (AU):** Lenovo Australia Direct
- **URLs:** 
  - EDU Store (WWAU3): `https://www.lenovo.com/au/edu/education/en/p/laptops/legion-laptops/legion-9-series/legion-9i-gen-10-18-inch-intel/83eycto1wwau3`
  - Pro Store (WWAU3): `https://www.lenovo.com/au/lenovopro/en/configurator/cto/?bundleId=83EYCTO1WWAU3`
  - Standard Store (WWAU4): `https://www.lenovo.com/au/en/p/laptops/legion-laptops/legion-9-series/legion-9i-gen-10-18-inch-intel/83eycto1wwau4`

## Key Specs
- **GPU:** NVIDIA RTX 5080 (16 GB) or RTX 5090 (24 GB)
- **CPU:** Intel Core Ultra 9
- **RAM:** Configurable (Target: 64 GB)
- **Storage:** Configurable (Target: 2 TB)
- **Display:** 18-inch

## AI Capability Summary
Fully capable of handling our local LLM inference requirements, comfortably exceeding the 16 GB floor. Ideal Track 1 target if discounts bring it under the $4,500 ceiling.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/39_msi-raider-a18-hx-refurb.md
`````markdown
<!-- TAGS: #Laptop #MSI #NVIDIA #VRAM-12GB #Refurbished #SingleGPU #Track1-Candidate -->
---
id: msi-raider-a18-hx-refurb
category: laptop
name: MSI Raider A18 HX (Remanufactured)
gpu: NVIDIA RTX 4080 Laptop GPU (12 GB)
price_aud: 3972
score: 7.0 (Meets Criteria)
---

# MSI Raider A18 HX — Remanufactured (PB Tech)

> ℹ️ **SPEC NOTE:** This model features an **RTX 4080 Laptop GPU with 12 GB VRAM**. This meets the newly relaxed Path 1A VRAM floor (8 GB minimum).

## Track 1 Status
- **Chassis family:** MSI Raider 18 ✅
- **Target GPU:** RTX 4080 Laptop GPU 12 GB ✅ (Meets relaxed 8GB floor)
- **GOOD ENOUGH check:** ✅ **PASSED** — Price ($3,972) is within the $4,500 budget and specs meet the relaxed criteria.

## Overview
- **VRAM Tier:** Meets Floor — 12 GB
- **Price (AUD):** $3,971.75
- **Vendor (AU):** PB Tech
- **URL:** `https://www.pbtech.com/au/product/NBKMSI187033R/MSI-Remanufactured-Raider-A18-HX-A7VHG-033NZ-RTX-4`

## Key Specs
- **GPU:** NVIDIA GeForce RTX 4080 Laptop GPU, 12 GB GDDR6
- **CPU:** Intel Core i9 HX series (Verify exact model)
- **RAM:** Configurable
- **Storage:** Configurable
- **Display:** 18-inch
- **Condition:** Remanufactured

## Conclusion
With the VRAM floor relaxed, the 12 GB RTX 4080 in this high-end Raider 18 chassis is a viable candidate. If the remanufactured price is highly competitive, the loss of 4 GB VRAM (compared to a 16 GB model) might be an acceptable trade-off for overall system quality and performance.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/40_msi-katana-17-hx.md
`````markdown
<!-- TAGS: #Laptop #MSI #NVIDIA #VRAM-8GB #New #SingleGPU #Track1-Candidate -->
---
id: msi-katana-17-hx
category: laptop
name: MSI Katana 17 HX
gpu: NVIDIA RTX 5070 Laptop GPU (8 GB)
price_aud: 2798
score: 6.5 (Budget Option, Lower VRAM)
---

# MSI Katana 17 HX — PB Tech

> ℹ️ **SPEC NOTE:** This model features an **RTX 5070 Laptop GPU with 8 GB VRAM**. This meets the newly relaxed Path 1A VRAM floor (8 GB minimum).

## Track 1 Status
- **Chassis family:** MSI Katana 17 (Budget/Mid-range tier)
- **Target GPU:** RTX 5070 Laptop GPU 8 GB ✅ (Meets relaxed 8GB floor)
- **GOOD ENOUGH check:** ✅ **PASSED** — Price ($2,798) is well within the budget and specs meet the relaxed criteria.

## Overview
- **VRAM Tier:** Meets Floor — 8 GB
- **Price (AUD):** $2,797.59
- **Vendor (AU):** PB Tech
- **URL:** `https://www.pbtech.com/au/product/NBKMSI1714094/MSI-Katana-17-HX-B14WGK-094NZ-NVIDIA-RTX-5070-Gami`

## Key Specs
- **GPU:** NVIDIA GeForce RTX 5070 Laptop GPU, 8 GB GDDR7
- **CPU:** Intel Core i7 or i9 HX series
- **RAM:** Configurable
- **Storage:** Configurable
- **Display:** 17-inch

## Conclusion
The RTX 5070 with 8 GB VRAM now meets the relaxed 8GB floor. While the Katana series represents a more budget-friendly tier and 8 GB is restrictive for larger local LLMs, it remains an eligible candidate based on the relaxed rules. A competitive price is required to offset the lower VRAM capacity compared to 12 GB or 16 GB alternatives.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/41_asus-rog-strix-g18-rtx-5070ti-2025.md
`````markdown
<!-- TAGS: #Laptop #ASUS #NVIDIA #VRAM-12GB #Track1-Candidate #OverBudget -->
---
id: asus-rog-strix-g18-rtx-5070ti-2025
category: laptop
name: ASUS ROG Strix G18 (2025)
gpu: NVIDIA RTX 5070 Ti Laptop GPU (12 GB)
vram: 12 GB
price_aud: 4334
score: 8.0 (Under Budget, 18" Bonus)
---

# ASUS ROG Strix G18 (2025) — G815LR-S9099W

> ⚠️ **BUDGET ALERT:** At **$4,956.25**, this unit currently exceeds the $4,500 budget ceiling. However, as an 18-inch model with 12GB VRAM, it is a prime candidate if cashback, sales, or educational pricing can reduce the cost by ~$450.

## Track 1 Status
- **Chassis family:** ASUS ROG Strix G18 ✅ (+Bonus for 18" thermals)
- **Target GPU:** RTX 5070 Ti Laptop GPU 12 GB ✅ (Meets relaxed 8GB floor)
- **GOOD ENOUGH check:** ✅ **PASSED** — Confirmed cheapest AU retail is **$4,334 (MSY/Umart)**. eBay has international sellers from $4,018 (inc. delivery). Best confirmed AU-local buy-it-now is $4,334.

## Overview
- **VRAM Tier:** Meets Floor — 12 GB
- **Price (AUD):** $4,018 inc. delivery (eBay/102_store from KR) | **$4,334 (MSY/Umart AU)** | $4,959 (Device Deal)
- **eBay sellers:** 102_store (99.8%, 30.8K reviews) @ AU$4,018+$42 delivery; tanyastreasuries @ AU$3,905+$160 delivery (US ship)
- **treasure_pc_online:** No current G18 RTX 5070 Ti listing found (100% positive, 15.8K sales — worth monitoring)
- **Cheapest AU-local Vendor:** MSY / Umart @ $4,334
- **StaticIce URL:** `https://www.staticice.com.au/cgi-bin/search.cgi?q=G815LR-S9099W`

## Key Specs
- **SKU:** G815LR-S9099W
- **GPU:** NVIDIA GeForce RTX 5070 Ti, 12 GB
- **CPU:** Intel Core Ultra 9 275HX
- **RAM:** 32 GB
- **Storage:** 1 TB NVMe
- **Display:** 18" WQXGA 240Hz

## Conclusion
A highly compelling Track 1 winner. At $4,334 from MSY or Umart, it is $621 cheaper than the user's previously seen TechBuy price of $4,956. The 18-inch chassis earns the scoring bonus for superior sustained LLM thermal performance.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/42_asus-rog-strix-g16-rtx-5080-2025.md
`````markdown
<!-- TAGS: #Laptop #ASUS #NVIDIA #VRAM-16GB #Track1-Candidate #OverBudget -->
---
id: asus-rog-strix-g16-rtx-5080-2025
category: laptop
name: ASUS ROG Strix G16 (2025)
gpu: NVIDIA RTX 5080 Laptop GPU (16 GB)
vram: 16 GB
price_aud: 4559
score: 7.0 (Marginal Budget — Over by $59)
---

# ASUS ROG Strix G16 (2025) — G615LW-S5165W

> ⚠️ **BUDGET ALERT:** At **$5,699.00**, this unit exceeds the $4,500 budget ceiling by nearly $1,200. It requires an unlikely ~21% discount to become viable.

## Track 1 Status
- **Chassis family:** ASUS ROG Strix G16
- **Target GPU:** RTX 5080 Laptop GPU 16 GB ✅ (Excellent VRAM)
- **GOOD ENOUGH check:** ⚠️ **BORDERLINE** — At **$4,559 (Mwave)**, it exceeds the $4,500 ceiling by only $59. This is far cheaper than the $5,699 user previously saw. Within discount or cashback reach.

## Overview
- **VRAM Tier:** Priority 2 — 16 GB
- **Price (AUD):** $4,559 (Mwave)
- **Cheapest Vendor (AU):** Mwave Australia (NSW)
- **StaticIce URL:** `https://www.staticice.com.au/cgi-bin/search.cgi?q=G615LW-S5165W`

## Key Specs
- **SKU:** G615LW-S5165W
- **GPU:** NVIDIA GeForce RTX 5080, 16 GB
- **CPU:** Intel Core Ultra 9 275HX
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **Display:** 16"

## Conclusion
A dramatically better deal than initially thought — the cheapest confirmed AU price is $4,559 at Mwave, not $5,699. It is only $59 over budget. Any small cashback or coupon code will push this inside the $4,500 ceiling. With 16GB VRAM (RTX 5080), this becomes one of the highest-spec Track 1 candidates within realistic reach.

> **See also:** The sibling **G615LR-S5128W** (RTX 5070 Ti / 12GB) is available for **$4,199** from MSY/Umart/Mwave/Scorptec — firmly under budget and may represent better value if 16GB vs 12GB VRAM is not critical to your workloads.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/43_asus-rog-zephyrus-g16-rtx-5070-2025.md
`````markdown
<!-- TAGS: #Laptop #ASUS #NVIDIA #VRAM-12GB #Track1-Candidate #OverBudget -->
---
id: asus-rog-zephyrus-g16-rtx-5070-2025
category: laptop
name: ASUS ROG Zephyrus G16 (2025)
gpu: NVIDIA RTX 5070 Laptop GPU (12 GB)
vram: 12 GB
price_aud: 3999
score: 7.5 (Under Budget, Strong VRAM/Display)
---

# ASUS ROG Zephyrus G16 (2025) — GA605KP-QR044W

> ⚠️ **BUDGET ALERT:** At **$5,299.00**, this unit is ~$800 over the $4,500 budget ceiling. The "Zephyrus" tax for the premium thin-and-light CNC chassis is steep.

## Track 1 Status
- **Chassis family:** ASUS ROG Zephyrus G16
- **Target GPU:** RTX 5070 Laptop GPU 12 GB ✅ (Meets relaxed 8GB floor)
- **GOOD ENOUGH check:** ✅ **PASSED** — At **$3,999 (MSY/Umart)**, this is $501 under the budget ceiling. User previously saw $5,299 at PLE — MSY/Umart are $1,300 cheaper.

## Overview
- **VRAM Tier:** Meets Floor — 12 GB
- **Price (AUD):** **$3,362 brand new (eBay/jw_computers)** | $3,902 (eBay/jw_computers alt listing) | $3,999 (MSY/Umart) | $5,299 (PLE) | $5,486 (Mwave)
- **eBay seller:** jw_computers (99.8% positive, 14.8K reviews) — brand new, free delivery, Ryzen AI 7 350 model confirmed
- **treasure_pc_online:** eBay seller confirmed (100% positive, 15.8K reviews) but no current GA605KP listing found. Seller stocks other Zephyrus G16 models — worth checking directly.
- **Cheapest Confirmed:** eBay jw_computers @ **$3,362** (brand new, free delivery)
- **StaticIce URL:** `https://www.staticice.com.au/cgi-bin/search.cgi?q=GA605KP-QR044W`
- **eBay URL:** `https://www.ebay.com.au/sch/i.html?_nkw=ROG+Zephyrus+G16+2025+RTX+5070&_sacat=0&_sop=15`

## Key Specs
- **SKU:** GA605KP-QR044W
- **GPU:** NVIDIA GeForce RTX 5070, 12 GB
- **CPU:** AMD Ryzen AI 7 350
- **RAM:** 32 GB
- **Storage:** 2 TB
- **Display:** 16" OLED 2.5K 240Hz

## Conclusion
Now confirmed as one of the best-value candidates in the entire matrix. eBay's `jw_computers` has brand new units from **$3,362** (free delivery). MSY/Umart at $3,999 is the best AU-local alternative. The Zephyrus chassis also runs noticeably cooler and quieter than Strix/Legion alternatives. At $3,362 delivered and new, this challenges the Alienware Aurora R11 ($2,300 refurb) for best overall value when portability is factored in. **treasure_pc_online** is confirmed as an official ASUS authorised eBay reseller — worth checking their store directly for this model.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/44_asus-rog-strix-g16-rtx-5070ti-2025.md
`````markdown
<!-- TAGS: #Laptop #ASUS #NVIDIA #VRAM-12GB #Track1-Candidate -->
---
id: asus-rog-strix-g16-rtx-5070ti-2025
category: laptop
name: ASUS ROG Strix G16 (2025) — RTX 5070 Ti
gpu: NVIDIA RTX 5070 Ti Laptop GPU (12 GB)
vram: 12 GB
price_aud: 4199
score: 8.0 (Under Budget, Strong VRAM)
---

# ASUS ROG Strix G16 (2025) — G615LR-S5128W

> ℹ️ **SPEC NOTE:** This is the RTX 5070 Ti variant of the G16 Strix, a tier below the RTX 5080 SKU (G615LW-S5165W). At $4,199, it is significantly cheaper and comfortably within budget.

## Track 1 Status
- **Chassis family:** ASUS ROG Strix G16 ✅
- **Target GPU:** RTX 5070 Ti Laptop GPU 12 GB ✅ (Meets 8GB floor, preferred 12GB+ tier)
- **GOOD ENOUGH check:** ✅ **PASSED** — At **$4,199 (MSY/Umart/Mwave/Scorptec)**, well within the $4,500 ceiling.

## Overview
- **VRAM Tier:** Meets Floor — 12 GB
- **Price (AUD):** $4,199 (MSY / Umart / Mwave / Scorptec) | $4,669 (CPL)
- **Cheapest Vendor (AU):** MSY / Umart / Mwave / Scorptec — all at same price
- **StaticIce URL:** `https://www.staticice.com.au/cgi-bin/search.cgi?q=G615LR`

## Key Specs
- **SKU:** G615LR-S5128W
- **GPU:** NVIDIA GeForce RTX 5070 Ti, 12 GB
- **CPU:** Intel Core Ultra 9 275HX
- **RAM:** 32 GB DDR5
- **Storage:** 1 TB NVMe
- **Display:** 16" 2.5K WQXGA IPS 240Hz

## Conclusion
The G16 Strix RTX 5070 Ti variant at $4,199 is a very strong Track 1 contender — $135 under budget with the preferred 12GB VRAM tier. It matches the Zephyrus G16 AMD on VRAM, but has a different CPU platform (Intel vs AMD) and a less premium display (IPS vs OLED). The price difference between this and the Zephyrus G16 AMD at $3,362 (eBay) makes them competitors worth evaluating side-by-side.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/45_asus-rog-zephyrus-g16-intel-rtx-5070ti-2025.md
`````markdown
<!-- TAGS: #Laptop #ASUS #NVIDIA #VRAM-12GB #Track1-Candidate -->
---
id: asus-rog-zephyrus-g16-intel-rtx-5070ti-2025
category: laptop
name: ASUS ROG Zephyrus G16 (2025) Intel — RTX 5070 Ti
gpu: NVIDIA RTX 5070 Ti Laptop GPU (12 GB)
vram: 12 GB
price_aud: 4499
score: 7.8 (Just Within Budget)
---

# ASUS ROG Zephyrus G16 (2025) Intel — GU605CP

> ℹ️ **SPEC NOTE:** This is the Intel Core Ultra 9 285H variant of the Zephyrus G16 with RTX 5070 Ti. The AMD variant (GA605KP) uses Ryzen AI 7 350 with RTX 5070 (8GB). This Intel variant upgrades to 12GB RTX 5070 Ti and an Intel CPU.

## Track 1 Status
- **Chassis family:** ASUS ROG Zephyrus G16 ✅
- **Target GPU:** RTX 5070 Ti Laptop GPU 12 GB ✅ (Preferred 12GB+ tier)
- **GOOD ENOUGH check:** ✅ **PASSED** — At **$4,499 (MSY/Umart)**, exactly at the budget ceiling.

## Overview
- **VRAM Tier:** Meets Floor — 12 GB
- **Price (AUD):** $4,499 (MSY/Umart — 32GB/1TB config) | $4,999 (Mwave/Computer Alliance — 32GB/1TB) | $5,399 (32GB/2TB config)
- **Cheapest Vendor (AU):** MSY / Umart @ $4,499
- **StaticIce URL:** `https://www.staticice.com.au/cgi-bin/search.cgi?q=GU605CP`

## Key Specs
- **SKU:** GU605CP-QR077X (32GB/1TB) | GU605CP-QR029W (32GB/2TB)
- **GPU:** NVIDIA GeForce RTX 5070 Ti, 12 GB
- **CPU:** Intel Core Ultra 9 285H
- **RAM:** 32 GB LPDDR5X
- **Storage:** 1 TB or 2 TB NVMe
- **Display:** 16" OLED 2.5K 240Hz Nebula Display

## Conclusion
Premium Zephyrus chassis (OLED display, ultra-slim) with the preferred 12GB VRAM, at exactly $4,499. Compared to the AMD Zephyrus G16 at $3,362 (jw_computers eBay), this Intel model costs $1,137 more for the bump from RTX 5070 (8GB) → RTX 5070 Ti (12GB) and Intel vs AMD CPU platform. Worth evaluating if 12GB headroom is critical.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/46_asus-rog-zephyrus-g16-intel-rtx-5090-2025.md
`````markdown
<!-- TAGS: #Laptop #ASUS #NVIDIA #VRAM-24GB #Track1-Candidate #OverBudget -->
---
id: asus-rog-zephyrus-g16-intel-rtx-5090-2025
category: laptop
name: ASUS ROG Zephyrus G16 (2025) Intel — RTX 5090
gpu: NVIDIA RTX 5090 Laptop GPU (24 GB)
vram: 24 GB
price_aud: 6749
score: 5.0 (Far Over Budget)
---

# ASUS ROG Zephyrus G16 (2025) Intel — GU605CX-QR124X

> ⚠️ **BUDGET ALERT:** At **$6,749**, this is $2,249 over the $4,500 ceiling. Documented for completeness — would require extraordinary discount or resale to qualify.

## Track 1 Status
- **Chassis family:** ASUS ROG Zephyrus G16 ✅
- **Target GPU:** RTX 5090 Laptop GPU 24 GB ✅ (Top tier VRAM)
- **GOOD ENOUGH check:** ❌ **FAILED** — Price far exceeds $4,500 budget.

## Overview
- **VRAM Tier:** Priority 1 — 24 GB
- **Price (AUD):** $6,749 (Device Deal) | $6,899 (PCDIY) | $7,289 (TechBuy) | $7,299 (Computer Alliance) | $7,499 (MSY/Umart)
- **Cheapest Vendor (AU):** Device Deal (VIC) @ $6,749
- **StaticIce URL:** `https://www.staticice.com.au/cgi-bin/search.cgi?q=GU605CX`

## Key Specs
- **SKU:** GU605CX-QR124X
- **GPU:** NVIDIA GeForce RTX 5090, 24 GB
- **CPU:** Intel Core Ultra 9 285H
- **RAM:** 64 GB LPDDR5X
- **Storage:** 2 TB NVMe
- **Display:** 16" OLED 2.5K 240Hz Nebula Display

## Conclusion
The ultimate Zephyrus G16 configuration, but at ~$6,749 minimum, it is completely out of the $4,500 budget. Not a viable Track 1 candidate unless a significant sale or open-box deal drops it below $4,500.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/47_asus-rog-strix-g18-2024-rtx4080.md
`````markdown
<!-- TAGS: #Laptop #ASUS #NVIDIA #VRAM-12GB #Track1-Candidate #Gen2024 -->
---
id: asus-rog-strix-g18-2024-rtx4080
category: laptop
name: ASUS ROG Strix G18 (2024) — RTX 4080
gpu: NVIDIA RTX 4080 Laptop GPU (12 GB)
vram: 12 GB
price_aud: 2455
score: 8.5 (Exceptional Value — 2024 Gen)
---

# ASUS ROG Strix G18 (2024) — G814JZR / G814JZ

> ℹ️ **VRAM PARITY NOTE:** RTX 4080 Laptop = **12 GB GDDR6** — identical VRAM to the 2025 RTX 5070 Ti. For local LLM inference (VRAM-bound), this is a direct functional equivalent at a significantly lower price.

## Track 1 Status
- **Chassis family:** ASUS ROG Strix G18 ✅ (+Bonus for 18" thermals)
- **Target GPU:** RTX 4080 Laptop GPU 12 GB ✅ (Meets relaxed 8GB floor, preferred 12GB tier)
- **GOOD ENOUGH check:** ✅ **PASSED** — eBay sourced units confirmed from ~$2,455 AUD.

## Generation Comparison
| Spec | G18 2024 | G18 2025 |
|:---|:---|:---|
| GPU | RTX 4080 (12GB) | RTX 5070 Ti (12GB) |
| CPU | i9-14900HX | Core Ultra 9 275HX |
| VRAM | 12 GB | 12 GB |
| GPU Gen | Ada Lovelace | Blackwell |
| Price (~AU) | ~$2,455 (refurb eBay) | $4,334 (MSY/Umart new) |

> **LLM inference verdict:** VRAM is identical. The RTX 5070 Ti has ~15–20% better compute throughput, but for token generation bottlenecked by VRAM bandwidth, the real-world difference on 7B–13B parameter models will be modest. The ~$1,879 price saving is significant.

## Overview
- **Price (AUD):** ~$2,455 refurb (eBay itsworthmore, US ship) | $3,146 new-other (eBay, US ship)
- **eBay note:** No AU-local stock confirmed on StaticIce. All listings ship from USA — add ~$880–900 delivery.
- **Cheapest all-in AU estimate:** ~$3,340 (refurb + delivery) vs $4,334 for 2025 new AU retail
- **StaticIce:** No AU retail listings found (cleared out)

## Key Specs
- **SKU:** G814JZR / G814JZ (various configs)
- **GPU:** NVIDIA GeForce RTX 4080 Laptop, 12 GB GDDR6
- **CPU:** Intel Core i9-14900HX or i9-13980HX
- **RAM:** 32–64 GB DDR5
- **Storage:** 1–2 TB NVMe
- **Display:** 18" QHD+ 240Hz

## Conclusion
The 2024 G18 RTX 4080 is the VRAM-equivalent predecessor to the 2025 G18 RTX 5070 Ti. For LLM use cases, it is a compelling budget play — but there are no AU-local eBay or retail listings. All available units ship from the USA, which adds ~$880 delivery and import risk. The all-in cost (~$3,340) narrows the gap with the 2025 model ($4,334 new). Worth monitoring for AU-local listings.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/48_asus-rog-zephyrus-g16-2024-rtx4080.md
`````markdown
<!-- TAGS: #Laptop #ASUS #NVIDIA #VRAM-16GB #Track1-Candidate #Gen2024 -->
---
id: asus-rog-zephyrus-g16-2024-rtx4080
category: laptop
name: ASUS ROG Zephyrus G16 (2024) — RTX 4080
gpu: NVIDIA RTX 4080 Laptop GPU (12 GB)
vram: 12 GB
price_aud: 3500
score: 8.0 (Strong Value — 2024 Gen with OLED)
---

# ASUS ROG Zephyrus G16 (2024) — GU605MI / GU605MH

> ℹ️ **VRAM PARITY NOTE:** RTX 4080 Laptop = **12 GB GDDR6** — identical VRAM to the 2025 RTX 5070 Ti. The 2024 Zephyrus also has the premium OLED display carried forward into the 2025 model.

## Track 1 Status
- **Chassis family:** ASUS ROG Zephyrus G16 ✅
- **Target GPU:** RTX 4080 Laptop GPU 12 GB ✅ (Preferred 12GB tier)
- **GOOD ENOUGH check:** ✅ **PASSED (with caveats)** — AU retail has one listing at $4,181 (Device Deal). eBay international listings from ~$2,762–$3,377 + delivery.

## Generation Comparison
| Spec | Zephyrus G16 2024 | Zephyrus G16 2025 (AMD) |
|:---|:---|:---|
| GPU | RTX 4080 (12GB) | RTX 5070 (12GB) |
| CPU | Intel Core Ultra 9 185H | AMD Ryzen AI 7 350 |
| VRAM | 12 GB | 12 GB |
| Display | OLED 2.5K 240Hz | OLED 2.5K 240Hz |
| Price (~AU) | $4,181 (Device Deal) | $3,362 (eBay jw_computers new) |

> **Key insight:** The 2024 model at $4,181 (Device Deal, clearance) is actually *more expensive* than the brand-new 2025 AMD model at $3,362. This makes the 2024 model a poor value at retail pricing. However, eBay pre-owned units from USA at ~$2,762 + ~$800 delivery ≈ $3,560 all-in become comparable.

## Overview
- **Price (AUD):** $4,181 AU retail (Device Deal, VIC — clearance, single unit) | ~$2,762 pre-owned + ~$803 delivery (eBay rose_2004_e) | ~$3,068 new-other + ~$849 delivery (eBay)
- **AU retail:** Device Deal (VIC) — only AU retailer with stock, likely clearance
- **StaticIce URL:** `https://www.staticice.com.au/cgi-bin/search.cgi?q=GU605MI`

## Key Specs
- **SKU:** GU605MI-QR074X (confirmed AU listing)
- **GPU:** NVIDIA GeForce RTX 4080 Laptop, 12 GB GDDR6 (Note: some configs may be 8GB RTX 4070)
- **CPU:** Intel Core Ultra 9 185H
- **RAM:** 32 GB LPDDR5X
- **Storage:** 1 TB NVMe
- **Display:** 16" OLED 2.5K 240Hz

## Conclusion
The 2024 Zephyrus G16 with RTX 4080 is the premium OLED predecessor to the 2025 model. At $4,181 AU retail (Device Deal clearance), it is actually *more expensive than the brand-new 2025 AMD variant at $3,362*. Unless this price drops further, the 2025 model is better value. If international eBay all-in cost drops below ~$3,200, it becomes competitive again.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/asus-proart-px13.md
`````markdown
---
id: asus-proart-px13
category: laptop
name: ASUS ProArt PX13
vram: 128 GB unified
---
# ASUS ProArt PX13
13.3" Strix Halo
ONLY pursue if refurbished/open-box/sale pricing <=$4,500 AUD
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/asus-rog-flow-z13.md
`````markdown
<!-- TAGS: #Laptop #ASUS #StrixHalo #Track1-Candidate -->
---
id: asus-rog-flow-z13-2025
category: laptop
name: ASUS ROG Flow Z13 (2025)
soc: AMD Ryzen AI Max+ 395 (Strix Halo)
unified_memory: UNKNOWN
price_aud: UNKNOWN
score: UNKNOWN — Pending Specs/Price
---

# ASUS ROG Flow Z13 (2025) — AMD Strix Halo

> ℹ️ **SPEC NOTE:** The 2025 iteration of the Flow Z13 uses the incredibly powerful AMD Ryzen AI Max+ 395 SoC. Because it uses Strix Halo unified memory instead of a low-VRAM discrete GPU (like older models), it is an excellent Path 1B candidate for local LLM inference.

## Track 1 Status
- **Chassis family:** ASUS ROG Flow Z13
- **Target SoC:** AMD Ryzen AI Max+ 395 ✅ (Meets Strix Halo requirement)
- **Unified Memory:** UNKNOWN (Must verify if it meets the relaxed 16 GB floor)
- **GOOD ENOUGH check:** PENDING — Requires final configuration (RAM) and price verification.

## Overview
- **Price (AUD):** UNKNOWN
- **Vendor (AU):** ASUS Australia
- **URL:** `https://rog.asus.com/au/laptops/rog-flow/rog-flow-z13-2025/`

## Key Specs
- **SoC:** AMD Ryzen AI Max+ 395 (with Radeon 8060S Graphics)
- **Unified Memory:** UNKNOWN
- **Storage:** UNKNOWN
- **Form Factor:** 13-inch Gaming Tablet / Ultra-portable

## Conclusion
A massive architectural leap from the previous Intel/NVIDIA models. By leveraging Strix Halo, the 2025 Flow Z13 avoids the severe VRAM bottlenecks of low-end discrete GPUs, making this 13-inch device a legitimate local AI powerhouse, provided the memory configuration meets our requirements.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/asus-tuf-a14.md
`````markdown
---
id: asus-tuf-a14
category: laptop
name: ASUS TUF Gaming A14 (2026) FA401EA
vram: 32 GB unified
---
# ASUS TUF Gaming A14
14" Strix Halo
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/asus-zenbook-duo-ux8406.md
`````markdown
<!-- TAGS: #Laptop #ASUS #IntelArc #NoDiscreteGPU #FailsTrack1 -->
---
id: asus-zenbook-duo-ux8406
category: laptop
name: ASUS Zenbook Duo UX8406
gpu: Intel Arc Graphics (Integrated)
vram: Shared
price_aud: UNKNOWN
score: 0.0 (Fails Track 1)
---

# ASUS Zenbook Duo UX8406 — eBay Listing

> ⚠️ **SPEC ALERT:** This is a dual-screen productivity laptop without a discrete NVIDIA GPU or an AMD Strix Halo SoC. It completely fails the baseline requirements for Track 1.

## Track 1 Status
- **Chassis family:** ASUS Zenbook Duo
- **Target GPU:** Integrated Intel Arc ❌ (No discrete GPU)
- **GOOD ENOUGH check:** ❌ **FAILED** — Unsupported hardware architecture for our specific local LLM requirements.

## Overview
- **Price (AUD):** UNKNOWN (See eBay listing)
- **Vendor (AU):** eBay AU
- **URL:** `https://www.ebay.com.au/itm/177334563385`

## Key Specs
- **GPU:** Intel Arc Graphics (Integrated)
- **CPU:** Intel Core Ultra 9 185H
- **RAM:** 32 GB
- **Storage:** 1 TB SSD
- **Display:** 14-inch 3K OLED Touch (Dual Screens)

## Conclusion
Rejected. While the dual-screen form factor is innovative, the lack of a discrete high-VRAM GPU or an advanced unified memory SoC like Strix Halo makes it incapable of running large local LLMs efficiently.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/hp-zbook-ultra-14-g1a.md
`````markdown
<!-- TAGS: #Laptop #HP #StrixHalo #UnifiedMemory-16GB -->
---
id: hp-zbook-ultra-14-g1a
category: laptop
name: HP ZBook Ultra 14 G1a
soc: AMD Ryzen AI Max Pro 380 (Strix Halo)
unified_memory: 16 GB
price_aud: UNKNOWN
score: UNKNOWN — Pending Price
---

# HP ZBook Ultra 14 G1a — AMD Strix Halo

> ℹ️ **SPEC NOTE:** This specific configuration features **16 GB of unified memory**. This meets the newly relaxed Path 1B minimum of 16 GB unified memory.

## Track 1 Status
- **Chassis family:** HP ZBook Ultra 14 G1a
- **Target SoC:** AMD Ryzen AI Max Pro 380 ✅ (Meets Strix Halo requirement)
- **Unified Memory:** 16 GB ✅ (Meets relaxed 16 GB floor)
- **GOOD ENOUGH check:** PENDING — Requires final price and availability verification.

## Overview
- **Memory Tier:** Meets Floor — 16 GB
- **Price (AUD):** UNKNOWN
- **Vendor (AU):** BPC Tech / HP Australia
- **URLs:** 
  - `https://www.bpctech.com.au/product/bg1p5pt-hp-zbook-ultra-14-g1a-14-wuxga-amd-ai-max-pro-380-16gb-512gb-ssd-win-11-pro-3yr-nbd-onsite-wty.html`
  - `https://www.hp.com/au-en/shop/hp-zbook-ultra-14-inch-g1a-mobile-workstation-pc-d9hr9pt.html`

## Key Specs
- **SoC:** AMD Ryzen AI Max Pro 380
- **Unified Memory:** 16 GB
- **Storage:** 512 GB SSD
- **Display:** 14" WUXGA

## Conclusion
With the unified memory floor relaxed to 16 GB, this Strix Halo ultra-portable is now an eligible Path 1B candidate. However, allocating only 16 GB of system RAM (which must be shared between the CPU and the GPU tile) will bottleneck local LLM inference compared to 32 GB+ models. It requires an exceptionally good price to justify the memory compromise.
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-009_lenovo-legion-pro-7i.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: lenovo-legion-pro-7i
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Lenovo Legion Pro 7i
gpu: RTX 4090 Mobile
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $4575 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Lenovo Legion Pro 7i

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $4575 AUD
- **Retailer:** Mike PC / Lenovo
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4090 Mobile
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** i9-14900HX
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
The best emotional-but-defensible one-machine route

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-010_msi-raider-18-hx-ai-a2xwjg.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-24GB #New #TrackUnknown #Verified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: msi-raider-18-hx-ai-a2xwjg
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: MSI Raider 18 HX AI A2XWJG
gpu: RTX 5090 Mobile
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $8488 AUD
condition: New
au_stock: UNKNOWN
verification: Verified
status: Active
score: UNKNOWN — pending manual review
---

# MSI Raider 18 HX AI A2XWJG

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $8488 AUD
- **Retailer:** Scorptec / JW Computers
- **URL:** [https://www.scorptec.com.au/product/ready-to-run-pcs/gaming-pc/124318-r2r10638](https://www.scorptec.com.au/product/ready-to-run-pcs/gaming-pc/124318-r2r10638)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090 Mobile
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 285HX
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Massive desktop replacement that overcomes traditional laptop VRAM limits

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-011_dell-alienware-m18-r2-area-51.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: dell-alienware-m18-r2-area-51
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Dell Alienware m18 R2 / Area-51
gpu: RTX 5090 Mobile
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $4499 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Dell Alienware m18 R2 / Area-51

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $4499 AUD
- **Retailer:** Dell Outlet / Best Buy
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090 Mobile
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 275HX
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
18-inch desktop replacement offering 24GB of mobile VRAM

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-012_razer-blade-18.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: razer-blade-18
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Razer Blade 18
gpu: RTX 5090 Mobile
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $7400 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Razer Blade 18

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $7400 AUD
- **Retailer:** Razer AU
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090 Mobile
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 275HX
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Highly premium CNC-milled unibody laptop featuring Thunderbolt 5

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-013_msi-crosshair-18-hx-ai.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: msi-crosshair-18-hx-ai
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: MSI Crosshair 18 HX AI
gpu: RTX 5070 Mobile
vram: 16 GB
unified_memory: UNKNOWN
price_aud: UNKNOWN
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# MSI Crosshair 18 HX AI

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** UNKNOWN
- **Retailer:** PB Tech AU
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5070 Mobile
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 275HX
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
High-end 18-inch laptop delivering strong AI performance

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-014_lenovo-thinkpad-t14-t14s-refurbished.md
`````markdown
<!-- TAGS: #Laptop #VRAM-Unknown #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: lenovo-thinkpad-t14-t14s-refurbished
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Lenovo ThinkPad T14 / T14s (Refurbished)
gpu: UNKNOWN
vram: UNKNOWN
unified_memory: UNKNOWN
price_aud: $800 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Lenovo ThinkPad T14 / T14s (Refurbished)

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $800 AUD
- **Retailer:** Australian Computer Traders
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** UNKNOWN
- **VRAM:** UNKNOWN
- **Unified Memory:** UNKNOWN
- **CPU:** Intel i5/i7
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
The absolute best companion device for a desktop-first strategy

## AI Capability Summary
UNKNOWN — to be completed after manual spec verification.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [ ] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-015_dell-latitude-7330-2-in-1-refurbished.md
`````markdown
<!-- TAGS: #Laptop #VRAM-Unknown #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: dell-latitude-7330-2-in-1-refurbished
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Dell Latitude 7330 2-in-1 (Refurbished)
gpu: UNKNOWN
vram: UNKNOWN
unified_memory: UNKNOWN
price_aud: $1254 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Dell Latitude 7330 2-in-1 (Refurbished)

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $1254 AUD
- **Retailer:** Australian Computer Traders
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** UNKNOWN
- **VRAM:** UNKNOWN
- **Unified Memory:** UNKNOWN
- **CPU:** 12th-gen Intel i5/i7
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Excellent portable cloud-first companion with a touchscreen

## AI Capability Summary
UNKNOWN — to be completed after manual spec verification.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [ ] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-036_alienware-16-area-51-new-config.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: alienware-16-area-51-new-config
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Alienware 16 Area-51 new config
gpu: RTX 5070 Ti Mobile
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $4198.70 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Alienware 16 Area-51 new config

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $4198.70 AUD
- **Retailer:** Dell AU
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5070 Ti Mobile
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 290HX
- **RAM:** 16 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Expensive for only 16GB VRAM; weak value for FLUX-class local image work

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-045_msi-stealth-a16-5080.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: msi-stealth-a16-5080
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: MSI Stealth A16 5080
gpu: RTX 5080 Mobile
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $4999 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# MSI Stealth A16 5080

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $4999 AUD
- **Retailer:** UNKNOWN
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5080 Mobile
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Loud under load

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-051_acer-predator-helios-18-rtx-4090-refurbished.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-16GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: acer-predator-helios-18-rtx-4090-refurbished
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Acer Predator Helios 18 RTX 4090 refurbished
gpu: RTX 4090 Mobile
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $4449 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Acer Predator Helios 18 RTX 4090 refurbished

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $4449 AUD
- **Retailer:** Acer AU Clearance
- **URL:** [https://store.acer.com/en-au/clearances/laptop](https://store.acer.com/en-au/clearances/laptop)
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4090 Mobile
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** i9-14900HX
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Desktop Replacement

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-052_acer-predator-helios-neo-16s-ai-rtx-5060.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-8GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: acer-predator-helios-neo-16s-ai-rtx-5060
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: Acer Predator Helios Neo 16S AI RTX 5060
gpu: RTX 5060
vram: 8 GB
unified_memory: UNKNOWN
price_aud: $2399 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Acer Predator Helios Neo 16S AI RTX 5060

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2399 AUD
- **Retailer:** Acer AU Clearance
- **URL:** [https://store.acer.com/en-au/](https://store.acer.com/en-au/)
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5060
- **VRAM:** 8 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Core Ultra 9 275HX
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Refurbished entry level laptop

## AI Capability Summary
Baseline — 8 GB VRAM sufficient for 7B Q4; larger models require significant offload.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-053_erazer-major-x20-rtx-4070.md
`````markdown
<!-- TAGS: #Laptop #NVIDIA #VRAM-8GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: erazer-major-x20-rtx-4070
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: ERAZER Major X20 RTX 4070
gpu: RTX 4070
vram: 8 GB
unified_memory: UNKNOWN
price_aud: $2999 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# ERAZER Major X20 RTX 4070

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2999 AUD
- **Retailer:** ERAZER AU
- **URL:** [https://erazer.com.au/collections/16-inch-screen-size](https://erazer.com.au/collections/16-inch-screen-size)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4070
- **VRAM:** 8 GB
- **Unified Memory:** UNKNOWN
- **CPU:** i9-14900HX
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Not recommended due to 8GB VRAM

## AI Capability Summary
Baseline — 8 GB VRAM sufficient for 7B Q4; larger models require significant offload.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/04_Laptops_Mainline/intake-072_hp-zbook-ultra-14-g1a.md
`````markdown
<!-- TAGS: #Laptop #AMD #VRAM-Unknown #New #TrackUnknown #NeedsVerification #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Laptop -->
---
id: hp-zbook-ultra-14-g1a
category: laptop
track: UNKNOWN
pathway: UNKNOWN
name: HP ZBook Ultra 14 G1a
gpu: Radeon 8060S
vram: UNKNOWN
unified_memory: UNKNOWN
price_aud: UNKNOWN
condition: New
au_stock: UNKNOWN
verification: Needs Verification
status: Active
score: UNKNOWN — pending manual review
---

# HP ZBook Ultra 14 G1a

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** UNKNOWN
- **Retailer:** HP
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** Radeon 8060S
- **VRAM:** UNKNOWN
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen AI MAX 395+
- **RAM:** 128 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Premium mobile workstation; 14-inch OLED

## AI Capability Summary
UNKNOWN — to be completed after manual spec verification.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/05_Apple_Silicon_Systems/01_apple-mac-studio-m4-max-64gb.md
`````markdown
<!-- TAGS: #AppleSilicon #UnifiedMemory #VRAM-64GB #New #PrimaryWorkstation #AgenticAI #ImageGeneration #Shortlist -->
<!-- PRODUCT CARD START: Apple Mac Studio M4 Max 64GB -->
### [90 / 100] — Apple Mac Studio M4 Max 64GB

- **Category**: Apple Mac
- **Condition**: UNKNOWN
- **Price (AUD)**: $4661
- **Vendor**: UNKNOWN
- **URL**: https://www.unsw.edu.au/content/dam/pdfs/myit/catalogues/2025-04-unsw-apple-catalogue-v1.pdf

#### Hardware Profile
- **GPU**: 64GB
- **CPU**: UNKNOWN
- **RAM**: UNKNOWN
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 90 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 90 / 110 (81%)

#### AI Capability Summary
Capable of running models suitable for 64GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 64GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Apple Mac Studio M4 Max 64GB -->
`````

## File: NotebookLM_Workspaces/05_Apple_Silicon_Systems/02_mac-studio-m4-max-64gb1tb-education-config.md
`````markdown
<!-- TAGS: #AppleSilicon #UnifiedMemory #VRAM-64GB #New #EducationConfig #PrimaryWorkstation #AgenticAI #Shortlist -->
<!-- PRODUCT CARD START: Mac Studio M4 Max 64GB/1TB Education config -->
### [90 / 100] — Mac Studio M4 Max 64GB/1TB Education config

- **Category**: Apple Mac
- **Condition**: UNKNOWN
- **Price (AUD)**: $4,414
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: 64GB
- **CPU**: UNKNOWN
- **RAM**: 64GB
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 90 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 90 / 110 (81%)

#### AI Capability Summary
Capable of running models suitable for 64GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 64GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Mac Studio M4 Max 64GB/1TB Education config -->
`````

## File: NotebookLM_Workspaces/05_Apple_Silicon_Systems/03_mac-studio-m4-max-64gb-unified-memory-1tb-ssd.md
`````markdown
<!-- TAGS: #AppleSilicon #UnifiedMemory #VRAM-64GB #New #PrimaryWorkstation #AgenticAI #NeedsReview -->
<!-- PRODUCT CARD START: Mac Studio M4 Max 64GB unified memory, 1TB SSD -->
### [75 / 100] — Mac Studio M4 Max 64GB unified memory, 1TB SSD

- **Category**: Apple Mac
- **Condition**: UNKNOWN
- **Price (AUD)**: $4849.0
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: 64GB
- **CPU**: UNKNOWN
- **RAM**: 64GB unified
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 10/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 75 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 75 / 110 (68%)

#### AI Capability Summary
Capable of running models suitable for 64GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 64GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Mac Studio M4 Max 64GB unified memory, 1TB SSD -->
`````

## File: NotebookLM_Workspaces/05_Apple_Silicon_Systems/04_refurb-mac-studio-m2-ultra-64gb.md
`````markdown
<!-- TAGS: #AppleSilicon #UnifiedMemory #VRAM-64GB #Refurbished #PrimaryWorkstation #AgenticAI #NeedsReview -->
<!-- PRODUCT CARD START: Refurb Mac Studio M2 Ultra 64GB -->
### [75 / 100] — Refurb Mac Studio M2 Ultra 64GB

- **Category**: Apple Mac
- **Condition**: UNKNOWN
- **Price (AUD)**: $5349.0
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: 64GB
- **CPU**: UNKNOWN
- **RAM**: 64GB unified
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 10/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 75 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 75 / 110 (68%)

#### AI Capability Summary
Capable of running models suitable for 64GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 64GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Refurb Mac Studio M2 Ultra 64GB -->
`````

## File: NotebookLM_Workspaces/05_Apple_Silicon_Systems/05_apple-macbook-pro-14-m4-pro-48gb.md
`````markdown
<!-- TAGS: #AppleSilicon #UnifiedMemory #VRAM-48GB #Laptop #New #Travel #SecondaryLaptop #Coding #NonUpgradeable -->
<!-- PRODUCT CARD START: Apple MacBook Pro 14 M4 Pro 48GB -->
### [90 / 100] — Apple MacBook Pro 14 M4 Pro 48GB

- **Category**: Apple Mac
- **Condition**: UNKNOWN
- **Price (AUD)**: $4816
- **Vendor**: UNKNOWN
- **URL**: https://www.unsw.edu.au/content/dam/pdfs/myit/catalogues/2025-04-unsw-apple-catalogue-v1.pdf

#### Hardware Profile
- **GPU**: 48GB
- **CPU**: UNKNOWN
- **RAM**: 48GB unified
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 90 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 90 / 110 (81%)

#### AI Capability Summary
Capable of running models suitable for 48GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 48GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Apple MacBook Pro 14 M4 Pro 48GB -->
`````

## File: NotebookLM_Workspaces/05_Apple_Silicon_Systems/06_apple-macbook-pro-16-m3-max-48gb-open-box.md
`````markdown
<!-- TAGS: #AppleSilicon #UnifiedMemory #VRAM-48GB #Laptop #OpenBox #Travel #SecondaryLaptop #Coding #NonUpgradeable -->
<!-- PRODUCT CARD START: Apple MacBook Pro 16 M3 Max 48GB open box -->
### [90 / 100] — Apple MacBook Pro 16 M3 Max 48GB open box

- **Category**: Apple Mac
- **Condition**: UNKNOWN
- **Price (AUD)**: $3999
- **Vendor**: UNKNOWN
- **URL**: https://www.phonebot.com.au/macbook-pro/apple-macbook-pro-16-inch-2023-m3-max-chip-48gb-1tb-open-box

#### Hardware Profile
- **GPU**: 48GB
- **CPU**: UNKNOWN
- **RAM**: 48GB unified
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 90 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 90 / 110 (81%)

#### AI Capability Summary
Capable of running models suitable for 48GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 48GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Apple MacBook Pro 16 M3 Max 48GB open box -->
`````

## File: NotebookLM_Workspaces/05_Apple_Silicon_Systems/07_refurbished-macbook-pro-16-inch-m4-max-48gb1tb.md
`````markdown
<!-- TAGS: #AppleSilicon #UnifiedMemory #VRAM-48GB #Laptop #Refurbished #Travel #SecondaryLaptop #Coding #NonUpgradeable -->
<!-- PRODUCT CARD START: Refurbished MacBook Pro 16-inch M4 Max 48GB/1TB -->
### [84 / 100] — Refurbished MacBook Pro 16-inch M4 Max 48GB/1TB

- **Category**: Apple Mac
- **Condition**: UNKNOWN
- **Price (AUD)**: $5,259
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: 48GB
- **CPU**: UNKNOWN
- **RAM**: 48GB
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 16/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 6/10
- **Raw Score**: 84 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 84 / 110 (76%)

#### AI Capability Summary
Capable of running models suitable for 48GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 48GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Refurbished MacBook Pro 16-inch M4 Max 48GB/1TB -->
`````

## File: NotebookLM_Workspaces/05_Apple_Silicon_Systems/08_apple-mac-studio-m4-max-36gb.md
`````markdown
<!-- TAGS: #AppleSilicon #UnifiedMemory #VRAM-36GB #New #PrimaryWorkstation #AgenticAI #NeedsReview -->
<!-- PRODUCT CARD START: Apple Mac Studio M4 Max 36GB -->
### [90 / 100] — Apple Mac Studio M4 Max 36GB

- **Category**: Apple Mac
- **Condition**: UNKNOWN
- **Price (AUD)**: $3716
- **Vendor**: UNKNOWN
- **URL**: https://www.unsw.edu.au/content/dam/pdfs/myit/catalogues/2025-04-unsw-apple-catalogue-v1.pdf

#### Hardware Profile
- **GPU**: 36GB
- **CPU**: UNKNOWN
- **RAM**: 36GB unified
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 90 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 90 / 110 (81%)

#### AI Capability Summary
Capable of running models suitable for 36GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 36GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Apple Mac Studio M4 Max 36GB -->
`````

## File: NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/16_minisforum-ms-01-deg1-oculink-rtx-3090-24gb.md
`````markdown
<!-- TAGS: #MiniPC #OCuLink #eGPU #NVIDIA #VRAM-24GB #New #Expandable #AgenticAI #ConditionalBuy -->
<!-- PRODUCT CARD START: Minisforum MS-01 + DEG1 OCuLink + RTX 3090 24GB -->
### [90 / 100] — Minisforum MS-01 + DEG1 OCuLink + RTX 3090 24GB

- **Category**: Mini PC / eGPU
- **Condition**: UNKNOWN
- **Price (AUD)**: $Est. 3,000–4,100; 3600.0
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: 24GB
- **CPU**: UNKNOWN
- **RAM**: 24GB VRAM external
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 90 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 90 / 110 (81%)

#### AI Capability Summary
Capable of running models suitable for 24GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 24GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Minisforum MS-01 + DEG1 OCuLink + RTX 3090 24GB -->
`````

## File: NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/40_minisforum-ai-x1-pro-strix-halo.md
`````markdown
<!-- TAGS: #MiniPC #AMD #StrixHalo #UnifiedMemory #Track2-PathwayC #New #NeedsManualData #VRAM-Unified-64GB+ -->
---
id: minisforum-ai-x1-pro-strix-halo
category: mini-pc
pathway: Track2-C
name: Minisforum AI X1 Pro — AMD Ryzen AI Max+ (Strix Halo, up to 128 GB)
gpu: AMD Radeon integrated Strix Halo GPU (unified memory)
vram: UNKNOWN (unified — 64 GB / 96 GB / 128 GB configs; confirm SKU)
score: UNKNOWN — pending manual AU retailer data
---

# Minisforum AI X1 Pro — AMD Ryzen AI Max+ (Strix Halo)

> ⚠️ **BLANK SHELL — all fields require manual data entry from AU retailer research.**
> Agent must not infer or guess missing values. UNKNOWN fields stay UNKNOWN until manually updated.

## Track 2 Pathway C Status
- **Pathway:** C — Unified Memory Mini PC
- **SoC requirement:** AMD Ryzen AI Max+ (Strix Halo) ✅ — confirmed SoC family (verify exact model at purchase)
- **Unified memory floor:** 64 GB minimum required for Pathway C gate clearance
- **Gate status:** ALL gates UNKNOWN — manual verification required before any action

## Pathway C Go/No-Go Gate Checklist
- [ ] SoC confirmed as Strix Halo (Ryzen AI Max / AI Max+) — NOT standard Ryzen or Intel
- [ ] Unified memory ≥ 64 GB confirmed from spec sheet for this SKU
- [ ] AU stock confirmed at credible retailer (Scorptec, Mwave, Centre Com, or official AU distributor)
- [ ] Price within AUD budget (0–4,000 AUD)
- [ ] Thermal adequacy confirmed — active cooling present and sufficient for sustained LLM inference
- [ ] No disqualifying ROCm gap for target workloads

## Overview
- **Unified Memory Tier:** UNKNOWN — expected configs: 64 GB / 96 GB / 128 GB (confirm SKU)
- **Price (AUD):** UNKNOWN — requires AU retailer check
- **Vendor (AU):** UNKNOWN — check: official Minisforum AU distributor, Scorptec, Mwave, Centre Com
- **In stock in AU:** UNKNOWN ← **critical gate**

## Key Specs
- **SoC:** AMD Ryzen AI Max+ (Strix Halo) — confirm exact model variant (890M, 395+, or equivalent)
- **Unified Memory:** UNKNOWN GB LPDDR5X — confirm SKU (64 / 96 / 128 GB options expected)
- **GPU portion (estimated):** UNKNOWN — Strix Halo typically allocates 60–75% of unified memory to GPU; 128 GB config ≈ 96 GB GPU-accessible
- **CPU cores:** UNKNOWN
- **Storage:** UNKNOWN (M.2 slots — confirm count and size)
- **Ports:** UNKNOWN — confirm Thunderbolt / USB4 / display outputs
- **Cooling:** UNKNOWN — confirm active fan cooling (passive = ⚠️ flag for sustained inference)
- **Form factor:** Mini PC / compact desktop
- **Dimensions:** UNKNOWN
- **Power supply:** UNKNOWN W — confirm external adapter or internal PSU
- **Warranty (AU):** UNKNOWN

## Thermal Notes
- **Sustained TDP (SoC):** UNKNOWN W
- **Cooling system:** UNKNOWN — active cooling required; passive-only is a Pathway C disqualifying flag
- **Thermal reputation under sustained load:** UNKNOWN

## ROCm / Software Compatibility
- **ROCm version support:** UNKNOWN — flag any known gaps for llama.cpp, Ollama, VLLM workloads
- **HIP SDK:** UNKNOWN
- **Known compatibility issues:** UNKNOWN

## AI Capability Summary
UNKNOWN — to be completed after specs confirmed. At 128 GB unified memory: expect capability for 70B Q4 models fully in-memory; 405B Q4 with offloading. At 64 GB: 34B–70B Q4 range. This is the primary Pathway C candidate due to memory ceiling potential.

## Rubric Scores (Pathway C profile — all UNKNOWN)
- UnifiedMemory_Adequacy: UNKNOWN
- SoC_Compute_Tier: UNKNOWN
- Sustained_Thermal_Rating: UNKNOWN
- AU_Retailer_Confidence: UNKNOWN ← **gate-critical**
- Price_AUD_Competitiveness: UNKNOWN
- ROCm_Compatibility_Flag: UNKNOWN ← **disqualifying flag if severe gap**
- Cooling_Adequacy: UNKNOWN ← **disqualifying flag if passive-only**
- Connectivity_Score: UNKNOWN

## Verification Required Before Any Action
- [ ] Confirm AU stock from named retailer with URL and price
- [ ] Confirm SoC: Ryzen AI Max+ (Strix Halo)
- [ ] Confirm exact unified memory size for available AU SKU (64 / 96 / 128 GB)
- [ ] Confirm active cooling present (fan, heat pipe — not passive slab)
- [ ] Confirm M.2 slot count and storage config
- [ ] Confirm external PSU wattage
- [ ] Confirm all display/port outputs
- [ ] Confirm warranty and AU return policy
- [ ] Confirm ROCm compatibility for llama.cpp / Ollama — check community reports
`````

## File: NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/hp_mini_pc_placeholder.md
`````markdown
---
id: hp-mini-pc-placeholder
category: mini-pc
name: HP Workstation Mini PC
vram: UNKNOWN
---
# HP Workstation Mini PC
Placeholder for HP Z2 Mini G1a or Elite Mini 800 G11 AI (Strix Halo variant).
All fields UNKNOWN pending verification.
`````

## File: NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/hp-z2-mini-g1a-strix-halo.md
`````markdown
<!-- TAGS: #Desktop #MiniPC #HP #StrixHalo #UnifiedMemory-32GB -->
---
id: hp-z2-mini-g1a-strix-halo
category: mini_pc
name: HP Z2 Mini G1a
soc: AMD Ryzen AI Max Pro 390 (Strix Halo)
unified_memory: 32 GB
price_aud: UNKNOWN
score: UNKNOWN — Pending Price
---

# HP Z2 Mini G1a — AMD Strix Halo

> ℹ️ **SPEC NOTE:** This specific configuration features **32 GB of unified memory**. This meets the newly relaxed Track 2 Pathway C minimum of 32 GB unified memory.

## Track 2 Status
- **Pathway:** Pathway C (Unified Memory Mini PC)
- **Target SoC:** AMD Ryzen AI Max Pro 390 (Strix Halo) ✅ (Meets SoC requirement)
- **Unified Memory:** 32 GB ✅ (Meets relaxed 32 GB minimum floor)
- **GOOD ENOUGH check:** PENDING — Requires final price and availability verification.

## Overview
- **Memory Tier:** Meets Floor — 32 GB
- **Price (AUD):** UNKNOWN
- **Vendor (AU):** BPC Tech / HP Australia
- **URLs:** 
  - `https://www.bpctech.com.au/product/c07pnpt-hp-z2-mini-g1a-ryzen-ai-max-pro-390-32gb-1tb-ssd-wlan-win-11-pro-3yr-nbd-onsite-wty.html`
  - `https://www.hp.com/au-en/shop/hp-z2-mini-g1a-workstation-desktop-pc-c07q2pt-2.html`

## Key Specs
- **SoC:** AMD Ryzen AI Max Pro 390
- **Unified Memory:** 32 GB
- **Storage:** 1 TB SSD
- **Form Factor:** Mini Workstation PC

## Conclusion
The HP Z2 Mini G1a is one of the highly anticipated Strix Halo mini workstations. With the memory floor relaxed to 32 GB, this base configuration is now officially an eligible Pathway C candidate. However, 32 GB of shared memory will be restrictive for larger LLMs (14B-30B+ parameters), so a custom-to-order (CTO) configuration with 64 GB+ memory remains strongly preferred if the budget allows.
`````

## File: NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/intake-038_minisforum-ai-x1-pro-deg2-rtx-5070-ti.md
`````markdown
<!-- TAGS: #MiniPC #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Mini PC / eGPU -->
---
id: minisforum-ai-x1-pro-deg2-rtx-5070-ti
category: mini pc
track: UNKNOWN
pathway: UNKNOWN
name: Minisforum AI X1 Pro + DEG2 + RTX 5070 Ti
gpu: RTX 5070 Ti
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $3633.19 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Minisforum AI X1 Pro + DEG2 + RTX 5070 Ti

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $3633.19 AUD
- **Retailer:** Amazon AU + Scorptec
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5070 Ti
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen AI 9 HX 370
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Better compact build; pay a modularity tax instead of buying a simpler tower

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/intake-039_minisforum-x1-lite-deg1-rtx-5070-ti.md
`````markdown
<!-- TAGS: #MiniPC #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Mini PC / eGPU -->
---
id: minisforum-x1-lite-deg1-rtx-5070-ti
category: mini pc
track: UNKNOWN
pathway: UNKNOWN
name: Minisforum X1 Lite + DEG1 + RTX 5070 Ti
gpu: RTX 5070 Ti
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $2851.98 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Minisforum X1 Lite + DEG1 + RTX 5070 Ti

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2851.98 AUD
- **Retailer:** Amazon AU + Scorptec
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5070 Ti
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 7 255
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
More cables; more setup friction; less elegance than a tower

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/06_Mini_PCs_and_eGPU/intake-071_gpd-win-5.md
`````markdown
<!-- TAGS: #MiniPC #AMD #VRAM-Unknown #New #TrackUnknown #NeedsVerification #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Mini PC / eGPU -->
---
id: gpd-win-5
category: mini pc
track: UNKNOWN
pathway: UNKNOWN
name: GPD WIN 5
gpu: Radeon 8060S
vram: UNKNOWN
unified_memory: UNKNOWN
price_aud: UNKNOWN
condition: New
au_stock: UNKNOWN
verification: Needs Verification
status: Active
score: UNKNOWN — pending manual review
---

# GPD WIN 5

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** UNKNOWN
- **Retailer:** GPD
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** Radeon 8060S
- **VRAM:** UNKNOWN
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen AI Max 395
- **RAM:** 128 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
7-inch handheld format; dual M.2 slots

## AI Capability Summary
UNKNOWN — to be completed after manual spec verification.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/08_Custom_Builds/10_custom-rtx-3090-24gb-desktop-refurbished-thinkpad-bundle.md
`````markdown
<!-- PRODUCT CARD START: Custom RTX 3090 24GB desktop + refurbished ThinkPad-class laptop bundle -->
<!-- TAGS: #CustomBuild #DesktopTower #NVIDIA #VRAM-24GB #Refurbished #Bundle #Expandable #PrimaryWorkstation #SecondaryLaptop #AgenticAI #ImageGeneration #Coding #Shortlist -->
<!-- PATH: Path 3 — Desktop tower + lightweight laptop -->
<!-- MERGED FROM: Card 10 (canonical), Card 19 (merged — earlier/lower-confidence version) -->

### [92 / 100] — Custom RTX 3090 24GB desktop + refurbished ThinkPad-class laptop bundle

- **Category**: Custom_Builds
- **Decision Lane**: Desktop-first AI workstation + secondary laptop
- **Condition**: Refurbished (tower) + Refurbished (laptop)
- **Price (AUD)**: ~$3,400–4,600 (bundle estimate)
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: RTX 3090 — 24GB VRAM
- **CPU**: UNKNOWN
- **RAM**: 64GB preferred (per Card 19 note); 24GB VRAM confirmed
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown (Card 10 — Canonical)
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 14/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 92 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 92 / 110 (83%)

#### Rubric Breakdown (Card 19 — Archived for reference)
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 10/25 ← lower confidence version
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 75 / 110 (68%) ← earlier estimate

#### AI Capability Summary
Capable of running 30B–35B parameter models at Q4/Q5 quantization with 24GB VRAM. Larger models require CPU/RAM offloading via PCIe. Suitable for autonomous agentic AI, image generation, and coding workloads.

#### ⭐ Mini Review

**Pros**
- 24GB VRAM — meets the local autonomy threshold for agentic LLM use
- Bundle framing provides both a primary AI workstation and mobile/secondary device in one purchase
- Strong value for money relative to new equivalents
- Refurbished desktops (Precision, Z-series) offer enterprise reliability

**Cons**
- PSU, motherboard, and case details are UNKNOWN — verify before buying
- Purchase safety score (3/10) reflects uncertainty in refurb source quality
- ThinkPad companion is a class recommendation, not a specific verified SKU

**Best for**
- Local LLM inference (Gemma 4 31B, Qwen 3.5 32B) at full context windows
- Local image generation
- Developer needing both a powerful AI tower at home and a portable coding device

#### ⚠️ Verification Required Before Purchase
- [ ] Confirm PSU wattage and connector compatibility
- [ ] Confirm motherboard PCIe slot layout
- [ ] Confirm case GPU clearance (320mm+)
- [ ] Identify specific ThinkPad model and price
<!-- PRODUCT CARD END: Custom RTX 3090 24GB desktop + refurbished ThinkPad-class laptop bundle -->
`````

## File: NotebookLM_Workspaces/08_Custom_Builds/13_refurb-3090-tower-thin-client.md
`````markdown
<!-- TAGS: #CustomBuild #DesktopTower #NVIDIA #VRAM-24GB #Refurbished #Bundle #Expandable #PrimaryWorkstation #SecondaryLaptop #AgenticAI #Shortlist -->
<!-- PRODUCT CARD START: Refurb 3090 Tower + Thin Client -->
### [80 / 100] — Refurb 3090 Tower + Thin Client

- **Category**: Windows Tower / Desktop
- **Condition**: UNKNOWN
- **Price (AUD)**: $Strong ("Claude-level" 32B capable)
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: 24GB
- **CPU**: UNKNOWN
- **RAM**: Unbeatable 24GB VRAM value, silent under desk, highly upgradable.
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 10/25
- **Value for Money**: 20/25
- **Design & Expandability**: 14/15
- **Purchase Safety & Risk**: 6/10
- **Raw Score**: 80 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 80 / 110 (72%)

#### AI Capability Summary
Capable of running models suitable for 24GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 24GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Refurb 3090 Tower + Thin Client -->
`````

## File: NotebookLM_Workspaces/08_Custom_Builds/intake-017_budget-build.md
`````markdown
<!-- TAGS: #CustomBuild #NVIDIA #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=DIY / Custom build -->
---
id: budget-build
category: diy build
track: UNKNOWN
pathway: UNKNOWN
name: Budget build
gpu: RTX 4060 Ti
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $899 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Budget build

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $899 AUD
- **Retailer:** UNKNOWN
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4060 Ti
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 5 5600X
- **RAM:** 32 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Best for beginners; students; Ollama on a budget

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/08_Custom_Builds/intake-018_mid-range-build.md
`````markdown
<!-- TAGS: #CustomBuild #NVIDIA #VRAM-8GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=DIY / Custom build -->
---
id: mid-range-build
category: diy build
track: UNKNOWN
pathway: UNKNOWN
name: Mid-range build
gpu: RTX 4070 Super
vram: 12 GB
unified_memory: UNKNOWN
price_aud: $1599 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Mid-range build

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $1599 AUD
- **Retailer:** UNKNOWN
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4070 Super
- **VRAM:** 12 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 7 7700X
- **RAM:** 64 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Best for developers; enthusiasts; 90% of local LLM use cases

## AI Capability Summary
Baseline — 8 GB VRAM sufficient for 7B Q4; larger models require significant offload.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/08_Custom_Builds/intake-019_pro-build.md
`````markdown
<!-- TAGS: #CustomBuild #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=DIY / Custom build -->
---
id: pro-build
category: diy build
track: UNKNOWN
pathway: UNKNOWN
name: Pro build
gpu: RTX 4090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $2899 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Pro build

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $2899 AUD
- **Retailer:** UNKNOWN
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 4090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** Ryzen 9 7900X
- **RAM:** 96 GB
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Best for researchers; heavy fine-tuning

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [x] Confirm CPU model
- [x] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/11_mike-pc-msi-rtx-3090-aero-24gb-gpu-build-route.md
`````markdown
<!-- TAGS: #Component #NVIDIA #VRAM-24GB #Used #CustomBuild #NeedsReview -->
<!-- PRODUCT CARD START: Mike PC MSI RTX 3090 AERO 24GB GPU build route -->
### [92 / 100] — Mike PC MSI RTX 3090 AERO 24GB GPU build route

- **Category**: Windows Tower / Desktop
- **Condition**: UNKNOWN
- **Price (AUD)**: $1,799 GPU; 12-month warranty noted in prior research
- **Vendor**: UNKNOWN
- **URL**: https://mikepc.com.au/products/msi-rtx-3090-aero-24gb-graphics-card

#### Hardware Profile
- **GPU**: 24GB
- **CPU**: UNKNOWN
- **RAM**: 24GB VRAM
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 14/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 92 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 92 / 110 (83%)

#### AI Capability Summary
Capable of running models suitable for 24GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 24GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Mike PC MSI RTX 3090 AERO 24GB GPU build route -->
`````

## File: NotebookLM_Workspaces/09_Individual_Components/14_msi-rtx-3090-aero-24gb-standalone-gpu.md
`````markdown
<!-- TAGS: #Component #NVIDIA #VRAM-24GB #Used #NeedsReview -->
<!-- PRODUCT CARD START: MSI RTX 3090 AERO 24GB standalone GPU -->
### [77 / 100] — MSI RTX 3090 AERO 24GB standalone GPU

- **Category**: Windows Tower / Desktop
- **Condition**: UNKNOWN
- **Price (AUD)**: $1799.0
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: 24GB
- **CPU**: UNKNOWN
- **RAM**: UNKNOWN
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 10/25
- **Value for Money**: 20/25
- **Design & Expandability**: 14/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 77 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 77 / 110 (70%)

#### AI Capability Summary
Capable of running models suitable for 24GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 24GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: MSI RTX 3090 AERO 24GB standalone GPU -->
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-021_nvidia-geforce-rtx-3090-24gb-2slot-turbo-blower.md
`````markdown
<!-- TAGS: #Component #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: nvidia-geforce-rtx-3090-24gb-2slot-turbo-blower
category: component
track: UNKNOWN
pathway: UNKNOWN
name: NVIDIA GeForce RTX 3090 24GB 2SLOT Turbo Blower
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $1739.49 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# NVIDIA GeForce RTX 3090 24GB 2SLOT Turbo Blower

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $1739.49 AUD
- **Retailer:** yzhan-695
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Blower type GPU

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-027_gigabyte-radeon-rx-9070-xt-gaming-oc-ice-16g.md
`````markdown
<!-- TAGS: #Component #AMD #VRAM-16GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: gigabyte-radeon-rx-9070-xt-gaming-oc-ice-16g
category: component
track: UNKNOWN
pathway: UNKNOWN
name: Gigabyte Radeon RX 9070 XT Gaming OC Ice 16G
gpu: RX 9070 XT
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $1235.40 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# Gigabyte Radeon RX 9070 XT Gaming OC Ice 16G

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $1235.40 AUD
- **Retailer:** Dick Smith
- **URL:** [https://www.dicksmith.com.au/da/buy/umart-online-gigabyte-radeon-rx-9070-xt-gaming-oc-ice-16g-graphics-card-gv-r907xgamingocice-16gd-90749/](https://www.dicksmith.com.au/da/buy/umart-online-gigabyte-radeon-rx-9070-xt-gaming-oc-ice-16g-graphics-card-gv-r907xgamingocice-16gd-90749/)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RX 9070 XT
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
GPU component

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-030_gigabyte-aorus-geforce-rtx-5090-master-ice-32g.md
`````markdown
<!-- TAGS: #Component #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: gigabyte-aorus-geforce-rtx-5090-master-ice-32g
category: component
track: UNKNOWN
pathway: UNKNOWN
name: GIGABYTE AORUS GeForce RTX 5090 Master Ice 32G
gpu: RTX 5090
vram: 32 GB
unified_memory: UNKNOWN
price_aud: $6499.00 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# GIGABYTE AORUS GeForce RTX 5090 Master Ice 32G

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $6499.00 AUD
- **Retailer:** Amazon AU
- **URL:** [https://www.amazon.com.au/dp/B0DVCB1NN1](https://www.amazon.com.au/dp/B0DVCB1NN1)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090
- **VRAM:** 32 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
GPU component

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-031_zotac-gaming-geforce-rtx-5090-solid-oc.md
`````markdown
<!-- TAGS: #Component #NVIDIA #VRAM-24GB #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: zotac-gaming-geforce-rtx-5090-solid-oc
category: component
track: UNKNOWN
pathway: UNKNOWN
name: ZOTAC Gaming GeForce RTX 5090 Solid OC
gpu: RTX 5090
vram: 32 GB
unified_memory: UNKNOWN
price_aud: $6569.95 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# ZOTAC Gaming GeForce RTX 5090 Solid OC

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $6569.95 AUD
- **Retailer:** Amazon AU
- **URL:** [https://www.amazon.com.au/dp/B0F1YG5STN](https://www.amazon.com.au/dp/B0F1YG5STN)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5090
- **VRAM:** 32 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
GPU component

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-057_asrock-radeon-rx-7900-xtx-phantom-gaming-24gb-oc.md
`````markdown
<!-- TAGS: #Component #AMD #VRAM-24GB #New #TrackUnknown #Verified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: asrock-radeon-rx-7900-xtx-phantom-gaming-24gb-oc
category: component
track: UNKNOWN
pathway: UNKNOWN
name: ASRock Radeon RX 7900 XTX Phantom Gaming 24GB OC
gpu: RX 7900 XTX
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $1229 AUD
condition: New
au_stock: UNKNOWN
verification: Verified
status: Active
score: UNKNOWN — pending manual review
---

# ASRock Radeon RX 7900 XTX Phantom Gaming 24GB OC

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $1229 AUD
- **Retailer:** Scorptec
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RX 7900 XTX
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Exceptionally aggressive price for a 24GB VRAM card backed by a full 3-year warranty

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-058_nvidia-rtx-pro-6000.md
`````markdown
<!-- TAGS: #Component #NVIDIA #VRAM-48GB+ #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: nvidia-rtx-pro-6000
category: component
track: UNKNOWN
pathway: UNKNOWN
name: NVIDIA RTX PRO 6000
gpu: RTX PRO 6000
vram: 96 GB
unified_memory: UNKNOWN
price_aud: $15999.00 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Out of Stock
score: UNKNOWN — pending manual review
---

# NVIDIA RTX PRO 6000

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Out of Stock
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $15999.00 AUD
- **Retailer:** Mwave
- **URL:** [https://www.mwave.com.au/product/nvidia-rtx-pro-6000-blackwell-96gb-professional-video-card-workstation-edition-ac86472](https://www.mwave.com.au/product/nvidia-rtx-pro-6000-blackwell-96gb-professional-video-card-workstation-edition-ac86472)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX PRO 6000
- **VRAM:** 96 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Workstation Edition; GDDR7 ECC

## AI Capability Summary
Exceptional — 48 GB+ VRAM supports 70B+ models fully in VRAM at Q4.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-060_nvidia-rtx-6000-96gb-gddr7-professional-video-card.md
`````markdown
<!-- TAGS: #Component #NVIDIA #VRAM-48GB+ #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: nvidia-rtx-6000-96gb-gddr7-professional-video-card
category: component
track: UNKNOWN
pathway: UNKNOWN
name: NVIDIA RTX 6000 96GB GDDR7 Professional Video Card
gpu: RTX 6000
vram: 96 GB
unified_memory: UNKNOWN
price_aud: $15499.00 AUD
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Out of Stock
score: UNKNOWN — pending manual review
---

# NVIDIA RTX 6000 96GB GDDR7 Professional Video Card

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Out of Stock
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $15499.00 AUD
- **Retailer:** Mwave
- **URL:** [https://www.mwave.com.au/product/nvidia-rtx-6000-96gb-gddr7-professional-video-card-blackwell-server-edition-ac84368](https://www.mwave.com.au/product/nvidia-rtx-6000-96gb-gddr7-professional-video-card-blackwell-server-edition-ac84368)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 6000
- **VRAM:** 96 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Blackwell Server Edition

## AI Capability Summary
Exceptional — 48 GB+ VRAM supports 70B+ models fully in VRAM at Q4.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-061_amd-radeon-pro-w7900-48gb-ecc-gddr6.md
`````markdown
<!-- TAGS: #Component #AMD #VRAM-48GB+ #New #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: amd-radeon-pro-w7900-48gb-ecc-gddr6
category: component
track: UNKNOWN
pathway: UNKNOWN
name: AMD Radeon Pro W7900 48GB ECC GDDR6
gpu: Radeon Pro W7900
vram: 48 GB
unified_memory: UNKNOWN
price_aud: UNKNOWN
condition: New
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# AMD Radeon Pro W7900 48GB ECC GDDR6

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** UNKNOWN
- **Retailer:** PBTech.com
- **URL:** [https://www.pbtech.com/au/product/VGAAMD017900/AMD-Radeon-Pro-W7900-48GB-ECC-GDDR6-Workstation-Gr](https://www.pbtech.com/au/product/VGAAMD017900/AMD-Radeon-Pro-W7900-48GB-ECC-GDDR6-Workstation-Gr)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** Radeon Pro W7900
- **VRAM:** 48 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Workstation GPU

## AI Capability Summary
Exceptional — 48 GB+ VRAM supports 70B+ models fully in VRAM at Q4.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [ ] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-067_evga-ftw3-ultra-rtx-3090.md
`````markdown
<!-- TAGS: #Component #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #NeedsVerification #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: evga-ftw3-ultra-rtx-3090
category: component
track: UNKNOWN
pathway: UNKNOWN
name: EVGA FTW3 Ultra RTX 3090
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $1318 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Needs Verification
status: Active
score: UNKNOWN — pending manual review
---

# EVGA FTW3 Ultra RTX 3090

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $1318 AUD
- **Retailer:** Outworld Systems
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Grade A condition; 1-yr eBay warranty; Converted from USD

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-068_intel-arc-pro-b70.md
`````markdown
<!-- TAGS: #Component #Intel #VRAM-24GB #New #TrackUnknown #NeedsVerification #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: intel-arc-pro-b70
category: component
track: UNKNOWN
pathway: UNKNOWN
name: Intel Arc Pro B70
gpu: Arc Pro B70
vram: 32 GB
unified_memory: UNKNOWN
price_aud: $1423 AUD
condition: New
au_stock: UNKNOWN
verification: Needs Verification
status: Active
score: UNKNOWN — pending manual review
---

# Intel Arc Pro B70

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $1423 AUD
- **Retailer:** UNKNOWN
- **URL:** UNKNOWN
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** Arc Pro B70
- **VRAM:** 32 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Budget option with 32GB VRAM; Converted from USD

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-069_nvidia-rtx-5000-ada-32gb.md
`````markdown
<!-- TAGS: #Component #NVIDIA #VRAM-24GB #New #TrackUnknown #Verified #AUStock-Confirmed -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: nvidia-rtx-5000-ada-32gb
category: component
track: UNKNOWN
pathway: UNKNOWN
name: NVIDIA RTX 5000 Ada 32GB
gpu: RTX 5000 Ada
vram: 32 GB
unified_memory: UNKNOWN
price_aud: $6368 AUD
condition: New
au_stock: Yes
verification: Verified
status: Active
score: UNKNOWN — pending manual review
---

# NVIDIA RTX 5000 Ada 32GB

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** Yes
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $6368 AUD
- **Retailer:** ITC Solutions
- **URL:** [https://itc-solutions.com.au/products/nvidia-rtx-5000-ada-32gb?pr_prod_strat=e5_desc&pr_rec_id=b5419423c&pr_rec_pid=7588252614750&pr_ref_pid=7588429758558&pr_seq=uniform](https://itc-solutions.com.au/products/nvidia-rtx-5000-ada-32gb?pr_prod_strat=e5_desc&pr_rec_id=b5419423c&pr_rec_pid=7588252614750&pr_ref_pid=7588429758558&pr_seq=uniform)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 5000 Ada
- **VRAM:** 32 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Reduced from $8375

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [x] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-070_nvidia-rtx-2000-ada-16gb.md
`````markdown
<!-- TAGS: #Component #NVIDIA #VRAM-16GB #New #TrackUnknown #Verified #AUStock-Confirmed -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: nvidia-rtx-2000-ada-16gb
category: component
track: UNKNOWN
pathway: UNKNOWN
name: NVIDIA RTX 2000 Ada 16GB
gpu: RTX 2000 Ada
vram: 16 GB
unified_memory: UNKNOWN
price_aud: $1233 AUD
condition: New
au_stock: Yes
verification: Verified
status: Active
score: UNKNOWN — pending manual review
---

# NVIDIA RTX 2000 Ada 16GB

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** Yes
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $1233 AUD
- **Retailer:** ITC Solutions
- **URL:** [https://itc-solutions.com.au/products/nvidia-rtx-2000-ada-16gb-1?pr_prod_strat=e5_desc&pr_rec_id=b5419423c&pr_rec_pid=7588430282846&pr_ref_pid=7588429758558&pr_seq=uniform](https://itc-solutions.com.au/products/nvidia-rtx-2000-ada-16gb-1?pr_prod_strat=e5_desc&pr_rec_id=b5419423c&pr_rec_pid=7588430282846&pr_ref_pid=7588429758558&pr_seq=uniform)
- **Condition:** New
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 2000 Ada
- **VRAM:** 16 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
Reduced from $1359

## AI Capability Summary
Solid — 16 GB VRAM handles 13B–20B Q4 natively; 34B requires offloading.

## Verification Checklist
- [x] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/Desktop_Gaming_Refurbished/09_alienware-aurora-r12-rtx-3090-refurbished.md
`````markdown
<!-- TAGS: #DesktopTower #NVIDIA #VRAM-24GB #Refurbished #SingleGPU #PrimaryWorkstation #AgenticAI #ImageGeneration #Shortlist -->
<!-- PRODUCT CARD START: Alienware Aurora R12 RTX 3090 refurbished -->
### [95 / 100] — Alienware Aurora R12 RTX 3090 refurbished

- **Category**: Windows Tower / Desktop
- **Condition**: UNKNOWN
- **Price (AUD)**: $3090
- **Vendor**: UNKNOWN
- **URL**: https://www.dicksmith.com.au/

#### Hardware Profile
- **GPU**: 24GB
- **CPU**: UNKNOWN
- **RAM**: 32GB
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 25/25
- **Value for Money**: 20/25
- **Design & Expandability**: 14/15
- **Purchase Safety & Risk**: 6/10
- **Raw Score**: 95 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 95 / 110 (86%)

#### AI Capability Summary
Capable of running models suitable for 24GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 24GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Alienware Aurora R12 RTX 3090 refurbished -->
`````

## File: NotebookLM_Workspaces/Desktop_Gaming_Refurbished/10_alienware-aurora-r11-rtx-3090-refurbished.md
`````markdown
<!-- TAGS: #Desktop #Alienware #NVIDIA #VRAM-24GB #Refurbished #Track1.5-Candidate -->
---
id: alienware-aurora-r11-rtx-3090-refurbished
category: desktop_gaming_refurbished
name: Alienware Aurora R11 Gaming PC
gpu: NVIDIA RTX 3090 (24 GB)
vram: 24 GB
price_aud: 2300
score: 8.5 (Exceptional Value)
---

# Alienware Aurora R11 Gaming PC — TechnologyLocker

> ℹ️ **SPEC NOTE:** This is a refurbished Track 1.5 candidate equipped with an **RTX 3090 (24 GB VRAM)**. It must pass the "Desktop ≤ 85% cost of comparable laptop" price threshold rule to be considered GOOD ENOUGH.

## Track 1.5 Status
- **Chassis:** Alienware Aurora R11 (Manufactured ~2020) ✅ (Meets ≥ 2020 age limit)
- **Target GPU:** RTX 3090 24 GB ✅ (Meets 8 GB minimum)
- **GOOD ENOUGH check:** ✅ **PASSED** — At $2,300, it is roughly 50% of the $4,500 laptop budget, making it an incredibly cost-effective high-VRAM solution.

## Overview
- **VRAM Tier:** Priority 1 — 24 GB
- **Price (AUD):** $2,300.00
- **Vendor (AU):** TechnologyLocker
- **URL:** `https://technologylocker.com.au/products/alienware-aurora-r11-gaming-pc-i9-10900kf-32gb-ram-2tb-hdd-rtx-3090-24gb`

## Key Specs
- **GPU:** NVIDIA GeForce RTX 3090, 24 GB GDDR6X
- **CPU:** Intel Core i9-10900KF
- **RAM:** 32 GB
- **Storage:** 2 TB HDD ⚠️ (Needs verification: does it have a boot SSD? If not, an SSD upgrade is mandatory for LLM/OS usability).
- **Condition:** Refurbished

## Conclusion
An exceptional Track 1.5 candidate due to the 24 GB RTX 3090 and the highly aggressive $2,300 price point. The primary flags are the 10th Gen Intel platform and the listed "2TB HDD", which **must** be supplemented with a fast NVMe SSD for tensor loading.
`````

## File: NotebookLM_Workspaces/Gaming_Laptops_AMD_Discrete/hp_omen_max.md
`````markdown
---
id: hp-omen-max-rtx-5090
category: laptop
architecture: discrete_gpu_amd
track_eligibility: track_1_nvidia_path
name: HP OMEN Max (Ryzen AI 9 HX 375 + RTX 5090)
gpu: NVIDIA RTX 5090
vram: 24 GB
---
# HP OMEN Max
Evaluate under Track 1 NVIDIA Path rules.
`````

## File: NotebookLM_Workspaces/workspace_redesign_proposal.md
`````markdown
# NotebookLM Workspace Redesign Proposal

## Guiding Principles
- **Folders** answer: "what kind of things are stored here?"
- **Tags** answer: "what properties does this thing have?"
- Avoid vague terms like "Master" or "Value" in folder names.
- Treat "Expandable", "SingleGPU", "Refurbished", etc. as tags, not folder names.

---

## Part 1: Revised Lane Names

| # | New Name | Old Name | Rationale |
|---|---|---|---|
| 01 | `Decision_System` | `01_Master_Hardware_Strategy_Ledger` | "Master" is vague. This folder *is* the decision framework — policies, scoring rubrics, VRAM spec, prompts, tagging rules, manifest. |
| 02 | `Desktop_Towers_Refurbished` | `02_Expandable_Workstations` | "Refurbished" is the acquisition reality for 24GB options. "Expandable" is now a tag. |
| 03 | `Desktop_Towers_New` | `03_Single_GPU_Desktop_Value` | Separates new-retail desktops from refurb. "Single GPU" and "Value" become tags. |
| 04 | `Laptops` | `04_Portable_Value_Laptops` | Plain and literal. "Portable" and "Value" become tags. |
| 05 | `Apple_Silicon` | `05_Apple_Unified_Memory` | "Unified Memory" is a spec trait → becomes a tag (`#UnifiedMemory`). |
| 06 | `Mini_PC_and_eGPU` | `06_Mini_PC_eGPU` | Keeps the literal form-factor description. |
| 07 | `Custom_Builds` | *(new)* | Home for DIY/custom configurations and component pairing proposals. |
| 08 | `Components` | *(new)* | Home for individual GPU, CPU, PSU, case, RAM, SSD cards. |
| 09 | `Research_and_Sources` | `07_Secondary_Laptop_Ergonomics` | Holds raw research, market analysis, source material. "Ergonomics" becomes a tag. |

---

## Part 2: Tagging Taxonomy

### Family A — VRAM / Capacity
| Tag | Meaning |
|---|---|
| `#VRAM-12GB` | 12GB GPU VRAM |
| `#VRAM-16GB` | 16GB GPU VRAM |
| `#VRAM-24GB` | 24GB GPU VRAM |
| `#VRAM-36GB` | 36GB Apple unified memory |
| `#VRAM-48GB` | 48GB GPU VRAM or unified memory |
| `#VRAM-64GB` | 64GB unified memory |
| `#UnifiedMemory` | Apple-style shared CPU/GPU pool (not discrete VRAM) |

### Family B — Acquisition / Condition
| Tag | Meaning |
|---|---|
| `#New` | Bought from retailer, sealed |
| `#Refurbished` | Professionally refurbished, carries warranty |
| `#Used` | Secondhand, private sale (eBay, Gumtree) |
| `#OpenBox` | Retail return, minor use |
| `#EducationConfig` | Education pricing / configuration |

### Family C — Form Factor
| Tag | Meaning |
|---|---|
| `#DesktopTower` | Full/mid-tower desktop |
| `#Workstation` | Enterprise-class tower (Precision, Z-series) |
| `#Laptop` | Any laptop |
| `#MiniPC` | Small-form-factor mini PC |
| `#CustomBuild` | DIY / assembled from components |
| `#Component` | Individual part (GPU, CPU, PSU, etc.) |
| `#Bundle` | System + accessory sold together |

### Family D — Architecture / Topology
| Tag | Meaning |
|---|---|
| `#NVIDIA` | NVIDIA GPU |
| `#AppleSilicon` | Apple M-series chip |
| `#AMD` | AMD GPU or CPU |
| `#SingleGPU` | One discrete GPU |
| `#DualGPU` | Two discrete GPUs installed or planned |
| `#eGPU` | External GPU via Thunderbolt or OCuLink |
| `#OCuLink` | PCIe-over-cable eGPU connection |

### Family E — Upgradeability
| Tag | Meaning |
|---|---|
| `#Expandable` | Platform can grow: second GPU slot, PSU room, RAM ceiling |
| `#NonUpgradeable` | Soldered, proprietary, or no headroom |
| `#PCIe-x16x16` | Two full x16 slots (dual GPU capable) |
| `#PCIe-x16x8` | One x16, one x8 (dual GPU with caveats) |
| `#PSU-850W` | 850W PSU installed |
| `#PSU-1000W+` | 1000W+ PSU installed |

### Family F — Role / Use Case
| Tag | Meaning |
|---|---|
| `#PrimaryWorkstation` | Intended as the main AI workhorse |
| `#SecondaryLaptop` | Companion device for mobility |
| `#AgenticAI` | Suitable for autonomous/long-context AI runs |
| `#ImageGeneration` | Suitable for local image generation |
| `#Coding` | Coding-focused workload fit |
| `#Ergonomics` | Ergonomic considerations (screen, keyboard, posture) |
| `#Travel` | Optimised for travel/portability |

### Family G — Review Status
| Tag | Meaning |
|---|---|
| `#Shortlist` | Candidate for final purchase decision |
| `#Verified` | All specs confirmed from source |
| `#NeedsReview` | Specs incomplete or unverified |
| `#Rejected` | Explicitly ruled out with reason |
| `#ConditionalBuy` | Good candidate pending one specific verification |
| `#StrongBuy` | Recommended per scoring rubric |

---

## Part 3: Per-Lane Summary

| Lane | What Lives Here | Example Tag Combo |
|---|---|---|
| `Decision_System` | Policies, rubrics, VRAM spec, prompts, tagging rules, manifest | — |
| `Desktop_Towers_Refurbished` | Refurb workstation towers (Dell Precision, HP Z-series, Alienware R12) | `#Workstation #Refurbished #NVIDIA #VRAM-24GB #Expandable #Shortlist` |
| `Desktop_Towers_New` | New retail towers (Scorptec, PLE, Acer Predator) | `#DesktopTower #New #NVIDIA #VRAM-16GB #SingleGPU #PrimaryWorkstation` |
| `Laptops` | All laptop cards, new and open-box | `#Laptop #New #NVIDIA #VRAM-16GB #AgenticAI #Coding #NonUpgradeable` |
| `Apple_Silicon` | All Apple Mac Studio and MacBook Pro cards | `#AppleSilicon #UnifiedMemory #VRAM-64GB #New #PrimaryWorkstation #AgenticAI` |
| `Mini_PC_and_eGPU` | Minisforum MS-01 + OCuLink combos | `#MiniPC #OCuLink #NVIDIA #VRAM-24GB #Expandable #ConditionalBuy` |
| `Custom_Builds` | DIY build proposals, component pairing strategies | `#CustomBuild #Refurbished #NVIDIA #VRAM-24GB #Expandable #Shortlist` |
| `Components` | Individual GPU, PSU, case, CPU cards | `#Component #NVIDIA #VRAM-24GB #Used #NeedsReview` |
| `Research_and_Sources` | VRAM analysis, market research, scoring raw data, source notes | — |

---

## Part 4: Migration Steps

### Safe to execute automatically (empty folders):
1. Rename `01_Master_Hardware_Strategy_Ledger` → `Decision_System`
2. Rename `02_Expandable_Workstations` → `Desktop_Towers_Refurbished`
3. Rename `03_Single_GPU_Desktop_Value` → `Desktop_Towers_New`
4. Rename `04_Portable_Value_Laptops` → `Laptops`
5. Rename `05_Apple_Unified_Memory` → `Apple_Silicon`
6. Rename `06_Mini_PC_eGPU` → `Mini_PC_and_eGPU`
7. Rename `07_Secondary_Laptop_Ergonomics` → `Research_and_Sources`
8. Create new folders: `Custom_Builds`, `Components`

### Do NOT move automatically — needs your review:
| Card | Issue |
|---|---|
| 10, 11, 13, 18, 19 | Straddle `Desktop_Towers_Refurbished` and `Custom_Builds` — you decide primary home |
| 15 (Normal laptop + remote GPU rental) | Strategy option, not a product — may belong in `Research_and_Sources` |
| 17 (System_RAM_GB_or_Unified_Memory_GB) | Reference document, not a product card — likely `Research_and_Sources` |
| 20 (Used enterprise workstation strategy) | Strategy doc, not a product — likely `Research_and_Sources` |
`````

## File: NotebookLM_Workspaces/09_Individual_Components/intake-020_asus-rog-strix-geforce-rtx-3090-oc-24gb-gddr6x.md
`````markdown
<!-- TAGS: #Component #NVIDIA #VRAM-24GB #Refurbished #TrackUnknown #Unverified #AUStock-Unknown -->
<!-- INTAKE: batch=2026-05-05_notebooklm_batch1_processed date=2026-05-05 route=Standalone component -->
---
id: asus-rog-strix-geforce-rtx-3090-oc-24gb-gddr6x
category: component
track: UNKNOWN
pathway: UNKNOWN
name: ASUS ROG Strix GeForce RTX 3090 OC 24GB GDDR6X
gpu: RTX 3090
vram: 24 GB
unified_memory: UNKNOWN
price_aud: $1591.98 AUD
condition: Refurbished
au_stock: UNKNOWN
verification: Unverified
status: Active
score: UNKNOWN — pending manual review
---

# ASUS ROG Strix GeForce RTX 3090 OC 24GB GDDR6X

> ⚠️ **INTAKE CARD — sourced from AI batch export. All fields require manual verification.**
> Do not treat prices, availability, or specs as confirmed until cross-checked with the retailer.

## Track Status
- **Track:** UNKNOWN
- **Pathway:** UNKNOWN
- **Status:** Active
- **AU Stock Confirmed:** UNKNOWN
- **GOOD ENOUGH check:** PENDING — confirm AU stock, price, and key specs below

## Overview
- **Price (AUD):** $1591.98 AUD
- **Retailer:** grayfox319
- **URL:** UNKNOWN
- **Condition:** Refurbished
- **Source batch:** 2026-05-05_notebooklm_batch1_processed (ingested 2026-05-05)

## Key Specs
- **GPU:** RTX 3090
- **VRAM:** 24 GB
- **Unified Memory:** UNKNOWN
- **CPU:** UNKNOWN
- **RAM:** UNKNOWN
- **Storage:** UNKNOWN
- **PSU / Charger:** UNKNOWN
- **Warranty (AU):** UNKNOWN

## Source Notes
eBay auction item

## AI Capability Summary
Strong — 24 GB VRAM handles 30B–34B Q4 models natively.

## Verification Checklist
- [ ] Confirm AU stock from named retailer with URL
- [x] Confirm price in AUD
- [x] Confirm GPU model and VRAM
- [ ] Confirm CPU model
- [ ] Confirm RAM installed and max supported
- [ ] Confirm storage installed and free M.2 slots
- [ ] Confirm PSU / charger wattage
- [ ] Confirm warranty term and type (AU)
- [ ] Check thermal reputation (reviews)
- [ ] Confirm AGENTS.md GOOD ENOUGH gate cleared
`````

## File: NotebookLM_Workspaces/Research_and_Sources/15_normal-laptop-remote-gpu-rental.md
`````markdown
<!-- TAGS: #Strategy #Cloud_First #Remote_GPU #Laptop #NeedsReview -->
<!-- PRODUCT CARD START: Normal laptop + remote GPU rental -->
### [77 / 100] — Normal laptop + remote GPU rental

- **Category**: Windows Laptop / Desktop Replacement
- **Condition**: UNKNOWN
- **Price (AUD)**: $UNKNOWN
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: 24GB
- **CPU**: UNKNOWN
- **RAM**: Local 32GB preferred
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 10/25
- **Value for Money**: 20/25
- **Design & Expandability**: 14/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 77 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 77 / 110 (70%)

#### AI Capability Summary
Capable of running models suitable for 24GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 24GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Normal laptop + remote GPU rental -->
`````

## File: NotebookLM_Workspaces/Research_and_Sources/20_used-enterprise-workstation-or-data-center-gpu-path.md
`````markdown
<!-- TAGS: #Strategy #Workstation #NVIDIA #VRAM-24GB #Used #NeedsReview -->
<!-- PRODUCT CARD START: Used enterprise workstation or data-center GPU path -->
### [75 / 100] — Used enterprise workstation or data-center GPU path

- **Category**: Other / Strategy
- **Condition**: UNKNOWN
- **Price (AUD)**: $UNKNOWN
- **Vendor**: UNKNOWN
- **URL**: UNKNOWN

#### Hardware Profile
- **GPU**: 24GB
- **CPU**: UNKNOWN
- **RAM**: 64GB-128GB+
- **Storage**: UNKNOWN
- **PSU**: UNKNOWN
- **Thermals / Cooling**: UNKNOWN
- **Warranty**: UNKNOWN

#### Rubric Breakdown
- **VRAM & GPU Generation**: 30/35
- **Ecosystem & Software**: 10/25
- **Value for Money**: 20/25
- **Design & Expandability**: 12/15
- **Purchase Safety & Risk**: 3/10
- **Raw Score**: 75 / 110
- **Self-Build Modifier**: N/A
- **Adjusted Score**: 75 / 110 (68%)

#### AI Capability Summary
Capable of running models suitable for 24GB VRAM. Larger models require offloading.

#### ⭐ Mini Review

**Pros**
- VRAM capacity: 24GB
- Ecosystem support

**Cons**
- Cost and risk factors
- Limited expandability

**Best for**
- Local AI workloads prioritizing VRAM size.
<!-- PRODUCT CARD END: Used enterprise workstation or data-center GPU path -->
`````

## Schema Drift Report
Run: grep -rh '^## ' NotebookLM_Workspaces/**/*.md | sort | uniq -c | sort -rn
   2 |vram_gb** | 24.0 GB |
   2 |price_aud** | $4,499.00 AUD |
   2 |Workload Fit** | `VRAM Adequacy` | 10: 48GB+, 8: 24GB, 5: 16GB, 0: <16GB |
   2 |Whitening method** | Follows RRD paper §4: standardise columns → estimate Σ → regularise Σ_λ = Σ + λI → compute Σ_λ^{-1/2} via eigen-decomp → weights ∝ row sums of Σ_λ^{-1/2}. This down-weights clusters of correlated metrics so they don't dominate collectively. |
   2 |Verification_Confidence** | 2 (Unverified) |
   2 |Value_Score** | 9 |
   2 |Value/Reliability** | `Price per GB VRAM` | 10: Excellent value (<$150/GB), 5: Average, 0: Very expensive |
   2 |VRAM** | 12GB (Entry), 16GB (Developer) | 24GB+ (Standard) |
   2 |Upgrade Path** | `Second PCIe x16 Slot Usability` | 10: True x16/x8 clear, 5: Shared x4/partially blocked, 0: None/blocked |
   2 |Track / Pathway** | Track 1, Pathway 1A |
   2 |Total CapEx (Upfront)** |~$2,200** |~$4,200** |~$7,500** |
   2 |Thermals/Noise** | `Intake Airflow Volume` | 10: High static pressure/mesh, 5: Standard airflow, 0: Solid glass/blocked |
   2 |TOTAL blocking** |~59 red-priority fields** |
   2 |System RAM** | 32GB | 64GB - 128GB (for weights offloading) |
   2 |Sustained_TGP_Rating** | UNKNOWN (0) |
   2 |Qwen 3.5 (32B Coder)** | 24GB | Best-in-class coding for 24GB VRAM. |
   2 |Project Research** | Large document ingestion (PDFs, codebases), cross-referencing. | Low | 64K - 256K+ tokens |
   2 |Price_to_Perf** | 9 |
   2 |Portability_Score** | UNKNOWN (0) |
   2 |PSU** | 850W (Single GPU) | 1000W - 1300W (Dual GPU growth) |
   2 |PCIe** | One x16 Slot | Dual x16 (x8/x8 electrical) |
   2 |NPU/TTFT** | < 500ms (30B models) | < 250ms (Reasoning/Thinking models) |
   2 |Model / Identifier** | Dell Alienware m18 R2 / Area-51 (intake-011) |
   2 |Misalignment filter** | Pairwise NeverBuy-vs-Preferred per criterion. Only flags SUSPECT (> 50% of pairs go the wrong way). Does not auto-invert — you decide. |
   2 |Manual overrides** | Appliedbefore** whitening distributes the remainder. VRAM ≥ 18%, `Second_x16_Usability` ≥ 8%, `PSU_Wattage_Ceiling` ≥ 5%. These represent your non-negotiable buying priorities. |
   2 |Llama 4 Scout** | 24GB (MoE) | Top local LLM in early 2026 using INT4. |
   2 |Gemma 4 (E2B/E4B)** | 8GB - 12GB | Optimized for edge/mobile via PLE architecture. |
   2 |Gemma 4 (31B Dense)** | 24GB+ | Claude surrogate; 256K context window support. |
   2 |Gemma 4 (26B A4B MoE)** | 16GB - 24GB | High "intelligence-per-GB" via Mixture-of-Experts. |
   2 |GPU** | ~$1,100 | ~$2,400 | ~$5,000 |
   2 |Final Score** | 50.9 / 100 |
   2 |Expandability gate** | If a machine's avg(`Second_x16_Usability`, `Chassis_2nd_GPU`, `PSU_Wattage_Ceiling`) < 6.0, its `Price_per_GB_VRAM`, `Warranty_Coverage`, and `Enterprise_Pedigree` scores arezeroed before scoring**. A great deal on a non-expandable machine can't rescue its rank. |
   2 |Est. Power (Monthly)** | ~$15 | ~$25 | ~$40 |
   2 |Cooling (Mod/Active Backplate)** | ~$200 | ~$0 (Stock) | ~$0 (Stock) |
   2 |Contribution math** | Points shown in the diff are `raw_score × final_weight × 10` so they sum to the displayed New_Score. |
   2 |Condition_Risk** | 6 (Refurbished) |
   2 |Component Synergy** | `PSU Headroom for Current GPU` | 10: 30%+ headroom over spikes, 5: adequate, 0: unsafe/unknown |
   2 |Compatibility** | `PCIe Slot Layout Clarity` | 10: Full motherboard diagram/specs, 5: Text description only, 0: Unknown |
   2 |Chat / Assistant** | High responsiveness, single-turn or short multi-turn interaction. | Low (1-2 users) | 4K - 16K tokens |
   2 |Break-even vs $100/mo Cloud** |~15 Months** |~29 Months** |~52 Months** |
   2 |Base System (CPU/MB/RAM/PSU)** | ~$1,100 | ~$1,800 | ~$2,500 |
   2 |Bandwidth** | 936 GB/s (3090) / 1008 GB/s (4090) | >1500 GB/s (5090) / Target >1000 GB/s |
   2 |Autonomous Agent** | Multi-step reasoning, tool use (terminal, browser), self-correction. | Moderate (1 agent) | 32K - 128K tokens |
   2 |Agentic Coding** | Codebase-wide analysis, autonomous debugging, multi-file edits. | Moderate | 64K - 128K tokens |
