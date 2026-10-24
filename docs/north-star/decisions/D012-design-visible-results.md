# D012 Design each visible result

Decided 2026-10-13. Source: upstream. Status: active.

A result that a person sees, such as a subagent report or a landing, gets a renderer that matches the existing cards. Plain Markdown in a message is not acceptable. Before they build, agents inspect the running app and screenshots. Agents also check a worker's screenshots.

**Why.** The user had to ask many times for reports as cards, because agents built them without inspecting the app (`67d1b54`).

**Evidence.** `67d1b54`. [Conventions](../../../AGENTS.md#conventions) holds the rule.
