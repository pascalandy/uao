# D021 Send updates as notes

Decided 2026-10-17. Source: upstream. Status: active.

Each message records its type: a one-way note, or a request that expects a reply. A note does not start a run in the recipient.

**Why.** An update from a parent must not start a run, but an open question needs a reply (`304e47e`). The post calls the note "a super helpful primitive for agents to communicate effectively" (section "Notes").

**Rejected.** A reply request on every delivery (`304e47e`).

**Evidence.** `304e47e`. `extensions/messages/README.md` holds the mechanics.
