# B05 Agent tools

Status: shipped, at the snapshot. Source: upstream.

The agent has Pi's default coding tools: read, write, edit, and bash. Codemode lets it run one script that composes tools and reads Ultimate's state. A browser tool lets the agent view and control web pages, including Ultimate's own UI.

The browser can send input and wait for Ultimate's state through `window.ultimate` (`c2a86cad`, `555ed54e`). Driven pages use the same SDK reads and actions as the app (`web/src/sdk/test-hook.ts`). Each page has one agent bridge, where the controls of the UI kit list their names and states. A UI step of the browser tool operates a control by its name, not by a selector or a screenshot (`fa9a3b6e`, `0fd21054`). The browser tool detaches a page that it opens at the host's own origin, so that page saves no shared UI state (`extensions/browser/server.ts`). On other pages that an agent drives, a change that the UI change log records names the agent as its writer (`134703fb`, [B14](B14-everything-on-record.md)). A UI step on a control marked `data-agent-confirm` fails with "Needs a person" (`extensions/browser/README.md`).

Codemode runs on Pi Durable's code mode tool ([D005](../decisions/D005-codemode-sandbox.md)). Reads stay `ultimate.*` globals. The script-only tools `tools.action` and `tools.tell` call extension actions and other projects. A script can also call Pi's `models.*`, such as `models.classify` (`3603c530`, `extensions/codemode/README.md`).

MCP servers expose their tools through one `mcp` tool (`5eae312d`). Configuration merges user servers with trusted project servers (`extensions/mcp/server.ts`). Transport failures reconnect without resending the failed call (`16a71d81`). Interrupted calls do not replay (`extensions/mcp/README.md`). Configured secret placeholders appear in the Secrets panel (`90fa141d`). [MCP mechanics](../../../extensions/mcp/README.md) lists the transports and limits, including no OAuth or legacy SSE support.

Upstream removed Sketch, because no conversation used it outside its previews (`e6909945`). That commit also removes the `subagent: false` definition field.

The browser tool runs Chromium with its sandbox on by default (`dbe9bb50`). It kills a browser that drops its connection and prefers Playwright's Chromium (`3fb5c2fc`). An automated browser never moves the user's tabs (`0040f365`). Codemode search filters by kind and returns compact hits by default (`1cc67661`). Codemode reads closed chapters through a read-only harness (`0d1e509f`).

`bash` with `background: true` starts a command, such as a dev server, in its own process group. It records the group and returns the command that stops it (`5abd5a39`, `extensions/coding-tools/README.md`). Agents had stopped dev servers by name or port, and one such kill stopped the Ultimate core (`5abd5a39`). When a conversation concludes, a durable effect stops the groups that it started before the conclusion (`115c86e9`, `a9c6efb6`). The Git attribution hooks of `bash` apply only to their first worktree (`fe47d47f`). `ultimate.entries` in codemode returns a compact view, and `full: true` returns the stored records (`c9c1bb26`).

The browser tool waits for a render before a screenshot (`b9cc436c`). A short `timeoutMs` no longer fails the launch (`d029734b`). A failed call names its error before the console errors (`1974900a`). A selector without a scope fails when it matches more than one element (`aa4f4917`, `bdbdac57`). The user can add a secret under a name of their choice from the Secrets panel (`29f05387`). A notice about a missing secret goes away when the user saves the secret (`a1abfdb3`). The browser tool takes a viewport width and height (`64dc9d81`), and it names each match of an ambiguous selector (`29432615`). MCP refuses a call without its required arguments and shows the input schema. It sends a rate-limited call once more after 5 s (`0986250e`, `680befed`). Agent shells start without the host's `NODE_ENV` (`cfc41b52`).

When the service runs with a delegated cgroup, `bash`, previews, lander checks, and automation scripts run in their own cgroups under `work/`. `work.memoryMax` caps all of `work/` together, 70% of RAM by default. When that work uses too much memory, the kernel stops the work, not the core (`f00dd1b6`, [Discovery and settings](../../../docs/settings.md)). `video_ask` lets an agent ask Gemini about a video that the user attached ([B12](B12-human-in-the-loop.md), `604927c2`).

## Where it lives

- `extensions/coding-tools/`: read, write, edit, and bash
- `extensions/codemode/`: the script sandbox
- `extensions/browser/`: screenshots and page control
- `extensions/parallel/`: web search and fetch
- `extensions/secrets/`: user-global secrets
- `web/src/sdk/test-hook.ts`: state-based waits for driven pages
- `extensions/mcp/`: MCP connections, secret declarations, and the single tool
- `extensions/video/`: video uploads and `video_ask`

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
- `5abd5a39` adds background process groups to `bash`, and `115c86e9` stops them after a conclusion
- `fe47d47f` limits the Git attribution hooks to their first worktree
- `0fd21054` adds UI steps that operate controls by name
- `3603c530` moves codemode onto Pi Durable's code mode tool
- `f00dd1b6` puts branch work in capped cgroups
