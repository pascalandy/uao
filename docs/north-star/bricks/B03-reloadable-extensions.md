# B03 Reloadable extensions and surfaces

Status: shipped, at the snapshot. Source: upstream.

Each feature that is not core plumbing is an extension folder, with a server facet for agent behavior and a web facet for UI (`README.md`). A user or a project adds, replaces, or turns off a feature with no change to the core. A surface lets an extension be a full-screen app, with the agent one keystroke away.

## How it works

Discovery reads the clone, then `~/.ultimate/extensions/`, then the project, and a later folder with the same name replaces an earlier one. Extensions talk through typed APIs, durable events, and points. A core tier of 15 extensions is always on and depends only on itself, and `pnpm check` enforces the direction. Eight built-ins ship off. The [extension guide](../../../extensions/README.md) and [Extension mechanics](../../../docs/extensions.md) hold the rules, and [contract.md](../contract.md) lists the guarantees.

## Where it lives

- `extensions/`: the 48 built-ins, each with a README
- `shared/extension-api.ts`: API tokens, the core-tier reader, and `defaultOff`
- `server/discovery.ts` and `server/extensions.ts`: find and load server facets
- `server/vite-extensions.ts` and `web/src/extensions.ts`: load web facets
- `web/src/sdk/`: the SDK that web facets import as `@/sdk`
- `lint/ultimate.ts` and `scripts/deps.ts`: enforce the boundaries

## Decisions

- [D004](../decisions/D004-ui-from-extensions.md) Build the UI from extensions
- [D007](../decisions/D007-surfaces.md) Make apps surfaces beside the agent
- [D024](../decisions/D024-typed-contracts-core-tier.md) Connect extensions through typed contracts
- [D031](../decisions/D031-resource-built-ins-off.md) Ship resource-needing built-ins off

## Next

- Nothing stated

## Evidence

- `fff6d4b` adds web facets
- `790c34e` adds surfaces
- `f466038` adds typed APIs
- `7463db5` adds durable events
- `0edd691` adds the core tier
- `5323967` ships eight built-ins off
