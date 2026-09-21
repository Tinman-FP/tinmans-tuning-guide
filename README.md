<p align="center">
  <img src="assets/tinmans-tuning-guide-cover.png"
       alt="Tinmans Tuning Guide encircling the TinmanX1 thumbnail logo"
       width="100%">
</p>

# Tinmans Tuning Guide

A source-backed, printer-neutral handbook for building reliable FFF/FDM
filament profiles.

This guide explains what to tune, why the order matters, how to read each test,
and how to preserve evidence so a good profile can be reproduced instead of
rediscovered. It is written for ordinary Cartesian, CoreXY, delta, bedslinger,
direct-drive, Bowden, single-tool, and multi-tool printers. Slicer and firmware
names vary, but the physical problems are the same.

## Start Here

If the printer is mechanically sound and the filament is dry, use this order:

1. [Define the baseline](guide/01-foundations.md).
2. [Condition the filament and tune temperature](guide/02-conditioning-and-temperature.md).
3. [Find a safe maximum volumetric flow](guide/03-volumetric-flow.md).
4. [Tune pressure or linear advance](guide/04-pressure-advance.md).
5. [Tune global and feature-specific flow](guide/05-flow-ratio.md).
6. [Balance cooling, bridges, and retraction](guide/06-cooling-and-retraction.md).
7. [Correct dimensions and fit](guide/07-dimensional-accuracy.md).
8. [Refine seams and surfaces](guide/08-seams-and-surfaces.md).
9. [Validate and release the profile](guide/09-validation.md).

For a symptom-first route, use the [diagnostic matrix](guide/diagnostic-matrix.md).
For unfamiliar terms, use the [glossary](guide/glossary.md).

## The Short Version

```mermaid
flowchart TD
    A[Machine baseline] --> B[Dry and identify filament]
    B --> C[Temperature]
    C --> D[Maximum volumetric flow]
    D --> E[Pressure or linear advance]
    E --> F[Global flow ratio]
    F --> G[Cooling and bridges]
    G --> H[Retraction and travel]
    H --> I[Dimensions and tolerances]
    I --> J[Seams and surfaces]
    J --> K[Representative validation print]
```

Later tests depend on earlier ones. A temperature change can alter melt flow,
pressure response, stringing, and layer adhesion. A pressure-advance change can
alter corners and seams. Dimensional compensation should therefore come after
the extrusion system is stable.

## Four Rules That Prevent Most Tuning Mistakes

1. Change one causal variable at a time after any broad search.
2. Keep a control sample and record the complete conditions.
3. Tune extrusion quality before dimensional compensation.
4. Use the setting that matches the error model.

That fourth rule is crucial:

- Use flow ratio to correct how much material is deposited.
- Use pressure advance to correct pressure lag during speed changes.
- Use shrinkage compensation for proportional cooled-part scale error.
- Use contour or hole compensation for near-constant offsets.
- Use elephant-foot compensation only for enlarged bottom layers.
- Do not alter axis calibration to hide filament shrinkage.

## What This Guide Does Not Promise

There is no universal best temperature, flow ratio, retraction distance, or
pressure-advance value. The result depends on the exact filament, color, lot,
moisture state, nozzle, hotend, extruder, layer geometry, speed, acceleration,
cooling, and chamber conditions. This guide provides a method for finding and
defending a value for a defined setup.

## Safety

- Treat hotends, beds, chambers, and freshly printed parts as burn hazards.
- Keep hands, tools, hair, and clothing clear of moving machinery.
- Follow the filament manufacturer's safety data and ventilation guidance.
- Do not leave an unproven material or profile unattended.
- Some materials release irritating or hazardous emissions. Use suitable local
  exhaust or enclosure ventilation for the material and environment.
- Dry filament only within the limits of its spool, packaging, and manufacturer.

## Repository Contents

| File | Purpose |
| --- | --- |
| [How to use this guide](guide/00-how-to-use-this-guide.md) | Test design, evidence, and decision rules |
| [Foundations](guide/01-foundations.md) | Mechanical and slicer baseline |
| [Conditioning and temperature](guide/02-conditioning-and-temperature.md) | Moisture, temperature towers, adhesion |
| [Volumetric flow](guide/03-volumetric-flow.md) | Melt-capacity ceiling and speed conversion |
| [Pressure advance](guide/04-pressure-advance.md) | Pressure lag, test reading, firmware notes |
| [Flow ratio](guide/05-flow-ratio.md) | Global and feature-specific extrusion |
| [Cooling and retraction](guide/06-cooling-and-retraction.md) | Cooling tradeoffs, bridges, travel artifacts |
| [Dimensional accuracy](guide/07-dimensional-accuracy.md) | Scale, offsets, holes, elephant foot |
| [Seams and surfaces](guide/08-seams-and-surfaces.md) | Seam diagnosis and surface refinement |
| [Validation](guide/09-validation.md) | Acceptance tests and profile release |
| [Material families](guide/10-material-families.md) | Material-specific starting priorities |
| [Diagnostic matrix](guide/diagnostic-matrix.md) | Symptom-to-cause triage |
| [Glossary](guide/glossary.md) | Definitions and formulas |
| [Experiment log](templates/experiment-log.md) | Reusable test record |
| [Release checklist](templates/profile-release-checklist.md) | Final profile audit |
| [Sources](SOURCES.md) | Primary references and further reading |
| [Credits](CREDITS.md) | Attribution and authorship |

## Evidence Standard

Every accepted value should have:

- a dated experiment record;
- the exact printer, tool, nozzle, material, and filament condition;
- the exact project or sliced G-code;
- a list of fixed variables and the one changed variable;
- photographs in a repeatable orientation;
- measurements taken after the part fully cooled;
- an explicit decision: `candidate`, `accepted`, `rejected`, or `superseded`.

The [experiment template](templates/experiment-log.md) is designed for this.

## License and Attribution

The original text and diagrams in this repository are licensed under
[CC BY 4.0](LICENSE). Source projects retain their own licenses. See
[CREDITS.md](CREDITS.md) and [SOURCES.md](SOURCES.md) for attribution.

Project initiated and experimentally informed by William Tinney. Researched,
written, organized, and published with Codex by OpenAI. No source author,
project, or company listed here has endorsed this guide.
