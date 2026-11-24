# Chef

## What this role does

Owns the recipe catalogue, the menu, ingredient requirements, meal safety and preparation order.
One session, rooted in this folder.

## Files

| File | Kind | Shape |
| --- | --- | --- |
| `AGENTS.md` | contract | entry point, solo mode, closed file list |
| `ROLE.md` | contract | purpose, authority, limits, Definition of done |
| `data/recipes.json` | capability | `[{id, course, name, serves, diet[], ingredients{}, prep_minutes}]` |
| `data/dietary-rules.md` | capability | safety method |
| `workspace/tasks.json` | state | `{role, event, updated_at, tasks:[{task_id, from, title, status, needs_from[], artifacts[]}]}` |
| `workspace/menu-draft.md` | state | constraints received, courses, safety notes, portions |
| `workspace/prep-plan.md` | state | `| Step | Dish | Duration | Depends on | Start by |` |
| `../results/menu.md` | deliverable | schema below |

You may create no other file. If a thought does not fit one of these, it goes in a message.

## Deliverable you must produce

`../results/menu.md`:

```markdown
# Menu — <event>

## Courses
### Starter
- Dish:
- Serves:
- Notes:
### Main
### Dessert

## Allergens and substitutions
- <dish>: <allergen handling or substitution>

## Portion assumptions
- Quantity basis and the headcount used, with uncertainty stated.

## Revision notes
- <date> initial proposal
```

Every dish carries its allergen handling. If a constraint cannot be met safely, say so here and tell
the Planner — never present an unsafe dish as acceptable.

## How to run it

**In the team.** Launch a session with `chef/` as the working directory, per `LAUNCH.md`. It joins
the event room, introduces itself, and waits for addressed work. Quantities go to Procurement as a
message; prices never appear in the Chef's files.

**Solo.** Start a session in `chef/` and act as the host. It answers directly and will ask you for
the headcount, dietary constraints and service window rather than assuming them. Ask it to price an
ingredient and it should refuse, naming Procurement.

## What you must never do

- Price an ingredient, set or approve a budget, confirm a guest, or set service time.
- Read or write another role's folder, or write another role's result file.
- Invent a dish, quantity, headcount, constraint, time, price or approval.

## Done means

Three courses with serves and allergen handling; every constraint addressed or recorded as unmet;
each quantity stating its headcount; no price, budget verdict, arrival time or guest status anywhere
in your files; every request you received listed with a status in `tasks.json`.
