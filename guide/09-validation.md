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

[VAL01](#val01-functional-bracket-and-fit-coupon) is the guide's standard functional
part for this step. Add your own production part as well when you have one.

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
safe to print with and what it is for. The field runs settled on these parts:

```text
Filament: STATUS - Machine - Nozzle - Brand Material - rNN
Process:  STATUS - Machine - Nozzle - Brand Material - Layer Purpose - rNN
```

The status always comes first and the revision last. The parts in between
came in two orders in the field runs: machine first on the Qidi and Snapmaker
printers, material first on the Prusa printers. Either works. Pick one order
for each printer and keep it, so that printer's lists sort the same way every
time. For example:

```text
CANDIDATE - 3D-Fuel Pro PCTG - CORE One+ INDX 8T 0.4 HF - r7
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
  date. If anything changes during promotion, it is a new candidate. In
  Tinman, detach the new preset from the candidate before you retire the
  candidate (see below).
- **One current generation.** Keep one tuned filament per machine, nozzle and
  material, and one tuned process per layer height and purpose. Move older
  generations out of the active lists into a dated folder with a short note of
  what replaced them, so they can be restored.
- **Test values never reach a release.** Calibration tests leave unsaved test
  values in the presets (see
  [Running Tinman's Calibration Tests](25-running-tinman-calibrations.md#how-a-test-is-built));
  save only the one value the test chose.

**Promoting in Tinman: detach the new preset first.** In Tinman (OrcaSlicer
2.5.1 base, November 2026), saving a `CANDIDATE` under its `TUNED` name with
**Save as** can write the new preset as a *child* of the candidate. Its file
then holds `"inherits": "CANDIDATE …"` and stores only the name, ID and notes;
every tuned value still lives in the candidate. Retire the candidate, as the
rule above says, and the tuned preset is orphaned and loses its values. This
happened on the guide's first release.

1. Turn on **Preferences → Developer → Developer mode**. The save dialog
   shows its parent option only in developer mode.
2. Save the `TUNED` preset with the parent box ticked. It is labelled
   **Detach from parent** when the dialog sees a parent, and **Save without
   parent** when it does not. In the field run the first save offered **Save
   without parent**, unticked, and still wrote a child. Saving again under the
   same name with **Detach from parent** ticked fixed it.
3. Open the saved preset's `.json` file in the user `filament` folder and
   check that `inherits` is empty (`""`).
4. Only then retire the `CANDIDATE`, and reload Tinman to confirm the `TUNED`
   preset still shows the tuned values.

This is Tinman's behaviour at the time of writing; a fix may change it.

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

## VAL01: Functional Bracket and Fit Coupon

VAL01 is a functional bracket with a fit coupon. It is the release gate: the
last print before a filament profile goes from `CANDIDATE` to `TUNED`, on every
printer and for every material.
Each calibration print tests one thing. VAL01 tests everything together, on a
part that has to work.

![The VAL01 model: a bracket with a cable channel, a windowed wall, gussets, a boss and clearance holes, and a fit coupon with four pins. Letters mark the pass marks A to H below; the inset shows the underside, where the deck over the channel has no hole. Rendered from models/val01_template.scad (v2), CC BY 4.0.](../assets/val01-model.png)

### When and Why to Run It

Run VAL01 after chapters 01–08 have chosen their values, with the exact
filament and process pair you intend to release. Slice it fresh from the saved
profiles, with no project-only changes, no object overrides and no supports:
the bridges are part of the test.

It was designed during the guide's tuning runs, on a CORE One+ INDX with PCTG
in November 2026. The profile there had passed every calibration test, but
nothing had yet shown that the values worked together on a real part. The
bracket puts the risky features of a typical functional print side by side:

- two 40 mm bridges, one of them under a solid deck that carries a boss (the
  layout that left craters on bridge decks in an earlier cooling test);
- 45° gussets;
- clearance holes for M5 and M3 screws;
- pins with 0.1 to 0.4 mm of clearance in 8 mm holes;
- flat tops with debossed text, seams, and a base that must sit flat;
- a tall wall that must not split.

Run it again as a regression check after a nozzle, hotend, firmware or slicer
change, when the profile is meant to stay `TUNED`.

### The Model

Download [models/val01_template.scad](../models/val01_template.scad)
(OpenSCAD source) or [models/val01.stl](../models/val01.stl) (labelled
"VAL01"). Both are version 2; see the [revision history](#val01-revision-history-why-v1-became-v2)
if you printed VAL01 before 1.2.1. The part is 70 × 85 × 38 mm.

![VAL01 dimensions in millimetres: top view of the bracket and fit coupon, front view of the bracket, and a section through the boss showing the blind bore and, dashed, the withdrawn v1 bore. Original drawing generated from models/val01_template.scad, CC BY 4.0.](../assets/val01-drawing.png)

- **Bracket:** a 70 × 40 × 8 mm base with a cable channel underneath, 40 mm
  wide and 4 mm tall, open at the front. That makes a 40 mm bridge with a 4 mm
  solid deck on top. An upright wall, 6 mm thick and 38 mm tall overall, has a
  40 × 12 mm window, which makes a 40 mm lintel bridge. Two 45° gussets, a
  Ø14 mm boss standing on the bridge deck, two Ø5.5 mm (M5 clearance) holes,
  two Ø3.4 mm (M3 clearance) holes, and a debossed label. The boss has a
  blind Ø5 mm bore, 10 mm deep, whose floor is the deck top, so nothing cuts
  through the bridge.
- **Fit coupon:** a plate with four Ø8.0 mm holes, and four 12 mm pins of
  Ø7.9, 7.8, 7.7 and 7.6 mm. Each pin carries 1 to 4 dimples on top: one
  dimple is the tightest (Ø7.9), four the loosest (Ø7.6).

**Known limitation: the dimples are hard to read.** On the PCTG runs (0.4 mm
nozzle) the dimples printed as short dashes, and the single dimple on the
Ø7.9 pin was barely visible on its small, rough top. The pins also stand in order: seen
from the coupon side, they run from 1 dimple (Ø7.9) on the left to 4 dimples
(Ø7.6) on the right, each in line with a hole. Note that order before you take
them off the plate. The marking does not affect the geometry under test.

Change only the label (`label` at the top of the `.scad` file), to the
material and revision under test, and export your own STL. Print at the profile's own layer height, on
the plate it will be used with.

### Pass Marks

Let the part cool for at least 30 minutes. Measure as for the dimensional
tests: at mid-side, on the upper half of walls, away from seams.

| # | Check | Pass if |
| --- | --- | --- |
| A | Bracket outside dimensions | base length 70.00 ± 0.15 mm; depth 40.00 ± 0.10 mm; wall thickness 6.00 ± 0.10 mm; boss Ø14.00 ± 0.15 mm; overall height 38.00 ± 0.10 mm |
| B | Clearance holes | an M5 screw (or a 5 mm drill shank) passes both Ø5.5 holes freely; an M3 screw passes both Ø3.4 holes freely. Without screws, measure the holes instead: each must be at least the screw size plus 0.2 mm (M5: 5.2 mm or more; M3: 3.2 mm or more). Record the boss bore (Ø5.0 nominal). |
| C | Fit coupon | at least the 3-dimple pin (Ø7.7, 0.3 mm clearance) slides fully through its hole by hand without force. Record the tightest pin that slides. |
| D | Bridges | channel underside: continuous strands, none dropped, sag at mid-span no more than about 0.5 mm (measured as below). Deck top, text and boss: no crater, hole or lifted strand. Lintel underside continuous. |
| E | Overhangs | the 45° gusset faces are clean, with no curl or droop |
| F | Surfaces | tops closed with no open channels; no rows of beads along top edges; the label legible; seams narrow; at most fine hairs of stringing |
| G | First layer and warp | sits flat on a flat surface without rocking; no corner lift over 0.2 mm; no bottom flare that stops a straight edge sitting flat |
| H | Layer adhesion | the wall survives a firm thumb push at its top, toward the front, with no crack or delamination. If you break a pin, it bends before it breaks. |

**Measuring sag (D).** Measure the height of each opening at both ends and
at mid-span: the channel (4.0 mm nominal) and the window (12.0 mm nominal).
The sag is how far the mid-span height falls below the average of the two
end heights. Measuring mid-span alone against the nominal height assumes the
ends printed exactly to size.

These limits were written for a 0.4 mm nozzle and 0.20 mm layers, and first
used with PCTG. If a material or setup needs a different limit (a flexible or
high-shrink material, a larger nozzle, thicker layers), write the new limit and
the reason in the experiment log **before** printing.

The tightest pin that slides (criterion C) is worth keeping: it is the
sliding-fit allowance for this material, nozzle and profile, and it is the
number to use when you design parts.

**Expected before the first print.** In the first run's dimension tests, 8 mm holes
came out about 0.05 mm small and small round parts slightly large. From that,
the 1-dimple pin probably won't fit, the 2-dimple pin may be snug, the 3-dimple
pin should slide and the 4-dimple pin will be loose. This was an inference
written before the first print; the measured result is under
"First result" below.

### If a Check Fails

Go back to the chapter that owns the defect, change one variable, and print
VAL01 again.

| Failed | Go back to |
| --- | --- |
| A | [Dimensional accuracy](07-dimensional-accuracy.md): shrinkage or contour compensation |
| B, C | [Dimensional accuracy](07-dimensional-accuracy.md#holes-and-fits): holes, polyholes, design allowance |
| D | [Bridges](06-cooling-and-retraction.md#bridge-controls); for craters on the deck, try **Extra bridge layers** |
| E | [Cooling](06-cooling-and-retraction.md#cooling-test-method): overhang fan |
| F | [Flow ratio](05-flow-ratio.md), [top surfaces](08-seams-and-surfaces.md#top-and-bottom-surfaces), [retraction](06-cooling-and-retraction.md#retraction-test) |
| G | [Foundations](01-foundations.md): first layer and plate; warping materials in [material families](10-material-families.md) |
| H | [Temperature and the bond check](02-conditioning-and-temperature.md#a-simple-bond-check); normal fan in [cooling](06-cooling-and-retraction.md) |

A profile becomes `TUNED` only when every check passes, plus whatever sign-off
your own process requires. Record the result, the measurements and the
tightest sliding pin in the profile's notes.

**First result: PCTG passed VAL01 and was released as `TUNED` r7.** VAL01 was
printed twice on 2026-11-21 on a CORE One+ INDX with 3D-Fuel Pro PCTG and the
same profile pair: run 1 from the v1 model, run 2 from v2. Run 1's bridge
failed because of the model (see the
[revision history](#val01-revision-history-why-v1-became-v2)). Run 2 passed
every check, graded from measurements of the part, photographs and the sliced
G-code. With the owner's approval the profile was released the same day as
`TUNED - 3D-Fuel Pro PCTG - CORE One+ INDX 8T 0.4 HF - r7`, with every value
unchanged from the tested r7, and the `CANDIDATE` was retired. A fresh slice of
VAL01 with the released profile gave G-code identical to the passing run, all
88,933 lines apart from comments. It was the first release through VAL01.

The pass covers this scope only: one toolhead with a 0.4 mm high-flow nozzle,
0.20 mm layers (a balanced process with Monotonic top surfaces), a
high-temperature plate at 85 °C, and the enclosure vent closed with the
chamber warmed to 40 °C.

| # | Run 2 (v2), measured or seen | Result |
| --- | --- | --- |
| A | base 70.12 mm (+0.12), depth 40.00, wall 6.01, boss Ø13.88 (−0.12), height 37.93 (−0.07) | pass |
| B | the Ø5.5 hole measured 5.41 mm and the Ø3.4 hole 3.24 mm, so both clear their screws by more than 0.2 mm; graded by measurement, without a screw test | pass |
| C | the 2-, 3- and 4-dimple pins slide by hand; the 1-dimple pin (Ø7.9) does not; tightest sliding pin Ø7.8 | pass |
| D | channel strands continuous, channel height 3.8 mm at mid-span against 4.0 nominal (about 0.2 mm sag); deck top with no crater, hole or lifted strand; window 11.68 mm at mid-span against 12.0 (about 0.3 mm) | pass |
| E | gusset faces clean (photographs) | pass |
| F | tops closed, label crisp, one fine hair at a wall corner (photographs) | pass |
| G | no rocking on a flat surface | pass |
| H | no crack on the thumb push | pass |

- **Sliding fit:** the tightest pin that slides is Ø7.8 in a Ø8.0 hole. So
  PCTG's sliding-fit allowance with this profile is 0.2 mm on the diameter,
  one step tighter than the 0.3 mm expected above. This was checked by hand,
  not inferred.
- **Sag:** only the mid-span heights were measured, so both sag figures assume
  the ends of each opening came out at their nominal height. *Inference:* the
  overall height came out 0.07 mm under, so the error from that assumption is
  small. Measure both ends next time (see the pass marks).
- **Holes:** the small holes came out 0.09 mm (Ø5.5) and 0.16 mm (Ø3.4)
  under size, the small-hole effect described in
  [Dimensional Accuracy](07-dimensional-accuracy.md#holes-and-fits). They
  still clear their screws. Allow for it when you design small holes.
- **Deck top:** no crater on either run. Both times the G-code printed the
  solid infill over the channel bridge at about 233 mm/s, the condition
  suspected of leaving craters in the earlier cooling test. If craters appear
  on a production part, try **Extra bridge layers** next.
- **Rings on the pins:** on both runs each pin shows two faint rings, about
  5 mm and 8 mm up. The G-code changes the conditions at exactly those
  heights. At Z 5 the coupon plate ends and the part fan steps up from 10 % to
  14 %. At Z 8 the bracket base ends, the layer time drops to about 8 s, and
  the pin walls slow from 200 to 120 mm/s. The filament fed per pin layer stays
  the same.
  - *Inference:* these are gloss changes at feature transitions (see the
    [surface artifact map](08-seams-and-surfaces.md#surface-artifact-map)),
    not over-extrusion.
  - They did not stop the pins sliding.
- **Cosmetic only:** the front strand at the channel mouth is slightly wavy,
  and one thin string hangs in the channel.
- **Not covered by this pass:** other layer heights, the other toolheads,
  multi-tool jobs, and prints much longer than this one (about 70 minutes).

### VAL01 Revision History: Why v1 Became v2

- **v1 (2026-11-21, withdrawn).** The boss's Ø5 mm bore ran down through the
  4 mm deck into the cable channel. On the first bridge layer, the slicer had
  to print the bore's edge as a loop of wall with nothing under it: the run-1
  G-code has 66 "Overhang wall" segments within 6 mm of the bore. The bridge
  strands were cut by the hole and anchored on that loose loop.
  - *Observed:* on run 1 the strands tangled around the bore and were
    continuous everywhere else.
  - *Inferred, from the G-code:* the loop in mid-air caused the tangle. A
    hole through a bridged span would fail with almost any filament, so v1
    tested the model, not the profile.
- **v2 (2026-11-21, current).** The bore is blind: it starts on the deck top
  (Z 8) and is 10 mm deep, so the deck is one unbroken 40 mm bridge. That is
  the condition criterion D is meant to check. Nothing else changed: the
  outside size, holes, pins, label and pass marks A–H are the same, and the
  files keep their names.
  - *Observed on run 2:* the bridge held, with no tangle under the bore. The
    run-2 G-code has no wall moves around the bore on the bridge layer, and
    the strands run straight across. That supports the inference above.
- If you printed v1, print v2 before you grade the bridges (D).

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
