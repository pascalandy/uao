# B14 Everything on record

Status: shipped, at the snapshot. Source: upstream.

Conversations stay on record, so Ultimate can study its own behavior (`docs/durability.md`). The user and the agents see tasks, events, traces, the model context, and failures. Call traces are diagnostics with a limit of seven days and 200,000 rows (`server/trace.ts`). "Everything on record" is the intent of the post, not a promise to keep each record without a limit. The post says that "The agent can read any action of any conversation of any subagent".

Hands-off goals keep goal decisions and any attached screenshots in goal reports ([B12](B12-human-in-the-loop.md), `extensions/goal/cards.tsx`).

## Where it lives

- `server/trace.ts`: the call trace
- `extensions/system/`: events, calls, and Agent Lanes
- `extensions/activity/`: the activity feed
- `extensions/tasks/`: the task graph
- `extensions/context/`: the model context
- `extensions/debug/`: the read-only debug tool
- `extensions/info/`: runtime facts
- `extensions/conversations/context.ts`: server records of each conversation's context use

## Evidence

- `2bf6879` adds the call trace
- `06cf3f3` adds the System stream
- `b204c0c` adds the activity feed
- `6a3f41a` adds parked tasks
- `86cf602` adds the context view
- `e3f355c` keeps async failures visible
- `ed0bb8a` publishes context use for the status line and automation triggers
- `001a193d` adds goal decisions and their evidence to the record
