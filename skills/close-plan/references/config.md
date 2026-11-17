# Configuration read by the close-plan skill

Contract versions read: **1**.

Source: `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml`. Missing file or missing
keys take these defaults.

| Key | Default | Used for |
|---|---|---|
| `artefacts.plan_dir` | `plans` | Resolving a bare plan filename |
| `artefacts.prd_dir` | `prds` | Locating the PRD or revision to mark shipped |
| `workspace.repos` | `[]` | Locating each repository's PR for a multi-repo plan |
| `tracker.type` | `none` | Whether follow-ups are created as tracker items |
| `tracker.issue_ref` | `#{n}` | How follow-up references are written |
| `tracker.uat_state` | `null` | State the tracker item moves to after the UAT handoff; null means no transition |
| `environments.uat` | `null` | Where the live UAT run happens; null means ask the user |
| `learning.gotchas_dir` | `null` | Where unplanned problems worth keeping are filed; null lists them instead |
| `learning.decisions_dir` | `null` | Where durable decisions are drafted as records; null lists them instead |

Extensions: `${CLAUDE_PROJECT_DIR}/.sdlc/extensions/close-plan.md`, headings
`sections`, `promote`.

`promote` content overrides `learning.*` for the kinds of learning it names,
for example sending gotchas about infrastructure to a different directory
from gotchas about application code.
