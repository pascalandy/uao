# D005 Compose tools in a codemode sandbox

Decided 2026-10-02, revised 2026-11-23. Source: upstream. Status: active.

The agent can run one JavaScript script that calls several tools and reads Ultimate's state. Since `3603c530`, codemode is Pi Durable's own code mode tool. The script runs in a QuickJS sandbox, and only injected functions reach the host. Pi Durable records the result of each nested call. A script that a restart interrupts runs again with the recorded results, so a finished call does not run twice. A script writes through the script-only tools `tools.action` and `tools.tell`, which never run again after an interruption (`extensions/codemode/README.md`).

**Why.** A sandbox already existed in `pi-codemode`. The commit pins `pi-codemode` "rather than rebuilding sandbox isolation" (`1a0453c`).

**Rejected.** A sandbox built inside Ultimate (`1a0453c`). The earlier codemode extension of Ultimate, whose store write left a crash window (`3603c530`).

**Evidence.** `1a0453c` adds codemode. `3603c530` moves it onto Pi Durable's tool.
