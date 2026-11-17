---
name: revise
description: Record a revision to a PRD that has already shipped (post-UAT feedback, a production defect that exposed a wrong specification, or a new ask against a live feature) as a revision document, and amend the parent PRD inline so it stays the current-state specification. Use when the user wants to revise, amend or raise a change against a shipped PRD, or invokes /revise. Never implements, and never revises a draft; that is an edit.
argument-hint: <PRD id or path> <what is changing>
---

# Revise

A revision is a PRD in delta form. It records what is changing in agreed
behaviour and why, adds or changes acceptance criteria, and updates the parent
PRD so the parent remains the single current-state description of the
feature. The revision document is what the owner signs off; the parent is
what everyone reads afterwards.

**Input:** $ARGUMENTS (absent: use the conversation).

## 0. Load configuration

1. Read `${CLAUDE_PROJECT_DIR}/.sdlc/config.yaml` if present; apply defaults
   from `references/config.md` for anything missing.
2. Read `${CLAUDE_PROJECT_DIR}/.sdlc/extensions/revise.md` if present. The one
   extension point is `checks`; keep its content for step 5. Warn once about
   unknown headings and ignore them.

## 1. Confirm the parent

Resolve the PRD from the input by id, folder, path or title under
`artefacts.prd_dir`. If several match, ask. Then check its status:

| Parent status | Do |
|---|---|
| `shipped` | Continue |
| `draft` or `signed-off` | Stop. The feature has not shipped; edit the PRD in place (optionally via the `prd` skill) and note the change in its revision history |
| `superseded` | Stop and point at the successor |

Read the parent in full, including its revision history and every earlier
revision document, so the new revision builds on the current state and not on
the original.

## 2. Clarify, leanly

Ask only what the revision needs: what the owner observed or wants, which
existing behaviour it changes, what must stay the same, and the concrete
example that shows it is right. Offer a best guess for each. Do not re-run
full intake; the parent already answers who, where and why.

## 3. The acceptance-criteria test

A revision must add or change at least one acceptance criterion. If the change
does not (wording, attribution, a clarification engineering needs), stop:
make the edit inline in the parent, add a revision-history row describing it
with no document link, and tell the user why no revision was created.

## 4. Identity, branch, documents

1. Compute the id from `ids.revision`: the next free number for this parent.
2. Create or switch to the branch from `branches.prd` using the revision id
   and a slug for this revision, not the parent's slug. Stop and ask if the
   working tree has unrelated changes.
3. Write the revision document from `templates/revision.md`: in the
   parent's folder as `R{nn}-{revision slug}.md` for the `folder` layout, or
   beside the parent as `{REVISION_ID}-{revision slug}.md` for `flat`. The Changes to
   the parent PRD section is the diff: every added, changed and removed
   sentence, by section. Acceptance-criteria numbering continues from the
   parent's highest.
4. Apply every change from that section to the parent inline, so the parent
   reads as the new current state. Retired criteria are struck through with
   the revision id, not deleted.
5. Add a row to the parent's revision history: revision id, date, one-line
   change, link to the document.

## 5. Checks

1. At least one acceptance criterion added or changed.
2. Every change listed in the revision document is present in the parent, and
   nothing changed in the parent that the document does not list.
3. No design language in either document (schema, table, column, event type,
   endpoint, migration, integration mechanics). Convert hits to open
   questions.
4. The impact table covers every parent criterion the change touches.
5. Everything under the `checks` extension point.

## 6. Sign off and hand off

Show both documents and invite changes. On the owner's confirmation:

1. Set `status: signed-off` on the revision document.
2. If `tracker.type` is not `none` and access exists, create the tracker item
   linked to the parent's item; otherwise tell the user what to create.
3. Hand off: name the `plan` skill with the revision document as its input.

## Never

- Implement, plan, or estimate.
- Revise a PRD that has not shipped.
- Create a revision that changes no acceptance criterion.
- Leave the parent describing the old behaviour.
- Delete a retired criterion; strike it through with the revision id.
