# Configuration read by the prd skill

Contract versions read: **1**.

Source: `.sdlc/config.yaml` in the target repository (below). Missing file
or missing keys take these defaults.

| Key | Default | Used for |
|---|---|---|
| `artefacts.prd_dir` | `prds` | Where the PRD file is written and existing PRDs are searched |
| `artefacts.prd_layout` | `folder` | `prds/<id>/prd.md` (folder) or `prds/<id>.md` (flat) |
| `artefacts.mockup_dir` | `null` | Where a mockup folder is created; null means inside the PRD folder |
| `ids.prd` | `{slug}` | The PRD id; the feature name by default |
| `branches.prd` | `docs/{id}` | The branch created for the PRD |
| `roles` | `[]` | The vocabulary personas are mapped onto |
| `design_system.path` | `null` | Enables the mockup step; folder of tokens and components |
| `design_system.guide` | `null` | Read before intake for product vocabulary |
| `placeholder_data` | `null` | Sample-data context for mockups |
| `tracker.type` | `none` | Whether a tracker item is created at sign-off |
| `context.always_read` | `[]` | Read before intake |
| `repo.kind` | `app` | A PRD spanning repositories belongs in a `workspace` repository |

Extensions: `.sdlc/extensions/prd.md` in the target repository, headings
`questions`, `sections`, `checks`.

## Id tokens

- `{seq:N}`: next integer after the highest existing id of that kind in
  `artefacts.prd_dir`, zero-padded to N digits.
- `{date}`: today as `YYYYMMDD`.
- `{initials}`: upper-case initials of `git config user.name`.
- `{slug}`: kebab-case, at most six words, derived from the title; unique under `artefacts.prd_dir`.
- `{tracker}`: the tracker item number; the item is created before the id is computed.

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
   skill the work names a repository when the feature description names one repository, or the user says which. Work that names several
   repositories, or none, stays in the workspace.
4. Otherwise `${CLAUDE_PROJECT_DIR}`.

The skill that runs is the one loaded in the session; it reads the target's
config at its own contract version, whatever version that repository has
vendored. Report the target once when it is not the project directory, and
run every git command from it.
