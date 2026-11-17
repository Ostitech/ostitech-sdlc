# Intake questions

Ask these in one grouped message, with a best guess offered against each so
the owner confirms or corrects rather than composes from nothing. Skip a
question only when the conversation has already answered it.

## The questions

1. **Who uses it?** Which personas, and what are they trying to get done?
2. **Who is allowed to do what?** For each persona: which configured role,
   whether they can reach the screen at all, view only or edit, and which
   destructive actions (delete, lock, export, approve) they can take. Any data
   scoping: own site versus all sites, own records versus all, redaction.
3. **Where does it live and what triggers it?** Which screen, menu, button,
   schedule or inbound event starts it.
4. **What is the outcome?** What can the user do or see afterwards that they
   could not before?
5. **What is NOT in scope?** The related thing we are deliberately leaving
   out.
6. **What data does it depend on?** Existing reference data, feeds from other
   systems, calculations that must already exist.
7. **How will you know it is right?** Two or three concrete examples the
   feature must handle correctly, with the expected result. These become the
   acceptance criteria.

## Good and bad answers

| Question | Weak answer, probe further | Strong answer, use as is |
|---|---|---|
| Who uses it | "Managers" | "Site managers at a single site; regional managers across their region" |
| Allowed to do what | "Managers can manage it" | "`site_manager`: view and edit own site; `regional`: view all sites, no edit; `support`: everything, including delete" |
| Trigger | "From the app" | "A new item on the Stock menu; also opened from the Count Due banner on the dashboard" |
| Outcome | "Better visibility" | "A manager sees which lines are uncounted before close and can enter counts from a phone" |
| Not in scope | "Nothing I can think of" | "Approval workflow for counts; that stays manual this release" |
| Data | "The usual" | "Needs the item list per site and yesterday's closing stock; both exist today" |
| Right | "It works" | "Given a site with three uncounted lines at 16:00, when the manager opens Count Due, then those three lines show with yesterday's count prefilled" |

## Turning examples into acceptance criteria

Each example becomes one criterion in Given/When/Then. Keep the owner's nouns.
If an example needs a word the product does not use yet, add it to Open
questions rather than inventing it.

- Given a state the reader can set up.
- When one action.
- Then one observable result, including what is shown to whom.

## What not to ask

- Anything convention already answers (button placement, standard layouts).
- Anything about schema, storage, events, endpoints or integration. If the
  owner volunteers it, note it as an open question for the plan and move on.
- Estimates or phases.
