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
