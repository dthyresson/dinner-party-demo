# Events

An event is a **room** plus a **set of seated role sessions**. Composing a new occasion means
creating one folder here, not editing any role directory.

```
events/<event-id>/
  brief.md          host input: occasion, date, headcount, budget, constraints
  manifest.json     setup record: room, seated roles, optional per-event display names
  state.json        Planner-owned progress: phase, seats, open approvals, blockers
```

There is no per-role seed folder. Roles start with capability knowledge only and ask for event
facts.

## Compose a new event

1. Copy an existing event folder and rename it (`new-years-2027`).
2. Rewrite `brief.md` with the new host request and constraints.
3. Edit `manifest.json`: `event`, `occasion`, `date`, `headcount`, `room`, and `seated` — only the
   roles this occasion needs. A birthday that needs no timing work omits `scheduler`; a potluck that
   needs no shopping omits `procurement`. `display_names` is optional, e.g.
   `{"chef": "Remy"}`, and labels this event's room only.
4. Reset `state.json` to `phase: "planned"`, one unseated entry per seated role, empty approvals.
5. Launch one session per seated role, rooted in that role's directory.

No role file changes between events.

## Ownership

| File | Writer |
| --- | --- |
| `brief.md` | setup input, read-only to agents |
| `manifest.json` | setup input, read-only to agents |
| `state.json` | the Planner, and only the Planner |

## Rules

- A role reads the brief and its own files; it does not read another role's `data/` or `workspace/`.
- Addresses and session identities are never configured here; the Planner records what each role
  reports at introduction.
