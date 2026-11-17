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

# Duplicate keys in the shipped config template or schema: YAML and JSON
# loaders keep the last silently, so an edit applied twice goes unnoticed.
import json

class _DupKeyLoader(yaml.SafeLoader):
    pass

def _no_dup_mapping(loader, node):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node)
        if key in seen:
            raise yaml.YAMLError(f"duplicate key {key!r}")
        seen.add(key)
    return loader.construct_mapping(node)

_DupKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dup_mapping)

def _no_dup_pairs(pairs):
    keys = [k for k, _ in pairs]
    dups = {k for k in keys if keys.count(k) > 1}
    if dups:
        raise ValueError(f"duplicate key(s) {sorted(dups)}")
    return dict(pairs)

template = ROOT / "skills/init-app/templates/config.yaml"
schema = ROOT / "skills/init-app/templates/sdlc.config.schema.json"
try:
    yaml.load(template.read_text(encoding="utf-8"), Loader=_DupKeyLoader)
except yaml.YAMLError as err:
    print(f"FAIL {template}: {err}"); failures += 1
try:
    json.loads(schema.read_text(encoding="utf-8"), object_pairs_hook=_no_dup_pairs)
except ValueError as err:
    print(f"FAIL {schema}: {err}"); failures += 1

print("skills check:", "FAILED" if failures else "ok")
sys.exit(1 if failures else 0)
