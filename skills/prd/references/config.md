# Configuration read by the prd skill

Contract versions read: **1**.

Source: `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml`. Missing file or missing
keys take these defaults.

| Key | Default | Used for |
|---|---|---|
| `artefacts.prd_dir` | `prds` | Where the PRD file is written and existing PRDs are searched |
| `artefacts.mockup_dir` | `prds/mockups` | Where a mockup folder is created |
| `ids.prd` | `PRD-{seq:3}` | The PRD id |
| `branches.prd` | `docs/{id}-{slug}` | The branch created for the PRD |
| `roles` | `[]` | The vocabulary personas are mapped onto |
| `design_system.path` | `null` | Enables the mockup step; folder of tokens and components |
| `design_system.guide` | `null` | Read before intake for product vocabulary |
| `placeholder_data` | `null` | Sample-data context for mockups |
| `tracker.type` | `none` | Whether a tracker item is created at sign-off |
| `context.always_read` | `[]` | Read before intake |

Extensions: `${CLAUDE_PROJECT_DIR}/.sdlc/extensions/prd.md`, headings
`questions`, `sections`, `checks`.

## Id tokens

- `{seq:N}`: next integer after the highest existing id of that kind in
  `artefacts.prd_dir`, zero-padded to N digits.
- `{date}`: today as `YYYYMMDD`.
- `{initials}`: upper-case initials of `git config user.name`.
- `{slug}`: kebab-case, at most six words, derived from the title.
