# History

This file says how upstream reached the [snapshot](upstream.md#snapshot): its eras, the life of a change unit, and how the rules and the team changed. [upstream.md](upstream.md#differences) records uao's additions since the fork. The [bricks](bricks/README.md) say what each part does, and the [decisions](decisions/README.md) say why.

Each date is an author date, as `git log --date=short` shows it. Each count is for upstream at `6b6d88b6`.

## Summary

- Upstream has 2,766 commits from 2026-10-01 to 2026-11-18 (`git rev-list --count 6b6d88b6`). Of these commits, 726 are merges (`git rev-list --count --merges 6b6d88b6`). The other 2,040 are work commits (`git rev-list --count --no-merges 6b6d88b6`)
- Daniel Griesser authored 2,608 commits, Juan 20, James Groat 19, Tobi Lütke 17, Juliano Julio Costa 13, and the agent identity `Ultimate` 12 (`git shortlog -sne 6b6d88b6`)
- 25 other author names have one to nine commits each. They include the agent identity `CI` (1) (`git shortlog -sne 6b6d88b6`)
- 1,683 work commits carry Ultimate's conversation trailer (`git log --no-merges --grep='^Ultimate-Conversation:' --oneline 6b6d88b6 | wc -l`). Thus, Ultimate's agents made most of the work (inferred)
- A change unit is the work of one conversation. The trailers name 863 change units, and 557 have one commit (`git log --no-merges --format='%(trailers:key=Ultimate-Conversation,valueonly)' 6b6d88b6 | sed '/^$/d' | sort | uniq -c`)

## Eras

Upstream went through eleven eras. An era is a span of days with one main theme. `git log --format=%ad --date=short 6b6d88b6 | sort | uniq -c` gives the commits of each day. A landing merge puts a change unit on `main` ([Life of a change unit](#life-of-a-change-unit)). A change unit counts in the era of its first work commit. `git log --no-merges --format='%ad %(trailers:key=Ultimate-Conversation,valueonly)' --date=short 6b6d88b6` gives each unit and its dates. Commits before 2026-10-14 have no trailer, so the table counts no change unit for them. `git log --merges --format='%ad %s' --date=short 6b6d88b6` gives the dates of the landing shapes defined below.

| Era                      | Dates (2026)   | Commits | Landing merges | Change units | Decisions              |
| ------------------------ | -------------- | ------: | -------------: | -----------: | ---------------------- |
| 1 Foundation             | 10-01 to 10-02 |      89 |              0 |            0 | D001 to D009           |
| 2 Parallel work          | 10-03 to 10-11 |      63 |              0 |            0 | none                   |
| 3 Delivery path          | 10-12 to 10-13 |     189 |             11 |            0 | D010 to D012           |
| 4 Conversation tree      | 10-14 to 10-16 |     217 |             11 |           76 | D013 to D015           |
| 5 One front door         | 10-17 to 10-18 |     289 |             21 |          121 | D016 to D024           |
| 6 Boundaries             | 10-19          |     168 |             14 |           44 | D025, D026             |
| 7 Memory and backups     | 10-20 to 10-21 |     172 |             15 |           53 | D027 to D029           |
| 8 Recoverable work       | 10-22 to 10-24 |     398 |             56 |          130 | D030, D031, D036, D037 |
| 9 Ordinary work          | 10-25 to 11-01 |     465 |             77 |          184 | D038 to D044           |
| 10 Outside contributions | 11-02 to 11-13 |     417 |             83 |          174 | none                   |
| 11 Enforced rules        | 11-14 to 11-18 |     299 |             39 |           81 | D045                   |

The sync of 2026-11-09 adds 177 work commits and 105 merges (`git rev-list --count --no-merges d0a2e17b..32e45c95`, `git rev-list --count --merges d0a2e17b..32e45c95`). Its commits dated up to 2026-11-01 go to era 9. Some author dates precede the old snapshot date because those commits reached upstream later (`8db6c877`, `01d0a9ed`, `db1d8d12`). Era 10 starts on 2026-11-02, when outside pull requests began to land in large numbers ([Outside contributions in the November 9 sync](#outside-contributions-in-the-november-9-sync)).

The sync of 2026-11-11 adds 32 work commits and 17 merges (`git rev-list --count --no-merges 32e45c95..11c89136`, `git rev-list --count --merges 32e45c95..11c89136`). All 49 commits are dated 2026-11-09 or 2026-11-10, so they go to era 10 (`git log --format=%ad --date=short 32e45c95..11c89136 | sort | uniq -c`).

The sync of 2026-11-18 adds 270 work commits and 156 merges (`git rev-list --count --no-merges 11c89136..6b6d88b6`, `git rev-list --count --merges 11c89136..6b6d88b6`). Its commits dated up to 2026-11-13 go to era 10, and the later ones start era 11 (`git log --format=%ad --date=short 11c89136..6b6d88b6 | sort | uniq -c`). Four of them have author dates of 2026-11-10 or earlier, because their pull requests landed later (`1ccebc60`, `bc938b06`, `e4a143e3`, `e59a9873`). Era 11 starts on 2026-11-14, when upstream put its rules for code into lint and a rule table ([Era 11](#era-11-enforced-rules)).

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
  - one root becomes several roots (`bbb0e3e`), and then the roots become tallies that run no turns (`00cdf3a`, [D015](decisions/D015-root-is-a-tally.md))
  - tests split into fast and browser runs (`d48d30a`)
  - the lander checks drop the tests for a time, and then run them again in one parallel group (`58250b7`, `c09e551`)
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
  - the cloud copies conversations (`8b5d5ac`), then adds a writer lease and project moves between machines (`d8f80cb`)
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
- Removed: model evaluations (`d9ae72d`), @sync, the writer lease, and project moves (`67caeb6`)
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
  - structured questions on messages, including a comment field on each answer card (`de87bde`, [B12](bricks/B12-human-in-the-loop.md))
  - built-in skills for extensions, UI previews, and UI verification (`bc3a786`, [B06](bricks/B06-project-specialization.md))
  - event and context triggers for automations (`a7f32b5`, [B13](bricks/B13-background-work.md))
  - user grants for dreams, compaction, and chapter switches (`d6c9628`, [B13](bricks/B13-background-work.md), [B15](bricks/B15-dreams-and-chapters.md))
  - server records of context use (`ed0bb8a`, [B14](bricks/B14-everything-on-record.md))
  - hands-off goals with goal decisions and a goal report (`001a193d`, `65a251f`, `a1b3c01`, [B12](bricks/B12-human-in-the-loop.md), [D037](decisions/D037-goals-delegate-approvals.md))
  - dreams after @ultimate's compaction, with checked chapter changes and continuation of its work (`6c1c6bc`, `4195ad4`, [B15](bricks/B15-dreams-and-chapters.md))
  - agent calls for backups and clone updates (`d3178ff`, [B16](bricks/B16-remote-backup-update.md))
  - self-compaction beyond @ultimate, with a wake-up for each request (`d3178ff`, `4a6aab5`, [B01](bricks/B01-durable-conversations.md))
- Reworked:
  - Pi moves to 1.4.0 (`d7dd683`)
  - Board extension becomes `messages` (`28d657a`)
  - a project keeps one root (`86ed900`)
  - eight built-ins are off by default (`5323967`, [D031](decisions/D031-resource-built-ins-off.md))
  - subscriptions become script triggers in automations, under one ledger and UI (`e099781`, `9dd221c`, [B13](bricks/B13-background-work.md))
  - the branch tool applies the coordinator definition's model and thinking level (`8ff34aa`, [B09](bricks/B09-coordinators-and-subagents.md))
  - previews use the `instance.model` setting (`a4843af`, [D036](decisions/D036-previews-on-instance-model.md))
  - agents avoid repeated tests on an unchanged tree (`1c8a97e`, [B09](bricks/B09-coordinators-and-subagents.md))
  - messages become separate modules, and a message to an agent can answer its earlier request (`2941024`, `b956232`, [B11](bricks/B11-notes-and-messages.md))
  - retryable rate limits pause the host (`a63e2fb`, `787fa1a`, [B12](bricks/B12-human-in-the-loop.md))
  - Play by itself releases rate-limit pauses (`d3178ff`, `4a6aab5`, [B12](bricks/B12-human-in-the-loop.md))
  - the **Agents tab** saves overlays and keeps their `addTools` (`d3c39fd`, `ba7984e`, [B06](bricks/B06-project-specialization.md))
  - coordinator branches receive deferred tools from overlays (`d3178ff`, [B09](bricks/B09-coordinators-and-subagents.md))
  - the watchdog reports idle branches sooner, and coordinators stop only for completion, a block, or a promised wake-up (`a7495cb`, [B09](bricks/B09-coordinators-and-subagents.md))
  - repeated cards and relative-time helpers use SDK exports (`0104d7a`, [B03](bricks/B03-reloadable-extensions.md))
  - the answer card's Undo countdown works on phones (`93dbff1`, [B12](bricks/B12-human-in-the-loop.md))
  - the title bar and conversation transitions change (`09d1ae5`, `7113b4f`)
- Removed:
  - root tools `new_root`, `seed_tally`, and `compact_tally` (`86ed900`)
  - faux mode (`f23e291`, [D030](decisions/D030-previews-on-real-models.md))
  - the separate subscriptions extension and agent definition (`e099781`, [B13](bricks/B13-background-work.md))
  - question extraction by the summary model (`de87bde`, [B12](bricks/B12-human-in-the-loop.md))

Additional work on October 24 completes era 8:

- Added: satellites (`2bfc6b22`), the installable web app (`12fd115c`), cache warming (`f9d91e85`), and voice input (`a0608d3f`)
- Added: the onboarding walkthrough (`79107fdd`, [B08](bricks/B08-ultimate-and-standing-agents.md))
- Reworked: dreams start before compaction (`09008b66`), at 70% context by default (`1353fb6b`)
- Reworked: Update ships on and offers a coordinator merge for a diverged clone (`7f011b47`, [B16](bricks/B16-remote-backup-update.md))
- Reworked: write and edit calls stream their arguments (`fbfe98ce`), and later Claude Code tools preserve the cached prefix (`dec99d5e`)

### Era 9: Ordinary work

New input and remote access join the existing workflow. Dreams, messages, and landings use fewer special agent roles (inferred from `be1608a7`, `136d9c01`, and `cfd0e93b`).

- Added:
  - live voice through the standing Voice agent (`f3b257b6`, [B12](bricks/B12-human-in-the-loop.md))
  - recall of relevant project memories (`48f2f2e6`, [B07](bricks/B07-conversation-tree.md))
  - read-only status for dashboards (`ca5dec4c`, `6b44de7b`, [B14](bricks/B14-everything-on-record.md))
  - remotes without cloud backups and machine selection (`2a6d9e51`, `197a3e3f`)
  - configurable worktree layout and commands (`2affc7ad`, `3b71cca5`)
  - the goal reminder (`64f94443`) and the idle dream trigger (`6c37a236`)
  - extension-owned agent definitions (`ab959a36`) and setup adaptation (`710be091`, [B06](bricks/B06-project-specialization.md))
  - declared secrets and provider-auth coverage (`457c5a53`, `07172eed`)
- Reworked:
  - model selection follows confirmed logins and protects subscription logins (`21ff1b3f`, `fa6830aa`, [D038](decisions/D038-models-follow-logins.md))
  - the contribution policy permits selected core improvements and keeps feature PRs as references (`465cf344`, [D016](decisions/D016-personal-project.md))
  - dreams become ordinary branch work, with only preparation and chapter changes in code (`be1608a7`, [D040](decisions/D040-dream-as-ordinary-work.md))
  - upward updates become notes; finished branches send waking reports (`136d9c01`, [D041](decisions/D041-state-based-waking.md))
  - a model-free lander concludes landed branches unless work remains under way; a concluded branch wakes its starter and frees its eligible checkout (`cfd0e93b`, [D042](decisions/D042-model-free-landing.md))
  - History and Memory become separate reading views (`76eaa574`, `21669aa1`)
  - task groups name work and deliveries (`b3462787`, `03d967f4`)
  - draft images survive reloads (`4eb6a626`), and transcript stretches fold intermediate steps (`ebb71f13`)
  - sounds follow agent actions and landings (`06a706bb`, `76ea0ae7`, `09befdd5`)
  - browser tabs share one event stream (`27e615d0`, `70f56ce5`)
  - final rate-limit failures no longer pause the host again (`9e3164f5`)
- Removed:
  - automation grants and `act` (`ef738270`, [D039](decisions/D039-remove-automation-grants.md))
  - the lineage branch action, leaving the messages tool as the agent entry point (`dbb79677`)
  - the minimap and its graveyard folder, replaced by project-memory tombstones (`6dfcf451`, `63f87af5`)
  - lander agent definitions, `workspace land`, and the deploy handoff (`cfd0e93b`)
  - the unused emergency terminal agent (`17d186bf`, [B02](bricks/B02-self-change-while-running.md))

The November 1 snapshot extends this era:

- Added:
  - model families and one Agents panel for their assignments (`741ec0da`, `490f88b2`, [D043](decisions/D043-model-families.md))
  - MCP servers through one tool, transport recovery, and configured secret declarations (`5eae312d`, `16a71d81`, `90fa141d`, [B05](bricks/B05-agent-tools.md))
  - Sketch UI and forms, then a separate Sketch model definition (`a7ab9797`, `b2f7043f`, [B05](bricks/B05-agent-tools.md))
  - narration for questions, failures, landings, and new branches (`451ac392`, [B12](bricks/B12-human-in-the-loop.md))
  - standing agent icons and tints in frontmatter (`17157665`, [B06](bricks/B06-project-specialization.md))
  - stable shell attributes for theme extensions and error reports to @ultimate (`eb77a9aa`, `cf2315bf`, [B03](bricks/B03-reloadable-extensions.md))
  - image drops in the composer (`3fa3753c`, [B12](bricks/B12-human-in-the-loop.md))
- Reworked:
  - branches ask the user after @ultimate weighs in; @ultimate sees pointers and answer notes (`5014cc55`, [D044](decisions/D044-branches-ask-the-user.md))
  - @ultimate's final answers return to all eligible reporting branches in the run (`dce7b5cf`, `aaa55768`, [D041](decisions/D041-state-based-waking.md))
  - @ultimate can settle open cards from the user's words in its chat (`7b09649d`, [B12](bricks/B12-human-in-the-loop.md))
  - new conversations preserve configured defaults without a login (`4497cb74`, [D038](decisions/D038-models-follow-logins.md))
  - previews use private copies of user configuration and a family assignment (`1efbcb19`, `d6f3657a`, [B10](bricks/B10-isolates-previews-lander.md))
  - project and agent-model facts come from current manifests and definitions, not memory (`08d193b3`, [B08](bricks/B08-ultimate-and-standing-agents.md))
  - the Plan panel shows epics without plan tasks by their criteria (`34624b5d`, [B07](bricks/B07-conversation-tree.md))
  - Update reports an owed core restart after a landing or clone change (`fe5907cd`, [B02](bricks/B02-self-change-while-running.md))
  - linked server facets reload after imported file changes (`c0c1197c`), and browser waits survive reloads (`cf4b7b1b`)
  - memory extraction gets a larger output budget (`5b4de93a`), and trace rows name shell exit codes (`5edd9810`)
  - PRs are welcome as shared ideas; core merges remain exceptions (`5524835f`, [D016](decisions/D016-personal-project.md))
- Removed:
  - per-model concurrency caps, added with families and removed before the snapshot (`741ec0da`, `a0b75c9e`)
  - feature threads, added and removed within this range (`050141d2`, `fe08571f`)
  - untyped service registration and the supervisor's service report (`6e9cd78d`)
  - unused transcript grouping and intro contributions (`49456b0c`, `7194ccfa`)

The November 9 sync adds 41 commits to this era, 38 of them dated 2026-11-01 (`git log --format=%ad --date=short d0a2e17b..32e45c95 | rg -c 2026-11-01`). These are the main changes:

- Added:
  - a pinned header with the current prompt and its changes since the last dismissal (`507b378f`, [B12](bricks/B12-human-in-the-loop.md))
  - the summary history of a branch on a sidebar hover (`870a0217`, [B07](bricks/B07-conversation-tree.md))
  - subagents made on the fly from a label, a family or a model, and instructions (`6b0fb859`, [B09](bricks/B09-coordinators-and-subagents.md))
  - a `transcript.top` slot for extensions (`14953598`, [B03](bricks/B03-reloadable-extensions.md))
- Reworked:
  - a small helper process starts child processes, and git and transcript streams stop blocking the host (`4b314408`, `5c610524`)
  - the conversation list re-renders only the conversations that changed (`830a36c1`, [B14](bricks/B14-everything-on-record.md))
  - automated browsers never steer the user's tabs (`0040f365`, [B05](bricks/B05-agent-tools.md))
  - `images: "latest"` covers only the current turn (`6cc90767`)
- Removed: Sketch and the `subagent: false` definition field (`e6909945`, [B05](bricks/B05-agent-tools.md))

Tobi Lütke's `d3c39fd` reached `main` through [HazAT/ultimate#2](https://github.com/HazAT/ultimate/pull/2). Its merge commit `1b62f6b` has a GitHub subject, not a landing-queue subject, and carries trailer `360463` (an Ultimate conversation).

### Outside contributions in the November 1 sync

These merged PRs are core fixes or extension improvements, consistent with the exception in D016 (inferred from the changes below). A merge can include a later adjustment:

| PR                                               | Change at the snapshot                                                                                                                  | Work commit and merge                                      |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [#35](https://github.com/HazAT/ultimate/pull/35) | macOS process groups, storage-lock identity, Git diagnostics, and portable fixtures. The harness later passes the start time explicitly | `f3ba79d3`, `6dd1aa58`, `e0d3f822`, `ba62f6c6`, `91f1fde4` |
| [#36](https://github.com/HazAT/ultimate/pull/36) | Preserve existing commit attribution when a commit is rewritten                                                                         | `df00cf20`, `546cb645`                                     |
| [#37](https://github.com/HazAT/ultimate/pull/37) | Prompt-level decision-card instruction merged, then removed in favor of each agent's instructions                                       | `247df3a8`, `194b556a`, `ec027220`                         |
| [#38](https://github.com/HazAT/ultimate/pull/38) | Keep the Tailscale URL above the local URL in the dashboard                                                                             | `fc77dee5`, `f5429d76`                                     |
| [#40](https://github.com/HazAT/ultimate/pull/40) | Larger memory output budget and shared limits. A later commit removes repeated limits                                                   | `5b4de93a`, `56b7fb6e`, `aa2f79da`                         |
| [#41](https://github.com/HazAT/ultimate/pull/41) | Send a held answer when the page is left during Undo                                                                                    | `46d0054d`, `2cc2b696`                                     |
| [#42](https://github.com/HazAT/ultimate/pull/42) | Recover released checkouts and preserve live descendants. The additional lander conclusion guard was removed                            | `27f9d781`, `43385153`, `1a0541ee`                         |
| [#43](https://github.com/HazAT/ultimate/pull/43) | A stale test-folder sweep failure no longer fails the test run                                                                          | `2789f8b8`, `af3d3996`                                     |
| [#48](https://github.com/HazAT/ultimate/pull/48) | Stable `data-ui` attributes for theme extensions                                                                                        | `eb77a9aa`, `28eb9e9c`, `f05016b6`                         |

No merged PR numbered 39 or 44 to 47 is present in that sync's history. `git log --merges --format='%h %s' 17d186b..d0a2e17b` lists the merges, including `pr-*` subjects.

### Era 10: Outside contributions

Outside pull requests land almost every day. The web UI becomes a production bundle, and the host gets safer defaults. The November 9 sync merges 44 outside pull requests, against nine in the November 1 sync. All but #49 land in this era ([table below](#outside-contributions-in-the-november-9-sync)). The November 11 sync merges four more ([table](#outside-contributions-in-the-november-11-sync)). The November 18 sync merges 60 more, in eras 10 and 11 ([table](#outside-contributions-in-the-november-18-sync)).

- Added:
  - Pi 1.5.0, with Pi's `pi-schema` for tool schemas (`669df90a`, `0bb05358`, [B01](bricks/B01-durable-conversations.md))
  - a production web bundle that a child process builds, in place of the Vite dev server (`47c08a50`, [B02](bricks/B02-self-change-while-running.md), [D001](decisions/D001-reload-by-layer.md))
  - attachments of any file, and image resize in the browser (`80016496`, `6bae2586`, [B12](bricks/B12-human-in-the-loop.md))
  - Web Push notifications, off by default, and a share target, always on (`ff44988c`, `extensions/push/README.md`, [B12](bricks/B12-human-in-the-loop.md))
  - Wire, the raw record of model calls, off by default (`9b8f1866`, `c16450c9`, [B14](bricks/B14-everything-on-record.md))
  - prompt-cache rebuilds in the transcript (`c30582af`, [B14](bricks/B14-everything-on-record.md))
  - a security policy (`c21f2d6d`, [B16](bricks/B16-remote-backup-update.md))
  - Claude Code model discovery (`983ad978`, [B04](bricks/B04-models-and-providers.md)) and an optional family in the branch tool (`0c176481`, [B09](bricks/B09-coordinators-and-subagents.md))
  - token weight on landing cards and `pnpm weigh` (`f7ba0607`, [B10](bricks/B10-isolates-previews-lander.md))
- Reworked:
  - previews get their own `HOME`, land on their own branch, and never push (`8f67613f`, `d1fe28fb`, [B10](bricks/B10-isolates-previews-lander.md))
  - Chromium runs with its sandbox, and other sites cannot frame the UI (`dbe9bb50`, `751b5e44`, `dcd6d4b8`, [B05](bricks/B05-agent-tools.md), [B16](bricks/B16-remote-backup-update.md))
  - Update restarts the host when facets fail against an old core, and loads wait for installs (`f20cc792`, `1441b930`, [B02](bricks/B02-self-change-while-running.md))
  - a branch's result reaches the agent whose request it worked on (`71582661`, [B11](bricks/B11-notes-and-messages.md))
  - the catch-up reads the target's first-parent history, and each landing merge carries its trailer (`29b5223d`, `9a79b7f9`, [B07](bricks/B07-conversation-tree.md))
  - the phone layout runs rows edge to edge, with the composer as a sheet (`1be263cf`, [B12](bricks/B12-human-in-the-loop.md))
  - ten built-ins ship off by default (`ff44988c`, `c16450c9`, [D031](decisions/D031-resource-built-ins-off.md))
  - a person's own family choices apply over the project's team settings (`885ee383`, [B04](bricks/B04-models-and-providers.md))
  - each extension's tests move into `extensions/<name>/test/` (`c387c88b`, [B03](bricks/B03-reloadable-extensions.md))
  - the extension guide splits into topic files under `docs/extensions/` (`729f493c`)
- Removed:
  - the architecture diagrams and the unused `review/ui.tsx` (`a1a53d4e`)
  - the Pi coupling check from the e2e suite, which `pnpm check` now runs (`770b0243`)

### Outside contributions in the November 9 sync

Each row is a merged outside pull request. `git log --merges --format='%h %s' d0a2e17b..32e45c95` lists the merges. Most land through a `Merge branch 'pr-<n>'` merge into a coordinator's Git branch, or through a `Merge PR #<n>` merge. A coordinator can adjust the change before it lands (inferred from `dcd6d4b8` and `7b7c58af`):

| PR                                                 | Change                                                              | Work commit and merge  |
| -------------------------------------------------- | ------------------------------------------------------------------- | ---------------------- |
| [#49](https://github.com/HazAT/ultimate/pull/49)   | Keep `/bin` on the Tailscale fixture's `PATH` on macOS              | `8db6c877`, `e02d43d4` |
| [#54](https://github.com/HazAT/ultimate/pull/54)   | Send on Cmd or Ctrl and Enter on touch devices                      | `b5bf77b1`, `7ed415ab` |
| [#55](https://github.com/HazAT/ultimate/pull/55)   | A larger Send button on touch devices                               | `db9f1a8a`, `02025706` |
| [#56](https://github.com/HazAT/ultimate/pull/56)   | Clarify configured landing checks and push                          | `ce3f14f9`, `98e03e95` |
| [#57](https://github.com/HazAT/ultimate/pull/57)   | Let the supervisor coordinate a systemd shutdown                    | `eade452f`, `38cbbfa1` |
| [#58](https://github.com/HazAT/ultimate/pull/58)   | The pinned prompt asks only after its conversation is known         | `61f6f7c2`, `3b85ec12` |
| [#59](https://github.com/HazAT/ultimate/pull/59)   | Find Google Chrome and older Playwright Chromium on macOS           | `cb5d3d69`, `679139b1` |
| [#60](https://github.com/HazAT/ultimate/pull/60)   | Name the OS in the prompt's environment section                     | `4cfb00c9`, `94a1bd01` |
| [#61](https://github.com/HazAT/ultimate/pull/61)   | Compact by context window, not model name                           | `3d922572`, `ee46cf01` |
| [#62](https://github.com/HazAT/ultimate/pull/62)   | Let compaction summaries use the model's output limit               | `596530bf`, `3d043ec5` |
| [#63](https://github.com/HazAT/ultimate/pull/63)   | Show a notice when a background compaction fails                    | `c3d5a2ea`, `fd470822` |
| [#65](https://github.com/HazAT/ultimate/pull/65)   | Disable Claude Code CLI auto-memory by default                      | `0ac012e7`, `876d94b8` |
| [#69](https://github.com/HazAT/ultimate/pull/69)   | Let `disable` turn off outside extensions that claim the core tier  | `0b4c4a0e`, `d562c935` |
| [#70](https://github.com/HazAT/ultimate/pull/70)   | Fix the extension docs' commit watcher and host field list          | `a8fe54d2`, `89bcf4d5` |
| [#71](https://github.com/HazAT/ultimate/pull/71)   | Answer brings the question card to the top of the view              | `4f38f2ed`, `8ec0ace8` |
| [#72](https://github.com/HazAT/ultimate/pull/72)   | A question link opens at the question                               | `323c3987`, `aefd922e` |
| [#73](https://github.com/HazAT/ultimate/pull/73)   | Enable Chromium's sandbox by default                                | `dbe9bb50`, `b2dc3ad8` |
| [#74](https://github.com/HazAT/ultimate/pull/74)   | Refuse cross-site frames. `dcd6d4b8` keeps only `frame-ancestors`   | `751b5e44`, `34965f1e` |
| [#75](https://github.com/HazAT/ultimate/pull/75)   | Review checks a branch spec in the checkout that the diff runs in   | `755e0322`, `1fe2a2ab` |
| [#77](https://github.com/HazAT/ultimate/pull/77)   | Kill a disconnected browser, and prefer Playwright's Chromium       | `3fb5c2fc`, `590d8c85` |
| [#78](https://github.com/HazAT/ultimate/pull/78)   | A definition title names a standing agent in the UI                 | `b9fb3b92`, `86caab3b` |
| [#79](https://github.com/HazAT/ultimate/pull/79)   | Type tool enums explicitly for provider compatibility               | `657d4bf8`, `fcf7585d` |
| [#81](https://github.com/HazAT/ultimate/pull/81)   | The previews switcher becomes its own title-bar chip                | `c52bd430`, `5e13ceb5` |
| [#82](https://github.com/HazAT/ultimate/pull/82)   | `data-status`, `data-final`, and transcript theming hooks           | `6fd731a3`, `72228b8f` |
| [#86](https://github.com/HazAT/ultimate/pull/86)   | Add a security policy                                               | `c21f2d6d`, `14f33b52` |
| [#89](https://github.com/HazAT/ultimate/pull/89)   | Source frames fetch only the server's own bundle assets             | `93ba229b`, `8fe9f220` |
| [#90](https://github.com/HazAT/ultimate/pull/90)   | Keep the composer while standing agents load                        | `a34cd2e2`, `42944abd` |
| [#96](https://github.com/HazAT/ultimate/pull/96)   | An unset composer redirect keeps an outer one                       | `2e95cf67`, `8c475419` |
| [#97](https://github.com/HazAT/ultimate/pull/97)   | Explain context reminder thresholds. `7b7c58af` drops one paragraph | `0ce6d5e3`, `a69ff865` |
| [#98](https://github.com/HazAT/ultimate/pull/98)   | A temporary folder still being written does not fail a landing      | `c99fc625`, `e1174f0d` |
| [#99](https://github.com/HazAT/ultimate/pull/99)   | Explain why Fall asleep waits. `9310a6c0` drops its copy test       | `018698fd`, `afab39bf` |
| [#100](https://github.com/HazAT/ultimate/pull/100) | Keep warm honors long retention on the Anthropic API                | `526412e5`, `656d94a0` |
| [#102](https://github.com/HazAT/ultimate/pull/102) | Catch up on the target's first-parent history                       | `29b5223d`, `8a837f2d` |
| [#103](https://github.com/HazAT/ultimate/pull/103) | A side chat whose ending faulted can be injected or discarded again | `f46c0050`, `f3b77382` |
| [#104](https://github.com/HazAT/ultimate/pull/104) | Raise the dual-stack connection timeout at startup                  | `630b6940`, `3c3be6f2` |
| [#106](https://github.com/HazAT/ultimate/pull/106) | The README uses `pnpm add -g .`                                     | `baeece3d`, `e96060a4` |
| [#108](https://github.com/HazAT/ultimate/pull/108) | A later chapter keeps its scripts in its own folder                 | `db1d8d12`, `9d77dced` |
| [#109](https://github.com/HazAT/ultimate/pull/109) | A conversation can send a message after its workspace is gone       | `01d0a9ed`, `42a7887b` |
| [#111](https://github.com/HazAT/ultimate/pull/111) | A user's answer names the card that it answers                      | `8e944092`, `f4114394` |
| [#113](https://github.com/HazAT/ultimate/pull/113) | Retry a Claude Code turn relay request that fails in transport      | `dd691fc1`, `af2ec01a` |
| [#114](https://github.com/HazAT/ultimate/pull/114) | Read the reading column's width from `--reading-width`              | `ed78db68`, `96a46517` |
| [#115](https://github.com/HazAT/ultimate/pull/115) | Show "awaiting @ultimate" apart from "waits on you"                 | `d61b2757`, `5a724fde` |
| [#116](https://github.com/HazAT/ultimate/pull/116) | A person's own families apply over the project's team settings      | `885ee383`, `a57641c6` |
| [#117](https://github.com/HazAT/ultimate/pull/117) | Inline code renderers for Markdown                                  | `c8cb825d`, `d3909db6` |

Other numbers from #49 to #117 have no merge in the November 9 sync's history.

### The November 11 sync

The November 11 sync adds 49 commits to this era. Upstream wrote all of them on 2026-11-09 and 2026-11-10. These are the main changes:

- Added:
  - the Inbox, a surface that lists each item that waits on the user, oldest first, with its answer card in place (`995c52d4`, [B12](bricks/B12-human-in-the-loop.md))
  - `panelBadges` and `Rendered` in the web SDK. An extension can put a badge on any panel tab and draw a part of the UI of another extension again (`a99235ce`, `8d09848d`, [B03](bricks/B03-reloadable-extensions.md))
  - `TodosApi.add` and an optional idempotency key on `todos/add` (`a9d47b01`, [B12](bricks/B12-human-in-the-loop.md))
- Reworked:
  - the model that the user selects in Get ready becomes the model of the default family, so new conversations and branches start on it (`fa9670c8`, [B04](bricks/B04-models-and-providers.md))
  - one default gives both the model and the thinking level. A provider that is not registered is not evidence of a missing login (`ba854f0e`, [D038](decisions/D038-models-follow-logins.md))
  - a conversation shows the family that it started on, not the first family with the same model (`f81d842b`, [B04](bricks/B04-models-and-providers.md))
  - a Pi Durable patch appends a new or returning prompt section. Before, Pi Durable sent the full system prompt again (`a5dea087`, [D026](decisions/D026-stable-system-prompt.md))
  - an open question to the user ranks above work in progress on the sidebar rows and on the phone button (`59136892`, `8bce83ea`, [B12](bricks/B12-human-in-the-loop.md))
  - the host signals a process group only for a pid that names a group, and pid files refuse pid 1 (`bf6830af`, `42ab5da0`, [B13](bricks/B13-background-work.md))
  - an onboarding start whose run failed before an answer can start again (`b59483eb`, `e77a4a21`, [B08](bricks/B08-ultimate-and-standing-agents.md))
- Removed: the idle lines that kept the plan, subagent, and automation prompt sections present. The Pi Durable patch makes them unnecessary (`a5dea087`)

### Outside contributions in the November 11 sync

`git log --merges --format='%h %s' 32e45c95..11c89136` lists the merges. Each work commit of these pull requests carries an `Ultimate-Conversation` trailer, such as `19583` on `a99235ce`. These trailers come from the instances of the contributors, not from the instance of upstream (inferred from the authors and the numbers):

| PR                                                 | Change                                                                               | Work commit and merge  |
| -------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------- |
| [#118](https://github.com/HazAT/ultimate/pull/118) | Keep the subagent and plan prompt sections present when idle. `a5dea087` replaces it | `7ef28f89`, `b6fe14c8` |
| [#119](https://github.com/HazAT/ultimate/pull/119) | Badges on any panel tab                                                              | `a99235ce`, `4d22556b` |
| [#123](https://github.com/HazAT/ultimate/pull/123) | A snapshot download that fails at once leaves no `.part` file                        | `6187f056`, `edc920d5` |
| [#124](https://github.com/HazAT/ultimate/pull/124) | `Rendered` lets an extension draw a part of the UI of another extension again        | `8d09848d`, `17fb9f3a` |

No merged pull request numbered 120 to 122 is present in this sync's history.

### The November 18 sync in era 10

The November 18 sync adds the commits of 2026-11-11 to 2026-11-13 to this era. These are the main changes:

- Added:
  - the projects rail, a switcher for each Ultimate that runs on this machine (`f5e963f1`, [B16](bricks/B16-remote-backup-update.md))
  - Voice moves the page, reads open questions, and answers them after a spoken read-back (`799df8e1`, [B12](bricks/B12-human-in-the-loop.md))
  - Inbox items from other extensions (`c497f99f`, [B12](bricks/B12-human-in-the-loop.md))
  - `ComposerPlaceholder` and `EmptyTranscript` in the web SDK (`f2f72298`, `8504f1e2`, [B03](bricks/B03-reloadable-extensions.md))
- Reworked:
  - Pi 1.5.2 (`3f11fcc2`, [B01](bricks/B01-durable-conversations.md))
  - an idle prompt section keeps an empty slot, so the Pi Durable patch hunk for returning sections goes (`568a20f6`, [D026](decisions/D026-stable-system-prompt.md))
  - @ultimate's final answer reaches each branch that its run read (`b015f0fa`, [B11](bricks/B11-notes-and-messages.md))
  - a 402 response is a billing limit, not a broken login (`446d54c6`, [B04](bricks/B04-models-and-providers.md))
  - the Git attribution hooks of `bash` apply only to their first worktree (`fe47d47f`, [B05](bricks/B05-agent-tools.md))
  - `instance start` takes a model for one start (`06c356c2`, [B10](bricks/B10-isolates-previews-lander.md))

### Era 11: Enforced rules

Upstream moves its rules for code into lint. `AGENTS.md` gets a table of each rule and the check that enforces it, and each lint message says why (`b4f0474f`). Product code loses its comments ([D045](decisions/D045-code-explains-itself.md)). Effects outside the store become durable tasks ([D002](decisions/D002-pi-durable-sqlite.md)). Outside pull requests continue to land each day ([table below](#outside-contributions-in-the-november-18-sync)).

- Added:
  - the lint rules `ultimate/no-raw-timer`, `ultimate/no-comments`, and `ultimate/no-unowned-work`, and a case for each member of a union in a switch (`b4f0474f`, `55136da8`, `24717b86`, `5d652bb5`, [D045](decisions/D045-code-explains-itself.md))
  - durable effect tasks, first for `tell` and pushes (`4dfe1142`, `47cfa17c`, [B01](bricks/B01-durable-conversations.md))
  - background process groups for `bash` (`5abd5a39`, [B05](bricks/B05-agent-tools.md))
  - wait labels on sidebar rows and System lanes (`900c96cc`, [B11](bricks/B11-notes-and-messages.md))
  - a skills list for each agent definition (`85b68619`, [B06](bricks/B06-project-specialization.md))
  - Read aloud (`e78fefa8`, [B12](bricks/B12-human-in-the-loop.md)) and box diagrams for `mermaid` blocks (`c23dd36a`, [B03](bricks/B03-reloadable-extensions.md))
  - the progress of acceptance criteria (`53e54861`, [B07](bricks/B07-conversation-tree.md))
  - user-level `modelFamilies` and Refresh model catalog (`db80d3fa`, `9a0d2931`, [B04](bricks/B04-models-and-providers.md))
  - the app name, the app icon, and the fixed port of a project (`b1012b4f`, [B06](bricks/B06-project-specialization.md))
- Reworked:
  - automations join the core tier, and the new `entries` extension holds shared entry kinds (`4601a36c`, [D024](decisions/D024-typed-contracts-core-tier.md))
  - standing agents can message the user (`400f5758`, [D044](decisions/D044-branches-ask-the-user.md))
  - the starter gets a one-line landing card, and @ultimate gets no commit catch-up (`cbc96a2c`, [B10](bricks/B10-isolates-previews-lander.md))
  - a supervised core ignores outside signals, and the Harness closes before the extensions (`4f2845dc`, `90d062f3`, [B02](bricks/B02-self-change-while-running.md))
  - discovery and project setup move from `server/` to `lib/` (`4c6ef265`)
- Removed:
  - the comments of product code, except contract documentation (`552d6164`, [D045](decisions/D045-code-explains-itself.md))
  - the landing distiller of project memory (`cd77dc1e`, [D029](decisions/D029-branches-start-from-memory.md))
  - the idle-branch note of the watchdog (`b5818c41`, [B09](bricks/B09-coordinators-and-subagents.md))
  - the `undici.install` call of the HTTP setup (`09c45130`, [B04](bricks/B04-models-and-providers.md))

### Outside contributions in the November 18 sync

`git log --merges --format='%h %s' 11c89136..6b6d88b6` lists the merges. Most land through a `Merge branch 'pr-<n>'` merge into a coordinator's Git branch, or through a `Merge PR #<n>` merge. A follow-up commit names the pull request when a coordinator changed it, such as `985124ae` for #220:

| PR                                                 | Change                                                                                                                   | Work commit and merge              |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| [#125](https://github.com/HazAT/ultimate/pull/125) | A repository too large to weigh never fails a landing                                                                    | `e4a143e3`, `defdaa1d`             |
| [#126](https://github.com/HazAT/ultimate/pull/126) | Pi packages 1.5.2                                                                                                        | `3f11fcc2`, `cee76831`             |
| [#128](https://github.com/HazAT/ultimate/pull/128) | The user adds a secret under a name of their choice                                                                      | `29f05387`, `19875c7b`             |
| [#129](https://github.com/HazAT/ultimate/pull/129) | The browser waits for a render before a screenshot                                                                       | `b9cc436c`, `500b5cc5`             |
| [#130](https://github.com/HazAT/ultimate/pull/130) | The status answers without the clone when Update fails                                                                   | `72bb1a1b`, `2ebef76e`             |
| [#131](https://github.com/HazAT/ultimate/pull/131) | Workers and coordinators run the project's own checks                                                                    | `8efec082`, `d5827505`             |
| [#132](https://github.com/HazAT/ultimate/pull/132) | Watcher script facts. `af4f768e` drops two of its rules                                                                  | `73937119`, `00c32708`             |
| [#133](https://github.com/HazAT/ultimate/pull/133) | Docs for message images and the preview assignment                                                                       | `633e307f`, `e8a114c4`             |
| [#136](https://github.com/HazAT/ultimate/pull/136) | `ComposerPlaceholder` in the web SDK                                                                                     | `f2f72298`, `dc526eea`             |
| [#137](https://github.com/HazAT/ultimate/pull/137) | `EmptyTranscript` in the web SDK                                                                                         | `8504f1e2`, `f8956108`             |
| [#139](https://github.com/HazAT/ultimate/pull/139) | An OpenAI API key login supplies the key of voice                                                                        | `fa24927a`, `3ff90d06`             |
| [#140](https://github.com/HazAT/ultimate/pull/140) | The e2e suite passes on macOS                                                                                            | `d7467267`, `cd98d8cb`             |
| [#141](https://github.com/HazAT/ultimate/pull/141) | Voice shows the reason when OpenAI refuses a live session                                                                | `3449a441`, `1bbbfb1b`             |
| [#143](https://github.com/HazAT/ultimate/pull/143) | An answer card keeps its picks                                                                                           | `63b8aaa7`, `76cf3d7f`, `46538c29` |
| [#144](https://github.com/HazAT/ultimate/pull/144) | The Inbox reading pane stays in the window                                                                               | `271ebeb2`, `22450e7f`             |
| [#145](https://github.com/HazAT/ultimate/pull/145) | Review reads a spec in the conversation's checkout                                                                       | `23d2f511`, `6d070f81`             |
| [#148](https://github.com/HazAT/ultimate/pull/148) | Long tokens fit a 375 px phone                                                                                           | `2370e5ef`, `b6da889f`             |
| [#149](https://github.com/HazAT/ultimate/pull/149) | The review of an unlanded range goes to the conversation of its head commit                                              | `00ce1f15`, `38f839af`             |
| [#150](https://github.com/HazAT/ultimate/pull/150) | A fork ignores the question pointers that it inherits                                                                    | `9ce056f4`, `df944f72`             |
| [#151](https://github.com/HazAT/ultimate/pull/151) | The standard meta tag for a mobile web app                                                                               | `bf0b7c3c`, `ca8d17f4`             |
| [#152](https://github.com/HazAT/ultimate/pull/152) | A 402 response is a billing limit                                                                                        | `446d54c6`, `d339a4ac`             |
| [#153](https://github.com/HazAT/ultimate/pull/153) | A short `timeoutMs` does not fail the browser launch                                                                     | `d029734b`, `2652a5b7`             |
| [#154](https://github.com/HazAT/ultimate/pull/154) | Load-dependent test failures fixed at their cause                                                                        | `f7e06eb2`, `affd5168`             |
| [#155](https://github.com/HazAT/ultimate/pull/155) | To-do rows show the id before the age                                                                                    | `be49ef49`, `67b618a6`             |
| [#160](https://github.com/HazAT/ultimate/pull/160) | Voice finishes replayed answers after a crash. `aaaf5b78` keeps one test                                                 | `46bdb0dd`, `a9f63d86`             |
| [#161](https://github.com/HazAT/ultimate/pull/161) | A definition is read inside the standing commit                                                                          | `865d214b`, `1b429071`             |
| [#162](https://github.com/HazAT/ultimate/pull/162) | Queued extension reloads stop when the server closes                                                                     | `8030aac9`, `a62cf90b`             |
| [#163](https://github.com/HazAT/ultimate/pull/163) | The projects rail uses the Tailscale port on tailnet pages                                                               | `5015bf60`, `b52d8eea`             |
| [#164](https://github.com/HazAT/ultimate/pull/164) | The Git hooks of `bash` apply only to their first worktree                                                               | `fe47d47f`, `5515c705`, `431ae46a` |
| [#169](https://github.com/HazAT/ultimate/pull/169) | Codemode respects model-only callers. `bd0fc71a` declares them                                                           | `c4b6f915`, `94c0a94c`             |
| [#170](https://github.com/HazAT/ultimate/pull/170) | The identity note after a compaction keeps the prompt cache                                                              | `d93c5527`, `0a8a21b7`             |
| [#171](https://github.com/HazAT/ultimate/pull/171) | A local narrator command                                                                                                 | `e8de47a0`, `54194398`             |
| [#172](https://github.com/HazAT/ultimate/pull/172) | The app name, the app icon, and the port of a project. `654ba01d` drops its comments                                     | `b1012b4f`, `d6522380`             |
| [#173](https://github.com/HazAT/ultimate/pull/173) | The fake model reads its command from each input                                                                         | `3b6fb3f2`, `c81f599a`             |
| [#175](https://github.com/HazAT/ultimate/pull/175) | The browser skips the driven mark in frames without storage                                                              | `746fa1ca`, `5ee16c53`             |
| [#176](https://github.com/HazAT/ultimate/pull/176) | A failed browser call names its error first                                                                              | `1974900a`, `1aed8a8b`             |
| [#177](https://github.com/HazAT/ultimate/pull/177) | A new chapter keeps the edited conditions of built-in triggers                                                           | `34dcbea1`, `bfa07f5c`             |
| [#178](https://github.com/HazAT/ultimate/pull/178) | Dream says that `learned` is an array of three strings                                                                   | `cbdecd26`, `6a34adc2`             |
| [#179](https://github.com/HazAT/ultimate/pull/179) | Setup warns while the project's `.ultimate/` is undecided                                                                | `a100d9ff`, `0818aa28`             |
| [#180](https://github.com/HazAT/ultimate/pull/180) | A setup card shows as settled when a decision comes from elsewhere                                                       | `439487f2`, `976f7fa5`             |
| [#183](https://github.com/HazAT/ultimate/pull/183) | The Inbox follows `--reading-width`                                                                                      | `051cf3cb`, `237ef39e`             |
| [#184](https://github.com/HazAT/ultimate/pull/184) | Watcher facts about `$AUTOMATION_STATE`. `07399ebb` drops two rules                                                      | `934c0817`, `ef16ed0c`, `c52a94e3` |
| [#185](https://github.com/HazAT/ultimate/pull/185) | The Inbox comes back to the last item that it showed                                                                     | `debca6f4`, `abf8acba`             |
| [#188](https://github.com/HazAT/ultimate/pull/188) | A badge after the title of a surface. `86030354` drops its comment                                                       | `7b2c18d8`, `3735a29e`             |
| [#196](https://github.com/HazAT/ultimate/pull/196) | The codemode test checks the automation of its own script                                                                | `8a951c93`, `694192a8`             |
| [#198](https://github.com/HazAT/ultimate/pull/198) | The browser waits for a selector, and a selector without a scope fails on several matches. `739cfda7` drops one sentence | `bdbdac57`, `aa4f4917`, `840ef687` |
| [#199](https://github.com/HazAT/ultimate/pull/199) | The `ultimate.tell` example parses                                                                                       | `6be5ec64`, `8ef5967d`             |
| [#201](https://github.com/HazAT/ultimate/pull/201) | On macOS, open the installed Chrome app                                                                                  | `0cb60feb`, `d52f70be`             |
| [#202](https://github.com/HazAT/ultimate/pull/202) | Previews with read-only copies or a deleted home stop. `cd5cb48f` drops a retry                                          | `c65112fb`, `b574e7a7`             |
| [#204](https://github.com/HazAT/ultimate/pull/204) | Dream says what a trace query returns                                                                                    | `e8035d0e`, `4cf82f54`             |
| [#206](https://github.com/HazAT/ultimate/pull/206) | A landing's weight counts only its diff                                                                                  | `e59a9873`, `8aa98fc9`             |
| [#207](https://github.com/HazAT/ultimate/pull/207) | The status carries the generation that the host serves                                                                   | `06bec5e5`, `fdf2642f`             |
| [#210](https://github.com/HazAT/ultimate/pull/210) | A parent's stop during a report keeps the child's status                                                                 | `569ccc43`, `c06febf1`             |
| [#211](https://github.com/HazAT/ultimate/pull/211) | Another project's answer stays when a post fails late                                                                    | `ceeaae56`, `e55fb6bd`             |
| [#214](https://github.com/HazAT/ultimate/pull/214) | The composer fits its width again when the width changes                                                                 | `32713af6`, `b7646f81`             |
| [#215](https://github.com/HazAT/ultimate/pull/215) | Markdown tables at full height                                                                                           | `ef24af5a`, `dd2fad70`             |
| [#216](https://github.com/HazAT/ultimate/pull/216) | A side-chat row clicked from another surface opens the main agent                                                        | `b86868de`, `ff91056f`             |
| [#218](https://github.com/HazAT/ultimate/pull/218) | The watchdog reports the failure of a tally to @ultimate. `29ffb55b` drops a re-export                                   | `df9719c9`, `f5d8c89f`             |
| [#219](https://github.com/HazAT/ultimate/pull/219) | The shown conversation's subscription ends when another shows                                                            | `1ccebc60`, `05d3072c`             |
| [#220](https://github.com/HazAT/ultimate/pull/220) | Skipped fires do not count toward the hourly cap. `985124ae` drops `maxFiresPerHour`                                     | `bc938b06`, `21aacad0`             |

Other numbers from #125 to #220 have no merge in this sync's history.

## Life of a change unit

At the snapshot, a change unit reaches `main` in these steps:

1. @ultimate starts a coordinator branch with the `branch` tool (`extensions/messages/branch.ts`)
2. The workspaces extension makes an isolate on Git branch `ultimate/<hash>-<n>`. `<n>` is the conversation ID, and `<hash>` comes from the home path (`extensions/workspaces/workspaces.ts`)
3. A Git hook of the `bash` tool adds `Ultimate-Conversation: <n>` to a commit without that trailer (`df00cf20`, `extensions/coding-tools/server.ts`). Rewritten commits keep their existing attribution (`df00cf20`)
4. Workers commit in their isolates. The coordinator merges their Git branches and `main` into its own
5. The coordinator calls `workspace submit`. Code of the landing queue merges the tip, then runs checks from `.ultimate/settings.json`
6. The code fast-forwards the target and pushes it (`extensions/workspaces/lander.ts`)
7. The lander notes the submitter and concludes it unless work remains under way. Only a concluded branch wakes its starter ([D042](decisions/D042-model-free-landing.md))
8. Lineage records the landing in the tally. A concluded branch releases its eligible checkout (`extensions/lineage/server.ts`, `extensions/workspaces/workspaces.ts`)

The landing queue uses `git merge` defaults (`extensions/workspaces/lander.ts`). Git makes a landing merge only if it cannot fast-forward. Its message is `Merge <sha> from #<n> into main` (`extensions/workspaces/lander.ts`). Since `9a79b7f9`, the message also carries the trailer `Ultimate-Conversation: <n>`, so the catch-up can label the merge.

The 312 landing merges with `#<n>` name 305 conversations (`git log --merges --format=%s 6b6d88b6`). Of these conversations, 245 appear in the work trailers, and the other 60 do not (`git log --no-merges --format='%(trailers:key=Ultimate-Conversation,valueonly)' 6b6d88b6`). Their landings contain work from other conversations, as `0eb16c0` shows below. The other units reached `main` by a fast-forward or through another unit, given those merge subjects and trailers (inferred).

Landings and their commit trailers can name different conversations. `0eb16c0` names `#209732`. Its commit `8c44921` has trailer `216060`.

### Commit shapes

`git log --merges --format=%s 6b6d88b6` shows 726 merges in six shapes:

| Shape                         | Subject                                       | Merges |
| ----------------------------- | --------------------------------------------- | -----: |
| Landing merge                 | `Merge <sha> from #<n> into main`             |    312 |
| Landing merge, old name       | `Merge <sha> from W<n> into main`             |     15 |
| Merge of `main` into a branch | `Merge branch 'main' into ultimate/...`       |    120 |
| Merge of a child              | `Merge branch 'ultimate/<hash>-<m>' into ...` |     84 |
| Merge by hand                 | `chore(integration): ...`                     |     24 |
| Other                         | Free text                                     |    171 |

The row for merges of `main` also counts subjects that start with `Merge main`, and remote-tracking merges of `origin/main` or `coord/main`. Of the 327 landing merges of both shapes, 226 have no trailer (`git log --merges --format='%s %(trailers:key=Ultimate-Conversation,valueonly)' 6b6d88b6`). The other 101 carry trailers. Five name conversation 30726, including conflict repair in `23f26ba` (inferred from its body). Two name conversation 377718. The 94 landing merges after `9a79b7f9` name their own conversation. The Other row includes pull request merges and merges of `pr-*` or satellite branches. Its share of all merges grew most in the November 9 sync, from 11.8 to 17.7 percent (53 of 448, then 98 of 553), because outside pull requests land through such merges ([Era 10](#era-10-outside-contributions)). At `11c89136`, the share was 17.9 percent (102 of 570). At `6b6d88b6`, it is 23.6 percent (171 of 726), because the November 18 sync lands 60 outside pull requests. The six shapes partition all merges, as the command below checks.

### Reproduce the merge shapes

These patterns are disjoint. The remaining subjects are Other:

```sh
git log --merges --format=%s 6b6d88b6 | awk '
	/^Merge [0-9a-f]+ from #[0-9]+ into main$/ { landing++; next }
	/^Merge [0-9a-f]+ from W[0-9]+ into main$/ { old++; next }
	/^Merge branch '\''main'\''/ || /^Merge main/ ||
	/^Merge remote-tracking branch '\''(origin|coord)\/main'\''/ { main++; next }
	/^Merge branch '\''ultimate\// { child++; next }
	/^chore\(integration\):/ { manual++; next }
	{ other++ }
	END { print landing, old, main, child, manual, other }
'
```

Output: `312 15 120 84 24 171`.

### How the process changed

- Eras 1 and 2: each commit went to `main` directly. No merge predates 2026-10-12
- Era 3: on 2026-10-12, 20 `chore(integration)` merges, such as `d37887a`, put work on `main`. Git does not show which agent made them. The landing queue began on 2026-10-13 (`5c36dcd`). `1d94cbc6` is the first landing merge, and it names `W25966`
- Era 4: `2166faa` is the first work commit with a trailer, on 2026-10-14. `19f960d` changed the label `W<n>` to `#<n>`, and `930d33e` is the first `#<n>` landing merge. 32 work commits on 2026-10-14 and 2026-10-15 have no trailer
- Eras 5 to 11: 42 work commits have no trailer (`git log --no-merges --format='%ad %h %(trailers:key=Ultimate-Conversation,valueonly)' --date=short 6b6d88b6`). The exceptions to 2026-11-01 are `ce2d46ab`, `d3c39fd`, `d0afb3e1`, `61b25245`, `2affc7ad`, `61a3f990`, `73d018f4`, `7849a479`, `b2b46f1c`, `741ec0da`, `81a29ea1`, `5edd9810`, `fc77dee5`, `5b4de93a`, and `751b5e44`. The November 9 sync adds `dbe9bb50`, `c21f2d6d`, `c99fc625`, `526412e5`, `29b5223d`, `f46c0050`, and `baeece3d`. All of them come from outside pull requests (inferred from the [table](#outside-contributions-in-the-november-9-sync)). The November 18 sync adds 20 more, all from outside pull requests: `e4a143e3`, `e59a9873`, `23d2f511`, `46bdb0dd`, `865d214b`, `8030aac9`, `5015bf60`, `c4b6f915`, `3b6fb3f2`, `439487f2`, `051cf3cb`, `ef16ed0c`, `934c0817`, `debca6f4`, `7b2c18d8`, `8a951c93`, `e8035d0e`, `06bec5e5`, `569ccc43`, and `ceeaae56` ([table](#outside-contributions-in-the-november-18-sync)). @ultimate starts branches (`c685a27`)
- Era 10: since `9a79b7f9` on 2026-11-07, each landing merge carries the trailer of its conversation. Outside pull requests reach a coordinator's Git branch through `Merge branch 'pr-<n>'` or `Merge PR #<n>`, and then land through the queue (inferred from `fcf7585d` and `9d77dced`)

### Find the commits of one conversation

Use these commands in a clone of uao:

- Work commits: `git log --grep='^Ultimate-Conversation: <n>$'`
- Landing merges: `git log --grep='from #<n> into main'`. Before 2026-10-14, search for `from W<n>`
- Merges into its Git branch: `git log --grep='ultimate/[0-9a-f]*-<n>'`
- Conversation of a commit: `git log -1 --format='%(trailers:key=Ultimate-Conversation)' <sha>`

Change unit 59981 has both landing shapes. Landing merge `a03d554` put its first commit on `main`, on 2026-10-15. Then `1283047` merged `main` into the unit's Git branch. Next, `550c478` landed by fast-forward (inferred).

## How the rules and the team changed

Up to era 5, most rule changes went to `AGENTS.md`. After era 5, most went to the agent definitions. `git log --no-merges --format=%ad --date=short 6b6d88b6 -- <path>` gives these counts:

| Path                              |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |  10 |  11 |
| --------------------------------- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| `AGENTS.md`                       |  21 |  12 |  21 |  29 |  23 |   4 |   7 |   9 |  13 |   5 |   5 |
| `agents/` and `.ultimate/agents/` |   3 |   0 |   7 |   9 |  22 |  12 |  21 |  38 |  32 |  14 |  12 |

Behavior rules live in prompts ([Principle 11](principles.md), `6b8477d`). These are the main changes:

- Era 1: `a300225` adds the scout, researcher, reviewer, and worker on the parent's model. `7a62d92` gives the coordinator the final verdict
- Era 3: `1772c50` adds the review quality rules and a review team with pinned models
- Era 4: `ef88374` adds the lander definition. `a8fbf6e` removes the mandatory review team. `8be9fec` holds small UI polish until user approval
- Era 5: `c685a27` adds @ultimate. `a410963` adds the coordinator. `e7a77ac` moves details to `docs/`, cutting `AGENTS.md` from 234 lines to 101. `30af13a` and `9d455ec` add @cloudflare and @sync
- Era 6: `9d764b6` names reviewers by their checks. `44bc478` removes @cloudflare
- Era 7: `63da866` restores the scout, adds the designer, and pins the worker to GPT-6.1 Sol
- Era 8: `556eb4c` keeps previews with the coordinator. `2f68182` lets @ultimate restart after core landings without asking. `8883ef7` sets Claude Code Opus 5.5 in the project coordinator definition. `8ff34aa` makes `branch` apply that model. `ce2d46ab` temporarily sets OpenRouter models, and `50930ec` restores the Claude Code and Codex models. `bc3a786` moves procedures into skills and removes the coordinator's check before submission. `1c8a97e` tells agents to reuse passed tests on an unchanged tree
- Also in era 8: `a7495cb` tells coordinators to continue unless a child, the lander, or a reply will wake them. `001a193d` lets @ultimate approve work during a hands-off goal ([D037](decisions/D037-goals-delegate-approvals.md)). `d3178ff` removes `workspace` from the project lander overlay
- Era 9: `465cf344` makes project and personal additions the preferred contribution path. `3b711c55` requires decision sources and conclusion of terminal branches. `be1608a7` moves the dream process into instructions. `cfd0e93b` removes the lander definitions and assigns failure repair to the submitter
- Also in era 9: `741ec0da` replaces shipped model pins with families. `d6f3657a` commits project family assignments. `e34af09d` makes branches ask after @ultimate weighs in. `08d193b3` derives projects and agent models instead of storing them in memory. `b2f7043f` gives Sketch a model-only definition, and `17157665` adds standing agent marks. `e6909945` removes Sketch and its definition. `6b0fb859` lets a parent make a subagent without a definition file. `fb03c2c7` trims prompt and tool text that repeats itself
- Era 10: `924a0b0c` requires a comment that names the origin of workaround code. `c387c88b` puts each extension's tests in its own folder. `47c08a50` changes the layer table for the production web bundle. `729f493c` splits the extension guide into topic files. `995c52d4` tells @ultimate that open questions wait in the user's Inbox
- Era 11: `b4f0474f` replaces the origin comment of `924a0b0c` with a reason in the commit message and a regression test, and adds the rule table ([D045](decisions/D045-code-explains-itself.md)). `85b68619` and `3f1ca441` give definitions a skills list. `cd77dc1e` tells @ultimate to remember only what a branch would get wrong without it. `af4f768e`, `07399ebb`, and `739cfda7` keep the facts of outside pull requests and drop their new rules, because prompts carry facts, not rules for failures that did not occur

[Subagents](../subagents.md) describes the team at the snapshot. Families select agent and feature models ([D043](decisions/D043-model-families.md)). New conversations can keep a configured default without a login ([D038](decisions/D038-models-follow-logins.md)). [D036](decisions/D036-previews-on-instance-model.md) records the preview override.
