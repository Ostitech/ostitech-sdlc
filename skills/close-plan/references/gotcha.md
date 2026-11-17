# Gotcha template

One file per unplanned problem worth keeping: non-obvious cause, or likely to
recur. Filed under `learning.gotchas_dir` by close-out. Short enough that the
next plan can read ten of them.

Filename: `{area}-{slug}.md`.

```markdown
---
title: {Symptom in one line}
date: {YYYY-MM-DD}
area: {subsystem, tool, or environment it belongs to}
source: {PLAN_ID}
---

# {Symptom in one line}

**Symptom.** {What you saw: the error, the wrong value, the hang.}
**Cause.** {Why it happened, with the file or setting responsible.}
**Fix.** {What resolved it, and what to do next time it appears.}
```

One paragraph of three sentences is the target. Do not include the full
investigation; link the plan checkpoint or investigation file if it exists.
