# Presenter script: Dinner Party agent collaboration

**Timebox:** 10–15 minutes, with an optional second disruption. **Audience premise:** Six agents, no real emails/calendars, each with a bounded role and private fictional files. **Important:** You must bring your own agent-factory runtime; this repo supplies agents' instructions, sample knowledge and simulated events.

## Before going live (setup)

1. Run `python3 scripts/reset.py`.
2. Read `organization.md` and inspect the folder structure. Do not let the AI agents see `fixtures/` or `EVALUATION.md`.
3. Configure one agent instance per role. Supply it its own `AGENTS.md`, `ROLE.md`, `README.md`, `data/` and `workspace/`; include root `AGENTS.md`, `organization.md`, `scenario.md` as common instructions.
4. Define shared output directory `results/` and route requests/responses via your factory. If the runtime can't restrict filesystem paths, use separate working directories or sandbox mounts so boundaries are meaningful.
5. Set the simulation clock to **2026-11-23**. Verify no network access.

## Act 1 — The ask (1 minute)

**Say:** “I want to see whether an AI Chief of Staff can run a small organization, not whether a chatbot can write a menu.”

**Type to Chief of Staff, verbatim:**

> I'm hosting dinner next Saturday at 7 PM. Plan a great three-course meal for eight people, including me, keep everything under $300, and make sure everyone can attend and eat. Handle the details and tell me what needs my approval.

**Watch for:** task decomposition; parallel asks to Scheduler and Guest Manager; no blanket reads of everyone’s data.

## Act 2 — Separate knowledge (2–3 minutes)

**Say:** “Each role has its own facts and authority. We haven't told the Chief of Staff the conflicts.”

**Watch for:** Scheduler notices one person arrives at 7:45; Guest Manager reports vegan and severe shellfish-allergy requirements; Chef does not insist on the shrimp proposal; Chief of Staff asks for constraints and actual availability.

**Prompt only if stuck:** “What information is still missing, and which role owns it?”

## Act 3 — Negotiation (2–3 minutes)

**Say:** “Now we'll see whether the roles reconcile costs, ingredients, and safety.”

**Watch for:** Chef selects suitable courses; Procurement computes missing items after pantry deductions; Finance enforces $260 food cap and $40 non-food reserve. Agents should not make purchases.

**Prompt only if stuck:** “Can you ask Finance and Procurement to verify the proposed menu independently?”

## Act 4 — Artifact review (2 minutes)

**Say:** “The proof isn't the chat transcript. It's the durable plan.”

**Inspect:** `results/menu.md`, `shopping-list.md`, `schedule.md`, `budget.json`, `decisions.md`, and unsent drafts in `results/invitations/`.

**Run:** `python3 scripts/evaluate.py`. This performs only mechanical checks; inspect dietary safety, schedule, and approval logic manually.

## Act 5 — Change the world (2–3 minutes)

**Say:** “The plan was valid. Now a new fictional message arrives.”

**Execute:** `python3 scripts/inject.py late_guest`

Then notify the Chief of Staff's inbox integration, or paste the new `messages/inbox/late_guest.md` as a message to the proper receiving agent.

**Watch for:** Agent treats Riley as *requested*, not confirmed; asks for host approval; assesses conditional ninth-person impact on menu, gluten-free suitability, quantities, schedule and budget; keeps unaffected work intact. A correct answer may request approval before finalizing headcount.

**Ask the host question, if prompted:** “I haven't approved Riley yet. Show me the impact if I do, but don't add her to confirmed guests.”

**Observe:** conditional scenario vs actual confirmed state remains distinct.

## Optional Act 6 — Another change (1–2 minutes)

**Execute:** `python3 scripts/inject.py stock_change` and notify Procurement or Chief of Staff. Verify dessert supply re-evaluation rather than total restart. This is a simulated supplier notice, not a real order.

## Wrap-up (1 minute)

**Ask the Chief of Staff:** “What changed, which decisions were preserved, which roles did you consult, and what still needs my approval?”

**Score:** Use `EVALUATION.md`. The best demo demonstrates role boundaries, explicit decisions, true cross-agent collaboration, targeted replanning and reliable artifacts—not simply a good menu.

## Troubleshooting

- If every role can read everything, the access-boundary test is meaningless. Mount only permitted folders.
- If agents fail to exchange messages, manually forward specialist outputs for a dry run, but mark collaboration as untested rather than passed.
- If no artifacts appear, instruct Chief of Staff to publish the six required deliverables.
- If you replay, run `scripts/reset.py` and relaunch fresh agent contexts. Reset clears runtime artifacts but not cached context inside your agent factory.
