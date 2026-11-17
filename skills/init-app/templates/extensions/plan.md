# Plan extensions

Each level-two heading below is an extension point of the `plan` skill. Content
under a heading is applied at that point. Delete the headings you do not need;
an empty file is a no-op. Keep content declarative: sections, tables,
checklists and file references. Procedure belongs in the skill, not here.

## context

<!-- Files or instructions the planner reads before exploring the codebase, every time.
Example:
- Read `docs/architecture.md` for the service boundaries.
- Read `docs/ux/playbook.md` when the work touches any screen. -->

## design

<!-- Extra rows or gates in the plan's design section.
Example:
- **Deploy path**: state which environments the change reaches and the switch that gates it.
- **Data dependencies**: every existing table or column the change reads or writes, with how its
  semantics were verified (test, schema comment, decision record). -->

## sections

<!-- Extra plan sections rendered after the design section.
Example:
### UX playbook compliance
| Concern | Playbook section | Primitive to use |
|---|---|---|
| | | | -->

## done-criteria

<!-- Appended to every phase's done-criteria.
Example:
- Decision records touched by this phase are updated or superseded in the same commit. -->

## checks

<!-- Verified before the plan is offered for approval.
Example:
- No phase named "tests", "docs", "e2e" or "deploy" exists. -->
