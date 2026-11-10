# B07 Conversation tree and project memory

Status: shipped, at the snapshot. Source: upstream.

A project keeps one tree of conversations. The root keeps the project memory and the tally, the record of the tree. When its first branch starts, the root becomes a tally and runs no more turns ([D015](../decisions/D015-root-is-a-tally.md)). Each branch does one feature, fix, or experiment. The branch starts from a brief of the project memory. A branch that resumes receives a catch-up about the activity in its tree.

The sidebar's project path opens read-only History (`6ee7d47c`). Its Memory row opens the separate Memory surface (`21669aa1`). The view groups memories by kind and filters their text (`extensions/lineage/web.tsx`). Each memory opens to show its content and source. The user can forget one memory there (`extensions/lineage/web.tsx`).

Recall adds relevant memories after @ultimate's input when optional classification is available (`48f2f2e6`). The [recall mechanics](../../../extensions/recall/README.md) describe its thresholds and cache limits.

Landing memory extraction allows 16,384 output tokens, including reasoning (`5b4de93a`, `extensions/lineage/memory.ts`). This budget replaces the smaller summary budget for that task (`5b4de93a`).

The Plan panel shows an epic without plan tasks by its status and acceptance criteria (`34624b5d`). Plan text preserves literal tags and line breaks (`34624b5d`).

A hover on a branch row in the sidebar shows the branch's summary history (`870a0217`). A steer refreshes the title, summary, and tag of a conversation (`37580ddf`). The catch-up reads only the target's first-parent history, and a failed catch-up no longer fails an input (`29b5223d`). Since `9a79b7f9`, each landing merge carries the trailer that labels its row in that catch-up.

## Where it lives

- `extensions/lineage/`: roots, branches, tally, memory, and catch-up
- `extensions/conversations/`: titles, summaries, abstracts, conclude, and resume
- `extensions/plan/`: the plan ledger of each conversation
- `extensions/sidebar/`: the tree in the sidebar
- `extensions/lineage/web.tsx`: the Memory surface and History page
- `extensions/recall/`: relevant memories for @ultimate's input

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
- `07e4945` normalizes the memory changes that a landing produces
- `f9ac8f2` concludes a landed branch only after its report gets an answer
- `cfd0e93b` replaces that report run with conclusion by the lander unless work remains under way
- `ea2437fe` makes Conclude stop the conversation and its subagents
- `1dbeb9d3` opens the project folder in Zed from History on the host
- `870a0217` adds the summary history of a branch
- `29b5223d` limits the catch-up to the target's first-parent history
