# D017 Explore questions, act on instructions

Decided 2026-10-17, revised 2026-10-24. Source: upstream. Status: active.

The agent investigates a question or a "how could we" and gives one proposal. Then the agent waits for approval from the user, or from @ultimate during a user-granted goal ([D037](D037-goals-delegate-approvals.md)). The agent executes a clear instruction at once, and a delegated task or a scheduled run counts as approval.

**Why.** A user who opens with a question usually wants to find a better approach first (`bf94a30`).

**Evidence.** `bf94a30` changes the principles of the prompt.
