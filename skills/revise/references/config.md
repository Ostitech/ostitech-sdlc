# Configuration read by the revise skill

Contract versions read: **1**.

Source: `.sdlc/config.yaml` in the target repository (below). Missing file
or missing keys take these defaults.

| Key | Default | Used for |
|---|---|---|
| `artefacts.prd_dir` | `prds` | Where the parent PRD is found and the revision is written |
| `artefacts.prd_layout` | `folder` | Where the revision document is written |
| `ids.revision` | `{prd}-R{seq:2}` | The revision id; `{prd}` is the parent id, `{seq:N}` the next free number for that parent |
| `branches.prd` | `docs/{id}` | The branch created for the revision, with the revision id |
| `tracker.type` | `none` | Whether a tracker item is created at sign-off |

Extensions: `.sdlc/extensions/revise.md` in the target repository, heading
`checks`.

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
   skill the work names a repository when the parent PRD lives in one (the walk from its path finds it), or the user says which. Work that names several
   repositories, or none, stays in the workspace.
4. Otherwise `${CLAUDE_PROJECT_DIR}`.

The skill that runs is the one loaded in the session; it reads the target's
config at its own contract version, whatever version that repository has
vendored. Report the target once when it is not the project directory, and
run every git command from it.
