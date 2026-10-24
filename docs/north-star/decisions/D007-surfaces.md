# D007 Make apps surfaces beside the agent

Decided 2026-10-02. Source: upstream. Status: active.

A surface is a full-screen app made of extensions. The conversation is the built-in Agent surface in `extensions/agent/`. The agent stays one keystroke away on every surface. A switch between surfaces never stops a run.

**Why.** A project can build full-screen apps while the agent stays one keystroke away. The Agent surface is also the smallest example. A project can replace the Agent surface by name (`790c34e`).

**Rejected.** Views and one fixed shell (`790c34e`).

**Evidence.** `790c34e` adds surfaces. [Surfaces](../../../extensions/README.md#surfaces) in the extension guide holds the mechanics.
