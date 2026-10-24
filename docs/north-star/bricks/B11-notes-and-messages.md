# B11 Notes and messages

Status: shipped, at the snapshot. Source: upstream.

Conversations exchange information without the user. A note gives another conversation context for its next turn and wakes nobody. A message wakes its recipient, can steer a run in progress, and can expect a reply. The exception is a subagent's one-way update to its parent, which arrives as a note ([messages README](../../../extensions/messages/README.md)). Also, @ultimate's triage can keep a one-way message from a conversation as context, with no wake ([triage](../../../extensions/messages/README.md#triage-for-the-primary-agent)). The @ultimate of one project can tell the @ultimate of another project what changed. Messages to a project on another machine need the user's own backup Worker, which uao does not ship (`lib/remote.ts`, [upstream.md](../upstream.md#what-still-points-at-hazat)). Tailscale alone does not let Ultimate find a project on another machine.

## Where it lives

- `extensions/messages/`: messages, replies, and steering
- `extensions/lineage/`: notes, notify, and catch-up
- `lib/remote.ts`: the address of another project

## Decisions

- [D021](../decisions/D021-updates-are-notes.md) Send subagent updates as notes
- [D022](../decisions/D022-route-through-ultimate.md) Route agent messages for the user through @ultimate

## Evidence

- `99c76b2` adds notes
- `304e47e` separates notes from requests
- `aa15369` limits subagents to their parent
- `3b95632` adds messages between projects
- `28d657a` renames Board to messages
