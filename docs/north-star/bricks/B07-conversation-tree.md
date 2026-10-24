# B07 Conversation tree and project memory

Status: shipped, at the snapshot. Source: upstream.

A project keeps one tree of conversations. The root runs no turns, and it keeps the project memory and the tally, the record of the tree. Each branch does one feature, fix, or experiment. The branch starts from a brief of the project memory. A branch that resumes receives a catch-up about the activity in its tree.

## Where it lives

- `extensions/lineage/`: roots, branches, tally, memory, and catch-up
- `extensions/conversations/`: titles, summaries, abstracts, conclude, and resume
- `extensions/plan/`: the plan ledger of each conversation
- `extensions/sidebar/`: the tree in the sidebar

## Decisions

- [D013](../decisions/D013-branch-is-not-subagent.md) Keep branches apart from subagents
- [D015](../decisions/D015-root-is-a-tally.md) Make the root a tally that runs no turns
- [D023](../decisions/D023-context-and-tally.md) Call the tally "context" in the UI
- [D029](../decisions/D029-branches-start-from-memory.md) Start branches from project memory

## Evidence

- `99c76b2` adds branches and notes
- `00cdf3a` makes roots tallies
- `fc99691` adds abstracts
- `4603cb9` adds rewind in place
- `4c1b652` adds project memory
- `86ed900` keeps one root for each project
