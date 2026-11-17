# CLAUDE.md block

Append exactly this block, with the directory names substituted from the
written config. If a block between the same two marker comments already
exists, replace its contents instead of appending.

```markdown
<!-- sdlc-skills:start -->
## Delivery workflow

This repository uses the SDLC skills (`/prd`, `/revise`, `/plan`,
`/implement`, `/close-plan`). Configuration and repo-specific
extensions live in `.sdlc/config.yaml` and `.sdlc/extensions/`; never edit
the vendored skills. PRDs live in `{prd_dir}/`, plans in `{plan_dir}/`.

Lane rule: small and needs no sign-off → plan mode, no artefact. Spans files
or sessions → a plan with an inline brief. Someone must sign off the
behaviour → PRD, then plan. Someone must sign off the architecture → decision
record, then plan.
<!-- sdlc-skills:end -->
```
