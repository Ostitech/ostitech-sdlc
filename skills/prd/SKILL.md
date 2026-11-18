---
name: prd
description: Capture a new feature as a PRD in the product owner's language (problem, users, roles, behaviour, acceptance criteria, scope boundaries, open questions) plus an optional static HTML mockup, then offer it for sign-off. Use when the user wants to describe, spec, design or brief a new screen, flow, report or capability, or invokes /prd. Never writes code, a plan, or technical design; a change to shipped behaviour belongs to /revise.
argument-hint: <feature description> | <path to an existing draft PRD to continue> [--repo <path>]
---

# PRD

Turn a product idea into a PRD someone outside engineering can sign off, and
an implementer can later plan against. The PRD says what, why, for whom, and
how we will know it is right. It never says how it will be built.

**Input:** $ARGUMENTS (absent: use the conversation).

## 0. Load configuration

1. Resolve the target repository (`references/config.md`, *Target
   repository*): a `--repo <path>` argument; else the nearest folder at or
   above the input path (or the current folder) holding `.sdlc/` or `.git`;
   when that is a workspace and the work names one of `workspace.repos`,
   that repository's checkout; else `${CLAUDE_PROJECT_DIR}`. Every path and
   git operation below is relative to it. Say which was chosen when it is
   not the project directory.
2. Read its `.sdlc/config.yaml` if present; apply defaults from
   `references/config.md` for anything missing.
3. Read its `.sdlc/extensions/prd.md` if present. Each
   level-two heading is an extension point (`questions`, `sections`,
   `checks`); keep its content to apply at that step. Warn once about unknown
   headings and ignore them.
4. If the input is a path to a draft PRD, read it and resume from step 3.

## 1. Lane

Decide what the ask is before asking anything else:

| The user is describing | Do |
|---|---|
| A change to behaviour that has already shipped | Stop and route to the `revise` skill |
| Something broken that should already work | Stop; it is a bug: route to the tracker and the `plan` skill |
| A small adjustment nobody needs to sign off | Say so and recommend plan mode; continue only if the user insists |
| A new capability, screen, flow, report or integration | Continue |

If the behaviour spans more than one repository and `repo.kind` is `app`,
say so: the PRD belongs in the workspace repository, where the plan can list
every repository it changes. Continue here only if the user confirms. The
converse is handled by target resolution: a feature that names one
repository, started from the workspace, is written into that repository.

Check `artefacts.prd_dir` for an existing PRD covering the same area, by
folder or file name and by title. If one exists and has shipped, this is
probably a revision; say so. If one exists with the slug you would choose,
stop: the feature already has a PRD.

## 2. Intake

Ask the questions in `references/intake-questions.md`, then anything under the
`questions` extension point. Ask in one message, grouped, with your best guess
offered for each so the owner can confirm rather than compose. Do not ask what
convention already answers.

Every persona the owner names must map onto a role from `roles` in config.
Personas are not authorisation; if `roles` is empty, ask the owner to define
the roles before continuing and record them for the config.

Read `design_system.guide` and every file in `context.always_read` when set,
so the PRD uses the product's existing vocabulary.

## 3. Identity and branch

1. Derive the slug: kebab-case, at most six words, the feature's name as
   people will say it. It must be unique under `artefacts.prd_dir`.
2. If `ids.prd` contains `{tracker}`, create the tracker item now (title and
   one-line summary) and use its number; stop if there is no tracker access.
3. Compute the id from `ids.prd` (token rules in `references/config.md`).
   By default the id is the slug.
4. Create or switch to the branch from `branches.prd`. If the working tree has
   unrelated changes, stop and ask before switching.

## 4. Write the PRD

Write the PRD from `templates/prd.md` to the path the layout gives:
`artefacts.prd_dir/{PRD_ID}/prd.md` for `folder` (the default), or
`artefacts.prd_dir/{PRD_ID}.md` for `flat`. Then:

- Use the owner's wording. Replace vague verbs (improve, enhance) with specific
  ones (add, show, filter by, block).
- Acceptance criteria in Given/When/Then, one per material behaviour, three to
  seven. Each checkable by someone who did not build it.
- Roles and permissions is required: access, action matrix, data scope.
- Out of scope is required. If the owner did not volunteer it, infer one thing
  they are not asking for and flag it in Open questions.
- Open questions hold only what is genuinely undecided. A UI choice made by
  convention is not a question.
- Append any sections under the `sections` extension point after the
  standard ones.

## 5. Mockup

Build a mockup only when `design_system.path` is set or the user asks. Follow
`references/mockup.md`: documented components and tokens only, realistic
sample data from `placeholder_data`, a top comment linking the PRD, modals and
slide-overs rendered open. Write it under `mockups/` inside the PRD folder,
or under `artefacts.mockup_dir/{PRD_ID}/` when that key is set or the layout
is `flat`. Set `mockups:` in the PRD frontmatter to the relative path.

## 6. Checks

Run before offering the PRD. Fix every failure, then report what changed.

1. **No design language.** Scan for schema, table, column, event type,
   endpoint, migration, payload, queue, and integration mechanics. Convert
   each hit into an open question and remove it from the body.
2. Three to seven acceptance criteria, all Given/When/Then.
3. Every persona mapped to a configured role; the action matrix has no empty
   cells.
4. Out of scope is not empty.
5. When a mockup exists, the frontmatter links it and every screen the PRD
   describes appears in it.
6. Everything under the `checks` extension point.

## 7. Iterate and sign off

Show the PRD (and mockup) and invite changes. Edit in place; do not create a
second file for the same feature. When the owner confirms:

1. Set `status: signed-off` and the date in the frontmatter.
2. If `tracker.type` is not `none` and access exists, create the tracker item
   (title, link to the PRD, acceptance criteria as the description) unless it
   was created in step 3, in which case update it. Record its reference in
   the frontmatter. Otherwise tell the user what to create.
3. Hand off: name the `plan` skill with the PRD path as its input.

## Never

- Write code, a plan, phases, estimates, or technical design.
- Put a schema, event type, endpoint or integration mechanism in the PRD.
- Leave a persona unmapped to a role.
- Invent acceptance criteria the owner did not confirm.
- Create a revision; that is the `revise` skill.
