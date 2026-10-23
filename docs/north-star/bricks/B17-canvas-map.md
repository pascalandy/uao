# B17 Canvas map

Status: dropped, at the snapshot. Source: upstream.

The Canvas showed each conversation and its subagents as a live map that the user could zoom, with conclusion cards for settled trees. Ultimate removed it to center on conversations. The code stays on the upstream branch `park/canvas`.

## How it works

A radial layout kept each branch in place when new agents arrived (`9c129ad`). The summary model wrote the conclusion cards.

## Where it lives

- The upstream branch `park/canvas`. Nothing on main

## Decisions

- [D014](../decisions/D014-remove-canvas.md) Remove the Canvas surface

## Next

- Nothing stated. `deb65f8` keeps the code "for possible future work"

## Evidence

- `9c129ad` adds the Canvas
- `deb65f8` removes it
