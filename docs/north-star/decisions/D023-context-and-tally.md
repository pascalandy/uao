# D023 Call the tally "context" in the UI

Decided 2026-10-18. Source: upstream. Status: active.

The UI and the docs for users call a root's tally its "context". Code, tool names, stored kinds, and agent prompts keep "tally".

**Why.** Agents and stored entries already use "tally". A rename needs migrations for no gain that a user sees (`b99106e`).

**Evidence.** `b99106e`. The [glossary](../glossary.md) gives both names.
