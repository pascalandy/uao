# D036 Preview every agent on one model

Decided 2026-10-24, revised 2026-10-29. Source: upstream. Status: active.

A preview runs every agent on one model (`a4843af`). An `instance.model` pin overrides the preview's model family (`741ec0da`, `extensions/instance/server.ts`). Without a pin, previews use the assigned family, `fast` by default (`lib/families.ts`). This repository commits that assignment in `.ultimate/settings.json` (`d6f3657a`). The product still has no faux demos or faux mode (`f23e291`, [D030](D030-previews-on-real-models.md)).

**Why.** The commit gives no reason (`a4843af`).

**Rejected.** Previews on the models that each agent definition sets ([D030](D030-previews-on-real-models.md)).

**Evidence.** `a4843af` and `741ec0da`. `extensions/instance/server.ts` resolves the model. `docs/running.md` holds the preview workflow.
