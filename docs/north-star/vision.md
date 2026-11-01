# Vision

This file says what uao is, who it is for, what Daniel meant, and where uao goes.

## What uao is

uao is Pascal's fork of Ultimate ([D032](decisions/D032-fork-as-uao.md)). Ultimate is a local coding agent with a web UI, built on Pi Durable. Ultimate runs the repository that it edits. Ultimate changes its own code while the user talks to it (`AGENTS.md`).

The [explainer](sources/explainer-page.md) describes an agent that keeps project context and writes tools for the project. Project tools travel with the project, and personal tools stay with the user (explainer, "I grow with the project").

The fork README says that uao stands for "the Ultimate Agent Orchestrator" (`7698625`). That line is a fact about the name, not a new plan.

## Who it is for

- Pascal, who directs uao ([D034](decisions/D034-follow-upstream.md))
- Agents that work on the repository: Claude Code or Codex sessions, and Ultimate itself
- Anyone who forks it, with no promise of stability ([D016](decisions/D016-personal-project.md))

## Daniel's original intent

The [first prompt](sources/first-prompt.md) asks for these things:

- A local coding agent with a web UI on Vite and Node, and the option of other storage, such as Cloudflare
- An agent that writes and builds its own UI. The agent knows its own source. The agent reloads live while the conversation and the tools continue, because everything runs in Pi Durable ([B01](bricks/B01-durable-conversations.md), [B02](bricks/B02-self-change-while-running.md))
- Few dependencies, a UI with hot reload, and Pi as the role model ([B03](bricks/B03-reloadable-extensions.md))
- A view of the model, the context use, the extensions, the skills, the machine, and the storage ([B14](bricks/B14-everything-on-record.md))
- Questions before the build, and then "we built ultimate with ultimate"

