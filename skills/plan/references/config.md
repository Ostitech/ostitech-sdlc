# Configuration read by the plan skill

Contract versions read: **1**.

Source: `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml`. Missing file or missing
keys take these defaults.

| Key | Default | Used for |
|---|---|---|
| `artefacts.plan_dir` | `plans` | Where the plan file is written |
| `artefacts.prd_dir` | `prds` | Where PRDs and revisions are looked up |
| `artefacts.investigations_dir` | `investigations` | Bug investigations read before a bug-fix plan |
| `ids.prd`, `ids.revision` | `PRD-{seq:3}`, `{prd}-R{seq:2}` | Recognising trigger ids in filenames |
| `tracker.type` | `none` | Whether milestones can be recorded on a tracker item |
| `tracker.issue_ref` | `#{n}` | How an issue id is written in the plan id and commits |
| `branches.work`, `branches.fix` | `feat/{id}-{slug}`, `fix/{id}-{slug}` | The branch named in the plan frontmatter |
| `validation.*` | `null` | Validation commands; when null, discover from `package.json` scripts, `Makefile`, `pyproject.toml` or equivalent |
| `context.always_read` | `[]` | Files read before exploration |
| `context.knowledge_index` | `false` | Enables `references/knowledge-index.md` |

Extensions: `${CLAUDE_PROJECT_DIR}/.sdlc/extensions/plan.md`, headings
`context`, `design`, `sections`, `done-criteria`, `checks`.

## Id tokens

- `{seq:N}`: next integer after the highest existing id of that kind in the
  directory, zero-padded to N digits.
- `{date}`: today as `YYYYMMDD`.
- `{initials}`: upper-case initials of `git config user.name`.
- `{prd}`: the parent PRD id (revisions only).
- `{slug}`: kebab-case, at most six words, derived from the title.

The plan id is never generated independently: it is always the trigger's id,
or `{date}-{slug}` for technical and inline work.
