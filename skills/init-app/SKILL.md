---
name: init-app
description: "Scaffold a repository for the SDLC skills: detect what the repo already has, ask only what cannot be detected, then write .sdlc/config.yaml, the config schema, one extensions file per skill, the artefact directories, and a short CLAUDE.md pointer. Use when onboarding a new or existing repository to the skills, or when the user invokes /init-app. Never edits the vendored skills themselves."
argument-hint: "[--yes to accept every detected default]"
---

# Init app

Prepare a repository so the `prd`, `revise`, `plan`, `implement` and
`close-plan` skills can run in it. Everything written is configuration and
scaffolding the repository owns; nothing under the skills folder is touched.

**Input:** $ARGUMENTS (`--yes` accepts detected defaults without asking).

## 0. Load configuration

1. If `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml` exists, read it: this is a
   re-run. Keep every value already set and only fill gaps.
2. Read `references/config.md` for the defaults and what each key is for.
3. There is no extensions file for this skill.

## 1. Detect

Inspect the repository without changing it, and record a finding for each row:

| Detect | How | Feeds |
|---|---|---|
| Existing scaffold | `.sdlc/`, `prds/`, `plans/`, `investigations/` | Re-run versus first run |
| Repository kind | Nested git repositories (folders one or two levels down holding `.git`) and no application build manifest → `workspace`; otherwise `app` | `repo.kind`, `workspace.repos` (name from the folder, `path` relative, `url` from its origin) |
| Validation commands | `package.json` scripts (lint, typecheck, test, e2e, build), `Makefile` targets, `pyproject.toml`, `Cargo.toml`, `*.csproj` | `validation.*` (not for a workspace) |
| Tracker | Remote host (`github.com` → `github`; `dev.azure.com` or `visualstudio.com` → `ado`) **and** tracker signals in the repository: `AB#{n}` references in recent commits or the PR template, `azure-pipelines.yml` or `.azuredevops/`, GitHub issue templates. The code host and the work-item tracker are often different systems, so the result is the default for a question, never a finding | `tracker.type`, `tracker.org`, `tracker.project` |
| Issue reference style | `github` → `#{n}`; `ado` → `AB#{n}` | `tracker.issue_ref` |
| Knowledge index | `docs/knowledge-index.json`, a `knowledge-index` script in the manifest, or tagged reference docs | `context.knowledge_index` |
| Ignore rules | A `.gitignore` whose first rule is `*` (an allow-list) | Warning: the scaffold is untracked until allow-listed |
| Decision records | `docs/decisions/`, `docs/adr/`, `adr/` | `learning.decisions_dir` |
| Gotchas or known issues | `docs/gotchas/`, `docs/known-issues.md` | `learning.gotchas_dir` |
| Design system | folders named `design-system`, `mockups`, a `tokens.css` or `components.md` | `design_system.*` |
| Guidance | `CLAUDE.md`, `AGENTS.md`, `.claude/rules/` | Whether to append or create |
| Existing artefacts | Folders holding files that look like PRDs or plans (frontmatter with an id, acceptance criteria or phases), their layout and id pattern | `artefacts.*`, `ids.*` continuity |

Present the findings as a table before asking anything.

## 2. Ask only the gaps

Ask in one grouped message, with the detected or default value offered for
each, and skip anything `--yes` or detection already settled:

1. **Tracker**: always asked, with the detected type as the default. When
   the remote host and the repository's signals disagree, say which pointed
   where. For `ado`, ask for the organisation and project. Never set the
   tracker from the remote alone.
2. **Where artefacts go**, only when existing artefacts were found. Offer
   two choices and do not pick silently: continue in the existing folders
   with their layout and id pattern (set `artefacts.*` and `ids.*` to match
   so the sequence continues), or adopt the defaults and leave the existing
   content where it is.
3. **Id scheme** for PRDs and revisions, unless question 2 settled it. Offer
   `{slug}` (the feature name) and `{prd}-R{seq:2}`, and mention `{tracker}`
   for organisations that want a number.
4. **Roles**: the authorisation vocabulary (name and one-line description
   each). If the codebase declares roles (an enum, a groups file, a policy
   table), list them as the offer.
5. **Design system** path and guide, if any folder was detected or the
   product has screens.
6. **Learning directories**: where gotchas and promoted decisions should be
   filed. Offer the detected folders, or `docs/gotchas` and
   `docs/decisions`.
7. **Placeholder data**: one paragraph of realistic sample context for
   mockups, only when a design system is set.
8. **Knowledge index**: only when one was detected, offer
   `context.knowledge_index: true`.
9. **Workspace**: only when the repository looks like one, confirm
   `repo.kind: workspace` and the detected `workspace.repos` list (name,
   path, url). A workspace is not asked for validation commands.

Do not ask about branches or validation commands when detection found an
answer; show them and move on.

## 3. Write

Create or update, preserving anything that already exists:

1. `.sdlc/config.yaml` from `templates/config.yaml`, with the answers filled
   in and detected values set. Leave every other key at its default so the
   file documents the contract.
2. `.sdlc/sdlc.config.schema.json`, copied from
   `templates/sdlc.config.schema.json`.
3. `.sdlc/extensions/{prd,revise,plan,implement,close-plan}.md` from
   `templates/extensions/`. Skip any that already exist.
4. The artefact directories from `artefacts.*`, each with a `.gitkeep`, plus
   `artefacts.mockup_dir` when a design system is set.
5. `CLAUDE.md`: append the block in `references/claude-md-block.md` (the
   workspace variant when `repo.kind` is `workspace`; create the file if
   absent). If an equivalent block is already present, update it in place
   rather than appending a second copy.
6. When `.gitignore` is an allow-list, do not edit it. Print the lines that
   make the scaffold visible (`!.sdlc/`, `!.sdlc/**`, and the same pair for
   each artefact directory) and offer to append them; until they are added
   the scaffold is untracked.

Validate the written config against the schema and fix any error before
reporting.

## 4. Report

Print, in order: the table of files written or updated, the detected values
that were accepted without asking, the keys left at default that the owner
may want to revisit (`roles` empty, `design_system` null, `validation` null),
a pointer to `references/ci-guard.md` for the CI check that protects the
vendored skills, and the one manual step remaining: review and commit. For a
workspace, also list the entries in `workspace.repos` that have no `.sdlc/`
of their own; each needs its own `/init-app` run in that repository.

## Never

- Edit, move or rename anything under the vendored skills folders.
- Overwrite a value already set in an existing `.sdlc/config.yaml`.
- Write client-specific content into a skill or template.
- Add more than the pointer block to `CLAUDE.md`; area-specific guidance
  belongs in reference docs and extensions.
