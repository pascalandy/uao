# B13 Background work

Status: shipped, at the snapshot. Source: upstream.

Work continues when no agent turn runs (`extensions/automations/README.md`). Automations use schedules, script triggers, domain events, or context thresholds (`extensions/automations/README.md`). Each automation starts a prompt run, wakes existing conversations, or does both (`extensions/automations/README.md`). A script waits without model calls and signals `FIRE` when its condition is met (`extensions/automations/README.md`).

Automation grants and the `act` operation are removed ([D039](../decisions/D039-remove-automation-grants.md)). The [automation mechanics](../../../extensions/automations/README.md#actions) describe prompt runs and subscriber delivery.

Event filters and subscribers can name a standing agent across chapters (`extensions/automations/triggers.ts`, `extensions/automations/server.ts`). Context conditions can require a period without user input (`6c37a236`). Dream ships two context automations ([B15](B15-dreams-and-chapters.md)).

## Where it lives

- `extensions/automations/`: triggers, actions, the ledger, and the UI
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
- `6c1c6bc` resolves standing-agent names in event filters
- `096ac794` requires every fire to reach someone and escalates scripts that remain stuck
- `6d96d892` keys nested tool receipts by call so each codemode call acts
- `903ce43e` keeps every subscriber delivery failure
