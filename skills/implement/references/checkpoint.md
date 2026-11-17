# Checkpoint format

A checkpoint is one commit that carries the phase's code and the plan's
updated Checkpoint line together. Both use fixed formats so the close-plan
skill can parse them, and the commit is located by its subject.

## Commit message

```
{PLAN_ID} phase {n}: {phase title}

Deviations:
- {what changed from the plan and why}, or "none"

Unplanned problems:
- {problem}: {cause}: {how it was handled}, or "none"

Amended later phases:
- Phase {m}: {reason}, or "none"
```

Subject under 72 characters; truncate the phase title, not the id. For a
bug-fix plan whose id is an issue reference, keep the reference exactly as
`tracker.issue_ref` writes it so the tracker links the commit.

Example:

```
PRD-014 phase 2: Order totals service

Deviations:
- Used the existing MoneyRounding helper instead of adding a new one; the
  plan assumed it did not exist.

Unplanned problems:
- Test database seed did not include a zero-quantity line; added one to the
  fixture.

Amended later phases:
- Phase 3: dropped task 2 (new rounding helper) since phase 2 reused the
  existing one.
```

## Checkpoint line in the plan

Replace the phase's placeholder with:

```
**Checkpoint:** {YYYY-MM-DD} · Deviations: {text or none} ·
Unplanned: {text or none}
```

Keep it to two or three lines. The commit body carries the detail. When a
phase was reworked after a failed review round, append a second checkpoint
line below the first rather than overwriting it:

```
**Checkpoint:** 2026-03-02 · Deviations: none · Unplanned: none
**Checkpoint (round 2):** 2026-03-04 · Deviations: AC3 fix, see review · Unplanned: none
```

## Amendment note on a later phase

Directly under the later phase's heading:

```
_Amended {YYYY-MM-DD} by phase {n}: {one line reason}._
```

Then edit that phase's tasks or done-criteria in place. Leave the rest of the
plan untouched.
