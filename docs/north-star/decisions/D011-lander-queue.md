# D011 Land through a durable queue

Decided 2026-10-13. Source: upstream. Status: active.

`workspace submit` puts a clean isolate tip in a queue. Code lands each submission in order. It merges, runs the configured checks, fast-forwards the target, and pushes without force. The lander's model works only when a step fails or a user messages it.

**Why.** Coordinators spent many turns to merge, check, land, and push. Also, `workspace land` often failed on a moved target or on an unrelated dirty file (`5c36dcd`).

**Rejected.** Synchronous `workspace land` as the default end of a branch. It stays as an alternative that never pushes (`docs/worktrees.md`).

**Evidence.** `5c36dcd` adds the queue. `extensions/workspaces/README.md` and `agents/lander.md` hold the mechanics.
