# B06 Project specialization

Status: shipped, at the snapshot. Source: upstream.

A project adds its own tools, panels, surfaces, agents, skills, and settings in its `.ultimate/` folder, and commits them. Everyone who opens the project gets the same specialized agent, and the core stays the same in every project. The README calls the product "a coding agent you specialize for the project you work on".

## How it works

Ultimate loads a project's `.ultimate/` only after the user trusts the project. Personal additions live in `~/.ultimate/` and follow the user to each project. The `integrate-ultimate` skill studies a project, suggests a few additions, and builds only the ones that the user picks. @ultimate writes configuration itself, and project code goes through a branch. An `addTools` overlay adds tools to a built-in agent with no full copy. [Discovery and settings](../../../docs/settings.md) holds the rules.

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

## Next

- Nothing stated

## Evidence

- `1135742` separates the clone from the project
- `a5fe6b8` gates the project setup on trust
- `248b25f` ships the `integrate-ultimate` skill
- `9d40a9b` adds `addTools` overlays
- `8cc313c` lets a project commit subscriptions
