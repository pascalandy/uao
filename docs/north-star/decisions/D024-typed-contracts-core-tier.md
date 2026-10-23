# D024 Connect extensions through typed contracts

Decided 2026-10-18, revised 2026-10-19. Source: upstream. Status: active.

Extensions use one another only through typed APIs, durable events, and points. A core tier of extensions is always on and depends only on itself. Optional extensions reach the core tier through points or events, and `pnpm check` enforces the direction.

**Why.** Service names were untyped strings, and a missing provider returned a silent `undefined` (`f466038`). A core extension that a user turned off made states that the code did not support (inferred from `0edd691`).

**Rejected.** Raw service strings with `host.provide` and `host.use` (`f466038`). An event bus in the memory of one process, which `afa5377` removed.

**Evidence.** `f466038`, `7463db5`, `0edd691`, and `1147824`. [Core tier](../../../docs/extensions.md#core-tier) holds the mechanics.
