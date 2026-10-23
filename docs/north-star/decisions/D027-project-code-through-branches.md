# D027 Send project code through a branch

Decided 2026-10-20. Source: upstream. Status: active.

Extensions, surfaces, and tools under a project's `.ultimate/` go through a coordinator branch, like other code. @ultimate writes settings, agent definitions, skills, and helper scripts itself.

**Why.** The commit gives the rule and no reason (`6dfc9e8`). A branch lets the coordinator preview the project extension from its own checkout (`6dfc9e8`).

**Evidence.** `6dfc9e8`. `agents/ultimate.md` holds the rule.
