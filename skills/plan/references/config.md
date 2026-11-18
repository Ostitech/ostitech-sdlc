# Configuration read by the plan skill

Contract versions read: **1**.

Source: `.sdlc/config.yaml` in the target repository (below). Missing file
or missing keys take these defaults.

| Key | Default | Used for |
|---|---|---|
| `repo.kind` | `app` | Whether a plan may list more than one repository (`workspace` only) |
| `workspace.repos` | `[]` | The repositories a multi-repo plan may name |
| `artefacts.plan_dir` | `plans` | Where the plan file is written |
| `artefacts.prd_dir` | `prds` | Where PRDs and revisions are looked up |
| `artefacts.investigations_dir` | `investigations` | Bug investigations read before a bug-fix plan |
| `artefacts.prd_layout` | `folder` | Whether a PRD is `prds/<id>/prd.md` or `prds/<id>.md` |
| `ids.prd`, `ids.revision` | `{slug}`, `{prd}-R{seq:2}` | Recognising trigger ids; the plan always reads the `id` from the trigger's frontmatter |
| `tracker.type` | `none` | Whether milestones can be recorded on a tracker item |
| `tracker.issue_ref` | `#{n}` | How an issue id is written in the plan id and commits |
| `branches.work`, `branches.fix` | `feat/{id}`, `fix/{id}` | The branch named in the plan frontmatter |
| `validation.*` | `null` | Validation commands; when null, discover from `package.json` scripts, `Makefile`, `pyproject.toml` or equivalent |
| `context.always_read` | `[]` | Files read before exploration |
| `context.knowledge_index` | `false` | Enables `references/knowledge-index.md` |

Extensions: `.sdlc/extensions/plan.md` in the target repository, headings
`context`, `design`, `sections`, `done-criteria`, `checks`.

## Id tokens

- `{seq:N}`: next integer after the highest existing id of that kind in the
  directory, zero-padded to N digits.
- `{date}`: today as `YYYYMMDD`.
- `{initials}`: upper-case initials of `git config user.name`.
- `{prd}`: the parent PRD id (revisions only).
- `{slug}`: kebab-case, at most six words, derived from the title.
- `{tracker}`: the tracker item number, which means the item is created before the id.

The plan id is never generated independently: it is the trigger's id for a
PRD or revision, `{issue number}-{slug}` for a bug fix, and `{date}-{slug}`
for technical and inline work. Every plan id is filename-safe and the plan
file is `{id}.plan.md`.

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
   skill the work names a repository when the trigger does: a PRD, revision or investigation that lives in one, or an issue or description that names one; a plan listing several in `repos:` stays in the workspace. Work that names several
   repositories, or none, stays in the workspace.
4. Otherwise `${CLAUDE_PROJECT_DIR}`.

The skill that runs is the one loaded in the session; it reads the target's
config at its own contract version, whatever version that repository has
vendored. Report the target once when it is not the project directory, and
run every git command from it.
