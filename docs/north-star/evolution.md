# Evolution

This file says where uao can change next, and the risk of each kind of change. [history.md](history.md) says how the code got here. Each count is for upstream at `33c05e9`.

## Change map

Each row is one kind of change. The columns use these meanings:

- **Layer**: a number from [Layers](architecture.md#layers). "Beside" is next to the layers, and "None" is outside them
- **Goes live**: a short form of the [layer table](../../AGENTS.md#layers-and-how-they-reload) and of [Discovery and settings](../settings.md)
- **Checks**: "Base" is `pnpm check` and the tests that cover the change ([Conventions](../../AGENTS.md#conventions)). After a submission, the lander runs the checks of `.ultimate/settings.json`. `pnpm check` covers only the repository (`extensions/README.md`)
- **Risk**: the number of upstream commits that touch the place, from `git log --no-merges --oneline 33c05e9 -- <path> | wc -l`. High is 100 or more, medium is 20 to 99, and low is 1 to 19. "None" is outside the repository. A path that upstream edits often has a higher risk of a merge conflict when uao edits it too (inferred)

| Change              | Place                             | Layer  | Goes live              | Checks            | Risk            |
| ------------------- | --------------------------------- | ------ | ---------------------- | ----------------- | --------------- |
| Web facet           | `extensions/<name>/web.tsx`       | 4 or 5 | Hot reload             | Base              | High, 312       |
| Server facet        | `extensions/<name>/server.ts`     | 4 or 5 | Reinstall on save      | Base              | High, 509       |
| Extension contract  | `extensions/<name>/api.ts`        | 4 or 5 | With its importers     | Base, `pnpm deps` | Medium, 46      |
| New built-in        | A new folder in `extensions/`     | 5      | Like its facets        | Base              | Low, note 1     |
| Project extension   | `.ultimate/extensions/<name>/`    | 6      | Note 2                 | Base              | Low, 16         |
| Personal extension  | `~/.ultimate/extensions/<name>/`  | 6      | Like its facets        | None              | None            |
| Helper              | `lib/`                            | Beside | With its importers     | Base              | Medium, 44      |
| Web core            | `web/`                            | 3      | Hot reload             | Base              | High, 164       |
| Core                | `server/`, `shared/`              | 2      | The `restart` tool     | Base              | High, 123       |
| Supervisor          | `bin/`                            | None   | `pnpm start` only      | Base              | Medium, 22      |
| Built-in definition | `agents/<name>.md`                | Beside | Note 3                 | Base              | Medium, 74      |
| Project definition  | A new file in `.ultimate/agents/` | Beside | At its next start      | Base              | Low, note 4     |
| Project setting     | `.ultimate/settings.json`         | Beside | Live                   | Base              | Medium, 24      |
| Personal setting    | `~/.ultimate/settings.json`       | Beside | Live                   | None              | None            |
| Project skill       | `.ultimate/skills/<name>/`        | Beside | Note 3                 | Base              | Low, 2          |
| Pi patch            | `patches/`, `pnpm-workspace.yaml` | 1      | Note 5                 | Base, note 5      | Low, 18, note 5 |
| Rule                | `AGENTS.md`                       | None   | Note 3                 | Base              | High, 121       |
| North-star          | `docs/north-star/`                | None   | When an agent reads it | `check_links.py`  | None, 0         |

Notes:

1. A new folder has no upstream history, so only a later upstream folder with the same name can collide with it (inferred). The guide requires a README (`extensions/README.md`). A web facet that imports a `.ts` file needs a line in `tsconfig.web.json`, which has 39 commits. 37 of these commits also touch `extensions/`
2. A project extension loads after the user trusts the project ([D009](decisions/D009-trust-before-project-setup.md)). Its code goes through a coordinator branch ([D027](decisions/D027-project-code-through-branches.md)). Then it goes live like the facets of a built-in (`extensions/README.md`)
3. A new conversation reads the new text. At its next input, @ultimate also gets a note that names the changed definition and instruction files. Other agents keep the instructions that they started with (`extensions/prompt/server.ts:80`). The skills go into the system prompt (`extensions/prompt/server.ts:264`)
4. An overlay extends a built-in definition instead of a copy of it ([Subagents](../subagents.md)). A new file has no upstream history. An edit of an upstream file in `.ultimate/agents/` meets 28 upstream commits
5. A Pi patch goes live after `pnpm install` and a restart (inferred from `8b87d6f`). `test/e2e/pi-upstream.test.ts` checks the list in [Borrowed from Pi](../pi-upstream.md). Upstream upgraded Pi four times (`8d5dc26`, `e93d930`, `f7f0863`, `d7dd683`). Each upgrade renamed the Pi Durable patch file with the new version

## Stable parts and parts that change often

Most changes go to the conversation lifecycle, the web app, and the agent definitions. The core contracts and the supervisor are stable. `git log --no-merges --format=%ad --date=short 33c05e9 -- <path>` gives each count, and "Last 3 days" counts 2026-10-21 to 2026-10-23.

| Path                            | Commits | Last 3 days | Reading                       |
| ------------------------------- | ------: | ----------: | ----------------------------- |
| `test/`                         |     813 |         152 | Changes with most features    |
| `extensions/conversations`      |     136 |          14 | Changes often                 |
| `extensions/subagents`          |     134 |          21 | Changes often                 |
| `extensions/lineage`            |     130 |          36 | Changes often, and still fast |
| `extensions/workspaces`         |     128 |          16 | Changes often                 |
| `web/src/app`                   |     129 |          24 | Changes often                 |
| `AGENTS.md`                     |     121 |           8 | Fewer changes now             |
| `agents/`                       |      74 |          30 | Receives the behavior rules   |
| `lib/`                          |      44 |          23 | Many new helpers              |
| `extensions/self`               |      35 |           1 | Stable                        |
| `shared/protocol.ts`            |      34 |           1 | Stable                        |
| `bin/`                          |      22 |           4 | Stable                        |
| `shared/extension-api.ts`       |       5 |           1 | Stable                        |
| `server/supervisor-protocol.ts` |       4 |           0 | Stable since 2026-10-12       |

A count measures 23 days of history. A low count can mean a young path, not a stable one: `extensions/side-chat` exists only since 2026-10-22 (`34c3633`). A rename starts a new count: `extensions/messages` has 8 commits, and the folder of the Board extension had 94 before the rename (`28d657a`).

Some parts did not last. Nine extension folders left `extensions/` before the snapshot. Upstream deleted eight, such as `canvas` (`deb65f8`), `sync` (`67caeb6`), and `faux` (`f23e291`). The ninth, the Board extension, became `extensions/messages` (`28d657a`). [history.md](history.md#eras) lists the removals of each era.

### Areas that change together

Some paths change in the same commits. `comm -12 <(git log --no-merges --format=%h 33c05e9 -- <a> | sort) <(git log --no-merges --format=%h 33c05e9 -- <b> | sort) | wc -l` counts the commits that touch both paths:

- `web/src/app` and `web/src/sdk`: 72 commits. A change to the app often changes the SDK (inferred)
- `extensions/conversations` with `extensions/workspaces`, `extensions/lineage`, or `extensions/subagents`: 38 to 45 commits for each pair. Branches, isolates, and conversations change as one lifecycle (inferred)
- `AGENTS.md` and `extensions/subagents`: 36 commits. A change to delegation changes the rules too (inferred)
- `server/extensions.ts` and `shared/protocol.ts`: 23 commits
- `package.json` and `pnpm-lock.yaml`: 23 commits

## Seams

A seam is a place where new behavior attaches with no edit to an upstream file. Each seam below is in an additive place of the [sync rule](upstream.md#sync-rule):

- **A new extension folder** in `.ultimate/extensions/<name>/` or `~/.ultimate/extensions/<name>/`. Discovery finds it, and it is on by default (`extensions/README.md`). A folder with the name of a built-in replaces the whole built-in, so that copy no longer follows upstream (inferred)
- **Extension APIs and points.** A new extension uses an upstream contract with `host.need` or `host.want`, or it fills a point of the core tier ([Extension APIs](../extensions.md#extension-apis), [Core tier](../extensions.md#core-tier))
- **Durable events.** A reactor reads the events of upstream extensions in order, across crashes ([Durable events](../extensions.md#durable-events))
- **Web contributions.** A web facet adds slots, panels, surfaces, renderers, and commands, and it can wrap the composer ([Contributions](../../extensions/README.md#contributions))
- **Hooks.** A server facet adds a hook such as `beforeInput` (`extensions/lineage/server.ts:1506`). Its transactional form comes from a local Pi patch ([Borrowed from Pi](../pi-upstream.md))
- **Agent definitions.** A new definition, an overlay, or a new `reviewer-<name>.md` in `.ultimate/agents/` or `~/.ultimate/agents/` ([Subagents](../subagents.md))
- **Personal setup** in `~/.ultimate/`: `settings.json`, `skills/`, and `AGENTS.md` ([Discovery and settings](../settings.md))
- **Project subscriptions** in `.ultimate/subscriptions/<slug>/`, which load stopped (`8cc313c`)

Two limits apply. The lander checks and the push target live in `.ultimate/settings.json`, an upstream file, so uao changes them with an edit (inferred). The personal places are outside the repository, so uao cannot keep them under version control (inferred).

## Areas in motion at the snapshot

These areas changed most on 2026-10-22 and 2026-10-23, the last two days before the snapshot. In these two days, upstream made 158 commits that are not merges. Each count comes from `git log --no-merges --format=%ad --date=short 33c05e9 -- <path> | grep -c '2026-10-2[23]'`:

- **Dreams and chapters**: `extensions/dream` 23 and `lib/chapters.ts` 6. Both are new on 2026-10-23 (`34c001a`, `4c94093`). Subscriptions do not move into a new chapter yet ([B15](bricks/B15-dreams-and-chapters.md))
- **The conversation tree**: `extensions/lineage` 22. A project keeps one root (`86ed900`), a branch starts with a title (`6c37b8f`), and catch-up waits for a ready checkout (`13cac20`) ([B07](bricks/B07-conversation-tree.md))
- **Subscriptions**: `extensions/subscriptions` 19. Projects commit them (`8cc313c`), and a panel shows them (`cc54171`) ([B13](bricks/B13-background-work.md))
- **The team**: `extensions/subagents` 16 and `agents/ultimate.md` 13. Tool denials (`556eb4c`), the watchdog (`fb51fea`), and the coordinator model (`8883ef7`) changed. The `branch` tool does not apply that model yet ([Known drift](upstream.md#known-drift-in-upstream-docs)) ([B09](bricks/B09-coordinators-and-subagents.md))
- **Messages**: 17 commits touch the Board extension or `extensions/messages`, around the rename (`28d657a`) ([B11](bricks/B11-notes-and-messages.md))
- **Isolates**: `extensions/workspaces` 12. The removal and the preparation of isolates changed (`9a0d246`, `3fcffd5`) ([B10](bricks/B10-isolates-previews-lander.md))
- **Side chats**: `web/src` 21 and `extensions/side-chat` 5. Conversation scopes and side chats are new (`c18bdbb`, `34c3633`) ([B12](bricks/B12-human-in-the-loop.md))

A uao change in one of these areas meets the most upstream motion at the next merge (inferred).
