# Strength Tab

Most of this tab is **Shared 2.4.2**. TinmanX1 adds the **Strength Lens** group
at the top; OrcaSlicer 2.4.2 begins with Walls. Strength settings affect the
amount and arrangement of material, but settings alone do not prove strength.
Validate critical parts with representative loads and failure tests.

## Strength Lens

**Difference:** **TinmanX1 addition.** OrcaSlicer 2.4.2 does not have this
pre-slice orientation aid.

**What:** colors the prepared model according to a simplified directional
strength model before slicing.

**Use it when:** deciding how to orient a part relative to an expected load,
especially when layer separation or continuous-fiber direction matters.

**Desired result:** an orientation that keeps the important load in stronger
printed directions and moves weak layer-normal loading away from critical
features.

- `Strength Lens` turns the view on.
- `Material model` selects the assumption: filament preset, isotropic,
  ordinary anisotropic FDM, or continuous fiber.
- `Load axis` chooses Auto, X, Y, or Z for the direction being evaluated.

The lens is a comparative visualization, not finite-element analysis or a
strength certification. See [TinmanX1 fiber and strength
tools](18-tinmanx1-fiber-and-strength-tools.md) for the model limits.

## Walls

**What:** controls the number and continuity of perimeter shells.

**Use it when:** a part needs better bending, impact, sealing, screw retention,
or exterior robustness. For many real parts, an extra wall is more useful than
the same plastic added as sparse infill.

**Desired result:** a continuous shell thick enough for the load without
crowding small features or adding unnecessary mass.

- `Wall loops` is the primary shell-thickness control.
- `Alternate extra wall` adds reinforcement on alternating layers, improving
  shell-to-infill connection with less material than another wall everywhere.
- `Detect thin walls` preserves narrow model features Classic walls might omit;
  with Arachne, inspect the preview because variable-width walls already solve
  many thin-feature cases.

## Top and Bottom Shells

**What:** controls the solid roofs and floors that close the part and transfer
load across sparse infill.

**Use it when:** top surfaces pillow or remain open, bottom skins are fragile,
or a face needs greater puncture and bending resistance.

**Desired result:** fully closed skins with enough total thickness to bridge the
infill and survive the intended load.

- `Top shell layers` and `bottom shell layers` set counts.
- `Top shell thickness` and `bottom shell thickness` enforce physical thickness
  even when layer height changes. The slicer uses whichever requirement demands
  more layers.
- `Top surface density` and `bottom surface density` control how fully the
  visible surface is filled.
- `Top surface pattern` and `bottom surface pattern` change path direction,
  continuity, and appearance. Monotonic families improve visual ordering;
  concentric follows outlines; decorative patterns trade speed and uniformity.
- `Top/bottom infill-wall overlap` joins solid skins to the shell. Too little
  leaves a gap; too much produces a raised perimeter band.

Do not tune a rough top with shell count alone. First determine whether the
problem is inadequate support, wrong top flow, path endpoints, or heat.

## Infill

**What:** creates the internal load path and support structure between shells.

**Use it when:** the part needs a different stiffness-to-weight tradeoff, the
roof needs better support, or the load has a known direction.

**Desired result:** enough connected internal structure to support skins and
carry the expected load without wasting material or creating excessive nozzle
crossings.

- `Sparse infill density` controls how much of the interior is occupied.
- `Sparse infill pattern` selects the load path. Rectilinear families are fast;
  gyroid and cubic families distribute load in more directions; lightning is
  mainly roof support, not general strength.
- `Infill direction` and the sparse rotation template orient or sequence layers.
- `Symmetric infill Y axis` mirrors orientation where part symmetry matters.
- `Infill-wall overlap` joins sparse infill to shells.
- `Infill anchor` and `maximum anchor length` control how far infill is tied
  into perimeters.
- `Internal solid infill pattern`, direction, and rotation template control
  buried solid regions.
- `Gap fill target` and `filter tiny gap fill` decide where narrow leftover
  spaces receive short roads. Excessive gap fill can create heat and blobs.
- `Extra solid infill` adds selected reinforcement through modifiers or painted
  regions.
- `Fill multiline` and the pattern-specific controls tune specialized patterns:
  optimized gyroid, locked-zag skin/skeleton density and widths, cross-hatch
  shift, lateral-lattice angles, lateral-honeycomb angle, and lightning branch
  angles.

Pattern-specific controls do nothing unless their matching pattern is active.
Change them only after the broad pattern and density are justified by the load.

## Advanced Strength

**What:** changes bridge orientation, combines infill layers, and adds solid
material where shell continuity would otherwise be weak.

**Use it when:** preview inspection reveals a directional bridge problem, tiny
sparse regions, inefficient infill on every layer, or thin sloped shells that
are not receiving enough support.

**Desired result:** continuous load paths and adequately supported shells with
no unnecessary solid mass or overly tall infill roads.

- `Align infill direction to model` makes orientation follow model coordinates
  instead of the plate, useful when rotating several copies of a directional
  part.
- `Bridge angle`, `internal bridge angle`, and `relative bridge angle` override
  automatic span direction. Use only after previewing the anchors.
- `Minimum sparse infill area` converts tiny sparse islands to solid fill.
- `Infill combination` prints sparse infill less often using taller roads;
  `maximum layer height` caps those roads. This saves time but can reduce local
  support and exceed flow limits.
- `Detect narrow internal solid infill` handles thin buried solids that a normal
  pattern cannot fill cleanly.
- `Ensure vertical shell thickness` adds material below sloped surfaces so the
  requested shell remains physically thick rather than merely having a fixed
  number of layers.

Continue with the [Speed tab](14-speed-tab.md).
