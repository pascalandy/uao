# B13 Background work

Status: shipped, at the snapshot. Source: upstream.

Work continues when no agent turn runs (`extensions/automations/README.md`). Automations use schedules, supervised scripts, domain events, or context thresholds (`extensions/automations/README.md`). Each automation starts a prompt run, wakes existing conversations, or does both (`extensions/automations/README.md`). A script waits without model calls and signals `FIRE` when its condition is met (`extensions/automations/README.md`).

User grants authorize named actions for dreams, compaction, or chapter switches (`extensions/automations/README.md`). The [automation mechanics](../../../extensions/automations/README.md#grants) hold the limits and the checks for those actions.

## Where it lives

- `extensions/automations/`: triggers, actions, grants, the ledger, and the UI
- `agents/watcher.md`: the agent that writes and repairs a script trigger
- `lib/process-group.ts`: process groups

## Evidence

- `3ad26d3` adds automations
- `656db80` adds subscriptions
- `8cc313c` adds project subscriptions
- `9b55a58` supervises process groups
- `e099781` folds subscriptions into automations and replaces the subscription agent with the watcher
- `9dd221c` gives schedules and scripts one UI
- `a7f32b5` adds event and context triggers
- `d6c9628` adds user grants for named actions
- `ab10dee` exposes triggers and grants in the UI
