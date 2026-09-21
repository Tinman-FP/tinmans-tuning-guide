# Quality Tab

**Version note:** every group below is **Shared 2.4.2**. Source comparison found
no TinmanX1-only Quality controls in the stated baseline. TinmanX1 adds related
tools elsewhere, especially [Strength Lens, fiber planning, and Wave
Overhangs](18-tinmanx1-fiber-and-strength-tools.md).

The Quality tab controls how the slicer turns model geometry into printable
roads. It can improve a surface only when the defect matches the kind of path
this tab changes. Do not use it to disguise wet filament, a loose machine, a
clog, or a melt-flow limit.

## Layer Height

**What:** sets the vertical thickness of normal and first layers. It changes
detail, staircase visibility, print time, and the amount of plastic demanded by
each road.

**Use it when:** curves look stepped, tiny Z details disappear, the first layer
needs a different thickness, or the chosen height is poorly matched to the
nozzle.

**Desired result:** the coarsest layer height that preserves the required
geometry, with a first layer that adheres without excessive squish.

- `Layer height` controls ordinary layers.
- `Initial layer height` trades first-layer detail for tolerance of small bed
  and Z errors. A thicker value is not permission to ignore a bad mesh or
  incorrect Z offset.

## Line Width

**What:** sets the planned width of roads for each feature. Width changes the
number of paths, contact between adjacent roads, detail resolution, flow demand,
and wall thickness.

**Use it when:** a particular feature is weak, poorly closed, too coarse, or
visibly different from the rest of the print after global flow is calibrated.

**Desired result:** widths that the nozzle can deposit consistently, with joined
roads and no unnecessary loss of detail.

- `Default line width` is the fallback.
- `Initial layer line width` changes bed contact.
- `Outer wall line width` trades fine geometry against a broader, more forgiving
  shell road.
- `Inner wall`, `sparse infill`, and `internal solid infill line width` govern
  structural roads.
- `Top surface line width` directly affects top closure and visible line scale.
- `Support line width` and `bridge line width` affect unsupported structures.

Change width before feature-specific flow when the problem is road geometry.
Change flow when road geometry is sensible but deposited volume is wrong.

## Seam

**What:** controls where perimeter loops begin and end and how pressure is
handed across that transition.

**Use it when:** one vertical scar, blobs, pits, hairs, or start/stop defects
repeat at the seam while the rest of the wall is sound.

**Desired result:** a predictable transition that is either hidden in a chosen
location or distributed without creating widespread marks.

- `Seam position` chooses the placement strategy: nearest, aligned, rear, or
  random. Aligned is best for diagnosis.
- `Staggered inner seams` separates inner-wall starts from the visible outer
  seam.
- `Seam gap` deliberately leaves a small end gap; too much creates a notch and
  too little can leave a ridge.
- `Wipe speed`, `wipe on loops`, and `wipe before external loop` control motion
  around the stop/start event.
- Scarf controls spread the transition over distance: `scarf joint type`,
  conditional use, threshold angles, speed, start height, full-loop use,
  minimum length, steps, inner-wall use, and flow ratio.

Tune pressure advance and global flow first. A scarf can distribute a bad
transition, but it cannot make an incorrect extrusion system correct.

## Precision

**What:** changes how closely sliced paths follow geometry and applies targeted
dimensional corrections.

**Use it when:** measured errors have a known model: constant contour offset,
hole-only error, bottom-layer flare, curve faceting, or lost narrow geometry.

**Desired result:** cooled parts meet the intended dimensions without applying
one correction to unrelated errors.

- `Slice gap closing radius` closes very small gaps in sliced regions. Excessive
  values can merge features that should remain separate.
- `Resolution` controls curve simplification; smaller values keep more points
  but produce larger, busier paths.
- `Arc fitting` replaces suitable short segments with arcs when the output and
  firmware support them.
- `X-Y contour compensation` offsets outside contours. It is for a nearly
  constant external error, not proportional material shrinkage.
- `X-Y hole compensation` offsets internal holes separately.
- `Elephant foot compensation`, layer count, and density target only the
  enlarged bottom region.
- `Precise wall` improves wall placement where line-center approximations would
  bias thickness.
- `Precise Z height` adjusts layer planning to finish closer to the requested
  height.
- Polyhole controls convert eligible round holes to printer-friendly polygons
  and define the size threshold and orientation.

See [Dimensional Accuracy and Tolerances](07-dimensional-accuracy.md) before
using compensation.

## Ironing

**What:** makes an extra low-flow pass over selected solid top surfaces to press
and redistribute plastic.

**Use it when:** an already closed, supported top needs a smoother cosmetic
finish. Do not use it to repair open channels, pillowing, or sparse support
below the roof.

**Desired result:** a more uniform sheen and reduced ridge height without edge
bulges, drag marks, or heat damage.

- `Ironing type` selects which surfaces receive the pass.
- `Pattern` chooses rectilinear or concentric motion.
- `Flow` supplies the small amount of material used to fill valleys.
- `Spacing` sets pass density; tighter spacing increases smoothing and heat.
- `Inset` keeps the tool away from perimeter edges.
- `Angle` and `fixed angle` control direction.
- `Ironing speed` is on the Speed tab and must be judged with flow and spacing.

