# VRAM Architecture Specification for Local AI (v1)

## 1. Workload Definitions

This section defines the computational and memory characteristics of local AI workloads in 2026.

| Workload Type | Characteristics | Concurrency | Context Requirements |
| :--- | :--- | :--- | :--- |
| **Chat / Assistant** | High responsiveness, single-turn or short multi-turn interaction. | Low (1-2 users) | 4K - 16K tokens |
| **Autonomous Agent** | Multi-step reasoning, tool use (terminal, browser), self-correction. | Moderate (1 agent) | 32K - 128K tokens |
| **Project Research** | Large document ingestion (PDFs, codebases), cross-referencing. | Low | 64K - 256K+ tokens |
| **Agentic Coding** | Codebase-wide analysis, autonomous debugging, multi-file edits. | Moderate | 64K - 128K tokens |

**Note on Agentic Reliability**: In agentic workflows, reliability (instruction following and tool use) is prioritized over raw speed. The "reasoning gap" between local and cloud models begins to close at the 24GB VRAM threshold.

**Sources**: `Local LLM GPU VRAM Analysis.md` §2.2, §5.2.

---

## 2. Hardware Constraints

### 2.1 Memory-Bandwidth Bottleneck
In the 2026 paradigm, LLM inference is primarily memory-bandwidth-bound. Generation speed is directly proportional to the GPU's memory bandwidth.

### 2.2 The VRAM Equation
The total VRAM footprint ($V_{total}$) is calculated as:
$$V_{total} = V_{weights} + V_{KV\_cache} + V_{overhead}$$

*   **$V_{weights}$**: Model parameters at specific quantization.
    *   Example (30B Model at Q4): ~18.0 - 20.0 GB.
*   **$V_{KV\_cache}$**: Stored attention states.
    *   32K-64K context: ~1.5 - 4.0 GB.
*   **$V_{overhead}$**: Backend/Runtime (CUDA, drivers, runtime graphs).
    *   Typical: ~0.75 - 1.0 GB.

### 2.3 Component Baseline Requirements
| Component | Minimum Requirement | Preferred for Growth |
| :--- | :--- | :--- |
| **VRAM** | 12GB (Entry), 16GB (Developer) | 24GB+ (Standard) |
| **Bandwidth** | TODO: REQUIRED_METRIC_MISSING - Specify GB/s for 3090/4090/5090 | TODO: REQUIRED_METRIC_MISSING - Specify target GB/s memory bandwidth for future-proofing. |
| **System RAM** | 32GB | 64GB - 128GB (for weights offloading) |
| **PSU** | 850W (Single GPU) | 1000W - 1300W (Dual GPU growth) |
| **PCIe** | One x16 Slot | Dual x16 (x8/x8 electrical) |
| **NPU/TTFT** | TODO: REQUIRED_METRIC_MISSING - Baseline TTFT for 2026 models | TODO: REQUIRED_METRIC_MISSING |

**Sources**: `Local LLM GPU VRAM Analysis.md` §1.1, `policy_expandable_workstation_scoring.md` §2.

---

## 3. Hardware Tier Evaluation

### 3.1 12GB Tier: Entry-Level Constraint
*   **Supported Workloads**: Short-context chat, basic code snippets, email drafting.
*   **Model Range**: 7B to 9B parameters.
*   **Limitations**: "Context cliff" occurs quickly; unusable for long-form research or complex agentic multi-turn runs.

### 3.2 16GB Tier: Developer’s Compromise
*   **Supported Workloads**: Multi-turn technical writing, professional coding (single-file), small-agent tasks.
*   **Model Range**: 14B to 20B parameters comfortably; 30B with aggressive quantization (Q2/Q3).
*   **Highlight**: **GPT-OSS 20B** (MXFP4) – 42 t/s on 16GB hardware.
*   **Limitations**: "VRAM envy"; unable to run 70B+ class frontier models effectively.

### 3.3 24GB Tier: Standard for Local Autonomy
*   **Supported Workloads**: Full project ingestion, autonomous agentic coding, massive RAG databases.
*   **Model Range**: 30B to 35B at high-quality quantization (Q5/Q6) with 64K+ context.
*   **Highlight**: **Llama 4 Scout** (109B MoE) at INT4 quantization – the gold standard for early 2026.
*   **Sources**: `Local LLM GPU VRAM Analysis.md` §3.1-3.3.

---

## 4. Compatible Model Ecosystems

