# B01 Durable conversations

Status: shipped, at the snapshot. Source: upstream.

Every conversation, tool call, subagent, and document reaches SQLite before the UI shows it. Committed conversation state survives a restart or a crash. A run resumes from its last checkpoint. An interrupted tool runs again only when it is marked replay-safe ([Durability](../../../docs/durability.md)). An effect outside the transaction is not rolled back ([Durability](../../../docs/durability.md), `extensions/codemode/README.md`). All other bricks depend on this brick. The agent can change its own code because its state is stored outside the process.

## Where it lives

- `server/harness.ts`: opens Pi Durable on the active chapter
- `server/project.ts`: finds the home of each project
- `patches/`: version-pinned patches to Pi packages

## Decisions

- [D002](../decisions/D002-pi-durable-sqlite.md) Build on Pi Durable over SQLite

## Evidence

- `692ca8f` opens the SQLite harness and tests a resume after SIGKILL
- `e3f76bb` keeps the ownership of storage through a swap and a crash
