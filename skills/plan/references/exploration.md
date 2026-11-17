# Exploration agents

Launch these in parallel for any change beyond a localised edit. Use the
read-only explorer agent type where the host provides one. Each prompt ends
with the same request: return the five to ten files that matter most, with one
line on why. The planner reads those files itself afterwards.

## Where: locate

```
Find where the code for {feature area} lives and what already exists that this
work should reuse or mirror.

Return, with file:line references:
- the entry points (routes, handlers, commands, jobs) for {area}
- the data access layer and the schema or types it depends on
- an analogous feature that was built the way this one should be, and the
  pattern it follows
- the tests that cover {area} and how they are structured (unit, integration,
  e2e, fixtures)
- configuration, feature flags, or permissions that gate {area}
- the validation commands this project uses (lint, typecheck, test, build)

Do not propose a design. Report what exists. End with the 5–10 files most
worth reading in full, one line each on why.
```

## How: trace

```
Trace how {behaviour} currently works, end to end, in this codebase.

Follow one concrete request or event from its entry point to its side effects:
control flow, data flow, state changes, external calls, error handling, and
what is observable at each step. Note every contract the path depends on
(schema columns, event shapes, API responses) and whether its meaning is
documented or merely implied by a name.

Report file:line for each step. Flag anything that contradicts {the request}
or that the request seems to assume without checking. Do not propose changes.
End with the 5–10 files most worth reading in full, one line each on why.
```

## For a bug fix: root cause

```
Establish the root cause of {symptom}.

Reproduce it if possible (test, command, or data). List the competing
explanations, then falsify all but one with evidence (file:line, test output,
data). State the causal chain from trigger to symptom, the smallest change
that breaks the chain, and the regression test that would have caught it.

Report evidence, not opinion. If you cannot reproduce it, say exactly what you
tried and what is missing.
```

## Merging results

- Prefer the trace over the locate when they disagree; the trace saw the code
  run.
- Any contract the trace marked "implied by a name" becomes a row in the
  plan's data-changes table with verification required.
- Read every file both agents named. If the decisive file is not on either
  list, the exploration was too narrow: run one more targeted trace.
