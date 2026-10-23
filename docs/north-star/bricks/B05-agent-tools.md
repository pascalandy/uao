# B05 Agent tools

Status: shipped, at the snapshot. Source: upstream.

The agent has Pi's default coding tools: read, write, edit, and bash. Codemode lets it run one script that composes tools and reads Ultimate's state. A browser tool lets it see and drive web pages, its own UI included.

## How it works

`coding-tools` installs the four tools with their transcript renderers. Each commit that bash makes gets an `Ultimate-Conversation` trailer, so a commit names its conversation. `codemode` runs a script in a QuickJS sandbox with `ultimate.*` helpers. `browser` opens a fresh Chromium page for each call. `parallel` adds web search and fetch, and `secrets` keeps keys out of prompts and results. Each extension README holds its mechanics, for example [codemode](../../../extensions/codemode/README.md).

## Where it lives

- `extensions/coding-tools/`: read, write, edit, and bash
- `extensions/codemode/`: the script sandbox
- `extensions/browser/`: screenshots and page control
- `extensions/parallel/`: web search and fetch
- `extensions/secrets/`: user-global secrets

## Decisions

- [D005](../decisions/D005-codemode-sandbox.md) Compose tools in a codemode sandbox

## Next

- Nothing stated

## Evidence

- `692ca8f` adds the local coding tools
- `1a0453c` adds codemode
- `930605c` adds the browser and test instances
- `ef3591a` adds the commit trailer
- `56c1a31` adds secrets and web tools
