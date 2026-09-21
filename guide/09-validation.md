# Validation and Profile Release

A calibration value is not finished when its test looks good. A profile is
finished when the complete settings work together on representative parts and
the evidence can be reproduced.

## Minimum Validation Set

### 1. Broad surface coupon

Checks global and top-surface flow, line continuity, wall contact, and visible
surface defects.

### 2. Dimensional artifact

Checks X, Y, and Z scale, external contours, several hole sizes, elephant foot,
and at least one functional clearance.

### 3. Geometry artifact

Checks bridges, overhangs, small towers, text, curves, corners, and travel
stringing.

### 4. Representative production part

Uses the actual layer height, wall strategy, infill, support, speed, chamber,
and build plate expected in service.

### 5. Mechanical specimen when needed

Validates layer adhesion or functional strength at the production temperature,
flow rate, cooling, orientation, and environmental conditioning.

## Acceptance Criteria

Define limits before printing. Examples:

```text
No missing or discontinuous perimeter lines.
No open top-surface channels visible under diffuse light.
External dimensions within +/- 0.10 mm over 50 mm.
Specified pin passes the sliding-fit hole without force.
No corner lift greater than 0.20 mm.
No layer separation in the defined bend comparison.
```

Avoid criteria such as "looks good" without a reference or failure threshold.

## Confirm the Operating Envelope

Validate the profile at the edges that production will use:

- lowest and highest normal layer heights;
- slow external walls and fastest infill;
- short and long layers;
- small and large bed footprints;
- longest expected print duration;
- enclosure and ambient extremes;
- tool changes or material changes when applicable.

A single cube cannot validate all of these.

## Review the G-Code

Before a final release, inspect the sliced result for:

- selected tool and nozzle;
- bed mesh and offset behavior;
- temperature transitions;
- fan commands and chamber behavior;
- PA or Linear Advance commands;
- flow and feature-specific overrides;
- actual volumetric-flow range;
- model scaling and compensation;
- unintended calibration-mode commands.

## Version the Profile

Record:

- profile name and semantic or dated revision;
- parent printer and process profiles;
- slicer and firmware versions;
- accepted values and their experiment records;
- known limits and provisional values;
- date, author, and reason for change.

Never overwrite the only known-good profile during experimentation. Duplicate
it, mark the new copy `candidate`, and promote it after validation.

## Regression Triggers

Run at least a short confirmation after:

- changing nozzle, hotend, extruder, or cooling duct;
- updating firmware or slicer behavior;
- switching material color, formulation, or lot;
- changing temperature, MVS, or PA materially;
- changing enclosure or chamber operation;
- observing a sudden quality change from a previously stable profile.

## Release Decision

Use the [profile release checklist](../templates/profile-release-checklist.md).
A released profile should state what it is optimized for: visual quality,
balanced use, speed, strength, dimensional work, or a specific process. One
profile does not need to win every tradeoff.

