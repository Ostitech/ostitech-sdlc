---
name: implement
description: Execute the phases of an approved plan with checkpoint discipline, one phase per loop or all phases in sequence, validating each phase before committing it and recording deviations in the plan. Use when the user asks to implement a plan, run the next phase, build phase N, execute the plan end to end, or invokes /implement. Never regenerates the plan, never skips validation, never edits the PRD.
argument-hint: <plan path> [next | <phase number> | all] [--repo <path>]
---

# Implement

Turn an approved plan into committed, validated code one phase at a time. The
plan is the state: every phase ends with a green validation, a commit, and a
Checkpoint note in the plan. Deviations amend later phases in place. Nothing
is regenerated.

**Input:** $ARGUMENTS. The first token is the plan path. The second is `next`
(default), a phase number, or `all`.

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
3. Read its `.sdlc/extensions/implement.md` if present.
   Level-two headings are extension points (`before-phase`, `validation`,
   `after-phase`); keep their content to apply at those steps. Warn once about
   unknown headings and ignore them.

## 1. Preflight

1. Read the plan. Stop if the file is missing or has no `## Phases` section.
2. Check `status` in the frontmatter. `approved` or `in-progress`: continue.
   `draft`: warn that the plan has not been approved and ask whether to
   proceed. `complete`: stop and say so.
3. Check the working tree. If it is dirty, list the changes and ask the user
   to commit, stash, or acknowledge before continuing.
4. Create or switch to the branch named in the plan frontmatter. If it exists
   on the remote, pull with fast-forward only. If the pull fails, stop and
   report.
5. Set `status: in-progress` in the frontmatter if it was `approved`.

### Multi-repo plans

When `repos:` names more than one repository, the target is the workspace
the plan lives in. Resolve each repository to a local checkout from
`workspace.repos[].path`; ask for the path when there is none, and stop if it
cannot be found. Steps 3 and 4 then run against the repository
of the selected phase, not the workspace, using the same branch name in every
repository. The plan stays in the workspace and is committed there.

## 2. Select the phase

- `next`: the first phase whose **Checkpoint** line is still the placeholder
  and whose **Depends on** phases are all checkpointed.
- `<phase number>`: that phase. Stop if any phase it depends on is not
  checkpointed; name the missing one.
- `all`: behave as `next`, then repeat step 2 after each checkpoint until no
  phase remains or a dependency blocks.

If the selected phase depends on a milestone listed under **Milestones
outside this plan**, stop and say which milestone must happen first. Do not
implement around it.

## 3. Read what the phase needs

Read the plan's **Shared context** (mandatory reading, patterns to mirror, how
to run, validation commands, not building) and the selected phase section
only. Open every file under mandatory reading. Do not read other phases unless
the current phase references them. Then run every step under the
`before-phase` extension point.

## 4. Implement the tasks

Work through the phase's tasks in order. After each task, run the cheapest
check that proves it: the typechecker, the test file you touched, a single
command. Mirror the patterns the plan names; where the plan's `file:line`
reference no longer matches the code, find the current equivalent and note it
as a deviation.

When a task cannot be done as written, do the smallest change that meets the
phase's done-criteria and record why in the deviations for this phase. Do not
widen scope to anything under **Not building**.

## 5. Validate the phase

Phase validation is, in this order:

1. Every validation command from the plan's **Validation commands** block (or
   `validation.*` from config when the plan has none).
2. Every item under the phase's **Done when** list, each with evidence.
3. Everything under the `validation` extension point.

On any failure, diagnose and fix, then re-run from step 1 of this list. Allow
at most three full attempts. After the third failure, stop and report as
described in `references/failure.md`. Never mark a phase done with a failing
check, and never weaken a check to make it pass.

## 6. Checkpoint

1. Replace the phase's **Checkpoint** placeholder with the checkpoint line
   from `references/checkpoint.md`: date, deviations, unplanned problems.
   Write `none` where there are none.
2. If a deviation invalidates an assumption in a later phase, amend that later
   phase's tasks or done-criteria in place and add `Amended {date}: {reason}`
   under its heading. Never rewrite the plan as a whole.
3. Stage the phase's code changes and the plan edit together and make one
   commit on the branch using the format in `references/checkpoint.md`:
   subject `{PLAN_ID} phase {n}: {phase title}`, body listing deviations and
   unplanned problems. The commit is found later by its subject, so no SHA is
   written into the plan. In a multi-repo plan the code commit goes to the
   phase's repository and the plan edit to the workspace, same subject, and
   the checkpoint line names the repository.
4. Run every step under the `after-phase` extension point.

## 7. Continue or finish

- In `all` mode, return to step 2.
- When every phase is checkpointed, run the plan's **UAT script** locally
  following `references/uat.md` and fill its `Local` column. Only when every
  row passes or is `n/a`, set `status: complete` in the frontmatter, commit
  that with the subject `{PLAN_ID} UAT local`, and tell the user to run the
  `close-plan` skill. A failing row is a failing validation: fix, re-run,
  three attempts, then stop and report.
- Otherwise report the phase just completed, the next phase, and anything the
  next phase is waiting on.

## Never

- Skip, weaken, or defer a validation check.
- Force-push, rewrite published history, or push to the default branch.
- Implement a phase whose dependencies are not checkpointed.
- Regenerate the plan. Amend the affected phase in place.
- Edit the PRD or revision document. A requirement that turns out wrong is a
  revision, raised through the `revise` skill.
- Continue past a milestone that belongs to a person or another team.
