# The bounded fix loop

Validation failing is normal. Validation failing three times in a row on the
same phase means the plan, the environment, or the understanding is wrong,
and that is a decision for a person.

## One attempt

An attempt is one full pass of the phase validation list: all validation
commands, all done-criteria, all `validation` extension content. Fixing a
single test and re-running only that test is part of an attempt, not a new
one.

Within an attempt:

1. Read the failure output in full. Do not guess from the first line.
2. Name the cause before changing anything. "The test expects X, the code
   does Y because Z."
3. Make the smallest change that addresses the cause.
4. Re-run the cheapest check that proves it, then the full list.

## Three attempts, then stop

After the third full failure, stop. Do not try a fourth variation, do not
disable the check, do not mark the phase done with a note. Leave the working
tree as it is (uncommitted) so the user can see the state.

## What to report when stopping

```
Phase {n} stopped after 3 validation attempts.

Failing: {check name or command}
Output (last 20 lines):
  ...

Attempts:
1. {cause named} → {change made} → {result}
2. ...
3. ...

Likely reason the loop is not converging:
- plan assumption wrong: {which}, or
- environment: {what is missing or different}, or
- the check itself is wrong: {why}

Working tree: uncommitted changes in {files}. Nothing was committed for this
phase.

Suggested next step: {amend the plan with ... | fix the environment by ... |
confirm the check should be ...}
```

Name the likeliest reason; do not list all three as equally likely unless they
genuinely are.

## Recoverable versus not

- A flaky test that passes on re-run without changes: note it as an unplanned
  problem, continue, and file it at close-out. Do not count it as an attempt.
- A failure in a check unrelated to this phase's files (pre-existing
  breakage): report it, confirm with the user whether to proceed, and record
  the decision in the checkpoint. Do not fix unrelated code inside the phase.
- A failure that needs a change to a phase already checkpointed: that is a
  deviation. Make the change, record it, and amend the earlier phase's
  checkpoint with a second line rather than rewriting history.
