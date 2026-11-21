# Support Tab

> **At a glance**
> - **Decide:** support type, gaps and interface for a validation part
> - **Test:** the real part, after the filament is tuned (tuning prints have no supports)
> - **Keep:** supports that come off cleanly and leave an acceptable underside

Ordinary support, raft, interface, advanced, and tree groups are **Shared
2.4.2**. The Wave groups are **TinmanX1 additions** and **experimental**.
Support tuning is a compromise among underside quality, removability, print
time, material, and the risk of a failed unsupported feature.

OrcaSlicer 2.5, and so current Tinman, changes support-interface generation.
Revalidate counts, materials, and removal quality after upgrading; see
[changed toolpaths](21-slicer-upgrades-and-calibration-changes.md#revalidate-toolpaths-not-only-entered-values).

Supports are tuned on validation parts, not on calibration coupons, which are
printed without supports. Every value in this chapter is a range you choose,
not a preset you must accept: the Z gaps, interface spacing and interface
layers can be set to any value the part needs. A PET-CF run's progression from
hard-to-remove supports to clean undersides is in
[Worked Examples](26-worked-examples.md#qidi-plus4-elegoo-pet-cf).

## Support

| This group | |
| --- | --- |
| **What it controls** | Decides whether support is generated, where it is allowed, and which broad geometry style it uses. |
| **Change it when** | A feature cannot be bridged or overhung reliably in its current orientation. |
| **Aim for** | The least support that makes the model succeed, with stable columns and reachable removal paths. |

| Control | What it does |
| --- | --- |
| `Enable support` | Turns generation on; automatic and manual support types decide whether angle rules or painted/enforced regions drive placement. |
| `Style` | Chooses normal grid/snug or tree-family behavior. |
| `Threshold angle`, `threshold overlap` | Control how unsupported a region may be before support appears. |
| `Initial layer density`, `initial layer expansion` | Stabilize the support's own footprint. |
| `On build plate only` | Prevents support from starting on the model. |
| `Critical regions only` | Limits support to regions judged most likely to fail. |
| `Ignore small overhangs` | Suppresses tiny, often self-supporting islands. |

Orient the part before increasing support. A better orientation can improve
strength and remove more support than any density adjustment.

## Raft

| This group | |
| --- | --- |
| **What it controls** | Creates sacrificial layers under the entire supported footprint. |
| **Change it when** | The part or support needs a stable, planar base that a brim cannot provide, or the machine/material combination makes first-layer recovery more important than bottom finish. |
| **Aim for** | A secure print that separates from the raft without tearing the part or leaving a badly distorted bottom. |

| Control | What it does |
| --- | --- |
| `Raft layers` | Controls raft thickness and rigidity. |
| `Raft contact distance` | Controls release versus underside support. Smaller is tighter and cleaner underneath but harder to remove. |

## Support Filament

| This group | |
| --- | --- |
| **What it controls** | Assigns material slots to support base and interface roles. |
| **Change it when** | A multi-material system can use a soluble, breakaway, or non-bonding interface material. |
| **Aim for** | Reliable tool changes and an interface that supports the model yet releases or dissolves as intended. |

| Control | What it does |
| --- | --- |
| `Support filament` | Selects the base material. |
| `Support interface filament` | Selects the contact material. |
| `Avoid interface filament for base` | Preserves expensive or slow interface material for contact layers only. |

Validate material compatibility; some pairs bond too strongly, too weakly, or
at incompatible temperatures.

## Support Ironing

| This group | |
| --- | --- |
| **What it controls** | Smooths the top of support before the model is printed on it. |
| **Change it when** | Support-interface texture transfers to a broad underside and ordinary interface spacing cannot provide a consistent platform. |
| **Aim for** | A flatter support roof without fusing the interface to the model. |

| Control | What it does |
| --- | --- |
| Enable, pattern, flow, and spacing | Work like ordinary ironing but apply to support. Heat buildup and excessive flow can make removal worse. |

## Wave Overhangs

**Difference:** **TinmanX1 addition, experimental.** OrcaSlicer 2.4.2 does not
have Wave Overhangs.

| This group | |
| --- | --- |
| **What it controls** | Replaces selected unsupported regions with wave-shaped paths intended to grow outward from supported material. |
| **Change it when** | Conventional supports are undesirable and the feature is a candidate for carefully previewed supportless construction. |
| **Aim for** | Connected wave paths that remain anchored and leave only small residual regions for ordinary support. |

| Control | What it does |
| --- | --- |
| `Use wave overhangs` | Enables the generator. |
| `Use wave overhangs instead of bridges` | Extends it to spans that would otherwise use straight bridge roads. |
| `Support remaining areas` | Keeps ordinary support under regions the wave planner cannot cover. |

Always inspect the preview. Leave ordinary support available until the wave
coverage has been validated for the exact part and material.

## Wave Detection

| This group | |
| --- | --- |
| **What it controls** | Decides which overhang regions qualify and how aggressively the planner grows them. |
| **Change it when** | Waves appear on easy geometry, fail to reach a useful region, or consume excessive computation and path complexity. |
| **Aim for** | Only genuinely difficult, sufficiently large regions are selected and solved in a reasonable number of iterations. |

| Control | What it does |
| --- | --- |
| Minimum angle and length | Reject easy or tiny candidates. |
| Maximum iterations | Caps planning work and outward growth. |

## Wave Pattern

| This group | |
| --- | --- |
| **What it controls** | Shapes and spaces the generated wave roads and determines how they meet ordinary perimeters. |
| **Change it when** | Previewed waves lack support, leave gaps, overfill edges, or start in poor locations. |
| **Aim for** | Continuous, evenly supported roads with a controlled joint to the real model boundary. |

- Pattern selects monotonic, zigzag, or smart path ordering.
- Seam mode chooses alternating, aligned, or deterministic random starts.
- Perimeter count retains ordinary walls at the edge.
- Line spacing and spacing mode control wave density and progression.
- Perimeter overlap controls attachment to normal walls.
- Minimum width and minimum new area suppress fragments.
- Flow per path length controls deposited wave volume directly.

## Wave Fringe Reinforcement

| This group | |
| --- | --- |
| **What it controls** | Limits small reinforcing wave regions near the boundary between real geometry and generated cover. |
| **Change it when** | Fringes either fail to support an edge or spread excessive material beyond the useful contact area. |
| **Aim for** | Enough local reinforcement to anchor the fringe, with no large artificial shelf. |

The cover-to-real ratio, maximum cover area, and contact-over-cap compensation
are interacting safety bounds. Change one at a time and inspect the path area,
not just the numeric value.

## Wave Corner Reinforcement

| This group | |
| --- | --- |
| **What it controls** | Increases support near corners where uniform wave spacing can leave a weak or abrupt transition. |
| **Change it when** | Preview or test prints show corner droop, separation, or a visible density step. |
| **Aim for** | A gradual, locally denser corner region without a blob. |

| Control | What it does |
| --- | --- |
| Enable | Turns on corner tapering. |
| Corner spacing, taper distance, and angle threshold | Set its density, reach, and eligibility. |

## Wave Motion

| This group | |
| --- | --- |
| **What it controls** | Assigns extrusion, perimeter, travel, and end-retraction behavior to wave paths. |
| **Change it when** | Geometry is correct in preview but physical waves detach, vibrate, ooze, or mark their endpoints. |
| **Aim for** | Calm deposition that keeps each wave attached while moving cleanly between regions. |

- Wave print, perimeter, and travel speeds separate the motion roles.
- End retraction controls pressure at the finish of a wave route.

## Wave Cooling

| This group | |
| --- | --- |
| **What it controls** | Applies wave-specific fans, nozzle temperature, and minimum timing. |
| **Change it when** | Waves remain soft and curl, or cool so aggressively that they do not bond. |
| **Aim for** | Each path is firm enough to support the next while still bonding to its anchor. |

| Control | What it does |
| --- | --- |
| Part and auxiliary fan | Targets control airflow. |
| Nozzle temperature | Controls bonding and sag. |
| Minimum wave and layer times | Prevent a rapid return to soft material. |

## Wave Floor Layers

| This group | |
| --- | --- |
| **What it controls** | Builds stabilizing layers under the final wave-supported surface. |
| **Change it when** | The top of the generated support needs a more uniform platform or gradual speed/cooling transition. |
| **Aim for** | A stable floor that supports the model without becoming a fused mass. |

| Control | What it does |
| --- | --- |
| Floor layer count | Sets depth. |
| Hilbert | Use, layer count, and density change floor topology. |
| Floor print/perimeter speed, speed ramp, and fan | Targets control the thermal transition into the model. |

## Wave Debug

| This group | |
| --- | --- |
| **What it controls** | Emits diagnostic G-code information for development and path audit. |
| **Change it when** | Reproducing or reporting a planner problem, not as routine print tuning. |
| **Aim for** | Enough trace evidence to explain a generated path without changing production geometry unintentionally. |

## Advanced Support

| This group | |
| --- | --- |
| **What it controls** | Controls the air gaps, patterns, interfaces, clearance, and layer planning that determine support quality and release. |
| **Change it when** | The broad support style is correct but the underside, removal, clearance, or support stability is not. |
| **Aim for** | A continuous interface close enough to support the model, far enough to release, and clear of visible sidewalls. |

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

| This group | |
| --- | --- |
| **What it controls** | Controls branch tips, spacing, density, diameter, angle, and roots for tree-style support. |
| **Change it when** | Support must reach isolated overhangs while avoiding much of the model surface. |
| **Aim for** | Branches that are stiff enough to survive motion, narrow enough to remove, and able to reach the target without collision. |

- Tip diameter controls contact size.
- Branch distance and top rate control how densely tips merge.
- Branch diameter and diameter angle control trunk growth toward the bed.
- Branch angle and preferred slow angle control reach versus stability.
- Organic variants apply to the organic style.
- Auto brim and brim width stabilize the roots.

Continue with the [Multimaterial tab](16-multimaterial-tab.md).
