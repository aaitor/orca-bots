# Usage

## Ask for a bot

Talk to your agent in plain words. The skill picks up requests like:

- "Create an Orca bot that …"
- "Write the SOUL for my bot Paco"
- "My bot ignores its personality, fix it"
- "Make avatar options for Charo" / "More variations of 2b"

A complete brief:

```text
Create an Orca bot called Ingrid, the Inspector. "check staging" runs our smoke tests against
staging and tells me what broke; "triage <issue>" reads the issue, reproduces it and labels it.
She can run tests and read logs, but she never touches production and never closes an issue.
She's a former Swedish safety inspector: calm, thorough, unimpressed by excuses, quietly funny,
knits during long test runs. Make her some avatars.
```

## What happens

The skill asks at most three questions, then writes the runbook, the SOUL and round-1 avatars, and
ends with a hand-over. The steps are in [How it works](../README.md#how-it-works); a real hand-over
is in [Margo's example](../skills/orca-bot-builder/examples/margo-the-doc-keeper/handover.md).

**New bot?** Make your first message in its chat "Your SOUL.md is final, keep it as it is."
Orca's first-run setup otherwise rewrites the SOUL on that first message.

## Avatar rounds

- **Round 1** is four to eight different concepts: a plain portrait, the persona's signature
  prop, and one or two ideas that break the frame.
- **Pick one, then ask for variations.** "Variations of 3" gets faces, looks, props and
  backgrounds changed one at a time, in groups you can compare. Use the codes in the file names:
  "2h but with the beard from 2e".
- **Ask for anything concrete**: older, fatter, angrier, a different shirt, a cat, sunglasses, a
  different background colour. Clothes should fit the persona; say so if they don't.
- **Upload** the one you like: click the bot's picture in Orca and choose the PNG.

Every bot keeps `~/Pictures/<slug>-avatars/avatar.py`, so you can come back months later and ask
for a winter hat.

## Voice check

After the SOUL is installed, ask for a voice check: a separate session gets the SOUL, the runbook
and the facts from one real request, with no tools that change anything, and writes the reply the
bot would give. It is the fastest way to see whether the personality survives a real report.

## Changing a bot later

- **Personality**: ask the skill to edit the SOUL ("make Paco less grumpy in reports"), then start
  a new Home Chat (`orca bot new-chat --bot "<Name>"`): an open chat keeps the SOUL it started with.
- **Job**: ask it to update the runbook. Keep the SOUL's Never list and the runbook's rules in step.
- **By hand**: `SOUL.md` is yours to edit. Keep the purpose line right under the title.

## Privacy and safety

- Building a bot never publishes, sends or contacts anything.
- Credentials are referred to by path or variable name, never copied into the SOUL or runbook.
- Briefs that ask for something a bot should not do, such as collecting people's private data,
  get the closest safe version, and the skill tells you once. The
  [Richard example](../skills/orca-bot-builder/examples/richard-the-dealmaker/) shows one.
