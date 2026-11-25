# Verified count: 116 characters (116 UTF-8 bytes).
LINE = "The GPS swears this is a shortcut. We have passed the same cow three times, and the cow is starting to recognize us."

import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(len(LINE))
