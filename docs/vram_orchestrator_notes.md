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
