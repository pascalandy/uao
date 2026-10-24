# D030 Preview on the configured models

Decided 2026-10-23. Source: upstream. Status: active.

A preview runs a clean Ultimate instance on the models that the user configured. The product has no faux demos or faux mode. Tests script Pi's faux provider directly.

**Why.** The commit gives no reason (`f23e291`). It says that previews and coordinator checks run clean instances on the configured models. A preview on configured models shows the configured behavior (inferred).

**Rejected.** Faux demos, `ULTIMATE_FAUX`, and the faux flag of the instance tool (`f23e291`).

**Evidence.** `f23e291`. `docs/running.md` holds the preview rules.
