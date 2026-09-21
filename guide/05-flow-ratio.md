# Global and Feature-Specific Flow

Flow ratio, also called extrusion multiplier, scales the amount of material the
slicer commands. Tune it for continuous, well-formed extrusion. Do not use it
as a general dimensional correction.

## Global Flow Versus Volumetric Flow

These are different controls:

- **Flow ratio** scales commanded material, such as `0.98` for `98%`.
- **Maximum volumetric flow** limits how quickly material is requested.

A correct flow ratio can still fail above the hotend's melt capacity. A low MVS
cannot repair an incorrect flow ratio; it only keeps requests inside a safer
rate.

## Use a Broad Top Surface

A useful visual test has:

- enough bottom layers and infill to support the top;
- several top layers;
- a broad region with long, parallel top lines;
- known top line width and moderate speed;
- enough perimeter distance to reveal wall-interface behavior.

Inspect with both sight and touch under glancing light.

### Too low

- open channels or dark valleys between lines;
- pinholes or incomplete closure;
- top lines separate from the perimeter;
- roughness caused by unsupported strands;
- weak, easily separated walls when other causes are excluded.

### Useful region

- continuous lines with no broad open channels;
- an even tactile surface;
- clean contact with perimeter walls;
- no repeated nozzle plowing or material pileup.

### Too high

- raised ridges that catch a fingernail;
- nozzle scars or plowing;
- material accumulating at line ends and walls;
- rough, overfilled corners;
- dimensional swelling across otherwise simple features.

Microscopic gaps visible only under extreme magnification can be normal. Judge
whether the surface meets its functional purpose.

## Coarse and Fine Passes

1. Start from a sane material profile.
2. Compare broad changes, often `1-2%`, to locate the useful region.
3. Refine around the best result in `0.5%` steps when needed.
4. Confirm on a fresh specimen.

If the starting ratio is `0.98` and a candidate modifier is `+2%`:

```text
new ratio = 0.98 * 1.02 = 0.9996
```

Confirm the calibration generator's formula. Some tools add percentage points;
others multiply the current value.

## Measured Single-Wall Methods

Prusa documents a vase-wall measurement method. It can work with a suitable
micrometer and controlled geometry, but ordinary calipers, rounded beads,
corner pressure, wall flex, and slicer line-width models can introduce large
relative error. Ellis' guide cautions against treating a single extruded wall
as an exact rectangular bead.

Policy for this guide:

- prefer the visual/tactile top-surface method for routine flow tuning;
- use measured mass or carefully designed walls when the experiment calls for
  them and the uncertainty is understood;
- solve dimensions with dimensional tests, not a wall-flow shortcut.

## Feature-Specific Flow

If walls and general extrusion are correct but one feature is deficient, use a
feature-specific control where available:

- top or bottom solid infill flow;
- bridge flow;
- internal solid-infill flow;
- support-interface flow;
- first-layer flow.

Effective feature flow is often multiplicative:

```text
effective top flow = global filament flow * top-surface flow ratio
```

Example:

```text
global flow = 0.98
top flow = 1.04
effective top flow = 0.98 * 1.04 = 1.0192
```

This deposits `1.92%` more than nominal on top surfaces while leaving walls at
the accepted global ratio.

## First-Layer and Top-Surface Traps

A rough top can originate below the visible layer. Check:

- insufficient top-shell thickness;
- sparse or poorly supported infill;
- pillowing from heat and inadequate cooling;
- warped lower layers;
- first-layer over-compression carried through a thin object;
- an unsuitable top pattern, speed, or line width.

Do not raise global flow if only the top skin is deficient and the walls,
dimensions, and other solid layers are correct.

Continue with [Cooling and Retraction](06-cooling-and-retraction.md).

