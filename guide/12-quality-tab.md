# Quality Tab

> **At a glance**
> - **Decide:** which Quality group (layers, widths, seams, precision, walls, bridges, overhangs) fits the defect
> - **Test:** the "Change it when" row of each group
> - **Keep:** defaults unless a print shows the matching symptom

**Version note:** every group below is **Shared 2.4.2**. Source comparison found
no TinmanX1-only Quality controls in the stated baseline. TinmanX1 adds related
tools elsewhere, especially [Strength Lens, fiber planning, and Wave
Overhangs](18-tinmanx1-fiber-and-strength-tools.md).

OrcaSlicer 2.5, and so current Tinman, adds precise seam placement and changes
wall generation; see [what the 2.5.1 base changed](21-slicer-upgrades-and-calibration-changes.md#what-the-251-base-changed-for-tuners).
The historical shared-control label does not imply identical new toolpaths.

The Quality tab controls how the slicer turns model geometry into printable
roads. It can improve a surface only when the defect matches the kind of path
this tab changes. Do not use it to disguise wet filament, a loose machine, a
clog, or a melt-flow limit.

## Layer Height

| This group | |
| --- | --- |
| **What it controls** | Sets the vertical thickness of normal and first layers. It changes detail, staircase visibility, print time, and the amount of plastic demanded by each road. |
| **Change it when** | Curves look stepped, tiny Z details disappear, the first layer needs a different thickness, or the chosen height is poorly matched to the nozzle. |
| **Aim for** | The coarsest layer height that preserves the required geometry, with a first layer that adheres without excessive squish. |

| Control | What it does |
| --- | --- |
| `Layer height` | Controls ordinary layers. |
| `Initial layer height` | Trades first-layer detail for tolerance of small bed and Z errors. A thicker value is not permission to ignore a bad mesh or incorrect Z offset. |

## Line Width

| This group | |
| --- | --- |
| **What it controls** | Sets the planned width of roads for each feature. Width changes the number of paths, contact between adjacent roads, detail resolution, flow demand, and wall thickness. |
| **Change it when** | A particular feature is weak, poorly closed, too coarse, or visibly different from the rest of the print after global flow is calibrated. |
| **Aim for** | Widths that the nozzle can deposit consistently, with joined roads and no unnecessary loss of detail. |

| Control | What it does |
| --- | --- |
| `Default line width` | The fallback. |
| `Initial layer line width` | Changes bed contact. |
| `Outer wall line width` | Trades fine geometry against a broader, more forgiving shell road. |
| `Inner wall`, `sparse infill`, `internal solid infill line width` | Govern structural roads. |
| `Top surface line width` | Directly affects top closure and visible line scale. |
| `Support line width`, `bridge line width` | Affect unsupported structures. |

Change width before feature-specific flow when the problem is road geometry.
Change flow when road geometry is sensible but deposited volume is wrong.

## Seam

| This group | |
| --- | --- |
| **What it controls** | Controls where perimeter loops begin and end and how pressure is handed across that transition. |
| **Change it when** | One vertical scar, blobs, pits, hairs, or start/stop defects repeat at the seam while the rest of the wall is sound. |
| **Aim for** | A predictable transition that is either hidden in a chosen location or distributed without creating widespread marks. |

| Control | What it does |
| --- | --- |
| `Seam position` | Chooses the placement strategy: nearest, aligned, rear, or random. Aligned is best for diagnosis. |
| `Staggered inner seams` | Separates inner-wall starts from the visible outer seam. |
| `Seam gap` | Deliberately leaves a small end gap; too much creates a notch and too little can leave a ridge. |
| `Wipe speed`, `wipe on loops`, `wipe before external loop` | Control motion around the stop/start event. |
| Scarf | Controls spread the transition over distance: `scarf joint type`, conditional use, threshold angles, speed, start height, full-loop use, minimum length, steps, inner-wall use, and flow ratio. |

Tune pressure advance and global flow first. A scarf can distribute a bad
transition, but it cannot make an incorrect extrusion system correct.

## Precision

| This group | |
| --- | --- |
| **What it controls** | Changes how closely sliced paths follow geometry and applies targeted dimensional corrections. |
| **Change it when** | Measured errors have a known model: constant contour offset, hole-only error, bottom-layer flare, curve faceting, or lost narrow geometry. |
| **Aim for** | Cooled parts meet the intended dimensions without applying one correction to unrelated errors. |

| Control | What it does |
| --- | --- |
| `Slice gap closing radius` | Closes very small gaps in sliced regions. Excessive values can merge features that should remain separate. |
| `Resolution` | Controls curve simplification; smaller values keep more points but produce larger, busier paths. |
| `Arc fitting` | Replaces suitable short segments with arcs when the output and firmware support them. |
| `X-Y contour compensation` | Offsets outside contours. It is for a nearly constant external error, not proportional material shrinkage. |
| `X-Y hole compensation` | Offsets internal holes separately. |
| `Elephant foot compensation` | Layer count, and density target only the enlarged bottom region. |
| `Precise wall` | Improves wall placement where line-center approximations would bias thickness. |
| `Precise Z height` | Adjusts layer planning to finish closer to the requested height. |
| Polyhole | Controls convert eligible round holes to printer-friendly polygons and define the size threshold and orientation. |

See [Dimensional Accuracy and Tolerances](07-dimensional-accuracy.md) before
using compensation.

## Ironing

| This group | |
| --- | --- |
| **What it controls** | Makes an extra low-flow pass over selected solid top surfaces to press and redistribute plastic. |
| **Change it when** | An already closed, supported top needs a smoother cosmetic finish. Do not use it to repair open channels, pillowing, or sparse support below the roof. |
| **Aim for** | A more uniform sheen and reduced ridge height without edge bulges, drag marks, or heat damage. |

| Control | What it does |
| --- | --- |
| `Ironing type` | Selects which surfaces receive the pass. |
| `Pattern` | Chooses rectilinear or concentric motion. |
| `Flow` | Supplies the small amount of material used to fill valleys. |
| `Spacing` | Sets pass density; tighter spacing increases smoothing and heat. |
| `Inset` | Keeps the tool away from perimeter edges. |
| `Angle`, `fixed angle` | Control direction. |
| `Ironing speed` | On the Speed tab and must be judged with flow and spacing. |

Tune ironing last.

## Z Contouring

| This group | |
| --- | --- |
| **What it controls** | Varies path height within a layer to represent sloped top geometry with less visible stair stepping. |
| **Change it when** | A shallow, upward-facing slope is visibly terraced and ordinary layer-height reduction is too slow or still leaves objectionable steps. |
| **Aim for** | A smoother slope with stable extrusion and no collisions or thin unsupported ridges. |

| Control | What it does |
| --- | --- |
| `Z contouring` | Enables the strategy. |
| `Minimize wall height angle` | Limits where variable-height walls are attempted. |
| `Minimum Z height` | Protects against impractically thin vertical changes. |
| `Do not alternate fill direction` | Keeps the fill direction consistent when alternating it would harm the contoured surface. |

This changes three-dimensional path geometry. Inspect the preview carefully and
validate clearance before production use.

## Wall Generator

| This group | |
| --- | --- |
| **What it controls** | Chooses how the slicer fits wall roads into changing thickness. Classic uses mostly fixed widths; Arachne varies width to fill narrow or tapered areas. |
| **Change it when** | Thin features vanish, wall thickness changes create gaps, or variable-width walls themselves create an uneven visible finish. |
| **Aim for** | Complete walls with stable widths, preserved detail, and no needless width oscillation. |

| Control | What it does |
| --- | --- |
| `Wall generator` | Chooses Classic or Arachne. |
| `Wall transition angle`, `filter deviation`, `transition length` | Decide how readily Arachne changes wall count and width. |
| `Wall distribution count` | Controls how many neighboring walls share a width transition. |
| `Minimum wall width`, `first-layer minimum wall width` | Reject roads too narrow to print reliably. |
| `Minimum feature size`, `minimum wall length` | Suppress tiny fragments. |
| `Maximum wall resolution`, `maximum wall deviation` | Simplify highly detailed wall paths while limiting geometric error. |

For surface finish, start with the generator choice and preview the outer wall.
Classic can look more uniform on simple boxes; Arachne often fills variable
geometry better. Neither corrects a wet filament or unstable extrusion system.

## Walls and Surfaces

| This group | |
| --- | --- |
| **What it controls** | Controls wall order, flow by feature, travel around walls, and special handling of small or top regions. |
| **Change it when** | Walls are dimensionally sound but show order-related marks, small top areas behave differently from broad ones, or one feature needs a small flow correction after global calibration. |
| **Aim for** | A clean outer shell, closed surfaces, minimal travel scars, and feature-specific flow that does not disturb the validated global profile. |

| Control | What it does |
| --- | --- |
| `Wall printing order` | Controls whether outer or inner walls are printed first. Outer-first can protect dimensions; inner-first often gives the visible wall more support. Inner-outer-inner is a deliberate compromise. |
| `Print infill first` | Changes what supports the wall and can make infill marks more visible through a thin shell. |
| `Wall loop direction` | Can move seam and overhang behavior relative to machine cooling and geometry. |
| `Print flow ratio` | Top, bottom, first-layer, wall, overhang, sparse-infill, solid-infill, gap-fill, support, and support-interface flow ratios are targeted multipliers. Enable the additional ratios only when evidence identifies a feature-specific error. |
| `Only one wall` | Options reduce walls on the first layer or top surfaces where extra walls would crowd a narrow region. |
| `Minimum top-surface width` | Decides what is treated as a visible top. |
| `Avoid crossing walls`, `maximum detour` | Trade travel distance for fewer scars across visible shells. |
| `Small-area flow compensation` | Its model reduce overfill caused by very short extrusion segments. Treat the model as an advanced calibration curve, not a cosmetic randomizer. |

This group is often relevant to surface finish, but change path order or the
specific feature before disturbing global flow.

## Bridging

| This group | |
| --- | --- |
| **What it controls** | Controls roads laid across air or sparse internal support. |
| **Change it when** | Unsupported spans sag, separate, curl, or become too dense while ordinary walls print correctly. |
| **Aim for** | Straight, attached bridge lines with acceptable sag and a usable surface above them. |

| Control | What it does |
| --- | --- |
| External and internal `bridge flow` | Change material per bridge road. |
| External and internal `bridge density` | Change spacing between roads. |
| `Thick bridges` | Selects the older thick-road behavior when needed. |
| `Extra bridge layer` | Adds a reinforcing layer above chosen bridges. |
| `Filter small internal bridges` | Decides whether short internal spans receive bridge treatment. |
| `Counterbore-hole bridging` | Chooses how flat-bottom holes are closed. |

Bridge speed is on the Speed tab and cooling is in the filament profile. Tune
the three together with separate tests.

## Overhangs

| This group | |
| --- | --- |
| **What it controls** | Changes wall generation for partially unsupported edges. |
| **Change it when** | Steep walls curl, droop, lose their edge, or need geometry adaptation before ordinary support is added. |
| **Aim for** | Attached overhang roads and a stable edge without needless geometry distortion. |

| Control | What it does |
| --- | --- |
| `Detect overhang wall` | Allows feature-specific speed and flow behavior. |
| `Make overhang printable` | Modifies difficult geometry; angle and hole-size limits determine where that modification is allowed. |
| `Extra perimeters on overhangs` | Creates more local support. |
| `Reverse on even`, `reverse internal only` | The reversal threshold change direction between layers to balance one-sided deposition effects. |

Overhang speed belongs to the Speed tab, while fan and layer-time controls
belong to the filament profile. TinmanX1's experimental Wave Overhang system is
documented separately because it generates a different supportless path family.

Continue with the [Strength tab](13-strength-tab.md).
