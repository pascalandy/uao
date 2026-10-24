# D002 Build on Pi Durable over SQLite

Decided 2026-10-02. Source: upstream. Status: active.

Ultimate runs on the Pi Durable harness with its SQLite storage. Pi Durable commits each conversation, tool call, and document before the UI shows them. After a crash, Pi Durable resumes unfinished tasks. Ultimate pins the `@earendil-works/*` packages to exact versions, because Pi Durable is experimental.

**Why.** Daniel found other durability layers "too complex, too involved and too integrated", and Pi Durable has "the right balance" ([post](https://danielgriesser.com/posts/ultimate/), section "How it Started"). The packages also supply the models, logins, coding tools, and reload support that the host needs (`692ca8f`).

**Evidence.** `692ca8f` opens the SQLite harness and tests a resume after SIGKILL. `docs/durability.md` states the guarantees.
