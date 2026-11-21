# Material-Family Priorities

These notes describe common tendencies, not fixed settings. Formulations vary
widely. Start with the manufacturer's current limits and safety information,
then use the same calibration workflow. Where the guide's own runs tuned a
material, the results are given as examples of a finished tune on one setup,
never as values to copy.

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
- balance cooling against layer bonding: keep the normal fan low and use the
  overhang and bridge fan for geometry;
- bracket temperature high enough to find the true optimum at production flow;
- expect sticky buildup on the nozzle to create blobs and scars.

If a temperature tower keeps improving at the hottest section, the optimum has
not been bracketed. Extend the range within manufacturer limits and include a
[bond check](02-conditioning-and-temperature.md#a-simple-bond-check). If it
keeps improving at the coolest section, do not go below the maker's minimum;
check bonding instead.

**Field results, 3D-Fuel Pro PCTG** (maker: `250-280 C`, low fan, hardened
nozzle recommended):

| Printer, nozzle | Temperature | MVS | PA | Flow | Notes |
| --- | --- | --- | --- | --- | --- |
| K2 Plus, `0.6 mm` hardened | `245 C` | `32` | `0.026` | `0.9476` | stringing and bridge sag rose with every hotter band |
| CORE One+ INDX, `0.4 mm` high-flow | `250 C` | `19` | `0.055` | `1.00` | normal fan `10-15 %`; chamber pre-warmed; shrinkage XY `99.6 %` |
| CORE One L+, `0.6 mm` high-flow | `250 C` | `27` | `0.035` | `0.97` | MVS set by a firmware warning |
| Qidi Plus4, `0.6 mm` hardened | `255 C` | `28` | `0.032` | `0.9875` | chamber `45 C` |

Every one of these chose a temperature at the cool end of, or below, the
maker's range, because stringing and bridge sag rose with temperature while
bonding stayed good. That is a pattern worth knowing, not a rule: confirm
bonding before accepting a cool temperature.

## ABS and ASA

Priorities:

- stable enclosure and chamber conditions;
- controlled drafts and conservative cooling;
- bed adhesion and heat soak;
- dimensional shrinkage after extrusion is tuned;
- ventilation appropriate for the material.

Warping, corner lift, and layer splitting are usually thermal-management
problems before they are flow problems.

**Field result, Push Plastic ABS on a Snapmaker U1** (`0.4 mm`, chamber
`50 C`): `240 C`, MVS `26`, PA `0.026`, flow `0.95`, overhang and bridge fan
`70 %` (normal fan at most `20 %`), Shrinkage (XY) `99.60 %`. The temperature
tower showed the same stringing in every band and a matte surface at
`225-230 C`, so `240 C` was taken from the middle of the clean range.

<!-- pdf:page-break-before -->

## Polycarbonate and PC Blends

Priorities:

- very dry filament;
- suitable high-temperature hardware and build surface;
- stable warm chamber when recommended;
- low uncontrolled cooling;
- strength validation at the intended flow rate.

Check the entire filament path and spool temperature rating before drying or
printing at high temperature. Check the printer's real bed limit, too: on a
Qidi Plus4, a `130 C` bed setting shut the printer's controller down twice,
so its PC profile uses `120 C`, with part cooling off and a `55 C` chamber.

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

**Nozzle size decides small-feature quality.** Carbon-filled PET (PET-CF) on a
`0.6 mm` hardened nozzle printed clean walls but left fine whiskers on every
feature narrower than about two nozzle widths, whatever the temperature, fan
or retraction. A `0.4 mm` hardened nozzle removed them. For filled materials,
`0.4 mm` hardened is a practical minimum; `0.6 mm` is more forgiving of clogs
but cannot draw fine features.

**Fibre texture hides small differences.** On PET-CF, PA tests and seam-gap
tests showed no visible change across their whole range. Choosing the lowest
value (PA `0`) or a middle value (seam gap `15 %`) and moving on was the right
call.

**Field result, Elegoo PET-CF on a Qidi Plus4** (`0.6 mm`, chamber `50 C`):
`275 C`, flow `1.04`, PA `0`, MVS `19` (no limit reached), retraction
`0.4 mm`, normal fan `20 %`, overhang fan `100 %`, XY contour compensation
`-0.13 mm`. The `0.4 mm` profile reuses these values with MVS capped at
`10`, which is recorded in its notes as inherited, not re-tested.

## Support and Soluble Materials

Priorities:

- moisture control;
- reliable tool-change purge and priming;
- interface temperature compatibility;
- idle-temperature and ooze management;
- storage and post-processing safety.

Validate the complete material pair, not each filament in isolation.

**Watch the bed temperature on mixed plates.** Many printer profiles set the
bed from the hottest filament used on the plate. On a Snapmaker U1, an ABS
support material set a `105 C` bed under a PCTG part whose own setting was
`80 C`, for ten hours, and the body lifted from the plate (the bed was never
proven to be the cause). The fix was a support profile
with an `80 C` bed and, for PCTG, HIPS as the support material instead of an
ABS-based support. Check the bed temperature in the G-code of any job that
mixes materials.

**HIPS with PCTG** is a convenient pair: HIPS printed around `240 C` with a
low MVS (`8 mm³/s`) and an `80 C` bed in the U1 run, and a long multi-tool tray
completed with it. The pairing was still a candidate when this edition was
written; check that the HIPS on the bed stays down at your bed temperature.
