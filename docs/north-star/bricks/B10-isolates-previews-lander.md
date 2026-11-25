# B10 Isolates, previews, and the lander

Status: shipped, at the snapshot. Source: upstream.

Each branch works in its own isolate, so several features can change the same code (`extensions/workspaces/README.md`). An isolate separates files, not processes (`extensions/subagents/README.md`). A coordinator previews its work in a separate Ultimate instance (`extensions/instance/README.md`).

Only `workspace submit` reaches the project's target branch ([D042](../decisions/D042-model-free-landing.md)). The model-free lander checks and lands the submission (`cfd0e93b`). It wakes the starter only when the landing concludes the branch (`extensions/workspaces/lander.ts`). Failures wake the submitter to fix and submit again (`cfd0e93b`).

A project can configure checkout paths and creation and removal commands (`2affc7ad`, `3b71cca5`). Clean checkouts can be released while their unlanded commits stay on their Git branches (`cfd0e93b`). The [workspace mechanics](../../../extensions/workspaces/README.md) describe safe recreation and cleanup.

Previews copy user configuration into a private user home (`1efbcb19`). Since `4360a446`, that copy includes the user extensions, and only the Tailscale registry stays linked. A preview refuses a relative home and a reused home that still links live user extensions (`4360a446`, `18c24554`). A released checkout is recreated before the next tool call (`27f9d781`).

A preview's `HOME` is its own folder, with the other entries of the real home linked back, so writes to `~/.ultimate` stay private (`8f67613f`). A preview lands on its own branch and never pushes (`d1fe28fb`). The lander log shows the running step and the duration of each step (`a1825fcd`). Each step names the check that it runs (`e0b337a3`). A landing card shows the changed lines and the estimated tokens (`f7ba0607`). A temporary folder that is still being written no longer fails a landing (`c99fc625`).

A landing's weight now counts only its diff, and a repository too large to weigh never fails a landing (`e59a9873`, `e4a143e3`). The lander runs the tests with `TMPDIR` on tmpfs again, not in the host home (`412781c0`). The starter gets a one-line landing card that names the pushed commit, with the divergence (`cbc96a2c`, `9bd52084`). The landing card also shows the acceptance criteria that the branch met ([B07](B07-conversation-tree.md), `53e54861`).

A crash no longer leaves preview servers running (`058c555e`). A preview with read-only copies or a deleted home still stops (`c65112fb`). `instance start` can take a model for one start, so a check does not edit the user settings (`06c356c2`). A sidebar row shows `reviewing`, `preview up`, or `preview awaits you` for a branch (`655ed511`, `extensions/sidebar/root.solid.tsx`).

The lander runs `pnpm check`, then `pnpm test:affected` (`.ultimate/settings.json`). `scripts/test.ts` selects the tests that a change reaches. A change to `server/`, `shared/`, `lib/`, `lint/`, `web/src/sdk/`, a config, or the lockfile runs both whole suites (`1e9f8a23`, [Conventions](../../../AGENTS.md#conventions)). One whole-suite run at a time takes a lock for the machine (`3ba7a725`). Lander checks and previews run in capped cgroups when the service allows it ([B05](B05-agent-tools.md), `f00dd1b6`). A flaky check names what failed on its first run (`396e2705`). A checkout that Git cannot count no longer stops a release (`ee39e668`).

## Where it lives

- `extensions/workspaces/`: isolates and the landing queue
- `extensions/workspaces/lander.ts`: the queue and its model-free log conversation
- `.ultimate/settings.json`: the checks, the push target, and the preview family assignment
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
- `27f9d781` keeps source checkouts with live descendant worktrees. `1a0541ee` removes that PR's additional lander conclusion guard
- `d1fe28fb` keeps previews from landing on the previewed branch and from pushing
- `9a79b7f9` adds the `Ultimate-Conversation` trailer to each landing merge
- `e59a9873` makes a landing's weight count only its diff
- `058c555e` stops the preview servers that a crash left running
- `cbc96a2c` gives the starter a one-line landing card
