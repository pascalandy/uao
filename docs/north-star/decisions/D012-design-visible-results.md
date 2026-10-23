# D012 Design each visible result

Decided 2026-10-13. Source: upstream. Status: active.

A result that a person sees, such as a subagent report or a landing, gets a renderer that matches the existing cards. Plain Markdown in a message is not acceptable. Agents look at the running app and at screenshots before they build, and they check a worker's screenshots.

**Why.** The user had to ask many times for reports as cards, because agents built them without a look at the app (`67d1b54`).

**Evidence.** `67d1b54`. [Conventions](../../../AGENTS.md#conventions) holds the rule.
