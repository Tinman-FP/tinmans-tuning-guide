# How to Use This Guide

Filament tuning is controlled experimentation. The goal is not to make one
calibration model look perfect. The goal is to produce a profile that behaves
predictably on real parts and can be explained, repeated, and maintained.

## The Three Layers of a Profile

Keep these categories separate:

| Category | Examples | Store the result in |
| --- | --- | --- |
| Machine | steps or rotation distance, bed mesh, tool offsets, input shaping | printer or firmware profile |
| Filament | temperature, flow ratio, PA, cooling, MVS, shrinkage | filament/material profile |
| Process | layer height, line width, walls, infill, support, speed strategy | process/print profile |

A symptom can cross categories, but a correction should live where its cause
lives. A single spool should not redefine the machine's X-axis calibration.

## Define the Question Before Printing

A useful test begins with one sentence:

> With every listed condition fixed, does changing **X** from **A** to **B**
> improve **Y**, measured by **Z**?

Example:

> With temperature, global flow, pressure advance, speed, and geometry fixed,
> does increasing top-surface flow from 1.00 to 1.04 close the visible channels
> without creating ridges or wall buildup?

If the test cannot be stated this way, it probably changes too many variables.

## Broad Search, Then Fine Search

Use a broad test to find the useful region, then narrow the increments:

1. Search a safe range with large steps.
2. Reject clearly bad regions.
3. Repeat around the best region with smaller steps.
4. Confirm the selected value on a separate print.

This is faster and more reliable than making many tiny changes from an unknown
starting point.

## Keep a Control

Preserve either the previous accepted specimen or an unchanged control in the
same print. A control reveals whether room temperature, filament moisture,
hardware state, or a slicer update changed between sessions.

For visual tests:

- use the same material color and lighting;
- photograph the same faces in the same orientation;
- label samples physically;
- avoid judging glossy material from a single flash angle.

## Freeze the Test Conditions

Unless the selected variable requires a change, hold these constant:

- printer, tool, nozzle, and nozzle wear state;
- build plate, cleaning procedure, and adhesive;
- filament spool, drying cycle, and feed path;
- chamber, door, lid, ambient temperature, and draft exposure;
- layer height, line width, wall count, infill, and model orientation;
- temperature, speed, acceleration, cooling, and retraction;
- bed mesh, Z offset, and tool offsets;
- slicer version and profile inheritance.

## Record Evidence, Not Memory

Save the complete project and final G-code when possible. A screenshot of a
settings panel is not enough because inherited or hidden settings can alter the
slice.

Use four result states:

- `candidate`: promising but not independently confirmed;
- `accepted`: repeatable and promoted to the profile;
- `rejected`: tested and unsuitable under the recorded conditions;
- `superseded`: once accepted, later replaced with evidence.

The [experiment log](../templates/experiment-log.md) captures the minimum useful
record.

<!-- pdf:page-break-before -->

## Measure Carefully

- Let the part fully cool before measuring.
- Use a suitable instrument and confirm its zero.
- Measure several locations, not the seam, corners, or elephant foot.
- Repeat the measurement and report resolution honestly.
- Use a larger artifact when a small dimensional error approaches the tool's
  uncertainty.
- Test both external and internal features before claiming a tolerance.

A `0.02 mm` difference measured once with ordinary calipers is not necessarily
real. A repeatable `0.13 mm` difference on multiple axes deserves attention.

## Separate Observation from Interpretation

Write both:

```text
Observation: parallel open channels remain between top lines.
Interpretation: top-surface deposition may be low; global under-extrusion is
less likely because the walls are continuous and dimensions are correct.
```

This preserves useful evidence even when the first interpretation is wrong.

## Know When to Stop

Stop tuning when the profile meets the defined requirements with margin. A
functional enclosure and a display model can need different profiles for the
same spool. Chasing an invisible difference can reduce strength, speed, or
reliability.

Move to [Foundations](01-foundations.md) before changing filament values.
