# D018 Keep a personal layer apart from Pi

Decided 2026-10-17. Source: upstream. Status: active.

Ultimate reads personal skills and instructions only from `~/.ultimate/`, not from Pi's personal layer. Ultimate still shares logins, models, and settings with Pi. To use a Pi skill, link it into `~/.ultimate/skills/`.

**Why.** Pi's personal layer can hold instructions that contradict Ultimate's coordinator role (`ec5dfad`).

**Rejected.** All of Pi's personal skills and its global `AGENTS.md` (`ec5dfad`).

**Evidence.** `ec5dfad`. `docs/settings.md` holds the order.
