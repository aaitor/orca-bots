# Changelog

## 1.0.2 (2026-11-21)

- A Claude-based bot's chat keeps the SOUL it started with, and a new bot's Home Chat starts with
  Orca's placeholder. Installing or changing a SOUL now ends with `orca bot new-chat --bot "<Name>"`.
  The docs used to say the next message was enough.
- New "Plugins and hooks" section: turn off user-level plugins that inject another persona or
  process at session start, per bot, in `<bot home>/.claude/settings.local.json`.

## 1.0.1 (2026-11-21)

From Sami's review:

- Warn about Orca's first-run setup, which rewrites a new bot's SOUL on its first answered message.
- Purpose line: one sentence under about 110 characters; `orca bot list` cuts the rest.
- The runbook no longer guesses the bot's folder: `<bot home>` until the bot exists.
- `behind()` now paints scanline rows too, so props behind the head aren't dotted after `shift_left()`.
- One-step install: `claude plugin install orca-bot-builder --marketplace aaitor/orca-bots`.
- Margo's example: exact brief in the Quick start, the run's hand-over added, honest about context.
- Charo and La Chani examples: personal-looking lines made generic.
- Less duplication between SKILL.md, the Orca guide and the docs.

## 1.0.0 (2026-11-21)

First public release.

- `orca-bot-builder` skill: from a brief to a SOUL.md, a runbook skill and arcade avatar options.
- Guides for writing SOULs, runbooks and avatars, and the Orca facts a bot builder needs.
- Templates: `SOUL.md`, `RUNBOOK.md` and a starter `avatar.py` with skin and hair palettes.
- `pixelart.py` helpers, including `behind()`, `save()` and `html_page()` for Orca inline visuals.
- Five worked examples (Paco, Sami, La Chani, Charo, Richard) with briefs, SOULs, avatar scripts,
  round contact sheets and the chosen avatars, plus Margo, built by the skill in one unedited run,
  runbook included.
- Claude Code plugin and marketplace manifests.
- CI: documentation links, manifests and pixel-exact redraws of the example avatars.