[Daniel's post](https://danielgriesser.com/posts/ultimate/) adds the reason. Daniel wants "the most malleable coding agent, or agent harness" that he has used. Earlier durability layers felt "too complex, too involved and too integrated", and Pi Durable made the idea possible (section "How it Started").

Daniel wanted an agent that keeps project knowledge because changes between projects lost context ([explainer](sources/explainer-page.md), "Why Daniel built me").

## uao direction

Source: uao ([D035](decisions/D035-adopt-blog-direction.md)). Pascal adopts the post and the [explainer](sources/explainer-page.md). Each point names its source section:

1. **An agent that knows the project.** The agent knows a project "inside out" and is "exactly the same every time I come back". It integrates with any project (post, "Ultimate on My Blog", and explainer, "I grow with the project"). See [B06](bricks/B06-project-specialization.md) and [B07](bricks/B07-conversation-tree.md)
2. **A team, not one agent.** The user talks to @ultimate. Coordinators manage the work in one isolate for each feature. Workers, scouts, designers, and reviewers do bounded work, and the lander requires the configured checks (post, "A Team, not an Agent", and explainer, "A team behind one conversation" and "Only working changes go in"). See [B09](bricks/B09-coordinators-and-subagents.md) and [B10](bricks/B10-isolates-previews-lander.md)
3. **One chat for the user.** "Everything else either keeps going on its own, or escalates to me with a question" (post, "Notes"). The explainer restates one conversation as the entry point ("A team behind one conversation"). Branches now ask their own questions ([B12](bricks/B12-human-in-the-loop.md)). See [B08](bricks/B08-ultimate-and-standing-agents.md) and [B11](bricks/B11-notes-and-messages.md)
4. **Standing agents for each project.** Nobody concludes the standing agents, so they keep what they learned. The post names the lander, a deploy agent for Cloudflare, and a writing agent ("A Team, not an Agent", "Ultimate on My Blog"). See [B08](bricks/B08-ultimate-and-standing-agents.md)
5. **Questions before the build.** The agent gives an assessment and a questionnaire that marks the agent's picks. The agent builds only after the user's approval (post, "An Example: Side Chats" and "Ultimate on My Blog", and explainer, "Something to try first"). See [B09](bricks/B09-coordinators-and-subagents.md) and [B12](bricks/B12-human-in-the-loop.md)
6. **Everything on record.** The agent studies its own tool calls, turns what works into tools, and removes what does not work. "I also throw away features way more often now" (post, "Everything is on Record"). The explainer restates learning from failed calls ("A simple, stable foundation"). See [B14](bricks/B14-everything-on-record.md) and [B15](bricks/B15-dreams-and-chapters.md)
7. **The real problem.** Agents solve the problem that the user explains, "not build exactly my first, limited solution" ("Just Getting Started")
8. **Speed.** With "a really tight loop" in a codebase that is "completely ready for agents", the work goes fast. Then "the limiting factor really becomes tokens per second" ("Just Getting Started")

### The examples of the post at the snapshot

| Example in the post                 | State at the snapshot | Evidence                                     |
| ----------------------------------- | --------------------- | -------------------------------------------- |
| Side chats                          | shipped               | `extensions/side-chat/server.ts`             |
| Steering of branches from @ultimate | shipped               | `steer` in `extensions/messages/delivery.ts` |
| Messages between instances          | shipped               | `tell` in `extensions/messages/remote.ts`    |

The post also names a better flow timeline and design polish. [Next](bricks/README.md#next) lists them.

### The claims of the explainer at the snapshot

These states describe upstream at `d0a2e17b`. A **partial** claim exceeds what the code supports in the stated way:

| Claim in the explainer                                     | State   | Code evidence and limit                                                                                                                                                                                                                 | Brick                                           |
| ---------------------------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Reload while running                                       | shipped | Extension reloads and checked core swaps preserve conversations (`server/extensions.ts`, `bin/ultimate.ts`)                                                                                                                             | [B02](bricks/B02-self-change-while-running.md)  |
| Self-aware: build, source, calls, and a separate test copy | partial | Build identity, file reads, and previews exist. The claim to read every call has a limit: diagnostic traces expire (`server/build.ts`, `extensions/coding-tools/server.ts`, `server/trace.ts`, `extensions/instance/server.ts`)         | [B14](bricks/B14-everything-on-record.md)       |
| Writes its own tools                                       | shipped | Trusted project extensions add tools and UI (`server/discovery.ts`, `server/extensions.ts`)                                                                                                                                             | [B05](bricks/B05-agent-tools.md)                |
| Keeps context precisely, with nothing lost                 | partial | Full conversation history survives compaction. Model context uses summaries, and external effects have crash windows. The absolute claim is unsupported (`docs/durability.md`, `extensions/lineage/server.ts`)                          | [B01](bricks/B01-durable-conversations.md)      |
| Team behind one conversation                               | shipped | @ultimate starts coordinator branches with bounded subagents (`extensions/messages/branch.ts`, `extensions/subagents/server.ts`)                                                                                                        | [B09](bricks/B09-coordinators-and-subagents.md) |
| Checks its own work                                        | shipped | Preview instances and browser tools support checks. The UI skills require review and approval for small visual changes (`extensions/instance/server.ts`, `skills/verify-ui/SKILL.md`, `skills/ui-preview-round/SKILL.md`)               | [B10](bricks/B10-isolates-previews-lander.md)   |
| Only working changes go in, after every test               | partial | The model-free lander runs configured checks. Checks are optional per project, and a retry can accept a flaky check. It cannot guarantee that every change works (`extensions/workspaces/lander.ts`, `extensions/workspaces/README.md`) | [B10](bricks/B10-isolates-previews-lander.md)   |
| Updates itself while running                               | shipped | Facets reload. Core changes require the restart tool, and Update reports the owed restart (`server/extensions.ts`, `extensions/self/server.ts`, `fe5907cd`)                                                                             | [B02](bricks/B02-self-change-while-running.md)  |
| Project memory                                             | shipped | Roots keep decisions, facts, and lessons. Branches start from their index (`extensions/lineage/memory.ts`, `extensions/lineage/server.ts`)                                                                                              | [B07](bricks/B07-conversation-tree.md)          |
| Work toward a goal                                         | shipped | User-granted goals supply criteria, decisions, and reports (`extensions/goal/server.ts`)                                                                                                                                                | [B12](bricks/B12-human-in-the-loop.md)          |
| A team of reviewers                                        | shipped | The review lead starts specialist definitions. This project has three (`agents/reviewer.md`, `.ultimate/agents/`)                                                                                                                       | [B09](bricks/B09-coordinators-and-subagents.md) |
| Ultimates on other projects and machines talk              | shipped | `tell` and remote reply admission connect other instances (`extensions/messages/remote.ts`, `lib/remote.ts`)                                                                                                                            | [B11](bricks/B11-notes-and-messages.md)         |
| Phone over a private network                               | shipped | Optional Tailscale access checks the allowed login. The UI supports phones (`extensions/tailscale/server.ts`, `web/public/manifest.webmanifest`)                                                                                        | [B16](bricks/B16-remote-backup-update.md)       |
| Many model providers, with Claude through Claude Code      | shipped | Pi supplies providers and logins. The Claude Code extension registers its provider (`server/harness.ts`, `extensions/claude-code/server.ts`)                                                                                            | [B04](bricks/B04-models-and-providers.md)       |
| Project tools stay in a project folder                     | shipped | Trusted `.ultimate/` resources load from the project (`server/discovery.ts`, `server/project-setup.ts`)                                                                                                                                 | [B06](bricks/B06-project-specialization.md)     |
| Personal tools stay with the user                          | shipped | Discovery loads user resources from `~/.ultimate/` (`server/discovery.ts`)                                                                                                                                                              | [B06](bricks/B06-project-specialization.md)     |

## Non-goals

- A library, or a product with users to support (`README.md`). The [explainer](sources/explainer-page.md) says "I'm not a product" ("I'm not trying to convince you")
- Stability or migration paths. The post says that "there are no guarantees about what stays and what changes" ([D016](decisions/D016-personal-project.md)). The [explainer](sources/explainer-page.md) repeats "No guarantees about what stays" in Daniel's final note
- A sandbox. An isolate separates files, not processes (`extensions/subagents/README.md`)
- A cloud host for conversations. Conversations stay on the machine that runs the project ([D028](decisions/D028-cloud-only-backs-up.md))
- Conversations or roots that the user creates by hand (`AGENTS.md`)
