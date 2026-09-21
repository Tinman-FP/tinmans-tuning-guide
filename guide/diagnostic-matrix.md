# Diagnostic Matrix

Use this table to select the first controlled experiment. It does not replace
inspection of the machine baseline.

| Symptom | First suspects | Check next | Avoid changing first |
| --- | --- | --- | --- |
| Open top channels, clean walls | top flow, top width, top speed | shell thickness, infill support | axis scale |
| Rough ridged top everywhere | global/top flow high | PA, first-layer carry-through | shrinkage |
| Thin or missing lines at high speed | MVS, temperature, partial clog | extruder grip, spool drag | dimensional compensation |
| Consistent under-extrusion at all speeds | flow ratio, diameter, obstruction | rotation distance, nozzle | cooling alone |
| Bulged non-seam corners | PA low | acceleration, wall order | global flow alone |
| Starved approach to corners | PA high | flow transitions, MVS | retraction alone |
| One vertical scar | seam transition | PA, retraction, wipe, gap | whole-model flow |
| Ringing after corners | input shaping, belts, rigidity | acceleration | flow ratio |
| Random pits or bubbles | moisture, contamination | temperature, nozzle debris | seam placement |
| Fine hairs everywhere | moisture, temperature | retraction, travel | dimensions |
| Thick strings between features | retraction, travel time, ooze | temperature, wipe | cooling alone |
| Gap after travel | retraction too high, restart | PA, clog, spool drag | more retraction |
| Weak layers | temperature, moisture, excess cooling | production flow, chamber | seam settings |
| ABS/ASA warp or split | chamber, drafts, bed adhesion | fan, geometry, heat soak | axis steps |
| Poor bridge with good walls | bridge flow/speed/fan | bridge PA, line width | global flow first |
| Curling overhang edge | cooling, speed, temperature | wall order | shrinkage |
| Uniform proportional XY error | material shrinkage | larger artifact, both axes | contour offset |
| Same external offset at many sizes | contour compensation | PA and flow | material scale |
| Undersized holes only | hole compensation, polyholes | seam, orientation | global XY scale |
| Bottom layers too wide | elephant foot, Z, bed heat | initial-layer flow | whole-part scale |
| X and Y differ | mechanics, squareness, airflow | axis motion, orientation | one shared shrink value |
| Z error grows with height | Z motion or Z material scale | thermal/mechanical repeatability | XY compensation |
| Only first layer fails | Z offset, bed preparation | plate temperature, mesh | global flow |
| Gloss band at speed change | flow/temperature/cooling transition | MVS, acceleration | random seam |
| Repeating horizontal bands | Z mechanics, thermal cycles | spool drag, layer timing | hole compensation |
| Extruder clicks | MVS, temperature, clog, path drag | tension, nozzle, spool | PA cosmetic tuning |
| Good small print, bad large print | chamber, warp, long-flow demand | heat soak, MVS | retraction tower |
| Good calibration, bad real part | test not representative | actual speeds, widths, cooling | arbitrary multiplier |

## Triage Order

When several symptoms appear together:

1. Stop for unsafe motion, thermal faults, collisions, or severe adhesion loss.
2. Check filament dryness and nozzle condition.
3. Confirm machine baseline and active profile.
4. Determine whether the defect is global, feature-specific, speed-dependent,
   directional, layer-dependent, or localized to a seam.
5. Run the smallest test that isolates the leading cause.
6. Preserve the rejected result and change only one causal variable.

## Useful Classifications

- **Global:** appears on every face and feature.
- **Directional:** depends on X/Y face or fan direction.
- **Rate-dependent:** begins at higher speed or flow.
- **Thermal:** changes with layer time, chamber state, or height.
- **Transition-localized:** appears at corners, starts, stops, or seams.
- **Bottom-only:** first-layer/Z/bed interaction.
- **Geometry-specific:** holes, bridges, overhangs, or top surfaces only.

This classification often identifies the correct settings family before a
single value is changed.

