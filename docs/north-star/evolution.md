# Evolution

This file says where uao can change next, and the risk of each kind of change. [history.md](history.md) says how the code got here. Each count is for upstream at `e8abe7f1`.

## Change map

A change goes live in the instance that runs its checkout (`extensions/prompt/server.ts`). Work in an isolate reaches the host when it lands ([D042](decisions/D042-model-free-landing.md)). A preview shows the isolate first (`extensions/instance/README.md`).

Each row is one kind of change. The columns have these meanings:

- **Layer**: a number from [Layers](architecture.md#layers). "Beside" means next to the layers. "None" means outside them
- **Goes live**: short for the [layer table](../../AGENTS.md#layers-and-how-they-reload) and [Discovery and settings](../settings.md)
- **Checks**: "Base" is `pnpm check` and the tests that cover the change ([Conventions](../../AGENTS.md#conventions)). After a submission, the landing queue runs the checks of `.ultimate/settings.json`: `pnpm check`, then `pnpm test:affected`, with timeouts of 120 and 600 seconds (`.ultimate/settings.json`, [B10](bricks/B10-isolates-previews-lander.md)). `pnpm check` covers only the repository (`extensions/README.md`)
- **Merge risk**: upstream commits that touch the path, from `git log --no-merges --oneline e8abe7f1 -- '<path>' | wc -l`. Quote a path that contains `*`. High is 100 or more, medium is 20 to 99, and low is 1 to 19. "None" means outside the repository. Frequent upstream edits to a path increase the risk of merge conflicts when uao also edits it (inferred)

For a facet count, use `extensions/*/server.ts` or `extensions/*/api.ts` as the quoted path. For web facets, pass both `extensions/*/web.tsx` and `extensions/*/web.solid.tsx`, because the move to Solid renamed each file ([D046](decisions/D046-solid-interface.md)). For a row with two paths, pass both paths to one `git log`, so a commit counts once.

The runtime risk follows the layer, not the count. A broken web facet shows an error card. A core change goes live only after a checked swap. Only a human restart applies a change to the supervisor ([the layer table](../../AGENTS.md#layers-and-how-they-reload)).

| Change              | Place                             | Layer  | Goes live              | Checks                 | Merge risk         |
| ------------------- | --------------------------------- | ------ | ---------------------- | ---------------------- | ------------------ |
| Web facet           | `extensions/<name>/web.solid.tsx` | 4 or 5 | Rebuild, page switches | Base                   | High, 672          |
| Server facet        | `extensions/<name>/server.ts`     | 4 or 5 | Reinstall on save      | Base                   | High, 1,059        |
| Extension contract  | `extensions/<name>/api.ts`        | 4 or 5 | With its importers     | Base, `pnpm deps`      | High, 124          |
| New built-in        | A new folder in `extensions/`     | 5      | Like its facets        | Base                   | Low, note 1        |
| Project extension   | `.ultimate/extensions/<name>/`    | 6      | Note 2                 | Base                   | Medium, 40         |
| Personal extension  | `~/.ultimate/extensions/<name>/`  | 6      | Like its facets        | None                   | None               |
| Helper              | `lib/`                            | Beside | With its importers     | Base                   | High, 176          |
| Web core            | `web/`                            | 3      | Rebuild, page switches | Base                   | High, 586          |
| Core                | `server/`, `shared/`              | 2      | The `restart` tool     | Base                   | High, 256          |
| Supervisor          | `bin/`                            | None   | `pnpm start` only      | Base                   | Medium, 36         |
| Built-in definition | `agents/<name>.md`                | Beside | Note 3                 | Base                   | High, 159          |
| Project definition  | A new file in `.ultimate/agents/` | Beside | At its next start      | Base                   | Low, note 4        |
| Project setting     | `.ultimate/settings.json`         | Beside | Live, `port` at start  | Base                   | Medium, 35         |
| Personal setting    | `~/.ultimate/settings.json`       | Beside | Live                   | None                   | None               |
| Project skill       | `.ultimate/skills/<name>/`        | Beside | Note 3                 | Base                   | Medium, 56         |
| Pi patch            | `patches/`, `pnpm-workspace.yaml` | 1      | Note 5                 | Base, note 5           | Medium, 60, note 5 |
| Rule                | `AGENTS.md`                       | None   | Note 3                 | Base                   | High, 153          |
| North-star          | `docs/north-star/`                | None   | When an agent reads it | Base, `check_links.py` | None, 0            |

Notes:

1. A new folder has no upstream history. Only a later upstream folder with the same name can conflict (inferred). A built-in that needs a resource ships off through `defaultOff` (`shared/extension-api.ts`, [D031](decisions/D031-resource-built-ins-off.md)). A user turns an extension on or off with the `enable` and `disable` lists of the settings ([Discovery and settings](../settings.md)). The guide requires a README (`extensions/README.md`). A web facet that imports a `.ts` file needs a line in `tsconfig.web.json`. That file has 118 commits, and 109 also change `extensions/` (the commands for merge risk and [co-change](#areas-that-change-together))
2. A project extension loads after the user trusts the project ([D009](decisions/D009-trust-before-project-setup.md)). Its code requires a coordinator branch ([D027](decisions/D027-project-code-through-branches.md)). Then it goes live like a built-in's facets (`extensions/README.md`)
3. A new conversation reads the new text. At its next input, @ultimate gets a note that names changed definition and instruction files (`extensions/prompt/server.ts`). Other agents keep their initial instructions (`extensions/prompt/server.ts`). But a standing agent reads its definition again before a message reaches it (`extensions/messages/delivery.ts`). The system prompt lists skills (`extensions/prompt/server.ts`). A `/skill:name` command expands one skill into the user input (`server/skills.ts`)
4. An overlay extends a built-in definition, not its copy ([Subagents](../subagents.md)). The **Agents tab** preserves that overlay ([B06](bricks/B06-project-specialization.md)). A new file has no upstream history. An edit to an upstream file in `.ultimate/agents/` meets 47 upstream commits (the command for merge risk)
5. A Pi patch goes live after `pnpm install` and a restart (inferred from `8b87d6f`). After a landing, loads wait for that install (`1441b930`). `scripts/pi-upstream.ts` checks the list in [Borrowed from Pi](../pi-upstream.md) as part of `pnpm check` (`770b0243`). Upstream upgraded Pi seven times (`8d5dc26`, `e93d930`, `f7f0863`, `d7dd683`, `669df90a`, `3f11fcc2`, `2f6ef78f`). Each upgrade renamed the Pi Durable patch file with the new version

## Stable parts and parts that change often

The conversation lifecycle and the web app have many historical edits. Recent work changes the interface, voice mode, codemode, and messages (inferred from the table below and [Areas in motion at the snapshot](#areas-in-motion-at-the-snapshot)). Since `c387c88b`, each extension's tests live in its own folder, so the count of an extension folder includes its tests from that commit on. `git log --no-merges --format=%ad --date=short e8abe7f1 -- <path>` gives each count. "Last 3 days" counts 2026-11-22 to 2026-11-24. Filter that output with `rg -c '2026-11-2[234]'` for the recent count.

| Path                            | Commits | Last 3 days | Reading                                    |
| ------------------------------- | ------: | ----------: | ------------------------------------------ |
| `test/`                         |   1,468 |          56 | Changes with most features                 |
| `web/src/sdk`                   |     367 |          45 | The Solid SDK and the stream of reads      |
| `web/src/app`                   |     323 |          27 | The Solid shell and the prompt box         |
| `extensions/subagents`          |     254 |          21 | Changes often                              |
| `extensions/workspaces`         |     251 |          10 | Changes often                              |
| `extensions/lineage`            |     238 |          11 | Changes often                              |
| `extensions/conversations`      |     237 |          25 | Changes often                              |
| `extensions/messages`           |     212 |          32 | The report judge and owned requests        |
| `extensions/automations`        |     184 |          28 | Watchers, subscribers, and sleeping tasks  |
| `lib/`                          |     176 |          17 | Formatters, secrets, and agent discovery   |
| `agents/`                       |     159 |          10 | Video, the judge, and direct questions     |
| `AGENTS.md`                     |     153 |           2 | Affected tests and pointers to the starter |
| `extensions/voice-live`         |     144 |          80 | Voice mode, rebuilt in this sync           |
| `extensions/self`               |      65 |           2 | Few recent changes                         |
| `shared/protocol.ts`            |      58 |           5 | Few recent changes                         |
| `bin/`                          |      36 |           1 | Few recent changes                         |
| `shared/extension-api.ts`       |      16 |           2 | The default-off list stays at ten          |
| `server/supervisor-protocol.ts` |       8 |           0 | No recent changes                          |

A count covers 56 days. A low count can mean a new path rather than a stable one. For example, `extensions/side-chat` exists only since 2026-10-22 (`34c3633`). A rename starts a new count. Thus, `extensions/messages` has 212 commits (the command above). Before the rename, the Board extension's folder had 94 (`git log --no-merges --oneline e8abe7f1 -- extensions/board | wc -l`, `28d657a`).

Fourteen extension folders left `extensions/` before the snapshot. Thirteen were deleted, including the minimap, feature threads, Sketch, and the redraws extension (`6dfcf451`, `fe08571f`, `e6909945`, `b4de946d`). The Board folder became `extensions/messages` (`28d657a`). This command counts folders that appear in history but are absent at the snapshot:

```sh
comm -23 \
	<(git log --format= --name-only e8abe7f1 -- extensions | awk -F/ 'NF > 2 { print $2 }' | sort -u) \
	<(git ls-tree -d --name-only e8abe7f1:extensions | sort) | wc -l
```

Output: `14`. The redraws extension came and went in this sync, on 2026-11-22 (`d4a349a9`, `b4de946d`). Five folders are new in this sync: `antigravity`, `reel`, `screen-recorder`, `ui`, and `video` (`76280bf9`, `3abdf324`, `9538d3e2`, `bd5246de`, `604927c2`). The November 18 sync added `diagrams`, `entries`, `projects`, and `read-aloud` (`c23dd36a`, `4601a36c`, `f5e963f1`, `e78fefa8`). The November 11 sync added `inbox` (`995c52d4`). The November 9 sync added `attachments`, `push`, `share`, and `wire` (`80016496`, `ff44988c`, `9b8f1866`). [history.md](history.md#eras) lists the main removals by era.

### Areas that change together

Some paths change together. `comm -12 <(git log --no-merges --format=%h e8abe7f1 -- <a> | sort) <(git log --no-merges --format=%h e8abe7f1 -- <b> | sort) | wc -l` counts commits that touch both paths:

- `web/src/app` and `web/src/sdk`: 174 commits. A change to the app often changes the SDK (inferred)
- `extensions/conversations` paired with `extensions/workspaces`, `extensions/lineage`, or `extensions/subagents`: 78, 73, and 72 commits, respectively. Branches, isolates, and conversations change as one lifecycle (inferred)
- `AGENTS.md` and `extensions/subagents`: 38 commits. A change to delegation changes the rules too (inferred)
- `server/extensions.ts` and `shared/protocol.ts`: 29 commits
- `package.json` and `pnpm-lock.yaml`: 47 commits

## Seams

A seam permits new behavior without edits to upstream files. Each seam below is an additive place in the [sync rule](upstream.md#sync-rule):

- **A new extension folder** in `.ultimate/extensions/<name>/` or `~/.ultimate/extensions/<name>/`. Discovery finds the extension. It is on by default (`extensions/README.md`). A folder named after a built-in replaces that whole built-in. Thus, the copy no longer follows upstream (inferred)
- **Extension APIs and points.** A new extension uses an upstream contract through `host.need` or `host.want`. Alternatively, it fills a core-tier point ([Contracts](../extensions/contracts.md), [Core tier](../extensions/core-tier.md))
- **Durable events.** A reactor reads the events of upstream extensions in order, across crashes ([Durable events](../extensions/events.md#durable-events))
- **Web contributions.** A web facet adds slots, panels, surfaces, renderers, and commands. It can also wrap the composer, put a badge on a panel tab, and draw a part of the UI of another extension again (`a99235ce`, `8d09848d`, [Contracts](../extensions/contracts.md), [Slots and panels](../extensions/slots.md), [Renderers](../extensions/renderers.md))
- **Hooks.** A server facet adds a hook such as `beforeInput` (`extensions/lineage/server.ts`). The transactional form of `beforeInput` comes from a local Pi patch ([Borrowed from Pi](../pi-upstream.md))
- **Agent definitions.** A new definition, an overlay, or a new `reviewer-<name>.md` in `.ultimate/agents/` or `~/.ultimate/agents/` ([Subagents](../subagents.md))
- **MCP servers.** `mcpServers` in user or trusted project settings adds external tools through one tool ([MCP](../../extensions/mcp/README.md))
- **Personal setup** in `~/.ultimate/`: `settings.json`, `skills/`, and `AGENTS.md` ([Discovery and settings](../settings.md))
- **Project automations** in `.ultimate/automations/<slug>/`. A script trigger loads stopped from its committed manifest (`e099781`, `extensions/automations/README.md`)

Two limits apply. Lander checks, the push target, and the preview family assignment live in upstream file `.ultimate/settings.json`. The project setting wins over the user setting. A change to those project choices requires an edit of that file (inferred from `d6f3657a`, [D036](decisions/D036-previews-on-instance-model.md)). Personal places are outside the repository, so uao cannot keep them under version control (inferred).

## Areas in motion at the snapshot

These areas changed on 2026-11-23 and 2026-11-24, the last two full days of work at the snapshot. Upstream made 193 work commits in those days (`git log --no-merges --format=%ad --date=short e8abe7f1 | rg -c '2026-11-2[34]'`). Each row uses the same command with `-- <path>`.

| Area        | Path                    | Commits | Change and evidence                                                                                                |
| ----------- | ----------------------- | ------: | ------------------------------------------------------------------------------------------------------------------ |
| Voice mode  | `extensions/voice-live` |      78 | Collected recordings, tap to talk, and handoffs to the branch on screen (`1e6c09e5`, `dbaaeb25`, `11e815c9`)       |
| Web core    | `web/`                  |      46 | The prompt box apart from the composer, videos, and the screen recorder (`72db8020`, `a2ecf28c`, `9538d3e2`)       |
| Codemode    | `extensions/codemode`   |      22 | Pi Durable's code mode tool and script-only tools (`3603c530`, `077b6715`)                                         |
| Docs        | `docs/`                 |      21 | The prompt box, the screen recorder, and the adversarial reviewer (`72db8020`, `9538d3e2`, `2fcc3bfe`)             |
| Messages    | `extensions/messages`   |      20 | The report judge, and pointers to the standing agent that started a branch (`161901f2`, `f18cdde5`, `52054fd9`)    |
| Classify    | `extensions/classify`   |      14 | The provider of the report judge (`161901f2`, `454096bf`)                                                          |
| Core server | `server/`               |      10 | Ordered read answers and limits on the event stream (`724dd76a`, `4a577a71`)                                       |
| Helpers     | `lib/`                  |       9 | Provider keys for secrets and the name of a macOS machine (`c8f84f4e`, `d9ff45c8`)                                 |
| Subagents   | `extensions/subagents`  |       9 | A standing agent's tools come from its definition before each fresh run (`d4a973b4`, `4a8c35ab`)                   |
| Definitions | `agents/`               |       8 | `video_ask`, the adversarial reviewer, and direct questions from coordinators (`107f68a8`, `2fcc3bfe`, `a7719a89`) |

The move to Solid touches most folders from 2026-11-19 to 2026-11-22, before these two days ([D046](decisions/D046-solid-interface.md)). This table counts author dates, including contributions merged later.

A uao edit in a frequently changed area has more opportunities to conflict at the next merge (inferred from the counts).
