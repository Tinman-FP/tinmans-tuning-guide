# Cooling, Bridges, Retraction, and Travel

Cooling and retraction both affect strings and small features, but they solve
different physical problems. Tune cooling first for deposited geometry, then
use retraction and travel controls for pressure and ooze during non-print moves.

## Cooling Is a Tradeoff

More part cooling can improve:

- overhang definition;
- short bridges;
- small features and minimum-layer-time behavior;
- resistance to curl on newly deposited edges.

Too much cooling can cause:

- weak layer bonding;
- warping or cracking;
- inconsistent shrinkage;
- poor chamber stability;
- nozzle-temperature droop when airflow strikes the heater block.

Use the least cooling that delivers the required geometry and strength.

## Separate Fan Roles

Printers may have several fans:

- hotend heatsink fan;
- part-cooling fan;
- auxiliary or side fan;
- chamber circulation fan;
- chamber exhaust fan.

Do not treat them as one percentage. An auxiliary fan can create a directional
surface difference or warping that the main part fan does not.

## Cooling Test Method

Use an artifact with repeatable overhang angles, small towers, and bridges.
Hold temperature, flow, and speed constant.

Evaluate:

- overhang edge curl and underside shape;
- bridge sag, strand separation, and anchoring;
- small-feature deformation;
- layer adhesion after cooling;
- directional differences between faces;
- warping, lifting, or inter-layer cracks.

High-shrink materials should be tested in the same enclosure and chamber state
used for production.

## Bridge Controls

Bridges can have their own speed, flow, line width, cooling, PA, and direction.
Tune them as a feature after general temperature and cooling are credible.

- Too much bridge flow can produce heavy sagging strands.
- Too little can produce thin, broken, or poorly anchored strands.
- Too fast can break anchoring or stretch strands excessively.
- Too slow can give the strand more time to sag.
- More fan can help shape but may hurt bonding or high-shrink materials.

Test the span lengths and directions that matter to the actual part.

## Retraction Purpose

Retraction temporarily relieves or removes material from the nozzle entrance
during travel. It cannot remove moisture, correct PA, or fix an excessively hot
and leaking nozzle by itself.

Tune retraction only after:

- the filament is dry;
- temperature is accepted;
- PA is reasonable;
- travel moves are fast and mechanically reliable;
- the nozzle is clean and not partially clogged.

## Retraction Test

1. Choose a range appropriate to the extruder path and manufacturer guidance.
2. Keep retraction speed fixed while tuning distance.
3. Select the shortest distance that gives the cleanest repeatable result.
4. Refine speed only if needed.
5. Confirm on a model with realistic travel distances and feature sizes.

Too much retraction can create:

- delayed restart or gaps after travel;
- filament grinding;
- heat-creep or clog risk;
- bubbles caused by drawing air into the melt zone;
- unnecessary wear and print time.

## Travel, Wipe, and Z Hop

- **Travel speed** reduces ooze time but must remain mechanically reliable.
- **Avoid crossing walls/perimeters** can hide strings inside a part at the
  cost of longer travel.
- **Wipe** can reduce material left at a seam, but interacts with PA and
  retraction.
- **Z hop** can avoid collisions, but adds time and may increase ooze or surface
  marks. Use it for a demonstrated need.
- **Extra restart/prime** is rarely the first fix for a tuned modern extrusion
  system; it can trade a gap for a blob.

## Diagnose Strings by Shape

| Evidence | First suspects |
| --- | --- |
| Fine hairs everywhere | moisture, temperature, material tendency |
| Thick strings between towers | retraction distance/speed, travel time |
| Blob followed by string | seam pressure, PA, ooze, wipe |
| Gap after every travel | excessive retraction or insufficient restart |
| Strings only on one side | fan direction, airflow, travel path |

Once deposited geometry and travel behavior are stable, move to
[Dimensional Accuracy](07-dimensional-accuracy.md).

