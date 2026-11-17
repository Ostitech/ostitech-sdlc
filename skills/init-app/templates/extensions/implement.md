# Implement extensions

Each level-two heading below is an extension point of the `implement` skill.
Content under a heading is applied at that point. Delete the headings you do
not need; an empty file is a no-op. Keep content declarative: steps to run,
commands, checklists. Procedure belongs in the skill, not here.

## before-phase

<!-- Steps run before each phase starts.
Example:
- Pull the latest reference data snapshot: `pnpm seed:refresh`.
- Confirm the feature switch for this work is off in local config. -->

## validation

<!-- Commands or checks added to every phase's validation.
Example:
- `pnpm db:check-migrations` must report no pending migrations.
- No file under `packages/*/src` imports from another package's internals. -->

## after-phase

<!-- Steps run after each checkpoint commit.
Example:
- Post the checkpoint note as a comment on the tracker item. -->
