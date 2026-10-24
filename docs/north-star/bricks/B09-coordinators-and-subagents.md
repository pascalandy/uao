# B09 Coordinators and subagents

Status: shipped, at the snapshot. Source: upstream.

A coordinator runs each branch. It assesses the request, plans, decides, and verifies. The coordinator delegates bounded work to subagents. Workers implement, scouts read, designers build UI from screenshots, and a reviewer leads a team of specialist reviewers. The post calls the coordinators "the real heroes of Ultimate".

A coordinator continues unfinished work unless it is blocked or a child, the lander, or a reply will wake it (`agents/coordinator.md`). The watchdog notes branches idle for 30 minutes, or two hours when they wait for another conversation's reply (`extensions/watchdog/idle.ts`). Branches that wait for the user do not count as idle (`extensions/watchdog/idle.ts`).

An overlay can give a coordinator deferred tools, even when its base inherits every tool (`lib/agents.ts`, `extensions/messages/branch.ts`).

## Where it lives

- `agents/coordinator.md`: the coordinator
- `agents/worker.md`, `agents/scout.md`, and `agents/designer.md`: bounded roles
- `agents/reviewer.md` and `.ultimate/agents/`: the review lead and the review team of this repository
- `extensions/subagents/`: delegation
- `extensions/messages/branch.ts`: the branch tool and the coordinator's model
- `lib/agents.ts`: tool inheritance and deferred tools
- `extensions/watchdog/`: failure reports and idle-branch notes

## Decisions

- [D012](../decisions/D012-design-visible-results.md) Design each visible result
- [D020](../decisions/D020-size-the-work.md) Size the work to the change
- [D025](../decisions/D025-assess-first.md) Assess a feature before building it

## Evidence

- `a300225` adds durable subagents
- `79cef07` routes review through one lead
- `7d29e8f` records divergence
- `25d180d` sizes the work to the change
- `f0d80a3` adds the assessment
- `fb51fea` reports failed runs
- `8ff34aa` applies the coordinator definition's model and clamps its thinking level
- `397c368` lets definitions disable automatic summaries
- `1c8a97e` tells agents to reuse passed tests on an unchanged tree
- `a7495cb` shortens the idle threshold and tells coordinators to continue unfinished work
- `d3178ff` passes deferred tools from overlays to coordinator branches
