# Template – Product Card Output

Use this exact Markdown structure for each candidate.

```markdown
<!-- PRODUCT CARD START: [Machine name or short label] -->
### [Machine name or short label]

**Headline verdict:** [1–2 lines. Example: “Strong single-GPU refurb, weak multi-GPU future.”]

**Score:** [X] / 100 overall
- Workload fit: [X] / 25
- Component synergy: [X] / 20
- Compatibility confidence: [X] / 15
- Thermals / noise: [X] / 10
- Upgrade path: [X] / 10
- Value: [X] / 15
- Efficiency / reliability: [X] / 5

**Classification**
- Expansion class: [Growth Platform / Single-24GB-GPU Candidate / Single-GPU Value Exception / Portable Value Exception / Unified-Memory Exception / Modular Exception / Rejected Benchmark]
- VRAM strategy fit: [48GB+ Growth Target / Single 24GB Target / 16GB Compromise / Rejected]
- Recommendation: [Strong buy / Conditional buy (if X) / Niche buy / Not recommended for expandable AI workstation]

**Key specs (from listing)**
- CPU:
- RAM (capacity, type, slots used/free):
- Storage (NVMe, SATA, total bays):
- GPU (if included, else “not included”):
- Motherboard notes (chipset, slots, PCIe layout if known):
- PSU (model, wattage, efficiency, connectors if known):
- Case / form factor (size, GPU clearance, fan positions if known):
- Warranty / seller terms:

**Synergy analysis**
- CPU ↔ GPU balance:
- PSU ↔ GPU(s) / CPU headroom:
- Cooling ↔ workload:
- Case ↔ GPU length / airflow:
- Platform ↔ upgrade path:

**Best-fit use case**
[Short paragraph describing who this is actually good for and at what budget/performance tradeoff.]

**Rejected or risky points**
- [Bottleneck, imbalance, or risk]
- [Unknown that meaningfully affects scoring]
- [Platform limitation for future dual-GPU or high-TDP upgrades]

**Overall recommendation**
[Strong buy / Conditional buy (if X) / Niche buy / Not recommended for expandable AI workstation]

**Verification required before purchase**
- [PSU model / wattage / connectors]
- [Motherboard PCIe slot layout]
- [Case GPU clearance]
- [Warranty / return policy]
<!-- PRODUCT CARD END: [Machine name or short label] -->
```
