# TinmanX1 Fiber and Strength Tools

Everything in this chapter is a **TinmanX1 addition** relative to OrcaSlicer
2.4.2. The settings are distributed across three profile types because they
answer different questions:

- the **process profile** decides where and how fiber is planned;
- the **filament profile** describes the continuous fiber and carrier plastic;
- the **printer profile** describes FibreSeek hardware and machine commands.

Do not move a machine-contract value into process tuning. A part strategy may
change from job to job; nozzle offsets, cutter travel, and tool-change commands
must remain faithful to the hardware.

## Strength Lens

**What:** provides a pre-slice color view of orientation risk using a simplified
material model and chosen load axis.

**Use it when:** orienting a load-bearing part or deciding where continuous fiber
could help. It is most useful for comparing orientations of the same design.

**Desired result:** critical loads run through strong printed roads instead of
trying to separate the layer stack.

- `Strength Lens` enables the overlay.
- `Material model` selects filament-preset behavior, isotropic comparison,
  ordinary anisotropic FDM, or continuous fiber.
- `Load axis` selects Auto, X, Y, or Z.
- `Strength Lens payload` is saved analysis data. It is a **profile-contract
  field**, not a normal tuning control, and should not be hand-edited.

The lens is not finite-element analysis. It does not know the real boundary
conditions, defects, voids, fiber waviness, temperature history, or measured
material allowables. Use it to choose what to test, not to certify a part.

## Process Profile: Planning

**What:** selects the manufacturing model and broad fiber layout for the part.

**Use it when:** choosing whether fiber supplements plastic roads or owns
composite roads, and when establishing the first defensible layup before fine
motion tuning.

**Desired result:** only intentional, manufacturable routes appear, beginning on
the intended layers and aligned with the load strategy.

- `Fiber manufacturing mode` chooses **Plastic + fiber overlay** or
  **Fiber-owned composite roads**. Overlay preserves the polymer structure and
  adds fiber; composite-road mode lets fiber planning own selected roads and
  refill the remaining plastic regions.
- `Generate fiber perimeters` requests closed reinforcement near outlines.
- `Generate fiber infill` requests internal reinforcing routes.
- `Fiber reinforcement mode` applies the Light, Medium, or Heavy planning
  policy. Treat these as coordinated starting presets, not measured strength
  grades.
- `Fiber start layer` delays reinforcement until the part has a stable plastic
  foundation or until fiber reaches a useful Z region.
- `Fiber infill pattern` chooses the broad internal layout.
- `Fiber infill density` derives road spacing from line width when set above
  zero; zero delegates spacing to the mode or explicit spacing field.
- `Fiber infill angles` supplies a comma-separated angle sequence when the part
  needs known directions rather than the pattern default.
- `Fiber infill source` chooses plastic traces, newly generated ribs, or
  explicitly marked fiber paths.
- `Fiber seam position` chooses source, nearest, aligned, rear, or deterministic
  random start locations for closed routes.
- `Fiber seam angle` positions aligned starts around each loop.
- `Fiber print order` is an expert planner-order code. Leave it at the validated
  profile value unless a documented workflow requires a different sequence.

Choose route family and direction before density. More fiber in the wrong
direction can add cost and complexity without solving the load case.

## Process Profile: Geometry

**What:** constrains fiber-road width, spacing, layer schedule, curvature,
minimum length, and clearance from walls.

**Use it when:** planned routes do not match the physical composite road, enter
spaces the nozzle cannot reach, bend too tightly, or create impractically short
segments.

**Desired result:** smooth, continuous routes that fit the machine's placement
geometry and stay inside valid model regions.

- `Fiber line width` should match the effective deposited composite road, not
  merely the nominal fiber diameter.
- `Fiber infill spacing` sets explicit road pitch; zero delegates it to the
  reinforcement mode.
- `Fiber layer height` sets the fiber macro-layer spacing; zero uses the mode.
- `Fiber layer step` reinforces every Nth printable layer; zero uses the mode.
- `Fiber minimum radius` expresses the preferred bend quality. Larger values
  favor smoother paths, but the planner may still use shorter-radius paths when
  necessary.
- `Fiber max arc segment` controls how finely curves are divided. Short segments
  are smoother but produce more G-code and motion blocks.
- `Fiber minimum route length` filters generated routes; zero uses the planner
  default.
- `Fiber perimeter minimum length` specifically rejects short closed or
  outline-oriented routes.
- `Fiber hardware minimum length` protects the cutter/feed mechanism from
  segments shorter than it can manage reliably.
- `Fiber perimeter inset` places outline reinforcement away from the model
  boundary; zero delegates to the planner.
- `Fiber infill inset` keeps generated ribs away from walls and holes; zero
  delegates to the planner.

The mechanical minimum is a hardware constraint. Do not lower it simply to make
more preview paths appear.

## Process Profile: Feed and Motion

