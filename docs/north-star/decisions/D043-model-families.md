# D043 Run agents and features on model families

Decided 2026-10-28, revised 2026-10-29. Source: upstream. Status: active.

Agent definitions and model features use named model families (`741ec0da`). A model pin takes precedence over a family (`lib/families.ts`). A family in an overlay replaces an earlier model pin (`a0b75c9e`). The Agents panel configures families and their assignments (`490f88b2`).

**Why.** One family change sets the model for each assigned agent or feature (`741ec0da`). Open conversations keep their model (`extensions/models/README.md`).

**Rejected.** Per-model concurrency caps were added with families, then removed before the snapshot (`741ec0da`, `a0b75c9e`). No local models needed them, and they added core code (`a0b75c9e`).

**Evidence.** `741ec0da`, `a0b75c9e`, `490f88b2`, and `11809560`. [Model families](../../../extensions/models/README.md#model-families) holds the settings and precedence.
