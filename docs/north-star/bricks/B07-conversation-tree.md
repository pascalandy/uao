# B07 Conversation tree and project memory

Status: shipped, at the snapshot. Source: upstream.

A project keeps one tree of conversations. The root runs no turns, and it keeps the project memory and the tally, the record of the tree. Each branch does one feature, fix, or experiment, and it starts from a brief of the memory. A branch that resumes catches up on what its tree did.

## How it works

`lineage` owns the root, the branches, the tally, the memory, notes, catch-up, and rewind. A branch is a fork without an owner, so it is never a subagent. `conversations` writes titles, summaries, and abstracts with the summary model, and it concludes and resumes conversations. `plan` keeps a durable ledger of epics and tasks for a coordinator. The [lineage README](../../../extensions/lineage/README.md) holds the mechanics.

## Where it lives

- `extensions/lineage/`: roots, branches, tally, memory, and catch-up
- `extensions/conversations/`: titles, summaries, abstracts, conclude, and resume
- `extensions/plan/`: the epic and task ledger
- `extensions/sidebar/`: the tree in the sidebar

## Decisions

- [D013](../decisions/D013-branch-is-not-subagent.md) Keep branches apart from subagents
- [D015](../decisions/D015-root-is-a-tally.md) Make the root a tally that runs no turns
- [D023](../decisions/D023-context-and-tally.md) Call the tally "context" in the UI
- [D029](../decisions/D029-branches-start-from-memory.md) Start branches from project memory

## Next

- Nothing stated

## Evidence

- `99c76b2` adds branches and notes
- `00cdf3a` makes roots tallies
- `fc99691` adds abstracts
- `4603cb9` adds rewind in place
- `4c1b652` adds project memory
- `86ed900` keeps one root for each project
