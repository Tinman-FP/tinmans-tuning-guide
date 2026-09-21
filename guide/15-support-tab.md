# Support Tab

Ordinary support, raft, interface, advanced, and tree groups are **Shared
2.4.2**. The Wave groups are **TinmanX1 additions** and **experimental**.
Support tuning is a compromise among underside quality, removability, print
time, material, and the risk of a failed unsupported feature.

## Support

**What:** decides whether support is generated, where it is allowed, and which
broad geometry style it uses.

**Use it when:** a feature cannot be bridged or overhung reliably in its current
orientation.

**Desired result:** the least support that makes the model succeed, with stable
columns and reachable removal paths.

- `Enable support` turns generation on; automatic and manual support types
  decide whether angle rules or painted/enforced regions drive placement.
- `Style` chooses normal grid/snug or tree-family behavior.
- `Threshold angle` and `threshold overlap` control how unsupported a region may
  be before support appears.
- `Initial layer density` and `initial layer expansion` stabilize the support's
  own footprint.
- `On build plate only` prevents support from starting on the model.
- `Critical regions only` limits support to regions judged most likely to fail.
- `Ignore small overhangs` suppresses tiny, often self-supporting islands.

Orient the part before increasing support. A better orientation can improve
strength and remove more support than any density adjustment.

## Raft

**What:** creates sacrificial layers under the entire supported footprint.

**Use it when:** the part or support needs a stable, planar base that a brim
cannot provide, or the machine/material combination makes first-layer recovery
more important than bottom finish.

**Desired result:** a secure print that separates from the raft without tearing
the part or leaving a badly distorted bottom.

- `Raft layers` controls raft thickness and rigidity.
- `Raft contact distance` controls release versus underside support. Smaller is
  tighter and cleaner underneath but harder to remove.

## Support Filament

**What:** assigns material slots to support base and interface roles.

**Use it when:** a multi-material system can use a soluble, breakaway, or
non-bonding interface material.

**Desired result:** reliable tool changes and an interface that supports the
model yet releases or dissolves as intended.

- `Support filament` selects the base material.
- `Support interface filament` selects the contact material.
- `Avoid interface filament for base` preserves expensive or slow interface
  material for contact layers only.

Validate material compatibility; some pairs bond too strongly, too weakly, or
at incompatible temperatures.

## Support Ironing

**What:** smooths the top of support before the model is printed on it.

**Use it when:** support-interface texture transfers to a broad underside and
ordinary interface spacing cannot provide a consistent platform.

**Desired result:** a flatter support roof without fusing the interface to the
model.

- Enable, pattern, flow, and spacing work like ordinary ironing but apply to
  support. Heat buildup and excessive flow can make removal worse.

## Wave Overhangs

**Difference:** **TinmanX1 addition, experimental.** OrcaSlicer 2.4.2 does not
have Wave Overhangs.

**What:** replaces selected unsupported regions with wave-shaped paths intended
to grow outward from supported material.

**Use it when:** conventional supports are undesirable and the feature is a
candidate for carefully previewed supportless construction.

**Desired result:** connected wave paths that remain anchored and leave only
small residual regions for ordinary support.

- `Use wave overhangs` enables the generator.
- `Use wave overhangs instead of bridges` extends it to spans that would
  otherwise use straight bridge roads.
- `Support remaining areas` keeps ordinary support under regions the wave
  planner cannot cover.

Always inspect the preview. Leave ordinary support available until the wave
coverage has been validated for the exact part and material.

## Wave Detection

**What:** decides which overhang regions qualify and how aggressively the
planner grows them.

**Use it when:** waves appear on easy geometry, fail to reach a useful region,
or consume excessive computation and path complexity.

**Desired result:** only genuinely difficult, sufficiently large regions are
selected and solved in a reasonable number of iterations.

- Minimum angle and length reject easy or tiny candidates.
- Maximum iterations caps planning work and outward growth.

## Wave Pattern

**What:** shapes and spaces the generated wave roads and determines how they
meet ordinary perimeters.

**Use it when:** previewed waves lack support, leave gaps, overfill edges, or
start in poor locations.

**Desired result:** continuous, evenly supported roads with a controlled joint
to the real model boundary.

