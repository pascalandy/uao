# B16 Remote access, backups, and updates

Status: shipped, at the snapshot. Source: upstream.

The user reaches a running Ultimate from another machine over Tailscale. A project backs up to the user's own backup Worker, and one command restores it on another machine. A backup needs that Worker, which uao does not ship ([upstream.md](../upstream.md#what-still-points-at-hazat)). Each Ultimate shows the new commits on the origin of its clone and updates by fast-forward only.

## Where it lives

- `extensions/tailscale/`: remote access
- `extensions/cloud/`: backups
- `scripts/restore.ts`: the restore command
- `extensions/update/`: updates
- `lib/fast-forward.ts`: fetch and fast-forward

## Decisions

- [D028](../decisions/D028-cloud-only-backs-up.md) Use the cloud only for backups
- [D031](../decisions/D031-resource-built-ins-off.md) Ship resource-needing built-ins off

## Evidence

- `a5adb0f` adds owner-only Tailscale access
- `67caeb6` adds backups and `pnpm restore`
- `a8fba5e` adds updates
- `8ede22b` guards updates
