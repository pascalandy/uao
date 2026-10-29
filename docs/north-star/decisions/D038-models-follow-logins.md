# D038 Use models with a confirmed login

Decided 2026-10-25, revised 2026-10-27. Source: upstream. Status: active.

New conversations use a model with a login (`21ff1b3f`). An existing conversation switches only after a fresh check confirms that its login is gone (`fa6830aa`). A subscription login can fall back only to another subscription login (`fa6830aa`).

**Why.** An uncertain auth probe must not replace a usable model or turn a request on a subscription login into a paid-key request (`fa6830aa`).

**Evidence.** `21ff1b3f`, `fa6830aa`, and `c2257e8d`. `extensions/models/fallback.ts` and `extensions/models/README.md` own the fallback order and refusal.
