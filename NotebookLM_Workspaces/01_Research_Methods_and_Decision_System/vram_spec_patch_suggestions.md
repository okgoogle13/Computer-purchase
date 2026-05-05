# VRAM Spec Patch Suggestions

Apply these manual edits to `vram_architecture_spec_v1.md` to resolve the issues identified in the validation report.

## Patch 1: Fix Vague TODO in Hardware Constraints
**Location**: Section 2.3 Component Baseline Requirements (Table)
**Issue**: The "Preferred for Growth" Bandwidth column has a vague TODO marker.
**Action**: Replace the cell contents.
```diff
- | **Bandwidth** | TODO: REQUIRED_METRIC_MISSING - Specify GB/s for 3090/4090/5090 | TODO: REQUIRED_METRIC_MISSING |
+ | **Bandwidth** | TODO: REQUIRED_METRIC_MISSING - Specify GB/s for 3090/4090/5090 | TODO: REQUIRED_METRIC_MISSING - Specify target GB/s memory bandwidth for future-proofing. |
```

## Patch 2: Add Missing Source Evidence for Apple vs NVIDIA
**Location**: Section 4 Compatible Model Ecosystems (Architecture Comparison)
**Issue**: The comparison makes claims about Apple unified memory exceeding 24GB limits without explicit spec backing from the product cards.
**Action**: Insert a TODO marker to force spec extraction.
```diff
- *   **Apple Unified Memory**: Separate "quiet" route; 64GB+ unified memory allows running larger models that exceed 24GB consumer GPU limits, but with potentially different memory-bandwidth characteristics.
+ *   **Apple Unified Memory**: Separate "quiet" route; 64GB+ unified memory allows running larger models that exceed 24GB consumer GPU limits. TODO: REQUIRED_METRIC_MISSING - Extract memory bandwidth specifications from Apple product cards to compare directly with NVIDIA CUDA performance.
```

## Patch 3: Clarify Inconclusive TCO Split
**Location**: Section 5 Total Cost of Ownership (TCO)
**Issue**: The $1,100 / $1,100 split for Base System / GPU is an estimation not explicitly found in the source text, which only specifies the $2,200 total and $950-$1,100 marketplace price.
**Action**: Add a disclaimer to the Assumptions block.
```diff
- **Assumptions**: 3-year horizon. AUD pricing. used/refurbished vs. new.
+ **Assumptions**: 3-year horizon. AUD pricing. used/refurbished vs. new. *Note: The used RTX 3090 CapEx split ($1,100 base + $1,100 GPU) is an estimate; the source (`Local LLM GPU VRAM Analysis.md`) only explicitly confirms the $2,200 total.*
```
