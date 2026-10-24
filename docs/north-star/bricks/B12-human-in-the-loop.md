# B12 Human in the loop

Status: shipped, at the snapshot. Source: upstream.

The user stays in control with no need to watch each conversation. Questions wait as answer cards until the user answers or dismisses them. The user can review a diff before it lands, pause the whole host, stop one bash call, and explore a tangent in a side chat.

The cards render the structured questions of a message without a model (`extensions/questions/README.md`). A card offers choices, multiple choices, confirmation, text, or a scale, plus a separate comment field (`extensions/questions/README.md`).

The user can start one hands-off goal and let @ultimate give decisions and preview approvals in their place ([D037](../decisions/D037-goals-delegate-approvals.md)). @ultimate records criteria and decisions, then leaves a report card (`extensions/goal/README.md`). The user can end the goal early (`extensions/goal/README.md`).

The user can enable **Play by itself** to release a rate-limit pause after a chosen delay (`extensions/pause/README.md`). This setting is off by default, and only the user can change it (`extensions/pause/server.ts`). A pause that the user starts always waits for Play (`extensions/pause/server.ts`).

## Where it lives

- `extensions/questions/`: answer cards
- `extensions/goal/`: hands-off goals, recorded decisions, and report cards
- `extensions/messages/questions.ts`: the questions of a message and their validation
- `extensions/todos/`: the to-do list
- `extensions/review/`: diffs and line comments
- `extensions/pause/`: the host-wide pause
- `extensions/side-chat/`: side chats
- `extensions/sounds/`: sound cues

## Decisions

- [D037](../decisions/D037-goals-delegate-approvals.md) Let a user-granted goal delegate approvals
- [D022](../decisions/D022-route-through-ultimate.md) Route agent messages for the user through @ultimate

## Evidence

- `38553fb` adds the panel of open questions
- `f074882` adds review
- `3aa830b` adds pause
- `0328cac` adds to-dos
- `a8de706` cancels one bash call
- `34c3633` adds side chats
- `de87bde` replaces question extraction with structured fields on the message tool
- `a8445df` lets the user send @ultimate to work on an open to-do
- `a63e2fb` and `787fa1a` pause the host on a retryable rate limit
- `001a193d` adds hands-off goals
- `65a251f` commits each goal change with its card's delivery task
- `d3178ff` adds the user timer for rate-limit pauses
- `4a6aab5` records automatic Play before the scheduler resumes
- `93dbff1` fixes the answer card's Undo countdown on phones
