# Contributing

Thanks for helping grow **Awesome Internet of the Body**. The goal is a trustworthy,
scannable index of places you can **consume human data via app integrations**.

## What belongs here

An entry qualifies if it:

1. **Gathers human data** — physiology, biometrics, behavior, or -omics — **and moves
   it somewhere** (an app, a cloud, or your own server).
2. Is **real and verifiable** — a working link to the project, product, API, or spec.
3. Ideally exposes an **integration surface** (API, SDK, webhook, or open export).
   Link it directly when one exists.

## What does *not* belong

- Pure lifestyle blogs, newsletters, or podcasts with no data surface
- Dead products with no remaining archive or API (open an issue to remove them)
- Generic EHR vendors with no consumer/device body-data angle (unless they expose a clear patient-facing data API)
- Fabricated, AI-hallucinated, or unverifiable links

## Formatting rules

- One entry per line, in the section it best fits.
- Start with the **openness** marker: 🟢 open source · 🔵 open standard / SDK · ⚪ commercial / proprietary.
- End data-feed entries with a **cadence** tag in backticks: `` `live` `` · `` `snapshot` `` · `` `live + history` ``.
  Leave standards, SDKs, and tooling untagged (they carry either mode).
- Keep the description to **one factual line**. No marketing copy, no hype.
- Prefer linking the **developer docs / API / source repo** when one exists, not only the marketing homepage.
- **No fabricated links or claims.** If you can't verify it, don't add it.
- Use plain words in any new section heading (avoid `&`, commas, en-dashes) so the
  table-of-contents anchors resolve consistently.
- Prefer **alphabetical order within a section** when it does not hurt readability.

## How to submit

Open a pull request that:

- Adds your entry (and, if needed, a new section + its Contents link).
- Updates the entry-count claim in the intro (`200+`) if the total moves materially.
- Keeps sections readable — clarity beats strict ordering.

Or open an issue proposing the addition with a source, and a maintainer can add it.

## Removals

Entries can be removed if a project shuts down, a link dies, or it turns out not to
gather human data. A dead link is a bug — please report it.

## Quality bar

Before merging, a maintainer should be able to answer:

1. What human signal does this capture?
2. Where does the data go?
3. Is the link still live?
