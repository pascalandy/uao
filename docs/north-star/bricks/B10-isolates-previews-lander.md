# B10 Isolates, previews, and the lander

Status: shipped, at the snapshot. Source: upstream.

Each branch works in its own isolate, a git worktree, so several features run in parallel on the same code. An isolate separates files, not processes, so it is not a sandbox for the shell (`extensions/subagents/README.md`). A coordinator previews its work in a separate Ultimate instance on its own port. When the work is ready, the landing queue merges it, runs every check, and lands only a result that passes every check.

## Where it lives

- `extensions/workspaces/`: isolates and the landing queue
- `agents/lander.md` and `.ultimate/agents/lander.md`: the lander
- `.ultimate/settings.json`: the checks, the push target, and the preview model
- `extensions/instance/`: previews

## Decisions

- [D008](../decisions/D008-worktree-per-conversation.md) Give parallel work its own isolate
- [D010](../decisions/D010-push-without-asking.md) Push landed work without asking again
- [D011](../decisions/D011-lander-queue.md) Land through a durable queue
- [D036](../decisions/D036-previews-on-instance-model.md) Preview every agent on one model

## Evidence

- `1c10440` adds isolates
- `a8acb1b` moves isolates into an extension
- `5c36dcd` adds the landing queue
- `b40b9c2` shares the folder until a project can have isolates
- `4a6d393` previews other projects
- `f23e291` runs previews on the configured models
- `a4843af` makes `instance.model` control every agent in a preview ([D036](../decisions/D036-previews-on-instance-model.md))
