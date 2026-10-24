# B06 Project specialization

Status: shipped, at the snapshot. Source: upstream.

A project adds its own tools, panels, surfaces, agents, skills, and settings in its `.ultimate/` folder, and commits them. Everyone who opens the project and trusts it gets the same specialized agent ([D009](../decisions/D009-trust-before-project-setup.md)). The core stays the same in every project. The README calls the product "a coding agent you specialize for the project you work on".

## Where it lives

- `.ultimate/`: the setup of this repository, an example
- `skills/integrate-ultimate/SKILL.md`: the specialization workflow
- `extensions/onboarding/`: setup cards, the project choice, and the Extensions panel
- `server/discovery.ts` and `server/project-setup.ts`: precedence and trust

## Decisions

- [D006](../decisions/D006-clone-apart-from-project.md) Keep the clone apart from the project
- [D009](../decisions/D009-trust-before-project-setup.md) Load a project setup only after the user trusts it
- [D018](../decisions/D018-own-personal-layer.md) Keep a personal layer apart from Pi
- [D027](../decisions/D027-project-code-through-branches.md) Send project code through a branch

## Evidence

- `1135742` separates the clone from the project
- `a5fe6b8` requires project trust before the project setup
- `248b25f` ships the `integrate-ultimate` skill
- `9d40a9b` adds `addTools` overlays
- `8cc313c` lets a project commit subscriptions
