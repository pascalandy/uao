# B04 Models and providers

Status: shipped, at the snapshot. Source: upstream.

The user picks a model and a thinking level for each conversation. The user can change the model in the middle of a run (post, section "It Rebuilds Itself while it Runs"). Ultimate uses Pi's providers and logins, so any Pi provider works. A small summary model writes titles, summaries, and abstracts, so that the main model keeps its tokens for the work (post, section "Just Getting Started").

A confirmed missing login can switch a conversation's model at its next input ([D038](../decisions/D038-models-follow-logins.md)). A subscription never falls back to a paid key (`fa6830aa`).

Keep warm renews idle @ultimate's existing Claude Code cache, without transcript entries (`f9d91e85`). The user controls these billable pings (`extensions/keep-warm/README.md`).

## Where it lives

- `extensions/models/`: model picker and provider login
- `extensions/claude-code/`: the provider for the Claude Code CLI
- `extensions/fast/`: the priority tier
- `extensions/health/`: provider health
- `extensions/classify/`: typed judgments from a TypeSafe model, for other extensions
- `extensions/status-line/`: the model, the context use, and the token rates
- `extensions/models/fallback.ts`: model changes after a confirmed missing login
- `extensions/keep-warm/`: cache pings and their usage

## Decisions

- [D026](../decisions/D026-stable-system-prompt.md) Keep the system prompt stable
- [D038](../decisions/D038-models-follow-logins.md) Use models with a confirmed login

## Evidence

- `692ca8f` shares Pi's models and logins
- `ecc5a3d` moves login into the `models` extension
- `787b454` adds the provider for the Claude Code CLI
- `dc59e4a` makes the summary model a setting
- `56c1fe4` adds the priority tier
- `89bccf4c` claims each cache ping before sending and checks pause and cache age again
- `dec99d5e` defines later Claude Code tools inline to preserve the cached prompt prefix
- `cae9a0d6` adds a per-conversation Claude Code environment hook
- `98389c49` uses Pi's TypeSafe provider configuration for classification
