# D001 Reload each layer without ending the conversation

Decided 2026-10-01. Source: upstream. Status: active.

Each layer of the code goes live in its own way. The table in [AGENTS.md](../../../AGENTS.md#layers-and-how-they-reload) lists these ways. Behavior goes in `extensions/` when possible, because an extension reloads without a restart. Only a change to `bin/` needs a human restart.

**Why.** Ultimate runs the repository that it edits, so a change must not end the conversation that made it (`9b341af`). The [first prompt](../sources/first-prompt.md) asks that the conversation and the tools continue during a live reload.

**Evidence.** `9b341af` seeds `AGENTS.md` with the layer table.
