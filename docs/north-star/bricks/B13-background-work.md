# B13 Background work

Status: shipped, at the snapshot. Source: upstream.

Work continues when no agent turn runs (`extensions/automations/README.md`). Automations use schedules, script triggers, domain events, or context thresholds (`extensions/automations/README.md`). Each automation starts a prompt run, wakes existing conversations, or does both (`extensions/automations/README.md`). A script waits without model calls and signals `FIRE` when its condition is met (`extensions/automations/README.md`).

Automation grants and the `act` operation are removed ([D039](../decisions/D039-remove-automation-grants.md)). The [automation mechanics](../../../extensions/automations/README.md#actions) describe prompt runs and subscriber delivery.

Event filters and subscribers can name a standing agent across chapters (`extensions/automations/triggers.ts`, `extensions/automations/server.ts`). Context conditions can require a period without user input (`6c37a236`). Dream ships two context automations ([B15](B15-dreams-and-chapters.md)).

Automations are now in the core tier, so settings cannot turn them off ([Core tier](../../../docs/extensions/core-tier.md), `4601a36c`). A skipped fire no longer counts toward the hourly cap (`bc938b06`, `985124ae`). `$AUTOMATION_STATE` is a folder, and a watcher script keeps its state in files inside it (`ef16ed0c`, `agents/watcher.md`). Code waits through the named helpers of `lib/timers.ts`, and signals replace polls where a signal already exists (`8e5b688c`). Keep warm and idle automations sleep as tasks instead of a loop each minute (`81a178cb`).

Watchers start in the project root, not in the worktree of the branch that created them (`70b39ce3`). A pause or a delete of a script stops its watcher (`c04f973e`). A prompt run delivers its answer to its subscribers, and an update keeps them (`d2e7683e`, `896f4c45`). The receipt of the tool names the next fire in UTC and from now (`820aa283`). An automation run keeps `subagent` when its definition lists it (`1d0597f3`).

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
- `db1d8d12` gives a later chapter its own script folders in `<project>@<chapter>/<id>`
- `bf6830af` and `42ab5da0` signal a process group only for an integer pid above 1, because `kill(-1)` reaches every process of the user (`lib/process-group.ts`)
- `4601a36c` moves automations into the core tier
- `bc938b06` stops counting skipped fires toward the hourly cap
