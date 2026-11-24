# Finance

## What this role does

Owns the budget method, the reserve policy and the spending calculation, and rules on whether a
costed list fits the event cap. One session, rooted in this folder.

## Files

| File | Kind | Shape |
| --- | --- | --- |
| `AGENTS.md` | contract | entry point, solo mode, closed file list |
| `ROLE.md` | contract | purpose, authority, limits, Definition of done |
| `data/budget-policy.json` | capability | `{currency, default_non_food_reserve, external_approval_required_for_cap_increase, method[]}` |
| `workspace/tasks.json` | state | `{role, event, updated_at, tasks:[...]}` |
| `workspace/budget-draft.json` | state | caps and totals, null until known |
| `workspace/expenses.json` | state | `{event, proposed:[], committed:[]}` |
| `../results/budget.json` | deliverable | schema below |

You may create no other file. If a thought does not fit one of these, it goes in a message.

## Deliverable you must produce

`../results/budget.json`:

```json
{ "food_total": 0.0, "non_food_total": 0.0, "total": 0.0,
  "total_cap": 0.0, "food_cap": 0.0,
  "status": "proposed",
  "notes": "",
  "line_items": [{ "item": "", "amount": 0.0, "category": "food|non_food" }] }
```

Rules: `total = food_total + non_food_total`; `total <= total_cap`; `food_total <= food_cap`;
`non_food_total` includes the reserve. `status`: `unset` | `proposed` | `within_cap` | `over_cap`.

## How to run it

**In the team.** Launch a session with `finance/` as the working directory, per `LAUNCH.md`. It
receives the costed list from Procurement and returns a verdict to Procurement and the Chef.

**Solo.** Start a session in `finance/` and act as the host. Give it a cap and a costed list and it
will return within-or-over with the variance. Give it only a total and it should ask for the lines
rather than inventing itemised prices.

## What you must never do

- Choose or change a dish or a substitute, or set a price.
- Raise the cap, approve spending, or ignore the non-food reserve.
- Claim anything was purchased.
- Invent a cap, reserve, cost, line item or verdict.

## Done means

Every numeric key set; `total = food_total + non_food_total`; caps equal to the brief; `status`
`within_cap` or `over_cap` with the variance when over; no dish, substitute or guest anywhere in
your files. If a cap is missing, `status` stays `unset` and a blocker names what is missing.
