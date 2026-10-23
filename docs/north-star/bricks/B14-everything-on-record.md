# B14 Everything on record

Status: shipped, at the snapshot. Source: upstream.

Every action of every conversation stays readable, so Ultimate can study its own behavior. The user and the agents see tasks, events, traces, the model context, and failures. The post says that "The agent can read any action of any conversation of any subagent".

## How it works

`server/trace.ts` links nested calls by parent. `system` shows events and calls, with Agent Lanes, a timeline of who worked when. `activity` is a feed of events with filters. `tasks` shows the durable task graph and the tasks that a crash loop parked. `context` shows what the model received. `debug` gives agents a read-only view of events and traces. [Tracing](../../../docs/extensions.md#tracing) holds the mechanics.

## Where it lives

- `server/trace.ts`: the call trace
- `extensions/system/`: events, calls, and Agent Lanes
- `extensions/activity/`: the activity feed
- `extensions/tasks/`: the task graph
- `extensions/context/`: the model context
- `extensions/debug/`: the read-only debug tool
- `extensions/info/`: runtime facts

## Decisions

- None recorded

## Next

- A better flow timeline. The post says that the timeline "isn't ideal yet" (section "An Example: Side Chats")

## Evidence

- `2bf6879` adds the call trace
- `06cf3f3` adds the System stream
- `b204c0c` adds the activity feed
- `6a3f41a` adds parked tasks
- `86cf602` adds the context view
- `e3f355c` keeps async failures visible
