# B10 Isolates, previews, and the lander

Status: shipped, at the snapshot. Source: upstream.

Each branch works in its own isolate, a git worktree, so several features run in parallel on the same code. A coordinator previews its work in a separate Ultimate instance on its own port. When the work is ready, the lander merges it, runs every check, and lands only a green result.

## How it works

`workspaces` gives a conversation an isolate when the project has a Git branch and a first commit. `workspace submit` puts the tip in a queue. Code merges, checks, fast-forwards, and pushes, and the lander's model only diagnoses or fixes a failure. `.ultimate/settings.json` sets the checks and the push target of this repository. `instance` starts a clean preview on the configured models. [Worktrees and integration](../../../docs/worktrees.md) holds the mechanics.

## Where it lives

- `extensions/workspaces/`: isolates and the landing queue
- `agents/lander.md` and `.ultimate/agents/lander.md`: the lander
- `.ultimate/settings.json`: the checks and the push target
- `extensions/instance/`: previews

## Decisions

- [D008](../decisions/D008-worktree-per-conversation.md) Give parallel work its own isolate
- [D010](../decisions/D010-push-without-asking.md) Push landed work without asking again
- [D011](../decisions/D011-lander-queue.md) Land through a durable queue
- [D030](../decisions/D030-previews-on-real-models.md) Preview on the configured models

## Next

- Nothing stated

## Evidence

- `1c10440` adds isolates
- `a8acb1b` moves isolates into an extension
- `5c36dcd` adds the landing queue
- `b40b9c2` shares the folder until a project can have isolates
- `4a6d393` previews other projects
- `f23e291` runs previews on the configured models
