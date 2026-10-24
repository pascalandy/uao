# D010 Push landed work without asking again

Decided 2026-10-12. Source: upstream. Status: active.

The top-level agent may commit verified work, land it, and push the destination branch to `origin` with no new question. With `workspace submit`, the code of the landing queue runs the checks and does the push (`extensions/workspaces/lander.ts`). Subagents commit and report, but never push. The permission excludes force pushes, other repositories, releases, deployments, and changes to GitHub issues and pull requests.

**Why.** The user gave a standing permission for this repository, public or private (`219dad1`).

**Evidence.** `219dad1`. [Push permission](../../../AGENTS.md#push-permission) holds the rule. [upstream.md](../upstream.md) says what `origin` is in uao.
