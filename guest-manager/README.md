# Guest Manager

## What this role does
Own the fictional guest roster, invitation/RSVP state, dietary requirements and preferences.

## How to run it
Load `AGENTS.md`, then `ROLE.md`, the root instructions and assigned task. The simulated data is local to this directory. Keep work in `workspace/` and send role-to-role requests using the agent factory's own messaging mechanism (or file messages in `../messages/` for a file-driven test).

## Seed data
See `data/` (if present). It contains fictional information under this role's responsibility; it is not globally shared by default.

## Expected handoff
Return a concise task status, key facts/constraints, recommendations, unresolved questions and path to artifacts. Notify the Chief of Staff of any conflict that threatens dinner feasibility.

## Limitations
Do not invite or accept a new attendee without host approval; avoid sharing unnecessary individual dietary details.
