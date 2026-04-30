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
