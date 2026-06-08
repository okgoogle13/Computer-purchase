# NotebookLM Hardware Decision System

## Project Overview
This repository contains a structured, AI-assisted decision framework for evaluating, scoring, and selecting hardware for CareerCopilot development.

Rather than relying on ad-hoc shopping, this project uses standardized product cards, live AU verification, and fixed-weight MCDA scoring to reach a practical purchase decision.

## Quickstart – 5‑Phase Hardware Decision Flow

0. **Spec Clarification (optional)**  
   `python scripts/agents/spec_clarifier/agent.py`  
   Interactively defines your requirements (track, VRAM floor, budget) and outputs a `--spec-json` blob.

1. **Build shortlist**  
   `python scripts/build_shortlist.py --batch YYYY-MM-DD_notebooklm_batchN`  
   Add `--spec-json '{...}'` to apply Phase 0 output as filter overrides.

2. **Phase 3a scaffold pricing schema**  
   `python scripts/enrich_shortlist_pricing.py NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist.csv`

3. **Phase 3b fill live pricing verification**  
   `python scripts/fill_shortlist_live_pricing.py NotebookLM_Workspaces/intake/shortlist/YYYY-MM-DD_shortlist_pricing_enriched.csv`

4. **Manual/AI scoring (Phase 4)**  
   Fill the five MCDA factor columns (`Performance_Headroom`, `Price_Value`, `Future_Proof`, `Portability`, `Track2_Avoidance`) on the live-enriched CSV.

5. **Weighting & final decision (Phase 5)**  
   Run `python NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/rubric_weighting_engine.py --csv *_shortlist_pricing_enriched_live.csv --output-csv *_shortlist_ranked.csv`.

## Canonical Workflow
The active workflow is the 5-phase pipeline defined in `AGENTS.md` and `scripts/README_pipeline.md`.

Track 1 laptops are the default buying path. Track 1.5 and Track 2 are only evaluated under the escalation rules in `AGENTS.md`.

Generated context bundles are support artifacts, not policy.

Phase 3 is split by ownership:
- `scripts/enrich_shortlist_pricing.py` is scaffold-only and must not perform live lookup.
- `scripts/fill_shortlist_live_pricing.py` performs live fill for queued rows.
- `rubric_weighting_engine.py` keeps MCDA weighting intact and adds transparent seller/source risk post-processing columns.

## Repository Structure (Source of Truth)
The repository is organized into distinct hardware "lanes" and a central decision engine:

* `/NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/` - Policy packs, older research notes, and the MCDA ranking engine.
* `/NotebookLM_Workspaces/` - **The Hardware Lanes.**
  * `/03_New_Desktop_Systems/`
  * `/02_Refurbished_Desktop_Towers/`
  * `/08_Custom_Builds/`
  * `/09_Individual_Components/`
  * `/04_Laptops_Mainline/`
  * `/06_Mini_PCs_and_eGPU/`
* `/scripts/` - Contains the automation pipeline:
  * `normalize_intake.py` and `intake_to_cards.py` (Phase 1: Intake)
  * `build_shortlist.py` (Phase 2: Shortlist; accepts `--spec-json`)
  * `enrich_shortlist_pricing.py` (Phase 3a: schema scaffold only)
  * `fill_shortlist_live_pricing.py` (Phase 3b: live verification fill)
  * `scoring/rubric_weighting_engine.py` (Phase 5: MCDA rank)
  * `agents/spec_clarifier/` (Phase 0: conversational intake agent — ADK pattern)
* `/_Archive_Legacy_Data/` - Superseded research, raw notes, and deferred lanes (e.g., Apple Silicon).

## Getting Started
1. Review `CURRENT_STATE.md` for the latest project milestone and immediate next actions.
2. Read `scripts/README_pipeline.md` to understand the 5-phase workflow with Phase 3a/3b split.
3. Do not add raw web clippings to the workspace folders. Run new hardware candidates through the Phase 1 scripts first.
4. To execute a ranking pass, run `build_shortlist.py` to generate the CSV score sheet, fill it out, and then run `python NotebookLM_Workspaces/01_Research_Methods_and_Decision_System/Policy_Pack/expandable_workstation_scoring_policy_pack/rubric_weighting_engine.py --csv <scored_csv>`.
