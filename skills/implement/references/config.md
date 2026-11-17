# Configuration read by the implement skill

Contract versions read: **1**.

Source: `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml`. Missing file or missing
keys take these defaults.

| Key | Default | Used for |
|---|---|---|
| `artefacts.plan_dir` | `plans` | Resolving a bare plan filename |
| `branches.work`, `branches.fix` | `feat/{id}-{slug}`, `fix/{id}-{slug}` | Fallback branch name when the plan frontmatter has none |
| `tracker.issue_ref` | `#{n}` | Issue reference in commit bodies for bug-fix plans |
| `validation.*` | `null` | Fallback validation commands when the plan has no Validation commands block; when null, discover from `package.json` scripts, `Makefile`, `pyproject.toml` or equivalent |

Extensions: `${CLAUDE_PROJECT_DIR}/.sdlc/extensions/implement.md`, headings
`before-phase`, `validation`, `after-phase`.

The plan itself is the primary source for branch, validation commands, and
phase structure. Config is consulted only where the plan is silent.
