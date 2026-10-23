# B12 Human in the loop

Status: shipped, at the snapshot. Source: upstream.

The user stays in control with no need to watch each conversation. Questions wait as answer cards until the user answers or dismisses them. The user can review a diff before it lands, pause the whole host, stop one bash call, and explore a tangent in a side chat.

## Where it lives

- `extensions/questions/`: answer cards
- `extensions/todos/`: the to-do list
- `extensions/review/`: diffs and line comments
- `extensions/pause/`: the host-wide pause
- `extensions/side-chat/`: side chats
- `extensions/sounds/`: sound cues

## Decisions

- [D017](../decisions/D017-questions-get-proposals.md) Explore questions, act on instructions
- [D022](../decisions/D022-route-through-ultimate.md) Route agent messages for the user through @ultimate

## Evidence

- `38553fb` adds the panel of open questions
- `f074882` adds review
- `3aa830b` adds pause
- `0328cac` adds to-dos
- `a8de706` cancels one bash call
- `34c3633` adds side chats
