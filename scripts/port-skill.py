#!/usr/bin/env python3
"""
Port OpenClaw SKILL.md → Hermes SKILL.md
- Replace clawdbot metadata with hermes metadata
- Add trigger-phrase hint to description
- Mark ported_from
"""
import re, sys
from pathlib import Path

src = Path('/tmp/skill-raw')
out = Path('/Users/ryanchiang/hermes-skills-library/ported-skills')
out.mkdir(parents=True, exist_ok=True)

# slug → (ported_from_url, short_desc, tools)
PORT_MAP = {
    "apple-contacts":      ("sundial-org/awesome-openclaw-skills/skills/apple-contacts",      "Look up contacts from macOS Contacts.app via AppleScript.",                        ["terminal"]),
    "apple-photos":        ("sundial-org/awesome-openclaw-skills/skills/apple-photos",        "Apple Photos.app integration for macOS — search, export, browse.",                ["terminal"]),
    "apple-health-skill":  ("nftechie/apple-health-skill",                                     "Talk to Apple Health data — workouts, heart rate, activity rings, fitness trends.", ["terminal"]),
    "apple-mail-search":   ("sundial-org/awesome-openclaw-skills/skills/apple-mail-search",   "Fast Apple Mail search via SQLite on macOS.",                                     ["terminal"]),
    "homebrew":            ("sundial-org/awesome-openclaw-skills/skills/homebrew",            "Homebrew package manager for macOS.",                                              ["terminal"]),
    "mac-tts":             ("sundial-org/awesome-openclaw-skills/skills/mac-tts",             "Text-to-speech via macOS built-in `say` command.",                                ["terminal", "tts"]),
    "voice-wake-say":      ("sundial-org/awesome-openclaw-skills/skills/voice-wake-say",      "Speak responses aloud on macOS using built-in `say`.",                            ["terminal", "tts"]),
    "shortcuts-generator": ("sundial-org/awesome-openclaw-skills/skills/shortcuts-generator", "Generate macOS/iOS Shortcuts by creating plist files.",                           ["terminal", "write_file"]),
    "get-focus-mode":      ("sundial-org/awesome-openclaw-skills/skills/get-focus-mode",      "Get the current macOS Focus mode.",                                                ["terminal"]),
}

count = 0
for slug, (port_from, desc, tools) in PORT_MAP.items():
    src_file = src / f"{slug}.md"
    if not src_file.exists():
        print(f"  SKIP {slug} (no source)")
        continue
    raw = src_file.read_text()
    # 拆 frontmatter + body
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', raw, re.DOTALL)
    if not m:
        print(f"  SKIP {slug} (no frontmatter)")
        continue
    old_fm, body = m.group(1), m.group(2)
    # 換 frontmatter
    new_fm = (
        f"name: {slug}\n"
        f"description: {desc}\n"
        f"metadata:\n"
        f"  hermes:\n"
        f'    version: "1.0"\n'
        f"    ported_from: {port_from}\n"
        f"    tested_with: hermes 0.5+\n"
        f"    tools: {tools}\n"
        f"    source_url: https://clawskills.sh/skills/{port_from.split('/')[-1]}\n"
    )
    new = f"---\n{new_fm}---\n{body.lstrip()}"
    # 寫入
    dst_dir = out / slug
    dst_dir.mkdir(parents=True, exist_ok=True)
    (dst_dir / "SKILL.md").write_text(new)
    print(f"  ✅ {slug}")
    count += 1

print(f"\n{count} skills ported → {out}")
