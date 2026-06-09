# Policy Drift Eliminator

## Problem Statement
The hardware procurement pipeline relies on two separate policy files: a human/agent-readable markdown file ([AGENTS.md](file:///Users/okgoogle13/Projects/Computer%20purchase/AGENTS.md)) and a machine-readable config file ([procurement_policy.json](file:///Users/okgoogle13/Projects/Computer%20purchase/config/procurement_policy.json)). Numeric thresholds have drifted or been entirely removed from the markdown file, leading to the validator (`policy_drift_check.py`) reporting all policy checks as `UNRESOLVED`.

## Recommended Direction
Make `config/procurement_policy.json` the single canonical source of truth for all quantitative/numeric policy thresholds. Update `scripts/policy_drift_check.py` to automatically verify alignment, and add an option (`--sync`) to automatically update the markdown file by splicing generated tables directly into [AGENTS.md](file:///Users/okgoogle13/Projects/Computer%20purchase/AGENTS.md) between specific marker tags (`<!-- POLICY_START -->` and `<!-- POLICY_END -->`).

## Key Assumptions to Validate
- [ ] AI agents and human readers require clear, up-to-date numeric thresholds in [AGENTS.md](file:///Users/okgoogle13/Projects/Computer%20purchase/AGENTS.md) to make correct evaluation decisions.
- [ ] Auto-generating these markdown blocks from [procurement_policy.json](file:///Users/okgoogle13/Projects/Computer%20purchase/config/procurement_policy.json) will eliminate the cognitive overhead of manual duplication.

## MVP Scope
1. **Marker Splicing in [AGENTS.md](file:///Users/okgoogle13/Projects/Computer%20purchase/AGENTS.md)**: Insert comment block tags around the Decision Tracks and Threshold Gates section.
2. **Harness Rewrite in [policy_drift_check.py](file:///Users/okgoogle13/Projects/Computer%20purchase/scripts/policy_drift_check.py)**:
   - Read and parse [procurement_policy.json](file:///Users/okgoogle13/Projects/Computer%20purchase/config/procurement_policy.json).
   - Generate formatted Markdown showing all track caps, memory minimums, and path budgets.
   - If in check-mode (default), compare with the spliced block inside [AGENTS.md](file:///Users/okgoogle13/Projects/Computer%20purchase/AGENTS.md) and fail if they mismatch.
   - If in sync-mode (`--sync`), overwrite the spliced section in place.
3. **Pipeline Integration**: Integrate the check step in the automatic pipeline runner ([run_automated_pipeline.py](file:///Users/okgoogle13/Projects/Computer%20purchase/scripts/run_automated_pipeline.py)).

## Not Doing (and Why)
- **JSON-izing Behavioral Rules**: We will not attempt to represent qualitative guidelines (e.g. "Good enough equals outcome-enabled" or token-saving rules) in JSON; they remain native markdown in [AGENTS.md](file:///Users/okgoogle13/Projects/Computer%20purchase/AGENTS.md).
- **Interactive Prompts**: No GUI or interactive prompt for syncing; it should be a simple CLI flag for terminal compatibility.

## Open Questions
- None.
