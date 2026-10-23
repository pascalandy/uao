# B18 Cloud fleet

Status: dropped, at the snapshot. Source: upstream.

The cloud fleet kept a project reachable while its machine was off, and it moved a project between machines. The [first prompt](../sources/first-prompt.md) asked to keep the door open for Cloudflare. Ultimate built the fleet on Cloudflare, removed it, and kept only backups.

## How it works

First, a Cloudflare replica served a copy of each conversation (`8b5d5ac`). Later, a writer lease named the one machine that could write, and a standing agent, @sync, moved projects (`d8f80cb`, `9d455ec`).

## Where it lives

- Nothing on main. The backup Worker lives in the private repository `HazAT/ultimate-fleet` (`extensions/cloud/README.md`)

## Decisions

- [D028](../decisions/D028-cloud-only-backs-up.md) Use the cloud only for backups

## Next

- Nothing stated

## Evidence

- `8b5d5ac` syncs conversations to a replica
- `d8f80cb` adds the writer lease
- `9d455ec` adds @sync
- `c9cc95e` removes the conversation copy
- `67caeb6` removes the lease and @sync
