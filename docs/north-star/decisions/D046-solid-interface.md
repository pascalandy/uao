# D046 Build the interface on Solid

Decided 2026-11-19, revised 2026-11-22. Source: upstream. Status: active.

The web core and every web facet use Solid, not React. A web facet is `web.solid.tsx`, and a facet imports the web SDK as `@/sdk/solid` (`extensions/README.md`). A `web.tsx` facet loads as an error card that asks for the move to Solid (`256f9cee`, `lib/discovery.ts`). Controls come from the UI kit on `@ui-sdk/solid`, so agents can operate them by name ([B05](../bricks/B05-agent-tools.md), `0fd21054`). The Solid and ui-sdk packages are pinned to exact versions (`f06ad003`).

**Why.** The purpose is a front end that is more robust, faster, simpler, and smaller. Each step reported its change against a measured baseline (`0f7f8d3e`). The compat layer went before the first release, so that release makes no promise about React. No facet on Daniel's machine used that layer (`256f9cee`).

**Rejected.** React facets on a compat layer that loads only when an outside React facet is on. That layer existed from `2fb5782a` to `256f9cee`.

**Evidence.** `f06ad003` adds the toolchain and the `solid-ui` skill. `0dea5af2` makes the shell Solid. `256f9cee` and `b8657b86` remove React. `skills/solid-ui/SKILL.md` holds the rules for Solid code.
