# Speed Tab

All groups in this chapter are **Shared 2.4.2**. A speed target is a request, not
a guarantee: acceleration, path length, cooling, and maximum volumetric flow
may prevent the machine from reaching it.

## First Layer Speed

**What:** controls extrusion and travel while adhesion is being established.

**Use it when:** the first layer drags, curls, fails to join, or is disturbed by
fast travel even though Z offset and plate preparation are correct.

**Desired result:** continuous, well-attached roads with clean direction changes
and no nozzle pickup.

- `Initial layer speed` covers first-layer walls and ordinary extrusion.
- `Initial layer infill speed` sets broad first-layer fill independently.
- `Initial layer travel speed` controls non-extruding moves near fresh roads.
- `Number of slow layers` ramps toward normal speed instead of changing
  abruptly after layer one.

## Other Layers Speed

**What:** assigns speed targets by feature role.

**Use it when:** one role has a different finish, dimensional, cooling, or flow
requirement from the rest of the part.

**Desired result:** visible and critical features receive conservative motion,
while hidden, well-supported features use available throughput safely.

- `Outer wall speed` strongly influences visible finish and dimensional
  consistency.
- `Inner wall speed` can be faster, provided it remains within melt and motion
  limits and does not disturb the outer wall.
- `Small perimeter speed` and its size threshold slow short loops that cannot
  settle thermally or dynamically.
- `Sparse infill speed` is usually throughput-oriented.
- `Internal solid infill speed` must still provide a stable base for top skins.
- `Top surface speed` trades time for visible consistency and closure.
- `Gap infill speed` protects short, pressure-sensitive roads.
- `Ironing speed` works with ironing flow and spacing.
- `Support speed` and `support interface speed` separate disposable structure
  from the layer touching the model.

If a defect begins only above a certain speed, confirm maximum volumetric flow
before lowering every feature speed.

## Overhang Speed

**What:** slows partially unsupported walls by degree and assigns external and
internal bridge speeds.

**Use it when:** ordinary walls are clean but overhang edges curl or bridges sag.

**Desired result:** each new road remains attached to the previous layer and has
time to cool before the next pass.

- `Slow down for overhangs` enables percentage-based overhang bands.
- The four overhang speeds cover increasingly unsupported portions of a road;
  zero means use the normal wall behavior for that band.
- `Slow down for curled perimeters` reduces speed where the slicer predicts a
  collision-prone curled edge.
- External and internal `bridge speed` can differ because visible spans and
  buried spans have different priorities.

Cooling and nozzle temperature can dominate this test. Keep them fixed while
comparing speeds.

## Travel Speed

**What:** sets non-extruding movement speed.

**Use it when:** travel time contributes to ooze, stringing, or heat marks, or
the machine becomes noisy and inaccurate during rapid repositioning.

**Desired result:** prompt movement between features without skipped motion,
frame excitation, or disturbance of fresh plastic.

High travel speed can reduce ooze time but only if acceleration and mechanics
can support it. A short move may never reach the requested value.

## Acceleration

**What:** controls how quickly speed changes for each feature role.

**Use it when:** ringing, rounded corners, weak start/stop behavior, or excessive
print time comes from transitions rather than steady speed.

**Desired result:** the highest acceleration that preserves placement, corner
quality, extrusion response, and mechanical reliability.

- `Normal printing acceleration` is the fallback.
- Outer wall, inner wall, bridge, sparse infill, internal solid infill, top
  surface, first layer, first-layer travel, and travel accelerations provide
  role-specific limits.
- `Acceleration to deceleration` and its factor limit abrupt transition energy
  where supported by the selected firmware and G-code flavor.

Pressure advance must be calibrated for the actual acceleration regime. Do not
use low acceleration to conceal badly tuned extrusion pressure.

## Junction Deviation

**What:** requests a cornering model based on allowed path deviation rather than
a direct instantaneous speed-change number.

**Use it when:** the firmware and G-code flavor support junction deviation and
corner behavior needs a profile-level limit.

**Desired result:** controlled corner speed without visible ringing or excessive
rounding.

Do not tune junction deviation and classic jerk simultaneously. Confirm which
model the firmware actually consumes.

## Jerk (XY)

**What:** supplies feature-specific corner-transition limits for firmware that
uses classic jerk-style controls.

**Use it when:** supported firmware shows ringing, harsh motion, or rounded
corners that depend on feature role.

**Desired result:** crisp but mechanically calm direction changes.

- Default, outer-wall, inner-wall, infill, top-surface, first-layer,
  first-layer-travel, and travel jerk targets are available.

Values and meanings are firmware-specific. A number copied from another motion
system is not a calibration.

## Advanced Speed

**What:** limits how quickly commanded extrusion rate may change along a path.

**Use it when:** a high-flow transition creates gloss bands, pressure shocks, or
inconsistent width even though maximum volumetric flow and pressure advance are
already calibrated.

**Desired result:** smoother extrusion-rate transitions without slowing the
entire model more than necessary.

- `Maximum volumetric extrusion rate slope` limits rate-of-change.
- `Slope segment length` sets the distance over which the limiter evaluates the
  change.
- `External perimeter only` confines smoothing to visible walls when internal
  throughput need not be limited.

This is an advanced transition tool, not a replacement for the filament's
maximum volumetric speed.

Use [Motion Diagnostics](19-motion-diagnostics.md) when the question is whether
texture comes from acceleration, input shaping, VFA, or hidden geometry rather
than a single feature-speed setting.

Continue with the [Support tab](15-support-tab.md).
