# D023 Call the tally "context" in the UI

Decided 2026-10-18, revised 2026-10-28. Source: upstream. Status: active.

The tally is project context in user-facing text and a read-only History page (`76eaa574`). Code and stored kinds keep "tally" (`b99106e`). The sidebar's project path opens History, and its Memory row opens the separate Memory surface (`6ee7d47c`, `21669aa1`).

**Why.** Agents and stored entries already use "tally". A rename needs migrations for no gain that a user sees (`b99106e`).

**Evidence.** `b99106e`. The [glossary](../glossary.md) gives both names.
