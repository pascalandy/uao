# D013 Keep branches apart from subagents

Decided 2026-10-14. Source: upstream. Status: active.

A subagent has an owner, which is the conversation that started it. A branch has no owner. It records only its source and its fork point. In code, `parentConversationId` marks the owner and `branchOf` marks the source.

**Why.** A branch without an owner must stay a top-level conversation (`40359cf`).

**Rejected.** One parent link for both the source and the owner (`40359cf`).

**Evidence.** `99c76b2` adds branches. `40359cf` separates the source from the owner. `extensions/lineage/README.md` holds the mechanics.
