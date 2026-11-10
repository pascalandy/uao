# D031 Disable by default the built-ins that need resources

Decided 2026-10-23, revised 2026-11-09. Source: upstream. Status: active.

Ten built-ins ship off by default: `cloud`, `parallel`, `tailscale`, `health`, `classify`, `phase`, `sounds`, `voice-live`, `push`, and `wire` (`shared/extension-api.ts`). The user or project enables them through `extensions.enable` (`docs/settings.md`). Update now ships on (`7f011b47`). Live voice, push notifications, and Wire ship off (`ab959a36`, `ff44988c`, `c16450c9`).

**Why.** Each built-in needs its own resource, such as an API key, a backup Worker, or Tailscale (`docs/settings.md`). The commit gives no reason (`5323967`).

**Rejected.** Every built-in on by default (`3da36b9`).

**Evidence.** `5323967`. `defaultOff` in `shared/extension-api.ts` holds the list. The README now says that some built-ins start off (`464697b3`).
