# D029 Start branches from project memory

Decided 2026-10-21. Source: upstream. Status: active.

A root keeps a project memory of decisions, facts, and lessons, with at most 150 entries. A new branch starts from a brief: the memory index, the last 10 landings, and where the full tally is. Each write to the memory is all or nothing.

**Why.** The brief keeps the start of a branch short, and the tally stays a history that the user can read (inferred from `4c1b652`).

**Rejected.** The whole tally as the start of each branch from a root with memory (`4c1b652`).

**Evidence.** `4c1b652`. `extensions/lineage/README.md` holds the mechanics.
