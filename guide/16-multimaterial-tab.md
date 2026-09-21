# Multimaterial Tab

All groups in this chapter are **Shared 2.4.2**. TinmanX1's continuous-fiber
system is not configured through these ordinary color/material-change controls;
see [TinmanX1 fiber and strength tools](18-tinmanx1-fiber-and-strength-tools.md).

## Prime Tower

**What:** creates a sacrificial structure used to restore pressure, purge color
or material, and stabilize tool changes.

**Use it when:** multi-material transitions produce missing starts,
contamination, unstable pressure, or unreliable nozzle readiness.

**Desired result:** clean, repeatable transitions with the smallest tower that
remains mechanically stable.

- Enable controls tower creation.
- Skip points and interface features tune path continuity around changes.
- Interface cooldown controls tower cooling during transition work.
- Framework, width, prime volume, brim width, and infill gap control tower
  structure and purge capacity.
- Rotation changes footprint orientation.
- Bridging distance, purge-line spacing, extra flow, and maximum purge speed
  control how purge roads are deposited.
- Wall type, cone angle, rib length/width, and wall fillet tune stability.
- `No sparse layers` avoids a weak intermittent tower.
- Single-extruder multimaterial priming enables startup behavior for that
  hardware class.

Inspect tower paths and confirm bed clearance. A tower that is too small can
fail late and endanger an otherwise good part.

## Filament for Features

**What:** assigns filament slots to outer walls, inner walls, sparse infill,
internal solids, top surfaces, bottom surfaces, and the tower.

**Use it when:** different materials or colors intentionally serve different
visual or structural roles.

**Desired result:** each feature uses the intended compatible material, with
tool changes and purge volume that are justified by the design.

Do not assume that a stronger filament automatically produces a stronger mixed
part. The interface between materials may govern failure.

## Ooze Prevention

**What:** manages idle-tool temperature and preheating before the next use.

**Use it when:** an inactive nozzle drools, contaminates the model, or returns
too cold and under-extrudes.

**Desired result:** the idle tool stays cool enough to resist ooze and reheats
early enough to extrude correctly at its next path.

- Enable turns the strategy on.
- Standby temperature delta lowers the idle target.
- Preheat time and steps shape the return to printing temperature.

Avoid temperature changes outside the material's safe processing range.

## Flush Options

**What:** diverts otherwise wasted purge material into internal features or
designated objects.

**Use it when:** color purity and material compatibility allow purge to become
part of the print.

**Desired result:** reduced waste with no visible contamination, weak interface,
or incorrect support behavior.

- Flush into infill hides compatible purge inside sparse structure.
- Flush into objects uses specifically designated purge objects.
- Flush into support uses disposable support, provided the material remains
  suitable for support and interface roles.

## Advanced Multimaterial

**What:** creates interlocking geometry between material regions and controls
segmented-interface behavior.

**Use it when:** adjacent materials need more mechanical keying than a flat
boundary provides.

**Desired result:** a larger, mechanically interlocked interface that does not
break through visible surfaces or overwhelm small geometry.

- Interlocking beam enables the strategy.
- Interface shells add boundary structure.
- Segmented-region width and depth set where segmentation applies.
- Beam width, orientation, layer count, depth, and boundary avoidance define
  the mechanical key.

Use test coupons. Chemical compatibility and temperature remain decisive even
when geometry is interlocked.

Continue with the [Others tab](17-others-tab.md).
