# Seams and Surface Quality

A seam is the repeated start and stop of a perimeter. It concentrates pressure,
ooze, travel, retraction, wipe, and placement effects into one visible region.
Treat it as a local transition problem, not automatic evidence that global flow
is wrong.

## Read the Seam in Two Parts

### End of the previous perimeter

- Bulge: pressure may remain too high; PA may be low.
- Gap or thin finish: PA may be high, the seam gap may be large, or wipe may be
  excessive.

### Start of the next perimeter

- Blob: ooze, over-prime, short travel, temperature, or inconsistent restart.
- Gap: excess retraction, delayed pressure recovery, large seam gap, or
  insufficient restart.

Long and short travels can produce different starts. Compare both before tuning
one global restart value.

## Tuning Order

1. Dry the filament and settle temperature.
2. Tune MVS, PA, and global flow.
3. Choose a repeatable seam location for diagnosis.
4. Tune retraction and wipe if travel artifacts remain.
5. Adjust seam gap or scarf behavior in small increments.
6. Validate around curves and sharp corners.

Aligned seams make diagnosis easier. Random seams can make cosmetic texture
less concentrated but hide a systematic error.

## Conventional Seam Controls

- seam position or painting;
- seam gap;
- wipe before or while retracting;
- retraction distance and speed;
- travel path and wall-crossing avoidance;
- perimeter order;
- start-point placement and corner preference.

Change one control at a time because several of these alter the same material
transition.

## Scarf Seams

A scarf seam spreads a layer transition over a distance instead of placing the
entire start/stop event at one point. It can reduce a vertical ridge but adds
variables such as scarf length, start height, conditional use, wall selection,
and gap behavior.

Tune scarf settings only after ordinary pressure and flow are stable. A scarf
can spread an incorrect transition without correcting its cause.

## Surface Artifact Map

| Surface evidence | First suspects |
| --- | --- |
| Repeating vertical line at one XY point | seam transition and placement |
| Bulge on every sharp corner | PA low, acceleration, wall order |
| Thin approach to corners | PA high or flow transition |
| Periodic vertical ripples after corners | ringing/input shaping/mechanics |
| Repeating fine vertical texture | VFA, motor/motion system, belt behavior |
| Random pits or bubbles | moisture, contamination, nozzle debris |
| Horizontal banding at regular Z spacing | Z motion, lead screw, temperature cycle |
| Gloss changes at feature transitions | speed/flow/temperature/cooling change |
| Rough top only | top flow, support below top, top speed/width/pattern |
| Wall roughness only at high speed | MVS, temperature, extrusion-rate transition |

## Top and Bottom Surfaces

Surface quality depends on more than flow:

- shell thickness;
- pattern and direction;
- top/bottom speed and acceleration;
- line width;
- overlap with perimeters;
- infill support;
- monotonic ordering;
- ironing, if used;
- lower-layer flatness.

Tune ironing last. It can hide top texture but introduces its own flow, spacing,
speed, heat, and edge behavior.

## Judge in Appropriate Light

Glossy and dark polymers exaggerate small ridges under flash. Use diffuse and
glancing light, touch the surface, and compare a control. Decide whether the
surface fails the intended use, not whether one photograph can reveal a line.

Finish with [Validation and Profile Release](09-validation.md).

