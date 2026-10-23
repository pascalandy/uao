# Developer preferences

These rules override the upstream text that they name, such as the push permission in `AGENTS.md`. Source: Pascal's answers of 2026-10-23, and the rules that the agent proposed to him that day.

## How a change lands

- An outside agent, such as Claude Code or Codex, sends its work through a pull request on `pascalandy/uao`
- The [push permission](../../AGENTS.md#push-permission) in `AGENTS.md` is for Ultimate's top-level agent. It does not cover an outside agent
- A commit uses `pascalandy@users.noreply.github.com` as the author and committer email
- Before a commit, run `pnpm check` and the tests that cover the change (`AGENTS.md`)
- Before a commit that changes the north-star, run `python3 docs/north-star/check_links.py`. It must print `ok`

## Private notes

- The repository is public. Do not cite or paraphrase Pascal's private notes
