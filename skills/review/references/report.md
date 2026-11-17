# Review report template

Verdict first. A reader who stops after the first line knows whether the work
is done.

```markdown
# Review: {PLAN_ID} — {title} · Round {n}

**Verdict: PASS** — all gates hold. The work is done.
<!-- or -->
**Verdict: FAIL** — gate {k} ({name}) does not hold. See below.

Branch `{branch}` · PR {reference} · Plan `{plan path}` · Reviewed {YYYY-MM-DD}

## Gates

| Gate | Result | Evidence |
|---|---|---|
| 1. Acceptance criteria | pass / fail | see table below |
| 2. Plan conformance | pass / fail / n/a | {summary of conformance findings} |
| 3. {extension gate name} | pass / fail | {evidence} |

### Acceptance criteria

| AC | Result | Evidence |
|---|---|---|
| AC1 | pass | `orders.test.ts > totals include tax` passes; observed total 118.00 for fixture #3 |
| AC2 | fail | no test covers the zero-quantity line; observed total 0.00, expected 10.00 |

### Conformance findings (gate 2)

| Finding | Gate impact | Detail |
|---|---|---|
| Change with no task | fails | `src/export/csv.ts` added; not in any phase, no checkpoint deviation |
| Deviation recorded | conformant | Phase 2 reused `MoneyRounding`; checkpoint notes it |

## What must change for a PASS

{Only on FAIL. One line per failing item, naming the criterion or finding and
the smallest fix that would satisfy it. No design advice.}

## Advisory findings (filed, not blocking)

Grouped by category. These do not affect the verdict and do not start a
review round.

### Correctness risk
- `src/orders/totals.ts:41` — rounding happens before summing; fine for the
  delivered criteria, would drift for multi-currency. Filed as {ref}.

### Maintainability
- `src/orders/totals.ts:12-60` — three near-identical branches; a table would
  do. Filed as {ref}.

### Test coverage
- No test for negative quantities; outside the delivered criteria.

## Follow-ups

| Item | Tracker ref | Owner |
|---|---|---|
| Multi-currency rounding | {ref} | |

## Round history

| Round | Date | Outcome | Scope |
|---|---|---|---|
| 1 | {date} | FAIL on AC2 | full |
| 2 | {date} | PASS | AC2 and `totals.ts` path only |
```

## Rules for the report

- Evidence is a test name with its result, a command with its output, or an
  observed state. "Looks correct" is not evidence.
- On PASS, omit "What must change". On FAIL, that section lists only gate
  items.
- Advisory findings cite `file:line`. One or two lines each. No fix proposals
  beyond a phrase.
- Keep the round history so a third failure of the same gate is visible.
- Never include an improvements, alternatives, or roadmap section.
