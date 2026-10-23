# B08 @ultimate and standing agents

Status: shipped, at the snapshot. Source: upstream.

The user talks to one agent, @ultimate, which knows the project and stays the same each time the user comes back. @ultimate onboards the project, keeps its memory and to-dos, and starts and steers branches. Other standing agents, such as @lander, keep their own conversation and what they learned.

## How it works

A definition with `resident: true` owns one permanent conversation in each project, and nobody concludes it. A button in the top bar and the first sidebar row open @ultimate from every surface. Questions and results for the user arrive in its transcript. A project can add its own standing agents in its `.ultimate/agents/`. [Subagents](../../../docs/subagents.md) holds the mechanics.

## Where it lives

- `agents/ultimate.md`: the definition of @ultimate
- `extensions/subagents/`: standing conversations
- `extensions/onboarding/`: project setup through @ultimate
- `extensions/agent/`: the Agent surface

## Decisions

- [D017](../decisions/D017-questions-get-proposals.md) Explore questions, act on instructions
- [D019](../decisions/D019-standing-agents.md) Keep standing agents
- [D022](../decisions/D022-talk-to-ultimate.md) Let the user talk only to @ultimate

## Next

- Nothing stated

## Evidence

- `8a1c100` adds standing agents
- `0319295` sets projects up through @ultimate
- `4d3605e` routes messages for the user through @ultimate
- `eeae136` replaces the Board surface with the @ultimate button
