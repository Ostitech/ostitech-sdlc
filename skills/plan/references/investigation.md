# Investigations

An investigation is written when a bug's cause is not obvious from the report.
It is short, evidence-led, and kept after the fix because the next person to
hit the area will want it.

Location: `artefacts.investigations_dir/{issue id}-{slug}.md`.

```markdown
---
issue: {tracker reference}
status: open | resolved
created: {YYYY-MM-DD}
---

# {Issue id} — {symptom in one line}

## Symptom
What was observed, by whom, where, and how often. Exact messages and data.

## Reproduction
Steps, test, or query that shows it. "Could not reproduce" with what was tried.

## Explanations considered
| # | Explanation | Evidence for | Evidence against | Verdict |
|---|---|---|---|---|

## Root cause
The causal chain from trigger to symptom, with file:line.

## Smallest fix boundary
What must change, and what must not.

## Regression check
The test or check that would have caught this.

## Does the specification hold?
Yes: this is a bug fix. No: this is a revision; stop and route to the
`revise` skill before planning.
```

The last section is the lane check. A fix that would change agreed behaviour
is a revision, however small.
