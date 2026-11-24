# Presenter script: Dinner Party agent collaboration

**Timebox:** 10–15 minutes, with an optional second disruption. **Audience premise:** Six positional
roles, each its own session with its own folder, no real emails or calendars. **Important:** You
must bring your own agent-factory runtime; this repo supplies the role contracts, the event record
and the simulated events.

## Before going live (setup)

1. Read `organization.md` and `LAUNCH.md`, and inspect the folder structure. Do not let the AI agents
   see `fixtures/`.
2. Pick the event folder (`events/dinner-2026-11-28/`). Read its `brief.md` for the host request and
   `manifest.json` for the room and the `seated` list.
3. Launch **one session per seated role**, each rooted in its own role directory, per `LAUNCH.md`.
   Give each session only its own folder, the root documents, the event `brief.md` and read-only
   `results/`. If the runtime can't restrict paths, say so and treat boundaries as untested.
4. Seat every session's agent in the event room. Set the simulation clock to **2026-11-23**. Verify
   no network access.

There is no seed data. Every role starts with knowledge and no event facts, so each one has to ask.

## Act 1 — The ask (1 minute)

**Say:** “Each role is a real agent in its own process, with its own facts. Watch whether they
delegate cleanly or spill into each other's lanes.”

**Type to the Planner, verbatim:**

> I'm hosting dinner next Saturday at 7 PM. Plan a great three-course meal for eight people,
> including me, keep everything under $300, and make sure everyone can attend and eat. Handle the
> details and tell me what needs my approval.

**Watch for:** the Planner seats the roles the manifest lists and counts a seat only after that
role introduces itself; it asks for constraints in parallel rather than reading anyone's folder; no
blanket read of everyone's data.

## Act 2 — Separate knowledge (2–3 minutes)

**Say:** “Nobody has the guest list yet. Watch where each fact goes.”

**Watch for:** the Guest Manager asks for the roster and the dietary constraints instead of
inventing guests; the Scheduler asks for commitments instead of assuming a start; the Chef asks for
headcount and constraints and does not pick a dish blind.

**Prompt only if stuck:** “What information is still missing, and which role owns it?”

## Act 3 — Negotiation (2–3 minutes)

**Say:** “Now watch cost, ingredients and safety reconcile without anyone leaving their lane.”

**The lobster loop:** the Chef states quantities; Procurement prices them from the catalogue and
flags anything out of stock; Finance rules whether the cost fits the cap and by how much;
Procurement offers alternatives; the Chef revises; Finance re-checks.

**Watch for:** only the Chef names a dish, only Procurement quotes a price, only Finance says
“over” or “within”; no purchase is made; the $40 non-food reserve is respected; no role creates a
file it does not own.

**Prompt only if stuck:** “Ask Finance and Procurement to verify the proposed menu independently.”

## Act 4 — Artifact review (2 minutes)

**Say:** “The proof isn't the chat transcript. It's the durable plan, written by its owner.”

**Inspect:** `results/menu.md`, `shopping-list.md`, `schedule.md`, `budget.json`, `decisions.md`,
and unsent drafts in `results/invitations/` — plus each role's `workspace/` for its task list.

**Check by hand:** dietary safety, timing, approval logic, and whether each file's owner actually
wrote it. There is no scoring script; the schemas in each role's `README.md` and in
`results/README.md` are the contract.

## Act 5 — Change the world (2–3 minutes)

**Say:** “The plan was valid. Now a new fictional message arrives.”

**Deliver:** open `fixtures/late_guest.md` and paste it to the Guest Manager as a message from the
host. With the file fallback, drop it in `messages/inbox/`.

**Watch for:** the Guest Manager treats Riley as *requested*, not confirmed, and asks the Planner for
host approval; the Planner assesses the conditional ninth-person impact on menu, gluten-free
suitability, quantities, schedule and budget; unaffected work stays intact. A correct answer may
request approval before finalizing headcount.

**Ask the host question, if prompted:** “I haven't approved Riley yet. Show me the impact if I do,
but don't add her to confirmed guests.”

**Observe:** the conditional scenario and the confirmed state remain distinct.

## Optional Act 6 — Another change (1–2 minutes)

**Deliver:** `fixtures/second_disruption.md` to Procurement. Verify dessert supply is re-evaluated
rather than the whole plan restarting. This is a simulated supplier notice, not a real order.

## Wrap-up (1 minute)

**Ask the Planner:** “What changed, which decisions were preserved, which roles did you consult, and
what still needs my approval?”

**What good looks like:** strict role boundaries, one writer per artifact, no invented fact, true
cross-role collaboration, targeted replanning, and a decision record that never claims an approval
the host did not give.

## Troubleshooting

- If every session can read every folder, the access-boundary test is meaningless. Mount only the
  permitted folders, or mark boundaries untested.
- If agents fail to exchange messages, manually forward specialist outputs for a dry run, but mark
  collaboration as untested rather than passed.
- If no artifacts appear, instruct the Planner to ask each owner to publish its file.
- To run a different occasion, copy the event folder, edit `brief.md` and `manifest.json`, reset
  `state.json`, and launch only the `seated` roles. No role file changes.
