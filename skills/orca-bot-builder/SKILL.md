---
name: orca-bot-builder
description: >-
  Use when someone wants a new Orca bot, or wants to give an existing one a personality, a runbook or a
  face: "create a bot that does X", "make me an Orca bot for Y with this personality", "write the SOUL
  for my bot", "my bot ignores its personality", "make avatar options for my bot", "more avatar
  variations". Turns a short brief (the tasks plus the personality) into the whole bot: a SOUL.md
  with a voice and guardrails, a runbook skill the bot follows step by step, and arcade pixel-art
  avatar options to pick from.
---

# Orca bot builder

An Orca bot is an agent with a home folder (`~/.orca/bots/<slug>/`) and a `SOUL.md` that says who it
is. A bot that feels like a teammate has three parts, and this skill builds all of them:

| Part | What it decides | Where it goes |
|---|---|---|
| **SOUL.md** | Who the bot is, how it sounds, what it never does | `~/.orca/bots/<slug>/SOUL.md` |
| **Runbook** | What it does for each request, step by step, and which facts it reports | `~/.claude/skills/<runbook>/SKILL.md` |
| **Avatar** | Its face: arcade pixel-art options, then variations of the pick | `~/Pictures/<slug>-avatars/` |

`<skill>` below means this skill's folder (the one this file is in).

## 0. Read the brief

The owner gives the tasks and the personality, in any words. Pull out:

- **Name and role**: "Paco, the Releaser". The role is the job in two words.
- **Requests**: three to six phrasings the owner will type ("release minor", "brief me", "review PR #N").
- **Sources and tools**: the repos, docs, accounts, MCP servers and existing skills the job needs.
- **Autonomy**: what it does alone, and what it only drafts for approval. Anything that publishes,
  sends, spends money, touches production or contacts people needs the owner's go each time.
- **Personality**: age, background, quirks, tastes, how it talks, what it jokes about.
- **The owner's name and language**, so the bot can address them and answer in their language.

Ask at most three questions, and only about what would change the result. Default the rest and
say what you assumed. If the owner points at past sessions or existing skills as examples, read
them: corrections the owner made there are the most valuable input you will get.

