# Foundations: Establish a Trustworthy Baseline

Filament calibration cannot compensate for a loose printer, a partially
blocked nozzle, an unstable bed, or an incorrect tool offset. Prove the machine
first.

## Hardware Checklist

Inspect and record:

- nozzle diameter, material, installation, contamination, and wear;
- hotend assembly, heater, temperature sensor, and fan operation;
- extruder gear cleanliness, tension, alignment, and filament path drag;
- belts, pulleys, fasteners, rails, wheels, bearings, and lubrication;
- build plate type, flatness, attachment, cleanliness, and damage;
- part-cooling duct position and fan response;
- chamber sensors, doors, lids, and exhaust behavior;
- spool path, reverse Bowden tube, buffer, or material changer resistance.

Filled or abrasive materials can enlarge a soft nozzle. A worn nozzle changes
line geometry and may make a formerly valid profile appear over-extruded.

## Firmware and Motion Checklist

Confirm:

- X, Y, Z, and extruder motion calibration are mechanically correct;
- homing and endstop behavior are repeatable;
- bed tramming and mesh probing are valid at the intended temperature;
- the expected mesh and tool offsets are actually loaded;
- input shaping or resonance compensation is appropriate for the machine;
- acceleration and speed limits do not cause skipped steps;
- thermal protection is enabled and temperature control is stable.

Extruder rotation distance or E-steps is a machine relationship between motor
motion and commanded filament feed. Establish it with the extruder operating in
the manufacturer's supported manner. Do not retune it for every spool.

## First Layer

The first layer must be repeatable before material tuning:

- adjacent lines touch without deep ridges;
- the line adheres through corners and direction changes;
- the nozzle does not scrape the plate;
- the bottom is not so compressed that it creates a large elephant foot;
- the plate reaches a stable temperature before probing and printing.

Do not judge global flow from a first layer. First-layer height, Z offset, bed
texture, and initial-layer flow deliberately change its appearance.

## Temperature Stability and Heat Soak

High-temperature materials and large enclosed printers can change as the frame,
bed, chamber, and toolhead warm. Use the same heat-soak procedure for calibration
and production. Record either the soak time or the condition that starts the
print, such as chamber temperature and bed stability.

## Slicer Baseline

Create or duplicate a known working printer profile. Record:

- slicer name and exact version;
- firmware flavor and machine limits;
- tool and nozzle assignment;
- layer height and line widths;
- speed and acceleration by feature;
- wall generator and wall order;
- seam strategy;
- top/bottom layers and surface pattern;
- cooling and minimum-layer-time behavior;
- any start G-code that changes mesh, offsets, PA, flow, or temperature.

Calibration generators can leave temporary overrides in a project. Start a
fresh project after using them and verify the resulting G-code.

## Filament Identity

Give each profile a precise identity:

```text
Manufacturer / product / material / color / diameter / lot / date opened
```

Colorants and additives can change flow, temperature, and cooling behavior.
Treat a different color or lot as unverified until a short confirmation print
passes.

## Baseline Acceptance Print

Before advanced tuning, print a simple artifact that includes:

- a broad wall;
- a top surface;
- a short bridge;
- an overhang;
- a seam or repeated corner;
- a known external dimension.

The purpose is not perfection. It confirms that the printer can complete a
controlled test and reveals obvious mechanical or thermal faults.

Proceed to [Conditioning and Temperature](02-conditioning-and-temperature.md).

