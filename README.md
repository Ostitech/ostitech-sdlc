# ostitech-sdlc

A light, configuration-driven delivery procedure for agentic software
development, packaged as [Agent Skills](https://agentskills.io) for Claude
Code and any agent that reads `SKILL.md`.

Two documents (PRD and plan), one plan per piece of work, phased
implementation with checkpoints, and a one-page close-out that feeds the next plan. Everything that
varies by organisation lives in the adopting repository's `.sdlc/` folder.
The skills themselves are never edited in place.

Read [docs/methodology.md](docs/methodology.md) for the procedure and
[docs/extension-points.md](docs/extension-points.md) for the customisation
contract.

## Skills

| Skill | Purpose |
|---|---|
| `prd` | Capture a feature as a PRD in the product owner's language, plus an optional static mockup |
| `revise` | A revision to a shipped PRD: delta document, parent amended inline |
| `plan` | The single implementation plan: design section, shared context, verification-bounded phases |
| `implement` | Execute plan phases with checkpoint discipline: validation green, commit, note |
| `close-plan` | Close out a plan: outcomes, deviations, gotchas, decisions promoted, follow-ups |
| `init-app` | Scaffold `.sdlc/` configuration and extensions in a repository |

## Install into a repository

Vendored, pinned to a release, copied rather than symlinked so it works on
Windows without Developer Mode:

```bash
npx skills add ostitech/ostitech-sdlc@v0.1.5 --all -a claude-code --copy -y
```

Commit `.claude/skills/`, `.agents/skills/` and `skills-lock.json`. Then run
`/init-app` once to write `.sdlc/config.yaml` and the extension files.

Upgrade when you choose:

```bash
npx skills check
```

```bash
npx skills update -y
```

Guard the boundary in CI so a vendored skill is never edited in place:

```bash
npx skills list --json
```

Fail the build when any skill reports status `modified`. A snippet for GitHub
Actions and Azure Pipelines is in the `init-app` skill's references.

## Install as a plugin

The same repository is a Claude Code plugin for teams that prefer marketplace
distribution:

```
/plugin marketplace add ostitech/ostitech-sdlc
/plugin install ostitech-sdlc@ostitech
```

Plugins do not load in Claude Code cloud sessions; vendoring does.

## Customising

Never edit a skill. Put values in `.sdlc/config.yaml` (identifiers,
directories, tracker, roles, validation commands, design system) and
additions in `.sdlc/extensions/<skill>.md` (extra questions, sections, gates,
done-criteria, context). A change the extension points cannot express is a
pull request to this repository.

## Adopting as an organisation

An organisation that wants its own copy keeps a repository with this one as
`upstream`, so it owns the copy outright and can still merge releases:

```bash
git remote add upstream https://github.com/Ostitech/ostitech-sdlc.git
```

```bash
git fetch upstream --tags && git merge upstream/main
```

Two rules keep the merge clean and the boundary honest:

- The core skill folders under `skills/` are never edited in the copy. A
  change the extension points cannot express is a pull request here.
- Organisation-specific skills live in their own folders in the copy
  (`skills/<org>-<name>/`), so an install with `--all` from the copy gives a
  repository the core plus the organisation's additions in one step.
  Repository-level values and additions still go in that repository's
  `.sdlc/` folder.
- Values the organisation sets the same way everywhere (tracker, id scheme,
  learning directories, initial extensions) go in a `skills/<org>-defaults/`
  folder holding `sdlc.defaults.yaml`. `init-app` reads it before asking
  anything. Format and precedence: the `init-app` skill's
  `references/org-defaults.md`.

## Layout

```
skills/<name>/SKILL.md          the skill
skills/<name>/references/       detail loaded on demand
skills/<name>/templates/        files the skill writes from
docs/                           methodology and the extension contract
evals/                          plugin eval cases (claude plugin eval)
.claude-plugin/                 plugin and marketplace manifests
```

## Licence

Apache-2.0. See [LICENSE](LICENSE).
