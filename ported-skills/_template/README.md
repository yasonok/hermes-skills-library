# Skill porting template

Copy this directory to `ported-skills/<your-skill-slug>/SKILL.md` and fill in the
frontmatter + body. Strip this README before publishing.

## Structure

```
ported-skills/
└── <skill-slug>/
    ├── SKILL.md           # required
    ├── scripts/           # optional: helper shell scripts
    ├── references/        # optional: API docs, cheat sheets
    └── assets/            # optional: templates, images
```

## Frontmatter

```yaml
---
name: my-skill
description: One-sentence summary. Triggered when user asks to ...
metadata:
  hermes:
    version: "1.0"
    ported_from: clawskills.sh/skills/<original-slug>
    tested_with: hermes 0.5+
    tools: [terminal, web_search]   # which Hermes toolsets the skill needs
---
```

## Body

Use markdown. Sections that work well:
- **When to use** — clear trigger phrases
- **Prerequisites** — env vars, installed CLIs, accounts
- **Workflow** — numbered steps with concrete commands
- **Pitfalls** — what goes wrong, how to recover
- **Verification** — how to confirm it worked

See [Hermes skill docs](https://hermes-agent.nousresearch.com/docs) for the full spec.
