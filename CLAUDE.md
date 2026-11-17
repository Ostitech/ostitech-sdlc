# ostitech-sdlc

Open-core skills for agentic software delivery. Read `docs/methodology.md`
before changing any skill and `docs/extension-points.md` before changing the
configuration contract.

## Rules for this repository

- A skill is generic. Anything an organisation would set differently goes
  through `.sdlc/config.yaml` or an extension point, never into a skill body.
- No client material. No client names, products, file paths, incidents or
  worked examples. Examples are invented and domain-neutral.
- `SKILL.md` stays under about 180 lines. Detail goes in `references/`,
  loaded on demand. Templates the skill writes from go in `templates/`.
- Every file a skill needs lives inside that skill's folder, because the
  skills CLI vendors skill folders only.
- Changing the meaning of a config key or an extension point is a contract
  version bump; adding one is not. Record both in `CHANGELOG.md`.
- Prose style: second person, imperative, short sentences, no em-dashes.

## Checks before committing

```
claude plugin validate .
claude plugin eval evals
```
