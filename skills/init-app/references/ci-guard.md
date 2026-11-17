# CI guard for vendored skills

The skills are installed into the repository by the `skills` CLI, which
records each skill's source commit and a content hash in `skills-lock.json`.
A skill edited in place silently forks from its upstream: the next update
either overwrites the edit or is skipped forever, and customisation ends up
somewhere the extension points cannot see. This check fails the build when any
vendored skill no longer matches its lock hash, so the only routes for
customisation are `.sdlc/config.yaml`, `.sdlc/extensions/`, or a pull request
upstream.

`npx skills check` also exits non-zero when an update is merely available, so
the guard reads `npx skills list --json` and fails only on status `modified`.
Skills the lock does not track (the repository's own skills) report
`untracked` and pass.

## GitHub Actions

```yaml
name: skills-guard
on: [pull_request, push]
jobs:
  guard:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - name: Fail on locally modified vendored skills
        run: |
          npx --yes skills list --json > skills-status.json
          node -e '
            const s = JSON.parse(require("fs").readFileSync("skills-status.json","utf8"));
            const all = Array.isArray(s) ? s : (s.skills || s.project || []);
            const bad = all.filter(x => x.status === "modified").map(x => x.name);
            if (bad.length) { console.error("Vendored skills modified locally: " + bad.join(", ")); process.exit(1); }
            console.log("Vendored skills match skills-lock.json");
          '
```

## Azure Pipelines

```yaml
trigger: [main]
pr: [main]
pool:
  vmImage: ubuntu-latest
steps:
  - task: NodeTool@0
    inputs:
      versionSpec: '22.x'
  - script: |
      npx --yes skills list --json > skills-status.json
      node -e '
        const s = JSON.parse(require("fs").readFileSync("skills-status.json","utf8"));
        const all = Array.isArray(s) ? s : (s.skills || s.project || []);
        const bad = all.filter(x => x.status === "modified").map(x => x.name);
        if (bad.length) { console.error("Vendored skills modified locally: " + bad.join(", ")); process.exit(1); }
        console.log("Vendored skills match skills-lock.json");
      '
    displayName: Fail on locally modified vendored skills
```

The JSON shape from `skills list --json` has changed between CLI versions;
the snippets accept either a top-level array or an object with a `skills` or
`project` array. Pin the CLI version with `npx --yes skills@<version>` once a
version is in use.
