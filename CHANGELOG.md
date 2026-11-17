# Changelog

All notable changes to the skills and the configuration contract.
Contract version bumps are called out explicitly.

## v0.1.3

### Fixed
- Knowledge-index detection in `init-app` no longer names one organisation's file and script; it looks for an index described in the repository guidance or typed frontmatter on reference docs.

## v0.1.2

### Added
- Cross-repo work: `repo.kind` (`app` | `workspace`), `repo.name` and `workspace.repos` in the config; a plan may list `repos:` when written in a workspace, with one repository per phase, contract phase in the providing repository, one PR per repository, and a checkpoint line that names the repository. Methodology section "Cross-repo work". Additive; contract version stays 1.
- `init-app` detects a workspace (nested git repositories, no build), fills `workspace.repos`, and writes a workspace variant of the CLAUDE.md block.
- `init-app` detects a documentation index described in the repository's guidance and asks about `context.knowledge_index`.
- `init-app` warns when `.gitignore` is an allow-list, since the scaffold is untracked until allow-listed.

### Changed
- `init-app` always asks the tracker question, with a default from the remote host and tracker signals in the repository (`AB#` references, pipelines files, issue templates), instead of assuming the code host is the tracker.
- `init-app` offers an explicit choice when artefacts already exist: continue in the existing folders with their layout and id pattern, or adopt the defaults and leave the old content in place.
- `prd` and `plan` route work that spans repositories to the workspace repository.

## v0.1.1

### Fixed
- `init-app` frontmatter was not strict YAML (unquoted colon in the description), so the skills CLI skipped it on install. Descriptions are now quoted and `scripts/check-skills.py` parses every skill strictly before release.

## v0.1.0

### Added
- Methodology and extension-points documents.
- Configuration contract version 1 (`.sdlc/config.yaml`, schema shipped with `init-app`).
- Skills: `prd`, `revise`, `plan`, `implement`, `close-plan`, `init-app`.
- Plugin and marketplace manifests so the repository also installs as a Claude Code plugin.
- Eval skeleton for `claude plugin eval`.

### Changed
- PRD identity is the feature slug by default, laid out as `prds/<id>/prd.md` with revisions and mockups inside (`artefacts.prd_layout`, new `{tracker}` id token, `mockup_dir` now optional, branch defaults no longer append a slug). Additive; contract version stays 1.

### Reserved
- `context.knowledge_index` in the config and the plan skill's retrieval protocol. The tooling for a tagged documentation index ships separately.
