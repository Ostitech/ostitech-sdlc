# Configuration read by the review skill

Contract versions read: **1**.

Source: `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml`. Missing file or missing
keys take these defaults.

| Key | Default | Used for |
|---|---|---|
| `artefacts.plan_dir` | `plans` | Locating the plan by id when the PR body does not link it |
| `artefacts.prd_dir` | `prds` | Locating the PRD or revision the plan names |
| `tracker.type` | `none` | Whether advisory findings are filed as tracker items |
| `tracker.issue_ref` | `#{n}` | How filed items are referenced in the report |
| `reviewers` | `[]` | Extra reviewer skills run in step 4, by name |
| `validation.*` | `null` | Fallback test commands when the plan has none |

Extensions: `${CLAUDE_PROJECT_DIR}/.sdlc/extensions/review.md`, headings
`gates`, `advisory`.

The built-in `review-conformance` skill always runs for gate 2; it is not
listed in `reviewers`.
