# D044 Let branches ask after @ultimate weighs in

Decided 2026-10-30, revised 2026-11-16. Source: upstream. Status: active.

A branch sends its decisions to @ultimate first (`e34af09d`). After @ultimate weighs in, the branch asks the user in its own conversation (`5014cc55`). @ultimate receives a question pointer and the answer as a note (`5014cc55`, `ae0d4fc2`). It can combine questions across branches or decide from existing authority (`agents/ultimate.md`). A standing agent can also message the user (`400f5758`).

@ultimate can settle an open question from the user's answer in its chat (`7b09649d`). The action records the calling conversation and the user's input (`extensions/messages/server.ts`).

**Why.** The pointer and answer note keep @ultimate informed without a relay through its chat (`5014cc55`).

**Rejected.** Only @ultimate can ask the user ([D022](D022-route-through-ultimate.md)). Subagents and side chats still cannot message the user (`extensions/messages/send.ts`, `400f5758`).

**Evidence.** `e34af09d`, `5014cc55`, `ae0d4fc2`, `7b09649d`, and `400f5758`. [Questions](../../../extensions/questions/README.md) holds the answer-card mechanics.
