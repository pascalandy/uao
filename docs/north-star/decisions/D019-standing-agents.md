# D019 Keep standing agents

Decided 2026-10-17, revised 2026-11-23. Source: upstream. Status: active.

An agent definition with `resident: true` owns one permanent conversation in each project (`docs/subagents.md`). Nobody concludes a standing agent, so it keeps what it learned (`AGENTS.md`). @ultimate is a standing agent. The Voice standing agent is gone: voice mode now forks @ultimate (`1401d351`). The lander now runs no model ([D042](D042-model-free-landing.md)).

**Why.** The commit gives no reason (`8a1c100`). The post says that a standing agent "keeps its conversation and everything it learned about the project" (section "A Team, not an Agent").

**Evidence.** `8a1c100`. `docs/subagents.md` holds the mechanics.
