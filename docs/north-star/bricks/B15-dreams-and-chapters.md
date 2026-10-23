# B15 Dreams and chapters

Status: shipped, at the snapshot. Source: upstream.

Ultimate studies its own memory, failures, tools, and corrections, and then proposes what to codify or remove. A dream can seed a fresh chapter, a new conversation database that starts with the selected memory and work. Old chapters stay readable.

## Where it lives

- `extensions/dream/`: dream sessions
- `agents/dream-pass.md`: the read-only pass
- `lib/chapters.ts`: chapter databases and the switch journal

## Evidence

- `34c001a` adds dreams
- `4c94093` adds chapters
- `74f38c9` seeds a chapter from a dream
- `af3b3a3` gates the chapter switch
