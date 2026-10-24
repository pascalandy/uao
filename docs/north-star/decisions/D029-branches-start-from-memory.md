# D029 Start branches from project memory

Decided 2026-10-21. Source: upstream. Status: active.

A root keeps a project memory of decisions, facts, and lessons, with at most 150 entries. A new branch starts from a brief that contains the memory index, the last 10 landings, and the location of the full tally. Each write to the memory either completes in full or makes no change.

**Why.** The brief keeps the start of a branch short (inferred from `4c1b652`). The tally stays a history that the user can read (inferred from `4c1b652`).

**Rejected.** The whole tally as the start of each branch from a root with memory (`4c1b652`).

**Evidence.** `4c1b652`. `extensions/lineage/README.md` holds the mechanics.
