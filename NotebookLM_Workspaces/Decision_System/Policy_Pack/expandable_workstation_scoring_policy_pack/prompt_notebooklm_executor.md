# Prompt – NotebookLM Executor for Product Listings

Use this prompt inside a NotebookLM notebook after uploading:

- `Policy – Expandable Workstation Scoring`
- `Template – Product Card Output`
- Product listing sources

```text
Using the sources “Policy – Expandable Workstation Scoring” and “Template – Product Card Output” plus the product listing sources in this notebook:

1. For each candidate desktop, extract all available spec details relevant to PSU, motherboard, RAM, storage, case, cooling, and GPU support.
2. Apply the policy scoring rubric exactly as written, explicitly penalising uncertainty where the listing hides or omits critical facts.
3. Produce one product card per candidate using the exact Markdown structure from the template source. Do not add extra sections. Do not omit headings.
4. In “Rejected or risky points”, clearly state any reasons this machine is a bad fit for multi-GPU or high-TDP workloads, even if it looks good as a normal gaming PC.
5. If a listing lacks enough information to score safely, say so in the compatibility confidence line and avoid “Strong buy”. Use “Conditional buy” or “Not recommended for expandable AI workstation”.
6. Prioritise 24GB+ usable NVIDIA VRAM now, or platforms that can grow toward multiple GPUs and 48GB+ total VRAM. Do not over-rank 16GB VRAM systems unless price is unusually compelling.
7. Penalise builds that technically work now but leave no PSU, PCIe, storage, cooling, or chassis room for future GPU expansion.

Start with these listings:
[Paste listing names / source names / URLs here]

When finished, briefly compare the cards and label the single best candidate for expandable AI workstation use, not generic gaming.
```
