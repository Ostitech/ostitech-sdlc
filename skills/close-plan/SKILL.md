---
name: close-plan
description: Close out a fully checkpointed plan by appending a one-page Close-out section (outcomes against acceptance criteria, deviations, unplanned problems, decisions to promote, follow-ups), filing gotchas and decision records where the repository keeps them, and marking the plan and its PRD or revision shipped. Use when the user asks to wrap up, close out, or finish a plan, or invokes /close-plan after the PR has merged. Never rewrites earlier plan sections.
argument-hint: <plan path>
---

# Close-out

The learning loop. Everything the implementation discovered that outlives
this work leaves the plan now: unplanned problems become gotchas, durable
decisions become decision records, loose ends become tracker items. The plan
gets a one-page closing section and is marked complete.

**Input:** $ARGUMENTS (the plan path).

## 0. Load configuration

1. Read `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml` if present; apply defaults
   from `references/config.md` for anything missing.
2. Read `${CLAUDE_PROJECT_DIR}/.sdlc/extensions/close-plan.md` if present.
   Level-two headings are extension points (`sections`, `promote`); keep
   their content. Warn once about unknown headings and ignore them.

## 1. Preconditions

1. Read the plan. Every phase must have a filled **Checkpoint** line. If any
   is still the placeholder, list those phases and stop; close-out runs after
   implementation, not instead of it.
2. If a **Close-out** section already has content, stop and say the plan is
   already closed out. Do not overwrite it.
3. Find the PR for the plan's branch when PR access exists and note its
   reference and merge state. Close-out normally runs after merge; if the PR is
   open, say so and continue only on the user's confirmation.

## 2. Collect outcomes

For each acceptance criterion under **Delivers** in the plan's Brief, record
the result and the evidence: a review report's evidence if one exists on the PR,
otherwise the test names from the checkpointed commits. Criteria under
**Defers** are listed as deferred with their follow-up reference. Anything
dropped during implementation is listed as dropped with the checkpoint that
records it.

## 3. Collect deviations and problems

From every **Checkpoint** line and its commit body:

1. **Deviations**: one line per phase that deviated, with the reason.
2. **Unplanned problems**: each problem with its cause. Mark a problem as
   worth filing when it is non-obvious (the cause was not visible from the
   symptom) or likely to recur (environment, tooling, a trap in an existing
   API). Skip one-off typos and local mistakes.

For each problem worth filing, when `learning.gotchas_dir` is set, write one
short file there from `references/gotcha.md`: title, date, area, and a
one-paragraph body covering symptom, cause and fix. When the directory is not
set, list them under the close-out for the user to file. Apply any override
under the `promote` extension point.

## 4. Promote decisions

For each row in the Design section's **Decisions** table marked durable:

1. When `learning.decisions_dir` is set, draft a decision record there from
   `references/decision-record.md` with status `proposed`, the plan id as
   context, and the alternatives rejected. Number it after the highest
   existing record in that directory.
2. When the directory is not set, list the decision in the close-out with the
   recommendation to record it.
3. Decisions not marked durable are not promoted. Do not re-judge them.

Apply any override under the `promote` extension point.

## 5. Follow-ups

Gather deferred criteria, findings a review left unresolved, and anything
the checkpoints flagged for later. When `tracker.type` is not `none` and
access exists, create one tracker item per follow-up and record the
reference. Otherwise list them with an owner column for the user.

## 6. Write the section

1. Append the Close-out section to the plan from `templates/close-out.md`, then
   any `sections` extension content.
2. Cap it at one page, about sixty lines. Trim in this order: evidence detail,
   then follow-up detail, then deviation detail. Never trim the outcomes
   table or the decisions-to-promote table.
3. Set `status: complete` in the plan frontmatter.
4. Set `status: shipped` in the PRD or revision the plan's `trigger` names,
   if any, and add a revision-history row linking the plan when the document
   has one.
5. Commit the plan edit, the PRD edit, and any gotcha or decision files
   together with the message `{PLAN_ID} close-out`.

## 7. Report

Print five lines: criteria passed, deferred and dropped; deviations count;
gotchas filed with paths; decision records drafted with paths; follow-ups
created with references.

## Never

- Rewrite the Design, Shared context, or Phase sections. Close-out appends.
- File an advisory code-quality finding as a gotcha; those are follow-ups.
- Promote a decision the Design section did not mark durable.
- Exceed the page cap by adding sections.
- Run before every phase is checkpointed.
