# B09 Coordinators and subagents

Status: shipped, at the snapshot. Source: upstream.

A coordinator runs each branch. It assesses the request, plans, decides, and verifies, and it delegates bounded work to subagents. Workers implement, scouts read, designers build UI from screenshots, and a reviewer leads a team of specialist reviewers. The post calls the coordinators "the real heroes of Ultimate".

## How it works

`subagents` starts each child as its own conversation, in the foreground or the background, from an agent definition. A child survives a stop of its parent. The coordinator makes a small change itself and sends substantive work through workers and review. Each report states its divergence from the task. `watchdog` reports a failed run to its owner. [Subagents](../../../docs/subagents.md) holds the mechanics.

## Where it lives

- `agents/coordinator.md`: the coordinator
- `agents/worker.md`, `agents/scout.md`, and `agents/designer.md`: bounded roles
- `agents/reviewer.md` and `.ultimate/agents/`: the review lead and the review team of this repository
- `extensions/subagents/`: delegation
- `extensions/watchdog/`: failure reports

## Decisions

- [D012](../decisions/D012-design-visible-results.md) Design each visible result
- [D020](../decisions/D020-size-the-work.md) Size the work to the change
- [D025](../decisions/D025-assess-first.md) Assess a feature before building it

## Next

- Nothing stated

## Evidence

- `a300225` adds durable subagents
- `79cef07` routes review through one lead
- `7d29e8f` records divergence
- `25d180d` sizes the work to the change
- `f0d80a3` adds the assessment
- `fb51fea` reports failed runs
