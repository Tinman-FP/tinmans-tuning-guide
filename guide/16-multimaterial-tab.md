# Multimaterial Tab

> **At a glance**
> - **Decide:** prime tower, purge and tool-change settings
> - **Test:** a short multi-material part, checked in the G-code
> - **Keep:** clean, repeatable changes with the smallest stable tower

All groups in this chapter are **Shared 2.4.2**. TinmanX1's continuous-fiber
system is not configured through these ordinary color/material-change controls;
see [TinmanX1 fiber and strength tools](18-tinmanx1-fiber-and-strength-tools.md).

OrcaSlicer 2.5, and so current Tinman, extends nozzle variants and
tool-change settings; see the [upgrade chapter](21-slicer-upgrades-and-calibration-changes.md#new-controls-do-not-replace-the-tuning-order).
Verify each tool's resolved filament values and slot mapping after sync or
migration, and check the bed temperature the G-code actually uses when
materials with different bed temperatures share a plate.

## Prime Tower

| This group | |
| --- | --- |
| **What it controls** | Creates a sacrificial structure used to restore pressure, purge color or material, and stabilize tool changes. |
| **Change it when** | Multi-material transitions produce missing starts, contamination, unstable pressure, or unreliable nozzle readiness. |
| **Aim for** | Clean, repeatable transitions with the smallest tower that remains mechanically stable. |

| Control | What it does |
| --- | --- |
| Enable | Controls tower creation. |
| Skip points and interface features | Tune path continuity around changes. |
| Interface cooldown | Controls tower cooling during transition work. |
| Framework, width, prime volume, brim width, and infill gap | Control tower structure and purge capacity. |
| Rotation | Changes footprint orientation. |
| Bridging distance, purge-line spacing, extra flow, and maximum purge speed | Control how purge roads are deposited. |
| Wall type, cone angle, rib length/width, and wall fillet | Tune stability. |
| `No sparse layers` | Avoids a weak intermittent tower. |
| Single-extruder multimaterial priming | Enables startup behavior for that hardware class. |

Inspect tower paths and confirm bed clearance. A tower that is too small can
fail late and endanger an otherwise good part.

## Filament for Features

| This group | |
| --- | --- |
| **What it controls** | Assigns filament slots to outer walls, inner walls, sparse infill, internal solids, top surfaces, bottom surfaces, and the tower. |
| **Change it when** | Different materials or colors intentionally serve different visual or structural roles. |
| **Aim for** | Each feature uses the intended compatible material, with tool changes and purge volume that are justified by the design. |

Do not assume that a stronger filament automatically produces a stronger mixed
part. The interface between materials may govern failure.

## Ooze Prevention

| This group | |
| --- | --- |
| **What it controls** | Manages idle-tool temperature and preheating before the next use. |
| **Change it when** | An inactive nozzle drools, contaminates the model, or returns too cold and under-extrudes. |
| **Aim for** | The idle tool stays cool enough to resist ooze and reheats early enough to extrude correctly at its next path. |

| Control | What it does |
| --- | --- |
| Enable | Turns the strategy on. |
| Standby temperature delta | Lowers the idle target. |
| Preheat time and steps | Shape the return to printing temperature. |

Avoid temperature changes outside the material's safe processing range.

## Flush Options

| This group | |
| --- | --- |
| **What it controls** | Diverts otherwise wasted purge material into internal features or designated objects. |
| **Change it when** | Color purity and material compatibility allow purge to become part of the print. |
| **Aim for** | Reduced waste with no visible contamination, weak interface, or incorrect support behavior. |

- Flush into infill hides compatible purge inside sparse structure.
- Flush into objects uses specifically designated purge objects.
- Flush into support uses disposable support, provided the material remains
  suitable for support and interface roles.

## Advanced Multimaterial

| This group | |
| --- | --- |
| **What it controls** | Creates interlocking geometry between material regions and controls segmented-interface behavior. |
| **Change it when** | Adjacent materials need more mechanical keying than a flat boundary provides. |
| **Aim for** | A larger, mechanically interlocked interface that does not break through visible surfaces or overwhelm small geometry. |

| Control | What it does |
| --- | --- |
| Interlocking beam | Enables the strategy. |
| Interface shells | Add boundary structure. |
| Segmented-region width and depth | Set where segmentation applies. |
| Beam width, orientation, layer count, depth, and boundary avoidance | Define the mechanical key. |

Use test coupons. Chemical compatibility and temperature remain decisive even
when geometry is interlocked.

Continue with the [Others tab](17-others-tab.md).
