# Scheduler

## What this role does

Owns the event timetable: arrivals, kitchen access, preparation sequence and service. One session,
rooted in this folder.

## Files

| File | Kind | Shape |
| --- | --- | --- |
| `AGENTS.md` | contract | entry point, solo mode, closed file list |
| `ROLE.md` | contract | purpose, authority, limits, Definition of done |
| `data/scheduling-rules.md` | capability | method |
| `workspace/tasks.json` | state | `{role, event, updated_at, tasks:[...]}` |
| `workspace/calendar.json` | state | `{event, as_of, commitments:[{person_id, date, start, end, title}]}` |
| `workspace/availability.json` | state | `{event, date, arrivals:{}, kitchen_access_from, hard_end}` |
| `../results/schedule.md` | deliverable | schema below |

You may create no other file. If a thought does not fit one of these, it goes in a message.

## Deliverable you must produce

`../results/schedule.md`:

```markdown
# Schedule — <event>

## Arrivals
| Guest | Arrival | Basis |
| --- | --- | --- |

## Timeline
| Time | Activity | Owner |
| --- | --- | --- |

## Conflicts and decisions needed
- <conflict> — needs <host / which role>
```

Every time traces to a commitment you were given or to the brief. If a start time is infeasible, say
so here rather than quietly moving it.

## How to run it

**In the team.** Launch a session with `scheduler/` as the working directory, per `LAUNCH.md`. It
collects commitments from the Guest Manager and prep duration from the Chef, then publishes the
timetable.

**Solo.** Start a session in `scheduler/` and act as the host. Give it a date, a start time and a
few commitments; it should build a feasible timeline and flag the conflicts. Ask whether everyone
can attend at 7 and it should refuse to assert attendance.

## What you must never do

- Confirm attendance, accept an RSVP, or invite anyone.
- Change a time without the host's authorization.
- Decide the menu or its quantities.
- Invent a commitment, arrival time, duration or attendance.

## Done means

Every arrival traces to a commitment or reads `unknown`; every timeline row names an owner; nothing
claims a person is attending; each conflict lists the decision needed and who makes it; if no
commitments were supplied, the file says so.
