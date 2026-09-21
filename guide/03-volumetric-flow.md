# Maximum Volumetric Flow

Maximum volumetric flow is the amount of plastic the complete extrusion system
can melt and deposit per second under defined conditions. It is not a universal
hotend specification. Filament, temperature, nozzle geometry, extruder grip,
and cooling all affect the result.

## The Basic Equation

For a straight extruded path:

```text
volumetric flow (mm^3/s) = speed (mm/s) * line width (mm) * layer height (mm)
```

Rearranged:

```text
maximum speed = maximum volumetric flow / (line width * layer height)
```

Example:

```text
MVS = 15 mm^3/s
line width = 0.45 mm
layer height = 0.20 mm
maximum steady extrusion speed = 15 / (0.45 * 0.20) = 166.7 mm/s
```

The machine may still be limited by acceleration, motion, minimum layer time,
or feature-specific speed.

## Why Tune MVS Before Flow Ratio

A flow-ratio test printed beyond the melt limit can look under-extruded even
when the ratio is correct. Establish a safe throughput region first so later
tests evaluate the requested setting rather than hotend saturation.

## Printed Ramp Method

Use a tower or continuous artifact whose requested volumetric flow increases
with height.

1. Use the accepted nozzle temperature and representative cooling.
2. Set a sufficiently high feature speed so MVS is the limiting factor.
3. Confirm the actual flow range in the slicer preview.
4. Print while watching for the first sustained change.
5. Measure the height of the onset and calculate the corresponding flow.

Failure evidence includes:

- matte or changed gloss that persists;
- thin, rough, or discontinuous lines;
- gaps between walls;
- missing material after acceleration;
- extruder clicking, skipping, or filament grinding;
- a sudden loss of layer adhesion;
- inability to hold nozzle temperature under load.

Ignore a single isolated blemish. Select the start of a sustained trend.

## Gravimetric Extrusion Method

An optional bench method commands a known filament length at increasing rates,
weighs the output, and compares actual mass with expected mass. This can reveal
gradual flow drop-off before obvious print failure. It requires a reliable scale,
known filament density or a consistent reference mass, safe collection of hot
extrudate, and careful control of temperature and timing.

The printed-ramp method is simpler and includes motion and deposited-line
behavior. The gravimetric method is useful for comparing hotends or diagnosing
the extrusion system itself. Do not treat the two results as interchangeable.

## Set a Production Limit

For a general-quality profile, set the slicer MVS below the first sustained
quality loss. A practical starting margin is `5-10%`:

```text
profile MVS = observed onset * 0.90 to 0.95
```

Use a larger margin for structural parts, long jobs, variable ambient
conditions, or spools with inconsistent diameter. A speed-focused infill
profile may accept more risk than an external-wall profile, but the tradeoff
must be explicit.

## Retest When These Change

- filament material, formulation, color, or moisture state;
- nozzle diameter, material, geometry, or wear;
- hotend, heater, heatbreak, or extruder;
- nozzle temperature;
- high-flow insert or nozzle;
- substantial layer-height or line-width regime;
- unusual backpressure from filled, flexible, or highly viscous material.

## Strength Is a Separate Limit

The highest flow that looks continuous may not produce the strongest layer
bond. If the part is structural, compare strength at the intended production
flow and at a slower control. Surface appearance alone does not establish melt
quality throughout the bead.

With a safe flow envelope established, tune
[pressure advance](04-pressure-advance.md).

