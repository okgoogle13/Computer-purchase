# Project Restructuring and NotebookLM Initialization Plan

This plan uses ODD (Observation, Deduction, Decision) principles to systematically clean up the project directory, establish the requested NotebookLM structure for hardware evaluation, and finally synchronize the repository to GitHub.

## Observation & Strategy
**Observations**: The current directory has a mix of legacy notes, raw sources, Python scripts, zip archives, and an initial `notebooklm_hardware_project` folder. A new scoring policy pack is available in Downloads. The primary goal is finding an expandable AI workstation (24GB VRAM preferred) while maintaining other value-exception lanes.
**Deductions**: We need a clean staging area to separate "raw/legacy data" from "NotebookLM ready data". The 7 requested decision lanes must become the structural backbone of the new NotebookLM directories. The policy pack needs to be extracted and integrated.
**Decisions**:
1. Create an `archive_raw_data/` folder to sweep up all current loose files and old folders.
2. Build a fresh `NotebookLM_Workspaces/` directory containing the 7 specific lanes.
3. Extract the `expandable_workstation_scoring_policy_pack.zip` into the Master Strategy folder.
4. Generate the necessary prompts, tagging system, and source mappings.
5. Execute Git Initialization and push to GitHub.

---

## Phase 1: Folder Cleanup & Structure Prep

### [NEW] Clean Directory Structure
Create a pristine working environment by moving legacy data and establishing the 7 requested NotebookLM lanes.

1. **Create Archival Area**:
   Move `archive_legacy`, `Computer Purchase_notes (1)`, `Computer Purchase_sources`, `evaluated_products`, `product_cards`, `research`, and `.zip` files into a new `_Archive_Legacy_Data/` directory.

2. **Initialize NotebookLM Workspaces**:
   Create the exact directory structure reflecting the 7 decision lanes:
   - `NotebookLM_Workspaces/01_Master_Hardware_Strategy_Ledger/`
   - `NotebookLM_Workspaces/02_Expandable_Workstations/`
   - `NotebookLM_Workspaces/03_Single_GPU_Desktop_Value/`
   - `NotebookLM_Workspaces/04_Portable_Value_04_Laptops_Mainline/`
   - `NotebookLM_Workspaces/05_Apple_Unified_Memory/`
   - `NotebookLM_Workspaces/06_Mini_PC_eGPU/`
   - `NotebookLM_Workspaces/07_Secondary_Laptop_Ergonomics/`

3. **Integrate Policy Pack**:
   Extract `/Users/okgoogle13/Downloads/expandable_workstation_scoring_policy_pack.zip` directly into `NotebookLM_Workspaces/01_Master_Hardware_Strategy_Ledger/Policy_Pack/`.

---

## Phase 2: NotebookLM Optimization & Prompts

*Note: These files will be generated during the execution phase.*

### 1. Notebook List & Source Mapping
Inside `01_Master_Hardware_Strategy_Ledger/notebook_manifest.md`, detail exactly which files belong in which notebook:
*   **Notebook 1 (Master)**: All policy documents, scoring rubrics, master ledger, and output summaries from Notebooks 2-7.
*   **Notebook 2 (Expandable Workstations)**: `product_cards` tagged `#Expandable`, motherboard specs, PCIe lane diagrams.
*   **Notebook 3 (Single-GPU)**: `product_cards` tagged `#SingleGPUValue`, standard desktop reviews.
*   **Notebook 4 (Laptops)**: `product_cards` tagged `#PortableValue`, thermal throttling reports.
*   **Notebook 5 (Apple)**: `product_cards` tagged `#AppleSilicon`, unified memory deep dives.
*   **Notebook 6 (Mini PC)**: `product_cards` tagged `#MiniPC`, OCuLink benchmark data.
*   **Notebook 7 (Secondary)**: `product_cards` tagged `#Ergonomics`, thin-and-light laptop specs.

### 2. Tagging System
Create `01_Master_Hardware_Strategy_Ledger/tagging_taxonomy.md` with rules:
*   **Tier Tags**: `#VRAM-16GB`, `#VRAM-24GB`, `#VRAM-48GB+`
*   **Category Tags**: `#Expandable`, `#SingleGPUValue`, `#PortableValue`, `#AppleSilicon`, `#MiniPC`, `#Ergonomics`
*   **Status Tags**: `#Verified`, `#Incomplete`, `#Rejected`

### 3. Reusable Prompts
Create `01_Master_Hardware_Strategy_Ledger/prompts.md` containing:
*   **Lane-Specific Prompt**: A prompt to evaluate cards within a specific lane (e.g., "Compare these 24GB expandable systems based on PCIe lane distribution and future upgrade paths...").
*   **Master-Notebook Prompt**: A prompt to pit the "winners" from each lane against each other based on the ultimate goal (best ROI for local AI growth vs. current utility).

---

## Phase 3: Git Initialization & GitHub Sync

#### [NEW] [.gitignore](file:///Users/okgoogle13/Projects/Computer purchase/.gitignore)
- Exclude `.DS_Store`
- Exclude `*.zip`
- Exclude `_Archive_Legacy_Data/` (to keep the repo clean and under size limits)

### Execution Steps
1. `git init`
2. `git add .`
3. `git commit -m "feat: restructure for NotebookLM 7-lane hardware evaluation"`
4. `gh repo create "Computer-purchase" --public --source=. --remote=origin --push`
