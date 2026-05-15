# OpenCAD Examples (Scripts Directory)

This folder contains runnable OpenCAD example scripts.

For the fastest onboarding, use:

- [../README.md](../README.md) for repository entry
- [../docs/QUICKSTART.md](../docs/QUICKSTART.md) for setup and first run
- [../docs/EXAMPLES.md](../docs/EXAMPLES.md) for script selection
- [../docs/AGENT_EXAMPLES.md](../docs/AGENT_EXAMPLES.md) for agent usage

## Run an example

```bash
python -m opencad.cli run examples/hardware_mounting_bracket.py \
  --export bracket.step \
  --tree-output bracket-tree.json
```
