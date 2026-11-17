# Cutting phases

A phase serves the implementation, not the reader. It exists because the
implementer cannot hold the whole change in one loop, and because errors must
be caught before the next phase builds on them.

## The three tests a phase must pass

1. **Bounded.** It fits one agent session with headroom for exploration,
   implementation and validation. If a phase needs more than one session,
   split it; if two phases would be validated by the same command run, merge
   them.
2. **Verifiable alone.** Its done-criteria are executable (a named test, a
   command, a golden sample, a contract test with a simulated counterpart) and
   pass without any later phase existing.
3. **Committable.** The repository is in a consistent state after it: builds,
   lints, existing tests pass.

## Phase 1 is the contract

Whatever later phases mirror must be real before they are planned against it:
schema and migrations, shared types and enums, interface shapes, external
contracts, the test fixtures that encode them. When the biggest unknown is a
design question rather than a contract, phase 1 is a spike with a written
result, and the plan stops there for a second pass (a *hinge*).

This is also where inherited assumptions get verified. A plan that reads an
existing column, event or field states what it believes that thing means and
how it checked. "The name suggests" is not verification.

## Tests and docs are done-criteria

A phase that produces behaviour owns the tests that prove it and the
documentation that describes it. A separate phase called tests, e2e, docs,
journeys or hardening means earlier phases were allowed to finish unproven.

## Non-agent work is a milestone

Human sign-off, a change by another team, a deploy, a pilot, confirmation
testing by a person: these go in the plan's **Milestones outside this plan**
table and onto the tracker item. They are never phases, because the
implementer cannot do them and the plan would stall on them.

## Shape follows the codebase

- **Greenfield** work usually splits by layer after the contract: generators
  with golden samples, then orchestration with a simulated client, then the
  UI with its journeys. Nothing works end to end until late, and that is
  acceptable because each layer is proven alone and the contract was fixed
  first.
- **Changes to a mature system** usually split by capability, because the
  foundation exists and each capability is a thin path through it.
- **Integration risk** earns its own early phase only when a new external
  interface is the thing most likely to be wrong: build the thin path through
  it with a simulated counterpart before anything else.

Neither shape is prescribed. Ask what can be proven next.

## Parallel phases

Phases with no dependency between them and no overlapping files may run in
parallel worktrees off the feature branch. Mark `Depends on: none` and keep
their file lists disjoint. This is an optimisation; do not contort phases to
enable it.

## Smells

- More than about five phases. Look for ceremony, tracker items, or a PRD that
  is really two.
- A phase whose done-criteria are "reviewed" or "approved".
- A phase that touches every layer *and* every later phase touches every layer
  again. The contract was not fixed first.
- Phase names that are nouns for layers with no deliverable ("Backend").
