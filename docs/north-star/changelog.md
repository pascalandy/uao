# Changelog review

Source: upstream. This review uses the public [changelog](https://danielgriesser.com/ultimate/changelog/) and its [JSON feed](https://danielgriesser.com/ultimate/changelog/feed.json). The review date is 2026-11-02 UTC.

Four of the eight entries are in the [snapshot](upstream.md#snapshot). Four entries describe later upstream code. This review leaves the snapshot unchanged.

## Entries in the snapshot

Each commit below is an ancestor of the snapshot. The linked brick describes the capability.

| Published  | Change                                                         | Commit     | Brick                                    |
| ---------- | -------------------------------------------------------------- | ---------- | ---------------------------------------- |
| 2026-11-01 | Optional spoken notifications                                  | `451ac392` | [B12](bricks/B12-human-in-the-loop.md)   |
| 2026-10-31 | Image drops attach to the draft. File drops keep the page open | `3fa3753c` | [B12](bricks/B12-human-in-the-loop.md)   |
| 2026-10-28 | Project memory has a separate view                             | `21669aa1` | [B07](bricks/B07-conversation-tree.md)   |
| 2026-10-25 | Dreams can start after a long pause                            | `6c37a236` | [B15](bricks/B15-dreams-and-chapters.md) |

## Entries after the snapshot

These changes are upstream-only at this review. Each row links to the published entry and every commit that its feed record lists.

| Published  | Change                                                                                                                       | Upstream commits                                                                                                                                                                                                                                                                                                                                                                                                          | Related brick                                   |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| 2026-11-01 | [Branch summaries appear on desktop hover](https://danielgriesser.com/ultimate/changelog/summary-history/)                   | [Summary history](https://github.com/HazAT/ultimate/commit/870a0217313811ad53213bd2e4c0b113ffea3ef4), [tooltip cleanup](https://github.com/HazAT/ultimate/commit/118814f98562fbd615de42a8a1bdb4befc57255a)                                                                                                                                                                                                                | [B07](bricks/B07-conversation-tree.md)          |
| 2026-11-01 | [Sketch is removed](https://danielgriesser.com/ultimate/changelog/sketch-removed/)                                           | [Removal](https://github.com/HazAT/ultimate/commit/e69099450e14f8b3bcdcdb758f1a3a951b752b2b)                                                                                                                                                                                                                                                                                                                              | [B05](bricks/B05-agent-tools.md)                |
| 2026-11-01 | [Conversation updates redraw fewer components](https://danielgriesser.com/ultimate/changelog/fewer-rerenders/)               | [Store and hooks](https://github.com/HazAT/ultimate/commit/830a36c14696e3e710e7cd976e7a69a9f2a48614)                                                                                                                                                                                                                                                                                                                      | [B14](bricks/B14-everything-on-record.md)       |
| 2026-11-01 | [A helper starts child processes with fewer host pauses](https://danielgriesser.com/ultimate/changelog/fewer-launch-stalls/) | [Helper](https://github.com/HazAT/ultimate/commit/4b3144083ef54879c8dadd9e7d6b130fc47b6f71), [stream handling](https://github.com/HazAT/ultimate/commit/f9d5a689f59ab8006224082bfce283c896bb2e06), [output cleanup](https://github.com/HazAT/ultimate/commit/afffdf68cdc0907f876f26fffe1ac262f3778d5b), [less Git and transcript work](https://github.com/HazAT/ultimate/commit/5c610524627d1956c42fccf676466dd7c2a3603a) | [B09](bricks/B09-coordinators-and-subagents.md) |

Sketch still exists in the snapshot. Its later removal does not change the current status of B05. The performance figures in the changelog are upstream measurements. This review does not repeat those measurements.

## Other commits after the snapshot

This review checks [the fetched upstream head](https://github.com/HazAT/ultimate/commit/984b887d6aa99e1121fc6fd7060ddd8d320bcc23). That head contains 39 commits after the snapshot: 28 work commits and 11 merges. The fetched head has a UTC date of 2026-11-01.

Other changes include:

- [Previews use private copies of user settings, agents, and skills through `HOME`](https://github.com/HazAT/ultimate/commit/8f67613f)
- [A host restart after a failed extension reload](https://github.com/HazAT/ultimate/commit/f20cc792), when the running core is older than the code
- [Agent definitions supplied when a subagent starts](https://github.com/HazAT/ultimate/commit/6b0fb859)
- [A pinned current prompt](https://github.com/HazAT/ultimate/commit/507b378f), with [later pin behavior](https://github.com/HazAT/ultimate/commit/1cab961b)
- [Images limited to the current turn](https://github.com/HazAT/ultimate/commit/6cc90767) when a message uses `latest`
- [Separate navigation for automated browser pages](https://github.com/HazAT/ultimate/commit/0040f365)

The published feed selects changes. The feed is not a complete record of upstream commits.

## Reproduce the comparison

These commands use the fetched remote. The first result counts all commits. The second counts work commits. The last command checks the narrator commit against the snapshot.

```bash
git rev-list --count d0a2e17b..984b887d
git rev-list --count --no-merges d0a2e17b..984b887d
git merge-base --is-ancestor 451ac392 d0a2e17b
```

An exit code of zero means that the commit is present. An exit code of one means that the commit is absent. All 12 commits listed by the eight feed entries were checked.

`git merge-tree --write-tree HEAD upstream/main` found no conflicts against the reviewed fork head, `d7d484bd`. This check creates no worktree changes. It does not run the checks required for a sync. A future sync follows the [sync rule](upstream.md#sync-rule).
