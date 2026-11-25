# B12 Human in the loop

Status: shipped, at the snapshot. Source: upstream.

The user stays in control with no need to watch each conversation. Questions wait as answer cards until the user answers or dismisses them. The user can review a diff before it lands, pause the whole host, stop one bash call, and explore a tangent in a side chat.

The Inbox lists each item that waits on the user, oldest first, and shows the answer card of the selected item (`995c52d4`, `extensions/inbox/README.md`). A row under @ultimate's sidebar row counts the items (`extensions/inbox/README.md`). An open question to the user ranks above work in progress on sidebar rows and on the phone button (`59136892`, `8bce83ea`). Other extensions can add items to the Inbox through `inbox.items` (`c497f99f`). The Inbox shows its count after its title (`7b2c18d8`). An answer card keeps its picks when the user leaves the surface and comes back (`63b8aaa7`).

The cards render the structured questions of a message without a model (`extensions/questions/README.md`). A card offers choices, multiple choices, confirmation, text, or a scale, plus a separate comment field (`extensions/questions/README.md`). Branches ask in their own conversation after @ultimate weighs in ([D044](../decisions/D044-branches-ask-the-user.md)). @ultimate can settle those questions from the user's words in its chat (`7b09649d`).

The user can start one hands-off goal and let @ultimate make goal decisions and give preview approvals ([D037](../decisions/D037-goals-delegate-approvals.md)). @ultimate records criteria and goal decisions, then leaves a goal report (`extensions/goal/README.md`). The user can end the goal early (`extensions/goal/README.md`).

**Play by itself** releases a rate-limit pause after a delay, 30 minutes by default. Only the user can change it or turn it off (`87d81283`, `extensions/pause/README.md`). A pause that the user starts always waits for Play (`extensions/pause/server.ts`).

Voice input inserts a recording's transcript into the unsent draft, through an OpenAI API key (`a0608d3f`, `extensions/voice/README.md`). Dictation now lives in the prompt box (`72db8020`). Voice mode replaces the live voice session and the Voice agent. The user holds a key or the talk bar, and a fork of @ultimate thinks the matter through, speaks its answer, and highlights the sentence that it reads. The fork can read, look things up, and drive the user's page, but it cannot run commands or edit files. When the user agrees, it hands the outcome to @ultimate, or to the branch on screen, as a card (`1401d351`, `a6d74768`, `553717c9`). The user can collect several recordings and send them together (`1e6c09e5`). Voice mode ships off by default. It needs the login of its model, Claude Opus 5.5 by default, and an OpenAI API key for transcription (`59f993ce`, `extensions/voice-live/README.md`).

Read aloud puts a speaker button on agent messages. It plays the whole answer, which the summary model rewrites lightly for listening (`e78fefa8`, `extensions/read-aloud/README.md`). It uses OpenAI speech with a key, or browser speech without one (`extensions/read-aloud/README.md`). It is on by default, because `defaultOff` does not list it (`e78fefa8`, `shared/extension-api.ts`). The narrator can use a local command for speech (`e8de47a0`).

The user can install the web app on a device's home screen (`12fd115c`). Draft images survive a page reload (`4eb6a626`). Between @ultimate's messages, the transcript folds updates and steps into one expandable line (`ebb71f13`).

@ultimate can propose a hands-off goal as a card that the user starts with one press (`1b9c842a`). An optional goal reminder wakes @ultimate every 30 minutes (`64f94443`). A goal can pause and resume its reminder (`64f94443`, `extensions/goal/README.md`).

Optional sounds include music that follows agent actions and landing notifications (`06a706bb`, `76ea0ae7`, `09befdd5`). The [sound mechanics](../../../extensions/sounds/README.md) describe the controls.

The composer attaches any file: images go inline, and other files upload to the host with a path in the prompt (`80016496`). The browser resizes images that are too large (`6bae2586`). A pinned header shows the current prompt of a conversation and its changes since the user last dismissed it (`507b378f`). A question link opens the conversation at the question (`323c3987`).

