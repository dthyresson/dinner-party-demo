# Organization and collaboration protocol

## Roles

| Role | Owns | Core decisions | Escalation |
| --- | --- | --- | --- |
| Planner | Event outcome, composition, event state | Seating, assignment, what needs host approval | Host approvals |
| Guest Manager | Guest roster, RSVP, dietary constraints | Headcount, minimum necessary constraint | Extra guests, unknown RSVP |
| Scheduler | Timing and calendar | Feasible event timetable | Time change requiring host approval |
| Chef | Recipes and food safety | Menu, ingredient needs, prep sequence | Cannot satisfy dietary safety |
| Shopper (Procurement) | Catalogue, prices and supply availability | Costed shopping plan, substitutions | Purchases and ingredient changes |
| Finance | Budget method and spending policy | Budget viability, cap check | Additional spending |

## Role titles

Roles are positional. There is a Chef, not a person with a name. An event may give a role a display
name in `events/<event>/manifest.json` under `display_names`; that name labels the event's room only
and changes nothing about the role or its authority. Two events may name the Chef differently, or
not at all.

## Composition

A role is a contract, not a person. Each role runs as its own session, rooted in its own directory,
and is seated in the event's room. An event seats only the roles it needs: `seated` in
`events/<event>/manifest.json` is the launch list. Composing Thanksgiving, a birthday or New Year's
means a new event folder and a new room — never an edit to a role directory.

## Team protocol

- Every role is a separate session. It joins the room named in the manifest.
- **Introduce yourself before you are counted.** Report role title, what you own, what you can and
  cannot do, and whether automatic message pickup works. The Planner records the seat in
  `events/<event>/state.json` only after the introduction.
- The Planner keeps `state.json` current: `phase`, `seats`, `open_approvals`, `blockers`.
- Address the session that owns the fact. A room-wide message wakes nobody by default.
- Use the response contract: `task_id`, `status` (done/blocked/needs_input), `findings`,
  `constraints`, `proposals`, `assumptions`, `needs_from`, `artifacts`.
- One writer per file. Corrections come back as messages, and the owner republishes.

## No seed data

Every role starts with capability knowledge only. There is no guest list, calendar, pantry, recipe
choice or event cap beyond what the brief states. A role asks the owning role for each fact and
records `unknown` rather than filling the gap with a plausible value.

## Data ownership

| Tier | Path | Read | Write |
| --- | --- | --- | --- |
| Capability knowledge | `<role>/data/` | owning session | owning session |
| Working state and tasks | `<role>/workspace/` | owning session | owning session |
| Event record | `events/<event>/` | every seated session | Planner owns `state.json`; `brief.md` and `manifest.json` are setup input |
| Published deliverables | `results/` | everyone | exactly one owner per file |

Each role writes only the files its own `AGENTS.md` lists. No role creates extra documents.

## Handoff chain

The canonical negotiation, and the proof that lanes do not cross:

1. **Chef** proposes a dish and states exact quantities and headcount assumptions. It messages
   Procurement and copies the Planner. The Chef never prices anything.
2. **Procurement** prices those quantities, deducts anything the host confirmed is on hand, flags
   out-of-stock goods and catalogue alternatives, and messages the costed list to Finance, copying
   the Chef. It never changes the menu or the quantities.
3. **Finance** checks the costed list against the event cap and the non-food reserve. It returns
   *within the cap*, or *over by an amount* with the category breakdown, to Procurement and the
   Chef. It never picks a dish or a substitute.
4. **If over budget**, Procurement proposes catalogue alternatives; the Chef decides the menu
   change; Finance re-checks. Nobody cuts quantities silently, and no specialist may declare "it
   fits".
5. **Escalation.** Only the Planner may say the host approved something. Only the host may raise the
   cap, add a guest, or move the time.

Worked example: the Chef wants twelve lobsters. The Chef states the twelve and the headcount it
assumes. Procurement prices them and reports the cost. Finance replies that this puts the meal $100
over the food cap. Procurement offers cheaper catalogue alternatives. The Chef revises the dish.
Finance re-checks. At no point does the Chef quote a price, Procurement cut the count, or Finance
choose the replacement.

Each role may speak only for its own domain.

## Access boundaries

Each role sees the root `AGENTS.md`, `organization.md`, its own role directory, the event's
`brief.md`, and `results/` read-only. It does not see another role's `data/` or `workspace/`. The
Planner sees the manifest, the event state and each role's introductions and replies, not their
private data. The presenter alone sees `fixtures/`.

## Approvals

Do not purchase or send invitations. A ninth guest must not be marked accepted without host
approval. All simulated outward communications are drafts until approved. Finance may validate
budget compliance but may not approve an increase of the cap.