If the brief asks for something the bot should not do (collect private personal data, act in the
owner's name without approval, deceive people), build the closest safe version and say so plainly,
once. Example: "find the decision makers" becomes work contacts only, never personal phones, home
addresses or body details.

## 1. Research the job

- What exists already: `ls ~/.claude/skills`, the repo's docs, `orca bot list`, `orca bot tools`,
  `orca bot connectors`. Reuse an existing skill or tool before writing a new one.
- The source of truth for every fact the bot will state (a README, docs, code, a config file). The
  runbook makes the bot re-read it each time, never answer from memory.
- Credentials the job needs: refer to them by file path or variable name only. Never read their
  values into the chat, the SOUL or the runbook.

## 2. Write the runbook (what the bot does)

Read `references/runbook.md` and start from `templates/RUNBOOK.md`. One section per request type,
the sources of truth, what needs approval, and the rules. Its report section must say **"write
the report in your SOUL.md voice, from the first line to the last, without changing any fact"**,
or the runbook's format wins and the personality disappears.

Skip this step when one existing skill already covers the job; the SOUL points at it instead.

Paths into the bot's home folder (reports, drafts) use the folder found in step 4. Orca names it
from the bot's full name, so don't guess it: until the bot exists, write `<bot home>` and fill it
in when you install.

## 3. Write the SOUL (how the bot sounds)

Read `references/soul.md` and start from `templates/SOUL.md`. The rules that matter most:

- **First person.** "I racked servers before the CMO was born", not "He is a 60-year-old sysadmin".
  A description gives the model facts; a voice gives it something to copy.
- **The paragraph under the title is the purpose**: one sentence, under about 110 characters.
  Orca shows it as the bot's "For:" line and cuts the rest.
- **Who wins**: "The runbook decides what I do and which facts I report. This file decides how I sound."
- **I'm in every line**, not only the first and the last.
- **Seven to ten example lines** ("How I sound"). They shape the tone more than any description.
- **A serious mode** for high stakes (production, money, health, deadlines): the jokes stop.
- **What others see stays clean**: posts, emails, PR comments and client pages never carry the persona.
- **The voice never bends the facts.** Numbers, versions, dates and results stay exact.
- **Never** list, then **Purpose**: "Before acting on any request, read <runbook> and follow it."

## 4. Install it in Orca

Read `references/orca.md` for the folder layout, first-run setup and tools. The steps:

1. Find the CLI: `$ORCA_CLI_COMMAND` if set, else `orca`. On Linux outside an Orca terminal use
   `orca-ide`: bare `orca` there is the GNOME screen reader.
2. `orca bot list --json` lists the bots by name. A bot's folder is the one whose `bot.json` has
   that name: `grep -l '"name": "<Name>' ~/.orca/bots/*/bot.json`. If the bot exists, read its
   `SOUL.md` first and keep anything the owner wrote by hand. If it does not, ask the owner to
   create it in Orca with the name and the purpose line. Inside a bot's chat, `orca bot create
   --offer --name "<Name>" --purpose "<purpose line>"` puts a creation card in the chat instead.
3. Write `SOUL.md` and the runbook. Never edit `AGENTS.md`, `CLAUDE.md` or `bot.json`: Orca rewrites them.
4. Check that `orca bot list` shows the new "For:" line. Orca sends the new SOUL with the next message;
   no new chat is needed.

## 5. Draw the avatar options

Read `references/avatars.md` and look at the closest example in `examples/`. Then:

1. Pull three or four visual cues from the SOUL: age, job, mood, era, clothes, props.
2. Set up the folder and draw round 1, four to eight **different concepts**:
   ```bash
   D=~/Pictures/<slug>-avatars; mkdir -p "$D"
   cp <skill>/templates/avatar.py <skill>/scripts/pixelart.py "$D/"
   # edit $D/avatar.py: LEFT, palette, helpers, CONCEPTS
   python3 "$D/avatar.py"            # -> $D/round-1/*.png + contact-sheet.png
   ```
3. **Look before you show**: read the contact sheet and one full-size PNG, and fix what reads wrong
   (a face that looks like an animal, a prop that vanishes at 40px, a prop over the head).
4. Show the contact sheet (see "Showing pictures" in `references/avatars.md`), recommend two or
   three, and ask which one to vary.
5. Round 2 and later: variations of the pick, **one axis at a time** (face, look, prop, background).
6. The owner uploads the pick in Orca by clicking the bot's picture. There is no CLI for avatars.

The avatar only needs a SOUL draft, so it can be drawn while the owner reads the SOUL and the runbook.

## 6. Hand it over

Tell the owner, briefly and in plain words:

- what was created, with paths: SOUL, runbook, avatar folder;
- what the bot does alone, what it drafts for approval, and what it never does;
- anything you reshaped from the brief, and why;
- three prompts to try in the bot's chat;
- the avatars you recommend, and how to upload one;
- for a new bot: make the first message in its chat "Your SOUL.md is final, keep it as it is."
  A new bot's first answered message runs Orca's first-run setup, which rewrites `SOUL.md`.

Offer a **voice check**: give a separate session the SOUL, the runbook and the facts from one real
request, with no tools that change anything, and show the owner how the bot sounds.

## Rules

- Building a bot changes local files only. Never publish, send, post or contact anyone while doing it.
- No secrets in the SOUL, the runbook, the avatar folder or the chat. Paths and variable names only.
- The owner's private details (health, family, addresses, credentials) never go into anything public.
- Read a file before you replace it, and show the owner what changed in a file they wrote.
- Don't invent the owner's tools or facts. If the job needs something that doesn't exist, say so.
