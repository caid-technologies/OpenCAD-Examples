# OpenCAD Examples

This repository contains small, focused OpenCAD scripts that demonstrate how to model
hardware, software interface, firmware support, and full-device parts. Each example is
standalone and can be run directly with the OpenCAD CLI.

## Repository layout

- `examples/hardware` — mechanical brackets, carriers, and similar parts
- `examples/software` — enclosures or panels driven by software UI needs
- `examples/firmware` — fixtures and tooling that support firmware workflows
- `examples/device` — full-device or multi-discipline parts
- `examples/agents` — agent-driven code generation examples

For a detailed list of scripts, see [`examples/README.md`](examples/README.md).

## Running an example

From the repository root:

```bash
python -m opencad.cli run examples/hardware/hardware_mounting_bracket.py \
  --export bracket.step \
  --tree-output bracket-tree.json
```
