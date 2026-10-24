# Evolution

This file says where uao can change next, and the risk of each kind of change. [history.md](history.md) says how the code got here. Each count is for upstream at `4aaa074`.

## Change map

A change goes live in the instance that runs the changed checkout. Work in an isolate reaches the running host only when it lands. Before that, a preview shows it (`extensions/prompt/server.ts:358`).

Each row is one kind of change. The columns have these meanings:

- **Layer**: a number from [Layers](architecture.md#layers). "Beside" means next to the layers. "None" means outside them
- **Goes live**: short for the [layer table](../../AGENTS.md#layers-and-how-they-reload) and [Discovery and settings](../settings.md)
- **Checks**: "Base" is `pnpm check` and the tests that cover the change ([Conventions](../../AGENTS.md#conventions)). After a submission, the landing queue runs the checks of `.ultimate/settings.json`: `pnpm check`, then `pnpm test` and `pnpm test:e2e` in parallel. `pnpm check` covers only the repository (`extensions/README.md`)
- **Merge risk**: upstream commits that touch the path, from `git log --no-merges --oneline 4aaa074 -- '<path>' | wc -l`. Quote a path that contains `*`. High is 100 or more, medium is 20 to 99, and low is 1 to 19. "None" means outside the repository. Frequent upstream edits to a path increase the risk of merge conflicts when uao also edits it (inferred)

The runtime risk follows the layer, not the count. A broken web facet shows an error card. A core change goes live only after a checked swap. Only a human restart applies a change to the supervisor ([the layer table](../../AGENTS.md#layers-and-how-they-reload)).

| Change              | Place                             | Layer  | Goes live              | Checks                 | Merge risk      |
| ------------------- | --------------------------------- | ------ | ---------------------- | ---------------------- | --------------- |
| Web facet           | `extensions/<name>/web.tsx`       | 4 or 5 | Hot reload             | Base                   | High, 332       |
| Server facet        | `extensions/<name>/server.ts`     | 4 or 5 | Reinstall on save      | Base                   | High, 550       |
| Extension contract  | `extensions/<name>/api.ts`        | 4 or 5 | With its importers     | Base, `pnpm deps`      | Medium, 58      |
| New built-in        | A new folder in `extensions/`     | 5      | Like its facets        | Base                   | Low, note 1     |
| Project extension   | `.ultimate/extensions/<name>/`    | 6      | Note 2                 | Base                   | Low, 16         |
| Personal extension  | `~/.ultimate/extensions/<name>/`  | 6      | Like its facets        | None                   | None            |
| Helper              | `lib/`                            | Beside | With its importers     | Base                   | Medium, 57      |
| Web core            | `web/`                            | 3      | Hot reload             | Base                   | High, 177       |
| Core                | `server/`, `shared/`              | 2      | The `restart` tool     | Base                   | High, 126       |
| Supervisor          | `bin/`                            | None   | `pnpm start` only      | Base                   | Medium, 23      |
| Built-in definition | `agents/<name>.md`                | Beside | Note 3                 | Base                   | Medium, 86      |
| Project definition  | A new file in `.ultimate/agents/` | Beside | At its next start      | Base                   | Low, note 4     |
| Project setting     | `.ultimate/settings.json`         | Beside | Live                   | Base                   | Medium, 25      |
| Personal setting    | `~/.ultimate/settings.json`       | Beside | Live                   | None                   | None            |
| Project skill       | `.ultimate/skills/<name>/`        | Beside | Note 3                 | Base                   | Low, 2          |
| Pi patch            | `patches/`, `pnpm-workspace.yaml` | 1      | Note 5                 | Base, note 5           | Low, 18, note 5 |
| Rule                | `AGENTS.md`                       | None   | Note 3                 | Base                   | High, 125       |
| North-star          | `docs/north-star/`                | None   | When an agent reads it | Base, `check_links.py` | None, 0         |

Notes:

1. A new folder has no upstream history. Only a later upstream folder with the same name can conflict (inferred). A built-in that needs a resource ships off through `defaultOff` (`shared/extension-api.ts`, [D031](decisions/D031-resource-built-ins-off.md)). A user turns an extension on or off with the `enable` and `disable` lists of the settings ([Discovery and settings](../settings.md)). The guide requires a README (`extensions/README.md`). A web facet that imports a `.ts` file needs a line in `tsconfig.web.json`. That file has 42 commits, and 40 also change `extensions/` (the commands for merge risk and [co-change](#areas-that-change-together))
2. A project extension loads after the user trusts the project ([D009](decisions/D009-trust-before-project-setup.md)). Its code requires a coordinator branch ([D027](decisions/D027-project-code-through-branches.md)). Then it goes live like a built-in's facets (`extensions/README.md`)
3. A new conversation reads the new text. At its next input, @ultimate gets a note that names changed definition and instruction files (`extensions/prompt/server.ts:139`). Other agents keep their initial instructions (`extensions/prompt/server.ts:139`). But a standing agent reads its definition again before a message reaches it (`extensions/messages/delivery.ts:30`). The system prompt lists skills (`extensions/prompt/server.ts:335`). A `/skill:name` command expands one skill into the user input (`server/skills.ts:61`)
4. An overlay extends a built-in definition, not its copy ([Subagents](../subagents.md)). The **Agents tab** preserves that overlay ([B06](bricks/B06-project-specialization.md)). A new file has no upstream history. An edit to an upstream file in `.ultimate/agents/` meets 31 upstream commits (the command for merge risk)
5. A Pi patch goes live after `pnpm install` and a restart (inferred from `8b87d6f`). `test/e2e/pi-upstream.test.ts` checks the list in [Borrowed from Pi](../pi-upstream.md). Upstream upgraded Pi four times (`8d5dc26`, `e93d930`, `f7f0863`, `d7dd683`). Each upgrade renamed the Pi Durable patch file with the new version

## Stable parts and parts that change often

Most changes affect the conversation lifecycle, web app, and agent definitions. Core contracts and the supervisor are stable. `git log --no-merges --format=%ad --date=short 4aaa074 -- <path>` gives each count. "Last 3 days" counts 2026-10-22 to 2026-10-24.

| Path                            | Commits | Last 3 days | Reading                           |
| ------------------------------- | ------: | ----------: | --------------------------------- |
| `test/`                         |     871 |         166 | Changes with almost every feature |
| `extensions/conversations`      |     144 |          19 | Changes often                     |
| `extensions/subagents`          |     143 |          25 | Changes often                     |
| `extensions/lineage`            |     139 |          31 | Changes often, also recently      |
| `extensions/workspaces`         |     131 |          15 | Changes often                     |
| `web/src/app`                   |     140 |          29 | Changes often                     |
| `AGENTS.md`                     |     125 |           8 | Few recent changes                |
| `agents/`                       |      86 |          29 | Receives the behavior rules       |
| `lib/`                          |      57 |          31 | Many new helpers                  |
| `extensions/self`               |      39 |           5 | More recent changes               |
| `shared/protocol.ts`            |      35 |           1 | Stable                            |
| `bin/`                          |      23 |           3 | Stable                            |
| `shared/extension-api.ts`       |       5 |           1 | New since 2026-10-18              |
| `server/supervisor-protocol.ts` |       4 |           0 | Stable since 2026-10-12           |

A count covers 24 days. A low count can mean a new path rather than a stable one. For example, `extensions/side-chat` exists only since 2026-10-22 (`34c3633`). A rename starts a new count. Thus, `extensions/messages` has 21 commits (the command above). Before the rename, the Board extension's folder had 94 (`git log --no-merges --oneline 4aaa074 -- extensions/board | wc -l`, `28d657a`).

Ten extension folders left `extensions/` before the snapshot. The paths in `git log --format= --name-only 4aaa074 -- extensions` include ten folders absent from `git ls-tree -d 4aaa074:extensions`. Upstream deleted nine, including subscriptions (`e099781`), `canvas` (`deb65f8`), `sync` (`67caeb6`), and `faux` (`f23e291`). The tenth, the Board extension, became `extensions/messages` (`28d657a`). [history.md](history.md#eras) lists the main removals by era.

### Areas that change together

Some paths change together. `comm -12 <(git log --no-merges --format=%h 4aaa074 -- <a> | sort) <(git log --no-merges --format=%h 4aaa074 -- <b> | sort) | wc -l` counts commits that touch both paths:

- `web/src/app` and `web/src/sdk`: 81 commits. A change to the app often changes the SDK (inferred)
- `extensions/conversations` paired with `extensions/workspaces`, `extensions/lineage`, or `extensions/subagents`: 40 to 47 commits per pair. Branches, isolates, and conversations change as one lifecycle (inferred)
- `AGENTS.md` and `extensions/subagents`: 36 commits. A change to delegation changes the rules too (inferred)
- `server/extensions.ts` and `shared/protocol.ts`: 23 commits
- `package.json` and `pnpm-lock.yaml`: 23 commits

## Seams

A seam permits new behavior without edits to upstream files. Each seam below is an additive place in the [sync rule](upstream.md#sync-rule):

- **A new extension folder** in `.ultimate/extensions/<name>/` or `~/.ultimate/extensions/<name>/`. Discovery finds the extension. It is on by default (`extensions/README.md`). A folder named after a built-in replaces that whole built-in. Thus, the copy no longer follows upstream (inferred)
- **Extension APIs and points.** A new extension uses an upstream contract through `host.need` or `host.want`. Alternatively, it fills a core-tier point ([Extension APIs](../extensions.md#extension-apis), [Core tier](../extensions.md#core-tier))
- **Durable events.** A reactor reads the events of upstream extensions in order, across crashes ([Durable events](../extensions.md#durable-events))
- **Web contributions.** A web facet adds slots, panels, surfaces, renderers, and commands. It can also wrap the composer ([Contributions](../../extensions/README.md#contributions))
- **Hooks.** A server facet adds a hook such as `beforeInput` (`extensions/lineage/server.ts:1500`). The transactional form of `beforeInput` comes from a local Pi patch ([Borrowed from Pi](../pi-upstream.md))
- **Agent definitions.** A new definition, an overlay, or a new `reviewer-<name>.md` in `.ultimate/agents/` or `~/.ultimate/agents/` ([Subagents](../subagents.md))
- **Personal setup** in `~/.ultimate/`: `settings.json`, `skills/`, and `AGENTS.md` ([Discovery and settings](../settings.md))
- **Project automations** in `.ultimate/automations/<slug>/`. A script trigger loads stopped from its committed manifest (`e099781`, `extensions/automations/README.md`)

Two limits apply. Lander checks, the push target, and the preview model live in upstream file `.ultimate/settings.json`. The project setting wins over the user setting, so a change to them requires an edit of that file (inferred from `a4843af`, [D036](decisions/D036-previews-on-instance-model.md)). Personal places are outside the repository, so uao cannot keep them under version control (inferred).

## Areas in motion at the snapshot

These areas changed on 2026-10-23 and 2026-10-24, the last two days at the snapshot. Upstream made 150 work commits in those days (`git log --no-merges --format=%ad --date=short 4aaa074 | grep -c '2026-10-2[34]'`). Counts below use `git log --no-merges --format=%ad --date=short 4aaa074 -- <path> | grep -c '2026-10-2[34]'`:

- **Dreams and chapters**: `extensions/dream` 43 and `lib/chapters.ts` 6. Both are new on 2026-10-23 (`34c001a`, `4c94093`). Dreams follow @ultimate's compaction and can continue its work in a checked chapter ([B15](bricks/B15-dreams-and-chapters.md), `6c1c6bc`)
- **The conversation tree**: `extensions/lineage` 16. Self-compaction extends beyond @ultimate (`d3178ff`). For other top-level conversations, `compact` commits the compaction with its wake-up (`4a6aab5`, [B01](bricks/B01-durable-conversations.md))
- **Automations**: `extensions/automations` 16. Event filters follow standing-agent names across chapters (`6c1c6bc`, [B13](bricks/B13-background-work.md))
- **Shared helpers**: `lib/` 21. Six of these commits change `lib/chapters.ts` (see above). Others preserve overlays and deferred tools (`lib/agents.ts`, `d3c39fd`, `d3178ff`) or share relative-time formatting (`lib/ago.ts`, `0104d7a`)
- **Context use**: `extensions/conversations` 10. The server records the context use of each conversation (`ed0bb8a`, [B14](bricks/B14-everything-on-record.md))
- **The team**: `extensions/subagents` 12 and `agents/ultimate.md` 13. The **Agents tab** preserves overlays ([B06](bricks/B06-project-specialization.md), `ba7984e`). Coordinators receive deferred tools from overlays ([B09](bricks/B09-coordinators-and-subagents.md), `d3178ff`)
- **Messages and questions**: 18 commits touch `extensions/messages`, and 11 touch `extensions/questions`. Questions become structured message fields (`de87bde`, [B12](bricks/B12-human-in-the-loop.md))
- **Isolates and previews**: `extensions/workspaces` 7 and `extensions/instance` 7. Previews use `instance.model` (`a4843af`, [B10](bricks/B10-isolates-previews-lander.md))
- **The web UI and side chats**: `web/src` 17 and `extensions/side-chat` 6. Shared cards and relative-time helpers replace repeated code (`0104d7a`, [B03](bricks/B03-reloadable-extensions.md))
- **Skills and the Reloaded divider**: `extensions/prompt` 7. The prompt lists scoped skills (`f23fbeb`), and the Reloaded divider and the hot-reload toast name landed features (`b535e02`, [B02](bricks/B02-self-change-while-running.md))
- **Hands-off goals**: `extensions/goal` 5. The user can delegate approvals and receive a goal report (`001a193d`, [B12](bricks/B12-human-in-the-loop.md), [D037](decisions/D037-goals-delegate-approvals.md))
- **Pause and recovery**: `extensions/pause` 5 and `extensions/watchdog` 5. Play by itself and earlier idle notes reduce manual intervention (`d3178ff`, `a7495cb`, [B12](bricks/B12-human-in-the-loop.md), [B09](bricks/B09-coordinators-and-subagents.md)) (inferred)

A uao change in one of these areas meets the most upstream changes at the next merge (inferred).
