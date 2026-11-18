---
name: plan
description: Produce the single implementation plan for a piece of work (feature from a PRD, revision, bug fix from an issue, or technical change) with a design section, shared context, and verification-bounded phases; or amend an existing plan. Use when the user asks to plan a feature, plan a fix, turn a PRD or revision into a plan, create an implementation plan, or invokes /plan. Plans only; never implements.
argument-hint: <prd path | revision path | issue ref | decision record | description> | amend <plan path> <note> [--repo <path>]
---

# Plan

Produce one plan a human can approve in a sitting and an implementer can
execute without rediscovering the design. Plan only: no code, no commits, no
PR. A spike is allowed only to settle a design hinge, and its code is
throwaway.

**Input:** $ARGUMENTS (absent: use the conversation).

## 0. Load configuration

1. Resolve the target repository (`references/config.md`, *Target
   repository*): a `--repo <path>` argument; else the nearest folder at or
   above the input path (or the current folder) holding `.sdlc/` or `.git`;
   when that is a workspace and the work names one of `workspace.repos`,
   that repository's checkout; else `${CLAUDE_PROJECT_DIR}`. Every path and
   git operation below is relative to it. Say which was chosen when it is
   not the project directory.
2. Read its `.sdlc/config.yaml` if present; apply defaults from
   `references/config.md` for anything missing.
3. Read its `.sdlc/extensions/plan.md` if present. Each
   level-two heading is an extension point (`context`, `design`, `sections`,
   `done-criteria`, `checks`); keep its content to apply at that step. Warn
   once about unknown headings and ignore them.
4. If the input starts with `amend`, go to **Amend mode**.

## 1. Resolve the trigger and the lane

Classify the input as one of:

| Input | Kind | Plan id |
|---|---|---|
| A PRD file or folder | feature | the PRD's `id` from its frontmatter |
| A revision file | revision | the revision's `id` from its frontmatter |
| An issue reference or a bug description | bug-fix | `{issue number}-{slug}`; the full reference goes in `tracker` |
| A decision record, refactor, upgrade, infra or tooling change | technical | decision id, else `YYYYMMDD-{slug}` |
| A description with none of the above | inline | `YYYYMMDD-{slug}` |

Then ask the lane question before doing anything else:

> Is this small enough that plan mode with no artefact would do? Does anyone
> other than the implementer need to sign off *what* is built before *how*?

- Small and single-session: say so, recommend plan mode, and stop unless the
  user insists on a file.
- Needs behaviour sign-off and there is no PRD or revision: stop and recommend
  the `prd` or `revise` skill. Do not write a plan against an unsigned
  requirement.
- Needs architecture sign-off and there is no decision record: write the plan,
  but mark the design decision as requiring a decision record before approval.
- Otherwise continue.

For a PRD or revision: read it fully, list its acceptance criteria, and note
which this plan will deliver and which are deferred. A plan may defer criteria
only with a named follow-up. For an issue: retrieve it through whatever
tracker access exists, read the comment history, and separate the required
outcome from any suggested implementation. For a bug: read any investigation
under `artefacts.investigations_dir` first; if there is none and the cause is
not obvious, write one before planning (see `references/investigation.md`).

Establish the invariant that must hold afterwards, the observable result that
proves it, and the constraints that are genuinely fixed. Ask the user only when
an ambiguity would produce materially different plans.

**Repositories.** Work that changes only this repository leaves `repos:`
empty. Work that changes several belongs in a workspace repository
(`repo.kind: workspace`): in an `app`, stop and say so; in a workspace, list
them in `repos:`, primary first, each matching an entry in `workspace.repos`.

## 2. Gather context

In this order, and record what was read for the plan's mandatory-reading list:

1. Repository guidance already loaded (CLAUDE.md and rules).
2. Every file in `context.always_read`.
3. Everything under the `context` extension point.
4. If `context.knowledge_index` is true, follow `references/knowledge-index.md`.
   Otherwise, look for a `docs/decisions` or `docs/adr` folder and read the
   titles; read any record whose title plausibly intersects this work.

Then explore the codebase. For anything beyond a localised change, launch
explorer agents in parallel with the prompts in `references/exploration.md`
(one for *where* the relevant code lives, one for *how* the behaviour flows),
ask each for the five to ten files that matter, then read those files
yourself. The planner owns the synthesis and must have seen the decisive code.

