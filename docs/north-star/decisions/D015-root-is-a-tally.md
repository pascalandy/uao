# D015 Make the root a tally that runs no turns

Decided 2026-10-16, revised 2026-10-22. Source: upstream. Status: active.

A root becomes a tally when its first branch starts. From then on, it accepts no input and runs no turns (`refuseTally` in `extensions/lineage/server.ts`). It records its tree: branch intents, abstracts, notes, and landings. All work happens in branches. Since `86ed900`, a project has one root. Independent work goes into branches.

**Why.** Work stays in branch conversations. The root collects what the tree did (`00cdf3a`). The tools that made and seeded roots became obsolete when branches started from project memory (`86ed900`).

**Rejected.** Roots that were agents and wrote a brief for each branch (`00cdf3a`). Several roots in one project (`bbb0e3e`), removed by `86ed900`.

**Evidence.** `bbb0e3e`, `00cdf3a`, and `86ed900`. `extensions/lineage/README.md` holds the mechanics.
