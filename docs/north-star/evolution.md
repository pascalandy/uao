# Evolution

This file says where uao can change next, and the risk of each kind of change. [history.md](history.md) says how the code got here. Each count is for upstream at `11c89136`.

## Change map

A change goes live in the instance that runs its checkout (`extensions/prompt/server.ts`). Work in an isolate reaches the host when it lands ([D042](decisions/D042-model-free-landing.md)). A preview shows the isolate first (`extensions/instance/README.md`).

Each row is one kind of change. The columns have these meanings:

- **Layer**: a number from [Layers](architecture.md#layers). "Beside" means next to the layers. "None" means outside them
- **Goes live**: short for the [layer table](../../AGENTS.md#layers-and-how-they-reload) and [Discovery and settings](../settings.md)
- **Checks**: "Base" is `pnpm check` and the tests that cover the change ([Conventions](../../AGENTS.md#conventions)). After a submission, the landing queue runs the checks of `.ultimate/settings.json`: `pnpm check`, then `pnpm test` and `pnpm test:e2e` in parallel. Each command has a configured timeout of 120 or 180 seconds (`.ultimate/settings.json`). `pnpm check` covers only the repository (`extensions/README.md`)
- **Merge risk**: upstream commits that touch the path, from `git log --no-merges --oneline 11c89136 -- '<path>' | wc -l`. Quote a path that contains `*`. High is 100 or more, medium is 20 to 99, and low is 1 to 19. "None" means outside the repository. Frequent upstream edits to a path increase the risk of merge conflicts when uao also edits it (inferred)

For a facet count, use `extensions/*/web.tsx`, `extensions/*/server.ts`, or `extensions/*/api.ts` as the quoted path. For a row with two paths, pass both paths to one `git log`, so a commit counts once.

The runtime risk follows the layer, not the count. A broken web facet shows an error card. A core change goes live only after a checked swap. Only a human restart applies a change to the supervisor ([the layer table](../../AGENTS.md#layers-and-how-they-reload)).

| Change              | Place                             | Layer  | Goes live              | Checks                 | Merge risk         |
| ------------------- | --------------------------------- | ------ | ---------------------- | ---------------------- | ------------------ |
| Web facet           | `extensions/<name>/web.tsx`       | 4 or 5 | Rebuild, page switches | Base                   | High, 473          |
| Server facet        | `extensions/<name>/server.ts`     | 4 or 5 | Reinstall on save      | Base                   | High, 737          |
| Extension contract  | `extensions/<name>/api.ts`        | 4 or 5 | With its importers     | Base, `pnpm deps`      | Medium, 84         |
| New built-in        | A new folder in `extensions/`     | 5      | Like its facets        | Base                   | Low, note 1        |
| Project extension   | `.ultimate/extensions/<name>/`    | 6      | Note 2                 | Base                   | Low, 16            |
| Personal extension  | `~/.ultimate/extensions/<name>/`  | 6      | Like its facets        | None                   | None               |
| Helper              | `lib/`                            | Beside | With its importers     | Base                   | High, 103          |
| Web core            | `web/`                            | 3      | Rebuild, page switches | Base                   | High, 280          |
| Core                | `server/`, `shared/`              | 2      | The `restart` tool     | Base                   | High, 185          |
| Supervisor          | `bin/`                            | None   | `pnpm start` only      | Base                   | Medium, 26         |
| Built-in definition | `agents/<name>.md`                | Beside | Note 3                 | Base                   | High, 125          |
| Project definition  | A new file in `.ultimate/agents/` | Beside | At its next start      | Base                   | Low, note 4        |
| Project setting     | `.ultimate/settings.json`         | Beside | Live                   | Base                   | Medium, 28         |
| Personal setting    | `~/.ultimate/settings.json`       | Beside | Live                   | None                   | None               |
| Project skill       | `.ultimate/skills/<name>/`        | Beside | Note 3                 | Base                   | Low, 19            |
| Pi patch            | `patches/`, `pnpm-workspace.yaml` | 1      | Note 5                 | Base, note 5           | Medium, 41, note 5 |
| Rule                | `AGENTS.md`                       | None   | Note 3                 | Base                   | High, 144          |
| North-star          | `docs/north-star/`                | None   | When an agent reads it | Base, `check_links.py` | None, 0            |

Notes:

1. A new folder has no upstream history. Only a later upstream folder with the same name can conflict (inferred). A built-in that needs a resource ships off through `defaultOff` (`shared/extension-api.ts`, [D031](decisions/D031-resource-built-ins-off.md)). A user turns an extension on or off with the `enable` and `disable` lists of the settings ([Discovery and settings](../settings.md)). The guide requires a README (`extensions/README.md`). A web facet that imports a `.ts` file needs a line in `tsconfig.web.json`. That file has 59 commits, and 55 also change `extensions/` (the commands for merge risk and [co-change](#areas-that-change-together))
2. A project extension loads after the user trusts the project ([D009](decisions/D009-trust-before-project-setup.md)). Its code requires a coordinator branch ([D027](decisions/D027-project-code-through-branches.md)). Then it goes live like a built-in's facets (`extensions/README.md`)
3. A new conversation reads the new text. At its next input, @ultimate gets a note that names changed definition and instruction files (`extensions/prompt/server.ts`). Other agents keep their initial instructions (`extensions/prompt/server.ts`). But a standing agent reads its definition again before a message reaches it (`extensions/messages/delivery.ts`). The system prompt lists skills (`extensions/prompt/server.ts`). A `/skill:name` command expands one skill into the user input (`server/skills.ts`)
4. An overlay extends a built-in definition, not its copy ([Subagents](../subagents.md)). The **Agents tab** preserves that overlay ([B06](bricks/B06-project-specialization.md)). A new file has no upstream history. An edit to an upstream file in `.ultimate/agents/` meets 39 upstream commits (the command for merge risk)
5. A Pi patch goes live after `pnpm install` and a restart (inferred from `8b87d6f`). After a landing, loads wait for that install (`1441b930`). `scripts/pi-upstream.ts` checks the list in [Borrowed from Pi](../pi-upstream.md) as part of `pnpm check` (`770b0243`). Upstream upgraded Pi five times (`8d5dc26`, `e93d930`, `f7f0863`, `d7dd683`, `669df90a`). Each upgrade renamed the Pi Durable patch file with the new version

## Stable parts and parts that change often

The conversation lifecycle and web app have many historical edits. Recent work changes messages, models, the sidebar, and process-group safety (inferred from the table below and [Areas in motion at the snapshot](#areas-in-motion-at-the-snapshot)). Since `c387c88b`, each extension's tests live in its own folder, so the count of an extension folder includes its tests from that commit on. `git log --no-merges --format=%ad --date=short 11c89136 -- <path>` gives each count. "Last 3 days" counts 2026-11-08 to 2026-11-10. Filter that output with `rg -c '2026-11-(08|09|10)'` for the recent count.

| Path                            | Commits | Last 3 days | Reading                                     |
| ------------------------------- | ------: | ----------: | ------------------------------------------- |
| `test/`                         |   1,195 |          35 | Changes with most features                  |
| `extensions/conversations`      |     161 |           2 | Changes often                               |
| `extensions/subagents`          |     184 |           8 | Changes often                               |
| `extensions/lineage`            |     180 |           6 | Changes often                               |
| `extensions/workspaces`         |     174 |           9 | Changes often                               |
| `web/src/app`                   |     215 |           7 | Changes often                               |
| `AGENTS.md`                     |     144 |           3 | Few recent changes                          |
| `agents/`                       |     125 |           2 | Receives the behavior rules                 |
| `lib/`                          |     103 |          11 | Spawn helper, default model, process groups |
| `extensions/self`               |      47 |           2 | Few recent changes                          |
| `shared/protocol.ts`            |      41 |           1 | Few recent changes                          |
| `bin/`                          |      26 |           0 | No changes in the last three days           |
| `shared/extension-api.ts`       |      12 |           3 | Default-off list grew to ten                |
| `server/supervisor-protocol.ts` |       6 |           0 | No changes since the Tailscale URL change   |

A count covers 41 days. A low count can mean a new path rather than a stable one. For example, `extensions/side-chat` exists only since 2026-10-22 (`34c3633`). A rename starts a new count. Thus, `extensions/messages` has 97 commits (the command above). Before the rename, the Board extension's folder had 94 (`git log --no-merges --oneline 11c89136 -- extensions/board | wc -l`, `28d657a`).

Thirteen extension folders left `extensions/` before the snapshot. Twelve were deleted, including the minimap, feature threads, and Sketch (`6dfcf451`, `fe08571f`, `e6909945`). The Board folder became `extensions/messages` (`28d657a`). This command counts folders that appear in history but are absent at the snapshot:

```sh
comm -23 \
	<(git log --format= --name-only 11c89136 -- extensions | awk -F/ 'NF > 2 { print $2 }' | sort -u) \
	<(git ls-tree -d --name-only 11c89136:extensions | sort) | wc -l
```

Output: `13`. One folder is new in this sync: `inbox` (`995c52d4`). The November 9 sync added `attachments`, `push`, `share`, and `wire` (`80016496`, `ff44988c`, `9b8f1866`). [history.md](history.md#eras) lists the main removals by era.

### Areas that change together

Some paths change together. `comm -12 <(git log --no-merges --format=%h 11c89136 -- <a> | sort) <(git log --no-merges --format=%h 11c89136 -- <b> | sort) | wc -l` counts commits that touch both paths:

- `web/src/app` and `web/src/sdk`: 111 commits. A change to the app often changes the SDK (inferred)
- `extensions/conversations` paired with `extensions/workspaces`, `extensions/lineage`, or `extensions/subagents`: 50, 50, and 48 commits, respectively. Branches, isolates, and conversations change as one lifecycle (inferred)
- `AGENTS.md` and `extensions/subagents`: 37 commits. A change to delegation changes the rules too (inferred)
- `server/extensions.ts` and `shared/protocol.ts`: 26 commits
- `package.json` and `pnpm-lock.yaml`: 30 commits

## Seams

A seam permits new behavior without edits to upstream files. Each seam below is an additive place in the [sync rule](upstream.md#sync-rule):

- **A new extension folder** in `.ultimate/extensions/<name>/` or `~/.ultimate/extensions/<name>/`. Discovery finds the extension. It is on by default (`extensions/README.md`). A folder named after a built-in replaces that whole built-in. Thus, the copy no longer follows upstream (inferred)
- **Extension APIs and points.** A new extension uses an upstream contract through `host.need` or `host.want`. Alternatively, it fills a core-tier point ([Contracts](../extensions/contracts.md), [Core tier](../extensions/core-tier.md))
- **Durable events.** A reactor reads the events of upstream extensions in order, across crashes ([Durable events](../extensions/events.md#durable-events))
- **Web contributions.** A web facet adds slots, panels, surfaces, renderers, and commands. It can also wrap the composer, put a badge on a panel tab, and draw a part of the UI of another extension again (`a99235ce`, `8d09848d`, [Slots and panels](../extensions/slots.md), [Renderers](../extensions/renderers.md))
- **Hooks.** A server facet adds a hook such as `beforeInput` (`extensions/lineage/server.ts`). The transactional form of `beforeInput` comes from a local Pi patch ([Borrowed from Pi](../pi-upstream.md))
- **Agent definitions.** A new definition, an overlay, or a new `reviewer-<name>.md` in `.ultimate/agents/` or `~/.ultimate/agents/` ([Subagents](../subagents.md))
- **MCP servers.** `mcpServers` in user or trusted project settings adds external tools through one tool ([MCP](../../extensions/mcp/README.md))
- **Personal setup** in `~/.ultimate/`: `settings.json`, `skills/`, and `AGENTS.md` ([Discovery and settings](../settings.md))
- **Project automations** in `.ultimate/automations/<slug>/`. A script trigger loads stopped from its committed manifest (`e099781`, `extensions/automations/README.md`)

Two limits apply. Lander checks, the push target, and the preview family assignment live in upstream file `.ultimate/settings.json`. The project setting wins over the user setting. A change to those project choices requires an edit of that file (inferred from `d6f3657a`, [D036](decisions/D036-previews-on-instance-model.md)). Personal places are outside the repository, so uao cannot keep them under version control (inferred).

## Areas in motion at the snapshot

These areas changed on 2026-11-09 and 2026-11-10, the last two days at the snapshot. Upstream made 68 work commits in those days (`git log --no-merges --format=%ad --date=short 11c89136 | rg -c '2026-11-(09|10)'`). Each row uses the same command with `-- <path>`.

| Area        | Path                        | Commits | Change and evidence                                                                                      |
| ----------- | --------------------------- | ------: | -------------------------------------------------------------------------------------------------------- |
| Docs        | `docs/`                     |      21 | Pi couplings, Wire, Claude Code discovery, and the test layout (`770b0243`, `a5dea087`, `c387c88b`)      |
| Families    | `extensions/models`, `lib/` |      11 | One default for model and thinking, the family label, and Get ready (`ba854f0e`, `f81d842b`, `fa9670c8`) |
| Messages    | `extensions/messages`       |      10 | Open questions rank first, and a pointer to a hidden question (`8bce83ea`, `cbac5781`, `cfccc89c`)       |
| Web UI      | `web/src`                   |      10 | Shared reads, panel badges, and `Rendered` (`a67802e1`, `a99235ce`, `8d09848d`)                          |
| Onboarding  | `extensions/onboarding`     |       9 | Get ready sets the default family, and a failed start starts again (`fa9670c8`, `b59483eb`, `1789ce2a`)  |
| Wire        | `extensions/wire`           |       8 | Raw model calls, cache diffs, and the System tab (`9b8f1866`, `5f3b8ef2`, `5c5dea51`)                    |
| Pi patches  | `patches/`                  |       8 | Prompt sections, Claude Code refusals, and group kills (`a5dea087`, `a14a0ccc`, `bf6830af`)              |
| Updates     | `extensions/update`         |       6 | Loads wait for installs, and failed installs offer Retry (`1441b930`, `acc2f9ab`)                        |
| Sidebar     | `extensions/sidebar`        |       6 | Open questions outrank work, and the Inbox row (`59136892`, `8bce83ea`, `995c52d4`)                      |
| Core server | `server/`                   |       6 | Load waits, extension test folders, and dangling links (`1441b930`, `961fd373`, `96de0d29`)              |
| Claude Code | `extensions/claude-code`    |       5 | Model catalog discovery, and its own refusal of a turn (`983ad978`, `a14a0ccc`)                          |

The test move touches most extension folders on 2026-11-10 (`c387c88b`). This table counts author dates, including contributions merged later.

A uao edit in a frequently changed area has more opportunities to conflict at the next merge (inferred from the counts).
