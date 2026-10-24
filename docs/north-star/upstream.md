# Upstream

This file says how uao relates to `HazAT/ultimate`: the snapshot, the fork point, the differences, what still points at HazAT, and the sync rule.

## Snapshot

Each status in the north-star is true at the snapshot:

- Upstream: `HazAT/ultimate` at `33c05e9`, 2026-10-23
- Fork: `pascalandy/uao` at `7698625`, 2026-10-23

`git log --oneline 33c05e9..$(git merge-base HEAD upstream/main)` lists the upstream commits that the map does not cover. No output means the map is current. The command needs the `upstream` remote.

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
- `AGENTS.md`, `agents/ultimate.md`, and `extensions/cloud/README.md` say that the backup Worker lives in the private repository `HazAT/ultimate-fleet`. The Worker code is not in this repository (`67caeb6`), so a backup from uao needs a Worker that uao does not ship (inferred)
- `docs/running.md` says that a scratch server is "for Daniel to open remotely"
- `CONTRIBUTING.md` keeps the upstream policy: a personal project, with no review of issues or pull requests
- `extensions/update/` compares the clone with `origin`. In uao, the extension follows `pascalandy/uao`, not upstream (inferred from `extensions/update/README.md` and the remotes)
- `.ultimate/settings.json` sets `"push": "origin"`, so the lander pushes to `pascalandy/uao` (inferred from the remotes)

## Sync rule

Pascal merges `upstream/main` when he wants its changes ([D034](decisions/D034-follow-upstream.md)). uao keeps its own additions in places that upstream does not edit: `docs/north-star/`, new files in `.ultimate/`, and `~/.ultimate/`.

After each merge:

1. Run `python3 docs/north-star/check_links.py` and the other checks in [How a change lands](dev-preferences.md#how-a-change-lands)
2. Check each brick status, and each item of [Known drift in upstream docs](#known-drift-in-upstream-docs), against the new code
3. Update the bricks and the decisions that changed
4. Only when the merge changes a principle or the status of a brick, add a decision
5. Add the new commits to [history.md](history.md)
6. Update the counts in [evolution.md](evolution.md)
7. Update the [snapshot](#snapshot)

## Known drift in upstream docs

These upstream texts disagree with the code at the snapshot. uao records these disagreements and does not fix the upstream texts:

- The README says that every built-in is on by default, but some built-ins are off by default ([D031](decisions/D031-resource-built-ins-off.md))
- `AGENTS.md` calls a project "a forest of conversation trees", and it also says "A project has one root" (`86ed900`)
- `extensions/README.md` says that `lib/` "holds no state", but `lib/chapters.ts` reads SQLite and writes journal files
- `docs/subagents.md` says that only `scout`, `worker`, and `designer` pin their models. `agents/subscription.md` and `agents/dream-pass.md` pin models too
- `.ultimate/agents/coordinator.md` sets Claude Code Opus 5.5 for coordinators (`8883ef7`). The `branch` tool applies only the instructions of the definition, so a coordinator keeps the model of @ultimate (`extensions/messages/server.ts:1374`)
- `docs/settings.md` says that `health` reports provider health with backups. `69a367a` stopped sending provider health with backups
