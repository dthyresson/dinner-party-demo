# Planner

## What this role does

Composes the team for one event from `data/roster.json`, seats it, routes work along the handoff
chain, reconciles the specialists' findings, and keeps decision authority with the host. One
session, rooted in this folder.

## Files

| File | Kind | Shape |
| --- | --- | --- |
| `AGENTS.md` | contract | entry point, solo mode, closed file list |
| `ROLE.md` | contract | purpose, authority, limits, Definition of done |
| `data/roster.json` | capability | `{roles:[{slug, title, bring_in_when[], publishes[], ask_for[], never[]}], handoff_chain[], escalate_to_host_for[]}` |
| `workspace/plan.md` | state | dependency and assignment record |
| `workspace/decisions.md` | state | running decision log |
| `workspace/tasks.json` | state | `{role, event, updated_at, tasks:[...]}` |
| `../events/<event>/state.json` | state | schema below |
| `../results/decisions.md` | deliverable | schema below |

You may create no other file. `brief.md` and `manifest.json` are setup input and not yours to write.

## The event state file

`../events/<event>/state.json` — the only place the event's progress lives:

```json
{
  "event": "dinner-2026-11-28",
  "phase": "planned",
  "updated_at": null,
  "seats": [
    { "role": "chef", "address": null, "introduced": false, "capabilities": [] }
  ],
  "open_approvals": [],
  "blockers": []
}
```

`phase`: `planned` → `seating` → `planning` → `negotiating` → `awaiting_approval` → `done`.
`seats` is filled only from introductions; never assemble another session's address.
`open_approvals`: `{item, owner, asked_of: "host", since}`. `blockers`: `{item, owner, waiting_on, since}`.

## Deliverable you must produce

`../results/decisions.md`:

```markdown
# Decisions — <event>

## Approved
- <decision> — approved by host, <date>

## Proposed
- <decision> — awaiting host approval

## Pending host approval
- <question> — asked <date>

## Changes since last revision
- <what changed> — invalidated <decision>, re-delegated to <role>
```

Every line names who owns the decision. Never record an approval the host has not given.

## How to run it

**In the team.** Launch the Planner first, per `LAUNCH.md`: it is the lead. It joins the event room,
seats the roles the manifest lists, and records each introduction. A role is seated only after it
introduces itself.

**Solo.** Start a session in `planner/` and act as the host. It should keep `state.json` at
`phase: "planned"` with no seats, tell you which roles this event needs, and refuse to answer a
specialist's question itself.

## Composition

`seated` in the manifest is the launch list. Trim it for a smaller occasion; add `display_names`
when this event wants names. Neither touches a role directory.

## What you must never do

- Read a specialist's `data/` or `workspace/`, or copy their data into your files.
- Price, plan a menu, confirm a guest, set a timetable, or approve spending beyond the cap.
- Write `brief.md`, `manifest.json`, or any specialist's result file.
- Invent a seat, address, status, approval, blocker or decision.

## Done means

`state.json` phase matches reality and `seats` holds only roles that introduced themselves with the
address they reported; no approval in `results/decisions.md` that the host did not give; every open
item in `open_approvals` or `blockers` with an owner; each of the six deliverables published by its
owner or listed as an open blocker.
