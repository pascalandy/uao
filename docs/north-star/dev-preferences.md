# Developer preferences

This file says how Pascal wants changes made in uao. It applies where `AGENTS.md` and the principles say nothing. The preferences come from Pascal's answers and from rules announced to him on 2026-10-23, unless a line cites another source.

## How a change lands

- An outside agent, such as Claude Code or Codex, sends its work through a pull request on `pascalandy/uao`
- Ultimate lands its own work through its lander, as `AGENTS.md` describes. The lander pushes to `origin`, which is `pascalandy/uao` (see [upstream.md](upstream.md#what-still-points-at-hazat))
- A commit uses `pascalandy@users.noreply.github.com` as the author and committer email
- Before a commit, run `pnpm check` and the tests that cover the change (`AGENTS.md`)

## Keep the fork additive

- Put uao's own work in places that upstream does not edit: `docs/north-star/`, new files in `.ultimate/`, and `~/.ultimate/` ([D034](decisions/D034-follow-upstream.md))
- Do not change the upstream files that still point at HazAT. [upstream.md](upstream.md) lists them
- After each merge of upstream, check each brick status again and move the snapshot

## Keep the north-star true

- Follow the [update rules](README.md#update-rules)
- Present a guess about Pascal's direction as a guess, never as a decision
- The repository is public. Do not cite or paraphrase Pascal's private notes

## Write

- Write the repository in English, also when Pascal writes in French
- Write the north-star in ASD-STE100 Simplified Technical English
- Use the names in the [glossary](glossary.md)
- Copy a source word for word only in `sources/`. Name the origin of each copy
