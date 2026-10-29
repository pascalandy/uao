# B15 Dreams and chapters

Status: shipped, at the snapshot. Source: upstream.

A dream is ordinary branch work (`be1608a7`). @ultimate writes its handoff, starts one dream branch, and receives proposals from six read-only passes (`extensions/dream/DREAM.md`). The passes include project-specific improvements (`743a0b65`). The [dream workflow](../../../extensions/dream/DREAM.md) owns the process.

Dream before compaction fires at 70% context by default (`1353fb6b`). Dream after a pause fires above 50% after eight hours without user input (`6c37a236`). Both are ordinary context automations that wake @ultimate (`extensions/dream/built-ins.ts`).

Approved proposals become ordinary branches or memory writes (`extensions/dream/DREAM.md`). @ultimate can prepare a fresh chapter, but only the user can press Fall asleep ([D040](../decisions/D040-dream-as-ordinary-work.md)). The switch preserves memory and open work through a seed, backups, and a journaled restart (`extensions/dream/server.ts`, `extensions/dream/seed.ts`).

Old chapters remain readable, and the user can switch back (`extensions/dream/README.md`). A seeded chapter starts its first backup when cloud backups are available (`ef1883dc`, `5704358d`). The [chapter mechanics](../../../extensions/dream/README.md#chapters) own the checks and recovery rules.

## Where it lives

- `extensions/dream/DREAM.md`: instructions for @ultimate and the dream branch
- `extensions/dream/built-ins.ts`: the two context automations
- `extensions/dream/server.ts`: preparation and user-only chapter changes
- `extensions/dream/seed.ts`: memory and open work for the next chapter
- `agents/dream-pass.md`: the read-only passes
- `lib/chapters.ts`: chapter databases and the switch journal

## Decisions

- [D039](../decisions/D039-remove-automation-grants.md) Remove automation grants
- [D040](../decisions/D040-dream-as-ordinary-work.md) Make dreaming ordinary work

## Evidence

- `34c001a` adds dreams, and `4c94093` adds chapters
- `09008b66` moves the dream trigger before compaction
- `ef738270` removes automation grants and makes Fall asleep user-only
- `be1608a7` removes tracked dream sessions, proposal states, `dream.asleepAfter`, and the scratch-instance chapter gate
- `d3da2f74` preserves pending delivery request IDs and refuses older pending seeds with a recovery path
