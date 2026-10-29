# B16 Remote access, backups, and updates

Status: shipped, at the snapshot. Source: upstream.

The user reaches a running Ultimate over Tailscale (`extensions/tailscale/README.md`). Remotes in user settings locate other machines' instances without cloud backups (`2a6d9e51`). Remote reads and `tell` can select a machine (`197a3e3f`, `extensions/codemode/README.md`).

A project can back up to the user's backup Worker and restore on another machine ([D028](../decisions/D028-cloud-only-backs-up.md)). uao does not ship that Worker ([upstream.md](../upstream.md#what-still-points-at-hazat)). A satellite refuses every backup, including forced backups, to protect the owner's history (`2bfc6b22`).

Update ships on by default and follows the clone's origin (`7f011b47`). Its direct update remains fast-forward only (`extensions/update/README.md`). When clone and project are the same repository, the user can ask @ultimate to merge a diverged origin through a coordinator branch (`7f011b47`, `extensions/update/README.md`).

Agents can start backups and clone updates through actions (`extensions/cloud/server.ts`, `extensions/update/server.ts`). The cloud join action remains user-only (`extensions/cloud/server.ts`).

## Where it lives

- `extensions/tailscale/`: remote access
- `extensions/cloud/`: backups
- `scripts/restore.ts`: the restore command
- `extensions/update/`: updates
- `lib/fast-forward.ts`: fetch and fast-forward
- `lib/remote.ts`: local instances, user remotes, then the optional cloud register

## Decisions

- [D028](../decisions/D028-cloud-only-backs-up.md) Use the cloud only for backups
- [D031](../decisions/D031-resource-built-ins-off.md) Disable by default the built-ins that need resources

## Evidence

- `a5adb0f` adds owner-only Tailscale access
- `67caeb6` adds backups and `pnpm restore`
- `a8fba5e` adds updates
- `8ede22b` guards updates
- `d3178ff` opens the backup and update actions to agents
- `68297d00` gives scratch servers separate Tailscale registrations and repairs a lost mapping
- `5c83c82f` keeps Tailscale teardown alive during a systemd stop
- `7849a479` prints the remote URL when Tailscale registers or removes it
