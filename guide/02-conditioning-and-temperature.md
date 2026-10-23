# Filament Conditioning and Temperature

Temperature tuning is meaningful only when the material condition is stable.
Water in filament can create defects that resemble poor temperature, flow,
retraction, or pressure advance.

When upgrading the slicer, record the temperature tower's generated geometry
and nozzle-scaling options. See [version-specific generator changes](21-slicer-upgrades-and-calibration-changes.md#temperature-and-vfa)
before comparing new towers with older specimens.

## Moisture Symptoms

Possible signs include:

- popping, crackling, or visible vapor at the nozzle;
- rough, foamy, or inconsistent extrusion;
- bubbles, pits, blobs, or smoke-like wisps;
- excessive stringing despite reasonable retraction;
- weak or brittle layers;
- an unstable surface finish from layer to layer.

These signs are not individually conclusive, but drying is the correct first
experiment when storage history is unknown.

## Drying Safely

Use the filament manufacturer's recommendation when available. Confirm that the
spool and any label, bag, RFID tag, or hub can tolerate the dryer temperature.
Prusa's drying table is a useful cross-check, not permission to exceed a product
limit.

Record:

- dryer type and measured temperature;
- drying duration;
- spool starting condition;
- time between drying and printing;
- whether the spool remained in a dry box during the test.

## Controlled PET-CF Drying Comparison

The photographs below compare Elegoo PET-CF printed from the same G-code on
the same Qidi Plus 4, nozzle, settings, and room conditions. The operator
reported the left tower as undried and the right tower as dried. The dried
specimen has markedly cleaner bridges, fewer loose strands, more coherent
overhangs, and a more uniform surface. This is a controlled A/B result for one
spool and process, not a universal drying schedule.

![Elegoo PET-CF temperature-tower comparison. In every paired view, the undried specimen is on the left and the dried specimen is on the right. Same G-code, printer, nozzle, settings, and room conditions. Field photographs by William Tinney, 2026.](../assets/field-tests/elegoo-pet-cf-dry-vs-undried-overview.jpg)

The comparison is also a useful diagnostic warning: moisture can produce
defects that look like excessive temperature, poor retraction, weak bridging,
or unstable flow. Dry and stabilize the spool before changing several slicer
variables to chase those symptoms.

## What Nozzle Temperature Changes

Higher temperature generally lowers melt viscosity and can improve high-flow
extrusion and layer bonding. It can also increase ooze, stringing, gloss,
degradation, and loss of small-feature definition.

Lower temperature may sharpen details and reduce ooze, but can cause poor
bonding, incomplete melting, high backpressure, skipped extrusion, or a matte
under-extruded surface.

The useful temperature therefore depends on flow rate and purpose. A slow
display print and a fast structural print may need different values.

## Design a Temperature Tower

1. Begin inside the manufacturer's safe range.
2. Use steps large enough to reveal a trend, commonly `5 C`.
3. Keep layer height, width, speed, cooling, and geometry fixed.
4. Verify in G-code preview or text that temperature commands occur at the
   intended heights.
5. Label each segment in the model or experiment record.
6. Include a range above and below the expected optimum when safe.

A tower does not identify an optimum if the best section is at the hottest or
coldest tested endpoint. Extend the range in that direction.

An endpoint is not a winner merely because one face looks smoother. First
check all repeated features and exclude temperature-transition layers. Do not
extend a range when every tier retains the same unresolved failure.

## Read the Tower

Evaluate every segment for:

- consistent walls and surface finish;
- overhang edge definition and curl;
- bridge sag and strand coherence;
- stringing and wisps;
- small-feature and text fidelity;
- corner quality and seams;
- discoloration or signs of degradation;
- layer adhesion after cooling.

Photographs are useful for appearance, but they cannot prove layer strength.
Use a controlled bend or break comparison when adhesion matters. Keep geometry
and loading consistent and use eye protection.

### When Every Temperature Retains the Defect

![Unresolved deposition example, not a temperature selection. This tower runs bottom to top 285, 280, 275, 270 and 265 C, with a separate 275 C first layer. Rough tracks and feature-edge discontinuities recur across bands. Photograph: William Tinney, IMG_6237, 2026-10-22. Native Tinman/OrcaSlicer calibration geometry; contributor credits are in CREDITS.](../assets/field-tests/pet-cf-temperature-unresolved.jpg)

This Qidi Plus4 / CM2 0.6 mm / Elegoo PET-CF example used stock-size native
geometry, 0.24 mm body layers, 0.30 mm first layer, flow 1.00, PA 0,
3 mm3/s diagnostic cap, 100 C bed and 50 C chamber target. Main cooling was
20% after the first three layers. The five body bands occupied layers
2-42, 43-84, 85-125, 126-167 and 168-208, respectively, not fixed 25-layer
steps. Reported temperatures followed the commands after transitions, but
fine tracks remained defective across the range. Height, time and repeated
feature geometry remain confounds; no temperature was accepted from this test.

Do not turn a generic moisture symptom list into a diagnosis. Wet filament
can cause roughness, pits, inconsistent extrusion and stringing, but those
observations overlap with delivery, toolpath and thermal/cooling faults.
Organized bands or defects that recur at the same feature transitions warrant
mapping to the emitted paths, layer timing, speed/width/flow and retract/restart
events. A sensor near the heater does not measure melt throughput, and an
upstream diameter sensor does not measure deposited volume.

Record actual conditioning history before deciding whether a drying A/B is
informative. In this case the owner reported new filament kept in a Creality
Pi dryer for four days, with a 65 C setting and humidity-triggered heater
cycling at 18% RH. That is useful history, not a continuous 24-hour heat soak
or a measurement of filament moisture. Conversely, a recipe mismatch alone
does not prove the defects are moisture-caused.

The [Elegoo PET-CF specification](https://www.elegoo.com/products/pet-cf),
reviewed 2026-10-22, gives 80 +/- 5 C for 8 hours, with drying before use.
Only use that schedule in a dryer and spool rated for it; do not defeat
temperature limits. A documented conditioning comparison can test a moisture
hypothesis, but a negative result must redirect diagnosis rather than trigger
endless drying or temperature sweeps. If suitable conditioning is already
verified, preserve it and test another supported hypothesis.

If no tier resolves the failure, stop the sweep. Audit the exact failed paths
and the machine/deposition baseline, then define a small, controlled test with
an explicit discriminating outcome. Do not advance automatically to MVS, PA,
flow or cosmetic retraction tuning. This is a return to the earliest affected
prerequisite, not a requirement to repeat every previously valid check.

## Selection Rule

Choose the lowest temperature that provides the required adhesion and stable
flow at the intended production rate, unless a hotter setting produces a
materially better mechanical result with acceptable detail and stringing.

For high-flow work, confirm the selected temperature again during the
volumetric-flow test. A visually good low-speed tower section may not melt fast
enough for production.

### Preserve Margin Above a Cold-Flow Failure

The dried Elegoo PET-CF tower below ran from `265 C` at the bottom through
`260 C`, `255 C`, and `250 C`. Two attempts stopped at approximately the same
point as the program moved toward the next, colder step. After cancellation,
the same filament path extruded `300 mm` normally after the nozzle was heated
to `300 C`. That result is consistent with insufficient melt capacity at the
low-temperature endpoint rather than a persistent clog.

![Dried Elegoo PET-CF tower details after removal from the plate. The repeated tower stopped below the completed 250 C tier; the 255 C tier provides the best balance of surface quality and temperature margin for the next controlled tests. Field photographs by William Tinney, 2026.](../assets/field-tests/elegoo-pet-cf-dried-tower-detail.jpg)

For this machine, `0.6 mm` nozzle, and test flow, `255 C` is the defensible
working selection. The `250 C` tier is visually competitive, but it is only one
`5 C` step above the repeatable loss-of-flow boundary. The `255 C` tier retains
clean walls, readable detail, and acceptable bridge behavior while preserving
process margin. Treat that value as a test-specific starting point and confirm
it again at the intended production volumetric flow.

This is a historical, setup-specific result, not a qualified temperature for
every later hotend/nozzle/profile revision. It is below the 260-290 C range
listed on Elegoo's current PET-CF product page reviewed 2026-10-22. Do not
silently transfer it to a new setup or use it to override the manufacturer's
current limits.

## First-Layer Temperature

A hotter first layer can improve wetting and reliability, but it is a separate
setting from normal-layer temperature. Excess heat can increase ooze, elephant
foot, or polymer degradation. Tune it only after Z offset and plate preparation
are correct.

## Common Misreads

| Observation | Do not assume | Check |
| --- | --- | --- |
| Stringing | temperature is too high | moisture, travel, retraction, nozzle residue |
| Matte upper tower | temperature is too low | whether flow rate also increases with height |
| Weak bridge | temperature alone is wrong | bridge fan, speed, flow, line width |
| Rough surface | over-extrusion | wet filament, partial clog, unstable temperature |
| Best result at endpoint | endpoint is optimum | extend the range safely |

Once temperature is bracketed, find the system's usable
[volumetric-flow limit](03-volumetric-flow.md).
