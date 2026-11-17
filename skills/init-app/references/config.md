# Configuration written by the init-app skill

Contract versions read: **1**. Writes contract version **1**.

Target: `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml`, validated against
`templates/sdlc.config.schema.json`. On a re-run, existing values are kept
and only missing keys are filled.

| Key | Default | Source on first run |
|---|---|---|
| `version` | `1` | Fixed |
| `repo.kind` | `app` | Detected (nested git repositories and no build → `workspace`), confirmed |
| `repo.name` | `null` | Default: the repository name from the origin URL, else the folder name (a worktree's folder name is not the repository's) |
| `workspace.repos` | `[]` | Detected from nested repositories when the kind is `workspace`, confirmed |
| `artefacts.prd_dir` | `prds` | Default, or the existing folder when the owner chooses to continue in it |
| `artefacts.plan_dir` | `plans` | Default, or the existing folder when the owner chooses to continue in it |
| `artefacts.investigations_dir` | `investigations` | Default, or the existing folder when the owner chooses to continue in it |
| `artefacts.prd_layout` | `folder` | Default; `flat` when the owner continues with flat existing PRDs |
| `artefacts.mockup_dir` | `null` | Default (inside the PRD folder), or detected mockup folder |
| `ids.prd` | `{slug}` | Asked; `{tracker}` and any existing artefact pattern offered |
| `ids.revision` | `{prd}-R{seq:2}` | Asked with the above |
| `tracker.type` | `none` | Asked; default from the git remote and tracker signals in the repository |
| `tracker.issue_ref` | `#{n}` | Derived from tracker type |
| `tracker.org`, `tracker.project` | unset | Parsed from an Azure DevOps remote |
| `tracker.uat_state` | `null` | Default; listed in the report as worth setting |
| `environments.uat` | `null` | Default; listed in the report as worth setting |
| `branches.*` | `docs/{id}`, `feat/{id}`, `fix/{id}` | Default |
| `roles` | `[]` | Asked; roles declared in code offered |
| `design_system.path`, `design_system.guide` | `null` | Asked when a candidate folder is detected |
| `placeholder_data` | `null` | Asked only when a design system is set |
| `validation.*` | `null` | Detected from the project manifest; left null for a workspace |
| `context.always_read` | `[]` | Default |
| `context.knowledge_index` | `false` | Asked when an index is detected |
| `learning.gotchas_dir`, `learning.decisions_dir` | `null` | Asked; detected folders offered |

## Organisation defaults

A vendored skill folder may carry `sdlc.defaults.yaml`: a partial config in
the same shape as `.sdlc/config.yaml`, validated against the same schema. Its
values take precedence over detection and the built-in defaults, and lose to
an existing config and to answers given during the run. Keys `repo`,
`workspace` and `validation` are ignored in it. An `extensions/` folder
beside it supplies the initial `.sdlc/extensions/<skill>.md` files. See
`references/org-defaults.md`.

## Other files written

| File | From |
|---|---|
| `.sdlc/sdlc.config.schema.json` | `templates/sdlc.config.schema.json` |
| `.sdlc/extensions/<skill>.md` | The organisation defaults' `extensions/<skill>.md`, else `templates/extensions/<skill>.md` |
| `<artefact dirs>/.gitkeep` | Created |
| `CLAUDE.md` block | `references/claude-md-block.md` |
