# D026 Keep the system prompt stable

Decided 2026-10-19. Source: upstream. Status: active.

The system prompt does not change between turns. Facts that change, such as the list of conversations, come from codemode or from a note on the next input.

**Why.** On the Claude Code path, each change rewrote the whole cached context. 74% of turns after a change read nothing from the cache, at $1.30 for each turn compared with $0.09 (`803cbee`).

**Rejected.** Prompt sections that listed the conversations and the surface on screen (`803cbee`).

**Evidence.** `803cbee`. `7054ecf` moves the identity of a conversation into an input note for the same reason. `a5dea087` patches Pi Durable to append a new or returning prompt section. Before, Pi Durable sent the full system prompt again, 40 times in two days (`a5dea087`, [Borrowed from Pi](../../pi-upstream.md)).
