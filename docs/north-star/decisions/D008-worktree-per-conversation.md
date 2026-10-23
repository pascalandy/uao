# D008 Give parallel work its own isolate

Decided 2026-10-02. Source: upstream. Status: active.

A worker, a designer, and each coordinator branch work in their own isolate, a git worktree. An isolate separates files only, so it is not a sandbox.

**Why.** Parallel edits stay away from the user's checkout (`1c10440`). In the post, "Every feature gets its own worktree", so features can change the same UI components at the same time (section "A Team, not an Agent").

**Rejected.** Workers that edit the shared checkout (`1c10440`).

**Evidence.** `1c10440` adds isolates. `agents/worker.md` and `agents/designer.md` set `isolate: worktree`. `docs/worktrees.md` holds the mechanics.
