# D021 Send subagent updates as notes

Decided 2026-10-17. Source: upstream. Status: active.

A subagent's one-way update to its owner becomes a note, which starts no turn. The owner reads the note in its next model request. Other one-way messages still wake their recipient (`extensions/messages/README.md`). One more exception applies: @ultimate's triage can keep a one-way message from a conversation as context, with no wake ([triage](../../../extensions/messages/README.md#triage-for-the-primary-agent)).

**Why.** An update from a subagent must not start a turn in its owner, but an open question needs a reply (`304e47e`). The post calls the note "a super helpful primitive for agents to communicate effectively" (section "Notes").

**Rejected.** A reply request on every delivery (`304e47e`).

**Evidence.** `304e47e`. `extensions/messages/README.md` holds the mechanics.
