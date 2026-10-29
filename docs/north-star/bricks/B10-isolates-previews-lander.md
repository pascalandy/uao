# B10 Isolates, previews, and the lander

Status: shipped, at the snapshot. Source: upstream.

Each branch works in its own isolate, so several features can change the same code (`extensions/workspaces/README.md`). An isolate separates files, not processes (`extensions/subagents/README.md`). A coordinator previews its work in a separate Ultimate instance (`extensions/instance/README.md`).

Only `workspace submit` reaches the project's target branch ([D042](../decisions/D042-model-free-landing.md)). The model-free lander checks and lands the submission, then wakes the starter (`cfd0e93b`). Failures wake the submitter to fix and submit again (`cfd0e93b`).

A project can configure checkout paths and creation and removal commands (`2affc7ad`, `3b71cca5`). Clean checkouts can be released while their unlanded commits stay on their Git branches (`cfd0e93b`). The [workspace mechanics](../../../extensions/workspaces/README.md) describe safe recreation and cleanup.

## Where it lives

- `extensions/workspaces/`: isolates and the landing queue
- `extensions/workspaces/lander.ts`: the queue and its model-free log conversation
- `.ultimate/settings.json`: the checks, the push target, and the preview model
- `extensions/instance/`: previews

## Decisions

- [D008](../decisions/D008-worktree-per-conversation.md) Give parallel work its own isolate
- [D010](../decisions/D010-push-without-asking.md) Push landed work without asking again
- [D042](../decisions/D042-model-free-landing.md) Use one model-free path to the target branch
- [D036](../decisions/D036-previews-on-instance-model.md) Preview every agent on one model
- [D037](../decisions/D037-goals-delegate-approvals.md) Let a user-granted goal delegate approvals

## Evidence

- `1c10440` adds isolates
- `a8acb1b` moves isolates into an extension
- `5c36dcd` adds the landing queue
- `b40b9c2` shares the folder until a project can have isolates
- `4a6d393` previews other projects
- `f23e291` runs previews on the configured models
- `a4843af` makes `instance.model` control every agent in a preview ([D036](../decisions/D036-previews-on-instance-model.md))
- `1a974c40` names failed tests on every failed check
- `b7060d00` records the landing decision once and preserves safe checkout release
- `903ce43e` keeps one wake-up per landed branch
