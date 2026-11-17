# Running the UAT script locally

The UAT script in the plan is the acceptance criteria in executable form.
Run it once every phase is checkpointed, against the system started as the
plan's **How to run** section describes.

1. Start the system and seed the data each scenario's **Start as** needs.
2. For each row, perform the steps as written. Use a browser or the CLI when
   the session has one; do not shortcut a step by calling the code directly,
   because the script is checking what a person sees.
3. Record the result in the `Local` column: `pass`, `fail: {what was seen}`,
   or `n/a: {why}` for a step the session cannot perform (no browser, a
   device, an external system). Never mark `pass` for a step not performed.
4. List every `n/a` row for the user with what they need to do, and wait for
   their result before completing the plan.
5. A `fail` is a failing validation: diagnose, fix, re-run the row and any
   row it could affect. Three attempts, then stop and report as in
   `references/failure.md`.

Rows the script could not foresee (a label changed, a step is missing) are
corrected in the script as a deviation and noted in the commit body. The
script is amended, never rewritten, so the live run and the owner's run
check the same thing.
