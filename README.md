# NotebookLM Hardware Decision System

## Project Overview
This repository contains a structured, AI-assisted decision framework for evaluating, scoring, and selecting hardware (GPUs, Workstations, Mobile systems) specifically for running local Large Language Models (LLMs) and autonomous AI agents. 

Rather than relying on ad-hoc shopping, this project uses standardized product cards, strict VRAM architectural specifications, and programmatic tagging to ingest market data into NotebookLM (and other LLMs) for objective, rubric-based procurement ranking.

## Quickstart – 5‑Phase Hardware Decision Flow

1. **Build shortlist**  
   `python scripts/build_shortlist.py --batch YYYY-MM-DD_notebooklm_batchN`

2. **Check cards & schema drift**  
   `./scripts/generate_checklist_prompt.sh` + fix missing cards / `UNKNOWN` fields per `audit_context.md`.

3. **Create AI context bundles**  
   - NotebookLM: `./scripts/export_mega_bundle.sh`  
   - Scoring: `npx --yes repomix ... > scoring_context.md`

4. **AI scoring (Phase 4)**  
   Use `scoring_context.md` with `scripts/prompt_templates/ai_scoring_execution_prompt.md` to produce `*_shortlist_scored.csv`.

5. **Weighting & final decision (Phase 5)**  
   Run `rubric_weighting_engine.py --csv *_shortlist_scored.csv --profile merged > final_scores.txt`, then apply `final_purchase_justification_prompt.md` to generate `final_justification.md`.

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
* `/scripts/` - Contains the 3-phase automation pipeline:
  * `normalize_intake.py` and `intake_to_cards.py` (Phase 1: Intake)
  * `build_shortlist.py` (Phase 2: Shortlist)
  * `rubric_weighting_engine.py` (Phase 3: Score, located in the Policy Pack but run from root)
* `/_Archive_Legacy_Data/` - Superseded research, raw notes, and deferred lanes (e.g., Apple Silicon).

## Getting Started
1. Review `CURRENT_STATE.md` for the latest project milestone and immediate next actions.
2. Read `scripts/README_pipeline.md` to understand the 3-Phase workflow (Intake → Shortlist → Score).
3. Do not add raw web clippings to the workspace folders. Run new hardware candidates through the Phase 1 scripts first.
4. To execute a ranking pass, run `build_shortlist.py` to generate the CSV score sheet, fill it out, and then run `rubric_weighting_engine.py --profile merged`.
