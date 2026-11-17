# Decision record template

Drafted by wrap-up for each decision the plan marked durable. Status starts
as `proposed`; the team accepts it through its normal review. Number it after
the highest existing record in `learning.decisions_dir`.

Filename: `{NNNN}-{slug}.md`.

```markdown
---
id: {NNNN}
title: {Decision in one line, as a statement}
status: proposed            # proposed | accepted | deprecated | superseded
date: {YYYY-MM-DD}
source: {PLAN_ID}
superseded_by: null
---

# {NNNN}: {Title}

## Context

{Two to five sentences. What situation forced a choice. Reference the plan
and the acceptance criteria or constraint that drove it. No restatement of
the whole feature.}

## Decision

{The choice, stated as a rule the next person can apply. One paragraph.}

## Alternatives rejected

- {Alternative} — {why not, in one line}

## Consequences

**Easier:** {what this makes simpler or safer}

**Harder:** {what this constrains or costs}

**Revisit when:** {the condition under which this decision should be
reconsidered, or "no known trigger"}
```

Keep the record under forty lines. A decision that needs more is two
decisions.
