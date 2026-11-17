Use the plan skill to plan the following feature. There is no .sdlc/config.yaml in this repository; use the skill's defaults. Do not ask me questions; make reasonable assumptions and state them.

Feature: a small inventory service (Node, Express, Postgres via a migrations folder, Jest) needs a "stock adjustment" capability. A store manager records a manual adjustment to an item's on-hand quantity with a reason code, the adjustment is stored as an immutable event, the item's current quantity is recomputed from events, and a list screen shows adjustments for a site with filters by date and reason. Acceptance criteria: AC1 an adjustment with a reason code is persisted and visible in the list within one request; AC2 an adjustment without a reason code is rejected with a 400; AC3 the item quantity equals the sum of its events; AC4 the list filters by date range and reason.

The deliverable is the plan file written to plans/.
