# D006 Keep the clone apart from the project

Decided 2026-10-02. Source: upstream. Status: active.

Ultimate's code stays in its clone. The tools and the conversation work in the project. Each project has its own home, locks, and port. Discovery reads the clone, then `~/.ultimate/`, then the project. A later item replaces an earlier item with the same name.

**Why.** A specialized agent can run in another repository without moving Ultimate or mixing project state (`1135742`).

**Rejected.** Ultimate that runs only on its own clone (`1135742`).

**Evidence.** `1135742` separates the source root from the project and scopes state by project. `docs/settings.md` holds the order of discovery.
