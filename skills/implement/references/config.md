# Configuration read by the implement skill

Contract versions read: **1**.

Source: `.sdlc/config.yaml` in the target repository (below). Missing file
or missing keys take these defaults.

| Key | Default | Used for |
|---|---|---|
| `artefacts.plan_dir` | `plans` | Resolving a bare plan filename |
| `workspace.repos` | `[]` | Resolving each repository of a multi-repo plan to a local checkout (`path`) |
| `branches.work`, `branches.fix` | `feat/{id}`, `fix/{id}` | Fallback branch name when the plan frontmatter has none |
| `tracker.issue_ref` | `#{n}` | Issue reference in commit bodies for bug-fix plans |
| `validation.*` | `null` | Fallback validation commands when the plan has no Validation commands block; when null, discover from `package.json` scripts, `Makefile`, `pyproject.toml` or equivalent |

Extensions: `.sdlc/extensions/implement.md` in the target repository, headings
`before-phase`, `validation`, `after-phase`.

The plan itself is the primary source for branch, validation commands,
phase structure and the UAT script. Config is consulted only where the plan
is silent.

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
   skill the work names a repository when the plan lives in one (the walk from its path finds it); a plan with several in `repos:` stays in the workspace and runs each phase in that phase's repository. Work that names several
   repositories, or none, stays in the workspace.
4. Otherwise `${CLAUDE_PROJECT_DIR}`.

The skill that runs is the one loaded in the session; it reads the target's
config at its own contract version, whatever version that repository has
vendored. Report the target once when it is not the project directory, and
run every git command from it.
