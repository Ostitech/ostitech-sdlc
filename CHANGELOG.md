# Changelog

All notable changes to the skills and the configuration contract.
Contract version bumps are called out explicitly.

## Unreleased

### Added
- Methodology and extension-points documents.
- Configuration contract version 1 (`.sdlc/config.yaml`, schema shipped with `init-app`).
- Skills: `prd`, `revise`, `plan`, `implement`, `close-plan`, `init-app`.
- Plugin and marketplace manifests so the repository also installs as a Claude Code plugin.
- Eval skeleton for `claude plugin eval`.

### Reserved
- `context.knowledge_index` in the config and the plan skill's retrieval protocol. The tooling for a tagged documentation index ships separately.
