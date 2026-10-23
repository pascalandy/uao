# D031 Ship resource-needing built-ins off

Decided 2026-10-23. Source: upstream. Status: active.

Eight built-ins that need a resource of their own ship off: `cloud`, `parallel`, `tailscale`, `update`, `health`, `classify`, `phase`, and `sounds`. The user or the project turns one on with `extensions.enable`.

**Why.** A personal switch must not write to a committed project settings file (`5323967`).

**Rejected.** Every built-in on by default (`3da36b9`).

**Evidence.** `5323967`. `defaultOff` in `shared/extension-api.ts` holds the list. [upstream.md](../upstream.md#known-drift-in-upstream-docs) notes that the README still says the opposite.
