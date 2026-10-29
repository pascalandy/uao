# B11 Notes and messages

Status: shipped, at the snapshot. Source: upstream.

Conversations exchange information without the user (`extensions/messages/README.md`). A note starts no turn (`extensions/lineage/README.md`). A message can wake or steer its recipient and expect a reply (`extensions/messages/delivery.ts`).

One-way updates to a subagent's parent or a branch's starter become notes (`136d9c01`). A branch reports when no work remains under way ([D041](../decisions/D041-state-based-waking.md)). This rule uses state and no triage model (`136d9c01`).

One project's @ultimate can tell another project's @ultimate what changed (`extensions/messages/remote.ts`). Remote reads and messages share instance discovery ([B16](B16-remote-backup-update.md), `lib/remote.ts`).

@ultimate's messages to the user can include images (`5962e1f8`). Its next question can answer the user's preceding reply and keep a new answer card (`96cad25f`, `a4110c8a`).

## Where it lives

- `extensions/messages/`: messages, replies, and steering
- `extensions/lineage/`: notes, notify, and catch-up
- `lib/remote.ts`: the address of another project

## Decisions

- [D041](../decisions/D041-state-based-waking.md) Use notes for updates and waking reports for finished work
- [D022](../decisions/D022-route-through-ultimate.md) Route agent messages for the user through @ultimate

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
