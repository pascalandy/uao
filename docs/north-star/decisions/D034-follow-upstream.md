# D034 Follow upstream through merges

Decided 2026-10-23. Source: uao. Status: active.

Pascal merges `upstream/main` into uao when he wants its changes. uao keeps its own additions in places that upstream does not edit, so that a merge has no conflict. After each merge, an agent checks each brick status again and moves the snapshot.

**Why.** Pascal wants Daniel's changes without a conflict at each merge (Pascal, 2026-10-23).

**Evidence.** Pascal stated the rule on 2026-10-23. [upstream.md](../upstream.md#sync-rule) holds the steps.
