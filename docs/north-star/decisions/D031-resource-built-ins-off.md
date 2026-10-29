# D031 Disable by default the built-ins that need resources

Decided 2026-10-23, revised 2026-10-25. Source: upstream. Status: active.

Eight built-ins ship off by default: `cloud`, `parallel`, `tailscale`, `health`, `classify`, `phase`, `sounds`, and `voice-live` (`shared/extension-api.ts`). The user or project enables them through `extensions.enable` (`docs/settings.md`). Update now ships on (`7f011b47`), and live voice ships off (`ab959a36`).

**Why.** Each built-in needs its own resource, such as an API key, a backup Worker, or Tailscale (`docs/settings.md`). The commit gives no reason (`5323967`).

**Rejected.** Every built-in on by default (`3da36b9`).

**Evidence.** `5323967`. `defaultOff` in `shared/extension-api.ts` holds the list. [upstream.md](../upstream.md#known-drift-in-upstream-docs) notes that the README still says the opposite.