**What:** controls normal fiber speed, start behavior, tensioning, feed ratio,
after-cut plastic, and optional Z lift.

**Use it when:** correct routes are visible in preview but physical fiber slips,
buckles, detaches at starts, remains loose, or drags after a cut.

**Desired result:** the strand starts attached, stays placed without excess
tension, and ends cleanly without disturbing the part.

- `Fiber print speed` is the normal deposition target; zero uses the planner
  default.
- `Fiber start speed` slows the beginning of a route; zero uses the default.
- Start, normal, and finish maximum speeds cap the three route phases.
- `Fiber start length` defines the initial controlled phase.
- `Fiber slow length` keeps the strand slow while adhesion develops.
- `Fiber tension length` defines the straightening segment.
- `Fiber tension feedrate` sets motion during tensioning.
- `Fiber tension release` returns a fraction of feed to reduce retained tension;
  zero disables release compensation.
- `Fiber feedrate` is fiber feed relative to path length. Below 100% adds
  tension; above 100% relaxes the strand. Small changes can have large physical
  effects.
- `After-cut plastic multiplier` adjusts polymer immediately after a fiber cut
  or restart.
- `Fiber Z hop after cut` lifts before travel to reduce dragging.

Do not compensate a wrong route length or cutter position with feed percentage.
Fix geometry and hardware contracts first.

## Process Profile: Advanced Feed Phases

**What:** places speed floors and curve-sensitive targets around start, normal,
finish, and correction phases.

**Use it when:** a validated basic route still changes quality between straight
and curved segments or trajectory corrections need dedicated motion behavior.

**Desired result:** smooth phase transitions with no stalls, sudden tension
spikes, or correction marks.

- Start, normal, and finish `minimum speed` values are curved-segment targets.
- Their `speed floor` values are the lowest allowed targets.
- `Override correction move speed` activates dedicated correction motion.
- `Correction move speed` and `correction fiber feedrate` define that motion.

These are expert controls. Zero commonly delegates to the existing planner
policy. Tune them only with synchronized video, G-code inspection, or other
evidence that identifies the failing phase.

## Process Profile: Fiber First Layer

**What:** supplies optional flow, width, height, and speed multipliers for
fiber-related first-layer geometry.

**Use it when:** fiber itself is intentionally present near the first layer and
the ordinary plastic first-layer settings do not produce a sound foundation.

**Desired result:** stable, dimensionally controlled first-layer fiber geometry
without over-compression or poor bed clearance.

- `Fiber first-layer flow`, `width`, `height`, and `speed` are expert overrides.
  Zero delegates to the validated defaults.

Do not use these fields to correct the printer's global Z offset or bed mesh.

## Process Profile: Planner Limits

**What:** caps route count and defines how fiber loops coexist with plastic
shells and cutter cycles.

**Use it when:** a layup is too dense, produces excessive cut/restart events, or
places fiber too close to the visible shell or internal voids.

**Desired result:** a bounded route plan with deliberate shell protection and a
manageable number of cutter operations.

- `Fiber max routes per layer` is a safety cap; zero uses the reinforcement
  mode.
- `Fiber routes per cut` groups same-layer routes into cut/restart cycles where
  the hardware and path permit.
- `Fiber outer loops` requests reinforcement near outside-oriented contours.
- `Fiber inner loops` requests reinforcement near holes or inside contours.
- `Plastic loops outside fiber` retains polymer between fiber and the visible
  exterior.
- `Plastic loops inside fiber` retains polymer between fiber and infill or
  internal openings.

Preview every layer containing holes. An apparent loop count is not useful if
the resulting bend radius or shell clearance is unmanufacturable.

## Process Profile: Advanced Layup Payload

**What:** stores serialized planner instructions that cannot be expressed by the
ordinary controls.

**Use it when:** an audited workflow generates explicit layup bands or solid
fiber definitions programmatically.

**Desired result:** schema-valid, reproducible planning data that survives save,
reload, and export without silent reinterpretation.

- `Fiber advanced layup payload` can encode layer/Z bands, mode, pattern,
  perimeter and infill intent, spacing, route caps, priority, and prime-line
  information.
- `Fiber solid infill payload` can encode solid-fiber angles, road width,
  extension, and minimum segment length.

Both are **profile-contract fields**. Most users should leave them unchanged.
Hand-editing unvalidated JSON can create plausible-looking but unsafe output.

## Filament Profile: Continuous Fiber

**What:** identifies the fiber spool and carrier plastic, then records material
temperatures, speeds, timing, and cost data.

**Use it when:** creating or auditing a TinmanX1 composite filament preset for a
specific fiber and polymer combination.

**Desired result:** one preset describes the actual installed materials and
supports traceable estimates and machine commands.

- `Composite enabled` marks the preset as a composite workflow.
- Fiber name, type, manufacturer, diameter, linear density, spool length, and
  cost identify and quantify the reinforcement.
