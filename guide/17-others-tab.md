# Others Tab

> **At a glance**
> - **Decide:** skirt, brim, special modes and output options
> - **Test:** the part that needs them
> - **Keep:** only what the part needs

The groups below are **Shared 2.4.2**. They collect adhesion aids, special
slicing modes, texture, output controls, scripts, and notes. Several can change
machine behavior far beyond appearance, so preview and validate them carefully.

## Skirt

| This group | |
| --- | --- |
| **What it controls** | Prints one or more lines around the part without attaching them to it. |
| **Change it when** | The nozzle needs priming, first-layer behavior needs a visual check, or a simple draft shield is useful. |
| **Aim for** | Stable extrusion before the part starts, with no wasted height or collision risk. |

| Control | What it does |
| --- | --- |
| Loops and minimum extrusion length | Control priming quantity. |
| Type | Chooses combined or per-object skirts. |
| Distance and start angle | Place the path. |
| Speed and height | Control deposition and vertical extent. |
| Draft shield and single-loop-after-first-layer | Turn the skirt into a thermal barrier. |

## Brim

| This group | |
| --- | --- |
| **What it controls** | Attaches sacrificial first-layer roads to the part or selected corners to increase bed contact. |
| **Change it when** | Corners lift or a narrow footprint needs more holding force. |
| **Aim for** | The part stays flat and the brim removes without damaging the edge. |

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

| This group | |
| --- | --- |
| **What it controls** | Changes how geometry is interpreted and how objects or layers are ordered. |
| **Change it when** | The model has unusual mesh topology, needs sequential printing, or is intentionally a single-wall spiral. |
| **Aim for** | A valid, collision-free toolpath whose special behavior is visible and understood in preview. |

| Control | What it does |
| --- | --- |
| `Slicing mode` | Chooses regular, even-odd, or close-holes interpretation. |
| `Print sequence` | Chooses by-layer or by-object printing. |
| `Print order` | Chooses the intra-layer object order. |
| `Spiral vase` | Removes ordinary seams by continuously raising a single wall. |
| Spiral smoothing, maximum XY smoothing, and start/finish flow ratios | Shape the transition into and out of the spiral. |
| `Timelapse` | Changes park/motion behavior for image capture. |
| `Wrapping detection` | Enables the supported wrap/clump detection workflow. |

Sequential printing requires verified toolhead and gantry clearance. A safe
bed layout is part of the setting, not an afterthought.

## Fuzzy Skin

| This group | |
| --- | --- |
| **What it controls** | Perturbs exterior paths to create intentional texture. |
| **Change it when** | Texture is a design choice, improves grip, or masks small surface variations that are already understood. |
| **Aim for** | Controlled, repeatable texture without dimensional loss at fits, holes, or first-layer edges. |

- Scope chooses which surfaces receive texture.
- Mode chooses displacement, extrusion variation, or both.
- Noise type, feature scale, octaves, and persistence shape the texture.
- Point distance and thickness control frequency and amplitude.
- Ripple count, offset, and layers between offsets create organized variation.
- First-layer application extends texture to the bed-contact layer.

Do not use fuzzy skin as evidence that an underlying extrusion defect is fixed.

## G-code Output

| This group | |
| --- | --- |
| **What it controls** | Controls output verbosity, object labeling, cancellation metadata, filenames, and some retraction reduction. |
| **Change it when** | The printer, host, or post-processing workflow needs specific metadata or file organization. |
| **Aim for** | Compatible, traceable G-code that preserves the controls required by the receiving system. |

- `Reduce infill retraction` avoids some unnecessary internal retracts.
- Line numbers and comments aid certain workflows but increase file size.
- Object labels and exclude-object metadata enable supported per-object control.
- Filename format builds traceable names from placeholders.

Open a sample output and verify the actual header and commands before relying on
metadata for automation.

## Change Extrusion Role G-code

| This group | |
| --- | --- |
| **What it controls** | Runs custom commands when the slicer changes feature role. |
| **Change it when** | An advanced, validated machine workflow genuinely requires a role transition command. |
| **Aim for** | Deterministic commands at the intended transitions, with no unsupported firmware instructions or unsafe state changes. |

Most filament tuning does not need this field. Treat pasted G-code as machine
control software and review it line by line.

## Post-processing Scripts

| This group | |
| --- | --- |
| **What it controls** | Sends completed G-code through external programs. |
| **Change it when** | A documented workflow must transform, validate, sign, or route the output after slicing. |
| **Aim for** | Reproducible transformed output, preserved safety commands, and a visible failure if the script cannot complete. |

Scripts can silently change the file after preview. Archive both the source
project and final sent G-code.

## Notes

| This group | |
| --- | --- |
| **What it controls** | Stores human-readable profile context. |
| **Change it when** | Recording assumptions, calibration date, material lot, dependencies, or warnings that numbers alone cannot express. |
| **Aim for** | Another operator can understand why the profile exists and what must be revalidated before reuse. |

Continue with [TinmanX1 Fiber and Strength Tools](18-tinmanx1-fiber-and-strength-tools.md).
