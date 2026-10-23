# Glossary

This file fixes the names in uao: one name for each thing, and one meaning for each name. Use these names in the north-star, in commits, and in prompts.

## Reading conventions

- Each entry starts with the name that the north-star uses
- "UI:" and "Code:" give the name in the UI or in code, tools, and stored data, when that name is different
- "Not:" names a thing that readers often confuse with the entry
- The path or SHA in parentheses is the source

## Names

- **Ultimate**: the product that runs. It is the `ultimate` command, the web UI, and the agent @ultimate. Daniel Griesser started it in `HazAT/ultimate` (`9b341af`)
- **uao**: the repository `pascalandy/uao`, which is Pascal's fork of Ultimate. The name means "Ultimate Agent Orchestrator" (`7698625`)
- **Upstream**: Daniel's repository, `HazAT/ultimate`. See [upstream.md](upstream.md)
- **Pi**: Earendil's minimal coding agent. Ultimate shares its logins, models, and settings in `~/.pi/agent` (`docs/running.md`)
- **Pi Durable**: the library `@earendil-works/pi-durable`. It stores each conversation and its tasks, and it resumes them after a crash (`docs/durability.md`)

## Work model

- **Project**: the repository that Ultimate works on. It can be Ultimate's own clone or another repository (`1135742`)
- **Clone**: the checkout of Ultimate's code that the host runs from. Code: `host.ultimateRoot` (`extensions/update/README.md`). Not: the project
- **Home**: the folder that holds the state of one project, by default under `~/.ultimate/projects/` (`docs/running.md`)
- **Conversation**: one durable transcript with its agent, tools, and tasks (`docs/durability.md`)
- **Root**: the top conversation of a project's tree. It accepts no input and runs no turns. It holds the project memory and the tally. A project has one root (`extensions/lineage/README.md`)
- **Tally**: the record that a root keeps of its tree. It holds one intent line for each branch, the latest abstract of each conversation, notes, and landings. UI: **context**. Code: `lineage.tally` (`b99106e`). Not: the context window of a model
- **Forest**: the word that `AGENTS.md` uses for a project's conversation trees. Since `86ed900`, a project has one root, so its forest holds one tree (inferred)
- **Branch**: a conversation that forks from the root or from a branch to do one feature, fix, or experiment. Its prompt is its first input (`extensions/lineage/README.md`). Not: a subagent
- **Intent**: the one line that names a branch in the tally. The full prompt stays in the branch (`ad1b2dd`)
- **Abstract**: the summary of one conversation in the tally. It changes with the work, and a landing freezes it (`fc99691`)
- **Project memory**: the decisions, facts, and lessons that a root keeps by slug. A new branch starts from a brief of this memory. Code: `lineage.memory`, tool `remember` (`4c1b652`)
- **Catch-up**: the update that a branch receives when it resumes. It holds the new tally events of its tree, then the new commits on its target (`extensions/lineage/README.md`)
- **Conclude**: to close a conversation when its work is done. A concluded conversation stays readable and can resume. Roots and standing agents are never concluded (`AGENTS.md`)
- **Compaction**: a summary of old messages that replaces them in the model context. The old messages stay in storage ([Pi Durable](https://earendil.com/posts/pi-durable/), `docs/settings.md`)
- **Divergence**: how a result differs from the task as given. Each report and each submission states it, or says "None" (`AGENTS.md`)

## Agents

- **Agent definition**: a Markdown file with frontmatter that sets the model, thinking level, tools, and instructions of an agent. Built-ins are in `agents/` (`docs/subagents.md`). Early commits call it a "profile" (`703b104`)
- **@ultimate**: the standing agent that the user talks to. It starts and steers branches, and it relays their questions (`agents/ultimate.md`). Code: definition `ultimate`
- **Standing agent**: an agent with one permanent conversation in a project. Nobody concludes it, so it keeps what it learned (`8a1c100`). Code: `resident: true`. Examples: @ultimate and @lander
- **Coordinator**: the agent that runs a branch. It plans, decides, and verifies, and it delegates execution but never judgment (`agents/coordinator.md`). UI: `branch · coordinator`
- **Subagent**: a child conversation that a tool call starts for bounded work. The conversation that started it owns it (`extensions/subagents/README.md`). Not: a branch, which has no owner
- **Worker**: a subagent that does one bounded task in its own isolate and makes one focused commit (`agents/worker.md`)
- **Scout**: a read-only subagent for one code question (`agents/scout.md`)
- **Designer**: a subagent for front-end work (`agents/designer.md`)
- **Reviewer**: a read-only subagent that reviews one fixed commit range. Here, it leads three specialist reviewers (`.ultimate/README.md`)
- **Lander**: the queue that lands submissions, and the standing agent that owns it. Code does the merge, the checks, the fast-forward, and the push. The model works only on a failure or a message (`agents/lander.md`). UI: @lander

## Change and landing

- **Isolate**: a git worktree that belongs to one conversation. It separates files, not processes, so it is not a sandbox (`extensions/subagents/README.md`). Code: the extension `workspaces` and the tool `workspace`
- **Submission**: a request to land the tip of an isolate, made with `workspace submit`. The lander takes submissions one at a time (`docs/worktrees.md`)
- **Landing**: a submission that passed every check and reached the target branch. The tally records each landing (`extensions/lineage/README.md`)
- **Preview**: a separate Ultimate instance that runs one checkout on its own port with the configured models. Code: the extension `instance` (`extensions/instance/README.md`)
- **Supervisor**: the small process in `bin/ultimate.ts` that holds the port and the lock, and starts each generation (`docs/running.md`)
- **Generation**: one core process that the supervisor starts. `ULTIMATE_GENERATION` labels it (`docs/running.md`)
- **Swap**: the change from one generation to the next. The supervisor prepares and type-checks the new generation first, and a failed boot keeps the old one (`docs/running.md`)
- **Restart**: the tool that requests a swap after a change to `server/` or `shared/` (`AGENTS.md`). Not: a human restart with `pnpm start`, which only a change to `bin/` needs

## Extensions

- **Extension**: a folder that adds agent behavior, UI, or both. A later folder with the same name replaces an earlier one (`extensions/README.md`)
- **Built-in**: an extension in the `extensions/` folder of the clone. Eight built-ins ship off, and the others ship on (`shared/extension-api.ts`)
- **Facet**: one side of an extension. `server.ts` holds agent behavior, and `web.tsx` holds UI. Each facet loads and fails alone (`fff6d4b`)
- **Core tier**: the extensions that settings cannot turn off. A core-tier extension depends only on other core-tier extensions (`docs/extensions.md`). Code: `tier = 'core'` in `api.ts`
- **Extension API**: a typed contract that one extension provides and another uses, with `need` when it is required or `want` when it is optional (`docs/extensions.md`)
- **Point**: a contract that a lower extension declares and a higher extension fills, so that dependencies go one way (`docs/extensions.md`)
- **Durable event**: a typed fact that an extension appends in the same commit as its cause (`docs/extensions.md`)
- **Reactor**: a named handler that reads durable events in order, across crashes (`docs/extensions.md`)
- **Document**: typed JSON state that an extension stores with a conversation, in the same commit as the transcript (`docs/durability.md`)
- **Action**: a typed JSON call from the browser or from codemode to a server facet (`extensions/README.md`)
- **Slot**: a named place in the shell where a web facet adds UI, such as the sidebar or the status line (`extensions/README.md`)
- **Panel**: a tab in the right panel (`extensions/README.md`)
- **Surface**: a full-screen app that the user switches to. The Agent surface is the conversation, and the agent stays one keystroke away on every surface (`790c34e`)
- **Codemode**: a tool that runs one JavaScript script in a QuickJS sandbox. The script can call tools and read Ultimate's state (`extensions/codemode/README.md`)

## Messages and the user

- **Message**: a durable delivery from one conversation to another. It wakes an idle recipient (`extensions/messages/README.md`). Code: the extension `messages`, with events named `board.*`
- **Note**: a message that does not start a turn. The recipient reads it when its next turn starts. Code: the tool `note` (`AGENTS.md`)
- **Notify**: a request to know when another conversation finishes. Code: the tool `notify` (`AGENTS.md`)
- **Steer**: a message that enters a run in progress, after the current tool calls (`extensions/messages/README.md`)
- **Question**: a message that expects a reply from the user. An answer card stays open until the user answers or dismisses it (`extensions/questions/README.md`)
- **To-do**: an open item for the user or for @ultimate, in one short list for each project (`extensions/todos/README.md`)
- **Side chat**: a temporary fork of @ultimate for a tangent. The user discards it, or injects a summary into the main conversation (`extensions/side-chat/README.md`)
- **Project trust**: the user's choice to load a project's `.ultimate/` folder. Until the user chooses, Ultimate uses only the global setup. Code: decision `local` or `global` (`docs/settings.md`)

## Background work and records

- **Task**: a unit of work that Pi Durable runs and checkpoints, such as a model request or a tool call ([Pi Durable](https://earendil.com/posts/pi-durable/)). Not: a task in a plan of `extensions/plan/`
- **Replay-safe**: a tool that can run again after a crash with no harm. Pi Durable runs an interrupted tool again only when it has this mark (`docs/durability.md`)
- **Automation**: a schedule that runs an agent prompt as its own conversation (`extensions/automations/README.md`)
- **Subscription**: a supervised script that wakes a conversation when its output says `FIRE` (`extensions/subscriptions/README.md`)
- **Pause**: a hold on new tasks for the whole host. Current work finishes, and Play releases the queue (`extensions/pause/README.md`)
- **Trace**: the record of nested calls of services, actions, reactors, and tools, with their parents (`docs/extensions.md`)
- **Summary model**: the small model for titles, summaries, and abstracts. Code: `summaryModel` (`docs/settings.md`)
- **Chapter**: one named conversation database in a home. Chapters stay side by side, and a journaled switch changes the active chapter (`4c94093`)
- **Dream**: a session in which Ultimate studies its memory, failures, and tools, and then proposes changes. A dream can seed a new chapter (`extensions/dream/README.md`)
- **Backup Worker**: the Cloudflare Worker that stores the backups of a user (`extensions/cloud/README.md`). Not: a worker subagent
- **Backup**: an encrypted copy of a project's database, on the user's own backup Worker. `pnpm restore` installs it on another machine (`extensions/cloud/README.md`)

## North-star terms

- **Brick**: one capability of the system, with its status at the snapshot. See [bricks](bricks/README.md)
- **Decision**: one choice with lasting effect, with its reason and its evidence. See [decisions](decisions/README.md)
- **Snapshot**: the commit that the north-star describes. See [README.md](README.md)
- **Source**: the owner of an intent. `upstream` is Daniel's project, and `uao` is Pascal's direction

## Retired names

Do not use these names for current things:

- **Board**: the old name of the messages extension (`28d657a`) and of a feed surface that `eeae136` removed
- **Canvas**: a map surface that `deb65f8` removed. The upstream branch `park/canvas` keeps it
- **@sync**, **writer lease**, **machine home**, and **move**: parts of the cloud fleet that `67caeb6` removed
- **Faux mode**: a demo mode without tokens that `f23e291` removed. Tests still use Pi's faux provider
- **Exclusive commands**: an extension that `89676a2` removed
