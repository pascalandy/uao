# Developer preferences

These rules override the upstream text that they name, such as the push permission in `AGENTS.md`. Source: Pascal's answers of 2026-10-23, and the rules that the agent proposed to him that day.

## How a change lands

- An outside agent, such as Claude Code or Codex, sends its work through a pull request on `pascalandy/uao`
- The [push permission](../../AGENTS.md#push-permission) in `AGENTS.md` is for Ultimate's top-level agent. It does not cover an outside agent
- A commit uses `pascalandy@users.noreply.github.com` as the author and committer email
- Before a commit, run `pnpm check` and the tests that cover the change (`AGENTS.md`)
- Before a commit that changes the north-star, run `python3 docs/north-star/check_links.py`. It must print `ok`
- `check_links.py` checks links, anchors, and cited paths. It also checks that each cited SHA is an ancestor of `HEAD`, and that each index links to each file in its folder

## Keep the north-star true

- Keep one home for each fact. Link to the mechanics. Restate a fact only when the reader cannot reach its source
- Cite evidence for each status, decision, and claim about behavior. Put the short SHA or the path in the same sentence or row. Write "(inferred)" after an inference
- Keep one snapshot. Each status must be true at the [snapshot](upstream.md#snapshot). After a merge of upstream, follow the [sync rule](upstream.md#sync-rule)
- Mark each brick and decision `Source: upstream` or `Source: uao`. A guess about Pascal's direction is not a decision
- Link down, not up. The [North star](../../AGENTS.md#north-star) table in `AGENTS.md` links to each file and index. The vision links to bricks. The principles and the bricks link to decisions. The bricks link to code and docs. A decision does not list the bricks that use it
- Use the names in the [glossary](glossary.md). Add a new term there before its first use
- Write in English, also when Pascal writes in French. Write the north-star in ASD-STE100 Simplified Technical English
- Copy a source word for word only in `sources/`. Name the origin of each copy

## Private notes

- The repository is public. Do not cite or paraphrase Pascal's private notes
