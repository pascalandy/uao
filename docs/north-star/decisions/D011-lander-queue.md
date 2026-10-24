# D011 Land through a durable queue

Decided 2026-10-13. Source: upstream. Status: active.

`workspace submit` queues the tip of a clean isolate. Code lands each submission in order. The code merges, runs the configured checks, fast-forwards the target, and pushes without force. The lander's model works only when a step fails or a user messages the lander.

**Why.** Coordinators spent many turns to merge, check, land, and push. Also, `workspace land` often failed on a target that advanced or on an unrelated dirty file (`5c36dcd`).

**Rejected.** Synchronous `workspace land` as the default end of a branch. It stays as an alternative that never pushes (`docs/worktrees.md`).

**Evidence.** `5c36dcd` adds the queue. `extensions/workspaces/README.md` and `agents/lander.md` hold the mechanics.
