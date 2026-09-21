# Material-Family Priorities

These notes describe common tendencies, not fixed settings. Formulations vary
widely. Start with the manufacturer's current limits and safety information,
then use the same calibration workflow.

## PLA and PLA Blends

Priorities:

- avoid excessive chamber heat and heat creep;
- provide enough cooling for overhangs and small features;
- verify high-flow strength rather than judging appearance alone;
- retest filled, silk, matte, foaming, and impact-modified products separately.

Silk and filled PLA can require different flow, temperature, PA, and MVS from a
plain PLA of the same brand.

## PETG and PCTG

Priorities:

- dry thoroughly before blaming retraction for strings;
- avoid excessive nozzle squish on the first layer;
- balance cooling against layer bonding;
- bracket temperature high enough to find the true optimum at production flow;
- expect sticky buildup on the nozzle to create blobs and scars.

If a temperature tower keeps improving at the hottest section, the optimum has
not been bracketed. Extend the range within manufacturer limits and include a
strength comparison.

## ABS and ASA

Priorities:

- stable enclosure and chamber conditions;
- controlled drafts and conservative cooling;
- bed adhesion and heat soak;
- dimensional shrinkage after extrusion is tuned;
- ventilation appropriate for the material.

Warping, corner lift, and layer splitting are usually thermal-management
problems before they are flow problems.

<!-- pdf:page-break-before -->

## Polycarbonate and PC Blends

Priorities:

- very dry filament;
- suitable high-temperature hardware and build surface;
- stable warm chamber when recommended;
- low uncontrolled cooling;
- strength validation at the intended flow rate.

Check the entire filament path and spool temperature rating before drying or
printing at high temperature.

## Nylon and Polyamide Blends

Priorities:

- strict moisture control and printing from a dry enclosure;
- nozzle wear for filled grades;
- dimensional conditioning after printing;
- creep, flexibility, and functional-fit validation;
- conservative MVS for highly filled formulations.

Nylon can change dimensions as it absorbs moisture. Define when dimensions are
measured and the expected service humidity.

## TPU and Other Flexible Materials

Priorities:

- low-resistance filament path and controlled extruder tension;
- conservative speed and volumetric flow;
- minimal necessary retraction;
- PA tuned specifically for the material and path;
- dimensional tests under relaxed, uncompressed conditions.

Hardness alone does not define print behavior. Different TPU chemistries with
the same Shore rating can need different profiles.

<!-- pdf:page-break-before -->

## Fiber-, Metal-, Wood-, and Mineral-Filled Materials

Priorities:

- manufacturer-required nozzle hardness and minimum diameter;
- nozzle wear tracking;
- reduced clog risk and suitable retraction;
- MVS testing rather than relying on the unfilled base polymer;
- ventilation and handling appropriate to the filler;
- dimensional validation because fillers alter shrinkage and anisotropy.

The base-polymer profile is only a starting point.

## Support and Soluble Materials

Priorities:

- moisture control;
- reliable tool-change purge and priming;
- interface temperature compatibility;
- idle-temperature and ooze management;
- storage and post-processing safety.

Validate the complete material pair, not each filament in isolation.
