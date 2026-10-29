# B14 Everything on record

Status: shipped, at the snapshot. Source: upstream.

Conversations stay on record, so Ultimate can study its own behavior (`docs/durability.md`). The user and the agents see tasks, events, traces, the model context, and failures. Call traces are diagnostics with a limit of seven days and 200,000 rows (`server/trace.ts`). "Everything on record" is the intent of the post, not a promise to keep each record without a limit. The post says that "The agent can read any action of any conversation of any subagent".

Hands-off goals keep goal decisions and any attached screenshots in goal reports ([B12](B12-human-in-the-loop.md), `extensions/goal/cards.tsx`).

The status action gives dashboards a compact read-only summary of one instance (`ca5dec4c`). It includes discovered extensions and their source, state, and load error (`6b44de7b`).

Tasks group runs and deliveries by meaning and show open messages (`b3462787`, `03d967f4`). Upstream removed the conversation minimap (`6dfcf451`). Rejected ideas use tombstones in project memory, replacing the graveyard folder (`63f87af5`).

## Where it lives

- `server/trace.ts`: the call trace
- `extensions/system/`: events, calls, and Agent Lanes
- `extensions/activity/`: the activity feed
- `extensions/tasks/`: the task graph
- `extensions/context/`: the model context
- `extensions/debug/`: the read-only debug tool
- `extensions/info/`: runtime facts
- `extensions/conversations/context.ts`: server records of each conversation's context use
- `extensions/status/`: the dashboard summary

## Evidence

- `2bf6879` adds the call trace
- `06cf3f3` adds the System stream
- `b204c0c` adds the activity feed
- `6a3f41a` adds parked tasks
- `86cf602` adds the context view
- `e3f355c` keeps async failures visible
- `ed0bb8a` publishes context use for the status line and automation triggers
- `001a193d` adds goal decisions and their evidence to the record
- `8402cb41` counts a tool's returned error result as a failed trace call
- `d0afb3e1` uses SQLite NORMAL for trace commits, so recent diagnostics can be lost on power failure
