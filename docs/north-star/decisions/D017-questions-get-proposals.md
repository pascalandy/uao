# D017 Explore questions, act on instructions

Decided 2026-10-17. Source: upstream. Status: replaced by D037.

The agent investigates a question or a "how could we" and gives one proposal. Then the agent waits for the user's approval. The agent executes a clear instruction at once. A delegated task and a scheduled run count as approval.

**Why.** A user who opens with a question usually wants to find a better approach first (`bf94a30`).

**Evidence.** `bf94a30` changes the principles of the prompt.
