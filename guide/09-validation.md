# Validation and Profile Release

> **At a glance**
> - **Decide:** whether the profile is finished
> - **Test:** a real part sliced fresh from the saved profile, checked against the pass marks
> - **Keep:** the candidate renamed `TUNED`, with a revision number and notes

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

Use more than one dimensional artifact when the symptom crosses categories. A
Benchy is a strong geometry-and-surface diagnostic but is not a substitute for
a multi-size dimensional stack, a multi-point XY/skew grid, or raw dial-gauge
motion verification. Preserve signed X and Y readings rather than reporting
only absolute error; opposite signs require an axis-specific investigation
before any global compensation is accepted.

### 3. Geometry artifact

For a Benchy, record the [official feature checks and nominal dimensions](24-benchy-inspection-and-measurement.md),
with local acceptance limits clearly separated from the source specifications.

Checks bridges, overhangs, small towers, text, curves, corners, and travel
stringing.

### 4. Representative production part

Uses the actual layer height, wall strategy, infill, support, speed, chamber,
and build plate expected in service.

### 5. Mechanical specimen when needed

Validates layer adhesion or functional strength at the production temperature,
flow rate, cooling, orientation, and environmental conditioning.

## Acceptance Criteria

Define limits **before the first tuning print**, not at the end (see
[Step 0](00-how-to-use-this-guide.md#step-0-decide-what-good-enough-means)).
Revisit them here. Examples:

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

- selected physical tool and nozzle, not only the preset label;
- bed mesh and offset behavior;
- temperature transitions;
- fan commands and chamber behavior;
- PA or Linear Advance commands;
- flow and feature-specific overrides;
- actual volumetric-flow range;
- layer heights and line widths consistent with the installed nozzle;
- model scaling and compensation;
- unexpected auxiliary, fiber, or tool-change commands;
- unintended calibration-mode commands.

Where the machine exposes live state, compare the important emitted commands
with the effective firmware values after printing begins. The last writer wins;
an earlier start-G-code command can be replaced by a later slicer command.

For a networked multi-tool printer, extend this review to the complete job
lifecycle. Confirm the uploaded file path, perform a real home before launch,
and audit not only the start tool but every load, purge, cutter, tool-change,
and unload command through the end block. Then verify the remote printer's
active filename, selected tool, temperatures, PA, and job progress after it
starts. A control request timing out does not establish its outcome; live state
is the authoritative record.

## Name, Version and Promote

A profile name should tell you, at a glance in a drop-down list, whether it is
safe to print with and what it is for. The field runs settled on this pattern:

```text
Filament: STATUS - Machine - Nozzle - Brand Material - rNN
Process:  STATUS - Machine - Nozzle - Brand Material - Layer Purpose - rNN
```

For example:

```text
CANDIDATE - CORE One+ INDX 8T 0.4 HF - 3D-Fuel Pro PCTG - r7
TUNED - Qidi Plus4 - 0.6mm - Elegoo PET-CF - r14
TUNED - Qidi Plus4 - 0.6mm - Elegoo PET-CF - 0.24mm Production - r25
```

Use ` - ` (space, hyphen, space) between parts. Avoid `|`, `/`, `\`, `:`,
`*`, `?`, `"`, `<`, `>`, `[` and `]`: profiles are saved as files, and Windows
does not allow these characters in file names. Tinman on macOS accepts `|`,
but a profile named that way cannot be shared with a Windows machine.

Rules that kept the field runs honest:

- **Status.** `CANDIDATE` while any stage is open. `TUNED` only after the
  required stages and a representative part pass for that exact machine,
  nozzle and material. `RETIRED - DO NOT USE` for anything superseded that must
  stay visible.
- **A new revision for each accepted change.** When a test changes an accepted
  value, save a new revision (`r09 -> r10`) and note which value changed and
  why. When a test confirms the current values, **do not** make a new revision:
  one K2 run finished four confirming tests with no change and stayed at r10.
- **Filament and process counters are independent.** The recommended release is
  a pair, such as filament r14 with process r25, not "both at r14".
- **Promote the tested file unchanged.** `TUNED` is the last `CANDIDATE`
  renamed, with its values byte-for-byte the same and a note of the release
  date. If anything changes during promotion, it is a new candidate.
- **One current generation.** Keep one tuned filament per machine, nozzle and
  material, and one tuned process per layer height and purpose. Move older
  generations out of the active lists into a dated folder with a short note of
  what replaced them, so they can be restored.
- **Test values never reach a release.** Calibration tests leave unsaved test
  values in the presets (see
  [Running Tinman's Calibration Tests](25-running-tinman-calibrations.md#how-a-test-is-built));
  save only the one value the test chose.

Record with every revision:

- the parent printer and process profiles;
- slicer and firmware versions;
- accepted values and their experiment records;
- known limits and provisional values (for example "MVS not reached",
  "0.4 mm values inherited from 0.6 mm, not retested");
- date, author, and reason for change.

Keep tuned filament profiles machine-specific and restrict their compatibility
to the matching printer. Tinman can also scope a profile to one physical printer
and nozzle when you save it (**Printer scope**), so a profile tuned on one
machine does not appear for another. Preserve the generic or supplier profile
as an untouched reference.

A visually improved coupon is still a candidate. Promote it only after a clean
project reproduces the slice and a representative functional part passes its
dimensional, fit, surface, and strength requirements.

## Tuning Prints and Validation Prints

![The same PET-CF part after three support settings on its validation print: r05 concentric interface (swirls), r06 ironed solid interface (fused), r07 spaced interface with 100 % interface fan (clean). Field photographs from the guide's tuning runs, 2026-11-19 and 2026-11-20; cropped and labeled.](../assets/field-tests/qidi-pet-cf-support-interface-r05-r07.jpg)

Tuning prints are printed **without supports**, so that supports do not hide or
cause the defect being tuned. Validation prints are printed the way production
will print them, **with supports** where the part needs them. Support settings
are then tuned on the validation part, not on coupons. A PET-CF run's
support-interface lessons are in [Worked Examples](26-worked-examples.md).

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
