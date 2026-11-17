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

## Workspace variant

When `repo.kind` is `workspace`, append this block instead:

```markdown
<!-- sdlc-skills:start -->
## Delivery workflow

This is a workspace repository: it holds the PRDs and plans whose acceptance
criteria span more than one repository, in `{prd_dir}/` and `{plan_dir}/`.
Work that changes one repository is planned and tracked in that repository.
Configuration lives in `.sdlc/config.yaml`; `workspace.repos` lists the
repositories a cross-repo plan may name. The skills (`/prd`, `/revise`,
`/plan`, `/implement`, `/close-plan`) are vendored; never edit them.

A cross-repo plan names one repository per phase, contract first, and lands
as one pull request per repository. Open this workspace to investigate or
plan across repositories; open the repository a phase changes to implement
it.
<!-- sdlc-skills:end -->
```
