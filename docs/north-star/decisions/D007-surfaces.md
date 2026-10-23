# D007 Make apps surfaces beside the agent

Decided 2026-10-02. Source: upstream. Status: active.

A surface is a full-screen app made of extensions. The conversation is the built-in Agent surface in `extensions/agent/`. The agent stays one keystroke away on every surface, and a switch never stops a run.

**Why.** A project can build full-screen apps while the agent stays near. The Agent surface is also the smallest example, and a project can replace it by name (`790c34e`).

**Rejected.** Views and one fixed shell (`790c34e`).

**Evidence.** `790c34e` adds surfaces. [Surfaces](../../../extensions/README.md#surfaces) in the extension guide holds the mechanics.
