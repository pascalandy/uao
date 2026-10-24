# D022 Route agent messages for the user through @ultimate

Decided 2026-10-18. Source: upstream. Status: active.

Only @ultimate may message the user, so messages, questions, and branch results for the user arrive in the conversation of @ultimate (`extensions/messages/README.md`). @ultimate is the default entry point, but the user can still talk to a coordinator directly (`agents/coordinator.md`, `f0d80a3`). The user does not create conversations or roots by hand (`AGENTS.md`).

**Why.** The commits give no reason. `4d3605e` restricts messages for the user to @ultimate. Other agents relay these messages through @ultimate. The post says that "the only thing I need to pay attention to is my chat with Ultimate itself" (section "Notes").

**Rejected.** The Board surface, a feed with an inbox for all agents (`eeae136`). Manual creation of roots and branches (`1d2f700`).

**Evidence.** `4d3605e`, `eeae136`, `cf96f4a`, and `f0d80a3`. [The work model](../../../AGENTS.md#how-work-is-organised-a-forest-of-conversation-trees) holds the rule.
