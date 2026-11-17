---
id: {PLAN_ID}                 # equals the trigger id: PRD id, revision id, issue id, decision id, or dated slug
title: {Title}
kind: {feature | revision | bug-fix | technical}
trigger: {path or reference to the PRD, revision, issue, decision record, or "inline"}
branch: {branch name}
tracker: {tracker item reference, or none}
status: draft                 # draft | approved | in-progress | complete
created: {YYYY-MM-DD}
---

# {PLAN_ID} — {Title}

## Brief

{For a plan with no PRD: three to six sentences on what, why, who, and the
observable result that proves it. For a plan with a PRD or revision: one line
linking it and naming the acceptance criteria this plan delivers.}

**Delivers:** {AC1, AC2, AC4} · **Defers:** {AC3 → follow-up reference}

## Design

### Decisions

| # | Decision | Alternatives rejected | Date | Durable? |
|---|---|---|---|---|
| D1 | | | | yes / no |

Durable decisions are promoted to decision records at wrap-up.

### Documents reconciled

Decision records, patterns and reference docs this work touches, with a note each.

| Document | Note |
|---|---|
| | follow / extend / supersede: {new id} / interim: {follow-up} |

### Data changes

| Table or type | Change | Owner | Verified by |
|---|---|---|---|
| | new / altered / read only | | {test, schema comment, decision record, or TODO} |

### Risks

| Risk | Likelihood | Mitigation or phase that retires it |
|---|---|---|
| | | |

## Shared context

Written once; every phase assumes it.

### Mandatory reading

- `{path}` — {why}

### Patterns to mirror

| Concern | Reference | Pattern |
|---|---|---|
| | `{file:line}` | {one line} |

### How to run

```
{start services, seed data, reset state, verify ready, tear down}
```

### Validation commands

```
{lint} ; {typecheck} ; {test} ; {e2e} ; {build}
```

### Not building

- {explicit scope limits for the implementer}

## Phases

Each phase ends at a checkpoint: validation green, a commit, a note under
**Checkpoint**. Phase 1 fixes the contract everything else mirrors.

### Phase 1 — {Contract: schema, types, interfaces, or the spike}

**Delivers:** {what exists after this phase}
**Tasks:**
1. {CREATE | UPDATE} `{path}` — {what}
2. …

**Done when:**
- {executable proof: test name, command, golden sample}
- {tests and docs for this phase are included here, never as a later phase}

**Checkpoint:** _(filled at implementation)_

### Phase 2 — {Name}

**Delivers:**
**Depends on:** Phase 1
**Tasks:**
1.

**Done when:**
-

**Checkpoint:** _(filled at implementation)_

## Milestones outside this plan

Non-agent work recorded on the tracker item, listed here for the reader only.

| Milestone | Who | Blocks |
|---|---|---|
| {sign-off, deploy, external team change, pilot} | | |

## Wrap-up

_(appended by the wrap-up skill)_
