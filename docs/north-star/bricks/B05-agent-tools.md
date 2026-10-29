# B05 Agent tools

Status: shipped, at the snapshot. Source: upstream.

The agent has Pi's default coding tools: read, write, edit, and bash. Codemode lets it run one script that composes tools and reads Ultimate's state. A browser tool lets the agent view and control web pages, including Ultimate's own UI.

The browser can send input and wait for Ultimate's state through `window.ultimate` (`c2a86cad`, `555ed54e`). Driven pages use the same SDK reads and actions as the app (`web/src/sdk/test-hook.ts`).

## Where it lives

- `extensions/coding-tools/`: read, write, edit, and bash
- `extensions/codemode/`: the script sandbox
- `extensions/browser/`: screenshots and page control
- `extensions/parallel/`: web search and fetch
- `extensions/secrets/`: user-global secrets
- `web/src/sdk/test-hook.ts`: state-based waits for driven pages

## Decisions

- [D005](../decisions/D005-codemode-sandbox.md) Compose tools in a codemode sandbox

## Evidence

- `fbfe98ce` streams write and edit calls while their arguments arrive
- `8eebfa32` shrinks images to the selected model's limits when the agent reads them
- `692ca8f` adds the local coding tools
- `1a0453c` adds codemode
- `930605c` adds the browser and test instances
- `ef3591a` adds the commit trailer
- `56c1a31` adds secrets and web tools
