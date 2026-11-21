# Worked Examples from Real Tuning Runs

> **At a glance**
> - **Decide:** nothing new: this chapter shows complete runs
> - **Test:** four real tuning runs, wrong turns included
> - **Keep:** the lessons, not the numbers

These are four complete tuning runs from November 2026, on four different
printers, using Tinman and this guide. They are told as they happened,
including the wrong turns, because the wrong turns teach the most. The values
belong to those machines; use them as a picture of a finished tune, not as
starting numbers.

Each run printed one test at a time. The printer's owner cleared every print,
graded the parts from photographs and caliper readings, and approved every
change to a profile.

## Creality K2 Plus, 3D-Fuel Pro PCTG, 0.6 mm

**Setup:** K2 Plus with its multi-spool feeder, 0.6 mm hardened nozzle,
0.24 mm layers, bed 85 °C, chamber 45 °C. Maker's range 250–280 °C.

### The first attempt

The early tests ran out of order and on shifting ground:

- The temperature tower was graded from photographs only and picked 245 °C,
  the coolest band tested: an end band, and below the maker's range.
- The spool's first half was yellow and its second half orange. Temperature
  and MVS were set on the yellow half; PA, flow, retraction and four cooling
  tests ran on the orange half.
- Four cooling and bridge tests (fan, chamber heater, bridge flow) followed,
  before temperature and MVS were confirmed. Bridges kept sagging; a small pin
  meant to show bonding broke differently in identical prints.
- Nobody had written down what "good enough" meant.

After the fourth cooling test the owner called a halt: the tests weren't
showing progress, so it was time to go back to basics.

### The restart

| Step | Test | Result | Kept |
| --- | --- | --- | --- |
| 0 | Pass marks written down (bonding, stringing, bridges) | - | - |
| 1 | New roll dried about 65 °C for 6–8 h; feeder desiccant replaced; nozzle cleaned | - | - |
| 2 | **Temperature** 280 → 240 °C | stringing and bridge sag rise steadily with temperature; pins strong in every band | 245 °C |
| 3 | **Max flowrate** 20 → 45 mm³/s | onset 34.5–38.5 mm³/s (measured heights 29–37 mm) | MVS 32 confirmed |
| 4 | **PA Pattern** 0.016 → 0.036 at 33/62/82 mm/s, 1200/3600 mm/s² | no too-high sign; tips match from about 0.026 | PA 0.026 |
| 5 | **Flow ratio, YOLO (Perfectionist)** around 0.9476 | all coupons felt alike, slightly rough | flow 0.9476 |
| 6 | Cooling model plus a new bridge piece | stopped three times by printer faults; not graded yet | open |

Steps 2–5 confirmed the profile instead of changing it, so no new revision was
made: the profile stayed at r10. That is a good outcome, not a wasted day:
the values had been right; the evidence for them had not.

### Value chain

| Revision | Change |
| --- | --- |
| r3 | MVS 58 (from a test on an earlier, undried spool at 280 °C) |
| r4 | PA 0.032 (from a tower that detached partway) |
| r6 | flow 0.97185 (Pass 1 and Pass 2) |
| r7 | new dry spool: 255 °C, MVS 32 |
| r8 | 245 °C |
| r9 | PA 0.026 |
| r10 | flow 0.9476 (YOLO, confirmed by the restart) |

### What to take from it

- An end-band temperature, a color change mid-spool and missing pass marks
  each cost prints. All three are rules in this guide; the run broke them
  before it followed them.
- A PA tower at one forced speed and a PA Pattern at production speeds
  disagreed. The pattern at production conditions decided.
