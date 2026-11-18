# Configuration read by the close-plan skill

Contract versions read: **1**.

Source: `.sdlc/config.yaml` in the target repository (below). Missing file
or missing keys take these defaults.

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

Extensions: `.sdlc/extensions/close-plan.md` in the target repository, headings
`sections`, `promote`.

`promote` content overrides `learning.*` for the kinds of learning it names,
for example sending gotchas about infrastructure to a different directory
from gotchas about application code.

## Target repository

The repository whose `.sdlc/` is read and whose files, branches and commits
the skill writes. Resolved once, before anything else, in this order:

1. `--repo <path>` in the input: that folder, which must be a git repository.
2. The input names a file or folder: the nearest folder at or above it holding
   `.sdlc/` or `.git`. With no path in the input, the same walk up from the
   current folder.
3. The folder found is a workspace (`repo.kind: workspace`) and the work names
   exactly one repository from `workspace.repos`: that repository's checkout
   at `workspace.repos[].path`; ask for the path when there is none. For this
   skill the work names a repository when the plan lives in one (the walk from its path finds it); a plan with several in `repos:` stays in the workspace. Work that names several
   repositories, or none, stays in the workspace.
4. Otherwise `${CLAUDE_PROJECT_DIR}`.

The skill that runs is the one loaded in the session; it reads the target's
config at its own contract version, whatever version that repository has
vendored. Report the target once when it is not the project directory, and
run every git command from it.
