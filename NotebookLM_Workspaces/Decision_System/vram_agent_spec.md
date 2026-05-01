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
