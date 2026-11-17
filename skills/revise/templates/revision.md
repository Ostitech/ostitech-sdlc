---
id: {REVISION_ID}
parent: {PRD_ID}
title: {Short description of this revision}
status: draft            # draft | signed-off | shipped
tracker: {tracker item reference, or none}
created: {YYYY-MM-DD}
---

# {REVISION_ID} — {Short description}

Parent: [{PRD_ID}](./{parent file}) · Trigger: {post-UAT feedback | production defect that exposed a wrong spec | new ask}

## What is changing and why

{Two to four sentences. What the owner observed or asked for, and why the
shipped behaviour no longer fits.}

## Changes to the parent PRD

Applied inline to the parent in the same change. This section is the diff.

### Added

- {Section} — {text added}

### Changed

- {Section} — was: {old}; now: {new}

### Removed

- {Section} — {text removed}

## New or changed acceptance criteria

A revision must add or change at least one. Numbering continues from the parent.

- **AC{n}** — Given {state}, when {action}, then {observable result}.

## Impact on existing acceptance criteria

| AC | Impact | Note |
|---|---|---|
| AC1 | unchanged / amended / retired | |

## Open questions

| # | Question | Owner | Resolved |
|---|---|---|---|
| Q1 | | | |

## Notes

{Sequencing constraints, related revisions, anything else.}
