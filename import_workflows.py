#!/usr/bin/env python3
"""Import 'Workflows by use case' from the anonymized case-study notes into workflows.json.

    python3 import_workflows.py /path/to/ai_solutions.md
Each '#### Industry: use case' block becomes {"type": ..., "steps": [[ACTOR, text], ...]}."""
import json
import re
import sys
from pathlib import Path

STEP = re.compile(r"^\s*\d+[a-z]?\.\s*\[(\w+)\]\s*(.+?)\s*$")


def parse(md):
    section = md.split("### Workflows by use case", 1)
    if len(section) < 2:
        raise SystemExit("no 'Workflows by use case' section found")
    out, cur = {}, None
    for line in section[1].splitlines():
        if line.startswith("## ") or line.strip() == "---":
            break
        if line.startswith("#### "):
            cur = line[5:].split(":", 1)[-1].strip()
            out[cur] = {"type": "workflow", "steps": []}
        elif cur and line.lower().startswith("workflow type:"):
            out[cur]["type"] = line.split(":", 1)[1].strip()
        elif cur and (m := STEP.match(line)):
            out[cur]["steps"].append([m.group(1).upper(), m.group(2)])
    return out


def main(argv):
    if not argv:
        raise SystemExit(__doc__)
    data = parse(Path(argv[0]).read_text())
    dest = Path(__file__).parent / "workflows.json"
    dest.write_text(json.dumps(data, indent=1, ensure_ascii=False))
    print(f"{len(data)} workflows -> {dest}")


if __name__ == "__main__":
    main(sys.argv[1:])
