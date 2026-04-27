# OpenCAD Examples

These examples show how to use the in-process OpenCAD API to model parts that commonly
appear in collaborative device-development work across hardware, software, and firmware
teams.

## Included scripts

- `hardware_mounting_bracket.py` — mechanical mounting bracket with fastener holes
- `hardware_pcb_carrier.py` — carrier plate for a controller or sensor PCB
- `software_hmi_panel.py` — front panel for a software-driven operator interface
- `firmware_programmer_fixture.py` — fixture plate for firmware flashing or debug access
- `full_device_cable_grommet.py` — cable-management part built from primitive booleans
- `agents/generate_mounting_bracket_code.py` — agent-driven example-style code generation

## Running an example

From the repository root:

```bash
python -m opencad.cli run examples/hardware_mounting_bracket.py \
  --export bracket.step \
  --tree-output bracket-tree.json
```

Each script leaves the final part in the default runtime context, so the CLI can export
both a STEP file and a serialized feature tree.

For agent-focused examples, see [`examples/agents/README.md`](agents/README.md).
