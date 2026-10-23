# Contract

This file lists what a user, a project, and an extension can rely on, at the snapshot. Each guarantee links to the file that holds its mechanics. Upstream gives no promise of stability, so a merge of upstream can change any line here ([D016](decisions/D016-personal-project.md)).

## A user can rely on these guarantees

- A conversation, its tool calls, and its documents survive a restart and a crash ([Durability](../durability.md))
- An interrupted tool runs again only when it is replay-safe. Any other interrupted tool reports "interrupted" to the model ([Durability](../durability.md))
- A change to the code does not end the conversation. Only a change to `bin/` needs a human restart ([the layer table](../../AGENTS.md#layers-and-how-they-reload))
- A failed core swap keeps the old generation ([Running the server](../running.md))
- Ultimate listens only on `127.0.0.1`. The `tailscale` extension, which ships off, admits only allowed logins and never turns on Funnel (`docs/running.md`, `extensions/tailscale/README.md`)
- A project's code does not run until the user trusts that project ([Discovery and settings](../settings.md))
- Logins stay on each machine and are never copied (`README.md`)
- Secrets are plaintext in `~/.ultimate/secrets.json`, with restrictive permissions. This file is not a vault (`extensions/secrets/README.md`)

## A project can rely on these guarantees

- Discovery reads the clone, then `~/.ultimate/`, then the project. A later name wins ([Discovery and settings](../settings.md))
- A project's settings override the user's settings ([Discovery and settings](../settings.md))
- `.ultimate/settings.json` sets the isolate setup, the lander checks, and the push target (`.ultimate/settings.json`)
- Isolates need a Git branch and a first commit. Until then, conversations share the folder (`b40b9c2`)
- Ultimate does not type-check a project's extensions (`skills/integrate-ultimate/SKILL.md`)
- Project subscriptions load stopped (`8cc313c`)

## An extension can rely on these guarantees

- A folder holds `server.ts`, `web.tsx`, or both, and a `README.md`. The folder name is the extension name ([An extension's files](../../extensions/README.md#an-extensions-files))
- A broken web facet shows an error card and keeps its previous version. The rest of the UI keeps running ([An extension's files](../../extensions/README.md#an-extensions-files))
- A saved server facet reinstalls, and a running tool call finishes on the old code ([the layer table](../../AGENTS.md#layers-and-how-they-reload))
- A durable event commits with the change that caused it. A reactor writes exactly once ([Durable events](../extensions.md#durable-events))
- A service handle finds the current provider at each call, so a reload of the provider does not break it ([Extension APIs](../extensions.md#extension-apis))

## An extension must keep these rules

- Reach another extension only through its `api.ts`, its `ui.tsx`, a point, or an event ([Conventions](../../extensions/README.md#conventions))
- In the core tier, depend only on the core tier ([Core tier](../extensions.md#core-tier))
- Treat the arguments of an action as untrusted input ([Actions](../../extensions/README.md#actions))
- Keep prompt sections stable. Put a value that changes in a note from a `beforeInput` hook ([Conventions](../../extensions/README.md#conventions))
- Give each `replay: 'safe'` a reason comment, and tolerate a second run of each effect outside the transaction ([Durability](../durability.md))
- Pass `pnpm check`. It checks the format, the lint rules, the types, and the dependency graph (`AGENTS.md`)
