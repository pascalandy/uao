# D028 Use the cloud only for backups

Decided 2026-10-21. Source: upstream. Status: active.

Conversations stay on the machine that runs the project. The `cloud` extension only creates backups of a project on the user's own backup Worker. `pnpm restore` installs a backup on another machine.

**Why.** The commit gives no reason (`67caeb6`). The post states the aim: "I don't want to lose any conversation". A restore takes "a single command" (section "The Small Things").

**Rejected.** A Cloudflare copy of the conversations that served them while the machine was off (`8b5d5ac`, removed by `c9cc95e`). A writer lease, project moves, and the @sync agent (`d8f80cb`, `9d455ec`, removed by `67caeb6`).

**Evidence.** `c9cc95e` and `67caeb6`. `extensions/cloud/README.md` holds the mechanics.
