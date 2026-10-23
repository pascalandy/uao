# B02 Self-change while running

Status: shipped, at the snapshot. Source: upstream.

Ultimate edits its own code while the conversation that edits it keeps running. A change to the UI or to an extension goes live at once, and a change to the core goes live through a checked swap. This capability is the premise of the [first prompt](../sources/first-prompt.md): "we built ultimate with ultimate".

## How it works

Each layer reloads in its own way, and [the layer table](../../../AGENTS.md#layers-and-how-they-reload) lists the ways. Vite hot-reloads web facets, and a server facet reinstalls on save. For a change to `server/` or `shared/`, the `restart` tool asks the supervisor for a swap. The supervisor type-checks and prepares a new generation, and a failed boot keeps the old one. [Running the server](../../../docs/running.md) holds the mechanics.

## Where it lives

- `bin/ultimate.ts`: the supervisor
- `server/supervisor-protocol.ts`: messages between the supervisor and a generation
- `server/build.ts`: the build identity of each section
- `extensions/self/`: the restart tool and its status
- `bin/cli.ts`: the emergency terminal agent for a broken UI, server, or database

## Decisions

- [D001](../decisions/D001-reload-by-layer.md) Reload each layer without ending the conversation
- [D003](../decisions/D003-supervisor-swap.md) Swap core generations through a supervisor

## Next

- Nothing stated

## Evidence

- `9b341af` seeds the layer table
- `e3f76bb` adds the swap and crash recovery
- `083fd2a` rolls back a failed swap
- `8233269` adds the build identity
- `56b0e1c` adds the emergency terminal agent
