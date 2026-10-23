# Decisions

Each decision records a choice with lasting effect, its reason, and its evidence. The rule itself lives in the file that owns it, such as `AGENTS.md` or an extension README, and the decision links to that file.

A decision is **active**, or **replaced by Dnnn** when a later decision takes its place. Its source is **upstream** for Daniel's project, or **uao** for Pascal's direction. A `Source: uao` decision cites Pascal's answer as its evidence. The fork commit `7698625` shows only the fork point. It does not prove a uao rule.

## Add a decision

1. Take the next free number. The numbers follow the dates of the decisions
2. Create the file `D<nnn>-<slug>.md`
3. Write the heading `# D<nnn> <title>`
4. Write the line `Decided <date>. Source: upstream | uao. Status: active.`
5. State the rule in one to three sentences
6. Write `**Why.**` with the reason that the source gives. If the source gives no reason, say so
7. If the source names an alternative, write `**Rejected.**` with it
8. Write `**Evidence.**` with short SHAs or paths
9. Add one row to the table below

The date of a decision is the date of its commit: `git log -1 --format=%ad --date=short <sha>`. When a later commit refines the same rule, write "revised <date>" after the first date. When a new rule replaces a decision, add a new decision. Set the status of the old one to `replaced by D<nnn>`. Do not list the bricks that use a decision.

## Index

| Decision                                      | Date       | Source   | Status | Title                                               |
| --------------------------------------------- | ---------- | -------- | ------ | --------------------------------------------------- |
| [D001](D001-reload-by-layer.md)               | 2026-10-01 | upstream | active | Reload each layer without ending the conversation   |
| [D002](D002-pi-durable-sqlite.md)             | 2026-10-02 | upstream | active | Build on Pi Durable over SQLite                     |
| [D003](D003-supervisor-swap.md)               | 2026-10-02 | upstream | active | Swap core generations through a supervisor          |
| [D004](D004-ui-from-extensions.md)            | 2026-10-02 | upstream | active | Build the UI from extensions                        |
| [D005](D005-codemode-sandbox.md)              | 2026-10-02 | upstream | active | Compose tools in a codemode sandbox                 |
| [D006](D006-clone-apart-from-project.md)      | 2026-10-02 | upstream | active | Keep the clone apart from the project               |
| [D007](D007-surfaces.md)                      | 2026-10-02 | upstream | active | Make apps surfaces beside the agent                 |
| [D008](D008-worktree-per-conversation.md)     | 2026-10-02 | upstream | active | Give parallel work its own isolate                  |
| [D009](D009-trust-before-project-setup.md)    | 2026-10-02 | upstream | active | Load a project setup only after the user trusts it  |
| [D010](D010-push-without-asking.md)           | 2026-10-12 | upstream | active | Push landed work without asking again               |
| [D011](D011-lander-queue.md)                  | 2026-10-13 | upstream | active | Land through a durable queue                        |
| [D012](D012-design-visible-results.md)        | 2026-10-13 | upstream | active | Design each visible result                          |
| [D013](D013-branch-is-not-subagent.md)        | 2026-10-14 | upstream | active | Keep branches apart from subagents                  |
| [D014](D014-remove-canvas.md)                 | 2026-10-14 | upstream | active | Remove the Canvas surface                           |
| [D015](D015-root-is-a-tally.md)               | 2026-10-16 | upstream | active | Make the root a tally that runs no turns            |
| [D016](D016-personal-project.md)              | 2026-10-17 | upstream | active | Share Ultimate as a personal project                |
| [D017](D017-questions-get-proposals.md)       | 2026-10-17 | upstream | active | Explore questions, act on instructions              |
| [D018](D018-own-personal-layer.md)            | 2026-10-17 | upstream | active | Keep a personal layer apart from Pi                 |
| [D019](D019-standing-agents.md)               | 2026-10-17 | upstream | active | Keep standing agents                                |
| [D020](D020-size-the-work.md)                 | 2026-10-17 | upstream | active | Size the work to the change                         |
| [D021](D021-updates-are-notes.md)             | 2026-10-17 | upstream | active | Send subagent updates as notes                      |
| [D022](D022-route-through-ultimate.md)        | 2026-10-18 | upstream | active | Route agent messages for the user through @ultimate |
| [D023](D023-context-and-tally.md)             | 2026-10-18 | upstream | active | Call the tally "context" in the UI                  |
| [D024](D024-typed-contracts-core-tier.md)     | 2026-10-18 | upstream | active | Connect extensions through typed contracts          |
| [D025](D025-assess-first.md)                  | 2026-10-19 | upstream | active | Assess a feature before building it                 |
| [D026](D026-stable-system-prompt.md)          | 2026-10-19 | upstream | active | Keep the system prompt stable                       |
| [D027](D027-project-code-through-branches.md) | 2026-10-20 | upstream | active | Send project code through a branch                  |
| [D028](D028-cloud-only-backs-up.md)           | 2026-10-21 | upstream | active | Use the cloud only for backups                      |
| [D029](D029-branches-start-from-memory.md)    | 2026-10-21 | upstream | active | Start branches from project memory                  |
| [D030](D030-previews-on-real-models.md)       | 2026-10-23 | upstream | active | Preview on the configured models                    |
| [D031](D031-resource-built-ins-off.md)        | 2026-10-23 | upstream | active | Ship resource-needing built-ins off                 |
| [D032](D032-fork-as-uao.md)                   | 2026-10-23 | uao      | active | Fork Ultimate as uao                                |
| [D033](D033-one-north-star.md)                | 2026-10-23 | uao      | active | Keep one north-star                                 |
| [D034](D034-follow-upstream.md)               | 2026-10-23 | uao      | active | Follow upstream through merges                      |
| [D035](D035-adopt-blog-direction.md)          | 2026-10-23 | uao      | active | Adopt the direction of the post                     |
