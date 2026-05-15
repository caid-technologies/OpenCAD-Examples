# Example Catalog

Use this file to quickly choose the right script.

## Hardware-focused

- `examples/hardware_mounting_bracket.py`  
  Mounting bracket with corner fastener holes and center cable pass-through.

- `examples/hardware_pcb_carrier.py`  
  PCB carrier plate with mounting holes and a center clearance opening.

## Software-interface-focused

- `examples/software_hmi_panel.py`  
  Front panel with display/button cutouts and an encoder opening.

## Firmware-focused

- `examples/firmware_programmer_fixture.py`  
  Fixture plate for programming header access and alignment points.

## Full device / cable management

- `examples/full_device_cable_grommet.py`  
  Simple cable grommet formed from concentric cylindrical booleans.

## Run any script

```bash
python -m opencad.cli run <script-path> --export output.step --tree-output output-tree.json
```

Example:

```bash
python -m opencad.cli run examples/software_hmi_panel.py \
  --export hmi-panel.step \
  --tree-output hmi-panel-tree.json
```
