# B15 Dreams and chapters

Status: shipped, at the snapshot. Source: upstream.

Ultimate studies its own memory, failures, tools, and corrections, and then proposes what to codify or remove. "Codify" is the name of the fifth pass of a dream (`extensions/dream/README.md`). A dream can seed a fresh chapter, a new conversation database that starts with the selected memory and work. Old chapters stay readable.

The built-in **Dream after compaction** automation starts a dream after @ultimate compacts, once other top-level conversations stop work (`extensions/dream/after-compaction.ts`). The user can pause or delete this automation (`extensions/dream/README.md`). @ultimate decides the dream's proposals only when the user grants `dream` on that automation (`agents/ultimate.md`).

After this dream settles, `dream.asleepAfter` sets how many landed or applied changes justify a fresh chapter (`extensions/dream/after-compaction.ts`). At or above the threshold, an `asleep` grant permits the checked switch (`extensions/dream/after-compaction.ts`). Without that grant, or if the grant is refused, the user gets a question (`extensions/dream/after-compaction.ts`). The [dream mechanics](../../../extensions/dream/README.md#dream-after-compaction) hold the defaults and gates. The new chapter carries @ultimate's latest compaction summary so its work can continue (`extensions/dream/seed.ts`).

## Where it lives

- `extensions/dream/`: dream sessions
- `extensions/dream/after-compaction.ts`: the built-in automation, its wait, and its chapter check
- `agents/dream-pass.md`: the read-only pass
- `lib/chapters.ts`: chapter databases and the switch journal

## Evidence

- `34c001a` adds dreams
- `4c94093` adds chapters
- `74f38c9` seeds a chapter from a dream
- `af3b3a3` gates the chapter switch
- `7c0a3f4` lets a user grant authorize a dream or a checked chapter switch
- `11d1d4c` keeps a refused chapter switch from releasing another switch's lock
- `6c1c6bc` starts dreams after @ultimate compacts and checks whether a fresh chapter is justified
- `1223ae5` and `fc92c4e` recover the exact built-in automation after a lost receipt
- `4195ad4` keeps old chapter seeds from deleting the built-in automation
