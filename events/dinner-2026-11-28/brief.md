# Event

A dinner for eight on Saturday, 28 November 2026 at 7 PM, under a $300 total cap.

- **Event id:** `dinner-2026-11-28`
- **Occasion:** dinner
- **Starts:** 2026-11-28 19:00
- **Headcount:** eight, including the host
- **Budget:** $300 total, including food and non-food supplies
- **Simulation date:** Monday, 23 November 2026
- **Scope:** planning, drafts and local artifacts only; no sending, purchases or real calendar changes

## Host request

> I'm hosting dinner next Saturday at 7 PM. Plan a great three-course meal for eight people,
> including me, keep everything under $300, and make sure everyone can attend and eat. Handle the
> details and tell me what needs my approval.

## Event seed

Per-role facts for this event live in `seed/<role>/` and are read-only to that role. Capability
knowledge (recipe catalogue, price catalogue, budget method, dietary rules) stays in the role's own
`data/` directory and travels with it to the next event.

## First deliverable

A feasible baseline dinner plan with an explanation of conflicts, uncertainty and approval needs.
