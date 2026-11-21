# Troubleshooting

## The bot ignores its personality

Most often the chat runs on an old SOUL: a Claude-based bot's chat keeps the SOUL it started with,
and a new bot's Home Chat starts with Orca's placeholder. Run `orca bot new-chat --bot "<Name>"`.
Next, user-level plugins that inject another persona at session start; turn them off for the bot
([Plugins and hooks](../skills/orca-bot-builder/references/orca.md#plugins-and-hooks)). After that:
the SOUL describes the bot in the third person, the runbook's report format wins, or there are no
example lines for that situation. Flat only in short replies or on serious topics: the SOUL needs
"I'm in every message" and a serious mode scoped to one item. The fixes are in
[the SOUL guide](../skills/orca-bot-builder/references/soul.md#when-the-owner-says-it-ignores-the-personality).
Ask the skill: "Paco's last report had no personality, fix it." It checks all of them.

## The SOUL changed after the bot's first message

Orca's first-run setup ran: a new bot's first answered message rewrites `SOUL.md`, keeping only
`## Never`. Ask the skill to reinstall the SOUL, then send "Your SOUL.md is final, keep it as it is."

## The personality leaks into published work

The SOUL needs a "What others see" section, and the runbook a matching rule: posts, PRs, emails and
client pages are written for their reader, in the right voice, with none of the bot's slang or
stories. For bots that write as you, say that the draft goes in its own block.

## `orca` starts a screen reader

On Linux, outside an Orca terminal, `orca` is often the GNOME screen reader. Use `orca-ide`, or
`$ORCA_CLI_COMMAND` when Orca sets it. Inside SOULs and runbooks, write `${ORCA_CLI_COMMAND:-orca}`.

## "Run this from a bot's chat"

`orca bot create --offer` only works inside a bot's chat. Anywhere else, create the bot in the Orca
app with its name and purpose, then ask the skill to install the SOUL.

## The bot's folder has a different name

The folder slug comes from the name the bot had when it was created. Renaming the bot later does not
move it. Find it by name: `grep -l '"name": "<Name>' ~/.orca/bots/*/bot.json`.

## Avatar problems

| Looks wrong | Fix |
|---|---|
| The face reads as an animal | It is one flat colour. Use skin plus an outline. |
| Nothing reads at 40 px | Heavier brows, a bigger signature prop with an outline and a highlight. |
| The face blends into the background | Change the background tone; light skin needs a mid-tone, dark skin a lighter or more saturated one. |
| A prop is painted over the head | Draw it with `behind()`, or `shift_left()` first to free the right edge. |
| A beard looks like noise | Sparse speckles on a base colour, not a checkerboard. |
| `ModuleNotFoundError: pixelart` | Copy `scripts/pixelart.py` next to the bot's `avatar.py`. |
| `ModuleNotFoundError: PIL` | `pip install pillow` |

More in the [avatar guide](../skills/orca-bot-builder/references/avatars.md).

## Uploading the avatar

There is no CLI for it. Click the bot's picture in Orca and pick the PNG from
`~/Pictures/<slug>-avatars/round-N/`.
