# Quick Start

## 1) Requirements

You need a Python environment where the OpenCAD CLI is available.

## 2) Run a shipped example

From the repository root:

```bash
python -m opencad.cli run examples/hardware_mounting_bracket.py \
  --export bracket.step \
  --tree-output bracket-tree.json
```

## 3) Check output files

- `bracket.step`: CAD export
- `bracket-tree.json`: serialized feature tree

## 4) Try another example

See [EXAMPLES.md](EXAMPLES.md) for a quick chooser.

## 5) Generate example code with the agent (optional)

See [AGENT_EXAMPLES.md](AGENT_EXAMPLES.md).
