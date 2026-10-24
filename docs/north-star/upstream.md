# Upstream

This file says how uao relates to `HazAT/ultimate`: the snapshot, the fork point, the differences, what still points at HazAT, and the sync rule.

## Snapshot

Each status in the north-star is true at the snapshot:

- Upstream: `HazAT/ultimate` at `11d1d4c`, 2026-10-24
- Fork: `pascalandy/uao` at `01a53cc`, 2026-10-23, the merge of this snapshot

`git log --oneline 11d1d4c..$(git merge-base HEAD upstream/main)` lists the upstream commits that the map does not cover. No output means the map is current. The command needs the `upstream` remote.

### Sync log

- 2026-10-23: upstream `11d1d4c` (2026-10-24), merged into uao by `01a53cc`

## Fork point

uao forked from upstream `33c05e9` on 2026-10-23. Its first commit after the fork, `7698625`, adds one line to `README.md`. In Pascal's clone, the remote `origin` is `pascalandy/uao` and the remote `upstream` is `HazAT/ultimate` (local git configuration, not in the repository).

## Differences

- `README.md`: the line "`uao` stands for the Ultimate Agent Orchestrator." (`7698625`)
- `docs/north-star/` and the North star section of `AGENTS.md`: this map (`7779cce`, `49ee895`, [D033](decisions/D033-one-north-star.md))

`README.md` and `AGENTS.md` are the only upstream files that uao changes. These two changes are the current exceptions to the sync rule. Using places that upstream does not edit decreases the risk of a merge conflict. These places do not prevent all conflicts.

## What still points at HazAT

uao does not change these files ([D034](decisions/D034-follow-upstream.md)). Read each pointer with its meaning in uao:

- [Push permission](../../AGENTS.md#push-permission) and `docs/worktrees.md` name `origin` as `HazAT/ultimate`. In uao, `origin` is `pascalandy/uao`
- `docs/worktrees.md` gives an example path under `/home/haza/`, the home folder of Daniel's machine
- `AGENTS.md` and `extensions/cloud/README.md` place the backup Worker in the private repository `HazAT/ultimate-fleet`. The Worker code is absent from this repository (`67caeb6`), so a backup from uao needs a Worker that uao does not ship (inferred)
- `docs/running.md` says that a scratch server is "for Daniel to open remotely"
- `extensions/pause/README.md` gives Daniel's wish as the reason why a pause after a rate limit does not end by itself
- `CONTRIBUTING.md` keeps the upstream policy: a personal project, with no review of issues or pull requests
- `extensions/update/` compares the clone with `origin`. In uao, the extension follows `pascalandy/uao`, not upstream (inferred from `extensions/update/README.md` and the remotes)
- `.ultimate/settings.json` sets `"push": "origin"`, so the lander pushes to `pascalandy/uao` (inferred from the remotes)

## Sync rule

Pascal merges `upstream/main` when he wants its changes ([D034](decisions/D034-follow-upstream.md)). uao keeps its own additions in places that upstream does not edit: `docs/north-star/`, new files in `.ultimate/`, and `~/.ultimate/`.

After each merge:

1. Run `python3 docs/north-star/check_links.py` and the other checks in [How a change lands](dev-preferences.md#how-a-change-lands)
2. Check each brick status, and each item of [Known drift in upstream docs](#known-drift-in-upstream-docs), against the new code
3. Update the bricks and the decisions that changed
4. Only when the merge changes a principle, the status of a brick, or the rule of a decision, add a decision
5. Add the new commits to [history.md](history.md)
6. Update the counts in [evolution.md](evolution.md)
7. Update the [snapshot](#snapshot)

## Known drift in upstream docs

These upstream texts disagree with the code at the snapshot. uao records these disagreements and does not fix the upstream texts:

- The README says that every built-in is on by default, but some built-ins are off by default ([D031](decisions/D031-resource-built-ins-off.md))
- `AGENTS.md` calls a project "a forest of conversation trees", and it also says "A project has one root" (`86ed900`)
- `AGENTS.md` says "Roots run no turns". A root becomes a tally and refuses turns only when its first branch starts (`extensions/lineage/server.ts`, [D015](decisions/D015-root-is-a-tally.md))
- `extensions/README.md` says that `lib/` "holds no state", but `lib/chapters.ts` reads SQLite and writes journal files
- `docs/subagents.md` says that only `scout`, `worker`, and `designer` pin their models. `agents/watcher.md` and `agents/dream-pass.md` pin models too
- `docs/settings.md` says that `health` reports provider health with backups. `69a367a` stopped sending provider health with backups
- `extensions/automations/README.md` names `act` in its text, but its list of 14 tool operations omits it. The tool exposes `act` (`extensions/automations/server.ts`)
- `docs/extensions.md` says that `workspaces.check`, `health.changed`, `cloud.backup`, and `conversations.compacted` are recorded for the history and the system stream. The event triggers of automations also react to them (`extensions/automations/triggers.ts`, `a7f32b5`)
