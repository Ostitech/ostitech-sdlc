"""Check every skill before release.

- Frontmatter parses as strict YAML (the skills CLI is strict even where
  Claude Code is lenient; an unquoted ": " in a description breaks install).
- The frontmatter name matches the folder name.
- No client-specific terms appear anywhere in the skill folders.

Run: python scripts/check-skills.py   (needs PyYAML)
"""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORBIDDEN = re.compile(r"maxtel|mcdonald|eventledger|cognito|truenorth|outsystems", re.I)
failures = 0

for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
    text = skill.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        print(f"FAIL {skill}: no frontmatter"); failures += 1; continue
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as err:
        print(f"FAIL {skill}: {str(err).splitlines()[0]}"); failures += 1; continue
    if meta.get("name") != skill.parent.name:
        print(f"FAIL {skill}: name {meta.get('name')!r} != folder {skill.parent.name!r}"); failures += 1
    if not meta.get("description"):
        print(f"FAIL {skill}: missing description"); failures += 1
    for f in skill.parent.rglob("*"):
        if f.is_file() and FORBIDDEN.search(f.read_text(encoding="utf-8", errors="ignore")):
            print(f"FAIL {f}: client-specific term"); failures += 1

print("skills check:", "FAILED" if failures else "ok")
sys.exit(1 if failures else 0)
