# Organisation defaults

An organisation that runs the skills across many repositories answers the
same questions every time: which tracker, which id scheme, where gotchas go.
Organisation defaults answer them once, in the organisation's own copy of the
skills repository, and travel to every repository with the vendored skills.

## How they travel

The skills CLI vendors skill folders and nothing else, so the defaults live
inside one. The organisation adds a skill folder to its copy:

```
skills/<org>-defaults/
  SKILL.md               frontmatter only; hidden from the slash menu
  sdlc.defaults.yaml     partial config, same shape and schema as .sdlc/config.yaml
  extensions/            optional initial .sdlc/extensions/<skill>.md files
    plan.md
    prd.md
```

`npx skills add <org>/<copy> -s '*' -a claude-code universal -y --copy` then
installs it beside the core skills,
and `init-app` finds `sdlc.defaults.yaml` under `.claude/skills/*/` or
`.agents/skills/*/`.

## SKILL.md

The folder needs a `SKILL.md` so the skills CLI accepts it. Keep it to
frontmatter that hides the skill from people and from the model, plus one
line of explanation:

```markdown
---
name: acme-defaults
description: "Acme organisation defaults for the SDLC skills. Read by init-app; not a command."
user-invocable: false
disable-model-invocation: true
---

Organisation defaults for `init-app`. Edit `sdlc.defaults.yaml`, not this file.
```

## sdlc.defaults.yaml

Any key from the config contract except `repo`, `workspace` and
`validation`, which are detected per repository. Unset keys keep the core
defaults. An invented example:

```yaml
version: 1

tracker:
  type: ado
  org: acme
  project: Platform
  issue_ref: "AB#{n}"

ids:
  prd: "{slug}"
  revision: "{prd}-R{seq:2}"

learning:
  gotchas_dir: docs/gotchas
  decisions_dir: docs/decisions

context:
  knowledge_index: true
```

## Precedence

For each key, `init-app` takes the first of:

1. the value already in the repository's `.sdlc/config.yaml` (a re-run);
2. the answer given during this run;
3. the organisation default;
4. the detected value;
5. the built-in default.

A key the organisation default sets is shown as settled and not asked. When
detection disagrees, the findings table says so and the organisation value
stands; the owner can still change it in `.sdlc/config.yaml` afterwards.

## Extensions

Files under `extensions/` are copied as the repository's initial
`.sdlc/extensions/<skill>.md` when that file does not exist yet. They are
starting points the repository then owns; `init-app` never overwrites them on
a re-run, and a change to the organisation's copy reaches existing
repositories only by hand.

## Two files found

Two vendored skill folders each carrying `sdlc.defaults.yaml` is a conflict,
usually a repository installed from two organisation copies. `init-app` asks
which applies rather than merging them.
