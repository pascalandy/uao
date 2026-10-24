# D009 Load a project setup only after the user trusts it

Decided 2026-10-02. Source: upstream. Status: active.

Ultimate loads the extensions, settings, agents, and skills of a project's `.ultimate/` only after the user trusts that project. Until then, Ultimate uses the global setup. Ultimate keeps each choice in `~/.ultimate/trust.json`.

**Why.** Project extensions run code (`README.md`). A project without a recorded trust choice must not control the user's extensions (`024ff05`).

**Evidence.** `a5fe6b8` adds the trust requirement. `024ff05` also applies the trust requirement to project settings. `docs/settings.md` holds the rules.
