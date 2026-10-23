# D014 Remove the Canvas surface

Decided 2026-10-14. Source: upstream. Status: active.

Ultimate removed the Canvas, a live map of conversations and their subagents, with its conclusion cards. The app now centers on conversations. The upstream branch `park/canvas` keeps the code.

**Why.** The commit says "Narrow the app to conversations" and gives no other reason (`deb65f8`).

**Evidence.** `9c129ad` adds the Canvas. `deb65f8` removes it.
