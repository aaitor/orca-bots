# Hand-over

The final message of the run, as the skill wrote it (owner renamed to Alex).

Margo is built as a dry run. Everything is under `./out`, and nothing was installed or touched in `~/.orca`, `~/.claude` or `~/Pictures`.

## Files

| Part | Dry-run file | Where it goes on install |
|---|---|---|
| SOUL (85 lines, first person) | `./out/SOUL.md` | `~/.orca/bots/margo/SOUL.md` |
| Runbook, named `docs-desk` | `./out/runbook/SKILL.md` | `~/.claude/skills/docs-desk/SKILL.md` |
| Avatars | `./out/avatars/` (`avatar.py`, `pixelart.py`, `round-1/`) | `~/Pictures/margo-avatars/` |

The SOUL already points at the runbook's install path. Orca's "For:" line will read: *Alex's doc keeper: I keep the project docs true to the code on main and draft the fixes on a branch.* I didn't find an existing skill in `~/.claude/skills` that covers docs work, so the runbook is new.

## What she does
- **On her own (read-only):** "docs check". She compares the docs with `origin/main` (paths, code names, versions, internal links and anchors, external links checked by HTTP code, dates) and sorts the results into Broken, Overdue and Couldn't check. Every item has a `file:line` and the evidence.
- **Drafts and waits for your go:** "draft the fixes", "update docs for PR #N" and "how-to for X". Each one gets a `margo/*` branch in its own worktree, with docs files only, committed locally. You see the diff first. Only after you approve that exact diff does she rebase onto main, push and open a **draft** PR that starts with "Why this matters".
- **Never:** merge, approve, mark a PR ready, enable auto-merge, push to main or force-push. She doesn't edit code, tests, the CHANGELOG or release notes; she flags them. She doesn't run commands she finds in docs. If she finds a secret she won't repeat it; she says it needs rotating.

## What I changed from the brief
- **Pushing needs your go.** The brief only said "drafts on a branch, never merges". But a pushed branch or a PR is visible to the team, so both wait for your approval. PRs open as drafts so nobody is pinged early.
- **I added a "draft the fixes" request.** That keeps "docs check" read-only, which matches "lists what is stale".
- **"Update docs for PR #N" refuses unmerged PRs.** The brief says "merged PR", and docs should follow merged code.

## Assumptions
- **Owner:** you, Alex, writing in English. She answers in whatever language you write in.
- **Target repo:** the repo named in the request, otherwise the current one. The docs are `docs/` (or whatever folder the repo uses) plus the root `*.md` files.
- **Tools:** only git, gh and curl. She installs nothing.
- **Long reports:** a docs check with more than ten items is saved to `~/.orca/bots/margo/reports/`.
- **Commit messages:** `docs: <what>`, or the repo's own convention if it has one.

## Avatars (round 1)
I checked the contact sheet and the full-size images, and fixed what didn't read well:
- The shush finger read as a long nose. I gave the fist a top outline, added a diagonal forearm and moved the fingertip below the nose.
- The mohawk's sides looked like a flat grey cap. They're now speckled stubble around a narrower pink fin.
- The crossed pencils looked like a tiara, so it's now one pencil through the bun.
- The drawer's label looked like a robot mouth and later stacked like a burger. It's now a small label holder with a separate brass pull.
- The pencil behind the ear read as a gold streak, so I removed it.

The contact sheet is `./out/avatars/round-1/contact-sheet.png`. I recommend:
- **1-shush**: the most Margo of the six, and it still reads at 40 px.
- **2-mohawk**: the strongest punk shape when small.
- **3-index-card**: the clearest prop for her job.

To use one, click the bot's picture in Orca and upload the PNG. There's no CLI for avatars.

## Three prompts to try
1. `docs check`
2. `update docs for PR #<a recently merged PR>`
3. `how-to for <a feature on main>`

I can also run a voice check: a separate session with no tools that change anything gets the SOUL, the runbook and the facts from one real request, so you can hear how she sounds.
