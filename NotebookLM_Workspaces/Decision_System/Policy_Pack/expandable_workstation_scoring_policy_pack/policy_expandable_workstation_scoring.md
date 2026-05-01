# Policy – Expandable Workstation Scoring

## Goal

Identify refurbished desktops, workstation towers, and selected boutique prebuilts that make excellent expandable AI / GPU workstations, not just good single-GPU gaming PCs.

The primary target is:

> **24GB+ usable NVIDIA VRAM now, or a tower/workstation platform that can grow toward multiple GPUs and 48GB+ total VRAM.**

16GB VRAM systems are not the central target. They may be scored only as discounted value exceptions, temporary compromise systems, or comparative benchmarks.

## Non-Negotiable Filters

### Form Factor

Prefer:
- Full tower, mid tower, full ATX, E-ATX, enterprise tower, workstation tower.
- Dell Precision tower-class systems.
- HP Z-series tower-class systems.
- Threadripper, Xeon, Ryzen 9, Core i9, workstation-class platforms.

Reject or heavily penalise:
- SFF / USDT / mini desktops unless they clearly support full-length GPUs and adequate PSU.
- Compact proprietary gaming cases with poor airflow unless price is unusually strong.
- Towers with no clear GPU clearance or no PSU details.

### PSU

Minimum baseline:
- 850W only for single 24GB GPU systems.
- 1000W–1300W preferred for future dual-GPU growth.
- 80+ Gold or better preferred.
- Must have enough safe PCIe power connectors for the current GPU and plausible future GPU.

For dual-GPU growth:
- Estimate CPU + GPU sustained load.
- Add transient-spike allowance.
- Aim for at least 30% headroom over worst-case sustained draw.
- Penalise unknown PSU brand/model/wattage.
- Penalise proprietary PSUs unless replacement modules and GPU cables are available.

### PCIe Slots and Lanes

Minimum:
- At least one full-length x16 physical slot.

Preferred:
- Two full-length PCIe x16 physical slots.
- x8/x8 electrical support or better for dual GPU.
- Slot spacing suitable for two 2-slot blower cards or two modern 3-slot cards.
- Additional PCIe slots for NIC, capture card, HBA, RAID, or future expansion.

Penalise:
- Unknown motherboard layout.
- Second slot physically blocked by GPU, PSU shroud, drive cage, or case layout.
- Consumer boards where second x16 slot is only x4 and shares lanes in unclear ways.
- No documentation of PCIe slot layout.

### Power Connectors

Verify:
- 8-pin / dual 8-pin / triple 8-pin / 12VHPWR / 12V-2x6 support.
- Native connectors are preferred.
- Safe manufacturer-approved adapters are acceptable only if PSU quality and connector load are credible.
- Avoid questionable daisy-chain PCIe power cabling for high-power GPUs.

### Cooling

Minimum:
- Clear front-to-back airflow path.
- At least two intake and one exhaust fan positions for high-power GPU use.
- CPU cooler adequate for target CPU sustained power.
- GPU intake/exhaust not blocked by solid panels or drive cages.

Preferred:
- Enterprise high-static-pressure airflow.
- Blower-style GPUs for dense dual-GPU setups.
- Large mesh front or workstation ducting.
- Clear thermal path for second GPU.

Penalise:
- Glass-box aesthetics with weak intake.
- Compact cases with one high-power open-air GPU already heat-soaked.
- Unknown fan layout.
- Laptop-style or proprietary cooling in desktop cases.

### Case Clearance

Minimum:
- Must fit modern full-length GPU.
- Target GPU clearance: 320mm+ preferred.
- For future cards, prefer clearance for 3-slot GPUs unless explicitly using blower/workstation 2-slot cards.

Penalise:
- Unknown clearance.
- Drive cages blocking GPU length.
- Case only suitable for one large GPU.
- No room between GPUs for airflow.

### RAM

Minimum:
- 32GB installed for serious use.
- 64GB preferred.
- Must support at least 128GB for growth-platform scoring.
- ECC support is a bonus for enterprise/workstation platforms.

Penalise:
- 16GB RAM on a high-end GPU system unless upgrade is cheap and straightforward.
- Soldered or limited RAM.
- Unknown RAM slot count.

### Storage

Minimum:
- At least one NVMe SSD.
- 1TB minimum; 2TB preferred.

Preferred:
- Two or more M.2 slots.
- SATA bays for bulk model/data storage.
- Easy drive access.

Penalise:
- Unknown storage expansion.
- Single small SSD with no expansion details.

### Reliability

Reward:
- Enterprise/workstation platforms.
- Known OEM workstation families.
- ECC RAM support.
- Local warranty.
- Refurbishers with clear return policies.
- Mature platforms with stable BIOS/chipset support.

Penalise:
- Unknown motherboard.
- Unknown PSU.
- No warranty.
- Seller avoids basic technical questions.
- Non-transferable warranty.

## Synergy Rules

### CPU ↔ GPU Balance

