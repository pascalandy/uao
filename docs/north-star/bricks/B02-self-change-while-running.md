# B02 Self-change while running

Status: shipped, at the snapshot. Source: upstream.

Ultimate edits its own code while the conversation that edits the code continues. A change to the UI or to an extension goes live at once. A change to the core goes live through a checked swap. This capability is the premise of the [first prompt](../sources/first-prompt.md): "we built ultimate with ultimate".

## Where it lives

- `bin/ultimate.ts`: the supervisor
- `server/supervisor-protocol.ts`: messages between the supervisor and a generation
- `server/build.ts`: the build identity of each section
- `extensions/self/`: the restart tool, its status, and the hot-reload toast
- `extensions/prompt/`: the Reloaded divider
- `docs/running.md`: supervisor diagnostics and recovery after failed boots

## Decisions

- [D001](../decisions/D001-reload-by-layer.md) Reload each layer without ending the conversation
- [D003](../decisions/D003-supervisor-swap.md) Swap core generations through a supervisor

## Evidence

- `9b341af` seeds the layer table
- `e3f76bb` adds the swap and crash recovery
- `083fd2a` reverts a failed swap
- `8233269` adds the build identity
- `56b0e1c` adds the emergency terminal agent. `17d186bf` removes it because it was unused
- `b535e02` names landed features in the Reloaded divider and the hot-reload toast
