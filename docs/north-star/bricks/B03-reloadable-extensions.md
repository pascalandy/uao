# B03 Reloadable extensions and surfaces

Status: shipped, at the snapshot. Source: upstream.

Each feature that is not core infrastructure is an extension folder, with a server facet for agent behavior and a web facet for UI (`README.md`). A user or a project adds, replaces, or disables a feature with no change to the core. A surface lets an extension be a full-screen app, with the agent one keystroke away.

Web facets can register code-block renderers by language (`61b25245`). Linked user and project extensions keep their current code and Tailwind styles after a link changes (`4ddbece8`, `027057d3`).

## Where it lives

- `extensions/`: the built-ins, each with a README
- `shared/extension-api.ts`: API tokens, the core-tier reader, and `defaultOff`
- `server/discovery.ts` and `server/extensions.ts`: find and load server facets
- `server/vite-extensions.ts` and `web/src/extensions.ts`: load web facets
- `web/src/sdk/`: the SDK that web facets import as `@/sdk`
- `lint/ultimate.ts` and `scripts/deps.ts`: enforce the boundaries

## Decisions

- [D004](../decisions/D004-ui-from-extensions.md) Build the UI from extensions
- [D007](../decisions/D007-surfaces.md) Make apps surfaces beside the agent
- [D024](../decisions/D024-typed-contracts-core-tier.md) Connect extensions through typed contracts
- [D031](../decisions/D031-resource-built-ins-off.md) Disable by default the built-ins that need resources

## Evidence

- `fff6d4b` adds web facets
- `790c34e` adds surfaces
- `f466038` adds typed APIs
- `7463db5` adds durable events
- `0edd691` adds the core tier
- `5323967` disables by default the built-ins that need resources
- `0104d7a` replaces repeated cards and time helpers with shared SDK exports
- `faed7909` refuses duplicate tool names from extensions in the same layer
- `27e615d0` and `70f56ce5` carry a tab's event subscriptions on one connection
