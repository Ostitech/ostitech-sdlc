# Extension points

The skills are generic. Everything that varies by organisation or repository
comes from two places inside the repository that adopts them:

```
.sdlc/config.yaml          values: identifiers, directories, tracker, roles, commands
.sdlc/extensions/<skill>.md  additions: sections, checks and context applied at named points
```

Skills read both at invocation. Neither file is required; a skill with no
config uses its documented defaults, and a missing extensions file is a no-op.

Editing a vendored skill to customise it is the one thing this design forbids.
A skill edited in place forks from the upstream it was installed from, and the
next update either overwrites the edit or is skipped forever. The adopting
repository's CI should fail when a vendored skill has local changes
(`npx skills list --json`, status `modified`).

## Config

`.sdlc/config.yaml` is validated against the schema shipped with the
`init-app` skill. All keys are optional. Defaults are shown.

```yaml
version: 1

artefacts:
  prd_dir: prds                  # PRDs and their revisions
  plan_dir: plans                # one plan per piece of work
  investigations_dir: investigations
  mockup_dir: prds/mockups       # static HTML mockups referenced by PRDs

ids:
  prd: "PRD-{seq:3}"             # tokens: {seq:N} zero-padded counter, {date} YYYYMMDD, {initials}
  revision: "{prd}-R{seq:2}"     # {prd} is the parent PRD id

tracker:
  type: none                     # github | ado | none
  issue_ref: "#{n}"              # how an issue is written in commits and plans

branches:
  prd: "docs/{id}-{slug}"
  work: "feat/{id}-{slug}"
  fix: "fix/{id}-{slug}"

roles: []                        # name + description; the vocabulary the PRD skill maps personas onto

design_system:
  path: null                     # folder with tokens/components the mockup must use
  guide: null                    # file the mockup builder reads first

placeholder_data: null           # one paragraph of realistic sample-data context for mockups

validation:                      # commands the plan and implement skills use; discovered from
  lint: null                     # package.json / Makefile when null
  typecheck: null
  test: null
  e2e: null
  build: null

context:
  always_read: []                # files the plan skill reads before exploring, every time
  knowledge_index: false         # reserved: enables the tagged-docs retrieval protocol

learning:
  gotchas_dir: null              # where close-out files recurring, non-obvious failures
  decisions_dir: null            # where promoted decision records go
```

Skills substitute `${CLAUDE_PROJECT_DIR}` to locate the file, so the config is
per repository even when the skills are installed globally.

## Extensions

`.sdlc/extensions/<skill>.md` is a markdown file whose level-two headings name
the point at which the content under them applies. Content is markdown the
skill follows or inserts; it is declarative (sections, checklists, questions,
file references), never procedure. Unknown headings produce a warning and are
ignored, so an extensions file written for a newer skill version degrades
gracefully.

### `prd`

| Point | Applied |
|---|---|
| `## questions` | Added to the intake questions the skill asks before drafting |
| `## sections` | Extra sections rendered into every PRD, after the standard ones |
| `## checks` | Conditions verified before the PRD is offered for sign-off |

### `revise`

| Point | Applied |
|---|---|
| `## checks` | Conditions verified before the revision is offered for sign-off |

### `plan`

| Point | Applied |
|---|---|
| `## context` | Files or instructions read before codebase exploration, in addition to `context.always_read` |
| `## design` | Extra rows or gates in the design section (for example a data-dependency table, a deploy-path statement) |
| `## sections` | Extra plan sections after the design section (for example a UX playbook compliance table) |
| `## done-criteria` | Appended to every phase's done-criteria |
| `## checks` | Conditions verified before the plan is offered for approval |

### `implement`

| Point | Applied |
|---|---|
| `## before-phase` | Steps run before each phase starts |
| `## validation` | Commands or checks added to every phase's validation |
| `## after-phase` | Steps run after each checkpoint commit |

### `close-plan`

| Point | Applied |
|---|---|
| `## sections` | Extra close-out sections |
| `## promote` | Where each kind of durable learning is filed, overriding `learning.*` in config |

## Versioning

`config.version` is the contract version. Each skill states the config versions
it reads in its `references/` folder. A breaking change to the config or to an
extension point's semantics bumps the version; additive changes do not.

## What does not belong here

- Procedure. If an organisation needs a step the skills do not have, that is a
  pull request to the skills, not an extension.
- Secrets or environment values. Those stay in the tooling that owns them.
- Area-specific knowledge (gotchas, endpoint catalogues, subsystem mechanics).
  That is reference documentation, retrieved by the plan skill through
  `context.always_read` or the knowledge index, not injected into every run.
