# Strength Tab

> **At a glance**
> - **Decide:** walls, shells and infill for the part's load
> - **Test:** a representative part, not a coupon
> - **Keep:** the lightest structure that passes its strength check

Most of this tab is **Shared 2.4.2**. TinmanX1 adds the **Strength Lens** group
at the top; OrcaSlicer 2.4.2 begins with Walls. Strength settings affect the
amount and arrangement of material, but settings alone do not prove strength.
Validate critical parts with representative loads and failure tests.

## Strength Lens

**Difference:** **TinmanX1 addition.** OrcaSlicer 2.4.2 does not have this
pre-slice orientation aid.

| This group | |
| --- | --- |
| **What it controls** | Colors the prepared model according to a simplified directional strength model before slicing. |
| **Change it when** | Deciding how to orient a part relative to an expected load, especially when layer separation or continuous-fiber direction matters. |
| **Aim for** | An orientation that keeps the important load in stronger printed directions and moves weak layer-normal loading away from critical features. |

| Control | What it does |
| --- | --- |
| `Strength Lens` | Turns the view on. |
| `Material model` | Selects the assumption: filament preset, isotropic, ordinary anisotropic FDM, or continuous fiber. |
| `Load axis` | Chooses Auto, X, Y, or Z for the direction being evaluated. |

The lens is a comparative visualization, not finite-element analysis or a
strength certification. See [TinmanX1 fiber and strength
tools](18-tinmanx1-fiber-and-strength-tools.md) for the model limits.

## Walls

| This group | |
| --- | --- |
| **What it controls** | Controls the number and continuity of perimeter shells. |
| **Change it when** | A part needs better bending, impact, sealing, screw retention, or exterior robustness. For many real parts, an extra wall is more useful than the same plastic added as sparse infill. |
| **Aim for** | A continuous shell thick enough for the load without crowding small features or adding unnecessary mass. |

| Control | What it does |
| --- | --- |
| `Wall loops` | The primary shell-thickness control. |
| `Alternate extra wall` | Adds reinforcement on alternating layers, improving shell-to-infill connection with less material than another wall everywhere. |
| `Detect thin walls` | Preserves narrow model features Classic walls might omit; with Arachne, inspect the preview because variable-width walls already solve many thin-feature cases. |

## Top and Bottom Shells

| This group | |
| --- | --- |
| **What it controls** | Controls the solid roofs and floors that close the part and transfer load across sparse infill. |
| **Change it when** | Top surfaces pillow or remain open, bottom skins are fragile, or a face needs greater puncture and bending resistance. |
| **Aim for** | Fully closed skins with enough total thickness to bridge the infill and survive the intended load. |

| Control | What it does |
| --- | --- |
| `Top shell layers`, `bottom shell layers` | Set counts. |
| `Top shell thickness`, `bottom shell thickness` | Enforce physical thickness even when layer height changes. The slicer uses whichever requirement demands more layers. |
| `Top surface density`, `bottom surface density` | Control how fully the visible surface is filled. |
| `Top surface pattern`, `bottom surface pattern` | Change path direction, continuity, and appearance. Monotonic families improve visual ordering; concentric follows outlines; decorative patterns trade speed and uniformity. |
| `Top/bottom infill-wall overlap` | Joins solid skins to the shell. Too little leaves a gap; too much produces a raised perimeter band. |

Do not tune a rough top with shell count alone. First determine whether the
problem is inadequate support, wrong top flow, path endpoints, or heat.

## Infill

| This group | |
| --- | --- |
| **What it controls** | Creates the internal load path and support structure between shells. |
| **Change it when** | The part needs a different stiffness-to-weight tradeoff, the roof needs better support, or the load has a known direction. |
| **Aim for** | Enough connected internal structure to support skins and carry the expected load without wasting material or creating excessive nozzle crossings. |

| Control | What it does |
| --- | --- |
| `Sparse infill density` | Controls how much of the interior is occupied. |
| `Sparse infill pattern` | Selects the load path. Rectilinear families are fast; gyroid and cubic families distribute load in more directions; lightning is mainly roof support, not general strength. |
| `Infill direction` | The sparse rotation template orient or sequence layers. |
| `Symmetric infill Y axis` | Mirrors orientation where part symmetry matters. |
| `Infill-wall overlap` | Joins sparse infill to shells. |
| `Infill anchor`, `maximum anchor length` | Control how far infill is tied into perimeters. |
| `Internal solid infill pattern` | Direction, and rotation template control buried solid regions. |
| `Gap fill target`, `filter tiny gap fill` | Decide where narrow leftover spaces receive short roads. Excessive gap fill can create heat and blobs. |
| `Extra solid infill` | Adds selected reinforcement through modifiers or painted regions. |
| `Fill multiline` | The pattern-specific controls tune specialized patterns: optimized gyroid, locked-zag skin/skeleton density and widths, cross-hatch shift, lateral-lattice angles, lateral-honeycomb angle, and lightning branch angles. |

Pattern-specific controls do nothing unless their matching pattern is active.
Change them only after the broad pattern and density are justified by the load.

## Advanced Strength

| This group | |
| --- | --- |
| **What it controls** | Changes bridge orientation, combines infill layers, and adds solid material where shell continuity would otherwise be weak. |
| **Change it when** | Preview inspection reveals a directional bridge problem, tiny sparse regions, inefficient infill on every layer, or thin sloped shells that are not receiving enough support. |
| **Aim for** | Continuous load paths and adequately supported shells with no unnecessary solid mass or overly tall infill roads. |

| Control | What it does |
| --- | --- |
| `Align infill direction to model` | Makes orientation follow model coordinates instead of the plate, useful when rotating several copies of a directional part. |
| `Bridge angle`, `internal bridge angle`, `relative bridge angle` | Override automatic span direction. Use only after previewing the anchors. |
| `Minimum sparse infill area` | Converts tiny sparse islands to solid fill. |
| `Infill combination` | Prints sparse infill less often using taller roads; `maximum layer height` caps those roads. This saves time but can reduce local support and exceed flow limits. |
| `Detect narrow internal solid infill` | Handles thin buried solids that a normal pattern cannot fill cleanly. |
| `Ensure vertical shell thickness` | Adds material below sloped surfaces so the requested shell remains physically thick rather than merely having a fixed number of layers. |

Continue with the [Speed tab](14-speed-tab.md).
