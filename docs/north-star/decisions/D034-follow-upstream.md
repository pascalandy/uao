# D034 Follow upstream through merges

Decided 2026-10-23, revised 2026-11-09. Source: uao. Status: active.

Each Wednesday, the job `uao-sync` merges `upstream/main` into uao through a pull request with a merge commit. The job merges that pull request without Pascal when the checks pass and both of the job's review loops approve: one by a DeepSeek model and one by a Codex model (Pascal, 2026-11-09). To undo one sync, run `git revert -m 1 <merge>` on a branch, and merge that revert through a pull request. uao keeps its own additions in places that upstream does not edit, to decrease the risk of a merge conflict. After each merge, an agent updates the north-star in the same pull request.

**Why.** Pascal wants Daniel's changes without a conflict at each merge (Pascal, 2026-10-23). A weekly merge keeps uao from falling weeks behind upstream (Pascal, 2026-11-09).

**Rejected.** A merge only when Pascal wants upstream's changes, the rule from 2026-10-23 to 2026-11-09.

**Evidence.** Pascal stated the first rule on 2026-10-23. Pascal approved the weekly job on 2026-11-09. The fork commit `7698625` shows the fork point, not the rule. `e683f686` is the first merge of the job. The [sync rule](../upstream.md#sync-rule) holds the steps and the places for additions.
