# B08 @ultimate and standing agents

Status: shipped, at the snapshot. Source: upstream.

The user talks to one agent, @ultimate, which knows the project and stays the same each time the user returns. @ultimate prepares the project, keeps the project memory and the project's to-dos, and starts and steers branches. Other standing agents, such as @lander, keep their own conversation and what they learned.

@ultimate can also pursue a user-granted hands-off goal ([B12](B12-human-in-the-loop.md), `agents/ultimate.md`).

## Where it lives

- `agents/ultimate.md`: the definition of @ultimate
- `extensions/subagents/`: standing conversations
- `extensions/onboarding/`: project setup through @ultimate
- `extensions/agent/`: the Agent surface

## Decisions

- [D037](../decisions/D037-goals-delegate-approvals.md) Let a user-granted goal delegate approvals
- [D019](../decisions/D019-standing-agents.md) Keep standing agents
- [D022](../decisions/D022-route-through-ultimate.md) Route agent messages for the user through @ultimate

## Evidence

- `8a1c100` adds standing agents
- `0319295` prepares projects through @ultimate
- `4d3605e` routes messages for the user through @ultimate
- `eeae136` replaces the Board surface with the @ultimate button
- `001a193d` adds the goal role to @ultimate
