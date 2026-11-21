# Running Tinman's Calibration Tests

The earlier chapters explain *what* each test measures and *how to judge* it.
This chapter explains how to run the tests in Tinman's **Calibration** menu
without the traps that cost the guide's field runs whole prints: the test
changing the wrong filament, objects printing from the wrong slot, a ramp that
silently goes flat, and test values leaking into a saved profile.

Tinman's calibration tests are OrcaSlicer 2.5.1's, with a short list of
Tinman fixes (listed at the end). Everything here also applies to OrcaSlicer
2.5.1 unless a line says "Tinman only".

## The Calibration Menu

| Menu item | Measures | Chapter |
| --- | --- | --- |
| **Temperature** | nozzle temperature | [Conditioning and temperature](02-conditioning-and-temperature.md) |
| **Max flowrate** | maximum volumetric speed (MVS) | [Volumetric flow](03-volumetric-flow.md) |
| **Pressure advance** | pressure advance (PA): Tower, Line or Pattern | [Pressure advance](04-pressure-advance.md) |
| **Flow ratio** | flow ratio: Pass 1, Pass 2, YOLO, YOLO (Perfectionist) | [Flow ratio](05-flow-ratio.md) |
| **Retraction** | retraction length | [Cooling and retraction](06-cooling-and-retraction.md#retraction-test) |
| **Cornering** | jerk or junction deviation | [Motion diagnostics](19-motion-diagnostics.md) |
| **Input Shaping** | shaper frequency and damping | [Motion diagnostics](19-motion-diagnostics.md) |
| **VFA** | speed-dependent wall texture | [Motion diagnostics](19-motion-diagnostics.md#use-a-vfa-sweep-for-speed-dependent-texture) |
| **Calibration Guide** | opens this guide | - |

The items work only in the **Prepare** view. Each dialog's round help button
opens the matching chapter of this guide.

There is no built-in cooling, bridge, dimensional or strength test. The
guide's chapters on those steps describe simple models you can print instead.

<!-- pdf:page-break-before -->

## How a Test Is Built

Knowing what the generator does explains every trap below. When you start a
test, Tinman:

1. starts a new project containing only the test model;
2. writes some test settings onto the model itself (stored in the project);
3. changes the **process, filament and printer presets that are open for
   editing**, without saving them. They show a `*` as modified;
4. for the tower tests (Temperature, Max flowrate, PA Tower, Retraction, VFA,
   Cornering, Input Shaping), keeps the ramp (the start, end and step you typed)
   in memory for the slice. That ramp is **not** saved in the project file.
   PA Pattern and Flow ratio are different: their values are stored on the
   plate and the coupons, and survive a save.

Four consequences follow:

- **The test changes the filament that is open for editing**, which is the one
  you last opened with a slot's edit (pencil) button. It is not necessarily
  the filament that will print the test.
- **The test objects start on filament 1.** Nothing moves them to the slot you
  want to test.
- **Test values sit in your presets as unsaved edits.** For example, after
  **Max flowrate** the edited filament shows an MVS of at least `200`, and after
  **Temperature** its nozzle temperature equals the tower's start temperature.
  Saving the preset at that moment writes those test values into your profile.
- **A reopened tower project has lost its ramp.** It slices as a plain model
  at one value. Generate the test again from the menu instead.

## The Safe Recipe

Use this sequence for every test. It takes a minute and prevents the most
common wasted prints.

1. **Start from a clean state.** Select the printer, nozzle, process and the
   filament profile you are tuning. Save or close any project you care about.
2. **Open the filament you are testing.** Click the edit (pencil) button on the
   filament slot that will print the test, look at it, and close it. That
   filament is now the one the test changes.
3. **Check the filament's own limits.** Its **Max volumetric speed** must be
   above the top of a Max flowrate ramp, and its flow ratio must be the value
   you mean to test around.
4. **Run the test** from the **Calibration** menu. Fill in the dialog.
5. **Answer the new-project question.** If Tinman asks what to do with modified
   presets, choose to transfer them into the test project. Do not press Cancel
   expecting the test to stop: in the current build, Cancel still builds the
   test into the open project (Flow ratio is the exception).
6. **Move the objects to the right slot.** Select all test objects and press the
   slot's number key (for example `2`). Check the filament column in the
   Objects list. **PA Pattern is the exception:** it sizes its lines from the
   *first* filament slot, so put the filament under test in slot 1 for that
   test.
7. **Slice and inspect before printing.** In the preview, confirm the values
   change through the part: temperature bands, the speed ramp, PA steps or
   retraction bands. On a multi-tool printer, confirm the G-code uses only the
   intended tool.
8. **Print, then grade the cooled part** using the chapter for that test.
9. **Enter only the chosen value** in the filament profile. Discard the other
   test edits, then save the profile as a new revision (see
   [naming and versioning](09-validation.md#name-version-and-promote)).

> **Field example.** On a Creality K2 Plus a Max flowrate ramp requested
> `20 -> 45 mm³/s` but printed flat at `32 mm³/s` above mid-height. The test had
> raised the MVS of a different, edited filament; the printing filament's own
> MVS of `32` still capped the speed. After step 2 of the recipe, the same test
> printed `20.7 -> 46.1 mm³/s`. On a Prusa CORE One+ INDX, a PA tower's layer-time
> and wall-speed changes landed on a PLA profile in other slots, so the PCTG
> tower printed at about a quarter of its intended speed.

<!-- pdf:page-break-before -->

## Test by Test

### Temperature

- **Dialog:** filament type (PLA, ABS/ASA, PETG, PCTG, TPU, PA-CF, PET-CF,
  Custom), start and end temperature, and **Auto-scale for nozzle**. The step
  is fixed at `5 C`.
- **Default ranges by type:** PLA `230 -> 190`, ABS/ASA `270 -> 230`, PETG
  `250 -> 230`, PCTG `280 -> 240`, TPU `240 -> 210`, PA-CF and PET-CF
  `320 -> 280`. Replace them with the filament maker's range, extended one or
  two steps each way where that is safe.
- **The model:** a stack of blocks, one per `5 C`, **hottest at the bottom**.
  Each block is `10 mm` tall for a `0.4 mm` nozzle. With **Auto-scale for
  nozzle** on, the tower scales with the nozzle (`15 mm` blocks for `0.6 mm`)
  and prints at a layer height of half the nozzle diameter. Every block carries
  its temperature as a number, an overhang, a bridge window, a hole with a cone
  for stringing, and a curved surface.
- **Reading it:** count blocks from the bottom. The temperature of block `n` is
  `start - 5 * (n - 1)`. The first few layers of the bottom block print while
  the nozzle is still settling, so judge each block above its transition.

### Max flowrate

- **Dialog:** start, end and step in `mm³/s` (default `5 -> 20`, step `0.5`).
- **The model:** a single-wall spiral (vase) print, `1.75 x` the nozzle wide
  and `0.8 x` the nozzle high per layer, cut to the height the range needs.
- **Reading it:** the requested flow at height `h` (in mm) is
  `start + step * h`. Measure the height of the first sustained defect, convert
  it with that formula, and set the profile MVS to `0.90-0.95` of that flow.
- **Watch for:** a flat ramp (see the field example above). Use the preview's
  speed or flow legend to confirm the ramp before printing.

### Pressure advance

- **Dialog:** extruder type (**DDE** for direct drive, **Bowden**), method
  (**PA Tower**, **PA Line**, **PA Pattern**), start, end and step, **Print
  numbers**, and for PA Pattern only, comma-separated **Accelerations** and
  **Speeds**.
- **Defaults (direct drive):** Tower and Line `0 -> 0.1`, step `0.002`; Pattern
  `0 -> 0.08`, step `0.005`. Bowden defaults run `0 -> 1.0` (step `0.02` for
  Tower and Line, `0.05` for Pattern), because a long tube needs far more PA.
- **PA Tower:** a hollow two-wall tower cut to about one millimetre per PA
  step. Tinman divides the sliced layers evenly among the PA values, so PA at a
  height `h` is about `start + step * h`, counting from the top of the first
  layer. The exact value of each band is in the PA command at that layer
  (`SET_PRESSURE_ADVANCE`, `M900 K` or `M572 S`); confirm a borderline reading
  there.
- **PA Line:** rows of slow-fast-slow lines on the first layers, labelled if
  **Print numbers** is ticked. Quick, but it is only as good as the first
  layer.
- **PA Pattern:** a set of chevrons per speed and acceleration pair, with every
  other PA value printed beside them, followed by the pattern's volumetric
  flow (in `mm³/s`) and acceleration. Enter your real production speeds and
  accelerations. The dialog requires the smallest acceleration to be larger than
  the largest speed. Leave the lists empty and Tinman picks one speed and the
  outer-wall acceleration for you, and says so. Each layer of the pattern ends
  by setting PA back to the test's start value.
- **Placement:** the patterns are placed in object order, not sorted by speed
  or acceleration. Read the flow and acceleration printed beside each pattern
  (a higher flow means a faster speed) instead of assuming a layout.

### Flow ratio

The dialog offers four test types and a top-surface pattern (Archimedean
Chords by default, or Monotonic). The arithmetic differs between them, so
note which one you printed.

| Test type | Coupon labels | Each coupon's flow ratio | New value |
| --- | --- | --- | --- |
| **Pass 1 (Coarse)** | `-20` to `+20` in steps of `5` (percent) | current x (100 + label) / 100 | current x (100 + best label) / 100 |
| **Pass 2 (Fine)** | `0` to `-9` in steps of `1` (percent) | same, from the Pass 1 result | current x (100 + best label) / 100 |
| **YOLO (Recommended)** | `-0.05` to `+0.05` in steps of `0.01` | current + label | **current + best label** |
| **YOLO (Perfectionist)** | `-0.040` to `+0.035` in steps of `0.005` | current + label | **current + best label** |

Examples: with a current flow ratio of `0.98`, a YOLO coupon labelled `+0.02`
printed at `1.00`, and that coupon chosen gives `1.00`. A Pass 1 coupon
labelled `+5` printed at `0.98 x 1.05 = 1.029`.

YOLO labels are **added**, not multiplied. A K2 Plus run first recorded a
YOLO choice as `x 0.975`; the next test showed the coupons had printed at
`current + label`, and the profile value was corrected. The dialog itself
does not say which arithmetic applies.

For the YOLO tests, "current" is read from the filament **open for editing**
(recipe step 2), and the coupons only print at the intended flow if they also
print from that slot (recipe step 6). Pass 1 and Pass 2 coupons simply scale
the flow ratio of whichever filament prints them.

### Retraction

- **Dialog:** start and end length in mm (default `0 -> 2`) and step (default
  `0.1`).
- **The model:** two pillars on a base. The base is `0.4 mm` high and belongs to
  the first band; every step above it is a `1 mm` band. Length at band `n`
  (counting from 0 at the bottom) is `start + step * n`.
- **Build note:** in OrcaSlicer 2.5.1 and in Tinman builds before 2026-11-21
  (PR 53), bands alternated between four and six layers because of a rounding
  error, so heights no longer mapped cleanly to lengths. Current Tinman bands
  are exactly `1 mm`. In any build, the G-code comments name the length of
  every band.
- **Limits of the test:** a fast printer may show no strings at any length,
  including `0`. That does not prove `0` is right; see
  [the retraction step](06-cooling-and-retraction.md#retraction-test).

### Cornering, Input Shaping and VFA

These are machine tests, not filament tests. Run them when the machine changes,
and keep their results in the printer profile or firmware. See
[Motion Diagnostics](19-motion-diagnostics.md). Tinman adds checks to the VFA
dialog: if the end speed would exceed the filament's MVS, it offers a smaller
layer height or a lower end speed. Do not raise a validated MVS just to pass
this check.

<!-- pdf:page-break-before -->

## What Each Test Changes

Every change below is an unsaved edit or a setting on the test object. None of
it reaches a saved profile unless you save the preset while it is showing `*`.

| Test | Edited filament | Edited process | Edited printer | Test object |
| --- | --- | --- | --- | --- |
| Temperature | nozzle temperatures set to the start value | minor | resonance avoidance off | layer height, brim, seam |
| Max flowrate | MVS at least `200`, layer-time slowdown off | spiral mode | resonance avoidance off, max layer height | one wall, wide line, tall layer |
| PA Tower | layer-time slowdown `1 s` | wall speeds set from the MVS | resonance avoidance off | two walls, rear seam, brim |
| PA Pattern | no retract or wipe on layer change | speeds, accelerations, widths, skirt and brim | no wipe | speed and acceleration per pattern |
| Flow ratio | none (reads the flow ratio, caps speeds at the MVS) | layer height half the nozzle | resonance avoidance off | per-coupon flow and surface settings |
| Retraction | none | minor | firmware retraction off | layer height, walls, no infill |

## Known Issues in Current Builds

Checked against Tinman `main` on 2026-11-21:

- A test changes the last-opened filament, and its objects start on filament
  1. Use the recipe.
- Cancel at the "save first?" prompt still builds the test into the open
  project, for every test except Flow ratio.
- A reopened tower-type calibration project slices without its ramp.
- PA Pattern sizes its lines from filament slot 1, whichever slot prints it.
- Discarding changes in the "Transfer or discard changes" dialog has reset the
  process to the default once in testing. Check the process name before you
  slice.
- Starting a job from some printers' touchscreens instead of from Tinman can
  run the printer's own pre-print calibration, which may replace the PA and
  flow the slicer sent. On a K2 Plus this replaced PA and flow for the first
  layer of a flow test. Start calibration prints from Tinman, with the printer's
  own auto-calibration off, and check the first layer's commands if in doubt.

## Tinman Changes to the Upstream Tests

- Help buttons and **Calibration Guide** open this guide.
- The Temperature, PA Tower, VFA, Cornering and Input Shaping towers use
  shared step arithmetic: a range that is not a whole number of steps no
  longer runs one step past its end value. (Max flowrate still ramps
  continuously with height.)
- Retraction-tower bands are exactly `1 mm` (PR 53, 2026-11-21).
- PA Pattern preview tags follow the selected printer, which fixes a halved
  time estimate on the first slice for non-Bambu printers (PR 53).
- The PA Line footprint is calculated from the pattern actually printed.
- VFA input checks and layer-height planning (see above).

Sources: Tinman `main` at `baf3f00dfe` (calibration dialogs, generators and
G-code output), Tinman pull requests 20 and 53, and the field reports
summarized in [Worked Examples](26-worked-examples.md).
