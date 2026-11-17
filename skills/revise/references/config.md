# Configuration read by the revise skill

Contract versions read: **1**.

Source: `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml`. Missing file or missing
keys take these defaults.

| Key | Default | Used for |
|---|---|---|
| `artefacts.prd_dir` | `prds` | Where the parent PRD is found and the revision is written |
| `ids.revision` | `{prd}-R{seq:2}` | The revision id; `{prd}` is the parent id, `{seq:N}` the next free number for that parent |
| `branches.prd` | `docs/{id}-{slug}` | The branch created for the revision, with the revision id |
| `tracker.type` | `none` | Whether a tracker item is created at sign-off |

Extensions: `${CLAUDE_PROJECT_DIR}/.sdlc/extensions/revise.md`, heading
`checks`.
