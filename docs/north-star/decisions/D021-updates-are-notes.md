# D021 Send subagent updates as notes

Decided 2026-10-17. Source: upstream. Status: active.

A subagent's one-way update to its parent becomes a note, which starts no run. The parent reads the note with its next model request. Other one-way messages still wake their recipient (`extensions/messages/README.md`).

**Why.** An update from a subagent must not start a run in its parent, but an open question needs a reply (`304e47e`). The post calls the note "a super helpful primitive for agents to communicate effectively" (section "Notes").

**Rejected.** A reply request on every delivery (`304e47e`).

**Evidence.** `304e47e`. `extensions/messages/README.md` holds the mechanics.
