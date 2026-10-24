# D030 Preview on the configured models

Decided 2026-10-23, revised 2026-10-24. Source: upstream. Status: active.

A preview runs a clean Ultimate instance on the `instance.model` setting (`a4843af`). The default is `openai-codex/gpt-6.1-sol` on the fast tier (`extensions/instance/README.md`). This setting overrides agent pins and the summary model (`a4843af`). Setting `instance.model` to `null` restores the configured models (`extensions/instance/README.md`). The product has no faux demos or faux mode (`f23e291`). Tests script Pi's faux provider directly (`f23e291`).

**Why.** The commit gives no reason (`f23e291`). It says that previews and coordinator checks run clean instances on the configured models. A preview on configured models shows the configured behavior (inferred).

**Rejected.** Faux demos, `ULTIMATE_FAUX`, and the faux flag of the instance tool (`f23e291`).

**Evidence.** `f23e291` removes faux mode. `a4843af` adds the preview override. `extensions/instance/README.md` holds the model rules, and `docs/running.md` holds the preview workflow.
