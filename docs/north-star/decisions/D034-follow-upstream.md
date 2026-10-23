# D034 Follow upstream through merges

Decided 2026-10-23. Source: uao. Status: active.

Pascal merges `upstream/main` into uao when he wants its changes. uao keeps its own additions in places that upstream does not edit, to decrease the risk of a merge conflict. After each merge, an agent updates the north-star.

**Why.** Pascal wants Daniel's changes without a conflict at each merge (Pascal, 2026-10-23).

**Evidence.** Pascal stated the rule on 2026-10-23. The fork commit `7698625` shows the fork point, not the rule. The [sync rule](../upstream.md#sync-rule) holds the steps and the additive places.
