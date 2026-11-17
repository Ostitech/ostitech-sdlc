# UAT script

The acceptance criteria say what must be true. The UAT script says how a
person checks it: which screen, which control, what to type, what to see. It
is the acceptance criteria in executable form, so it needs implementation
knowledge, which is why it lives in the plan and not the PRD.

## Writing it

- One scenario per acceptance criterion the plan delivers. A criterion that
  needs several paths (happy path, a validation error) gets several rows,
  each tied to the same AC.
- **Start as**: the role to be signed in as and the data or state that must
  exist first. Name seed data or a setup step; never assume the tester knows.
- **Steps**: numbered, concrete, one action each. Name controls by their
  visible label, not their component. "Click Save", not "submit the form".
- **Expect**: what the tester sees or what has changed, checkable without
  reading code. A message, a row, a state, a value; not "it works".
- Write for someone who did not build the feature and will not read the
  plan. The product owner runs this from the tracker item.
- A bug-fix plan's scenario is the reproduction: the steps that failed, now
  with the expected correct result. A technical plan with nothing a person
  can observe writes `none` and says why.
- Keep it to what the acceptance criteria require. Edge cases that matter are
  acceptance criteria; if one is missing, that is a revision, not a UAT row.

## Three runs

| Run | When | By | Recorded |
|---|---|---|---|
| Local | End of `implement`, before the plan is complete | The implementer, against the running system | `Local` column |
| Live | `close-plan`, after the PR has deployed to the validation environment | The implementer or the user | `Live` column |
| Owner | After the tracker handoff | The product owner, from the tracker item | On the tracker |

A cell holds `pass`, `fail: {what was seen}` or `n/a: {why}`. A `fail` in
the local run blocks completion; a `fail` in the live run blocks the
tracker handoff.
