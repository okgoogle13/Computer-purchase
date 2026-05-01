# NotebookLM Operational Manifest

## Project Goal & Rationale

**The Overarching Goal**: The user requires a new computer. 
**The Project Purpose**: To collate and synthesize extensive hardware research into a coherent, cohesive, comprehensive analysis and a structured, logical decision-making framework.
**The Rationale**: This thorough analysis stage is necessary to mitigate post-purchase cognitive dissonance. It empowers the user to confidently shortlist the best-value product propositions for their needs and lock in a purchase soon.

---

This document details the structure and source mapping for the 7 NotebookLM lanes that support the above goal.

## 1. Notebook List & Source Mapping

| Notebook Name | Directory Path | Source Files to Upload |
| :--- | :--- | :--- |
| **01 Master Strategy** | `01_Master_Hardware_Strategy_Ledger/` | `vram_architecture_spec_v1.md`, `Policy_Pack/`, `tagging_taxonomy.md`, `prompts.md`, `notebook_manifest.md` |
| **02 Expandable Workstations** | `02_Expandable_Workstations/` | Product cards tagged `#Expandable`, motherboard/PSU spec sheets. |
| **03 Single-GPU Value** | `03_Single_GPU_Desktop_Value/` | Product cards tagged `#SingleGPUValue`, standard desktop reviews. |
| **04 Portable Value** | `04_Portable_Value_Laptops/` | Product cards tagged `#PortableValue`, thermal/battery reports. |
| **05 Apple Route** | `05_Apple_Unified_Memory/` | Product cards tagged `#AppleSilicon`, unified memory deep dives. |
| **06 Mini PC + eGPU** | `06_Mini_PC_eGPU/` | Product cards tagged `#MiniPC`, OCuLink/Thunderbolt benchmarks. |
| **07 Secondary / Ergo** | `07_Secondary_Laptop_Ergonomics/` | Product cards tagged `#Ergonomics`, keyboard/display specs. |

## 2. Tagging System (`tagging_taxonomy.md`)

*   **Tier Tags**: `#VRAM-12GB`, `#VRAM-16GB`, `#VRAM-24GB`, `#VRAM-48GB+`
*   **Category Tags**: `#Expandable`, `#SingleGPUValue`, `#PortableValue`, `#AppleSilicon`, `#MiniPC`, `#Ergonomics`
*   **Status Tags**: `#Verified`, `#Incomplete`, `#Rejected`
*   **Condition Tags**: `#New`, `#Refurbished`, `#Used`

## 3. Comparison Prompts (`prompts.md`)

### Lane-Specific Comparison Prompt
> "Evaluate these product cards for [LANE_NAME]. Rank them primarily based on the scoring criteria in 'policy_expandable_workstation_scoring.md'. Focus on [PRIMARY_METRIC, e.g., PCIe lanes/VRAM density/Portability]. Highlight any TODO markers or missing technical data (PSU/Clearance) that needs verification."

### Master-Notebook Comparison Prompt
> "Compare the 'Strong Buy' winners from each category lane against the 'vram_architecture_spec_v1.md'. Which system offers the highest ROI for a three-year local AI growth trajectory? Contrast the Expandable Workstation route against the Apple Unified Memory route for long-term agentic autonomy."

---
**Sources**: `implementation_plan.md`, `vram_agent_spec.md`.
