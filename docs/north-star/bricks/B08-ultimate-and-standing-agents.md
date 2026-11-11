# B08 @ultimate and standing agents

Status: shipped, at the snapshot. Source: upstream.

The user talks to one agent, @ultimate, which keeps its conversation between visits (`agents/ultimate.md`). @ultimate prepares the project, keeps the project memory and the project's to-dos, and starts and steers branches (`agents/ultimate.md`).

@ultimate can also pursue a user-granted hands-off goal ([B12](B12-human-in-the-loop.md), `agents/ultimate.md`).

The first-run walkthrough introduces Ultimate before project setup (`79107fdd`). It supports replay and skipping the remaining steps (`79107fdd`, `skills/how-ultimate-works/SKILL.md`). Start here stays in @ultimate's conversation until setup runs or the user dismisses it (`c5ec041a`, `08c63235`). An onboarding start whose run failed before an answer, for example because of an expired login, can start again (`b59483eb`, `e77a4a21`, `extensions/onboarding/README.md`).

Voice can be a standing agent when live voice is enabled ([B12](B12-human-in-the-loop.md), `f3b257b6`). The lander is now code with a log conversation ([D042](../decisions/D042-model-free-landing.md)).

@ultimate derives other local projects and their standing agents from project manifests (`08d193b3`, `extensions/messages/remote.ts`). The subagent prompt derives agent models from current definitions (`08d193b3`, `extensions/subagents/server.ts`). Instructions prohibit storing those derived facts in project memory (`08d193b3`, `agents/ultimate.md`).

## Where it lives

- `agents/ultimate.md`: the definition of @ultimate
- `extensions/subagents/`: standing conversations
- `extensions/onboarding/`: project setup through @ultimate
- `extensions/agent/`: the Agent surface

## Decisions

- [D017](../decisions/D017-questions-get-proposals.md) Explore questions, act on instructions
- [D037](../decisions/D037-goals-delegate-approvals.md) Let a user-granted goal delegate approvals
- [D019](../decisions/D019-standing-agents.md) Keep standing agents
- [D044](../decisions/D044-branches-ask-the-user.md) Let branches ask after @ultimate weighs in

## Evidence

- `8a1c100` adds standing agents
- `0319295` prepares projects through @ultimate
- `4d3605e` routes messages for the user through @ultimate
- `eeae136` replaces the Board surface with the @ultimate button
- `001a193d` adds the goal role to @ultimate
- `33f42e7f` lets an experienced user turn onboarding off in user settings
- `b59483eb` and `e77a4a21` let a failed onboarding start run again
