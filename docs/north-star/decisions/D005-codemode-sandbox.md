# D005 Compose tools in a codemode sandbox

Decided 2026-10-02. Source: upstream. Status: active.

The agent can run one JavaScript script that calls several tools and reads Ultimate's state. The script runs in the QuickJS sandbox of `pi-codemode`, pinned to an exact version. A store write commits just before the tool returns, so `extensions/codemode/README.md` documents a crash window.

**Why.** A sandbox already existed in `pi-codemode`. The commit pins `pi-codemode` "rather than rebuilding sandbox isolation" (`1a0453c`).

**Rejected.** A sandbox built inside Ultimate (`1a0453c`).

**Evidence.** `1a0453c` adds codemode.
