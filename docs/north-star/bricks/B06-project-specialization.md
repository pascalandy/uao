# B06 Project specialization

Status: shipped, at the snapshot. Source: upstream.

A project adds its own tools, panels, surfaces, agents, skills, and settings in its `.ultimate/` folder, and commits them. Everyone who opens the project and trusts it gets the same specialized agent ([D009](../decisions/D009-trust-before-project-setup.md)). The core stays the same in every project. The README calls the product "a coding agent you specialize for the project you work on".

A trusted project can also share skills in `<project>/.agents/skills/` (`server/skills.ts`).

The **Agents tab** saves an extended definition as an overlay, so the base still supplies its instructions and tools (`lib/agents.ts`). The **Agents tab** refuses changes that an overlay cannot express (`lib/agents.ts`).

An enabled extension can ship agent definitions in its own `agents/` folder (`ab959a36`). Disabling the extension removes those definitions (`ab959a36`).

An agent definition can name a model family ([D043](../decisions/D043-model-families.md)). A standing agent's frontmatter can set its icon and tint (`17157665`), and a `title` that the UI shows as its name (`b9fb3b92`). A subagent can also start without a definition, from a label, a family or a model, tools, and instructions (`6b0fb859`).

Extensions declare their required secrets for setup and the Secrets panel (`457c5a53`, `40b17d20`). A named provider's login can satisfy a declared secret (`07172eed`). An OpenAI API key login can supply the `OPENAI_API_KEY` of voice. An OAuth login cannot (`fa24927a`).

An agent definition can list the skills that its agent sees in `skills:`. An empty list gives no skills, and no list gives all skills. The Agent card shows the listed skills as pills (`85b68619`, [Discovery and settings](../../../docs/settings.md)). The shipped scout, dream-pass, watcher, and reviewer definitions have empty lists (`3f1ca441`).

A project's `.ultimate/settings.json` can set the name and the icon of its installed app with `app`, and fix the port with `port` (`b1012b4f`, [Discovery and settings](../../../docs/settings.md)). A taken port then stops the start with its number (`docs/running.md`). While the project's `.ultimate/` is undecided, setup shows a warning (`a100d9ff`).

## Where it lives

- `.ultimate/`: the setup of this repository, an example
- `skills/integrate-ultimate/SKILL.md`: the specialization workflow
- `skills/write-extension/`, `skills/ui-preview-round/`, and `skills/verify-ui/`: procedures for extensions and UI checks
- `server/skills.ts`: skill discovery, diagnostics, scopes, and `/skill:name` commands
- `extensions/onboarding/`: setup cards, the project choice, and the Extensions panel
- `lib/discovery.ts` and `lib/project-setup.ts`: precedence and trust
- `lib/agents.ts`: definition discovery and overlay saves
- `skills/adopt-ultimate-setup/SKILL.md`: selection and adaptation of this repository's project setup

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
- `e099781` lets a project commit script triggers in `<project>/.ultimate/automations/<slug>/`
- `f23fbeb` adds skill scopes, diagnostics, and `/skill:name` commands
- `9e00ce6` keeps personal skills in `~/.ultimate/skills/`
- `bc3a786` adds three built-in skills for extensions and UI checks
- `d3c39fd` lets the **Agents tab** save overlays
- `ba7984e` keeps an overlay's `addTools` when its base inherits every tool
- `710be091` adds a tour that adapts selected project setup without copying the whole folder
- `e342ebe8` preserves symlinks during atomic JSON writes
- `85b68619` adds the skills list of a definition
- `b1012b4f` adds the app name, the app icon, and the fixed port of a project
