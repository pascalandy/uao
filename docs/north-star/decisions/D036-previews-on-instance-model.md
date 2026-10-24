# D036 Preview every agent on one model

Decided 2026-10-24. Source: upstream. Status: active.

A preview runs every agent on the `instance.model` setting. The setting overrides the default model of the root, the model of each agent definition, and the summary model. It also puts the model on the fast tier. The default is `openai-codex/gpt-6.1-sol`, and `null` turns the override off (`a4843af`, `extensions/instance/README.md`). The project setting wins over the user setting. This repository sets it in `.ultimate/settings.json` (`a4843af`). The product still has no faux demos or faux mode (`f23e291`, [D030](D030-previews-on-real-models.md)).

**Why.** The commit gives no reason (`a4843af`).

**Rejected.** Previews on the models that each agent definition sets ([D030](D030-previews-on-real-models.md)).

**Evidence.** `a4843af`. `extensions/instance/README.md` holds the model rules, and `docs/running.md` holds the preview workflow.
