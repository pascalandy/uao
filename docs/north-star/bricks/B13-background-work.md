# B13 Background work

Status: shipped, at the snapshot. Source: upstream.

Work continues when no agent turn runs. Automations run agent prompts on a schedule. Subscriptions run supervised scripts that wake a conversation only when something is ready, so no model polls.

## How it works

`automations` stores each schedule and runs each fire as its own conversation, and it skips a fire that overlaps a run. `subscriptions` supervises each script and wakes the subscribed conversation when the script prints `FIRE`. A project can commit subscription definitions, which load stopped. `lib/process-group.ts` starts and stops each child process group as one unit. Each extension README holds its mechanics.

## Where it lives

- `extensions/automations/`: schedules
- `extensions/subscriptions/`: supervised scripts
- `agents/subscription.md`: the agent that writes a subscription script
- `lib/process-group.ts`: process groups

## Decisions

- None recorded

## Next

- Nothing stated

## Evidence

- `3ad26d3` adds automations
- `656db80` adds subscriptions
- `8cc313c` adds project subscriptions
- `9b55a58` supervises process groups
