# NotebookLM Hardware Decision System

## Project Overview
This repository contains a structured, AI-assisted decision framework for evaluating, scoring, and selecting hardware (GPUs, Workstations, Mobile systems) specifically for running local Large Language Models (LLMs) and autonomous AI agents. 

Rather than relying on ad-hoc shopping, this project uses standardized product cards, strict VRAM architectural specifications, and programmatic tagging to ingest market data into NotebookLM (and other LLMs) for objective, rubric-based procurement ranking.

## Canonical Workflow: The 3-Notebook Architecture
After evaluating multiple ingestion models, the official execution path for this project is the **3-Notebook Architecture**. This prevents the AI from hallucinating specifications across different form factors (e.g., confusing a laptop RTX 4090 TDP with a desktop RTX 4090 TDP).

* **Notebook A (Policy & VRAM Brain):** Contains timeless logic, VRAM architecture specs, and scoring rubrics. *No product listings are ingested here.*
* **Notebook B (Desktop / Tower Arena):** Evaluates traditional x86/CUDA PC architectures (New Towers, Refurbished Workstations, Custom Builds, Components).
* **Notebook C (Mobile / Small-Form Arena):** Evaluates portable and edge-case architectures (Laptops, Mini-PCs, eGPUs).

*Note: A `Complete_Hardware_Procurement_Knowledge_Base.md` mega-bundle is also maintained in the root as a fallback/single-shot ingestion asset.*

## Repository Structure (Source of Truth)
The repository is organized into distinct hardware "lanes" and a central decision engine:

* `/01_Research_Methods_and_Decision_System/` - **The Brain.** Contains the VRAM Architecture Spec, Policy Packs, and the Master Scoring Rubric.
* `/NotebookLM_Workspaces/` - **The Hardware Lanes.**
  * `/03_New_Desktop_Systems/`
  * `/02_Refurbished_Desktop_Towers/`
  * `/08_Custom_Builds/`
  * `/09_Individual_Components/`
  * `/04_Laptops_Mainline/`
  * `/06_Mini_PCs_and_eGPU/`
* `/scripts/` - Contains automation tools (`tag_product_cards.py`, `sort_product_cards.sh`) for standardizing new hardware candidates.
* `/_Archive_Legacy_Data/` - Superseded research, raw notes, and deferred lanes (e.g., Apple Silicon).

## Getting Started
1. Review `CURRENT_STATE.md` for the latest project milestone and immediate next actions.
2. Do not add raw web clippings to the workspace folders. Run new hardware candidates through the Product Card template first.
3. To execute a ranking pass, follow the prompts located in the `/01_Research_Methods_and_Decision_System/` folder to process finalists from Notebooks B & C into Notebook A.
