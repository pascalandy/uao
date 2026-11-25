# B07 Conversation tree and project memory

Status: shipped, at the snapshot. Source: upstream.

A project keeps one tree of conversations. The root keeps the project memory and the tally, the record of the tree. When its first branch starts, the root becomes a tally and runs no more turns ([D015](../decisions/D015-root-is-a-tally.md)). Each branch does one feature, fix, or experiment. The branch starts from a brief of the project memory. A branch that resumes hears only of new target commits that overlap the files it changed. What its siblings did stays in the root's tally (`607dd8ca`, `AGENTS.md`).

The sidebar's project path opens read-only History (`6ee7d47c`). Its Memory row opens the separate Memory surface (`21669aa1`). The view groups memories by kind and filters their text (`extensions/lineage/web.solid.tsx`). Each memory opens to show its content and source. The user can forget one memory there (`extensions/lineage/web.solid.tsx`).

Recall adds relevant memories after @ultimate's input when optional classification is available (`48f2f2e6`). The [recall mechanics](../../../extensions/recall/README.md) describe its thresholds and cache limits.

A landing no longer writes project memory. Memory comes only from judgment: @ultimate's `remember` and the dream's memory pass, which the user approves (`cd77dc1e`, [lineage mechanics](../../../extensions/lineage/README.md)). Each memory must pass one test: would a branch that starts next month act differently without it (`cd77dc1e`, `agents/ultimate.md`). The `memory` tool takes a plain-text query, which recall answers when classification is available, and it reads several slugs at once. An unknown slug gets the index, not a failure (`4ded0eef`, `d9f0cbca`).

The Plan panel shows an epic without plan tasks by its status and acceptance criteria (`34624b5d`). Plan text preserves literal tags and line breaks (`34624b5d`). A criterion is confirmed when the coordinator lists it as met, or when the epic is done. Phase estimates the progress of the other criteria. The plan pill shows the confirmed criteria and the criteria that look done, such as `E1 · 3✓ 5/8` (`53e54861`, `extensions/plan/README.md`).

A hover on a branch row in the sidebar shows the branch's summary history (`870a0217`). A steer refreshes the title, summary, and tag of a conversation (`37580ddf`). The overlap note names each overlapping commit with its trailer and paths, and the number of commits that an isolate is behind (`607dd8ca`). It counts untracked files and skips the branch's own commits (`9f79d8da`, `f4b43a67`). Since `9a79b7f9`, each landing merge carries the trailer that the note shows. Before `607dd8ca`, the catch-up also told a branch what its siblings did (`29b5223d`). @ultimate has no workspace, so it gets no commit note (`cbc96a2c`). The sidebar header shows the project's name and its GitHub repository (`45cdaf28`).

## Where it lives

- `extensions/lineage/`: roots, branches, tally, memory, and overlap notes
- `extensions/conversations/`: titles, summaries, abstracts, conclude, and resume
- `extensions/plan/`: the plan ledger of each conversation
- `extensions/sidebar/`: the tree in the sidebar
- `extensions/lineage/web.solid.tsx`: the Memory surface and History page
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
- `607dd8ca` replaces the catch-up with a note about overlapping commits
- `cd77dc1e` removes the landing distiller, which `5b4de93a` had given a larger output budget
- `53e54861` adds the progress of acceptance criteria
