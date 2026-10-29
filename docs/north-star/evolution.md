# Evolution

This file says where uao can change next, and the risk of each kind of change. [history.md](history.md) says how the code got here. Each count is for upstream at `17d186b`.

## Change map

A change goes live in the instance that runs its checkout (`extensions/prompt/server.ts`). Work in an isolate reaches the host when it lands ([D042](decisions/D042-model-free-landing.md)). A preview shows the isolate first (`extensions/instance/README.md`).

Each row is one kind of change. The columns have these meanings:

- **Layer**: a number from [Layers](architecture.md#layers). "Beside" means next to the layers. "None" means outside them
- **Goes live**: short for the [layer table](../../AGENTS.md#layers-and-how-they-reload) and [Discovery and settings](../settings.md)
- **Checks**: "Base" is `pnpm check` and the tests that cover the change ([Conventions](../../AGENTS.md#conventions)). After a submission, the landing queue runs the checks of `.ultimate/settings.json`: `pnpm check`, then `pnpm test` and `pnpm test:e2e` in parallel. Each command has a configured timeout of 120 or 180 seconds (`.ultimate/settings.json`). `pnpm check` covers only the repository (`extensions/README.md`)
- **Merge risk**: upstream commits that touch the path, from `git log --no-merges --oneline 17d186b -- '<path>' | wc -l`. Quote a path that contains `*`. High is 100 or more, medium is 20 to 99, and low is 1 to 19. "None" means outside the repository. Frequent upstream edits to a path increase the risk of merge conflicts when uao also edits it (inferred)

For a facet count, use `extensions/*/web.tsx`, `extensions/*/server.ts`, or `extensions/*/api.ts` as the quoted path. For a row with two paths, pass both paths to one `git log`, so a commit counts once.

The runtime risk follows the layer, not the count. A broken web facet shows an error card. A core change goes live only after a checked swap. Only a human restart applies a change to the supervisor ([the layer table](../../AGENTS.md#layers-and-how-they-reload)).

| Change              | Place                             | Layer  | Goes live              | Checks                 | Merge risk         |
| ------------------- | --------------------------------- | ------ | ---------------------- | ---------------------- | ------------------ |
| Web facet           | `extensions/<name>/web.tsx`       | 4 or 5 | Hot reload             | Base                   | High, 406          |
| Server facet        | `extensions/<name>/server.ts`     | 4 or 5 | Reinstall on save      | Base                   | High, 637          |
| Extension contract  | `extensions/<name>/api.ts`        | 4 or 5 | With its importers     | Base, `pnpm deps`      | Medium, 74         |
| New built-in        | A new folder in `extensions/`     | 5      | Like its facets        | Base                   | Low, note 1        |
| Project extension   | `.ultimate/extensions/<name>/`    | 6      | Note 2                 | Base                   | Low, 16            |
| Personal extension  | `~/.ultimate/extensions/<name>/`  | 6      | Like its facets        | None                   | None               |
| Helper              | `lib/`                            | Beside | With its importers     | Base                   | Medium, 67         |
| Web core            | `web/`                            | 3      | Hot reload             | Base                   | High, 213          |
| Core                | `server/`, `shared/`              | 2      | The `restart` tool     | Base                   | High, 145          |
| Supervisor          | `bin/`                            | None   | `pnpm start` only      | Base                   | Medium, 24         |
| Built-in definition | `agents/<name>.md`                | Beside | Note 3                 | Base                   | High, 106          |
| Project definition  | A new file in `.ultimate/agents/` | Beside | At its next start      | Base                   | Low, note 4        |
| Project setting     | `.ultimate/settings.json`         | Beside | Live                   | Base                   | Medium, 26         |
| Personal setting    | `~/.ultimate/settings.json`       | Beside | Live                   | None                   | None               |
| Project skill       | `.ultimate/skills/<name>/`        | Beside | Note 3                 | Base                   | Low, 7             |
| Pi patch            | `patches/`, `pnpm-workspace.yaml` | 1      | Note 5                 | Base, note 5           | Medium, 26, note 5 |
| Rule                | `AGENTS.md`                       | None   | Note 3                 | Base                   | High, 137          |
| North-star          | `docs/north-star/`                | None   | When an agent reads it | Base, `check_links.py` | None, 0            |

Notes:

1. A new folder has no upstream history. Only a later upstream folder with the same name can conflict (inferred). A built-in that needs a resource ships off through `defaultOff` (`shared/extension-api.ts`, [D031](decisions/D031-resource-built-ins-off.md)). A user turns an extension on or off with the `enable` and `disable` lists of the settings ([Discovery and settings](../settings.md)). The guide requires a README (`extensions/README.md`). A web facet that imports a `.ts` file needs a line in `tsconfig.web.json`. That file has 50 commits, and 48 also change `extensions/` (the commands for merge risk and [co-change](#areas-that-change-together))
2. A project extension loads after the user trusts the project ([D009](decisions/D009-trust-before-project-setup.md)). Its code requires a coordinator branch ([D027](decisions/D027-project-code-through-branches.md)). Then it goes live like a built-in's facets (`extensions/README.md`)
3. A new conversation reads the new text. At its next input, @ultimate gets a note that names changed definition and instruction files (`extensions/prompt/server.ts`). Other agents keep their initial instructions (`extensions/prompt/server.ts`). But a standing agent reads its definition again before a message reaches it (`extensions/messages/delivery.ts`). The system prompt lists skills (`extensions/prompt/server.ts`). A `/skill:name` command expands one skill into the user input (`server/skills.ts`)
4. An overlay extends a built-in definition, not its copy ([Subagents](../subagents.md)). The **Agents tab** preserves that overlay ([B06](bricks/B06-project-specialization.md)). A new file has no upstream history. An edit to an upstream file in `.ultimate/agents/` meets 35 upstream commits (the command for merge risk)
5. A Pi patch goes live after `pnpm install` and a restart (inferred from `8b87d6f`). `test/e2e/pi-upstream.test.ts` checks the list in [Borrowed from Pi](../pi-upstream.md). Upstream upgraded Pi four times (`8d5dc26`, `e93d930`, `f7f0863`, `d7dd683`). Each upgrade renamed the Pi Durable patch file with the new version

## Stable parts and parts that change often

The conversation lifecycle and web app have many historical edits. Recent work also changes the landing path and agent rules (inferred from the table below). `git log --no-merges --format=%ad --date=short 17d186b -- <path>` gives each count. "Last 3 days" counts 2026-10-27 to 2026-10-29.

| Path                            | Commits | Last 3 days | Reading                           |
| ------------------------------- | ------: | ----------: | --------------------------------- |
| `test/`                         |   1,016 |          59 | Changes with almost every feature |
| `extensions/conversations`      |     146 |           2 | Changes often                     |
| `extensions/subagents`          |     153 |           4 | Changes often                     |
| `extensions/lineage`            |     157 |           7 | Changes often                     |
| `extensions/workspaces`         |     146 |          10 | Changes often                     |
| `web/src/app`                   |     166 |           8 | Changes often                     |
| `AGENTS.md`                     |     137 |           7 | Few recent changes                |
| `agents/`                       |     106 |           7 | Receives the behavior rules       |
| `lib/`                          |      67 |           2 | Few recent changes                |
| `extensions/self`               |      40 |           0 | No changes in the last three days |
| `shared/protocol.ts`            |      37 |           2 | Stable                            |
| `bin/`                          |      24 |           1 | Stable                            |
| `shared/extension-api.ts`       |       7 |           0 | New since 2026-10-18              |
| `server/supervisor-protocol.ts` |       4 |           0 | Stable since 2026-10-12           |

A count covers 29 days. A low count can mean a new path rather than a stable one. For example, `extensions/side-chat` exists only since 2026-10-22 (`34c3633`). A rename starts a new count. Thus, `extensions/messages` has 50 commits (the command above). Before the rename, the Board extension's folder had 94 (`git log --no-merges --oneline 17d186b -- extensions/board | wc -l`, `28d657a`).

Eleven extension folders left `extensions/` before the snapshot. Ten were deleted, including the minimap (`6dfcf451`). The Board folder became `extensions/messages` (`28d657a`). This command counts folders that appear in history but are absent at the snapshot:

```sh
comm -23 \
	<(git log --format= --name-only 17d186b -- extensions | awk -F/ 'NF > 2 { print $2 }' | sort -u) \
	<(git ls-tree -d --name-only 17d186b:extensions | sort) | wc -l
```

Output: `11`. [history.md](history.md#eras) lists the main removals by era.

### Areas that change together

Some paths change together. `comm -12 <(git log --no-merges --format=%h 17d186b -- <a> | sort) <(git log --no-merges --format=%h 17d186b -- <b> | sort) | wc -l` counts commits that touch both paths:

- `web/src/app` and `web/src/sdk`: 92 commits. A change to the app often changes the SDK (inferred)
- `extensions/conversations` paired with `extensions/workspaces`, `extensions/lineage`, or `extensions/subagents`: 40 to 47 commits per pair. Branches, isolates, and conversations change as one lifecycle (inferred)
- `AGENTS.md` and `extensions/subagents`: 36 commits. A change to delegation changes the rules too (inferred)
- `server/extensions.ts` and `shared/protocol.ts`: 24 commits
- `package.json` and `pnpm-lock.yaml`: 24 commits

## Seams

A seam permits new behavior without edits to upstream files. Each seam below is an additive place in the [sync rule](upstream.md#sync-rule):

- **A new extension folder** in `.ultimate/extensions/<name>/` or `~/.ultimate/extensions/<name>/`. Discovery finds the extension. It is on by default (`extensions/README.md`). A folder named after a built-in replaces that whole built-in. Thus, the copy no longer follows upstream (inferred)
- **Extension APIs and points.** A new extension uses an upstream contract through `host.need` or `host.want`. Alternatively, it fills a core-tier point ([Extension APIs](../extensions.md#extension-apis), [Core tier](../extensions.md#core-tier))
- **Durable events.** A reactor reads the events of upstream extensions in order, across crashes ([Durable events](../extensions.md#durable-events))
- **Web contributions.** A web facet adds slots, panels, surfaces, renderers, and commands. It can also wrap the composer ([Contributions](../../extensions/README.md#contributions))
- **Hooks.** A server facet adds a hook such as `beforeInput` (`extensions/lineage/server.ts`). The transactional form of `beforeInput` comes from a local Pi patch ([Borrowed from Pi](../pi-upstream.md))
- **Agent definitions.** A new definition, an overlay, or a new `reviewer-<name>.md` in `.ultimate/agents/` or `~/.ultimate/agents/` ([Subagents](../subagents.md))
- **Personal setup** in `~/.ultimate/`: `settings.json`, `skills/`, and `AGENTS.md` ([Discovery and settings](../settings.md))
- **Project automations** in `.ultimate/automations/<slug>/`. A script trigger loads stopped from its committed manifest (`e099781`, `extensions/automations/README.md`)

Two limits apply. Lander checks, the push target, and the preview model live in upstream file `.ultimate/settings.json`. The project setting wins over the user setting, so a change to them requires an edit of that file (inferred from `a4843af`, [D036](decisions/D036-previews-on-instance-model.md)). Personal places are outside the repository, so uao cannot keep them under version control (inferred).

## Areas in motion at the snapshot

These areas changed on 2026-10-28 and 2026-10-29, the last two days at the snapshot. Upstream made 50 work commits in those days (`git log --no-merges --format=%ad --date=short 17d186b | rg -c '2026-10-(28|29)'`). Each row uses the same command with `-- <path>`.

| Area                | Path                     | Commits | Change and evidence                                                           |
| ------------------- | ------------------------ | ------: | ----------------------------------------------------------------------------- |
| Sounds              | `extensions/sounds`      |      12 | Agent music and landing notifications (`76ea0ae7`, `09befdd5`)                |
| Messages            | `extensions/messages`    |      10 | Landing wake ownership and correct question replies (`b7060d00`, `91618d16`)  |
| Landing             | `extensions/workspaces`  |       7 | Model-free landing, conclusion, and checkout release (`cfd0e93b`, `903ce43e`) |
| Project memory      | `extensions/lineage`     |       6 | Separate History and Memory views (`6ee7d47c`, `21669aa1`)                    |
| Web UI              | `web/src`                |       5 | Folded transcript stretches and one event stream (`ebb71f13`, `27e615d0`)     |
| Automations         | `extensions/automations` |       4 | Per-call receipts and delivery failures (`6d96d892`, `903ce43e`)              |
| Core server         | `server/`                |       4 | Tailscale URL logs and shared stream subscriptions (`7849a479`, `70f56ce5`)   |
| Pause               | `extensions/pause`       |       2 | Final retry failures and held-parent notices (`9e3164f5`, `29480df2`)         |
| Supervisor commands | `bin/`                   |       1 | Emergency terminal agent removed (`17d186bf`)                                 |

Voice, remotes, and the dream rewrite belong to earlier days in this sync ([history.md](history.md#era-9-ordinary-work)). Their absence from this table means no edits in the last two days.

A uao edit in a frequently changed area has more opportunities to conflict at the next merge (inferred from the counts).
