# B04 Models and providers

Status: shipped, at the snapshot. Source: upstream.

The user picks a model and a thinking level for each conversation. The user can change the model in the middle of a run (post, section "It Rebuilds Itself while it Runs"). Ultimate uses Pi's providers and logins, so any Pi provider works. A small summary model writes titles, summaries, and abstracts, so that the main model keeps its tokens for the work (post, section "Just Getting Started").

## Where it lives

- `extensions/models/`: model picker and provider login
- `extensions/claude-code/`: the Claude Code CLI provider
- `extensions/fast/`: the priority tier
- `extensions/health/`: provider health
- `extensions/classify/`: typed judgments from a TypeSafe model, for other extensions
- `extensions/status-line/`: the model, the context use, and the token rates

## Decisions

- [D026](../decisions/D026-stable-system-prompt.md) Keep the system prompt stable

## Evidence

- `692ca8f` shares Pi's models and logins
- `ecc5a3d` moves login into the `models` extension
- `787b454` adds the Claude Code CLI provider
- `dc59e4a` makes the summary model a setting
- `56c1fe4` adds the priority tier
