# D011 Land through a durable queue

Decided 2026-10-13. Source: upstream. Status: replaced by D042.

The original queue merged clean submissions, ran checks, fast-forwarded the target, and pushed without force (`5c36dcd`). `ef883740` then made the lander a standing agent with a model that handled failures and messages. [D042](D042-model-free-landing.md) replaces that model with failure reports to the submitter.

**Why.** Coordinators spent many turns to merge, check, land, and push. Also, `workspace land` often failed on a target that advanced or on an unrelated dirty file (`5c36dcd`).

**Rejected.** Synchronous `workspace land` as the default end of a branch (`5c36dcd`). `cfd0e93b` later removes it ([D042](D042-model-free-landing.md)).

**Evidence.** `5c36dcd` adds the queue. `ef883740` adds the former lander definition and its model. `extensions/workspaces/README.md` holds the current model-free mechanics.
