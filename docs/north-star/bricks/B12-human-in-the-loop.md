# B12 Human in the loop

Status: shipped, at the snapshot. Source: upstream.

The user stays in control with no need to watch each conversation. Questions wait as answer cards until the user answers or dismisses them. The user can review a diff before it lands, pause the whole host, stop one bash call, and explore a tangent in a side chat.

## How it works

`questions` turns a message that expects a reply into an answer card. `todos` keeps one short list for the user and @ultimate. `review` shows diffs and sends line comments as one review input. `pause` holds new tasks and lets current work finish. `side-chat` forks @ultimate for a tangent, and then the user discards it or injects a summary. `sounds` plays a cue when @ultimate needs input. Each extension README holds its mechanics.

## Where it lives

- `extensions/questions/`: answer cards
- `extensions/todos/`: the to-do list
- `extensions/review/`: diffs and line comments
- `extensions/pause/`: the host-wide pause
- `extensions/side-chat/`: side chats
- `extensions/sounds/`: sound cues

## Decisions

- [D017](../decisions/D017-questions-get-proposals.md) Explore questions, act on instructions
- [D022](../decisions/D022-talk-to-ultimate.md) Let the user talk only to @ultimate

## Next

- Nothing stated

## Evidence

- `38553fb` adds the panel of open questions
- `f074882` adds review
- `3aa830b` adds pause
- `0328cac` adds to-dos
- `a8de706` cancels one bash call
- `34c3633` adds side chats
