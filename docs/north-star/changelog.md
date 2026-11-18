# Changelog review

Source: upstream. This review uses the public [changelog](https://danielgriesser.com/ultimate/changelog/) and its [JSON feed](https://danielgriesser.com/ultimate/changelog/feed.json). The review uses the feed as it was fetched at 07:03 UTC on 2026-11-18.

At that fetch, the feed had 28 entries. Each commit that an entry lists is an ancestor of the [snapshot](upstream.md#snapshot). No entry described code after the snapshot.

Later on 2026-11-18, upstream added two entries, [a reel of a branch's screenshots](https://danielgriesser.com/ultimate/changelog/reel/) and [talk a question through](https://danielgriesser.com/ultimate/changelog/talk-it-through/). Their seven commits are not in the snapshot, so the next sync reviews them. Upstream also added 12 commits to the fixes entry of 16 November and dated it 2026-11-17. These 12 commits are in the snapshot.

## Entries in the snapshot

The linked brick describes the capability. A row marked "this sync" lists commits that reached uao with the merge of `6b6d88b6`. A row marked "earlier" lists commits that reached uao with an earlier merge. A row marked "both" lists commits of the two kinds.

| Published  | Change                                             | Commits                                        | Brick                                          | Sync      |
| ---------- | -------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | --------- |
| 2026-11-17 | Spoken answers with Read aloud                     | `e78fefa8`, `56c3d7a2`, `2dd6eac1`             | [B12](bricks/B12-human-in-the-loop.md)         | this sync |
| 2026-11-16 | Fixes of the week of 16 November, 16 commits       | `fa11fd0c` to `cd77dc1e`, note 3               | Several                                        | this sync |
| 2026-11-16 | A skills list for each agent                       | `85b68619`                                     | [B06](bricks/B06-project-specialization.md)    | this sync |
| 2026-11-16 | What each conversation waits on                    | `900c96cc`, `fe4abaeb`, `20941e80`             | [B11](bricks/B11-notes-and-messages.md)        | this sync |
| 2026-11-15 | Fixes of the week of 9 November, 49 commits        | `8e944092` to `1fb18e43`, note 2               | Several                                        | both      |
| 2026-11-14 | The projects rail                                  | `f5e963f1`, `55da7426`, `0197a6a2`, note 4     | [B16](bricks/B16-remote-backup-update.md)      | this sync |
| 2026-11-12 | Answers to questions by voice                      | `799df8e1`                                     | [B12](bricks/B12-human-in-the-loop.md)         | this sync |
| 2026-11-10 | The Inbox                                          | `995c52d4`, `364a3c50`, `cfccc89c`             | [B12](bricks/B12-human-in-the-loop.md)         | earlier   |
| 2026-11-09 | Wire, the raw record of model calls                | `1dd3e145`, `9b8f1866`, `c16450c9`             | [B14](bricks/B14-everything-on-record.md)      | earlier   |
| 2026-11-08 | Push notifications and the share target            | `ff44988c`, `b17e228e`                         | [B12](bricks/B12-human-in-the-loop.md)         | earlier   |
| 2026-11-08 | More room on a phone                               | `1be263cf`                                     | [B12](bricks/B12-human-in-the-loop.md)         | earlier   |
| 2026-11-07 | Fixes of the week of 2 November, 29 commits        | `3d922572` to `630b6940`, note 1               | Several                                        | earlier   |
| 2026-11-04 | A sandboxed browser, and no framing by other sites | `751b5e44`, `eee453d9`, `dbe9bb50`             | [B16](bricks/B16-remote-backup-update.md)      | earlier   |
| 2026-11-04 | A title for a standing agent                       | `b9fb3b92`                                     | [B06](bricks/B06-project-specialization.md)    | earlier   |
| 2026-11-04 | The production web bundle                          | `47c08a50`, `e6c3be3c`, `5075c112`, `c5e469ab` | [B02](bricks/B02-self-change-while-running.md) | earlier   |
| 2026-11-03 | Attach any file                                    | `80016496`                                     | [B12](bricks/B12-human-in-the-loop.md)         | earlier   |
| 2026-11-03 | Prompt-cache rebuilds and their cause              | `c30582af`, `64105303`                         | [B14](bricks/B14-everything-on-record.md)      | earlier   |
| 2026-11-02 | Large images, attached from anywhere on the page   | `6bae2586`, `80aea86f`, `525678f3`, `88487f17` | [B12](bricks/B12-human-in-the-loop.md)         | earlier   |
| 2026-11-02 | Pi 1.5                                             | `6864f1a9`, `0bb05358`                         | [B01](bricks/B01-durable-conversations.md)     | earlier   |
| 2026-11-01 | Fewer host pauses when child processes start       | `4b314408`, `f9d5a689`, `afffdf68`, `5c610524` | [B05](bricks/B05-agent-tools.md)               | earlier   |
| 2026-11-01 | Fewer redraws of the conversation list             | `830a36c1`                                     | [B14](bricks/B14-everything-on-record.md)      | earlier   |
| 2026-11-01 | The summary history of a branch                    | `870a0217`, `118814f9`                         | [B07](bricks/B07-conversation-tree.md)         | earlier   |
| 2026-11-01 | Sketch is removed                                  | `e6909945`                                     | [B05](bricks/B05-agent-tools.md)               | earlier   |
| 2026-11-01 | A narrator for notifications                       | `451ac392`                                     | [B12](bricks/B12-human-in-the-loop.md)         | earlier   |
| 2026-11-01 | MCP servers                                        | `5eae312d`, `16a71d81`, `90fa141d`             | [B05](bricks/B05-agent-tools.md)               | earlier   |
| 2026-10-31 | Image drops on the composer                        | `3fa3753c`                                     | [B12](bricks/B12-human-in-the-loop.md)         | earlier   |
| 2026-10-28 | A separate view for project memory                 | `21669aa1`                                     | [B07](bricks/B07-conversation-tree.md)         | earlier   |
| 2026-10-26 | Dreams after a long pause                          | `6c37a236`                                     | [B15](bricks/B15-dreams-and-chapters.md)       | earlier   |

Notes:

1. The [fixes entry](https://danielgriesser.com/ultimate/changelog/fixes-2026-11-02/) lists 29 commits. Most of them come from the outside pull requests in [history.md](history.md#outside-contributions-in-the-november-9-sync)
2. The [fixes entry](https://danielgriesser.com/ultimate/changelog/fixes-2026-11-09/) now lists 49 commits, against 12 at the review of 2026-11-11, and the feed now dates it 2026-11-15. 30 of these commits reached uao in this sync, such as Pi 1.5.2 (`3f11fcc2`) and the 402 billing limit (`446d54c6`). The other 19 reached uao earlier
3. The [fixes entry](https://danielgriesser.com/ultimate/changelog/fixes-2026-11-16/) lists 16 commits. They include the end of the landing distiller (`cd77dc1e`), background process groups (`5abd5a39`), and messages to the user from standing agents (`400f5758`). Many come from the outside pull requests in [history.md](history.md#outside-contributions-in-the-november-18-sync)
4. The entry also lists `45cdaf28` and `5015bf60`

Seven entries are new in the feed since the review of 2026-11-11. The Inbox entry is one of them, but its commits were already in the earlier snapshot `11c89136`. The feed now gives some dates that differ from the review of 2026-11-02. This review uses the dates of the feed at the review date. The published feed selects changes. The feed is not a complete record of upstream commits. The performance figures in the changelog are upstream measurements. This review does not repeat those measurements.

## Reproduce the comparison

These commands use the fetched feed and the `upstream` remote. The script prints each listed commit that is not an ancestor of the snapshot. No output means that every listed commit is in the snapshot:

```bash
curl -s https://danielgriesser.com/ultimate/changelog/feed.json |
	jq -r '.entries[].commits[].sha' |
	while read -r sha; do git merge-base --is-ancestor "$sha" 6b6d88b6 || echo "$sha"; done
```

At the fetch of 07:03 UTC, the script printed nothing for the 148 listed commits, and `upstream/main` was the snapshot.
