# Troubleshooting

## The bot ignores its personality

The most common problem, and it usually has one of four causes:

1. **The reply came from the old SOUL.** Orca sends the updated `SOUL.md` with the next message. A
   reply that was already running used the previous version. Send another message.
2. **The SOUL describes the bot in the third person** ("He is a 60-year-old sysadmin"). Rewrite it
   as "I". A description gives the model facts; a voice gives it something to copy.
3. **The runbook wins.** A runbook that says "follow exactly" and shows a plain report template
   beats the SOUL. Add to its report section: "Write the report in your SOUL.md voice, from the
   first line to the last, without changing any fact."
4. **No example lines for that situation.** Add two or three "How I sound" lines for the exact
   moment that came out flat (a test report, a failure, a hand-over).

Ask the skill: "Paco's last report had no personality, fix it." It checks all four.

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
