# uao north-star

This folder is the one map of uao, for Pascal and for agents. It says what the system is for, what it can do, and why it works this way. Each claim cites a short SHA or a path as its evidence. The mechanics stay in `AGENTS.md`, `docs/`, and the extension READMEs, and the north-star links to them.

## Snapshot

Each status in this folder is true at this commit:

- Upstream: `HazAT/ultimate` at `33c05e9`, 2026-10-23
- Fork: `pascalandy/uao` at `7698625`, 2026-10-23, which is upstream plus one README line

`git log --oneline 33c05e9..$(git merge-base HEAD upstream/main)` lists the upstream commits that this map does not cover. No output means the map is current. The command needs the `upstream` remote.

## Find what you need

At the start of each session, read the files in the first three rows. When another row applies, read its file.

| Question                                     | File                                               | Read it when                     | Update it when                                    |
| -------------------------------------------- | -------------------------------------------------- | -------------------------------- | ------------------------------------------------- |
| What is uao, and where does it go?           | [vision.md](vision.md)                             | You start a session              | The purpose or the direction changes              |
| Which rules shape every design choice?       | [principles.md](principles.md)                     | You start a session              | A principle changes, with its decision            |
| Can I push? How do changes land?             | [dev-preferences.md](dev-preferences.md)           | You start a session              | Pascal states a new preference                    |
| What can the system do, and what comes next? | [bricks/README.md](bricks/README.md)               | You plan a new capability        | A brick changes status, or a source states a plan |
| Why does the system work this way?           | [decisions/README.md](decisions/README.md)         | You ask why a rule exists        | A choice with lasting effect is made              |
| What does a word mean?                       | [glossary.md](glossary.md)                         | A word is unclear                | Before the first use of a new term                |
| Where does each part live?                   | [architecture.md](architecture.md)                 | You change code                  | A process, a layer, or a folder changes           |
| How does uao relate to upstream?             | [upstream.md](upstream.md)                         | You merge, or see HazAT          | After a merge of upstream                         |
| How do I write an extension?                 | [extensions/README.md](../../extensions/README.md) | You write an extension           | Not from the north-star                           |
| What survives a crash?                       | [docs/durability.md](../durability.md)             | You change persistence or replay | Not from the north-star                           |
| What did Daniel ask for first?               | [first-prompt.md](sources/first-prompt.md)         | The original intent is unclear   | Never. It is a source                             |
| How do I run, test, or change the code?      | [AGENTS.md](../../AGENTS.md)                       | Before you change code           | Not from the north-star                           |

To add a brick or a decision, follow [Add a brick](bricks/README.md#add-a-brick) or [Add a decision](decisions/README.md#add-a-decision).

## Status legend

A brick has one of these statuses:

- **shipped**: the capability works at the snapshot
- **partial**: a part of the capability works at the snapshot
- **planned**: a source states the capability as a plan, and the code does not have it
- **dropped**: the code had the capability, and a later commit removed it

A decision is **active**, or **replaced by Dnnn** when a later decision takes its place. Each brick and decision has a source: **upstream** for Daniel's project, or **uao** for Pascal's direction.

## Update rules

- Keep one home for each fact. Link to the mechanics. Restate a fact only when the reader cannot reach its source
- Cite evidence for each status, decision, and claim about behavior. Put the short SHA or the path in the same sentence or row. Write "(inferred)" after an inference
- Keep one snapshot. Each status must be true at the snapshot commit. After a merge of upstream, follow the [sync rule](upstream.md#sync-rule)
- Mark each brick and decision `Source: upstream` or `Source: uao`. A guess about Pascal's direction is not a decision
- Link down, not up. This README links to each file and index. The vision links to bricks. The principles and the bricks link to decisions. The bricks link to code and docs. A decision does not list the bricks that use it
- Use the names in the [glossary](glossary.md). Add a new term there before its first use
- Write in English, also when Pascal writes in French. Write the north-star in ASD-STE100 Simplified Technical English
- Copy a source word for word only in `sources/`. Name the origin of each copy
- Before a commit, run the checks in [How a change lands](dev-preferences.md#how-a-change-lands)
