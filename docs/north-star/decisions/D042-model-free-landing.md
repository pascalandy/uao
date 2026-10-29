# D042 Use one model-free path to the target branch

Decided 2026-10-28. Source: upstream. Status: active.

Only `workspace submit` reaches the project's target branch (`cfd0e93b`). The lander runs no model and refuses input (`cfd0e93b`). A landing concludes the branch unless work remains under way, wakes its starter, and releases an eligible checkout (`cfd0e93b`).

**Why.** The commit makes landing the end of a branch's work (`cfd0e93b`). Failures return to the submitter to fix and submit again (`cfd0e93b`).

**Rejected.** The lander agent definitions, model-driven failure repair, `workspace land`, and the deploy handoff (`cfd0e93b`). An automation on `workspaces.landed` can follow a landing (`cfd0e93b`).

**Evidence.** `cfd0e93b`, `72ba8465`, `b7060d00`, and `903ce43e`. [Lander mechanics](../../../extensions/workspaces/README.md#lander) define checks, receipts, reports, and cleanup.
