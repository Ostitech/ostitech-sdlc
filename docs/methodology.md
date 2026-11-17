# The methodology

A light procedure for agentic software delivery, built on Claude Code's native
features. It defines two documents, one way of splitting work, a taxonomy of
changes, and the rule that chooses how much ceremony a piece of work gets.

The procedure is deliberately small. The durable value in a repository comes
from its context layer (decision records, patterns, reference docs retrieved on
demand), not from the per-change paperwork. This document covers the per-change
procedure only.

## Two documents

| Document | Question it answers | Who signs it off | Owned by |
|---|---|---|---|
| **PRD** | What are we building, why, for whom, and how will we know it is right? | Product owner or client | Product |
| **Plan** | How will we build it, in what order, and how do we prove each step? | Tech lead | Engineering |

A PRD contains problem, users, roles and permissions, today's behaviour,
proposed behaviour, acceptance criteria, out of scope, dependencies, open
questions, and links to mockups. It is written in the product owner's
language.

**A PRD never contains design.** No schema, no event types, no integration
mechanics, no phase table. If intake surfaces one of those, it becomes an open
question in the PRD and a decision in the plan.

A plan opens with a design section (decisions, documents reconciled, data
changes, scope committed for this delivery, risks), then the shared material an
implementer needs once (patterns to mirror, how to run and validate), then one
section per phase. Durable decisions made in a plan are promoted to decision
records at close-out; the plan is not the long-term home of a decision.

There is no third document between them. A product requirements document that
also carries technical design and a schedule is a PRD that has swallowed two
other documents, and it will be rewritten three times.

## Identity and layout

A PRD is an enduring record: it is amended for as long as the feature exists.
Its identity is therefore the feature's name, not a counter, a date or an
author.

```
prds/stock-adjustments/prd.md                 the PRD; id: stock-adjustments
prds/stock-adjustments/R01-reason-codes.md    revision; id: stock-adjustments-R01
prds/stock-adjustments/mockups/
plans/stock-adjustments.plan.md               plan for the feature
plans/stock-adjustments-R01.plan.md           plan for the revision
plans/213-reject-missing-reason.plan.md       plan for a bug fix, by issue number
plans/20260118-upgrade-orm.plan.md            plan for a technical change
```

Two developers can no longer clash on a number, because there is none. They
can clash on a name, and that is a signal worth having: the same feature is
being started twice. The tracker item number, recorded in the frontmatter, is
the short reference for conversation and commits. Organisations that want a
numeric id can put the tracker number in the id pattern.

A PRD is never archived by moving it. When a feature is replaced, its PRD is
marked superseded and points at the successor. Plans are transient and may be
archived once closed.

## One plan, phased implementation, one PR

Each piece of work produces **one plan** and lands as **one pull request**.
Implementation runs through the plan's phases in order. Each phase ends at a
checkpoint:

1. the phase's validation is green,
2. a commit on the feature branch,
3. a short note appended to the plan recording what deviated.

If a deviation invalidates an assumption in a later phase, that phase's section
is amended. Plans are amended, never regenerated.

A second planning pass happens only when the first phase was a genuine design
hinge (a spike, or an external contract whose outcome changes the design). Plan
up to the hinge, implement it, then plan the rest. Most work has no hinge.

## Phases

A phase exists to serve the implementation, not the reader. Phases are cut so
that each one:

- fits one agent loop with headroom for exploration, implementation and
  validation;
- ends with executable proof that is correct **without the later phases
  existing**;
- can be committed on its own.

Rules that follow:

- **The contract comes first.** Schema, types, shared enums, external interface
  shapes, and any spike that retires the largest unknown. Everything later
  mirrors it.
- **Tests and docs are never phases.** They are the done-criteria of the phase
  they belong to. A separate "e2e" or "docs" phase means the earlier phases were
  not verifiable on their own.
- **Non-agent work is not a phase.** Human sign-offs, external teams, deploys
  and pilots are milestones on the tracker item, not rows in the plan.
- **Shape follows the codebase.** Greenfield work tends to split by layer
  because the foundation does not exist yet. Changes to a mature system tend to
  split by capability because it does. Neither shape is prescribed.

The phase count is whatever the verification boundaries produce. A plan with
more than about five phases is worth a second look, usually because ceremony or
tracker items crept in, but the number is a smell, not a rule.

## Change taxonomy

Every piece of work is one of four kinds. The kind decides the sign-off
artefact, the plan lane, and where the work's identity comes from.

| Kind | What it changes | Sign-off artefact | Plan | Identity |
|---|---|---|---|---|
| **Feature** | Adds agreed behaviour | PRD | PRD file plus plan | The PRD's slug |
| **Revision** | Changes agreed behaviour of something shipped | Revision document; parent PRD amended inline | Plan, often one phase | Slug plus revision number |
| **Bug fix** | Restores agreed behaviour | The tracker issue, plus an investigation when the cause is not obvious | Plan mode, or a short plan if it spans files | Issue number plus slug |
| **Technical change** | Changes how, not what | A decision record when it changes a decision; otherwise none | Plan with an inline brief | Decision id or a dated slug |

Boundary cases:

- A bug fix that reveals the specification was wrong is a revision. Switch
  lanes before writing code.
- A revision that needs a data-model change is still a revision at the PRD
  level. The schema change is a decision in the plan.
- An engineering clarification is not a revision. A revision must add or change
  at least one acceptance criterion; otherwise it is an inline edit to the PRD
  with a line in its revision history.
- A small adjustment that changes nothing anyone agreed to is plan mode with no
  artefact.

## Lanes

The question that picks the lane:

> Does anyone other than the implementer need to sign off **what** is being
> built before **how** is decided? If so, is that about behaviour or about
> architecture?

| Answer | Lane |
|---|---|
| No, and it is small | Plan mode. No artefact. |
| No, but it spans files or sessions | A plan whose first section is a short inline brief. |
| Yes, about behaviour | PRD, then plan. |
| Yes, about architecture | Decision record, then plan. |

The lightest lane is the default. Choosing a heavier lane than the work needs
is the most common failure of structured workflows, and the skills ask the lane
question explicitly at the start rather than assuming the heaviest.

## Close-out

Implementation ends with a close-out section appended to the plan: what shipped
against the acceptance criteria, deviations, unplanned bugs found, decisions
that should outlive this work, and follow-ups. It is capped at a page. The
close-out is the learning loop: unplanned bugs feed the repository's gotchas,
durable decisions become decision records, and the next plan reads both.

## What the skills enforce

| Skill | Enforces |
|---|---|
| `prd` | Lane question; no design in the PRD; acceptance criteria present; roles mapped |
| `revise` | Revision adds or changes an acceptance criterion; parent amended inline |
| `plan` | Trigger resolved to one of the four kinds; design section before phases; contract phase first; tests and docs as done-criteria; non-agent work routed to the tracker |
| `implement` | Checkpoint discipline; amend not regenerate; stop at human gates |
| `close-plan` | Page cap; promotion of decisions and gotchas |
| `init-app` | Config and extensions scaffold for a new repository |

Everything client-specific (identifiers, directories, role vocabulary, tracker,
design system, extra gates and sections) comes from the repository's
configuration and extension files, never from edits to these skills. See
[extension-points.md](extension-points.md).
