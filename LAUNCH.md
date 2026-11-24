# Launching the team

This is the presenter/harness guide. It is the only document besides the demo script that names
Parle. **Agents never see it**; their contracts speak of "the room and message channel your harness
provides".

The point of this file: each role runs as its **own agent session**, in its **own working
directory**, with its **own room identity**. That is what makes the role boundaries real instead of
a paragraph of good intentions.

## What you need

- An agent harness you can run several sessions in (Command Code, Codex, Claude Code, …).
- A Parle account with a linked agent per session.
- This repo checked out locally.

## 1. Pick the event

`events/<event>/manifest.json` gives you the room and the `seated` list:

```json
{ "room": "dinner-2026-11-28",
  "seated": ["planner", "chef", "procurement", "finance", "scheduler", "guest-manager"] }
```

Launch one session per entry in `seated`. Nothing else is needed to change the occasion.

## 2. Create the room

Create one Parle room named after `room` and seat each session's agent in it. A dedicated room per
event keeps the message history as the team's shared record. Put the objective and the seated roles
in the room instructions so a late joiner can tell which team it is.

## 3. Start each session

Launch a session with its **working directory set to the role folder** and give it this prompt:

> Read `AGENTS.md`, `ROLE.md` and `README.md` in this folder, then `../AGENTS.md`,
> `../organization.md` and `../events/<event>/brief.md`. Connect to Parle, join `#<room>`, and
> introduce yourself: your role title, what you own, what you can and cannot do, and whether
> automatic message pickup works. Then wait for work addressed to you.

For the Planner, add: *you are the lead — record each introduction in
`events/<event>/state.json` and seat the roles the manifest lists.*

## What each session may see

| Role | Own folder (read/write) | Also reads |
| --- | --- | --- |
| planner | `planner/` | `events/<event>/` |
| chef | `chef/` | brief |
| procurement | `procurement/` | brief |
| finance | `finance/` | brief |
| scheduler | `scheduler/` | brief |
| guest-manager | `guest-manager/` | brief |

Everyone gets the root `AGENTS.md`, `organization.md`, the event `brief.md`, and `results/`
read-only.

**Give each session only its own role folder.** If you hand every session the whole repo, the
boundaries test is meaningless — record it as untested rather than passed. Where the harness cannot
restrict paths, say so out loud.

## 4. Confirm the seats

A role is a teammate only after it introduces itself. Check `events/<event>/state.json`: each seated
role should have an address and `introduced: true`. A silent role is not seated, even if it is in
the room's member list.

## 5. Drive the work

Send the host request from the event `brief.md` to the Planner. Work flows along the handoff chain in
`organization.md`: Chef → Procurement → Finance, with the Planner reconciling.

Injected events are just fixtures delivered as messages. Give each to its owner:

| Fixture | Owner |
| --- | --- |
| `fixtures/late_guest.md` | Guest Manager |
| `fixtures/second_disruption.md` | Procurement |

Open the file and paste its contents as a message from the presenter, or drop it in `messages/inbox/`
if you are running the file fallback.

## Dry run without separate sessions

If you only have one session, give it the Planner folder and manually forward specialist outputs.
Mark *Boundaries* and *Real collaboration* as untested; a plausible-looking artifact does not prove
the team worked.

To try a single role on its own, start a session in that role's folder and treat yourself as the
host. Every contract has a **Solo mode** clause: it answers directly, writes only its own files, and
still refuses to guess a missing fact or to do another role's work.

## Troubleshooting

- **A role never introduces itself** — ask that session to check its Parle messages; after a restart
  it should verify its identity and re-read the team record.
- **A session reads another role's folder** — the mount is too wide. Re-launch it scoped.
- **Messages wake nobody** — address the session that should respond. A room-wide message wakes no
  one by default.
- **A temporary address expired** — re-link that session and have it reintroduce itself; the Planner
  updates `state.json`.

## Replay

There are no helper scripts. Restore the working tree and remove runtime output:

```
git restore .
rm -rf results/menu.md results/shopping-list.md results/schedule.md results/budget.json \
       results/decisions.md results/invitations
rm -f */workspace/*.json */workspace/*.md
```

Keep the `workspace/` stubs that ship with the repo; delete only what a run wrote. Relaunch fresh
sessions — reset does not clear cached context inside your agent factory.
