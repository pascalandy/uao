# B01 Durable conversations

Status: shipped, at the snapshot. Source: upstream.

Every conversation, tool call, subagent, and document reaches SQLite before the UI shows it. Committed conversation state survives a restart or a crash. A run resumes from its last checkpoint. An interrupted tool runs again only when it is marked replay-safe ([Durability](../../../docs/durability.md)). An effect outside the transaction is not rolled back ([Durability](../../../docs/durability.md), `extensions/codemode/README.md`). All other bricks depend on this brick. The agent can change its own code because its state is stored outside the process.

A top-level conversation can request self-compaction when its definition names the deferred tool `compact` (`extensions/lineage/server.ts`). `extensions/lineage/server.ts` holds the two wake-up paths: one for @ultimate and one for other top-level conversations. Subagents use automatic compaction, which continues their run without a separate wake-up (`4a6aab5`).

An effect outside the store, such as a post to another Ultimate or a push notification, is a durable effect task. The commit that decides the effect also creates the task. The task runs at least once, so the effect must accept a second run with the same key (`4dfe1142`, `47cfa17c`, [Durability](../../../docs/durability.md)). The lint rule `ultimate/no-unowned-work` refuses server work that a crash would lose. An exception must give its reason in code with `rebuiltOnOpen` or `inProcess` (`24717b86`, `lib/errors.ts`). A replay-safe tool also gives its reason in code (`e427cb99`, `lib/replay.ts`).

When a server closes, the release callbacks of the extensions run first. Then the Harness closes before the extensions go, so work that runs at shutdown stays pending and continues at the next open (`4f2845dc`, `90d062f3`). Ultimate runs on Pi 1.5.2 (`3f11fcc2`).

## Where it lives

- `server/harness.ts`: opens Pi Durable on the active chapter
- `server/project.ts`: finds the home of each project
- `extensions/lineage/server.ts`: self-compaction and wake-up tasks
- `patches/`: version-pinned patches to Pi packages
- `lib/effect.ts`: durable effect tasks
- `lib/errors.ts` and `lib/replay.ts`: the named exceptions for unowned work and replay-safe tools

## Decisions

- [D002](../decisions/D002-pi-durable-sqlite.md) Build on Pi Durable over SQLite

## Evidence

- `692ca8f` opens the SQLite harness and tests a resume after SIGKILL
- `e3f76bb` keeps the ownership of storage through a swap and a crash
- `d3178ff` extends self-compaction beyond @ultimate
- `4a6aab5` commits self-compaction with its wake-up for top-level conversations other than @ultimate and refuses subagents
- `669df90a` and `0baa03e4` move Ultimate to Pi 1.5.0 and port the local Pi Durable patches
- `3d922572` chooses the compaction profile from the model's context window, not from the model name
- `3f11fcc2` moves Ultimate to Pi 1.5.2
- `4dfe1142` adds durable effect tasks, and `24717b86` adds the lint rule `ultimate/no-unowned-work`
- `4f2845dc` and `90d062f3` close the Harness before the extensions at shutdown
