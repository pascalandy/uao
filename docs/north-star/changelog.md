# Changelog review

Source: upstream. This review uses the public [changelog](https://danielgriesser.com/ultimate/changelog/) and its [JSON feed](https://danielgriesser.com/ultimate/changelog/feed.json). The review date is 2026-11-10 UTC.

The feed has 19 entries. Each commit that an entry lists is an ancestor of the [snapshot](upstream.md#snapshot). No entry describes code after the snapshot.

## Entries in the snapshot

The linked brick describes the capability. The rows marked "this sync" reached uao with the merge of `32e45c95`.

| Published  | Change                                             | Commits                                        | Brick                                          | Sync      |
| ---------- | -------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | --------- |
| 2026-11-08 | Push notifications and the share target            | `ff44988c`, `b17e228e`                         | [B12](bricks/B12-human-in-the-loop.md)         | this sync |
| 2026-11-08 | More room on a phone                               | `1be263cf`                                     | [B12](bricks/B12-human-in-the-loop.md)         | this sync |
| 2026-11-07 | Fixes of the week of 2 November, 29 commits        | `3d922572` to `630b6940`, note 1               | Several                                        | this sync |
| 2026-11-04 | A sandboxed browser, and no framing by other sites | `751b5e44`, `eee453d9`, `dbe9bb50`             | [B16](bricks/B16-remote-backup-update.md)      | this sync |
| 2026-11-04 | A title for a standing agent                       | `b9fb3b92`                                     | [B06](bricks/B06-project-specialization.md)    | this sync |
| 2026-11-04 | The production web bundle                          | `47c08a50`, `e6c3be3c`, `5075c112`, `c5e469ab` | [B02](bricks/B02-self-change-while-running.md) | this sync |
| 2026-11-03 | Attach any file                                    | `80016496`                                     | [B12](bricks/B12-human-in-the-loop.md)         | this sync |
| 2026-11-03 | Prompt-cache rebuilds and their cause              | `c30582af`, `64105303`                         | [B14](bricks/B14-everything-on-record.md)      | this sync |
| 2026-11-02 | Large images, attached from anywhere on the page   | `6bae2586`, `80aea86f`, `525678f3`, `88487f17` | [B12](bricks/B12-human-in-the-loop.md)         | this sync |
| 2026-11-02 | Pi 1.5                                             | `6864f1a9`, `0bb05358`                         | [B01](bricks/B01-durable-conversations.md)     | this sync |
| 2026-11-01 | Fewer host pauses when child processes start       | `4b314408`, `f9d5a689`, `afffdf68`, `5c610524` | [B05](bricks/B05-agent-tools.md)               | this sync |
| 2026-11-01 | Fewer redraws of the conversation list             | `830a36c1`                                     | [B14](bricks/B14-everything-on-record.md)      | this sync |
| 2026-11-01 | The summary history of a branch                    | `870a0217`, `118814f9`                         | [B07](bricks/B07-conversation-tree.md)         | this sync |
| 2026-11-01 | Sketch is removed                                  | `e6909945`                                     | [B05](bricks/B05-agent-tools.md)               | this sync |
| 2026-11-01 | A narrator for notifications                       | `451ac392`                                     | [B12](bricks/B12-human-in-the-loop.md)         | earlier   |
| 2026-11-01 | MCP servers                                        | `5eae312d`, `16a71d81`, `90fa141d`             | [B05](bricks/B05-agent-tools.md)               | earlier   |
| 2026-10-31 | Image drops on the composer                        | `3fa3753c`                                     | [B12](bricks/B12-human-in-the-loop.md)         | earlier   |
| 2026-10-28 | A separate view for project memory                 | `21669aa1`                                     | [B07](bricks/B07-conversation-tree.md)         | earlier   |
| 2026-10-26 | Dreams after a long pause                          | `6c37a236`                                     | [B15](bricks/B15-dreams-and-chapters.md)       | earlier   |

Notes:

1. The [fixes entry](https://danielgriesser.com/ultimate/changelog/fixes-2026-11-02/) lists 29 commits. Most of them come from the outside pull requests in [history.md](history.md#outside-contributions-in-the-november-9-sync)

The feed now gives some dates that differ from the review of 2026-11-02. This review uses the dates of the feed at the review date. The published feed selects changes. The feed is not a complete record of upstream commits. The performance figures in the changelog are upstream measurements. This review does not repeat those measurements.

## Reproduce the comparison

These commands use the fetched feed and the `upstream` remote. The script prints each listed commit that is not an ancestor of the snapshot. No output means that every listed commit is in the snapshot:

```bash
curl -s https://danielgriesser.com/ultimate/changelog/feed.json |
	jq -r '.entries[].commits[].sha' |
	while read -r sha; do git merge-base --is-ancestor "$sha" 32e45c95 || echo "$sha"; done
```

At the review date, the script printed nothing for the 64 listed commits, and `upstream/main` was the snapshot.