| Model Family | Target Tier | Logic |
| :--- | :--- | :--- |
| **Gemma 4 (E2B/E4B)** | 8GB - 12GB | Optimized for edge/mobile via PLE architecture. |
| **Gemma 4 (26B A4B MoE)** | 16GB - 24GB | High "intelligence-per-GB" via Mixture-of-Experts. |
| **Gemma 4 (31B Dense)** | 24GB+ | Claude surrogate; 256K context window support. |
| **Qwen 3.5 (32B Coder)** | 24GB | Best-in-class coding for 24GB VRAM. |
| **Llama 4 Scout** | 24GB (MoE) | Top local LLM in early 2026 using INT4. |

**Architecture Comparison**:
*   **NVIDIA CUDA**: Standard for local LLM inference; high performance on INT4/MXFP4.
*   **Apple Unified Memory**: Separate "quiet" route; 64GB+ unified memory allows running larger models that exceed 24GB consumer GPU limits. TODO: REQUIRED_METRIC_MISSING - Extract memory bandwidth specifications from Apple product cards to compare directly with NVIDIA CUDA performance.

**Sources**: `Local LLM GPU VRAM Analysis.md` §2, §5.

---

## 5. Total Cost of Ownership (TCO)

**Assumptions**: 3-year horizon. AUD pricing. used/refurbished vs. new. *Note: The used RTX 3090 CapEx split ($1,100 base + $1,100 GPU) is an estimate; the source (`Local LLM GPU VRAM Analysis.md`) only explicitly confirms the $2,200 total.*

| Component | Used RTX 3090 Build | New RTX 4090 Build | New RTX 5090 Build |
| :--- | :--- | :--- | :--- |
| **Base System (CPU/MB/RAM/PSU)** | ~$1,100 | ~$1,800 | ~$2,500 |
| **GPU** | ~$1,100 | ~$2,400 | ~$5,000 |
| **Cooling (Mod/Active Backplate)** | ~$200 | ~$0 (Stock) | ~$0 (Stock) |
| **Est. Power (Monthly)** | ~$15 | ~$25 | ~$40 |
| **Total CapEx (Upfront)** | **~$2,200** | **~$4,200** | **~$7,500** |
| **Break-even vs $100/mo Cloud** | **~15 Months** | **~29 Months** | **~52 Months** |

**Sources**: `Local LLM GPU VRAM Analysis.md` §4.2, `rubric_component_synergy_matrix.md`.

---

## 6. Deployment Logistics & Orchestration

### 6.1 Multi-GPU Considerations
*   **Single-Node**: Consumer setups (3090/4090) are limited by PCIe lane distribution.
*   **Enterprise/Workstation**: Dell Precision / HP Z-series allow for dual-GPU growth with proper x8/x8 or x16/x16 lane separation.
*   **Cooling**: Blower-style cards are preferred for multi-GPU density. RTX 3090 specifically requires VRAM thermal management (active backplate/waterblock).

### 6.2 Frameworks
*   **Ollama + OpenCode**: Low-friction developer setup for 16GB.
*   **OpenClaw + OpenCode**: Dual-agent setup for 24GB (mimicking Claude Code).
*   **Genkit / MCP Servers**: TODO: REQUIRED_METRIC_MISSING - Describe specific orchestration patterns present in repo.

**Sources**: `Local LLM GPU VRAM Analysis.md` §5.2, §6.1.

---

## 7. Decision Logic & Checklists

### 7.1 Platform Selection IF/THEN
*   **IF** ultimate goal is multi-year growth and multi-GPU (48GB+ VRAM) **THEN** choose **Expandable Workstation** (Xeon/Threadripper) with 1000W+ PSU.
*   **IF** budget is <$2,500 AUD and immediate 24GB VRAM is needed **THEN** choose **Used RTX 3090 Tower**.
*   **IF** mobility is critical and AI is secondary **THEN** choose **Apple 64GB Unified Memory** (MacBook/Studio).
*   **IF** desk space is limited but modularity is desired **THEN** choose **Mini PC + OCuLink eGPU**.

### 7.2 Deployment Checklist
1. [ ] **Verify PSU**: 850W minimum for single 3090/4090; 1000W+ for growth.
2. [ ] **Confirm PCIe Layout**: At least one x16 slot; dual slots for growth.
3. [ ] **Check Case Clearance**: 320mm+ for modern high-end GPUs.
4. [ ] **Ensure Airflow**: Mesh front or workstation ducting.
5. [ ] **VRAM Thermal Management**: Check backplate temps for 3090; consider active cooling.

**Sources**: `policy_expandable_workstation_scoring.md`, `rubric_component_synergy_matrix.md`, `Local LLM GPU VRAM Analysis.md` §7.
