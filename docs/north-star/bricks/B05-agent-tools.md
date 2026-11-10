# B05 Agent tools

Status: shipped, at the snapshot. Source: upstream.

The agent has Pi's default coding tools: read, write, edit, and bash. Codemode lets it run one script that composes tools and reads Ultimate's state. A browser tool lets the agent view and control web pages, including Ultimate's own UI.

The browser can send input and wait for Ultimate's state through `window.ultimate` (`c2a86cad`, `555ed54e`). Driven pages use the same SDK reads and actions as the app (`web/src/sdk/test-hook.ts`).

MCP servers expose their tools through one `mcp` tool (`5eae312d`). Configuration merges user servers with trusted project servers (`extensions/mcp/server.ts`). Transport failures reconnect without resending the failed call (`16a71d81`). Interrupted calls do not replay (`extensions/mcp/README.md`). Configured secret placeholders appear in the Secrets panel (`90fa141d`). [MCP mechanics](../../../extensions/mcp/README.md) lists the transports and limits, including no OAuth or legacy SSE support.

Upstream removed Sketch, because no conversation used it outside its previews (`e6909945`). That commit also removes the `subagent: false` definition field.

The browser tool runs Chromium with its sandbox on by default (`dbe9bb50`). It kills a browser that drops its connection and prefers Playwright's Chromium (`3fb5c2fc`). An automated browser never moves the user's tabs (`0040f365`). Codemode search filters by kind and returns compact hits by default (`1cc67661`). Codemode reads closed chapters through a read-only harness (`0d1e509f`).

## Where it lives

- `extensions/coding-tools/`: read, write, edit, and bash
- `extensions/codemode/`: the script sandbox
- `extensions/browser/`: screenshots and page control
- `extensions/parallel/`: web search and fetch
- `extensions/secrets/`: user-global secrets
- `web/src/sdk/test-hook.ts`: state-based waits for driven pages
- `extensions/mcp/`: MCP connections, secret declarations, and the single tool

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
- `b2b46f1c` finds Playwright's Chromium in the macOS cache
- `cf4b7b1b` keeps browser waits active through a page reload
- `df00cf20` preserves existing commit attribution when a commit is rewritten
- `e6909945` removes Sketch
- `4b314408` starts child processes from a small helper process, so a launch does not stall the host
- `6cc90767` limits `images: "latest"` to the current turn