Collect `file:line` references, existing primitives and extension points,
validation commands (from `validation.*` or discovered from the project's
manifest), and anything that contradicts the request.

## 3. Design

Write the design section before any phase. It holds:

- **Decisions.** Each choice with the alternatives rejected and whether it is
  durable (should outlive this work). Durable decisions get promoted at
  close-out.
- **Documents reconciled.** Every decision record, pattern or reference doc the
  work intersects, with a note: `follow`, `extend`, `supersede: <new id>`, or
  `interim: <follow-up>`. A change that contradicts a record needs
  `supersede` or `interim`; it cannot be silent.
- **Data changes.** Every table, type or contract read or written, with how its
  semantics were verified. Verify what is inherited; never assume a column or
  field means what its name suggests. A row verified by `TODO` blocks approval.
- **Risks** and which phase retires each.
- Everything under the `design` extension point.

If the design turns on a genuine hinge (a spike result, an external contract
not yet agreed), plan **only up to the hinge**, state that a second planning
pass follows it, and stop after that phase. Most work has no hinge.

## 4. Shared context

Written once, assumed by every phase: mandatory reading, patterns to mirror
with `file:line`, how to run and reset the system, validation commands, and
explicit scope limits. Then any sections under the `sections` extension point.

## 5. Phases

Cut phases by verification boundary, following `references/phases.md`:

- Phase 1 fixes the contract (schema, types, shared enums, interface shapes,
  or the spike). Everything later mirrors it.
- Each later phase is independently verifiable against that contract and ends
  with executable proof that does not depend on later phases.
- Each phase fits one agent loop with headroom. Split a phase that needs more
  than a session; merge phases that would be validated together.
- Tests and documentation are done-criteria inside the phase they belong to.
  Never create a phase named tests, e2e, docs, deploy or sign-off.
- Non-agent work (human sign-off, external teams, deploys, pilots) goes in the
  **Milestones outside this plan** table and onto the tracker item, never into
  a phase.
- In a plan with more than one repository, every phase names the one
  repository it changes on a **Repo:** line; a repository boundary is a
  verification boundary. The contract phase lands in the repository that
  provides the contract and consumers follow, so each repository's change is
  backward-compatible on its own.
- Append the `done-criteria` extension content to every phase.

Each phase lists tasks as `CREATE | UPDATE path — what`, its done-criteria,
and an empty **Checkpoint** line for the implementer. More than about five
phases is a signal to look for ceremony or tracker items that crept in; say so
if it happens.

## 6. UAT script

Write the UAT script following `references/uat.md`: one scenario per
delivered acceptance criterion, with the role and data to start from,
numbered steps a person performs, and the observation that proves it. A
bug-fix plan uses its reproduction steps; a technical plan may state `none`
with the reason. It runs locally at the end of implementation, live after the
PR, and from the tracker by the product owner, so write it for someone who
did not build the feature.

## 7. Write, check, offer

1. Write the file to `artefacts.plan_dir/{PLAN_ID}.plan.md` from
   `templates/plan.md`. If a plan with that id exists, stop and suggest
   `amend`.
2. If `tracker.type` is not `none`, record the milestones on the tracker item
   when access exists; otherwise list them for the user to add.
3. Run the checks: every delivered acceptance criterion maps to at least one
   phase's done-criteria; no data row is verified by `TODO`; no forbidden phase
   names; phase 1 is a contract or a spike; every delivered criterion has a
   UAT scenario; in a multi-repo plan every phase names one repository from
   `repos:` and phase 1 is in the providing repository; plus everything under
   the `checks` extension point. Report any
   failure and fix it before offering the plan.
4. Offer the plan for approval with a five-line summary: kind, criteria
   delivered and deferred, phase list, hinge if any, open decisions. On the
   user's approval set `status: approved` in the frontmatter.

## Amend mode

`amend <plan path> <note>`: read the plan, apply the note to the affected
section or phase, record the amendment under that phase's **Checkpoint** line
(or under **Decisions** when it changes one), and leave everything else
untouched. Never regenerate a plan; a plan that needs regenerating was wrong
about its hinge, and that is a second planning pass on the remaining phases.

## Never

- Implement, commit, or open a PR.
- Invent personas, business value, or success metrics the trigger does not
  state.
- Put a tracker milestone, a sign-off, or a deploy in a phase.
- Write a plan against requirements nobody has signed off when the lane
  question says they must.
