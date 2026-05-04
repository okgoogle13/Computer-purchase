import os
import shutil

base_dir = "/Users/okgoogle13/Projects/Computer purchase"

# 1. DELETE
try:
    os.remove(os.path.join(base_dir, "NotebookLM_Workspaces/Mini_PC_and_eGPU/41_asus-nuc-strix-halo.md"))
except FileNotFoundError:
    pass
try:
    os.remove(os.path.join(base_dir, "NotebookLM_Workspaces/Desktop_Towers_Refurbished/29_dell-precision-tower-7910-rtx-3090.md"))
except FileNotFoundError:
    pass

# CREATE DIRS
os.makedirs(os.path.join(base_dir, "NotebookLM_Workspaces/Gaming_Laptops_AMD_Discrete"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "NotebookLM_Workspaces/Desktop_Gaming_Refurbished"), exist_ok=True)

# MOVE & MODIFY CARDS
def move_and_tag(src, dest):
    src_path = os.path.join(base_dir, src)
    dest_path = os.path.join(base_dir, dest)
    if os.path.exists(src_path):
        with open(src_path, "r") as f:
            content = f.read()
        
        # Add metadata
        meta = """
track: track_1.5
category: refurbished_gaming_desktop
price_performance_vs_track1: CALCULATE (desktop_price / laptop_comparable_price)
vram_advantage_vs_track1: CALCULATE (desktop_vram - laptop_vram_gpu_available)
portability_penalty: true"""
        
        # Insert metadata after category/gpu etc. in frontmatter if exists
        if "---" in content:
            parts = content.split("---", 2)
            if len(parts) >= 3:
                parts[1] = parts[1].rstrip() + meta + "\n"
                content = "---".join(parts)
        
        with open(dest_path, "w") as f:
            f.write(content)
        os.remove(src_path)

move_and_tag("NotebookLM_Workspaces/Desktop_Towers_Refurbished/09_alienware-aurora-r12-rtx-3090-refurbished.md", 
             "NotebookLM_Workspaces/Desktop_Gaming_Refurbished/09_alienware-aurora-r12-rtx-3090-refurbished.md")
move_and_tag("NotebookLM_Workspaces/Desktop_Towers_Refurbished/26_acer-predator-orion-7000-rtx-4080-super.md",
             "NotebookLM_Workspaces/Desktop_Gaming_Refurbished/26_acer-predator-orion-7000-rtx-4080-super.md")

# CREATE NEW CARDS
def write_file(path, content):
    with open(os.path.join(base_dir, path), "w") as f:
        f.write(content)

write_file("NotebookLM_Workspaces/Gaming_Laptops_AMD_Discrete/hp_omen_max.md", """---
id: hp-omen-max-rtx-5090
category: laptop
architecture: discrete_gpu_amd
track_eligibility: track_1_nvidia_path
name: HP OMEN Max (Ryzen AI 9 HX 375 + RTX 5090)
gpu: NVIDIA RTX 5090
vram: 24 GB
---
# HP OMEN Max
Evaluate under Track 1 NVIDIA Path rules.
""")

write_file("NotebookLM_Workspaces/Laptops/asus-tuf-a14.md", """---
id: asus-tuf-a14
category: laptop
name: ASUS TUF Gaming A14 (2026) FA401EA
vram: 32 GB unified
---
# ASUS TUF Gaming A14
14" Strix Halo
""")

write_file("NotebookLM_Workspaces/Laptops/asus-proart-px13.md", """---
id: asus-proart-px13
category: laptop
name: ASUS ProArt PX13
vram: 128 GB unified
---
# ASUS ProArt PX13
13.3" Strix Halo
ONLY pursue if refurbished/open-box/sale pricing <=$4,500 AUD
""")

write_file("NotebookLM_Workspaces/Laptops/asus-rog-flow-z13.md", """---
id: asus-rog-flow-z13
category: laptop
name: ASUS ROG Flow Z13 GZ302EA
vram: UNKNOWN
---
# ASUS ROG Flow Z13
13.4" Strix Halo
""")

write_file("NotebookLM_Workspaces/Decision_System/track2_pathway_a_build_spec.md", """# Track 2 — Pathway A Build Spec

## Target Configuration

- **CPU:** Threadripper PRO 5955WX or 5975WX (WRX80 chipset)
- **Motherboard:** (specific model TBD, e.g. ASUS Pro WS WRX80E-SAGE)
- **RAM:** 128 GB DDR4 ECC (minimum)
- **PSU:** 1600W+ 80+ Platinum
- **Case:** (TBD — must fit dual 3-slot GPUs)
- **Primary GPU:** RTX 3090 × 2 (24 GB VRAM each)
""")

write_file("NotebookLM_Workspaces/Mini_PC_and_eGPU/hp_mini_pc_placeholder.md", """---
id: hp-mini-pc-placeholder
category: mini-pc
name: HP Workstation Mini PC
vram: UNKNOWN
---
# HP Workstation Mini PC
Placeholder for HP Z2 Mini G1a or Elite Mini 800 G11 AI (Strix Halo variant).
All fields UNKNOWN pending verification.
""")

