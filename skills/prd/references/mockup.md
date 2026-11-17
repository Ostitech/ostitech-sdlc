# Mockup rules

A mockup is a static HTML page that shows the owner what they asked for before
anything is built. It is a sign-off aid, not a prototype.

Build one only when `design_system.path` is set or the user asks for one.

## Location

`artefacts.mockup_dir/{PRD_ID}-{slug}/index.html`, one file per screen if the
PRD describes more than one (`index.html`, `detail.html`, and so on). Set the
PRD frontmatter `mockups:` to the folder's relative path.

## Rules

1. **Documented components and tokens only.** Read `design_system.guide`
   first, then use the stylesheet and component catalogue under
   `design_system.path`. Do not introduce colours, fonts, spacing or component
   styles that are not documented there.
2. **Per-screen tweaks stay small.** A screen-specific column treatment or
   layout goes in an inline `<style>` block in the head, under about thirty
   lines, using the design system's CSS variables. No hex codes.
3. **Realistic data, never lorem ipsum.** Use `placeholder_data` from config
   for names, places, quantities and currency. If it is null, ask the owner for
   one paragraph of sample context and propose adding it to the config.
4. **Match the product's screen anatomy** as the guide describes it
   (navigation, page header, filters, main content). A mockup that looks like
   a different product is not reviewable.
5. **Link back.** The first line of the file is an HTML comment naming the PRD
   id and its relative path.
6. **Render overlays open.** A modal, slide-over or popover the PRD describes
   is rendered in its open state so the reviewer sees it without clicking.
7. **Show every state the acceptance criteria mention.** Empty, loading,
   error, and role-restricted states each get a section or a second file.
8. **No behaviour.** No JavaScript beyond what the design system itself
   requires for rendering. Interaction is described in the PRD, not simulated.

## Review

Open the mockup in a browser when one is available and check it against the
PRD's Proposed behaviour section by name. Every screen, section and action the
PRD names must be visible in the mockup; every element in the mockup must be
named in the PRD. Fix the mismatch on whichever side is wrong.
