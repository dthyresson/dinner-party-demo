# Dinner Party — multi-agent chief-of-staff demo

A **fictional, local-only** test fixture for an agent factory. Six role-based agents coordinate a three-course dinner for eight on **Saturday, November 28, 2026**, with a **$300 total cap**. The scenario is designed to test delegation, private data boundaries, budget reconciliation, meal safety, and replanning after new information.

## Quick start

1. Read [`DEMO_SCRIPT.md`](DEMO_SCRIPT.md), then [`organization.md`](organization.md).
2. Give your agent-factory's Chief of Staff access to `chief-of-staff/AGENTS.md` and its role files. Set its simulated current date to **2026-11-23**.
3. Configure each specialist with its own `AGENTS.md`, `ROLE.md`, `README.md`, and its local `data/`. Do **not** give the Chief of Staff unrestricted access to other roles' `data/`.
4. Submit the initial request from `scenario.md`. Let specialists collaborate using your factory's task/delegation messaging. All outputs should go into `results/` or the respective role's `workspace/`.
5. Inject the late guest message with `python3 scripts/inject.py late_guest` (after making a valid baseline plan).
6. Inspect the revised plan and run `python3 scripts/evaluate.py` for artifact checks. Use [`EVALUATION.md`](EVALUATION.md) for behavior scoring.
7. Reset the sandbox with `python3 scripts/reset.py` to replay it.

Python 3.9+ standard library only. **This repository is a fixture, not an agent runtime.** Your agent-factory supplies agent execution, routing, and messaging. Local files are the only simulated records and state.

## Structure

- `AGENTS.md` — organization-wide instructions
- `organization.md`, `scenario.md` — org chart and assignment
- `chief-of-staff/`, `guest-manager/`, `scheduler/`, `chef/`, `procurement/`, `finance/` — roles, per-role readmes, agent entrypoints, and seed data
- `messages/` — local simulated incoming communications
- `results/` — expected output artifact locations (initially empty)
- `scripts/` — inject, reset, and evaluate helpers
- `fixtures/` — immutable scenario event messages, not to be seen until triggered
- `DEMO_SCRIPT.md` — presenter talk track and checkpoints
- `EVALUATION.md` — human rubric and machine-readable expectations

## Data isolation

Roles own their own facts. A role may publish minimum necessary facts through messages or shared artifacts; it shouldn't rely on the Chief of Staff reading all files. The `fixtures/` directory and `EVALUATION.md` are presenter/evaluator resources, not agent inputs.

## Intended outcome

A feasible menu covering vegan and shellfish allergy requirements, confirmed/proposed timing, a costed shopping list respecting the $300 total and $40 non-food reserve, drafts (not sent messages), and a clear record of unresolved host approvals.

## Naming

| Name        | Role           |
| ----------- | -------------- |
| **Steph**   | Chief of Staff |
| **Gigi**    | Guest Manager  |
| **Cal**     | Scheduler      |
| **Remy**    | Chef           |
| **Piper**   | Procurement    |
| **Frankie** | Finance        |

You can naturally say:

> "Steph, invite Alex to dinner. He's allergic to tree nuts, so make sure dessert is safe for him."

And observe how Steph coordinates the team.

## Agent organization

```mermaid
flowchart TD
    H["Host / User"]
    COS["Steph — Chief of Staff<br/>Owns overall outcome and reconciles constraints"]
    GM["Gigi — Guest Manager<br/>Roster, RSVPs, dietary restrictions"]
    SCH["Cal — Scheduler<br/>Calendar, arrivals, preparation and service timing"]
    CHEF["Remy — Chef<br/>Menu, recipes, food safety and preparation sequence"]
    PROC["Piper — Procurement<br/>Pantry, availability, pricing and shopping plan"]
    FIN["Frankie — Finance<br/>$300 budget and $40 non-food reserve"]

    H -->|"Dinner request and approvals"| COS
    COS -->|"Delegates work"| GM
    COS -->|"Delegates work"| SCH
    COS -->|"Delegates work"| CHEF
    COS -->|"Delegates work"| PROC
    COS -->|"Delegates work"| FIN

    GM -->|"Attendance and dietary constraints"| COS
    GM -.->|"Minimum necessary guest facts"| CHEF
    GM -.->|"Availability constraints"| SCH

    SCH -->|"Feasible event timetable"| COS
    SCH -.->|"Timing requirements"| CHEF
    SCH -.->|"Arrival and service timing"| GM

    CHEF -->|"Menu and ingredient requirements"| COS
    CHEF -.->|"Recipe quantities"| PROC
    CHEF -.->|"Safety and substitution decisions"| PROC
    CHEF -.->|"Dietary constraints"| GM
    CHEF -.->|"Preparation sequence"| SCH

    PROC -->|"Costed shopping proposal"| COS
    PROC -.->|"Prices and availability"| FIN
    PROC -.->|"Supply constraints and substitutions"| CHEF

    FIN -->|"Budget viability and trade-offs"| COS
    FIN -.->|"Spending limits"| PROC
```

**Approval boundaries**

- The host approves attendance additions, time changes, and extra spending.
- The Chief of Staff reconciles specialist findings and publishes integrated plans.
- Finance cannot increase the budget or permit purchases beyond the $300 cap.
- Procurement cannot purchase or independently change allergy-relevant ingredients.
- Guest Manager cannot send invitations or accept new guests without approval.
- Specialists may communicate directly, but material findings and blockers are summarized to the Chief of Staff.
