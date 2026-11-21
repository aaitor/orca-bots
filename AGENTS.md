# Working on this repository

The product is the skill in `skills/orca-bot-builder/`. Keep `SKILL.md` short and move detail into
`references/`; the agent loads those only when needed.

- **Examples are real.** Each `examples/<bot>/avatar.py` must redraw that bot's chosen
  `avatar.png` pixel for pixel. `python3 scripts/check.py` verifies it; run it after touching
  `scripts/pixelart.py` or an example. Never change an existing helper's behaviour; add new ones.
- **Commit only contact sheets and the chosen avatar.** Individual round PNGs are regenerated and
  ignored by git.
- **No private data.** Example SOULs use "Alex" for the owner and "Acme" for the company. No real
  emails, paths, credentials or internal systems in examples, docs or tests.
- **Writing.** Plain, concise English. Name the reader's task first. No invented features: every
  claim about Orca is checked against its CLI (`orca bot --help`).
- **README demo.** The avatar contact sheets are the demo. A terminal recording, if added, follows
  the shared format in aaitor/oss-repo-template: real Claude Code, black background, stop at the
  hand-over.
