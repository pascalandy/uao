# D031 Disable by default the built-ins that need resources

Decided 2026-10-23. Source: upstream. Status: active.

Eight built-ins that each need a separate resource are disabled by default: `cloud`, `parallel`, `tailscale`, `update`, `health`, `classify`, `phase`, and `sounds`. The user or the project enables a built-in through `extensions.enable`.

**Why.** Each built-in needs its own resource, such as an API key, a backup Worker, or Tailscale (`docs/settings.md`). The commit gives no reason (`5323967`).

**Rejected.** Every built-in on by default (`3da36b9`).

**Evidence.** `5323967`. `defaultOff` in `shared/extension-api.ts` holds the list. [upstream.md](../upstream.md#known-drift-in-upstream-docs) notes that the README still says the opposite.
