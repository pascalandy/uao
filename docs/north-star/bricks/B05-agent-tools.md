# B05 Agent tools

Status: shipped, at the snapshot. Source: upstream.

The agent has Pi's default coding tools: read, write, edit, and bash. Codemode lets it run one script that composes tools and reads Ultimate's state. A browser tool lets the agent view and control web pages, including Ultimate's own UI.

The browser can send input and wait for Ultimate's state through `window.ultimate` (`c2a86cad`, `555ed54e`). Driven pages use the same SDK reads and actions as the app (`web/src/sdk/test-hook.ts`).

MCP servers expose their tools through one `mcp` tool (`5eae312d`). Configuration merges user servers with trusted project servers (`extensions/mcp/server.ts`). Transport failures reconnect without resending the failed call (`16a71d81`). Interrupted calls do not replay (`extensions/mcp/README.md`). Configured secret placeholders appear in the Secrets panel (`90fa141d`). [MCP mechanics](../../../extensions/mcp/README.md) lists the transports and limits, including no OAuth or legacy SSE support.

Sketch asks a model to draw a small UI from a description and optional data (`a7ab9797`). Its own agent definition uses the `tiny` family by default (`b2f7043f`). Sketch can read inside the conversation's working directory when no data is supplied (`78373e7b`). Forms use a durable claim to prevent duplicate submission (`78373e7b`). After an interrupted delivery, the user can send the form again (`e82e9553`). [Sketch mechanics](../../../extensions/sketch/README.md) owns the block types and model-call limits.

## Where it lives

- `extensions/coding-tools/`: read, write, edit, and bash
- `extensions/codemode/`: the script sandbox
- `extensions/browser/`: screenshots and page control
- `extensions/parallel/`: web search and fetch
- `extensions/secrets/`: user-global secrets
- `web/src/sdk/test-hook.ts`: state-based waits for driven pages
- `extensions/mcp/`: MCP connections, secret declarations, and the single tool
- `extensions/sketch/`: model-generated UI and user-only form submission

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
