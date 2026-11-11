# D038 Keep model changes within confirmed logins

Decided 2026-10-25, revised 2026-11-10. Source: upstream. Status: active.

An existing conversation switches only after a fresh check confirms that its login is gone (`fa6830aa`). A provider that is not registered, because its extension did not load, is not evidence of a missing login (`ba854f0e`). A subscription login can fall back only to another subscription login (`fa6830aa`). A new conversation keeps a configured default when no configured choice has a login (`4497cb74`). Only with nothing configured does it choose the first model with a login (`lib/agents.ts`).

**Why.** An uncertain auth probe must not replace a usable model or turn a request on a subscription login into a paid-key request (`fa6830aa`).

The new-conversation rule prevents a missing Claude Code login from selecting an unrelated paid Anthropic model (`4497cb74`, `test/default-model.test.ts`).

**Evidence.** `21ff1b3f`, `fa6830aa`, `c2257e8d`, `4497cb74`, and `ba854f0e`. `extensions/models/fallback.ts` owns existing-conversation fallback. `lib/agents.ts` owns the new-conversation default.
