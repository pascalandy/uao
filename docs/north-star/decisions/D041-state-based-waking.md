# D041 Use notes for updates and waking reports for finished work

Decided 2026-10-27, revised 2026-10-31. Source: upstream. Status: active.

One-way messages to a subagent's parent or a branch's starter are notes (`136d9c01`). A branch's final answer wakes its starter when no work remains under way (`136d9c01`). Answers to another conversation's questions return only to that conversation (`91618d16`).

@ultimate's final answer also wakes each eligible branch whose reply or report made up its run (`dce7b5cf`, `aaa55768`). A user input or a landing card keeps that answer local (`extensions/messages/route.ts`). An answer to a routed answer does not start another exchange (`extensions/messages/route.ts`).

**Why.** The delivery decision follows state instead of a model's interpretation of the text (`136d9c01`).

**Rejected.** Model triage of upward messages (`136d9c01`). This rule extends [D021](D021-updates-are-notes.md).

**Evidence.** `136d9c01`, `104a5d4f`, `91618d16`, `dce7b5cf`, and `aaa55768`. [Waking upward](../../../extensions/messages/README.md#waking-upward-notes-and-reports) defines work under way and the report rules.
