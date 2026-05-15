# OpenCAD Examples

Practical OpenCAD scripts for common hardware, software-interface, and firmware fixture scenarios.

If you want to get running immediately, start here:

1. Read [docs/QUICKSTART.md](docs/QUICKSTART.md)
2. Pick an example from [docs/EXAMPLES.md](docs/EXAMPLES.md)
3. For AI-generated example code, use [docs/AGENT_EXAMPLES.md](docs/AGENT_EXAMPLES.md)

## Repository layout

- `examples/` — runnable OpenCAD example scripts
- `examples/agents/` — agent-driven code generation example
- `docs/` — step-by-step usage guides

## Run a first example

From the repository root:

```bash
python -m opencad.cli run examples/hardware_mounting_bracket.py \
  --export bracket.step \
  --tree-output bracket-tree.json
```

This exports:

- `bracket.step` (3D model)
- `bracket-tree.json` (feature tree)
