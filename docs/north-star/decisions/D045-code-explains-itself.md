# D045 Let product code explain itself

Decided 2026-11-14, revised 2026-11-15. Source: upstream. Status: active.

Product code has no comments, except the documentation of contracts, Pi upstream markers, and copied licences (`55136da8`, `552d6164`). Code that exists only because of something outside it gets its reason in its commit message and a regression test that fails without it (`b4f0474f`). A lint message says why the pattern is not wanted and what to do instead. `AGENTS.md` keeps a table of each rule and the check that enforces it (`b4f0474f`, [Review quality](../../../AGENTS.md#review-quality)).

**Why.** Agents copy the code base, so an exception in the code becomes a pattern for the next agent (`b4f0474f`, `AGENTS.md`).

**Rejected.** A comment at the code that names the origin of a workaround (`924a0b0c`). A reason comment before a replay-safe tool, which `ultimate/replay-safe-by-name` and `lib/replay.ts` replace (`e427cb99`).

**Evidence.** `b4f0474f`, `55136da8`, `552d6164`, and `e427cb99`. `6cde269a` adds tests that hold the workarounds whose origin comments go.
