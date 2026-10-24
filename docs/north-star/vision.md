# Vision

This file says what uao is, who it is for, what Daniel meant, and where uao goes.

## What uao is

uao is Pascal's fork of Ultimate ([D032](decisions/D032-fork-as-uao.md)). Ultimate is a local coding agent with a web UI, built on Pi Durable. Ultimate runs the repository that it edits. Ultimate changes its own code while the user talks to it (`AGENTS.md`).

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

## uao direction

Source: uao ([D035](decisions/D035-adopt-blog-direction.md)). Pascal adopts the direction of the post. Each point names its section:

1. **An agent that knows the project.** The agent knows a project "inside out" and is "exactly the same every time I come back". It integrates with any project ("Ultimate on My Blog"). See [B06](bricks/B06-project-specialization.md) and [B07](bricks/B07-conversation-tree.md)
2. **A team, not one agent.** The user talks to @ultimate. Coordinators manage the work in one isolate for each feature. Workers, scouts, designers, and reviewers do bounded work, and the lander lands only a result that passes every check ("A Team, not an Agent"). See [B09](bricks/B09-coordinators-and-subagents.md) and [B10](bricks/B10-isolates-previews-lander.md)
3. **One chat for the user.** "Everything else either keeps going on its own, or escalates to me with a question" ("Notes"). See [B08](bricks/B08-ultimate-and-standing-agents.md) and [B11](bricks/B11-notes-and-messages.md)
4. **Standing agents for each project.** Nobody concludes the standing agents, so they keep what they learned. The post names the lander, a deploy agent for Cloudflare, and a writing agent ("A Team, not an Agent", "Ultimate on My Blog"). See [B08](bricks/B08-ultimate-and-standing-agents.md)
5. **Questions before the build.** The agent gives an assessment and a questionnaire that marks the agent's picks. The agent builds only after the user's approval ("An Example: Side Chats", "Ultimate on My Blog"). See [B09](bricks/B09-coordinators-and-subagents.md) and [B12](bricks/B12-human-in-the-loop.md)
6. **Everything on record.** The agent studies its own tool calls, turns what works into tools, and removes what does not work. "I also throw away features way more often now" ("Everything is on Record"). See [B14](bricks/B14-everything-on-record.md) and [B15](bricks/B15-dreams-and-chapters.md)
7. **The real problem.** Agents solve the problem that the user explains, "not build exactly my first, limited solution" ("Just Getting Started")
8. **Speed.** With "a really tight loop" in a codebase that is "completely ready for agents", the work goes fast. Then "the limiting factor really becomes tokens per second" ("Just Getting Started")

### The examples of the post at the snapshot

| Example in the post                 | State at the snapshot | Evidence                                           |
| ----------------------------------- | --------------------- | -------------------------------------------------- |
| Side chats                          | shipped               | `extensions/side-chat/`                            |
| Steering of branches from @ultimate | shipped               | `steer` in `extensions/messages/README.md`         |
| Messages between instances          | shipped               | `ultimate.tell` in `extensions/messages/README.md` |

The post also names a better flow timeline and design polish. [Next](bricks/README.md#next) lists them.

## Non-goals

- A library, or a product with users to support (`README.md`)
- Stability or migration paths. The post says that "there are no guarantees about what stays and what changes" ([D016](decisions/D016-personal-project.md))
- A sandbox. An isolate separates files, not processes (`extensions/subagents/README.md`)
- A cloud host for conversations. Conversations stay on the machine that runs the project ([D028](decisions/D028-cloud-only-backs-up.md))
- Conversations or roots that the user creates by hand (`AGENTS.md`)
