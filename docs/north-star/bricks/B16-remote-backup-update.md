# B16 Remote access, backups, and updates

Status: shipped, at the snapshot. Source: upstream.

The user reaches a running Ultimate from another machine over Tailscale. A project backs up to the user's own backup Worker. One command restores the project on another machine. A backup needs that Worker, which uao does not ship ([upstream.md](../upstream.md#what-still-points-at-hazat)). Each Ultimate instance shows the new commits on the origin of its clone. The instance updates by fast-forward only.

Agents can now start backups and clone updates through actions (`extensions/cloud/server.ts`, `extensions/update/server.ts`). The cloud join action remains user-only (`extensions/cloud/server.ts`).

## Where it lives

- `extensions/tailscale/`: remote access
- `extensions/cloud/`: backups
- `scripts/restore.ts`: the restore command
- `extensions/update/`: updates
- `lib/fast-forward.ts`: fetch and fast-forward

## Decisions

- [D028](../decisions/D028-cloud-only-backs-up.md) Use the cloud only for backups
- [D031](../decisions/D031-resource-built-ins-off.md) Disable by default the built-ins that need resources

## Evidence

- `a5adb0f` adds owner-only Tailscale access
- `67caeb6` adds backups and `pnpm restore`
- `a8fba5e` adds updates
- `8ede22b` guards updates
- `d3178ff` opens the backup and update actions to agents
