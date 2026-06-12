import json
import glob
import os

conversations = [
    "f8770ee0-b499-4851-ac0d-9be5d43606f1",
    "f1e898e6-8f32-467a-bade-991bf9dd27c2",
    "7eb65a68-f596-4182-b179-20c903d9245b",
    "a944dc08-7d27-4ede-821f-5c782fd36df1",
    "fdf4bebb-54da-4d9f-8a56-4208471a7377"
]

base_dir = "/Users/okgoogle13/.gemini/antigravity-ide/brain/"
output_file = "/Users/okgoogle13/Projects/Computer purchase/scratch/model_responses.txt"

with open(output_file, 'w') as out:
    for conv in conversations:
        path = os.path.join(base_dir, conv, ".system_generated/logs/transcript.jsonl")
        if not os.path.exists(path):
            continue
            
        out.write(f"=== Conversation {conv} ===\n")
        with open(path, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data.get("source") == "MODEL" and data.get("type") in ("PLANNER_RESPONSE", "CHAT_RESPONSE"):
                        content = data.get("content", "")
                        if "pipeline" in content.lower() or "flaw" in content.lower() or "fail" in content.lower() or "fix" in content.lower() or "diagnos" in content.lower():
                            out.write(content + "\n")
                            out.write("-" * 80 + "\n")
                except Exception:
                    pass
        out.write("\n\n")

print(f"Extraction complete. Wrote to {output_file}")
