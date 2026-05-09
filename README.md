# NotebookLM Hardware Decision System

## Project Overview
This repository contains a structured, AI-assisted decision framework for evaluating, scoring, and selecting hardware for CareerCopilot development.

Rather than relying on ad-hoc shopping, this project uses standardized product cards, live AU verification, and fixed-weight MCDA scoring to reach a practical purchase decision.

## Quickstart – 5‑Phase Hardware Decision Flow

1. **Build shortlist**  
   `python scripts/build_shortlist.py --batch YYYY-MM-DD_notebooklm_batchN`

2. **Check cards & schema drift**  
   `./scripts/generate_checklist_prompt.sh` + fix missing cards / `UNKNOWN` fields per `audit_context.md`.

3. **Create AI context bundles**  
   - NotebookLM: `./scripts/export_mega_bundle.sh`  
   - Scoring: `npx --yes repomix ... > scoring_context.md`

4. **AI scoring (Phase 4)**  
   Use `scoring_context.md` with `scripts/prompt_templates/ai_scoring_execution_prompt.md` to fill the five MCDA factor columns.

5. **Weighting & final decision (Phase 5)**  
   Run `rubric_weighting_engine.py --csv *_shortlist_scored.csv > final_scores.txt`, then apply `final_purchase_justification_prompt.md` to generate `final_justification.md`.

## Canonical Workflow
The active workflow is the 5-phase pipeline defined in `AGENTS.md` and `scripts/README_pipeline.md`.

Track 1 laptops are the default buying path. Track 1.5 and Track 2 are only evaluated under the escalation rules in `AGENTS.md`.

Generated context bundles are support artifacts, not policy.

## Repository Structure (Source of Truth)
The repository is organized into distinct hardware "lanes" and a central decision engine:

* `/01_Research_Methods_and_Decision_System/` - Policy packs, older research notes, and the MCDA ranking engine.
* `/NotebookLM_Workspaces/` - **The Hardware Lanes.**
  * `/03_New_Desktop_Systems/`
  * `/02_Refurbished_Desktop_Towers/`
  * `/08_Custom_Builds/`
  * `/09_Individual_Components/`
  * `/04_Laptops_Mainline/`
  * `/06_Mini_PCs_and_eGPU/`
* `/scripts/` - Contains the automation pipeline:
  * `normalize_intake.py` and `intake_to_cards.py` (Phase 1: Intake)
  * `build_shortlist.py` (Phase 2: Shortlist)
  * `rubric_weighting_engine.py` (Phase 5: MCDA rank, located in the Policy Pack)
* `/_Archive_Legacy_Data/` - Superseded research, raw notes, and deferred lanes (e.g., Apple Silicon).

## Getting Started
1. Review `CURRENT_STATE.md` for the latest project milestone and immediate next actions.
2. Read `scripts/README_pipeline.md` to understand the 3-Phase workflow (Intake → Shortlist → Score).
3. Do not add raw web clippings to the workspace folders. Run new hardware candidates through the Phase 1 scripts first.
4. To execute a ranking pass, run `build_shortlist.py` to generate the CSV score sheet, fill it out, and then run `rubric_weighting_engine.py --profile merged`.
