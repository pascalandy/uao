# D039 Remove automation grants

Decided 2026-10-25. Source: upstream. Status: active.

Automations no longer grant authority to dream, compact, or change chapters (`ef738270`). The `act` operation is removed (`ef738270`). Fall asleep always requires the user (`ef738270`).

**Why.** No automation held a grant, and no `act` call had been made (`ef738270`).

**Rejected.** Grants and their action dispatcher, introduced by `d6c9628` and removed by `ef738270`.

**Evidence.** `ef738270`. `extensions/automations/README.md` owns automation actions. `extensions/dream/server.ts` makes chapter changes user-only.
