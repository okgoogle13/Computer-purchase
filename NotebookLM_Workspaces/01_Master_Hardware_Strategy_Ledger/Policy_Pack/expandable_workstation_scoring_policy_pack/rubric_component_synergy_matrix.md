# Component Synergy Matrix – Expandable AI Workstations

Use this as a checklist when evaluating whether a machine is cohesive.

## GPU ↔ PSU

| GPU setup | Minimum PSU | Preferred PSU | Notes |
|---|---:|---:|---|
| 1× RTX 3090 24GB | 850W | 1000W | 3090 transient spikes matter. |
| 2× RTX 3090 24GB | 1200W | 1300W+ | Prefer blower cards, strong airflow. |
| 1× RTX 4090 24GB | 850W | 1000W | Native 12VHPWR / safe cabling important. |
| 2× RTX 4090 24GB | 1300W | 1600W | Usually impractical in normal consumer cases. |
| 1× RTX A5000 24GB | 750W | 850W | Lower power, workstation-friendly. |
| 2× RTX A5000 24GB | 1000W | 1200W | Strong multi-GPU workstation route. |
| 1× RTX A6000 48GB | 850W | 1000W | Expensive but excellent capacity. |

## GPU ↔ Case

| Case trait | Score impact |
|---|---|
| 320mm+ GPU clearance | Positive |
| 3-slot GPU support | Positive |
| Two 2-slot blower GPUs supported | Strong positive |
| Drive cage blocks long GPU | Negative |
| Solid front panel with weak intake | Negative |
| Unknown clearance | Reduce compatibility confidence |

## CPU ↔ Workload

| CPU class | Fit |
|---|---|
| Xeon W / Threadripper / Threadripper Pro | Strong workstation fit |
| Ryzen 9 / Core i9 | Strong consumer creator fit |
| Ryzen 7 / Core i7 | Usually adequate for GPU-bound inference |
| Old low-core Xeon | Acceptable only if GPU value is excellent |
| Weak SFF CPU | Penalise for high-end GPU pairing |

## RAM ↔ Workload

| RAM | Fit |
|---:|---|
| 32GB | Minimum serious baseline |
| 64GB | Preferred current target |
| 128GB | Strong growth-platform target |
| 256GB+ | Enterprise bonus if price is reasonable |

## Storage ↔ Workload

| Storage setup | Fit |
|---|---|
| 1TB NVMe only | Minimum, likely needs upgrade |
| 2TB NVMe | Preferred baseline |
| 2× NVMe + SATA bays | Strong |
| No NVMe / HDD-only | Reject or upgrade immediately |

## Compatibility Confidence Caps

| Missing detail | Cap |
|---|---:|
| PSU wattage unknown | Compatibility confidence max 7/15 |
| Motherboard model / slot layout unknown | Upgrade path max 5/10 |
| Case GPU clearance unknown | Thermals/noise max 6/10 |
| GPU VRAM unclear | Workload fit max 12/25 |
| Warranty unclear | Reliability max 2/5 |
