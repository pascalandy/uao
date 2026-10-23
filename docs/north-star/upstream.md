# Upstream

This file says how uao relates to `HazAT/ultimate`: the fork point, the differences, what still points at HazAT, and the sync rule.

## Fork point

At the snapshot, uao is upstream `33c05e9` plus one commit, `7698625`, which adds one line to `README.md`. In Pascal's clone, the remote `origin` is `pascalandy/uao` and the remote `upstream` is `HazAT/ultimate` (local git configuration, not in the repository).

## Differences

- `README.md`: the line "`uao` stands for the Ultimate Agent Orchestrator." (`7698625`)
- `docs/north-star/` and one line in `AGENTS.md`: this map ([D033](decisions/D033-one-north-star.md))

`README.md` and `AGENTS.md` are the only upstream files that uao changes. A merge can conflict only in these two files today.

## What still points at HazAT

uao does not change these files ([D034](decisions/D034-follow-upstream.md)). Read each pointer with its meaning in uao:

- [Push permission](../../AGENTS.md#push-permission) and `docs/worktrees.md` name `origin` as `HazAT/ultimate`. In uao, `origin` is `pascalandy/uao`
- `docs/worktrees.md` gives an example path under `/home/haza/`, the home folder of Daniel's machine
- `AGENTS.md`, `agents/ultimate.md`, and `extensions/cloud/README.md` say that the backup Worker lives in the private repository `HazAT/ultimate-fleet`. The Worker code is not in this repository (`67caeb6`), so a backup from uao needs a Worker that uao does not ship (inferred)
- `docs/running.md` says that a scratch server is "for Daniel to open remotely"
- `extensions/update/` compares the clone with `origin`. In uao, it follows `pascalandy/uao`, not upstream (inferred from `extensions/update/README.md` and the remotes)
- `.ultimate/settings.json` sets `"push": "origin"`, so the lander pushes to `pascalandy/uao` (inferred from the remotes)

## Sync rule

Pascal merges `upstream/main` when he wants its changes ([D034](decisions/D034-follow-upstream.md)). uao keeps its own additions in places that upstream does not edit: `docs/north-star/`, new files in `.ultimate/`, and `~/.ultimate/`.

After each merge:

1. Run `pnpm check` and the tests
2. Check each brick status against the new code
3. Update the bricks and the decisions that changed
4. Add the new upstream decisions in date order
5. Move the snapshot in [README.md](README.md#snapshot)

## Known drift in upstream docs

These upstream texts disagree with the code at the snapshot. uao records them and does not fix them:

- The README says that every built-in is on by default. `5323967` ships eight built-ins off (`shared/extension-api.ts`)
- `AGENTS.md` calls a project "a forest of conversation trees", and it also says "A project has one root" (`86ed900`)
- `extensions/README.md` says that `lib/` "holds no state", but `lib/chapters.ts` reads SQLite and writes journal files
