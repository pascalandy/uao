# B03 Reloadable extensions and surfaces

Status: shipped, at the snapshot. Source: upstream.

Each feature that is not core infrastructure is an extension folder, with a server facet for agent behavior and a web facet for UI (`README.md`). A user or a project adds, replaces, or disables a feature with no change to the core. A surface lets an extension be a full-screen app, with the agent one keystroke away.

Web facets can register code-block renderers by language (`61b25245`). Linked user and project extensions keep their current code and Tailwind styles after a link changes (`4ddbece8`, `027057d3`).

Changes to imported files also reload a linked server facet (`c0c1197c`). Stable `data-ui` attributes let extensions style the app shell (`eb77a9aa`, `28eb9e9c`). Error cards can send an error report to @ultimate (`cf2315bf`).

A web facet goes live through a rebuild of the production bundle, about two seconds after a save (`47c08a50`, `AGENTS.md`). The bundle has source maps, so error reports show resolved stacks (`c5e469ab`). More hooks let extensions theme the shell and the transcript (`6fd731a3`, `1be263cf`). Web facets can fill a `transcript.top` slot (`14953598`) and render inline code spans (`c8cb825d`).

Each extension keeps its tests in `extensions/<name>/test/`. That folder is not part of the extension, so a save there reloads nothing (`c387c88b`, `961fd373`). `disable` can turn off an outside extension that claims the core tier (`0b4c4a0e`).

## Where it lives

- `extensions/`: the built-ins, each with a README
- `shared/extension-api.ts`: API tokens, the core-tier reader, and `defaultOff`
- `server/discovery.ts` and `server/extensions.ts`: find and load server facets
- `server/web.ts`, `server/web-build.ts`, and `web/src/extensions.ts`: build and load web facets
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
- `6e9cd78d` removes the untyped service API and the supervisor's service report
- `506cfe15` keeps attention cards visible outside folded activity
- `7b6f7177` moves tablet panel controls into the Agent extension
- `47c08a50` replaces Vite hot reload in the browser with a rebuilt production bundle
- `c387c88b` moves each extension's tests into its own folder
- `a67802e1` and `9c1cbdda` share `useAction` reads and key them by conversation