The prompt box takes videos that the user pastes, drops, or picks. On a desktop, a button records the screen and the microphone into a video for the prompt (`a2ecf28c`, `9538d3e2`). An agent asks Gemini about a video with `video_ask`, billed to the user's `GEMINI_API_KEY` (`604927c2`, `c3082104`, `extensions/video/README.md`). A **Reel** chip on a branch's question or landing card plays the screenshots of the branch as a full-screen slideshow. The reel stores nothing (`3abdf324`, `extensions/reel/README.md`). **Talk it through** on a question card opens a side chat in a read-only copy of its asker, and the side chat can fill the card's draft answers (`ad3bf0c5`, `99bf4c81`). An answer card comes with its picks chosen. Send locks the card and becomes Undo, and a hold on Send sends at once (`ecfc6e96`). Enter opens the next question (`aa1c5f25`). An answer up to 60 KiB goes with `keepalive`, so a page exit cannot drop it (`3c0f9aab`, `extensions/questions/card.solid.tsx`).

The optional `push` extension sends Web Push notifications for questions, landings, and @ultimate's failed runs, with Reply and Approve actions (`ff44988c`, `extensions/push/README.md`). Installed on Android, the web app is a share target for @ultimate's composer (`ff44988c`, `extensions/share/README.md`). On a phone, rows go edge to edge, and the composer is a sheet on the status line (`1be263cf`).

The narrator is off by default (`extensions/sounds/web.solid.tsx`). When enabled, the narrator speaks questions, failures, landings, and optionally new branches (`451ac392`). It uses OpenAI audio with a key, or browser speech without one (`extensions/sounds/server.ts`, `extensions/sounds/web.solid.tsx`). Finished answers keep their sound alone (`451ac392`).

## Where it lives

- `extensions/questions/`: answer cards
- `extensions/goal/`: hands-off goals, goal decisions, and goal reports
- `extensions/messages/questions.ts`: the questions of a message and their validation
- `extensions/inbox/`: the items that wait on the user
- `extensions/todos/`: the to-do list. Other extensions add to-dos through `TodosApi.add` (`a9d47b01`)
- `extensions/review/`: diffs and line comments
- `extensions/pause/`: the host-wide pause
- `extensions/side-chat/`: side chats
- `extensions/sounds/`: sound cues
- `extensions/voice/` and `extensions/voice-live/`: dictated drafts and voice mode
- `extensions/video/` and `extensions/screen-recorder/`: videos in the prompt box and screen recordings
- `extensions/reel/`: the reel of a branch's screenshots
- `extensions/read-aloud/`: spoken answers
- `extensions/attachments/`: uploaded files for the prompt
- `extensions/push/` and `extensions/share/`: Web Push notifications and the share target
- `web/public/manifest.webmanifest`: the installable web app

## Decisions

- [D017](../decisions/D017-questions-get-proposals.md) Explore questions, act on instructions
- [D037](../decisions/D037-goals-delegate-approvals.md) Let a user-granted goal delegate approvals
- [D044](../decisions/D044-branches-ask-the-user.md) Let branches ask after @ultimate weighs in

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
- `d3178ff` adds Play by itself for rate-limit pauses
- `4a6aab5` records automatic Play before the scheduler resumes
- `93dbff1` fixes the answer card's Undo countdown on phones
- `9e3164f5` stops the host from pausing again when the final rate-limit retry ends its run
- `29480df2` tells a held parent which subagent hit the rate limit
- `46d0054d` sends a held answer when the user leaves the page during Undo
- `3fa3753c` accepts image drops in the composer and prevents file drops from navigating away
- `c3d5a2ea` shows a notice when a background compaction fails
- `f46c0050` lets the user inject or discard again a side chat whose ending task faulted
- `995c52d4` adds the Inbox
- `a9d47b01` adds `TodosApi.add` and an optional idempotency key on `todos/add`
- `c497f99f` lets other extensions add Inbox items
- `799df8e1` lets Voice read and answer open questions
- `e78fefa8` adds Read aloud
