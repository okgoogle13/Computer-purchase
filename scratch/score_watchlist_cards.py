#!/usr/bin/env python3
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

scores_map = {
    "intake-001_gigabyte-aorus-174-ye5-173-rtx-3080ti-300hz-intel-i7-12th-ge.md": {
        "Performance_Headroom": "7.0",
        "Price_Value": "8.5",
        "Future_Proof": "7.0",
        "Portability": "5.0",
        "Track2_Avoidance": "7.0",
        "Upgrade_Ceiling": "3.0"
    },
    "intake-002_razer-blade-18-qhd-240hz-i9-13950hx-rtx4090-2tb-32gb-w11h-ga.md": {
        "Performance_Headroom": "7.0",
        "Price_Value": "4.5",
        "Future_Proof": "7.5",
        "Portability": "4.5",
        "Track2_Avoidance": "7.0",
        "Upgrade_Ceiling": "3.0"
    },
    "intake-003_aasus-rog-strix-scar-17-se-173-i7-12950hx-32g-2tb-ssd-rtx308.md": {
        "Performance_Headroom": "7.0",
        "Price_Value": "6.0",
        "Future_Proof": "7.0",
        "Portability": "5.0",
        "Track2_Avoidance": "7.0",
        "Upgrade_Ceiling": "3.0"
    },
    "intake-004_lenovo-legion-9i-18-wquxga-intel-ultra-9-240hz-2tb-64gb-rtx5.md": {
        "Performance_Headroom": "8.0",
        "Price_Value": "3.5",
        "Future_Proof": "8.0",
        "Portability": "4.5",
        "Track2_Avoidance": "7.0",
        "Upgrade_Ceiling": "3.0"
    },
    "intake-005_razer-blade-pro-17-173-intel-core-i7-10875h-gaming-laptop.md": {
        "Performance_Headroom": "0.0",
        "Price_Value": "5.0",
        "Future_Proof": "2.0",
        "Portability": "5.0",
        "Track2_Avoidance": "0.0",
        "Upgrade_Ceiling": "3.0"
    },
    "intake-006_asus-rog-strix-17-rtx-4090-laptop-qhd-240hz-display-64gb-ram.md": {
        "Performance_Headroom": "7.0",
        "Price_Value": "5.5",
        "Future_Proof": "7.5",
        "Portability": "5.0",
        "Track2_Avoidance": "7.0",
        "Upgrade_Ceiling": "3.0"
    }
}

def update_card(file_path: Path, scores: dict):
    print(f"Updating card: {file_path.name}")
    content = file_path.read_text(encoding="utf-8")
    
    # 1. Update frontmatter
    # Find frontmatter section
    fm_match = re.match(r"^(<!--.*?-->\s*<!--.*?-->\s*)?---(.*?)---", content, re.DOTALL)
    if not fm_match:
        print(f"  Error: Could not find frontmatter in {file_path.name}")
        return
        
    prefix = fm_match.group(1) or ""
    fm_body = fm_match.group(2)
    
    # Clean existing MCDA scores from frontmatter if they exist
    lines = []
    for line in fm_body.splitlines():
        if not any(line.strip().startswith(k + ":") for k in scores.keys()):
            lines.append(line)
            
    # Add new scores to frontmatter
    for k, v in scores.items():
        lines.append(f"{k}: {v}")
        
    new_fm_body = "\n".join(lines)
    
    # Replace frontmatter in content
    new_content = prefix + "---\n" + new_fm_body.strip() + "\n---" + content[fm_match.end():]
    
    # 2. Update markdown body MCDA scores section
    mcda_sec_pattern = r"## MCDA Scores\n- \*\*Performance_Headroom:\*\* [^\n]*\n- \*\*Price_Value:\*\* [^\n]*\n- \*\*Future_Proof:\*\* [^\n]*\n- \*\*Portability:\*\* [^\n]*\n- \*\*Track2_Avoidance:\*\* [^\n]*\n- \*\*MCDA_Total:\*\* [^\n]*"
    
    replacement_sec = f"""## MCDA Scores
- **Performance_Headroom:** {scores['Performance_Headroom']}
- **Price_Value:** {scores['Price_Value']}
- **Future_Proof:** {scores['Future_Proof']}
- **Portability:** {scores['Portability']}
- **Track2_Avoidance:** {scores['Track2_Avoidance']}
- **Upgrade_Ceiling:** {scores['Upgrade_Ceiling']}
- **MCDA_Total:** UNKNOWN"""

    new_content = re.sub(mcda_sec_pattern, replacement_sec, new_content)
    
    file_path.write_text(new_content, encoding="utf-8")
    print(f"  Successfully updated scores for {file_path.name}")

def main():
    cards_dir = REPO_ROOT / "cards"
    for filename, scores in scores_map.items():
        file_path = cards_dir / filename
        if file_path.exists():
            update_card(file_path, scores)
        else:
            print(f"Warning: File {filename} not found in {cards_dir}")

if __name__ == "__main__":
    main()
