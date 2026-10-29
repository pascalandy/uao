# D021 Send subagent updates as notes

Decided 2026-10-17. Source: upstream. Status: replaced by D041.

A subagent's one-way update to its parent becomes a note, which starts no turn (`304e47e`). The parent reads the note in its next model request (`304e47e`). The later [D041](D041-state-based-waking.md) extends this rule to branch updates and replaces triage.

**Why.** An update from a subagent must not start a turn in its parent, but an open question needs a reply (`304e47e`). The post calls the note "a super helpful primitive for agents to communicate effectively" (section "Notes").

**Rejected.** A reply request on every delivery (`304e47e`).

**Evidence.** `304e47e`. `extensions/messages/README.md` holds the mechanics.
