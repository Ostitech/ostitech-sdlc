# Review extensions

Each level-two heading below is an extension point of the `review` skill.
Content under a heading is applied at that point. Delete the headings you do
not need; an empty file is a no-op. Keep content declarative. Procedure
belongs in the skill, not here.

## gates

<!-- Findings that can fail the review, in addition to acceptance criteria and plan conformance.
Example:
- Stored or displayed money, quantity or classification values are wrong on the core data path.
- A row is written without the tenant or site scope the repository's data rules require. -->

## advisory

<!-- Finding categories to file but never block on.
Example:
- Naming and layout preferences.
- Refactors that would not change behaviour.
- Test coverage gaps outside the acceptance criteria. -->
