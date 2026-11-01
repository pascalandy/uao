# Evolution

This file says where uao can change next, and the risk of each kind of change. [history.md](history.md) says how the code got here. Each count is for upstream at `d0a2e17b`.

## Change map

A change goes live in the instance that runs its checkout (`extensions/prompt/server.ts`). Work in an isolate reaches the host when it lands ([D042](decisions/D042-model-free-landing.md)). A preview shows the isolate first (`extensions/instance/README.md`).

Each row is one kind of change. The columns have these meanings:

- **Layer**: a number from [Layers](architecture.md#layers). "Beside" means next to the layers. "None" means outside them
- **Goes live**: short for the [layer table](../../AGENTS.md#layers-and-how-they-reload) and [Discovery and settings](../settings.md)
- **Checks**: "Base" is `pnpm check` and the tests that cover the change ([Conventions](../../AGENTS.md#conventions)). After a submission, the landing queue runs the checks of `.ultimate/settings.json`: `pnpm check`, then `pnpm test` and `pnpm test:e2e` in parallel. Each command has a configured timeout of 120 or 180 seconds (`.ultimate/settings.json`). `pnpm check` covers only the repository (`extensions/README.md`)
- **Merge risk**: upstream commits that touch the path, from `git log --no-merges --oneline d0a2e17b -- '<path>' | wc -l`. Quote a path that contains `*`. High is 100 or more, medium is 20 to 99, and low is 1 to 19. "None" means outside the repository. Frequent upstream edits to a path increase the risk of merge conflicts when uao also edits it (inferred)

For a facet count, use `extensions/*/web.tsx`, `extensions/*/server.ts`, or `extensions/*/api.ts` as the quoted path. For a row with two paths, pass both paths to one `git log`, so a commit counts once.

The runtime risk follows the layer, not the count. A broken web facet shows an error card. A core change goes live only after a checked swap. Only a human restart applies a change to the supervisor ([the layer table](../../AGENTS.md#layers-and-how-they-reload)).

| Change              | Place                             | Layer  | Goes live              | Checks                 | Merge risk         |
| ------------------- | --------------------------------- | ------ | ---------------------- | ---------------------- | ------------------ |
| Web facet           | `extensions/<name>/web.tsx`       | 4 or 5 | Hot reload             | Base                   | High, 433          |
| Server facet        | `extensions/<name>/server.ts`     | 4 or 5 | Reinstall on save      | Base                   | High, 672          |
| Extension contract  | `extensions/<name>/api.ts`        | 4 or 5 | With its importers     | Base, `pnpm deps`      | Medium, 79         |
| New built-in        | A new folder in `extensions/`     | 5      | Like its facets        | Base                   | Low, note 1        |
| Project extension   | `.ultimate/extensions/<name>/`    | 6      | Note 2                 | Base                   | Low, 16            |
| Personal extension  | `~/.ultimate/extensions/<name>/`  | 6      | Like its facets        | None                   | None               |
| Helper              | `lib/`                            | Beside | With its importers     | Base                   | Medium, 77         |
| Web core            | `web/`                            | 3      | Hot reload             | Base                   | High, 242          |
| Core                | `server/`, `shared/`              | 2      | The `restart` tool     | Base                   | High, 157          |
| Supervisor          | `bin/`                            | None   | `pnpm start` only      | Base                   | Medium, 26         |
| Built-in definition | `agents/<name>.md`                | Beside | Note 3                 | Base                   | High, 117          |
| Project definition  | A new file in `.ultimate/agents/` | Beside | At its next start      | Base                   | Low, note 4        |
| Project setting     | `.ultimate/settings.json`         | Beside | Live                   | Base                   | Medium, 28         |
| Personal setting    | `~/.ultimate/settings.json`       | Beside | Live                   | None                   | None               |
| Project skill       | `.ultimate/skills/<name>/`        | Beside | Note 3                 | Base                   | Low, 11            |
| Pi patch            | `patches/`, `pnpm-workspace.yaml` | 1      | Note 5                 | Base, note 5           | Medium, 26, note 5 |
| Rule                | `AGENTS.md`                       | None   | Note 3                 | Base                   | High, 138          |
| North-star          | `docs/north-star/`                | None   | When an agent reads it | Base, `check_links.py` | None, 0            |

Notes:

1. A new folder has no upstream history. Only a later upstream folder with the same name can conflict (inferred). A built-in that needs a resource ships off through `defaultOff` (`shared/extension-api.ts`, [D031](decisions/D031-resource-built-ins-off.md)). A user turns an extension on or off with the `enable` and `disable` lists of the settings ([Discovery and settings](../settings.md)). The guide requires a README (`extensions/README.md`). A web facet that imports a `.ts` file needs a line in `tsconfig.web.json`. That file has 53 commits, and 51 also change `extensions/` (the commands for merge risk and [co-change](#areas-that-change-together))
2. A project extension loads after the user trusts the project ([D009](decisions/D009-trust-before-project-setup.md)). Its code requires a coordinator branch ([D027](decisions/D027-project-code-through-branches.md)). Then it goes live like a built-in's facets (`extensions/README.md`)
3. A new conversation reads the new text. At its next input, @ultimate gets a note that names changed definition and instruction files (`extensions/prompt/server.ts`). Other agents keep their initial instructions (`extensions/prompt/server.ts`). But a standing agent reads its definition again before a message reaches it (`extensions/messages/delivery.ts`). The system prompt lists skills (`extensions/prompt/server.ts`). A `/skill:name` command expands one skill into the user input (`server/skills.ts`)
4. An overlay extends a built-in definition, not its copy ([Subagents](../subagents.md)). The **Agents tab** preserves that overlay ([B06](bricks/B06-project-specialization.md)). A new file has no upstream history. An edit to an upstream file in `.ultimate/agents/` meets 37 upstream commits (the command for merge risk)
5. A Pi patch goes live after `pnpm install` and a restart (inferred from `8b87d6f`). `test/e2e/pi-upstream.test.ts` checks the list in [Borrowed from Pi](../pi-upstream.md). Upstream upgraded Pi four times (`8d5dc26`, `e93d930`, `f7f0863`, `d7dd683`). Each upgrade renamed the Pi Durable patch file with the new version

## Stable parts and parts that change often

The conversation lifecycle and web app have many historical edits. Recent work also changes messages, project memory, and agent rules (inferred from the table below). `git log --no-merges --format=%ad --date=short d0a2e17b -- <path>` gives each count. "Last 3 days" counts 2026-10-30 to 2026-11-01. Filter that output with `rg -c '2026-(10-(30|31)|11-01)'` for the recent count.

| Path                            | Commits | Last 3 days | Reading                           |
| ------------------------------- | ------: | ----------: | --------------------------------- |
| `test/`                         |   1,085 |          52 | Changes with most features        |
| `extensions/conversations`      |     150 |           3 | Changes often                     |
| `extensions/subagents`          |     165 |           6 | Changes often                     |
| `extensions/lineage`            |     168 |           9 | Changes often                     |
| `extensions/workspaces`         |     152 |           5 | Changes often                     |
| `web/src/app`                   |     191 |          23 | Changes often                     |
| `AGENTS.md`                     |     138 |           1 | Few recent changes                |
| `agents/`                       |     117 |           9 | Receives the behavior rules       |
| `lib/`                          |      77 |           4 | Few recent changes                |
| `extensions/self`               |      40 |           0 | No changes in the last three days |
| `shared/protocol.ts`            |      37 |           0 | No recent changes                 |
| `bin/`                          |      26 |           2 | Few historical changes            |
| `shared/extension-api.ts`       |       9 |           2 | Default-off list changed twice    |
| `server/supervisor-protocol.ts` |       6 |           2 | Tailscale URL and service removal |

A count covers 32 days. A low count can mean a new path rather than a stable one. For example, `extensions/side-chat` exists only since 2026-10-22 (`34c3633`). A rename starts a new count. Thus, `extensions/messages` has 68 commits (the command above). Before the rename, the Board extension's folder had 94 (`git log --no-merges --oneline d0a2e17b -- extensions/board | wc -l`, `28d657a`).

Twelve extension folders left `extensions/` before the snapshot. Eleven were deleted, including the minimap and feature threads (`6dfcf451`, `fe08571f`). The Board folder became `extensions/messages` (`28d657a`). This command counts folders that appear in history but are absent at the snapshot:

```sh
comm -23 \
	<(git log --format= --name-only d0a2e17b -- extensions | awk -F/ 'NF > 2 { print $2 }' | sort -u) \
	<(git ls-tree -d --name-only d0a2e17b:extensions | sort) | wc -l
```

Output: `12`. [history.md](history.md#eras) lists the main removals by era.

### Areas that change together

Some paths change together. `comm -12 <(git log --no-merges --format=%h d0a2e17b -- <a> | sort) <(git log --no-merges --format=%h d0a2e17b -- <b> | sort) | wc -l` counts commits that touch both paths:

- `web/src/app` and `web/src/sdk`: 103 commits. A change to the app often changes the SDK (inferred)
- `extensions/conversations` paired with `extensions/workspaces`, `extensions/lineage`, or `extensions/subagents`: 47, 46, and 43 commits, respectively. Branches, isolates, and conversations change as one lifecycle (inferred)
- `AGENTS.md` and `extensions/subagents`: 36 commits. A change to delegation changes the rules too (inferred)
- `server/extensions.ts` and `shared/protocol.ts`: 24 commits
- `package.json` and `pnpm-lock.yaml`: 25 commits

## Seams

A seam permits new behavior without edits to upstream files. Each seam below is an additive place in the [sync rule](upstream.md#sync-rule):

- **A new extension folder** in `.ultimate/extensions/<name>/` or `~/.ultimate/extensions/<name>/`. Discovery finds the extension. It is on by default (`extensions/README.md`). A folder named after a built-in replaces that whole built-in. Thus, the copy no longer follows upstream (inferred)
- **Extension APIs and points.** A new extension uses an upstream contract through `host.need` or `host.want`. Alternatively, it fills a core-tier point ([Extension APIs](../extensions.md#extension-apis), [Core tier](../extensions.md#core-tier))
- **Durable events.** A reactor reads the events of upstream extensions in order, across crashes ([Durable events](../extensions.md#durable-events))
- **Web contributions.** A web facet adds slots, panels, surfaces, renderers, and commands. It can also wrap the composer ([Contributions](../../extensions/README.md#contributions))
- **Hooks.** A server facet adds a hook such as `beforeInput` (`extensions/lineage/server.ts`). The transactional form of `beforeInput` comes from a local Pi patch ([Borrowed from Pi](../pi-upstream.md))
- **Agent definitions.** A new definition, an overlay, or a new `reviewer-<name>.md` in `.ultimate/agents/` or `~/.ultimate/agents/` ([Subagents](../subagents.md))
- **MCP servers.** `mcpServers` in user or trusted project settings adds external tools through one tool ([MCP](../../extensions/mcp/README.md))
- **Personal setup** in `~/.ultimate/`: `settings.json`, `skills/`, and `AGENTS.md` ([Discovery and settings](../settings.md))
- **Project automations** in `.ultimate/automations/<slug>/`. A script trigger loads stopped from its committed manifest (`e099781`, `extensions/automations/README.md`)

Two limits apply. Lander checks, the push target, and the preview family assignment live in upstream file `.ultimate/settings.json`. The project setting wins over the user setting. A change to those project choices requires an edit of that file (inferred from `d6f3657a`, [D036](decisions/D036-previews-on-instance-model.md)). Personal places are outside the repository, so uao cannot keep them under version control (inferred).

## Areas in motion at the snapshot

These areas changed on 2026-10-31 and 2026-11-01, the last two days at the snapshot. Upstream made 47 work commits in those days (`git log --no-merges --format=%ad --date=short d0a2e17b | rg -c '2026-(10-31|11-01)'`). Each row uses the same command with `-- <path>`.

| Area           | Path                    | Commits | Change and evidence                                                                  |
| -------------- | ----------------------- | ------: | ------------------------------------------------------------------------------------ |
| Web UI         | `web/src`               |      13 | Transcript cleanup, theme hooks, and file drops (`49456b0c`, `eb77a9aa`, `3fa3753c`) |
| Messages       | `extensions/messages`   |      12 | Routed branch answers and open-question settlement (`aaa55768`, `7b09649d`)          |
| Sketch         | `extensions/sketch`     |       8 | UI descriptions, forms, and its own model definition (`a7ab9797`, `b2f7043f`)        |
| MCP            | `extensions/mcp`        |       4 | Connections, recovery, and declared secrets (`5eae312d`, `16a71d81`, `90fa141d`)     |
| Project memory | `extensions/lineage`    |       4 | Derived facts and shared memory limits (`08d193b3`, `aa2f79da`)                      |
| Agents         | `extensions/subagents`  |       4 | Derived models, Sketch definition, and agent marks (`08d193b3`, `17157665`)          |
| Core server    | `server/`               |       3 | Typed APIs, lock identity, and dynamic secrets (`6e9cd78d`, `91f1fde4`, `90fa141d`)  |
| Landing        | `extensions/workspaces` |       2 | Lander guard removed, check-label style (`1a0541ee`, `cff3032a`)                     |
| Plan           | `extensions/plan`       |       2 | Epics without tasks and section labels (`34624b5d`, `160b6362`)                      |
| Updates        | `extensions/update`     |       2 | Owed restart for core changes and section labels (`fe5907cd`, `160b6362`)            |
| Sounds         | `extensions/sounds`     |       1 | Optional narrator (`451ac392`)                                                       |

The family introduction and branch question cards have earlier author dates in this sync ([history.md](history.md#era-9-ordinary-work)). This table counts author dates, including contributions merged later.

A uao edit in a frequently changed area has more opportunities to conflict at the next merge (inferred from the counts).
