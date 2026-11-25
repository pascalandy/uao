# D044 Let branches ask after @ultimate weighs in

Decided 2026-10-30, revised 2026-11-24. Source: upstream. Status: active.

A branch sends its decisions to @ultimate first (`e34af09d`). After @ultimate weighs in, the branch asks the user in its own conversation (`5014cc55`). The standing agent that started the branch receives a question pointer and the answer as a note. That agent is @ultimate when a coordinator, a side chat, or no standing agent started the branch (`5014cc55`, `ae0d4fc2`, `52054fd9`). It can combine questions across branches or decide from existing authority (`agents/ultimate.md`). Any conversation except a subagent can message the user, for example a chat that an extension or an automation starts (`400f5758`, `3aed7ab8`). A coordinator asks the user directly when the user talks to it (`a7719a89`).

@ultimate can settle an open question from the user's answer in its chat (`7b09649d`). The action records the calling conversation and the user's input (`extensions/messages/server.ts`).

**Why.** The pointer and answer note keep @ultimate informed without a relay through its chat (`5014cc55`).

**Rejected.** Only @ultimate can ask the user ([D022](D022-route-through-ultimate.md)). A subagent still answers only the conversation that started it (`3aed7ab8`).

**Evidence.** `e34af09d`, `5014cc55`, `ae0d4fc2`, `7b09649d`, `400f5758`, `3aed7ab8`, and `52054fd9`. [Questions](../../../extensions/questions/README.md) holds the answer-card mechanics.
