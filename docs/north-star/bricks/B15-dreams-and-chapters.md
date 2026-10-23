# B15 Dreams and chapters

Status: shipped, at the snapshot. Source: upstream.

Ultimate studies its own memory, failures, tools, and corrections, and then proposes what to codify or remove. A dream can seed a fresh chapter, a new conversation database that starts with the selected memory and work. Old chapters stay readable.

## How it works

`dream` runs sessions with read-only passes and keeps a journal and proposals. A chapter switch waits for idle conversations, a reviewed seed, and a final backup where possible. Then it restarts through a journal. `lib/chapters.ts` finds the chapter databases. The [dream README](../../../extensions/dream/README.md) holds the mechanics.

## Where it lives

- `extensions/dream/`: dream sessions
- `agents/dream-pass.md`: the read-only pass
- `lib/chapters.ts`: chapter databases and the switch journal

## Decisions

- None recorded

## Next

- A user subscription cannot move into a new chapter. Dream records a to-do to create it again (`74f38c9`)

## Evidence

- `34c001a` adds dreams
- `4c94093` adds chapters
- `74f38c9` seeds a chapter from a dream
- `af3b3a3` gates the chapter switch
