# Bricks

A brick is one capability of the system, at the level of a person who decides what to build next. The bricks follow a logical order, starting with the basic capabilities. Each status is true at the [snapshot](../upstream.md#snapshot).

## Status legend

- **shipped**: the capability works at the snapshot
- **partial**: a part of the capability works at the snapshot
- **planned**: a source states the capability as a plan, and the code does not have it
- **dropped**: the code had the capability, and a later commit removed it

Each brick has a source: **upstream** for Daniel's project, or **uao** for Pascal's direction.

## Add a brick

1. Add a brick only for a capability. A task or a fix is not a brick
2. Take the next free number
3. Put the row where the brick fits in the order
4. Create the file `B<nn>-<slug>.md`
5. Copy the sections of [B01](B01-durable-conversations.md) into it
6. Fill each section
7. Omit a section that has nothing to record
8. For a planned brick, cite the source that states the plan. Without such a source, do not add the brick
9. Link to the decisions behind the brick, and to the docs that hold its mechanics
10. Put each gap or wish in [Next](#next), not in the brick

## Index

| Brick                                      | Name                                 | Status  | Source   |
| ------------------------------------------ | ------------------------------------ | ------- | -------- |
| [B01](B01-durable-conversations.md)        | Durable conversations                | shipped | upstream |
| [B02](B02-self-change-while-running.md)    | Self-change while running            | shipped | upstream |
| [B03](B03-reloadable-extensions.md)        | Reloadable extensions and surfaces   | shipped | upstream |
| [B04](B04-models-and-providers.md)         | Models and providers                 | shipped | upstream |
| [B05](B05-agent-tools.md)                  | Agent tools                          | shipped | upstream |
| [B06](B06-project-specialization.md)       | Project specialization               | shipped | upstream |
| [B07](B07-conversation-tree.md)            | Conversation tree and project memory | shipped | upstream |
| [B08](B08-ultimate-and-standing-agents.md) | @ultimate and standing agents        | shipped | upstream |
| [B09](B09-coordinators-and-subagents.md)   | Coordinators and subagents           | shipped | upstream |
| [B10](B10-isolates-previews-lander.md)     | Isolates, previews, and the lander   | shipped | upstream |
| [B11](B11-notes-and-messages.md)           | Notes and messages                   | shipped | upstream |
| [B12](B12-human-in-the-loop.md)            | Human in the loop                    | shipped | upstream |
| [B13](B13-background-work.md)              | Background work                      | shipped | upstream |
| [B14](B14-everything-on-record.md)         | Everything on record                 | shipped | upstream |
| [B15](B15-dreams-and-chapters.md)          | Dreams and chapters                  | shipped | upstream |
| [B16](B16-remote-backup-update.md)         | Remote access, backups, and updates  | shipped | upstream |

Dropped: the Canvas map ([D014](../decisions/D014-remove-canvas.md)) and the cloud fleet ([D028](../decisions/D028-cloud-only-backs-up.md)).

## Next

Each item below is a gap or a wish that a source states. The code does not cover it at the snapshot:

- A better flow timeline. The post says that the timeline "isn't ideal yet" (section "An Example: Side Chats"). See [B14](B14-everything-on-record.md)
- Design polish. The post says that the design is "functional, but not super nice" (section "Just Getting Started")
- Subscriptions that move into a new chapter. At the snapshot, a dream turns each user subscription into a to-do to create the subscription again (`74f38c9`, `extensions/dream/README.md`). See [B15](B15-dreams-and-chapters.md)
- The removal of the local Pi patches and couplings when Pi exports or fixes what they replace (`docs/pi-upstream.md`). See [B01](B01-durable-conversations.md)

uao has no plan of its own yet. A planned brick with `Source: uao` comes only from Pascal.
