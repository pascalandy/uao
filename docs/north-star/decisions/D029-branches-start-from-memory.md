# D029 Start branches from project memory

Decided 2026-10-21, revised 2026-11-16. Source: upstream. Status: active.

A root keeps a project memory of decisions, facts, and lessons, with at most 150 entries. A new branch starts from a brief that contains the memory index, the last 10 landings, and the location of the full tally. Each write to the memory either completes in full or makes no change. Only @ultimate's `remember` and the dream's memory pass write memory. A landing does not (`cd77dc1e`).

**Why.** The brief keeps the start of a branch short (inferred from `4c1b652`). The tally stays a history that the user can read (inferred from `4c1b652`).

**Rejected.** The whole tally as the start of each branch from a root with memory (`4c1b652`). A summary model that turned each landing into memory. It wrote most of the 145 memories of one root, with facts that the code, the docs, and `git log` already show (`cd77dc1e`).

**Evidence.** `4c1b652` and `cd77dc1e`. `extensions/lineage/README.md` holds the mechanics.