- Pattern selects monotonic, zigzag, or smart path ordering.
- Seam mode chooses alternating, aligned, or deterministic random starts.
- Perimeter count retains ordinary walls at the edge.
- Line spacing and spacing mode control wave density and progression.
- Perimeter overlap controls attachment to normal walls.
- Minimum width and minimum new area suppress fragments.
- Flow per path length controls deposited wave volume directly.

## Wave Fringe Reinforcement

**What:** limits small reinforcing wave regions near the boundary between real
geometry and generated cover.

**Use it when:** fringes either fail to support an edge or spread excessive
material beyond the useful contact area.

**Desired result:** enough local reinforcement to anchor the fringe, with no
large artificial shelf.

The cover-to-real ratio, maximum cover area, and contact-over-cap compensation
are interacting safety bounds. Change one at a time and inspect the path area,
not just the numeric value.

## Wave Corner Reinforcement

**What:** increases support near corners where uniform wave spacing can leave a
weak or abrupt transition.

**Use it when:** preview or test prints show corner droop, separation, or a
visible density step.

**Desired result:** a gradual, locally denser corner region without a blob.

- Enable turns on corner tapering.
- Corner spacing, taper distance, and angle threshold set its density, reach,
  and eligibility.

## Wave Motion

**What:** assigns extrusion, perimeter, travel, and end-retraction behavior to
wave paths.

**Use it when:** geometry is correct in preview but physical waves detach,
vibrate, ooze, or mark their endpoints.

**Desired result:** calm deposition that keeps each wave attached while moving
cleanly between regions.

- Wave print, perimeter, and travel speeds separate the motion roles.
- End retraction controls pressure at the finish of a wave route.

## Wave Cooling

**What:** applies wave-specific fans, nozzle temperature, and minimum timing.

**Use it when:** waves remain soft and curl, or cool so aggressively that they
do not bond.

**Desired result:** each path is firm enough to support the next while still
bonding to its anchor.

- Part and auxiliary fan targets control airflow.
- Nozzle temperature controls bonding and sag.
- Minimum wave and layer times prevent a rapid return to soft material.

## Wave Floor Layers

**What:** builds stabilizing layers under the final wave-supported surface.

**Use it when:** the top of the generated support needs a more uniform platform
or gradual speed/cooling transition.

**Desired result:** a stable floor that supports the model without becoming a
fused mass.

- Floor layer count sets depth.
- Hilbert use, layer count, and density change floor topology.
- Floor print/perimeter speed, speed ramp, and fan targets control the thermal
  transition into the model.

## Wave Debug

**What:** emits diagnostic G-code information for development and path audit.

**Use it when:** reproducing or reporting a planner problem, not as routine
print tuning.

**Desired result:** enough trace evidence to explain a generated path without
changing production geometry unintentionally.

## Advanced Support

**What:** controls the air gaps, patterns, interfaces, clearance, and layer
planning that determine support quality and release.

**Use it when:** the broad support style is correct but the underside, removal,
clearance, or support stability is not.

**Desired result:** a continuous interface close enough to support the model,
far enough to release, and clear of visible sidewalls.

- Top and bottom Z distances control vertical separation.
- Support wall loops and base pattern/spacing control base stiffness.
- Pattern angle rotates the support structure.
- Top and bottom interface layers, pattern, and spacing control the contact roof
  and floor.
- Support expansion grows or shrinks normal support laterally.
- Object XY distance protects sidewalls; first-layer gap protects the model's
  first-layer region.
- `Do not support bridges` trusts bridge paths instead of placing support below.
- `Maximum bridge length` limits that trust.
- `Independent support layer height` lets support use its own vertical schedule.

Tune Z distance in layer-height-aware increments. A distance that is not
representable by the layer plan may not behave as the decimal suggests.

## Tree Supports

**What:** controls branch tips, spacing, density, diameter, angle, and roots for
tree-style support.

**Use it when:** support must reach isolated overhangs while avoiding much of the
model surface.

**Desired result:** branches that are stiff enough to survive motion, narrow
enough to remove, and able to reach the target without collision.

- Tip diameter controls contact size.
- Branch distance and top rate control how densely tips merge.
- Branch diameter and diameter angle control trunk growth toward the bed.
- Branch angle and preferred slow angle control reach versus stability.
- Organic variants apply to the organic style.
- Auto brim and brim width stabilize the roots.

Continue with the [Multimaterial tab](16-multimaterial-tab.md).
