# Upstream

This file says how uao relates to `HazAT/ultimate`: the snapshot, the fork point, the differences, what still points at HazAT, and the sync rule.

## Snapshot

Each status in the north-star is true at the snapshot:

- Upstream: `HazAT/ultimate` at `11c89136`, 2026-11-10 (author date)
- Fork: `pascalandy/uao` at `b3aef5f4`, 2026-11-11, the merge of this snapshot

`git log --oneline 11c89136..$(git merge-base HEAD upstream/main)` lists the upstream commits that the map does not cover. No output means the map is current. The command needs the `upstream` remote.

The [changelog review](changelog.md) compares the public entries with this snapshot and records later upstream changes. Read that review when you assess a sync. Later upstream entries do not change a brick's status until their code reaches uao.

### Sync log

- 2026-10-23: upstream `11d1d4c` (2026-10-24), merged into uao by `01a53cc`
- 2026-10-24: upstream `4aaa074` (2026-10-24), merged into uao by `342b1e2`
- 2026-10-29: upstream `17d186b` (2026-10-29), merged into uao by `58a9e05`
- 2026-11-01: upstream `d0a2e17b` (2026-11-01), merged into uao by `739d025c`
- 2026-11-09: upstream `32e45c95` (2026-11-10), merged into uao by `e683f686`, the first merge of the job `uao-sync`, run by hand before its first Wednesday
- 2026-11-11: upstream `11c89136` (2026-11-10), merged into uao by `b3aef5f4`, the first Wednesday run of the job `uao-sync`

## Fork point

uao forked from upstream `33c05e9` on 2026-10-23. Its first commit after the fork, `7698625`, adds one line to `README.md`. In Pascal's clone, the remote `origin` is `pascalandy/uao` and the remote `upstream` is `HazAT/ultimate` (local git configuration, not in the repository).

## Differences

- `README.md`: the line "`uao` stands for the Ultimate Agent Orchestrator." (`7698625`)
- `docs/north-star/` and the North star section of `AGENTS.md`: this map (`7779cce`, `49ee895`, [D033](decisions/D033-one-north-star.md))

`README.md` and `AGENTS.md` are the only upstream files that uao changes. These two changes are the current exceptions to the sync rule. Using places that upstream does not edit decreases the risk of a merge conflict. These places do not prevent all conflicts.

## What still points at HazAT

uao does not change these files ([D034](decisions/D034-follow-upstream.md)). Read each pointer with its meaning in uao:

- [Push permission](../../AGENTS.md#push-permission) and `docs/worktrees.md` name `origin` as `HazAT/ultimate`. In uao, `origin` is `pascalandy/uao`
- `extensions/cloud/README.md` still places the backup Worker in `HazAT/ultimate-fleet`. The Worker code remains absent, so uao needs its own Worker for backups (inferred from `67caeb6` and `extensions/cloud/README.md`)
- `README.md` and the [explainer](sources/explainer-page.md) give a setup prompt for `HazAT/ultimate` (`4c4b02f1`). A uao setup must use `pascalandy/uao` instead (inferred from the remotes)
- `CONTRIBUTING.md` and `extensions/dream/DREAM.md` search `HazAT/ultimate` for feature reference PRs (`465cf344`). The contribution policy now accepts selected core improvements ([D016](decisions/D016-personal-project.md))
- `extensions/update/` compares the clone with `origin`. In uao, the extension follows `pascalandy/uao` (inferred from `extensions/update/README.md` and the remotes)
- `.ultimate/settings.json` sets `"push": "origin"`, so the lander pushes to `pascalandy/uao` (inferred from the remotes)
- `README.md` tells a fork to paste the changelog's follow prompt into @ultimate (`c19ee333`). uao does not need that prompt, because it merges upstream each week ([D034](decisions/D034-follow-upstream.md))
- `lib/schema.ts` and `server/http.ts` cite `HazAT/ultimate` pull requests as the origin of workarounds (`91a29827`, `f16640f0`). The rule for such origin comments comes from `924a0b0c`. These links are history, not instructions

The old machine-specific paths and user names in `docs/worktrees.md`, `docs/running.md`, and `extensions/pause/README.md` are gone (`eb5b61d2`). `AGENTS.md` no longer advertises the private backup Worker (`55544315`).

## Sync rule

The job `uao-sync` merges `upstream/main` into uao each Wednesday through a pull request. The job runs the checks and its two review loops, then merges the pull request without Pascal ([D034](decisions/D034-follow-upstream.md)). To undo one sync, run `git revert -m 1 <merge>` on a branch, and merge that revert through a pull request. The sync pull request lands with a merge commit, never with a squash or a rebase (Pascal, 2026-10-24). A squash or a rebase replaces the upstream commits with new commits, so `check_links.py` rejects the upstream SHAs that the north-star cites. uao keeps its own additions in places that upstream does not edit: `docs/north-star/`, new files in `.ultimate/`, and `~/.ultimate/`.

After each merge:

1. Run `python3 docs/north-star/check_links.py` and the other checks in [How a change lands](dev-preferences.md#how-a-change-lands)
2. Check each brick status, and each item of [Known drift in upstream docs](#known-drift-in-upstream-docs), against the new code
3. Update the bricks and the decisions that changed
4. Only when the merge changes a principle, a brick's status, or a decision's rule, add a decision
5. Add the new commits to [history.md](history.md)
6. Update the counts in [evolution.md](evolution.md)
7. Update the [snapshot](#snapshot)

## Known drift in upstream docs

These upstream texts disagree with the code at the snapshot. uao records these disagreements and does not fix the upstream texts:

- `AGENTS.md` calls a project "a forest of conversation trees", and it also says "A project has one root" (`86ed900`)
- `AGENTS.md` says "Roots run no turns". A root becomes a tally and refuses turns only when its first branch starts (`extensions/lineage/server.ts`, [D015](decisions/D015-root-is-a-tally.md))
- `extensions/README.md` says that `lib/` "holds no state", but `lib/chapters.ts` reads SQLite and writes journal files
- `extensions/models/README.md` still describes model selection for the lander. The lander runs no model (`cfd0e93b`, `extensions/workspaces/lander.ts`). That README also says that new conversations avoid defaults without a login. The code preserves a configured default when no configured choice has a login (`4497cb74`, `lib/agents.ts`)
- `extensions/instance/README.md` gives one fixed default preview model. The preview uses its assigned family when no model pin is set (`741ec0da`, `extensions/instance/server.ts`)
- `extensions/workspaces/README.md` says that the starter wakes after each landing, also when the branch still has work under way. The code wakes the starter only for a concluded branch, and otherwise writes the report as a note (`extensions/workspaces/lander.ts`)
- `docs/settings.md` says Update checks hourly. The timer compares every five minutes; only fetches have an hourly gate (`extensions/update/server.ts`, `extensions/update/README.md`)
- `extensions/onboarding/README.md` lists seven default-off built-ins. `defaultOff` has ten: it adds `voice-live`, `push`, and `wire` (`ab959a36`, `ff44988c`, `c16450c9`, `shared/extension-api.ts`)

The old pinned-model list is fixed in `docs/subagents.md`. Shipped definitions now name families (`741ec0da`, `b2f7043f`). The event-history description in [Events](../extensions/events.md) does not claim exclusivity, so event triggers do not contradict it (`a7f32b5`). The README now says that some built-ins start off, so it agrees with [D031](decisions/D031-resource-built-ins-off.md) (`464697b3`).

The former health-backup claim is fixed in settings and health docs (`f6a7d570`, `e766c96e`). The former mismatch around automation `act` is gone because grants and `act` were removed (`ef738270`).
