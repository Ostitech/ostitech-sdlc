# Configuration written by the init-app skill

Contract versions read: **1**. Writes contract version **1**.

Target: `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml`, validated against
`templates/sdlc.config.schema.json`. On a re-run, existing values are kept
and only missing keys are filled.

| Key | Default | Source on first run |
|---|---|---|
| `version` | `1` | Fixed |
| `artefacts.prd_dir` | `prds` | Default, or existing folder |
| `artefacts.plan_dir` | `plans` | Default, or existing folder |
| `artefacts.investigations_dir` | `investigations` | Default, or existing folder |
| `artefacts.prd_layout` | `folder` | Default; `flat` offered when existing PRDs are flat files |
| `artefacts.mockup_dir` | `null` | Default (inside the PRD folder), or detected mockup folder |
| `ids.prd` | `{slug}` | Asked; `{tracker}` and any existing artefact pattern offered |
| `ids.revision` | `{prd}-R{seq:2}` | Asked with the above |
| `tracker.type` | `none` | Detected from the git remote |
| `tracker.issue_ref` | `#{n}` | Derived from tracker type |
| `tracker.org`, `tracker.project` | unset | Parsed from an Azure DevOps remote |
| `branches.*` | `docs/{id}`, `feat/{id}`, `fix/{id}` | Default |
| `roles` | `[]` | Asked; roles declared in code offered |
| `design_system.path`, `design_system.guide` | `null` | Asked when a candidate folder is detected |
| `placeholder_data` | `null` | Asked only when a design system is set |
| `validation.*` | `null` | Detected from the project manifest |
| `context.always_read` | `[]` | Default |
| `context.knowledge_index` | `false` | Default |
| `learning.gotchas_dir`, `learning.decisions_dir` | `null` | Asked; detected folders offered |

## Other files written

| File | From |
|---|---|
| `.sdlc/sdlc.config.schema.json` | `templates/sdlc.config.schema.json` |
| `.sdlc/extensions/<skill>.md` | `templates/extensions/<skill>.md` |
| `<artefact dirs>/.gitkeep` | Created |
| `CLAUDE.md` block | `references/claude-md-block.md` |