- Carrier-plastic name, type, manufacturer, diameter, density, cost, and spool
  weight identify the matrix material.
- Fiber-nozzle preheat and standby temperatures define the composite thermal
  state around use and idle periods.
- `Fiber first layers height` records the plastic foundation height before fiber
  placement.
- Plastic and fiber extrusion speeds describe material-specific feed behavior.
- `Fiber restart pause` gives the mechanism time to establish a restarted
  strand.
- `Fiber finish ironing distance` controls the end-of-route finishing distance.
- `Fiber priming line height` describes priming geometry.
- `Fiber material kind` classifies the reinforcement for planning and Strength
  Lens behavior.
- `Fiber source material ID` links the preset to a source material record.

Material identity is evidence, not decoration. Record lot, conditioning, and
source ID so a good layup can be reproduced.

## Printer Profile: FibreSeek Machine Contract

**What:** declares that a printer supports fiber, identifies the nozzle
arrangement, and selects the post-processing contract.

**Use it when:** commissioning or auditing a FibreSeek-capable printer profile.

**Desired result:** the slicer describes the real machine exactly and emits only
operations the machine can perform.

- `Fiber enabled` activates FibreSeek capability for the printer profile.
- `Shared fiber nozzle` states whether plastic and fiber share the same nozzle
  path.
- Plastic and composite nozzle diameters define the two road systems.
- `Fiber postprocessor type` selects the expected output transformation.

These are **profile-contract fields**. They should not vary per cosmetic print.

## Printer Profile: Extruder Contract

**What:** records plastic/composite tool offsets, heat-up rates, and
firmware-addressable fans.

**Use it when:** calibrating tool alignment, time estimates, or tool-specific
cooling hardware.

**Desired result:** plastic and composite paths align in X, Y, and Z, thermal
planning is credible, and the correct fans are addressed.

- Plastic and composite X/Y/Z offsets locate each extrusion path.
- Plastic and composite heat-up speeds support timing and preheat planning.
- `Has fan` and fan index identify each tool's controllable cooling output.

An incorrect offset is a collision and placement risk. Measure and validate it
with dedicated registration tests.

## Printer Profile: Thermal and Timing

**What:** records bed and chamber heat-up rates plus the firmware motion-buffer
capacity used in planning and estimates.

**Use it when:** commissioning the machine or correcting consistently wrong
thermal/time estimates.

**Desired result:** estimates and staged operations match observed machine
behavior without overrunning the controller's intended motion capacity.

- Bed and chamber heat-up speeds are measured rates.
- Motion-block buffer size is a firmware capability value.

These are **profile-contract fields**, not speed-tuning shortcuts.

<!-- pdf:page-break-before -->

## Printer Profile: Cut and Contact

**What:** defines cutter travel, restart feed, nozzle clearance, lane roles, and
the commands surrounding cutting and fiber tool changes.

**Use it when:** commissioning, repairing, or formally updating FibreSeek
hardware behavior.

**Desired result:** reliable cut/restart cycles, collision-free placement, and
correct state transitions.

- `Fiber cut distance` must match the cutter mechanism.
- `Fiber restart length` restores fiber after a cut.
- Normal and extended nozzle contact radii reserve clearance around the physical
  placement tool.
- `Fiber slot roles` maps lanes to plastic, composite, or fiber roles.
- Cut G-code and before/after-toolchange G-code are machine commands.
- `Fiber machine contract` is serialized capability data.

Every field in this group is a **profile-contract field**. Review custom G-code
line by line and prove changes on a safe commissioning artifact.

## Printer Profile: Continuous Fiber Lane

**What:** identifies the reinforcement loaded in the machine lane independently
of the process strategy.

**Use it when:** associating a physical lane with a material record.

**Desired result:** the machine lane, filament preset, estimates, and exported
metadata all refer to the same fiber.

- Name, type, material kind, source material ID, diameter, and linear density
  define the lane contents.

## TinmanX1 Wave Overhangs

Wave Overhangs are another TinmanX1-only strength/support tool, but they are not
a fiber feature. Their complete group-by-group guide is in the [Support
tab](15-support-tab.md#wave-overhangs). Keep the two systems conceptually
separate: wave paths try to support geometry during printing; continuous fiber
routes try to reinforce the finished part.

## Fiber Validation Gate

Before releasing a fiber profile:

1. Confirm the machine contract and tool offsets against the physical printer.
2. Confirm material identity and conditioning.
3. Preview every reinforced layer, route start, cut, restart, hole, and narrow
   region.
4. Verify minimum radius, minimum route length, and contact clearance.
5. Print a disposable placement coupon before a valuable part.
6. Section or destructively test representative samples when strength matters.
7. Save the project, final G-code, profile revisions, and exact TinmanX1 commit.

Return to the [settings reference overview](11-orca-tinmanx1-settings-reference.md)
or continue with [Validation and Profile Release](09-validation.md).
