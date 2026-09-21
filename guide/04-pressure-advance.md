# Pressure Advance and Linear Advance

Molten polymer, filament, Bowden tubes, and the extrusion path behave like a
spring-damper system. When toolhead speed changes, nozzle pressure does not
change instantly. Pressure advance compensates for that lag by adjusting
extruder motion around acceleration and deceleration.

Common names include:

- Pressure Advance in Klipper and RepRapFirmware;
- Linear Advance or K-factor in Marlin;
- flow dynamics or similar vendor-specific terms.

The values are not portable between algorithms or firmware families.

## What PA Can and Cannot Fix

Correct PA can reduce:

- bulging at corners and line ends;
- thin starts after acceleration;
- pressure-related seam blobs or gaps;
- inconsistent width during speed transitions.

PA does not correct:

- the total amount of material commanded;
- wet filament;
- a partial clog;
- backlash, loose belts, or resonance;
- a wrong dimensional scale;
- poor cooling or unsupported geometry.

## Prerequisites

Before testing:

- settle temperature;
- stay below the safe MVS ceiling;
- use a mechanically sound extruder and nozzle;
- disable conflicting slicer pressure tricks where the firmware documentation
  requires it;
- choose representative speed and acceleration;
- confirm which firmware or slicer owns the active PA value.

## Test Methods

### Line or pattern test

Alternates slow and fast segments across a range of PA values. It is fast and
material-efficient but depends heavily on first-layer quality.

### Tower test

Changes PA with height and shows repeated corners. It is slower but easier to
read when first-layer variation would obscure a line test.

### Adaptive test

Some slicers can model PA across multiple flow and acceleration conditions.
This is useful only when the hardware, firmware, and slicer support it and when
a single value is demonstrably inadequate. Establish a good fixed PA first.

## Read the Result

| Appearance | Likely interpretation |
| --- | --- |
| Corner protrudes or remains swollen | PA too low |
| Line becomes thin before or after speed change | PA too high |
| Corner is sharp with continuous adjacent line | useful region |
| Only layer-change corner is damaged | seam/retraction contamination; read other corners |
| All values look poor | wrong range, flow saturation, mechanical problem, or wet filament |

Klipper specifically advises ignoring the corner with the seam when reading its
tower. When several values are equally good, choose the lower acceptable value;
excessive PA can create subtle starvation and demands more extruder response.

## Calculation Example

If a tower starts at `0.000`, increases by `0.002` per millimeter, and the best
region is `8 mm` above the start:

```text
PA = start + step * height
PA = 0.000 + 0.002 * 8 = 0.016
```

Use the exact generator formula. Some tests change per layer rather than per
millimeter.

## Dependence on Print Conditions

PA can change with:

- material and moisture;
- temperature and volumetric flow;
- nozzle and hotend;
- direct-drive versus Bowden path;
- acceleration and requested speed;
- flexible or highly compressible filament.

Retest after a meaningful upstream change. If a production profile spans a very
wide flow and acceleration range, validate the compromise at slow external
walls and fast internal features.

## Do Not Judge PA by the Seam Alone

Seam placement, retraction, wipe, travel distance, ooze, and layer change can
hide an otherwise correct PA value. Use non-seam corners for the initial PA
decision, then return to seam tuning later.

Next, tune [global flow ratio](05-flow-ratio.md).