- A YOLO result was first recorded as a multiplication; the arithmetic is
  addition. See [Flow Ratio](05-flow-ratio.md#run-the-coupons-in-tinman).
- The printer stopped jobs for its own reasons many times: probe connection
  drops, feeder empty-print detection, a Z-tilt check. None were filament
  results, and each was logged and reprinted unchanged.

## Prusa CORE One+ INDX, 3D-Fuel Pro PCTG, 0.4 mm High-Flow

**Setup:** CORE One+ with an eight-tool INDX changer, all 0.4 mm high-flow
nozzles, tuned on one tool. Smooth PEI, bed 85 °C. A brand-new printer.

The run started with a baseline Benchy, then followed the guide's order. Two
early surprises were machine problems, not filament problems: repeated bed
leveling failures came from a wrong rear bed stop fitted during the build, and
a partly clogged nozzle moved the work to the second tool.

| Step | Test | Result | Kept |
| --- | --- | --- | --- |
| Baseline | 3DBenchy | clean walls, overhangs and text; fine hairs; flat top ridges | accepted |
| Temperature | 270 → 240 °C | 250 °C: straight overhang lip, clean bridge, light stringing; cooler bands sag | 250 °C |
| Max flowrate | 10 → 30 mm³/s | gaps on straight walls from 21 mm = 20.5 mm³/s | MVS 19 (r3) |
| PA Tower | 0 → 0.1 | corners read 0.062 and 0.068; a faint line partway up | inconclusive |
| PA Tower | 0.040 → 0.090 | corners clean at different heights, 0.052–0.065 | inconclusive |
| PA Tower, chamber pre-warmed | same | single clean reading, no line | PA 0.055 (r5) |
| Flow ratio, YOLO | 0.95 → 1.05 | no coupon felt different from the others | flow 1.00 |
| Cooling model | bridges 10–40 mm, fins to 70 deg | all bridges pass at 90 % bridge fan; overhangs clean to 65 deg; pin snaps clean | - |
| Cooling model, max fan 15 % | one setting changed | geometry the same; pin still snaps clean on layers both prints ran at minimum fan | inconclusive |
| Pins only, max fan 15 % | short layers so the fan limit applies | all three 3 mm pins bent before they broke | max fan 15 % (r6) |
| Retraction | 0 → 2 mm | no strings at any length | kept 1.6 mm |
| Dimensions | frames 120/80/40 mm, holes 3–10 mm | same-sign 0.4 % error in X and Y | Shrinkage (XY) 99.6 % (r7) |
| Dimensions, confirm | same model on r7 | 120 mm frame within 0.10 mm | no change |
| Seams and surfaces | five shapes | narrow seams; beads along every top edge from Monotonic Line | A/B under way |

The chamber result is the one to remember. The printer's chamber fans switched
on partway through the first towers, when the chamber passed its target, and
every corner reading changed at that moment. Warming the chamber first and
keeping its fans off gave a single, clean reading. The profile now asks the
printer to warm the chamber before printing.

At the time of writing the profile is `CANDIDATE r7`: the remaining steps are a
representative part and the top-surface comparison.

## Qidi Plus4, Elegoo PET-CF

**Setup:** Qidi Plus4 with a hardened 0.6 mm nozzle, later a 0.4 mm one;
bed 100 °C, chamber 50 °C; filament dried and printed from a heated dry box.

### Foundation first

An earlier series had already "tuned" this filament: a temperature, a PA and a
flow ratio of 1.137. A review found the first layer printing far too thick
(coupons sliced at 0.30 mm measured 0.45–0.66 mm), because plastic left on
the nozzle after the purge made the probe set zero 0.3–0.4 mm high, very
repeatably. Every value from that series was marked invalid. A nozzle wipe
while cooling, and a start-code gate that stops the print when the probe reads
outside a window, fixed the foundation. Then tuning began again.

### The tune (0.6 mm)

| Step | Result | Kept |
| --- | --- | --- |
| Temperature, 285 → 260 °C | 260 °C fails, 265 °C marginal, 270–285 °C equal | 275 °C |
| MVS ramp to 21 mm³/s | no defect anywhere | MVS 19 (a floor) |
| PA tower 0 → 0.080 | no visible difference | PA 0 |
| Flow patches by caliper | top closes toward 1.04; parts keep growing above | flow 1.04 |
| Cooling | overhang fan 100 % fixed curl; bonding survived | overhang fan 100 % |
| Bridges, deck thickness | bridge flow 0.9 at 16 mm/s gave the best deck; faster was worse | bridge flow 0.9 |
| Retraction | no strings at any band | 0.4 mm |
| Dimensions, 70/45/20 mm | constant +0.27 mm outside | XY contour -0.13 mm |
| Seams 0/15/30 % | no visible seam at any setting | 15 % |

Validation on a real part then found fine whiskers on every feature narrower
than about two nozzle widths. A 5 °C drop, more fan, retract-before-wipe and
longer retraction all failed to clear them; a 0.4 mm nozzle did. The 0.4 mm
profile reuses the 0.6 mm filament values with MVS capped at 10, recorded
as inherited.

### Supports on the real part

Calibration prints had no supports. The validation part, a frame with many
holes and ledges, needed them, and getting them right took four process
revisions:

| Revision | Support interface | Result |
| --- | --- | --- |
| r03 | tree supports, 0.2 mm gaps | very hard to remove (a per-object override in the project made it worse) |
| r05 | concentric interface, three layers | came off easily, but each tree tip left a swirl |
| r06 | normal supports, rectilinear interface, support ironing on | clean underside where it came off, but the ironed interface fused to the part |
| r07 | as r06 without ironing; interface spacing 0.2 mm, top gap 0.2 mm; support-interface fan 100 % | a clear improvement: easy removal, clean underside |

![The same PET-CF frame after three support settings: r05 concentric interface (swirls under every tree tip), r06 ironed solid interface (fused to the part), r07 spaced rectilinear interface with 100 % interface fan (clean). Field photographs from the guide's tuning runs, 2026-11-19 and 2026-11-20; cropped and labeled.](../assets/field-tests/qidi-pet-cf-support-interface-r05-r07.jpg)

The released pairs are filament r14 with process r25 for 0.6 mm, and
filament r02 with process r07 for 0.4 mm. The revision numbers differ
because filament and process revisions count separately.

## Snapmaker U1, Push Plastic ABS, 0.4 mm

**Setup:** Snapmaker U1, four 0.4 mm toolheads, tuned on one; bed 100 °C,
heated chamber 50 °C, textured PEI.

| Stage | Test | Result | Revision |
| --- | --- | --- | --- |
| 1 | Benchy | no warp, clean overhangs; mild stringing; hull 1.25 % short | r01 (240 °C, MVS 20) |
| 2 | Temperature 250 → 225 °C | stringing the same in every band; 225–230 °C matte | keep 240 °C |
| 3 | Max flowrate 8 → 30 | no limit to 31 mm³/s | MVS 26 (r02) |
| 4 | PA Pattern 0.010 → 0.040 at three speeds, two accelerations | sharpest 0.024–0.028 | PA 0.026 (r03) |
| 5 | Flow ratio, YOLO | best coupon at the low end, -0.05 | flow 0.95 (r04) |
| 6 | Flow ratio, YOLO again, centred on 0.95 | raised ring above 0.95 | 0.95 confirmed |
| 7 | Retraction 0.2 → 2.0 | no strings from 0.3 to about 1.5 mm | keep 0.8 mm |
| 8 | Cooling model | bridges pass; fins clean to 55 deg; 70 deg fails | overhang fan 70 % (r05) |
| 8b | Fins again | 70 deg fins print full height | - |
| 9 | Dimension stack | same-sign proportional error in X and Y; holes not a constant error | Shrinkage (XY) 99.60 % (r06) |
| 10 | Seams and surfaces | judged nearly perfect | `TUNED r06` |

Two Tinman lessons came out of this run. The Max flowrate test was built
while a different filament was open for editing, so the ramp was capped at
the printing filament's own limit and had to be corrected by post-processing
the G-code. And because the test objects start on filament 1,
every test had to be moved to the fourth slot before slicing. Both are now
covered by [the safe recipe](25-running-tinman-calibrations.md#the-safe-recipe).

The run then built a faster "Quality" process on the tuned filament, about
half the print time of the original process, and checked it with the same
dimension stack and seam test: the dimensions stayed within about 0.1 mm of
the slower process and the seams were as clean. Reusing the stage 9 and stage
10 test models as acceptance tests for a new process is a cheap, honest check.

## What All Four Runs Had in Common

- **Every one found a foundation or machine problem first**: a soft bed under
  load, a wrong bed stop, plastic on the nozzle, a filament feeder pausing
  layer one. Fixing those mattered more than any filament value.
- **Several tests "failed" by showing nothing**: flow coupons that all felt
  the same, a PA tower with no change, retraction towers with no strings. Each
  of those was a result, and the right response was to keep the current value
  and move on.
- **The same filament tuned differently on every printer.** 3D-Fuel Pro PCTG
  ran at 245, 250, 250 and 255 °C on four machines, with MVS from 19
  to 32 and PA from 0.026 to 0.055.
- **Written pass marks and one change per print** were what finally made each
  run converge.
