# Organization and collaboration protocol

## Roles

| Role           | Owns                                    | Core decisions                          | Escalation                          |
| -------------- | --------------------------------------- | --------------------------------------- | ----------------------------------- |
| Chief of Staff | Overall outcome and decisions           | Delegation, reconciliation, reporting   | Host approvals                      |
| Guest Manager  | Guest roster, RSVP, dietary preferences | Invitations and guest constraints       | Extra guests, unknown RSVP          |
| Scheduler      | Timing and calendar                     | Feasible event schedule                 | Time change requiring host approval |
| Chef           | Recipes and food safety                 | Menu, ingredient needs, prep sequence   | Cannot satisfy dietary safety       |
| Procurement    | Pantry, prices and supply availability  | Costed shopping plan, substitutions     | Purchases and ingredient changes    |
| Finance        | Budget and spending policy              | Budget viability, spending limit checks | Additional spending                 |

## Naming

| Name        | Role           |
| ----------- | -------------- |
| **Steph**   | Chief of Staff |
| **Gigi**    | Guest Manager  |
| **Cal**     | Scheduler      |
| **Remy**    | Chef           |
| **Piper**   | Procurement    |
| **Frankie** | Finance        |

Now you can naturally say:

> "Steph, invite Alex to dinner. He's allergic to tree nuts, so make sure dessert is safe for him."

And observe how Steph coordinates the team.

## Contract for collaboration

A specialist responds with: `task_id`, `status` (done/blocked/needs_input), `findings`, `constraints`, `proposals`, `assumptions`, `needs_from`, `artifacts`. The Chief of Staff tracks the dependency graph and approvals, not each specialist's raw data.

Specialists may communicate directly (e.g. Chef ↔ Procurement) and send the Chief of Staff a concise summary. Only the owning role may update source-of-truth data in its `data/` directory. Cross-role deliverables can be placed in `results/` with source attribution.

## Access boundaries

Each role sees the root `AGENTS.md`, `organization.md`, `scenario.md` and its own directory. The Chief of Staff sees shared outputs and agent responses but not all specialist `data/` by default. The presenter alone sees `fixtures/` and `EVALUATION.md`.

## Approvals

Do not purchase or send invitations. A ninth guest must not be marked accepted without host approval. All simulated outward communications are drafts until approved. Finance may validate budget compliance but may not approve an increase of the $300 cap.
