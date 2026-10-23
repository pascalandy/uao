# B16 Remote access, backups, and updates

Status: shipped, at the snapshot. Source: upstream.

The user reaches a running Ultimate from another machine over Tailscale. A project backs up to the user's own backup Worker, and one command restores it on another machine. Each Ultimate shows the new commits on the origin of its clone and updates by fast-forward only.

## How it works

`tailscale` serves the UI over HTTPS to allowed logins only, and never turns on Funnel. Ultimate itself listens only on loopback (`docs/running.md`). `cloud` uploads encrypted snapshots, and `pnpm restore` installs one. `update` checks `origin` and refuses a dirty, diverged, or busy clone. The three extensions ship off. Each extension README holds its mechanics.

## Where it lives

- `extensions/tailscale/`: remote access
- `extensions/cloud/`: backups
- `scripts/restore.ts`: the restore command
- `extensions/update/`: updates
- `lib/fast-forward.ts`: fetch and fast-forward

## Decisions

- [D028](../decisions/D028-cloud-only-backs-up.md) Use the cloud only for backups
- [D031](../decisions/D031-resource-built-ins-off.md) Ship resource-needing built-ins off

## Next

- Nothing stated

## Evidence

- `a5adb0f` adds owner-only Tailscale access
- `67caeb6` adds backups and `pnpm restore`
- `a8fba5e` adds updates
- `8ede22b` guards updates