Avoid pairing ultra-high-end GPUs with very weak CPUs unless the workload is clearly GPU-bound inference and the price is compelling.

Score higher when:
- CPU has enough cores/threads for data prep, dev workloads, multitasking, and model serving.
- Platform has enough PCIe lanes for GPU + NVMe + expansion.
- CPU generation is not so old that platform stability, driver support, or general responsiveness suffers.

### PSU ↔ GPU(s) ↔ CPU

Always estimate:
- CPU sustained power.
- GPU sustained power.
- Future second-GPU power.
- Transient spike risk.
- Connector availability.

Score lower if a build technically works today but needs a PSU replacement before the intended second GPU.

### Cooling ↔ Case ↔ Workload

AI inference/image generation can run sustained high GPU load.

Score higher for:
- Airflow-first cases.
- Workstation ducts.
- Blower cards in dense multi-GPU platforms.
- Conservative thermals over RGB aesthetics.

Score lower for:
- Compact cases.
- Poor intake.
- Hot-running open-air GPUs stacked together.
- Unknown fan layout.

### Platform ↔ Upgrade Path

Reward systems that can accept:
- More RAM.
- More NVMe/SATA storage.
- Second GPU.
- Higher-TDP CPU.
- Standard ATX PSU replacement.
- Standard case/fan upgrades.

Penalise systems that require a total rebuild to reach the stated target.

## Scoring Rubric (Atomic Dimensions)

Evaluate each candidate on the following atomic dimensions. Score each out of 10 points based on the facts provided in the listing.

| Category / UX Grouping | Subcriterion | Scale (0-10) Guidelines |
|---|---|---|
| **Workload Fit** | `VRAM Adequacy` | 10: 48GB+, 8: 24GB, 5: 16GB, 0: <16GB |
| | `GPU Compute Tier` | 10: RTX 4090/A6000, 8: RTX 3090, 6: RTX 4080/5070Ti |
| | `CPU Multi-core Sustained` | 10: High-end Threadripper/Xeon W, 8: Modern i9/R9, 5: i7/R7 |
| | `System RAM Capacity` | 10: 128GB+, 8: 64GB, 5: 32GB, 0: <32GB |
| **Component Synergy** | `PSU Headroom for Current GPU` | 10: 30%+ headroom over spikes, 5: adequate, 0: unsafe/unknown |
| | `CPU/GPU PCIe Bottleneck Risk` | 10: Full x16 Gen4+, 5: Shared lanes/older Gen, 0: Severe bottleneck |
| **Compatibility** | `PCIe Slot Layout Clarity` | 10: Full motherboard diagram/specs, 5: Text description only, 0: Unknown |
| | `PSU Connector Availability` | 10: Native cables listed, 5: Adapters needed, 0: Unknown cables |
| **Thermals/Noise** | `Intake Airflow Volume` | 10: High static pressure/mesh, 5: Standard airflow, 0: Solid glass/blocked |
| | `Sustained Thermal Stability` | 10: Blower/workstation layout, 5: Standard open-air, 0: Compact case |
| **Upgrade Path** | `Second PCIe x16 Slot Usability` | 10: True x16/x8 clear, 5: Shared x4/partially blocked, 0: None/blocked |
| | `Chassis Clearance for 2nd GPU` | 10: 320mm+ with spacing, 5: Tight but possible, 0: No room |
| | `PSU Wattage Ceiling` | 10: 1200W+ (Multi-GPU ready), 8: 1000W, 5: 850W, 0: Proprietary <800W |
| **Value/Reliability** | `Price per GB VRAM` | 10: Excellent value (<$150/GB), 5: Average, 0: Very expensive |
| | `Enterprise Pedigree` | 10: Dell Precision/HP Z, 5: Quality custom, 0: Unknown OEM/cheap prebuilt |
| | `Warranty Coverage` | 10: 3yr+ Onsite, 8: 1yr Return, 0: No warranty |

*Note: Final weighting will be handled by external correlation-aware aggregation.*

## Hard Scoring Rules

- Never score a machine as **Strong buy** if PSU model, motherboard layout, or case clearance are completely unknown.
- If PSU wattage is unknown, compatibility confidence is capped at 7/15.
- If motherboard PCIe layout is unknown, upgrade path is capped at 5/10.
- If case clearance is unknown, thermals/noise is capped at 6/10.
- If GPU VRAM is below 24GB, workload fit is capped unless the listing is a value exception.
- If the system cannot plausibly support a future second GPU, it cannot be classified as a Growth Platform.
- If a listing hides too many technical details, use **Conditional buy** or **Not recommended**, not **Strong buy**.

## Recommendation Labels

Use exactly one:

- **Strong buy**: Strong current capability, clear specs, strong value, and no critical unknowns.
- **Conditional buy (if X)**: Good candidate but depends on verifying PSU, motherboard, warranty, clearance, or price.
- **Niche buy**: Useful for a specific scenario but not broadly recommended.
- **Not recommended for expandable AI workstation**: Fails expansion, value, thermals, or critical-spec confidence.
