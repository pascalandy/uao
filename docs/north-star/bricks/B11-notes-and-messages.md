# B11 Notes and messages

Status: shipped, at the snapshot. Source: upstream.

Conversations talk to each other without the user. A note gives another conversation context for its next turn and wakes nobody. A message wakes its recipient, can steer a run in progress, and can expect a reply. The @ultimate of one project can tell the @ultimate of another project what changed.

## How it works

`lineage` holds `note`, `notify`, and catch-up. `messages` holds durable messages, replies, steering, and one-hop messages between projects. `lib/remote.ts` finds the other project on loopback or on the tailnet. Only @ultimate may message the user, and a subagent may message only its parent. The [messages README](../../../extensions/messages/README.md) holds the mechanics.

## Where it lives

- `extensions/messages/`: messages, replies, and steering
- `extensions/lineage/`: notes, notify, and catch-up
- `lib/remote.ts`: the address of another project

## Decisions

- [D021](../decisions/D021-updates-are-notes.md) Send updates as notes
- [D022](../decisions/D022-talk-to-ultimate.md) Let the user talk only to @ultimate

## Next

- Nothing stated

## Evidence

- `99c76b2` adds notes
- `304e47e` separates notes from requests
- `aa15369` limits subagents to their parent
- `3b95632` adds messages between projects
- `28d657a` renames Board to messages
