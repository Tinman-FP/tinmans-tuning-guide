# Dimensional Accuracy and Tolerances

Dimensional tuning works only when the cause of the error is classified. A
proportional scale error, a constant contour offset, an undersized hole, and an
elephant foot require different controls.

## Measure After Extrusion Is Stable

Settle temperature, MVS, PA, flow, and cooling first. Otherwise a geometry test
can accidentally encode an extrusion defect into compensation.

Measurement protocol:

1. Let the part fully cool and condition consistently.
2. Zero and check the measurement tool.
3. Measure several points and both principal XY axes.
4. Avoid seams, corners, embossed text, and bottom flare.
5. Record raw values before averaging.
6. Use a larger test piece when the expected correction approaches the tool's
   uncertainty.
7. Include external and internal features.

## Classify the Error Model

### Proportional material scale error

The error grows with feature size. Use per-filament shrinkage or scale
compensation.

### Nearly constant external offset

Different-sized external features are all too large or small by a similar
absolute amount. Use contour compensation after confirming flow and PA.

### Internal holes differ from external contours

Use hole compensation, precise-wall controls, polyholes, or a design tolerance
after testing multiple hole sizes and orientations.

### Bottom layers alone are enlarged

Use elephant-foot compensation, first-layer/Z correction, or bed-temperature
changes. Do not scale the entire model.

### X and Y disagree

Investigate belts, squareness, mechanics, axis-specific motion, cooling
direction, and measurement method before applying one shared material value.

## Proportional Compensation Formula

For slicers that request the measured cooled percentage, including OrcaSlicer's
documented shrinkage field:

```text
measured percentage = measured dimension / nominal dimension * 100
effective correction scale = 100 / measured percentage
```

If a nominal `100.00 mm` feature measures `99.40 mm`:

```text
measured percentage = 99.40%
correction scale = 100 / 99.40 = 1.006036
```

The slicer expands the model by about `0.6036%`.

## Worked Field Example

A controlled `20.00 mm` cube measured:

```text
X = 20.13 mm
Y = 20.13 mm
Z = 20.00 mm
```

The measured XY percentage was:

```text
20.13 / 20.00 * 100 = 100.65%
```

The corresponding effective scale was:

```text
100 / 100.65 = 0.993542
```

After entering `100.65%` as the XY measured percentage and retaining `100%` in
Z, the confirmation cube measured exactly `20.00 x 20.00 x 20.00 mm`.

This result was produced in a controlled September 2026 experiment by William
Tinney with analysis by Codex. It demonstrates the convention, not a universal
material value. A small cube is a fast test; confirm the result on a larger
artifact and a functional tolerance model.

## Why a Value Above 100% Can Be Correct

The field name may say "shrinkage," but OrcaSlicer documents it as the
percentage actually measured after cooling. If a printed feature is larger than
nominal, the measured percentage is above `100%`, and the slicer scales it down.

Always verify the convention used by the exact slicer and version. Other tools
may request a correction percentage rather than a measured percentage.

## Never Fix Material Scale with Axis Steps

Axis steps or rotation distance describe the machine's motion. Changing them to
fix one filament makes every other material and machine coordinate wrong. Use
axis calibration only for a demonstrated motion error, and use filament
shrinkage for material-specific proportional error.

## Holes and Fits

Printed holes are influenced by polygon approximation, extrusion width,
pressure, cooling, seam placement, bridge behavior, and the measurement axis.
Test several diameters and orientations.

For mating parts, tune to the required clearance rather than an abstract perfect
number. Keep separate acceptance classes for sliding, locating, press, and
threaded fits.

## Avoid Double Compensation

Do not manually scale a model when the filament profile already applies
shrinkage unless the model needs an additional intentional change. Likewise,
do not bake a calibration transform into a project and apply the same profile
correction again.

With geometry credible, refine [Seams and Surfaces](08-seams-and-surfaces.md).

