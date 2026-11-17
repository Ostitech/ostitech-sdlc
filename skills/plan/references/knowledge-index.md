# Knowledge-index retrieval (reserved)

Enabled by `context.knowledge_index: true`. This contract version ships the
hook but not the tooling; the retrieval protocol below is what the plan skill
runs when a repository carries a tagged documentation index.

Expected shape, per repository: `docs/knowledge-index.json` with
`{ _meta, docs: [{ id, type, scope, status, tags, summary, path }] }`, and a
`docs/tags.yaml` declaring the tag vocabulary and any cross-repository routing.

## Protocol at plan time

1. Derive candidate tags from the trigger: title, acceptance criteria, touched
   paths.
2. Load the repository's index and, if a parent workspace index exists, that
   too.
3. Follow any routing rules whose tags overlap the candidates and load the
   indexes they name.
4. Tag-match across loaded indexes; ignore entries whose status is
   `deprecated` or `superseded`.
5. Read the matched documents in full. Decision records are reconciled,
   patterns are followed, architecture is understood, runbooks and references
   are read on demand.
6. Fill the plan's **Documents reconciled** table from the matches, one row
   each, with a note.

When the index file is absent despite the flag, warn and fall back to the
default behaviour in SKILL.md step 2.
