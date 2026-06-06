# 🦞 Hermes Skills Library

A community-maintained library of **Hermes Agent** skills, ported and curated from the
[OpenClaw](https://openclaw.ai) ecosystem.

> **Hermes Agent** is a locally-running AI assistant by [Nous Research](https://nousresearch.com).
> Skills are markdown files (`SKILL.md`) that teach the agent how to use external tools, APIs, and
> workflows. They live in `~/.hermes/skills/` (global) or `<project>/skills/` (workspace).

This repo indexes **5,378 OpenClaw skills** across 30 categories, tracking which ones have been
ported to work with Hermes and which are still pending.

---

## 📦 How to install a ported skill

```bash
# From this repo (after git clone):
cp -R ported-skills/<skill-name> ~/.hermes/skills/

# Or via the Hermes installer (coming soon):
hermes skills install <skill-name>
```

Hermes auto-discovers anything under `~/.hermes/skills/` — no restart needed.

---

## 🗂 Categories

| Category | Skills | Hermes ports | Status |
|----------|-------:|-------------:|--------|
| [AI & LLMs](categories/ai-and-llms.md) | 185 | 0 | ⬜ |
| [Apple Apps & Services](categories/apple-apps-and-services.md) | 44 | 0 | ⬜ |
| [Browser & Automation](categories/browser-and-automation.md) | 323 | 0 | ⬜ |
| [Calendar & Scheduling](categories/calendar-and-scheduling.md) | 66 | 0 | ⬜ |
| [Clawdbot Tools](categories/clawdbot-tools.md) | 37 | 0 | ⬜ |
| [CLI Utilities](categories/cli-utilities.md) | 179 | 0 | ⬜ |
| [Coding Agents & IDEs](categories/coding-agents-and-ides.md) | 1,202 | 0 | ⬜ |
| [Communication](categories/communication.md) | 146 | 0 | ⬜ |
| [Data & Analytics](categories/data-and-analytics.md) | 40 | 0 | ⬜ |
| [DevOps & Cloud](categories/devops-and-cloud.md) | 392 | 0 | ⬜ |
| [Gaming](categories/gaming.md) | 36 | 0 | ⬜ |
| [Git & GitHub](categories/git-and-github.md) | 159 | 0 | ⬜ |
| [Health & Fitness](categories/health-and-fitness.md) | 84 | 0 | ⬜ |
| [Image & Video Generation](categories/image-and-video-generation.md) | 172 | 0 | ⬜ |
| [iOS & macOS Development](categories/ios-and-macos-development.md) | 29 | 0 | ⬜ |
| [Marketing & Sales](categories/marketing-and-sales.md) | 104 | 0 | ⬜ |
| [Media & Streaming](categories/media-and-streaming.md) | 84 | 0 | ⬜ |
| [Moltbook](categories/moltbook.md) | 44 | 0 | ⬜ |
| [Notes & PKM](categories/notes-and-pkm.md) | 69 | 0 | ⬜ |
| [PDF & Documents](categories/pdf-and-documents.md) | 111 | 0 | ⬜ |
| [Personal Development](categories/personal-development.md) | 51 | 0 | ⬜ |
| [Productivity & Tasks](categories/productivity-and-tasks.md) | 206 | 0 | ⬜ |
| [Search & Research](categories/search-and-research.md) | 354 | 0 | ⬜ |
| [Security & Passwords](categories/security-and-passwords.md) | 54 | 0 | ⬜ |
| [Self-Hosted & Automation](categories/self-hosted-and-automation.md) | 32 | 0 | ⬜ |
| [Shopping & E-commerce](categories/shopping-and-e-commerce.md) | 51 | 0 | ⬜ |
| [Smart Home & IoT](categories/smart-home-and-iot.md) | 43 | 0 | ⬜ |
| [Speech & Transcription](categories/speech-and-transcription.md) | 46 | 0 | ⬜ |
| [Transportation](categories/transportation.md) | 110 | 0 | ⬜ |
| [Web & Frontend Development](categories/web-and-frontend-development.md) | 925 | 0 | ⬜ |
| **TOTAL** | **5,378** | **0** | **0%** |

---

## 🔄 Porting a skill

OpenClaw skills use the same `SKILL.md` frontmatter convention as Hermes, but their runtime
assumes the `openclaw` CLI. Porting a skill usually means:

1. **Fetch the original** — find the source repo from the skill's `clawskills.sh` page
2. **Read SKILL.md** — understand the workflow it describes
3. **Rewrite tool calls** — replace `openclaw ...` with `hermes ...` or the equivalent native tool
4. **Update frontmatter** — change `name`/`description` so Hermes's skill discovery picks it up
5. **Test** — drop it into `~/.hermes/skills/` and verify the agent picks it up
6. **Add `port-status: ✅ ported` to the category index** so others can find it

Template for a ported skill: see [`ported-skills/_template/SKILL.md`](ported-skills/_template/SKILL.md).

### Hermes-native equivalent for common OpenClaw tools

| OpenClaw | Hermes equivalent |
|----------|-------------------|
| `openclaw skills install` | copy to `~/.hermes/skills/` |
| `openclaw onboard --auth-choice X` | `hermes config set X` |
| `claude-code`/`codex` sub-agents | `delegate_task` (subagent) |
| Composio OAuth bridge | `native-mcp` skill |

---

## 🤝 Contributing

**Pick a skill from any category table**, mark it with a ✅ in a PR, and submit the ported
`SKILL.md` under `ported-skills/<skill-name>/`.

- ✅ = ported and tested with Hermes ≥ 0.5
- 🟡 = ported but partially working
- ⬜ = not started

---

## ⚠️ Security

> Skills in the OpenClaw ecosystem are **curated, not audited**. They can include prompt
> injections, hidden payloads, or unsafe data handling. Always review the source code
> before installing.

Recommended tools: [Snyk agent-scan](https://github.com/snyk/agent-scan).

---

## 📜 Credits

- Skill index: [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) (MIT)
- Registry: [openclaw/clawhub](https://github.com/openclaw/clawhub)
- Hermes Agent: [Nous Research](https://nousresearch.com)
