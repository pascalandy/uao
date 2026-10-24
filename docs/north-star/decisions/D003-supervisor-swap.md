# D003 Swap core generations through a supervisor

Decided 2026-10-02. Source: upstream. Status: active.

A small supervisor in `bin/` holds the public port and the lock. For a change to `server/` or `shared/`, the supervisor type-checks and prepares a new generation next to the old generation. The old generation releases storage only when the new generation is ready. If the new generation fails to boot, the old generation stays.

**Why.** A restart or a crash must keep the ownership of storage and the live run (`e3f76bb`). In the words of the post, "the browser just reconnects, and everything keeps going as it was" (section "It Rebuilds Itself while it Runs").

**Evidence.** `e3f76bb` adds the swap and the crash recovery. `083fd2a` adds the rollback of a failed swap. `docs/running.md` holds the mechanics.
