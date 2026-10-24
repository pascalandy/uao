# History

This file says how upstream reached the [snapshot](upstream.md#snapshot): its eras, how a change lands, and how the rules and the team changed. The [bricks](bricks/README.md) say what each part does, and the [decisions](decisions/README.md) say why.

Each date is an author date, as `git log --date=short` shows it. Each count is for upstream at `33c05e9`.

## Summary

- Upstream has 1,395 commits from 2026-10-01 to 2026-10-23 (`git rev-list --count [--merges] 33c05e9`). 289 are merges and 1,106 are work commits
- Daniel Griesser authored all but one commit, `ca2348d` (`git shortlog -sne 33c05e9`)
- 791 work commits carry the trailer that the `bash` tool of Ultimate adds (`git log --no-merges --grep='^Ultimate-Conversation:'`). So Ultimate's agents made most of the work (inferred)
- A change unit is the work of one conversation. The trailers name 365 change units, and 212 of them have one commit

## Eras

Upstream went through eight eras. An era is a span of days with one main theme. `git log --format=%ad --date=short 33c05e9 | sort | uniq -c` gives the commits of each day. A landing merge puts a change unit on `main` ([How a change lands](#how-a-change-lands)). A change unit counts in the era of its first work commit. Commits before 2026-10-14 have no trailer, so the table counts no change unit for them.

| Era                  | Dates (2026)   | Commits | Landing merges | Change units | Decisions    |
| -------------------- | -------------- | ------: | -------------: | -----------: | ------------ |
| 1 Foundation         | 10-01 to 10-02 |      89 |              0 |            0 | D001 to D009 |
| 2 Parallel work      | 10-03 to 10-11 |      63 |              0 |            0 | none         |
| 3 Delivery path      | 10-12 to 10-13 |     189 |             11 |            0 | D010 to D012 |
| 4 Conversation tree  | 10-14 to 10-16 |     217 |             11 |           76 | D013 to D015 |
| 5 One front door     | 10-17 to 10-18 |     289 |             21 |          121 | D016 to D024 |
| 6 Boundaries         | 10-19          |     168 |             14 |           44 | D025, D026   |
| 7 Memory and backups | 10-20 to 10-21 |     172 |             15 |           53 | D027 to D029 |
| 8 Recoverable work   | 10-22 to 10-23 |     208 |             24 |           71 | D030, D031   |

### Era 1: Foundation

Daniel builds a durable host that edits its own code. Extensions form its UI.

- Added:
  - layer table (`9b341af`, [D001](decisions/D001-reload-by-layer.md))
  - Pi Durable host (`692ca8f`, [B01](bricks/B01-durable-conversations.md))
  - supervisor swap (`e3f76bb`, [B02](bricks/B02-self-change-while-running.md))
  - web facets and surfaces (`fff6d4b`, `790c34e`, [B03](bricks/B03-reloadable-extensions.md))
  - codemode (`1a0453c`, [B05](bricks/B05-agent-tools.md))
  - subagents in isolates (`a300225`, `1c10440`, [B09](bricks/B09-coordinators-and-subagents.md))
  - project setups only after trust (`1135742`, `a5fe6b8`, [B06](bricks/B06-project-specialization.md))
- Reworked: commands, agent definitions, and model login move from the core into extensions (`98a9f64`, `1b48020`, `ecc5a3d`)
- Removed: `bouncy-ball`, a reload test extension (`844198e`)

### Era 2: Parallel work

Conversations run in parallel in one project. Each boundary has an owner.

- Added:
  - top-level conversations aware of each other (`59f065b`)
  - automations (`3ad26d3`, [B13](bricks/B13-background-work.md))
  - owner-only Tailscale access (`a5adb0f`, [B16](bricks/B16-remote-backup-update.md))
  - `integrate-ultimate` skill (`248b25f`)
- Reworked:
  - durable tasks for isolate land and discard (`7ed6c04`)
  - project settings wait for the trust choice (`024ff05`, [D009](decisions/D009-trust-before-project-setup.md))
- Removed: the native Claude Code provider moves to Git branch `feature/claude-code` (`52f6b52`)

### Era 3: Delivery path

The work of an isolate gets a path to `main` through checks and a push.

- Added:
  - isolates for any conversation (`ce5839e`, [B10](bricks/B10-isolates-previews-lander.md))
  - push permission (`219dad1`, [D010](decisions/D010-push-without-asking.md))
  - landing queue (`5c36dcd`, [D011](decisions/D011-lander-queue.md))
  - commit trailer (`ef3591a`)
  - fixed review team (`1772c50`)
  - Canvas (`9c129ad`)
  - Claude Code CLI provider (`787b454`, [B04](bricks/B04-models-and-providers.md))
- Reworked:
  - isolates move into the workspaces extension (`a8acb1b`)
  - visible results get cards (`67d1b54`, [D012](decisions/D012-design-visible-results.md))
- Removed: Claude Code reviewers. Native reviewers replace them (`a7a47e8`)

### Era 4: Conversation tree

A project's conversations form a tree that its root records.

- Added:
  - branches and notes (`99c76b2`, [B07](bricks/B07-conversation-tree.md), [D013](decisions/D013-branch-is-not-subagent.md))
  - standing lander (`ef88374`)
  - landing notes and catch-up (`2166faa`, `04e5be3`)
  - abstracts (`fc99691`)
  - divergence (`7d29e8f`)
  - one review lead (`79cef07`)
- Reworked:
  - one root becomes several (`bbb0e3e`), then tallies that run no turns (`00cdf3a`, [D015](decisions/D015-root-is-a-tally.md))
  - tests split into fast and browser runs (`d48d30a`)
  - lander checks: tests dropped for a time, then back in one parallel group (`58250b7`, `c09e551`)
- Removed: Canvas (`deb65f8`, [D014](decisions/D014-remove-canvas.md)), exclusive commands (`89676a2`), and scout and researcher definitions (`638ccf9`)

### Era 5: One front door

The user talks to @ultimate. Standing agents and messages do the rest.

- Added:
  - standing agents (`8a1c100`, [B08](bricks/B08-ultimate-and-standing-agents.md), [D019](decisions/D019-standing-agents.md))
  - durable messages (`986ca6c`, [B11](bricks/B11-notes-and-messages.md))
  - personal layer (`ec5dfad`, [D018](decisions/D018-own-personal-layer.md))
  - extension APIs and durable events (`f466038`, `7463db5`, [D024](decisions/D024-typed-contracts-core-tier.md))
  - call trace (`2bf6879`, [B14](bricks/B14-everything-on-record.md))
  - `lib/` (`2a79f3b`)
- Reworked:
  - questions get proposals (`bf94a30`, [D017](decisions/D017-questions-get-proposals.md))
  - work fits its size (`25d180d`, [D020](decisions/D020-size-the-work.md))
  - updates become notes (`304e47e`, [D021](decisions/D021-updates-are-notes.md))
  - only @ultimate messages the user (`4d3605e`, [D022](decisions/D022-route-through-ultimate.md))
  - tally named "context" in the UI (`b99106e`, [D023](decisions/D023-context-and-tally.md))
  - the cloud copies conversations (`8b5d5ac`), then adds a writer lease and moves (`d8f80cb`)
  - Ultimate becomes a personal project (`e445117`, [D016](decisions/D016-personal-project.md))
- Removed: Board surface (`eeae136`) and manual conversation creation (`64f3bc4`)

### Era 6: Boundaries

Extensions get enforced boundaries. The work of the agents goes on record.

- Added:
  - core tier (`0edd691`)
  - System stream, a paged list of events and calls (`06cf3f3`)
  - assessment (`f0d80a3`, [D025](decisions/D025-assess-first.md))
  - Review (`f074882`, [B12](bricks/B12-human-in-the-loop.md))
  - emergency terminal agent (`56b0e1c`)
- Reworked:
  - stable system prompt (`803cbee`, [D026](decisions/D026-stable-system-prompt.md))
  - the transcript opens on recent content. It loads older pages when the reader scrolls (`70646c7`)
  - the cloud no longer serves conversations (`c9cc95e`)
- Removed: the single-process event bus (`afa5377`)

### Era 7: Memory and backups

Branches start from project memory. The cloud keeps only backups.

- Added:
  - pause and rewind (`3aa830b`, `4603cb9`)
  - project memory (`4c1b652`, [D029](decisions/D029-branches-start-from-memory.md))
  - to-dos (`0328cac`)
  - clone updates (`a8fba5e`)
  - subscriptions (`656db80`)
- Reworked:
  - project code needs a coordinator branch (`6dfc9e8`, [D027](decisions/D027-project-code-through-branches.md))
  - overlays extend built-in definitions (`9d40a9b`)
  - the cloud keeps only backups (`67caeb6`, [D028](decisions/D028-cloud-only-backs-up.md))
- Removed: model evaluations (`d9ae72d`), @sync, the writer lease, and moves (`67caeb6`)
- Also removed: a home's standby state (`0146ec6`) and machine home (`1708844`)

### Era 8: Recoverable work

Background work gets supervision and recovery. The history of a home gets chapters.

- Added:
  - supervised process groups (`9b55a58`)
  - parked tasks (`6a3f41a`)
  - watchdog for failed runs (`fb51fea`)
  - project subscriptions (`8cc313c`)
  - side chats (`34c3633`)
  - dreams and chapters (`34c001a`, `4c94093`, [B15](bricks/B15-dreams-and-chapters.md))
- Reworked:
  - Pi moves to 1.4.0 (`d7dd683`)
  - Board extension becomes `messages` (`28d657a`)
  - a project keeps one root (`86ed900`)
  - eight built-ins are off by default (`5323967`, [D031](decisions/D031-resource-built-ins-off.md))
- Removed: root tools `new_root`, `seed_tally`, and `compact_tally` (`86ed900`), and faux mode (`f23e291`, [D030](decisions/D030-previews-on-real-models.md))

## How a change lands

Since era 5, a change unit reaches `main` in these steps:

1. @ultimate starts a coordinator branch with the `branch` tool (`extensions/messages/server.ts:1327`)
2. The workspaces extension makes an isolate on Git branch `ultimate/<hash>-<n>`. `<n>` is the conversation ID. `<hash>` comes from the home path (`extensions/workspaces/workspaces.ts:914`)
3. A Git hook of the `bash` tool adds the trailer `Ultimate-Conversation: <n>` to each commit (`extensions/coding-tools/server.ts:59`)
4. Workers commit in their isolates. The coordinator merges their Git branches and `main` into its own
5. The coordinator calls `workspace submit`. Code of the landing queue merges the tip, then runs checks from `.ultimate/settings.json`
6. The code sets `main` to the merge result, then pushes it. It records a landing note in the tally. Resumed branches get a catch-up. The lander agent acts only when a step fails ([D011](decisions/D011-lander-queue.md))

The landing queue uses `git merge` defaults (`extensions/workspaces/lander.ts:769`). Git makes a landing merge only if it cannot fast-forward. Its message is `Merge <sha> from #<n> into main` (`extensions/workspaces/lander.ts:819`).

The 81 landing merges with `#<n>` name 79 conversations. 75 of these conversations are among the 365 change units, and the other 4 have no trailer on their commits. The other change units landed by a fast-forward, or in the Git branch of another unit (inferred).

Landings and their commit trailers can name different conversations. `0eb16c0` names `#209732`. Its commit `8c44921` has trailer `216060`.

### Commit shapes

`git log --merges --format=%s 33c05e9` shows 289 merges in six shapes:

| Shape                   | Subject                                       | Merges |
| ----------------------- | --------------------------------------------- | -----: |
| Landing merge           | `Merge <sha> from #<n> into main`             |     81 |
| Landing merge, old name | `Merge <sha> from W<n> into main`             |     15 |
| Catch-up merge          | `Merge branch 'main' into ultimate/...`       |     73 |
| Merge of a child        | `Merge branch 'ultimate/<hash>-<m>' into ...` |     72 |
| Merge by hand           | `chore(integration): merge ...`               |     24 |
| Other                   | Free text                                     |     24 |

The catch-up row also counts merges of `origin/main` or of a local path. 91 landing merges have no trailer. The other 5 list conflicts and carry the trailer of conversation 30726, such as `23f26ba`. That conversation is the lander, which fixed the conflicts (inferred).

### How the process changed

- Eras 1 and 2: each commit went to `main` directly. No merge predates 2026-10-12
- Era 3: on 2026-10-12, the top-level agent made 20 manual `chore(integration)` merges, such as `d37887a`. The landing queue began on 2026-10-13 (`5c36dcd`). `1d94cbc6` is the first landing merge, and it names `W25966`
- Era 4: `2166faa` is the first work commit with a trailer, on 2026-10-14. `19f960d` changed the label `W<n>` to `#<n>`, and `930d33e` is the first `#<n>` landing merge. 32 work commits on 2026-10-14 and 2026-10-15 have no trailer
- Eras 5 to 8: each work commit has a trailer. @ultimate starts branches (`c685a27`)

### Find the commits of one conversation

Use these commands in a clone of uao:

- Work commits: `git log --grep='^Ultimate-Conversation: <n>$'`
- Landing merges: `git log --grep='from #<n> into main'`. Before 2026-10-14, search for `from W<n>`
- Merges into its Git branch: `git log --grep='ultimate/[0-9a-f]*-<n>'`
- Conversation of a commit: `git log -1 --format='%(trailers:key=Ultimate-Conversation)' <sha>`

Change unit 59981 has both landing shapes. Landing merge `a03d554` put its first commit on `main`, on 2026-10-15. Then `1283047` merged `main` into the unit's Git branch. Next, `550c478` landed by fast-forward (inferred).

## How the rules and the team changed

Up to era 5, most rule changes went to `AGENTS.md`. After era 5, most went to the agent definitions. `git log --no-merges --format=%ad --date=short 33c05e9 -- <path>` gives these counts:

| Path                              |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |
| --------------------------------- | --: | --: | --: | --: | --: | --: | --: | --: |
| `AGENTS.md`                       |  21 |  12 |  21 |  29 |  23 |   4 |   7 |   4 |
| `agents/` and `.ultimate/agents/` |   3 |   0 |   7 |   9 |  22 |  12 |  21 |  19 |

Behavior rules live in prompts ([Principle 11](principles.md), `6b8477d`). These are the main changes:

- Era 1: `a300225` adds the scout, researcher, reviewer, and worker on the parent's model. `7a62d92` gives the coordinator the final verdict
- Era 3: `1772c50` adds the review quality rules and a review team with pinned models
- Era 4: `ef88374` adds the lander definition. `a8fbf6e` removes the mandatory review team. `8be9fec` holds small UI polish until user approval
- Era 5: `c685a27` adds @ultimate. `a410963` adds the coordinator. `e7a77ac` moves details to `docs/`, cutting `AGENTS.md` from 234 lines to 101. `30af13a` and `9d455ec` add @cloudflare and @sync
- Era 6: `9d764b6` names reviewers by their checks. `44bc478` removes @cloudflare
- Era 7: `63da866` restores the scout, adds the designer, and pins the worker to GPT-6.1 Sol
- Era 8: `556eb4c` keeps previews with the coordinator. `2f68182` lets @ultimate restart after core landings without asking. `8883ef7` sets Claude Code Opus 5.5 in the project coordinator definition. But `branch` does not use that model ([Known drift](upstream.md#known-drift-in-upstream-docs))

[Subagents](../subagents.md) describes the team at the snapshot, and each definition names its model.
