# Changelog review

Source: upstream. This review uses the public [changelog](https://danielgriesser.com/ultimate/changelog/) and its [JSON feed](https://danielgriesser.com/ultimate/changelog/feed.json). The review uses the feed as it was fetched at 07:06 UTC on 2026-11-25.

At that fetch, the feed had 37 entries. Each commit that an entry listed was an ancestor of the [snapshot](upstream.md#snapshot). No entry described code after the snapshot.

Two entries describe code that changed after the entry. The voice mode entry says that voice mode runs on Gemini through Antigravity by default. At the snapshot, its default model is Claude Opus 5.5 (`59f993ce`, `extensions/voice-live/README.md`). The entry about the end of the move to Solid says that outside React extensions keep working on a compat layer. One day later, `256f9cee` removed that layer ([D046](decisions/D046-solid-interface.md)).

## Entries in the snapshot

The linked brick describes the capability. A row marked "this sync" lists commits that reached uao with the merge of `e8abe7f1`. A row marked "earlier" lists commits that reached uao with an earlier merge. A row marked "both" lists commits of the two kinds.

| Published  | Change                                             | Commits                                        | Brick                                           | Sync      |
| ---------- | -------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------- | --------- |
| 2026-11-23 | Voice mode, a fork of @ultimate that hands over    | `1401d351`, `a6d74768`, `1e6c09e5`, `553717c9` | [B12](bricks/B12-human-in-the-loop.md)          | this sync |
| 2026-11-22 | Fixes of the week of 16 November, 55 commits       | `fa11fd0c` to `95b45985`, note 3               | Several                                         | both      |
| 2026-11-22 | Recovery from outages and crashes                  | `0d0516d0`, `e600a47f`, `8ca81954`, `39bf0a76` | [B09](bricks/B09-coordinators-and-subagents.md) | this sync |
| 2026-11-21 | The interface is all Solid                         | `f8ba9711`, `250bec71`, `b8657b86`             | [B03](bricks/B03-reloadable-extensions.md)      | this sync |
| 2026-11-21 | Most of the interface runs on Solid                | `0dea5af2`, `79a9e74e`, `3fb3c21b`, `ac117cb8` | [B03](bricks/B03-reloadable-extensions.md)      | this sync |
| 2026-11-20 | Antigravity models                                 | `76280bf9`, `7f30c318`                         | [B04](bricks/B04-models-and-providers.md)       | this sync |
| 2026-11-20 | The interface moves to Solid                       | `f06ad003`, `32b33f12`, `0f7f8d3e`             | [B03](bricks/B03-reloadable-extensions.md)      | this sync |
| 2026-11-19 | Agents operate controls by name                    | `0fd21054`, `fa9a3b6e`, `134703fb`             | [B05](bricks/B05-agent-tools.md)                | this sync |
| 2026-11-18 | A reel of a branch's screenshots                   | `3abdf324`, `03a7d39d`, `6dfa3e8f`             | [B12](bricks/B12-human-in-the-loop.md)          | this sync |
| 2026-11-18 | Talk a question through                            | `ad3bf0c5`, `99bf4c81`, `561f42d2`, `da797175` | [B12](bricks/B12-human-in-the-loop.md)          | this sync |
| 2026-11-17 | Spoken answers with Read aloud                     | `e78fefa8`, `56c3d7a2`, `2dd6eac1`             | [B12](bricks/B12-human-in-the-loop.md)          | earlier   |
| 2026-11-16 | A skills list for each agent                       | `85b68619`                                     | [B06](bricks/B06-project-specialization.md)     | earlier   |
| 2026-11-16 | What each conversation waits on                    | `900c96cc`, `fe4abaeb`, `20941e80`, `c351b2b1` | [B11](bricks/B11-notes-and-messages.md)         | both      |
| 2026-11-15 | Fixes of the week of 9 November, 49 commits        | `8e944092` to `1fb18e43`, note 2               | Several                                         | earlier   |
| 2026-11-14 | The projects rail                                  | `f5e963f1`, `55da7426`, `0197a6a2`, note 4     | [B16](bricks/B16-remote-backup-update.md)       | earlier   |
| 2026-11-12 | Answers to questions by voice                      | `799df8e1`                                     | [B12](bricks/B12-human-in-the-loop.md)          | earlier   |
| 2026-11-10 | The Inbox                                          | `995c52d4`, `364a3c50`, `cfccc89c`             | [B12](bricks/B12-human-in-the-loop.md)          | earlier   |
| 2026-11-09 | Wire, the raw record of model calls                | `1dd3e145`, `9b8f1866`, `c16450c9`             | [B14](bricks/B14-everything-on-record.md)       | earlier   |
| 2026-11-08 | Push notifications and the share target            | `ff44988c`, `b17e228e`                         | [B12](bricks/B12-human-in-the-loop.md)          | earlier   |
| 2026-11-08 | More room on a phone                               | `1be263cf`                                     | [B12](bricks/B12-human-in-the-loop.md)          | earlier   |
| 2026-11-07 | Fixes of the week of 2 November, 29 commits        | `3d922572` to `630b6940`, note 1               | Several                                         | earlier   |
| 2026-11-04 | A sandboxed browser, and no framing by other sites | `751b5e44`, `eee453d9`, `dbe9bb50`             | [B16](bricks/B16-remote-backup-update.md)       | earlier   |
| 2026-11-04 | A title for a standing agent                       | `b9fb3b92`                                     | [B06](bricks/B06-project-specialization.md)     | earlier   |
| 2026-11-04 | The production web bundle                          | `47c08a50`, `e6c3be3c`, `5075c112`, `c5e469ab` | [B02](bricks/B02-self-change-while-running.md)  | earlier   |
| 2026-11-03 | Attach any file                                    | `80016496`                                     | [B12](bricks/B12-human-in-the-loop.md)          | earlier   |
| 2026-11-03 | Prompt-cache rebuilds and their cause              | `c30582af`, `64105303`                         | [B14](bricks/B14-everything-on-record.md)       | earlier   |
| 2026-11-02 | Large images, attached from anywhere on the page   | `6bae2586`, `80aea86f`, `525678f3`, `88487f17` | [B12](bricks/B12-human-in-the-loop.md)          | earlier   |
| 2026-11-02 | Pi 1.5                                             | `6864f1a9`, `0bb05358`                         | [B01](bricks/B01-durable-conversations.md)      | earlier   |
| 2026-11-01 | Fewer host pauses when child processes start       | `4b314408`, `f9d5a689`, `afffdf68`, `5c610524` | [B05](bricks/B05-agent-tools.md)                | earlier   |
| 2026-11-01 | Fewer redraws of the conversation list             | `830a36c1`                                     | [B14](bricks/B14-everything-on-record.md)       | earlier   |
| 2026-11-01 | The summary history of a branch                    | `870a0217`, `118814f9`                         | [B07](bricks/B07-conversation-tree.md)          | earlier   |
| 2026-11-01 | Sketch is removed                                  | `e6909945`                                     | [B05](bricks/B05-agent-tools.md)                | earlier   |
| 2026-11-01 | A narrator for notifications                       | `451ac392`                                     | [B12](bricks/B12-human-in-the-loop.md)          | earlier   |
| 2026-11-01 | MCP servers                                        | `5eae312d`, `16a71d81`, `90fa141d`             | [B05](bricks/B05-agent-tools.md)                | earlier   |
| 2026-10-31 | Image drops on the composer                        | `3fa3753c`                                     | [B12](bricks/B12-human-in-the-loop.md)          | earlier   |
| 2026-10-28 | A separate view for project memory                 | `21669aa1`                                     | [B07](bricks/B07-conversation-tree.md)          | earlier   |
| 2026-10-26 | Dreams after a long pause                          | `6c37a236`                                     | [B15](bricks/B15-dreams-and-chapters.md)        | earlier   |

Notes:

1. The [fixes entry](https://danielgriesser.com/ultimate/changelog/fixes-2026-11-02/) lists 29 commits. Most of them come from the outside pull requests in [history.md](history.md#outside-contributions-in-the-november-9-sync)
2. The [fixes entry](https://danielgriesser.com/ultimate/changelog/fixes-2026-11-09/) lists 49 commits. 30 of them reached uao in the November 18 sync, and the other 19 reached uao earlier
3. The [fixes entry](https://danielgriesser.com/ultimate/changelog/fixes-2026-11-16/) now lists 55 commits, against 16 at the review of 2026-11-18, and the feed now dates it 2026-11-22. 27 of these commits reached uao in this sync, such as Pi 1.6.0 (`2f6ef78f`), messages from any conversation except a subagent (`3aed7ab8`), and Send that becomes Undo (`ecfc6e96`). The other 28 reached uao earlier. Many come from the outside pull requests in [history.md](history.md#outside-contributions-in-the-november-25-sync)
4. The entry also lists `45cdaf28` and `5015bf60`

Nine entries are new in the feed since the review of 2026-11-18. Two of them, the reel and talk a question through, were the later entries that the earlier review named. The wait labels entry now also lists `c351b2b1`, which reached uao in this sync. The published feed selects changes. The feed is not a complete record of upstream commits. The performance figures in the changelog are upstream measurements. This review does not repeat those measurements.

## Reproduce the comparison

These commands compare the live feed with the snapshot through the `upstream` remote. The script prints each listed commit that is not an ancestor of the snapshot. No output means that every listed commit is in the snapshot:

```bash
curl -s https://danielgriesser.com/ultimate/changelog/feed.json |
	jq -r '.entries[].commits[].sha' |
	while read -r sha; do git merge-base --is-ancestor "$sha" e8abe7f1 || echo "$sha"; done
```

At the fetch of 07:06 UTC, the script printed nothing for the 218 listed commits, and `upstream/main` was the snapshot.
