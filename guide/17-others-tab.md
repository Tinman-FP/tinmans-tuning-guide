# Others Tab

The groups below are **Shared 2.4.2**. They collect adhesion aids, special
slicing modes, texture, output controls, scripts, and notes. Several can change
machine behavior far beyond appearance, so preview and validate them carefully.

## Skirt

**What:** prints one or more lines around the part without attaching them to it.

**Use it when:** the nozzle needs priming, first-layer behavior needs a visual
check, or a simple draft shield is useful.

**Desired result:** stable extrusion before the part starts, with no wasted
height or collision risk.

- Loops and minimum extrusion length control priming quantity.
- Type chooses combined or per-object skirts.
- Distance and start angle place the path.
- Speed and height control deposition and vertical extent.
- Draft shield and single-loop-after-first-layer turn the skirt into a thermal
  barrier.

## Brim

**What:** attaches sacrificial first-layer roads to the part or selected corners
to increase bed contact.

**Use it when:** corners lift or a narrow footprint needs more holding force.

**Desired result:** the part stays flat and the brim removes without damaging
the edge.

- Type chooses automatic, ears, painted, outer, inner, both, or none.
- Width controls adhesion area.
- Object gap trades holding force for removability.
- Flow ratio adjusts brim deposition independently.
- Elephant-foot outline use makes the brim follow the compensated first-layer
  contour.
- Combine brims joins nearby objects.
- Ear angle and detection length decide which corners receive ears.

A brim cannot correct oil, debris, a bad Z offset, or severe enclosure drafts.

## Special Mode

**What:** changes how geometry is interpreted and how objects or layers are
ordered.

**Use it when:** the model has unusual mesh topology, needs sequential printing,
or is intentionally a single-wall spiral.

**Desired result:** a valid, collision-free toolpath whose special behavior is
visible and understood in preview.

- `Slicing mode` chooses regular, even-odd, or close-holes interpretation.
- `Print sequence` chooses by-layer or by-object printing.
- `Print order` chooses the intra-layer object order.
- `Spiral vase` removes ordinary seams by continuously raising a single wall.
- Spiral smoothing, maximum XY smoothing, and start/finish flow ratios shape the
  transition into and out of the spiral.
- `Timelapse` changes park/motion behavior for image capture.
- `Wrapping detection` enables the supported wrap/clump detection workflow.

Sequential printing requires verified toolhead and gantry clearance. A safe
bed layout is part of the setting, not an afterthought.

## Fuzzy Skin

**What:** perturbs exterior paths to create intentional texture.

**Use it when:** texture is a design choice, improves grip, or masks small
surface variations that are already understood.

**Desired result:** controlled, repeatable texture without dimensional loss at
fits, holes, or first-layer edges.

- Scope chooses which surfaces receive texture.
- Mode chooses displacement, extrusion variation, or both.
- Noise type, feature scale, octaves, and persistence shape the texture.
- Point distance and thickness control frequency and amplitude.
- Ripple count, offset, and layers between offsets create organized variation.
- First-layer application extends texture to the bed-contact layer.

Do not use fuzzy skin as evidence that an underlying extrusion defect is fixed.

## G-code Output

**What:** controls output verbosity, object labeling, cancellation metadata,
filenames, and some retraction reduction.

**Use it when:** the printer, host, or post-processing workflow needs specific
metadata or file organization.

**Desired result:** compatible, traceable G-code that preserves the controls
required by the receiving system.

- `Reduce infill retraction` avoids some unnecessary internal retracts.
- Line numbers and comments aid certain workflows but increase file size.
- Object labels and exclude-object metadata enable supported per-object control.
- Filename format builds traceable names from placeholders.

Open a sample output and verify the actual header and commands before relying on
metadata for automation.

## Change Extrusion Role G-code

**What:** runs custom commands when the slicer changes feature role.

**Use it when:** an advanced, validated machine workflow genuinely requires a
role transition command.

**Desired result:** deterministic commands at the intended transitions, with no
unsupported firmware instructions or unsafe state changes.

Most filament tuning does not need this field. Treat pasted G-code as machine
control software and review it line by line.

## Post-processing Scripts

**What:** sends completed G-code through external programs.

**Use it when:** a documented workflow must transform, validate, sign, or route
the output after slicing.

**Desired result:** reproducible transformed output, preserved safety commands,
and a visible failure if the script cannot complete.

Scripts can silently change the file after preview. Archive both the source
project and final sent G-code.

## Notes

**What:** stores human-readable profile context.

**Use it when:** recording assumptions, calibration date, material lot,
dependencies, or warnings that numbers alone cannot express.

**Desired result:** another operator can understand why the profile exists and
what must be revalidated before reuse.

Continue with [TinmanX1 Fiber and Strength Tools](18-tinmanx1-fiber-and-strength-tools.md).
