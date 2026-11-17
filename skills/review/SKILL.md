---
name: review
description: Verdict-first review of a pull request, branch or plan, where only three gates decide PASS or FAIL (acceptance criteria hold, the diff conforms to the plan, configured extra gates) and every other finding is filed as advisory. Use when the user asks to review a PR, review a feature, check whether a story is done, re-review after fixes, or invokes /review. Never fixes code and never fails a story on an advisory finding.
argument-hint: <PR reference | branch | plan path>
---

# Review

Answer one question: is this work done? Three gates decide the verdict and
nothing else can. Code quality, refactoring ideas and coverage gaps are
receipts filed for later, never reasons to withhold a pass. Iterate on
failures, not on ideas.

**Input:** $ARGUMENTS (a PR reference, a branch name, or a plan path).

## 0. Load configuration

1. Read `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml` if present; apply defaults
   from `references/config.md` for anything missing.
2. Read `${CLAUDE_PROJECT_DIR}/.sdlc/extensions/review.md` if present.
   Level-two headings are extension points (`gates`, `advisory`); keep their
   content. Warn once about unknown headings and ignore them.

## 1. Locate the work

1. Resolve the input to a branch and a diff against the default branch. For a
   PR reference, use the host's PR access (`gh`, the tracker, or the session's
   PR tools) to get the branch, body, and existing review comments.
2. Find the plan: a path in the PR body, else a file in `artefacts.plan_dir`
   whose id appears in the branch name. No plan: say so, review against the
   PR description as the only source of intent, and mark gate 2 as not
   applicable.
3. Find the PRD or revision the plan's `trigger` names, if any. Read it. The
   acceptance criteria the plan lists under **Delivers** are the ones under
   review; deferred criteria are out of scope.
4. Read the plan's **Checkpoint** lines; they are the implementer's record of
   deviations and are evidence for gate 2.
5. Check for a prior review report on this PR. If one exists, this is a later
   round: see step 5.

## 2. Gate 1: acceptance criteria hold

For each delivered acceptance criterion:

1. Find the test or check that proves it. A criterion with no test is not
   proven by the code looking right.
2. Run the test suite the plan's validation commands name. Record pass or
   fail per criterion.
3. Where the plan's **How to run** section allows, run the behaviour locally
   and observe the result the criterion describes. Prefer the oracle (data,
   response, state) over the screen.
4. Record evidence per criterion: test name and result, command output, or
   an observed state.

Any delivered criterion that does not hold fails the gate.

## 3. Gate 2: plan conformance

Run the `review-conformance` skill with the plan path and the diff range. It
returns structured findings: plan tasks with no change, changes with no task,
deviations not recorded in Checkpoint lines, criteria claimed without
evidence, data-changes rows still marked TODO.

A finding fails the gate when it means the work does something the plan did
not say, or omits something the plan required, without a recorded deviation.
A recorded deviation with a reason is conformant.

## 4. Gate 3 and advisory reviewers

1. Apply every gate under the `gates` extension point. Each needs evidence
   the same way gates 1 and 2 do.
2. Run each skill named in config `reviewers`, then any host-provided code
   review skill present in the session. Collect their findings.
3. Classify each finding: it is a gate failure only if it breaks a delivered
   criterion, makes stored or displayed data wrong on the core path, or hits
   an extension gate. Everything else is advisory, grouped under the
   categories the `advisory` extension point names (default: correctness
   risk, maintainability, test coverage, performance, convention).

## 5. Round discipline

- A failing gate gets as many rounds as it takes. Re-review it after each fix
  until it holds.
- A round is scoped to what failed: the failed criteria, the findings the fix
  claims to close, and any passed criterion whose code path the fix touched.
  Do not re-run the full review.
- Advisory findings never start a round. New advisory observations in a
  later round are added to the filed list and do not block the pass.
- If the same gate fails three rounds running, say so plainly: the fix is not
  converging, the criterion may be wrong, or the environment cannot prove it.
  Let the user decide.

## 6. Verdict and report

1. All gates hold: **PASS**. Say the work is done. Do not soften it because
   advisory findings exist.
2. Any gate fails: **FAIL**, naming the gate, the criterion or finding, and
   the evidence.
3. Write the report from `references/report.md`: verdict first, gates table
   with evidence, advisory findings with `file:line`, follow-ups.
4. Post the report to the PR when PR access exists; otherwise print it.
5. File advisory findings as tracker items when `tracker.type` is not `none`
   and access exists, one item per theme, linked from the report. Otherwise
   list them for the user to file.

## Never

- Fix code, even a one-line finding. Report it.
- Turn a PASS into a FAIL on an advisory finding, however large the list.
- Produce an improvements section, alternative designs, or a hardening plan.
- Re-review passing criteria whose code the fix did not touch.
- Review deferred acceptance criteria as if they were delivered.
