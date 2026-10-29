# Glossary

This file defines the names in uao. Each thing has one name, and each name has one meaning. Use these names in the north-star, in commits, and in prompts.

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
- **Subscription login**: a provider login that Pi marks as a subscription. A conversation on a subscription login never falls back to a pay-per-token login (`extensions/models/fallback.ts`). Not: a subscription, the retired name for a script trigger
- **Pi Durable**: the library `@earendil-works/pi-durable`. It stores each conversation and its tasks, and it resumes them after a crash (`docs/durability.md`)

## Work model

- **Project**: the repository that Ultimate works on. It can be Ultimate's own clone or another repository (`1135742`)
- **Clone**: the checkout of Ultimate's code that the host runs from. Code: `host.ultimateRoot` (`extensions/update/README.md`). Not: the project
- **Home**: the folder that holds the state of one project, by default under `~/.ultimate/projects/` (`docs/running.md`)
- **Conversation**: one durable transcript with its agent, tools, and tasks (`docs/durability.md`)
- **Root**: the top conversation of a project's tree. It becomes a tally when its first branch starts, and then it accepts no input and runs no turns (`extensions/lineage/server.ts`). It holds the project memory and the tally. A project has one root (`extensions/lineage/README.md`)
- **Tally**: the record that a root keeps of its tree. It holds branch intents, abstracts, notes, and landings. UI: **History** page, also called project context. Code: `lineage.tally` (`76eaa574`). Not: the context window of a model
- **History**: the read-only page for a project's tally. The sidebar's project path opens it (`76eaa574`, `6ee7d47c`)
- **Forest**: the word that `AGENTS.md` uses for a project's conversation trees. Since `86ed900`, a project has one root, so its forest holds one tree (inferred)
- **Branch**: a conversation that forks from the root or from a branch to do one feature, fix, or experiment. Its prompt is its first input (`extensions/lineage/README.md`). Not: a subagent
- **Intent**: the one line that names a branch in the tally. The full prompt stays in the branch (`ad1b2dd`)
- **Abstract**: the summary of one conversation in the tally. The abstract changes with the work. A landing keeps the abstract unchanged (`fc99691`)
- **Project memory**: the decisions, facts, and lessons that a root keeps by slug. A new branch starts from a brief of this memory. Code: `lineage.memory`, tool `remember` (`4c1b652`)
- **Memory surface**: the full-screen view of project memory. The sidebar's Memory row opens it (`21669aa1`)
- **Recall**: an input hook that adds relevant project memories to @ultimate's context. It uses the optional `classify` extension (`48f2f2e6`)
- **Catch-up**: the update that a branch receives when it resumes. It holds the new tally events of its tree, then the new commits on its target (`extensions/lineage/README.md`)
- **Conclude**: to close a conversation when its work is done. A concluded conversation stays readable and can resume. Roots and standing agents are never concluded (`AGENTS.md`)
- **Compaction**: a summary of old messages that replaces them in the model context. The old messages stay in storage ([Pi Durable](https://earendil.com/posts/pi-durable/), `docs/settings.md`)
- **Self-compaction**: a conversation's request to compact its own context. Code: `compact`, a deferred tool for top-level conversations (`extensions/lineage/server.ts`). Not: automatic compaction
- **Divergence**: how a result differs from the task as given. Each report and each submission states it, or says "None" (`AGENTS.md`)

## Agents

- **Agent definition**: a Markdown file with frontmatter for an agent's model, tools, and instructions. Built-ins live in `agents/` or an enabled extension's `agents/` folder (`ab959a36`). Early commits call it a "profile" (`703b104`)
- **Agents tab**: the UI tab where the user edits agent definitions (`extensions/subagents/README.md`). UI: **Agents tab**. Not: the Agent surface
- **Overlay**: an agent definition with the name of an earlier definition and an `addTools` key. It can change settings, add tools, and append text, but it keeps the earlier instructions (`docs/subagents.md`, `9d40a9b`)
- **Deferred tool**: a tool that loads when an agent definition names it, including through an overlay's `addTools` (`lib/agents.ts`, `d3178ff`)
- **Skill**: instructions that an agent reads for a task, stored in `SKILL.md`. A `/skill:name` command adds the named skill to user input (`server/skills.ts`)
- **Top-level agent**: the agent of a conversation that is not a subagent, such as @ultimate or a coordinator (inferred). Only a top-level agent pushes (`docs/worktrees.md`). Not: a subagent
- **@ultimate**: the standing agent that the user talks to. It starts and steers branches, and it relays their questions (`agents/ultimate.md`). Code: definition `ultimate`
- **Standing agent**: an agent with one permanent conversation in a project. Nobody concludes it, so it keeps what it learned (`8a1c100`). Code: `resident: true`. Examples: @ultimate and Voice (`f3b257b6`). Not: the model-free lander (`cfd0e93b`)
- **Voice**: the standing agent that answers spoken status questions and forwards work to @ultimate. GPT-Live carries its audio (`f3b257b6`, `26c21a52`)
- **GPT-Live**: the audio model that hears and speaks in a live voice session. Voice decides which requests reach @ultimate (`extensions/voice-live/README.md`)
- **Coordinator**: the agent that runs a branch. It plans, decides, and verifies. It delegates execution but never judgment (`agents/coordinator.md`). UI: `branch · coordinator`
- **Subagent**: a child conversation that a tool call starts for bounded work. The parent conversation owns the subagent (`extensions/subagents/README.md`). Not: a branch, which has no owner
- **Worker**: a subagent that does one bounded task in its own isolate and makes one focused commit (`agents/worker.md`)
- **Scout**: a read-only subagent for one code question (`agents/scout.md`)
- **Designer**: a subagent for front-end work (`agents/designer.md`)
- **Watcher**: the agent that owns one automation with a script trigger, and writes and repairs its script (`agents/watcher.md`)
- **Reviewer**: a read-only subagent that reviews one fixed commit range. Here, it leads three specialist reviewers (`.ultimate/README.md`)
- **Landing queue**: the durable queue of submissions. Its code lands them one at a time, in order ([D042](decisions/D042-model-free-landing.md))
- **Lander**: the code that processes the landing queue. Its conversation records the log, refuses input, and runs no model (`cfd0e93b`). UI: @lander

## Change and landing

- **Isolate**: a git worktree that belongs to one conversation (`extensions/subagents/README.md`). Code: the extension `workspaces` and the tool `workspace`
- **Submission**: a request to land the tip of an isolate, made with `workspace submit`. The landing queue takes submissions one at a time (`docs/worktrees.md`)
- **Landing**: a submission that passed every check and reached the target branch. The tally records each landing (`extensions/lineage/README.md`)
- **Change unit**: the work of one conversation in Git. Its commits carry the trailer `Ultimate-Conversation: <n>`. Its isolate uses the Git branch `ultimate/<hash>-<n>` (`extensions/workspaces/workspaces.ts`). See [history.md](history.md#life-of-a-change-unit)
- **Work commit**: a commit that is not a merge
- **Trailer**: a `Key: value` line at the end of a commit message. The `bash` tool of Ultimate adds `Ultimate-Conversation: <n>` (`extensions/coding-tools/server.ts`)
- **Landing note**: the entry that the tally records for each landing (`extensions/lineage/README.md`)
- **Landing merge**: the merge commit that the queue makes when integration cannot fast-forward. Its message is `Merge <sha> from #<n> into main` (`extensions/workspaces/lander.ts`). Before `19f960d`, the message named `W<n>`. Not: a merge of `main` into a Git branch
- **Preview**: a separate Ultimate instance that runs one checkout on its own port. Code: the extension `instance` (`extensions/instance/README.md`). [D036](decisions/D036-previews-on-instance-model.md) records its model setting
- **Supervisor**: the small process in `bin/ultimate.ts` that holds the port and the lock, and starts each generation (`docs/running.md`)
- **Generation**: one core process that the supervisor starts. `ULTIMATE_GENERATION` labels it (`docs/running.md`)
- **Swap**: the change from one generation to the next. The supervisor prepares and type-checks the new generation first. If the new generation fails to boot, the supervisor keeps the old generation (`docs/running.md`)
- **Restart**: the tool that requests a swap after a change to `server/` or `shared/` (`AGENTS.md`). Not: a human restart with `pnpm start`, which only a change to `bin/` needs

## Extensions

- **Extension**: a folder that adds agent behavior, UI, or both. A later folder with the same name replaces an earlier one (`extensions/README.md`)
- **Built-in**: an extension in the `extensions/` folder of the clone (`docs/settings.md`)
- **Facet**: one side of an extension. `server.ts` holds agent behavior, and `web.tsx` holds UI. Each facet loads and fails independently (`fff6d4b`)
- **Core tier**: the extensions that settings cannot turn off. A core-tier extension depends only on other core-tier extensions (`docs/extensions.md`). Code: `tier = 'core'` in `api.ts`
- **Extension API**: a typed contract that one extension provides and another uses. The second extension uses `need` for a required contract or `want` for an optional contract (`docs/extensions.md`)
- **Point**: a contract that a lower extension declares and a higher extension fills, so that dependencies go one way (`docs/extensions.md`)
- **Durable event**: a typed fact that an extension appends in the same commit as its cause (`docs/extensions.md`)
- **Reactor**: a named handler that reads durable events in order, across crashes (`docs/extensions.md`)
- **Document**: typed JSON state that an extension stores with a conversation, in the same commit as the transcript (`docs/durability.md`)
- **Action**: a typed JSON call from the browser or from codemode to a server facet (`extensions/README.md`)
- **Slot**: a named place in the shell where a web facet adds UI, such as the sidebar or the status line (`extensions/README.md`)
- **Panel**: a tab in the right panel (`extensions/README.md`)
- **Surface**: a full-screen app that the user switches to. The Agent surface is the conversation. The agent is accessible with one keystroke on every surface (`790c34e`)
- **Codemode**: a tool that runs one JavaScript script in a QuickJS sandbox. The script can call tools and read Ultimate's state (`extensions/codemode/README.md`)

## Messages and the user

- **Message**: a durable delivery that wakes its recipient. One-way updates to a subagent's parent or a branch's starter become notes instead (`136d9c01`). Code: extension `messages`, events `board.*`
- **Note**: context that starts no turn. The `note` tool writes context for the recipient's next input (`extensions/lineage/README.md`). Upward one-way messages reach its next model request, also during a run (`extensions/messages/README.md`). Not: the comment field on an answer card, whose reply wakes the sender (`extensions/questions/README.md`)
- **Starter**: the conversation that called `branch`. Code: a branch's `board.started` document (`extensions/messages/branch.ts`)
- **Report**: a branch's final answer that wakes its starter when no work remains under way. Code: `report: true` (`136d9c01`)
- **Notify**: a request to know when another conversation finishes. Code: the tool `notify` (`AGENTS.md`)
- **Steer**: a message that enters a run in progress, after the current tool calls (`extensions/messages/README.md`)
- **Question**: one structured request for a user answer, carried by a message (`extensions/messages/questions.ts`). Its answer card stays open until the user answers or dismisses the message (`extensions/questions/README.md`)
- **Hands-off goal**: a user-granted goal during which @ultimate decides what it would otherwise ask the user (`extensions/goal/README.md`). Code: the extension `goal`. Chapter changes still require the user (`ef738270`)
- **Goal decision**: a choice that @ultimate records for the user during a hands-off goal, including the reason (`extensions/goal/README.md`). Code: `goal {action: 'decide'}`. Not: a north-star decision
- **Goal report**: the card that records a hands-off goal's outcome, criteria, summary, and goal decisions (`extensions/goal/README.md`). UI: **Hands-off report**. Code: `goal.report`
- **To-do**: an open item for the user or for @ultimate, in one short list for each project (`extensions/todos/README.md`)
- **Side chat**: a temporary fork of @ultimate for a tangent. The user discards it, or injects a summary into the main conversation (`extensions/side-chat/README.md`)
- **Voice input**: microphone recording that becomes unsent text at the composer's cursor. Not: a live voice session (`a0608d3f`)
- **Installable web app**: the browser app installed on a device's home screen, with standalone display (`web/public/manifest.webmanifest`, `12fd115c`)
- **Project trust**: the user's choice to load a project's `.ultimate/` folder. Until the user chooses, Ultimate uses only the global setup. Code: decision `local` or `global` (`docs/settings.md`)

## Background work and records

- **Task**: a unit of work that Pi Durable runs and checkpoints, such as a model request or a tool call ([Pi Durable](https://earendil.com/posts/pi-durable/)). Not: a task in a plan of `extensions/plan/`
- **Replay-safe**: a tool that can run again after a crash with no harm. Pi Durable runs an interrupted tool again only when it has this mark (`docs/durability.md`)
- **Automation**: a rule for background work that acts when its trigger fires. Code: the tool `automation` (`extensions/automations/README.md`)
- **Trigger**: the condition that fires an automation. A trigger uses a schedule, a script, a domain event, or a context threshold (`extensions/automations/README.md`)
- **Script trigger**: a trigger that runs a supervised script with no model calls. The script fires its automation when it prints `FIRE` (`extensions/automations/README.md`)
- **Pause**: a hold on new tasks for the whole host. Current work finishes, and Play releases the queue (`extensions/pause/README.md`). The user's **Play by itself** setting can release rate-limit pauses ([B12](bricks/B12-human-in-the-loop.md))
- **Trace**: the record of nested calls of services, actions, reactors, and tools, together with the parents of those calls (`docs/extensions.md`)
- **Summary model**: the small model for titles, summaries, and abstracts. Code: `summaryModel` (`docs/settings.md`)
- **Keep warm**: optional cache pings for idle @ultimate on Claude Code. They renew an existing cache without transcript entries (`f9d91e85`, `extensions/keep-warm/README.md`)
- **Chapter**: one named conversation database in a home. Chapters stay side by side, and a journaled switch changes the active chapter (`4c94093`)
- **Dream**: ordinary branch work that studies the project and proposes changes. @ultimate can then prepare a fresh chapter (`be1608a7`)
- **Prepared chapter**: a chapter name, three learned lines, and a handover that @ultimate records before the user presses Fall asleep (`extensions/dream/refs.ts`)
- **Backup Worker**: the Cloudflare Worker that stores the backups of a user (`extensions/cloud/README.md`). Not: a worker subagent
- **Backup**: an encrypted copy of a project's database, on the user's own backup Worker. `pnpm restore` installs it on another machine (`extensions/cloud/README.md`)
- **Satellite**: a machine that runs a project but never uploads its backups. Code: `cloud.satellite` in user settings (`2bfc6b22`)
- **Remotes**: user settings that map machine and project names to running instance URLs. They permit remote reads and messages without cloud backups (`2a6d9e51`)
- **Tombstone**: a project memory that records a removed or rejected idea and its reason (`63f87af5`)

## North-star terms

- **Brick**: one capability of the system, with its status at the snapshot. See [bricks](bricks/README.md)
- **Decision**: one choice with lasting effect, with its reason and its evidence. See [decisions](decisions/README.md). Not: a goal decision
- **Snapshot**: the commit that the north-star describes. See [upstream.md](upstream.md#snapshot)
- **Era**: a span of days in the history of upstream with one main theme. See [history.md](history.md#eras)
- **Seam**: a place where new behavior attaches with no edit to an upstream file. See [evolution.md](evolution.md#seams)
- **Source**: the owner of an intent. `upstream` is Daniel's project, and `uao` is Pascal's direction

## Retired names

Do not use these names for current things:

- **Board**: the old name of the messages extension (`28d657a`) and of a feed surface that `eeae136` removed
- **Canvas**: a map surface that `deb65f8` removed. The upstream branch `park/canvas` keeps it
- **@sync**, **writer lease**, and **move**: parts of the cloud fleet that `67caeb6` removed
- **Machine home**: the home of @sync on each machine. `1708844` removed it
- **Faux mode**: a demo mode without tokens that `f23e291` removed. Tests still use Pi's faux provider
- **Exclusive commands**: an extension that `89676a2` removed
- **Subscription**: the old name for a script trigger. `e099781` replaced subscriptions with script triggers in automations. Not: a subscription login
- **Automation grant**: approval for an automation's dream, compaction, or chapter action. `ef738270` removed grants and the `act` operation
- **Triage**: the model's former decision about whether a message should wake @ultimate. `136d9c01` replaced it with state-based waking
- **Graveyard**: the short-lived folder for rejected ideas. `63f87af5` replaced it with tombstones in project memory
- **Emergency terminal agent**: the former server-independent recovery agent. `17d186bf` removed `pnpm cli` and `ultimate --cli`