Tune ironing last.

## Z Contouring

**What:** varies path height within a layer to represent sloped top geometry
with less visible stair stepping.

**Use it when:** a shallow, upward-facing slope is visibly terraced and ordinary
layer-height reduction is too slow or still leaves objectionable steps.

**Desired result:** a smoother slope with stable extrusion and no collisions or
thin unsupported ridges.

- `Z contouring` enables the strategy.
- `Minimize wall height angle` limits where variable-height walls are attempted.
- `Minimum Z height` protects against impractically thin vertical changes.
- `Do not alternate fill direction` keeps the fill direction consistent when
  alternating it would harm the contoured surface.

This changes three-dimensional path geometry. Inspect the preview carefully and
validate clearance before production use.

## Wall Generator

**What:** chooses how the slicer fits wall roads into changing thickness. Classic
uses mostly fixed widths; Arachne varies width to fill narrow or tapered areas.

**Use it when:** thin features vanish, wall thickness changes create gaps, or
variable-width walls themselves create an uneven visible finish.

**Desired result:** complete walls with stable widths, preserved detail, and no
needless width oscillation.

- `Wall generator` chooses Classic or Arachne.
- `Wall transition angle`, `filter deviation`, and `transition length` decide
  how readily Arachne changes wall count and width.
- `Wall distribution count` controls how many neighboring walls share a width
  transition.
- `Minimum wall width` and `first-layer minimum wall width` reject roads too
  narrow to print reliably.
- `Minimum feature size` and `minimum wall length` suppress tiny fragments.
- `Maximum wall resolution` and `maximum wall deviation` simplify highly
  detailed wall paths while limiting geometric error.

For surface finish, start with the generator choice and preview the outer wall.
Classic can look more uniform on simple boxes; Arachne often fills variable
geometry better. Neither corrects a wet filament or unstable extrusion system.

## Walls and Surfaces

**What:** controls wall order, flow by feature, travel around walls, and special
handling of small or top regions.

**Use it when:** walls are dimensionally sound but show order-related marks,
small top areas behave differently from broad ones, or one feature needs a
small flow correction after global calibration.

**Desired result:** a clean outer shell, closed surfaces, minimal travel scars,
and feature-specific flow that does not disturb the validated global profile.

- `Wall printing order` controls whether outer or inner walls are printed first.
  Outer-first can protect dimensions; inner-first often gives the visible wall
  more support. Inner-outer-inner is a deliberate compromise.
- `Print infill first` changes what supports the wall and can make infill marks
  more visible through a thin shell.
- `Wall loop direction` can move seam and overhang behavior relative to machine
  cooling and geometry.
- `Print flow ratio`, top, bottom, first-layer, wall, overhang, sparse-infill,
  solid-infill, gap-fill, support, and support-interface flow ratios are targeted
  multipliers. Enable the additional ratios only when evidence identifies a
  feature-specific error.
- `Only one wall` options reduce walls on the first layer or top surfaces where
  extra walls would crowd a narrow region.
- `Minimum top-surface width` decides what is treated as a visible top.
- `Avoid crossing walls` and `maximum detour` trade travel distance for fewer
  scars across visible shells.
- `Small-area flow compensation` and its model reduce overfill caused by very
  short extrusion segments. Treat the model as an advanced calibration curve,
  not a cosmetic randomizer.

This group is often relevant to surface finish, but change path order or the
specific feature before disturbing global flow.

## Bridging

**What:** controls roads laid across air or sparse internal support.

**Use it when:** unsupported spans sag, separate, curl, or become too dense while
ordinary walls print correctly.

**Desired result:** straight, attached bridge lines with acceptable sag and a
usable surface above them.

- External and internal `bridge flow` change material per bridge road.
- External and internal `bridge density` change spacing between roads.
- `Thick bridges` selects the older thick-road behavior when needed.
- `Extra bridge layer` adds a reinforcing layer above chosen bridges.
- `Filter small internal bridges` decides whether short internal spans receive
  bridge treatment.
- `Counterbore-hole bridging` chooses how flat-bottom holes are closed.

Bridge speed is on the Speed tab and cooling is in the filament profile. Tune
the three together with separate tests.

## Overhangs

**What:** changes wall generation for partially unsupported edges.

**Use it when:** steep walls curl, droop, lose their edge, or need geometry
adaptation before ordinary support is added.

**Desired result:** attached overhang roads and a stable edge without needless
geometry distortion.

- `Detect overhang wall` allows feature-specific speed and flow behavior.
- `Make overhang printable` modifies difficult geometry; angle and hole-size
  limits determine where that modification is allowed.
- `Extra perimeters on overhangs` creates more local support.
- `Reverse on even`, `reverse internal only`, and the reversal threshold change
  direction between layers to balance one-sided deposition effects.

Overhang speed belongs to the Speed tab, while fan and layer-time controls
belong to the filament profile. TinmanX1's experimental Wave Overhang system is
documented separately because it generates a different supportless path family.

Continue with the [Strength tab](13-strength-tab.md).
