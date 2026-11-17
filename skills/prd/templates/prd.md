---
id: {PRD_ID}
title: {Title}
status: draft            # draft | signed-off | shipped | superseded
owner: {product owner or client contact}
tracker: {tracker item reference, or none}
mockups: {relative path to the mockup folder, or none}
created: {YYYY-MM-DD}
---

# {Title}

## Revision history

| Rev | Date | Change | Doc |
|---|---|---|---|
| — | {YYYY-MM-DD} | Initial | — |

## What and why

{Two to five sentences in the product owner's language. The problem, who has it,
and what changes for them when this ships. No solution language.}

## Who uses it

{One line per persona: who they are and what they are trying to get done.}

## Roles and permissions

Personas are not authorisation. Map every persona to a configured role.

**Access.** {Which roles can reach the screen, route or capability at all.}

**Actions.**

| Action | {role} | {role} | {role} |
|---|---|---|---|
| View | | | |
| Edit | | | |
| {destructive action} | | | |

**Data scope.** {Single-site vs all-sites, own records vs all, any redaction.}

## Today's behaviour

{What the user does now, and where it falls short. Omit for new capabilities.}

## Proposed behaviour

{Describe the behaviour per screen, flow or capability. Specific verbs: add,
show, filter by, block. Reference mockup sections by name. No schema, no event
types, no integration mechanics — those are decisions for the plan.}

## Acceptance criteria

One per material behaviour. Three to seven. Each must be checkable by someone
who did not build it.

- **AC1** — Given {state}, when {action}, then {observable result}.
- **AC2** — Given {state}, when {action}, then {observable result}.
- **AC3** — Given {state}, when {action}, then {observable result}.

## Out of scope

{What this PRD explicitly does not cover. Required: infer something if the
owner did not volunteer it, and flag it in Open questions.}

## Dependencies and assumptions

{Existing data, external feeds, other PRDs, people or teams this depends on.}

## Open questions

{Only what is genuinely undecided and needs the owner. Decisions already made
by convention are not questions.}

| # | Question | Owner | Resolved |
|---|---|---|---|
| Q1 | | | |

## Notes

{Anything that helps the reader and fits nowhere above.}
