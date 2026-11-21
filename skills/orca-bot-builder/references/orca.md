# Orca facts for bot builders

Checked against Orca 1.4. If a command here fails, run `<orca> bot --help` and trust that.

## The CLI

SKILL.md step 4 says which executable to use. Inside a SOUL or runbook, write
`${ORCA_CLI_COMMAND:-orca}` so it works from any bot.

## A bot's home

```
~/.orca/bots/<slug>/
  SOUL.md      who the bot is: owned by the owner, written by this skill
  MEMORY.md    the bot's memory index, one line per fact; details in memory/<topic>.md
  memory/
  AGENTS.md    written by Orca: "You are <Name>, a bot that runs in Orca…"
  CLAUDE.md    written by Orca: "@AGENTS.md"
  bot.json     written by Orca: id, name, agent (claude or codex), avatar, members
  avatar.png   the uploaded picture
```

Orca rewrites `AGENTS.md`, `CLAUDE.md` and `bot.json`; edits to them are lost. Everything the bot
should know about itself goes in `SOUL.md`; everything about the job goes in the runbook.

What a bot is for is the first paragraph of its `SOUL.md`. `orca bot list` shows it as **For:**
(`specialty` in `--json`), cut at about 117 characters, and other agents see it when they look for
a bot to ask. Keep it to one sentence under about 110 characters.

## Creating the bot

SKILL.md step 4 covers the two ways (the Orca app, or `orca bot create --offer` from a bot's chat).
What it doesn't say:

- The folder slug comes from the name at creation (`Sami (the Architect)` → `sami-the-architect`).
  Renaming the bot later does not move the folder.
- `orca bot create --offer` fails with "Run this from a bot's chat" anywhere else; the bot exists
  only after the owner presses **Create bot**.
- **First-run setup.** A new bot's first answered message runs Orca's first-run setup, which tells
  the bot to write `SOUL.md` from what it knows, keeping only a `## Never` section. That would
  replace the SOUL this skill installed. Tell the owner to make the first message "Your SOUL.md is
  final, keep it as it is."

## When a SOUL change takes effect

Orca sends the current `SOUL.md` with the next message to the bot. A reply that was already running
used the old one. No new chat is needed.

## Tools and accounts

- `orca bot tools` lists a bot's own MCP servers and the ones it inherits from Claude Code or Codex;
  `orca bot tools add` gives it one of its own.
- `orca bot connectors` shows, per service, which tool to use, who it acts as and whether it is
  signed in.
- Skills under `~/.claude/skills/` are available to Claude-based bots. The SOUL points at the
  runbook by path, so a Codex-based bot can read it too.

## Avatars

There is no CLI for avatars. The owner clicks the bot's picture in Orca and uploads a PNG (Orca
shows it small and round). The 512 x 512 PNGs this skill makes are 5 to 10 KB.

## Showing pictures in an Orca chat

When `ORCA_CHAT_SCRATCH_DIR` is set, Orca can show an HTML page inline. Write a self-contained HTML
file there (images as `data:` URLs, under 512 KB, a new file name each time) and put this on its
own line in the reply:

```
::orca-visual{file="<name>.html" title="<title>"}
```

`file` is the bare file name, not a path. Outside Orca, give the PNG paths instead.
