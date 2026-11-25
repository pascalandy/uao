# D004 Build the UI from extensions

Decided 2026-10-02, revised 2026-11-22. Source: upstream. Status: active.

The web core stays small. It holds a surface host, a typed SDK in `web/src/sdk`, the transcript, and the composer. Each feature adds its UI through a `web.solid.tsx` facet, a Solid file since [D046](D046-solid-interface.md). New UI is a new extension folder, not a change to `web/` (`AGENTS.md`).

**Why.** Each facet loads alone, so a broken facet shows an error card while the rest keeps running. The user can delete an extension, and the shell continues to run (`fff6d4b`).

**Evidence.** `fff6d4b` adds the web core and the facet registry. `256f9cee` replaces the `web.tsx` facet with `web.solid.tsx`.
