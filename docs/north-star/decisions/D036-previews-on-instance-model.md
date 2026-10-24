# D036 Preview every agent on one model

Decided 2026-10-24. Source: upstream. Status: active.

A preview runs every agent on `instance.model`, which overrides the root's default model, each agent definition's model, and the summary model (`a4843af`). The project setting wins over the user setting, and this repository sets the model in `.ultimate/settings.json` (`a4843af`). The product still has no faux demos or faux mode (`f23e291`, [D030](D030-previews-on-real-models.md)).

**Why.** The commit gives no reason (`a4843af`).

**Rejected.** Previews on the models that each agent definition sets ([D030](D030-previews-on-real-models.md)).

**Evidence.** `a4843af`. `extensions/instance/README.md` holds the other model rules, such as the default model, the `null` value, and the fast tier. `docs/running.md` holds the preview workflow.
