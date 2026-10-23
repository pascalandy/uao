# B01 Durable conversations

Status: shipped, at the snapshot. Source: upstream.

Every conversation, tool call, subagent, and document reaches SQLite before the UI shows it. A restart or a crash resumes each run from its last checkpoint, so no work and no context is lost. All other bricks stand on this one. The agent can change its own code because its state does not live in the process.

## How it works

Ultimate opens a Pi Durable harness on the SQLite database of the active chapter in the project home. Pi Durable runs an interrupted tool again only when the tool is replay-safe. Any other interrupted tool reports "interrupted" to the model. A durable event commits in the same transaction as its cause, so a reactor writes exactly once. [Durability](../../../docs/durability.md) explains the guarantees, and [Borrowed from Pi](../../../docs/pi-upstream.md) lists the local couplings to Pi.

## Where it lives

- `server/harness.ts`: opens Pi Durable on the active chapter
- `server/project.ts`: finds the home of each project
- `patches/`: version-pinned patches to Pi packages

## Decisions

- [D002](../decisions/D002-pi-durable-sqlite.md) Build on Pi Durable over SQLite

## Next

- Drop each local coupling and patch when Pi exports or fixes the capability (`docs/pi-upstream.md`)

## Evidence

- `692ca8f` opens the SQLite harness and tests a resume after SIGKILL
- `e3f76bb` keeps the ownership of storage through a swap and a crash
