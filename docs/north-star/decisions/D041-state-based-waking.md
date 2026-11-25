# D041 Use notes for updates and waking reports for finished work

Decided 2026-10-27, revised 2026-11-23. Source: upstream. Status: active.

One-way messages to a subagent's parent or a branch's starter are notes (`136d9c01`). A branch's final answer wakes its starter when no work remains under way (`136d9c01`). When `classify` is on, a Jev judge first weighs that report with one choice. A report that the judge scores below 0.5 becomes a note. Without `classify`, after a timeout, or on an error, the answer reports (`161901f2`, [Messages](../../../extensions/messages/README.md)). Answers to another conversation's questions return only to that conversation (`91618d16`).

@ultimate's final answer also wakes each eligible branch whose reply or report was an input of its run (`dce7b5cf`, `aaa55768`). The other inputs of the run, such as a user input or a card, do not receive the answer and do not keep it from a branch (`b015f0fa`, [Messages](../../../extensions/messages/README.md)). An answer to a routed answer does not start another exchange (`extensions/messages/route.ts`).

**Why.** The delivery decision follows state instead of a model's interpretation of the text (`136d9c01`). The judge came later, because rules on typed input missed cases in both directions. Its commit reports 39 of 41 real branch runs and 7 of 7 test cases as a match (`161901f2`).

**Rejected.** Model triage of every upward message (`136d9c01`). A rule that only typed input from the user turns a report into a note (`121e739c`, `161901f2`). This rule extends [D021](D021-updates-are-notes.md).

**Evidence.** `136d9c01`, `104a5d4f`, `91618d16`, `dce7b5cf`, `aaa55768`, `b015f0fa`, and `161901f2`. [Waking upward](../../../extensions/messages/README.md#waking-upward-notes-and-reports) defines work under way and the report rules.
