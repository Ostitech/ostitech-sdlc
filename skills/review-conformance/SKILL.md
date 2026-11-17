---
name: review-conformance
description: Read-only conformance check of a diff against its plan, run as a subagent by the review skill. Reports plan tasks with no change, changes with no task, deviations missing from Checkpoint lines, acceptance criteria claimed without evidence, and data-changes rows still marked TODO. Not invoked directly by users and never edits files.
argument-hint: <plan path> <diff range or branch>
context: fork
user-invocable: false
---

# Review conformance

Compare what the plan said would happen with what the diff did. Report
differences as structured findings. Make no judgement about whether the code
is good; that belongs to the review skill and its advisory reviewers.

**Input:** $ARGUMENTS. First token is the plan path. Second is a git range
(`main...feature`) or a branch name, which is compared against the default
branch.

## 1. Read the plan

Extract from the plan:

- Each phase's **Tasks** list as `CREATE | UPDATE path — what`.
- Each phase's **Done when** list.
- Each phase's **Checkpoint** line(s), including deviations and amendments.
- The **Delivers** line in **Brief**: the acceptance criteria claimed.
- The **Data changes** table and each row's **Verified by** cell.
- The **Not building** list.

## 2. Read the diff

Produce the file list with change type (added, modified, deleted, renamed)
and read the diff hunks. For test files, note which behaviours the tests
assert by name. Do not read files outside the diff except to resolve a
reference a task names.

## 3. Match and report

Produce findings in these five categories. Each finding carries a location
and one line of detail.

1. **Task with no change.** A plan task whose target path (or its current
   equivalent, if renamed) does not appear in the diff and whose phase has a
   checkpoint. Exclude tasks a checkpoint deviation says were dropped.
2. **Change with no task.** A file in the diff that no task names and that
   is not a test or fixture for a named task, not a lockfile or generated
   artefact, and not covered by a checkpoint deviation. Flag anything under
   **Not building** separately as `scope breach`.
3. **Unrecorded deviation.** A task done differently from its wording (other
   path, other approach, partial) with no matching deviation in that phase's
   checkpoint line or commit body.
4. **Criterion without evidence.** An acceptance criterion under **Delivers**
   with no test in the diff (or in the existing suite, when the plan names
   one) whose name or assertions correspond to it.
5. **Unverified data row.** A **Data changes** row whose **Verified by** cell
   still reads `TODO` or is empty, when the diff touches that table or type.

## 4. Output

Return exactly this structure and nothing else:

```
CONFORMANCE REPORT · {plan id} · {diff range}

Summary: {n} task-without-change · {n} change-without-task ({n} scope breach)
· {n} unrecorded deviation · {n} criterion-without-evidence · {n} unverified
data row

## Task with no change
- Phase {n}, task {k}: `{path}` — {detail}

## Change with no task
- `{path}` ({added|modified|deleted}) — {detail} [scope breach]

## Unrecorded deviation
- Phase {n}, task {k}: {what differs} — {detail}

## Criterion without evidence
- {AC id}: {criterion text, truncated} — {what was searched}

## Unverified data row
- `{table or type}`: {change} — Verified by: {cell content}

Conformant:
- {one line per phase that matched its tasks and recorded its deviations}
```

Write `none` under an empty category. Keep each finding to one line.

## Never

- Edit, create, or delete any file.
- Judge code quality, style, performance, or design.
- Decide the verdict. The review skill decides what fails a gate.
- Read beyond the plan, the diff, and files a task names.
