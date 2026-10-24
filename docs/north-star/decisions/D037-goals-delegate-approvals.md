# D037 Let a user-granted goal delegate approvals

Decided 2026-10-24. Source: upstream. Status: active.

During a user-granted hands-off goal, @ultimate gives the approvals that [D017](D017-questions-get-proposals.md) assigns to the user (`001a193d`). @ultimate records each goal decision with its reason (`extensions/goal/README.md`). Secrets, logins, and force pushes still need the user (`agents/ultimate.md`).

**Why.** The goal lets work continue while the user is away (`extensions/goal/README.md`). The commit gives no further reason (`001a193d`).

**Evidence.** `001a193d` adds goals and changes the approval instructions. `65a251f` makes each goal change and its card delivery durable. `extensions/goal/README.md` holds the goal mechanics. `agents/coordinator.md` and `skills/ui-preview-round/SKILL.md` accept @ultimate's approvals during the goal.
