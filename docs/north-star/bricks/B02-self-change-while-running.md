# B02 Self-change while running

Status: shipped, at the snapshot. Source: upstream.

Ultimate edits its own code while the conversation that edits the code continues. A change to the UI or to an extension goes live at once. A change to the core goes live through a checked swap. This capability is the premise of the [first prompt](../sources/first-prompt.md): "we built ultimate with ultimate".

Update reports an owed restart when `server/` or `shared/` differs from the build at process start (`fe5907cd`). An agent still restarts the core with the `restart` tool (`agents/ultimate.md`). Update restarts it without an agent only for the stale-core recovery below.

The browser runs a production bundle, not the Vite dev server (`47c08a50`). A change to `web/` or a web facet rebuilds the bundle in a short-lived child process, and open pages switch to it with their view and drafts (`AGENTS.md`, `server/web.ts`). Reloads and restarts wait for the checkout and its packages after a landing (`1441b930`). When a facet fails to load against an old core, Update restarts the host through the checked swap (`f20cc792`, `ec0f235d`).

## Where it lives

- `bin/ultimate.ts`: the supervisor
- `server/supervisor-protocol.ts`: messages between the supervisor and a generation
- `server/build.ts`: the build identity of each section
- `server/web.ts` and `server/web-build.ts`: the production bundle of the web UI
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
- `6dd1aa58` verifies core process identity before a stale storage lock is taken
- `91f1fde4` passes the core start time explicitly to the lock check
- `eade452f` lets the supervisor coordinate a systemd shutdown
- `47c08a50` serves the web UI as a production bundle that a child process builds
- `f20cc792` restarts the host when a facet fails to load against an old core
- `1441b930` makes loads wait for the checkout and its packages after a landing
