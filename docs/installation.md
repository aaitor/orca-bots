# Installation

## Requirements

- [Orca](https://github.com/stablyai/orca) 1.4 or later, to run the bots.
- An agent that loads Agent Skills. Tested with Claude Code.
- Python 3.9+ and [Pillow](https://pypi.org/project/pillow/) for the avatars: `pip install pillow`.
  The agent runs the avatar scripts; nothing else needs installing.

The skill only writes local files. It needs no API keys, accounts or network access of its own.

## Claude Code plugin

```text
/plugin install orca-bot-builder --marketplace aaitor/orca-bots
```

On older Claude Code versions, add the marketplace first:

```text
/plugin marketplace add aaitor/orca-bots
/plugin install orca-bot-builder@orca-bots
```

Update later with `claude plugin update orca-bot-builder`.

## Skill folder

Clone the repository and link the skill into your skills directory:

```bash
git clone https://github.com/aaitor/orca-bots.git
ln -s "$PWD/orca-bots/skills/orca-bot-builder" ~/.claude/skills/orca-bot-builder
```

`git pull` in the clone updates it. To keep a copy instead of a link, use `cp -r`.

## Other agents

The skill is a plain folder: `SKILL.md`, guides, templates and a Python helper. Agent Skills
clients other than Claude Code (Codex, for example) can load the same folder from their own skills
directory. Orca bots running on Codex work too, because a bot reads its runbook by path.

## Check it works

Ask your agent:

```text
Use the orca-bot-builder skill to draw round-1 avatar concepts for a bot called Test,
a cheerful lighthouse keeper. Don't install anything.
```

You should get a contact sheet under `~/Pictures/test-avatars/round-1/`.

## What the skill writes, and where

| File | Default location | Change it by |
|---|---|---|
| SOUL | `~/.orca/bots/<slug>/SOUL.md` | Fixed by Orca |
| Runbook | `~/.claude/skills/<desk>/SKILL.md` | Asking for another path in the brief |
| Avatars | `~/Pictures/<slug>-avatars/` | Asking for another folder in the brief |

It never edits `AGENTS.md`, `CLAUDE.md` or `bot.json` in a bot's folder; Orca owns those.
