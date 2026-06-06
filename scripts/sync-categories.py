#!/usr/bin/env python3
"""
Sync category indexes from VoltAgent/awesome-openclaw-skills into this repo.

Usage:
    python3 scripts/sync-categories.py /path/to/aos/categories/ ./categories/
"""
import re, sys
from pathlib import Path

if len(sys.argv) != 3:
    print(__doc__)
    sys.exit(1)

src = Path(sys.argv[1])
out = Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)

total = 0
for md in sorted(src.glob('*.md')):
    text = md.read_text()
    rows = re.findall(r'^- \[([^\]]+)\]\((https?://clawskills\.sh/skills/[^)]+)\) - (.*)$', text, re.MULTILINE)
    count_m = re.search(r'\*\*(\d+) skills\*\*', text)
    count = int(count_m.group(1)) if count_m else len(rows)
    total += count
    lines = [
        f"# {md.stem.replace('-', ' ').title()}",
        "",
        f"**{count} skills** (source: [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills))",
        "",
        "| # | Skill | Description | Hermes port |",
        "|---|-------|-------------|-------------|",
    ]
    for i, (name, url, desc) in enumerate(rows, 1):
        desc_safe = desc.replace('|', '\\|')
        lines.append(f"| {i} | [{name}]({url}) | {desc_safe} | ⬜ |")
    (out / md.name).write_text("\n".join(lines) + "\n")
    print(f"  {md.stem:40s} {count:5d}")

print(f"\nTOTAL: {total} skills")
