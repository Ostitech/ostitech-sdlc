# Changelog

All notable changes to the skills and the configuration contract.
Contract version bumps are called out explicitly.

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
