# Criteria

Score the run against the plan file it wrote under plans/. Each criterion is pass or fail.

1. Exactly one plan file was written, and it follows the plan template: frontmatter with id, kind, trigger, status; a Brief; a Design section with Decisions, Documents reconciled, Data changes and Risks; Shared context; Phases; Milestones outside this plan.
2. Phase 1 fixes the contract: it creates or alters the schema, migration, shared types or event shape before any behaviour is built.
3. No phase is named tests, e2e, docs, documentation, deploy, sign-off, review or hardening, and no phase consists only of writing tests or documentation.
4. Every phase has done-criteria that name executable proof (a test, a command, a sample) and that do not depend on a later phase.
5. Each of AC1 to AC4 appears in at least one phase's done-criteria or is explicitly deferred with a follow-up.
6. The plan has at most five phases, or it has more and says why.
7. No row in the Data changes table is verified by TODO.
8. The plan contains no implementation code beyond short illustrative snippets, and the run did not create or edit any file outside plans/.
