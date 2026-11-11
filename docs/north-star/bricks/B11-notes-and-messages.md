# B11 Notes and messages

Status: shipped, at the snapshot. Source: upstream.

Conversations exchange information without the user (`extensions/messages/README.md`). A note starts no turn (`extensions/lineage/README.md`). A message can wake or steer its recipient and expect a reply (`extensions/messages/delivery.ts`).

One-way updates to a subagent's parent or a branch's starter become notes (`136d9c01`). A branch reports when no work remains under way ([D041](../decisions/D041-state-based-waking.md)). This rule uses state and no triage model (`136d9c01`).

One project's @ultimate can tell another project's @ultimate what changed (`extensions/messages/remote.ts`). Remote reads and messages share instance discovery ([B16](B16-remote-backup-update.md), `lib/remote.ts`).

@ultimate's messages to the user can include images (`5962e1f8`). Its next question can answer the user's preceding reply and keep a new answer card (`96cad25f`, `a4110c8a`).

@ultimate's final answer can return to every eligible branch whose reply or report shared its run ([D041](../decisions/D041-state-based-waking.md)). A routed answer folds into the transcript's update stretch (`f2d39af7`). Only a branch's reply to its own starter shows that it awaits @ultimate (`bb2a4398`).

A branch that @ultimate starts while it owes another agent an answer records that request. When the branch concludes, @ultimate's final answer goes to that agent (`71582661`). `notify` skips an answer that the caller already received as a reply (`d20dad42`). One set of status rules decides whether a message is open, owed, or awaited (`c058fba7`). A user's answer names the card that it answers (`8e944092`).

Branches can ask the user directly after @ultimate weighs in ([D044](../decisions/D044-branches-ask-the-user.md)). Question pointers keep their summaries and outcomes outside the bounded message log (`ae0d4fc2`, `extensions/messages/notice.ts`). When the message log trims to 300 messages, it keeps each open message (`cfccc89c`). A pointer shows an open question that scrolled out of the view of the transcript (`cbac5781`).

## Where it lives

- `extensions/messages/`: messages, replies, and steering
- `extensions/lineage/`: notes, notify, and catch-up
- `lib/remote.ts`: the address of another project

## Decisions

- [D041](../decisions/D041-state-based-waking.md) Use notes for updates and waking reports for finished work
- [D044](../decisions/D044-branches-ask-the-user.md) Let branches ask after @ultimate weighs in

## Evidence

- `99c76b2` adds notes
- `304e47e` separates notes from requests
- `aa15369` limits subagents to their parent
- `3b95632` adds messages between projects
- `28d657a` renames Board to messages
- `b956232` makes a message answer the recipient's earlier request when the sender owes that answer
- `2941024` separates the branch tool, admission, delivery, triage, routing, and remote messages into modules
- `104a5d4f` counts pending reports, landings, and notifies as work under way
- `b9bb9113` finds waking tasks by status without a recent-task limit
- `91618d16` routes an answer only to the conversation that asked its question
- `71582661` sends a branch's result to the agent whose request it worked on
- `01d0a9ed` lets a conversation send a message after its workspace is gone
- `cfccc89c` keeps open messages when the message log trims
