# Glossary

**Acceleration**  
Rate at which toolhead speed changes, usually in `mm/s^2`. It affects pressure
transients, cornering, and whether a short move reaches its requested speed.

**Elephant foot**  
Enlargement of the lowest layers caused by Z compression, heat, or first-layer
flow. Correct it locally rather than scaling the whole part.

**Extrusion multiplier / flow ratio**  
A multiplier on commanded material. `1.00` is `100%`; `0.98` is `98%`.

**FFF / FDM**  
Layer-by-layer material-extrusion printing. FDM is a common industry term and a
Stratasys trademark; FFF is the generic term used by many open-source projects.

**Filament shrinkage compensation**  
A per-material model scale intended to offset proportional dimensional change
after cooling.

**Heat soak**  
Time or temperature condition used to let the bed, chamber, frame, and tool
reach a repeatable thermal state before calibration or printing.

**Line width**  
The nominal width of a deposited path. It influences required flow, geometry,
strength, and speed.

**Maximum volumetric speed (MVS)**  
The profile limit for requested plastic volume per second, in `mm^3/s`.

**Pressure Advance (PA) / Linear Advance**  
Firmware compensation for lag in nozzle pressure during speed changes.

**Retraction**  
Temporary reverse or relief motion in the extrusion path during non-print
travel, intended to reduce ooze.

**Seam**  
The start/stop transition where a perimeter closes or a new layer begins.

**Top-surface flow**  
A feature-specific multiplier applied to top solid infill, usually multiplied
by the global filament flow ratio.

**Volumetric flow**  
Requested deposited volume per second:

```text
Q = speed * line width * layer height
```

**XY contour compensation**  
A near-constant offset applied to external contours.

**XY hole compensation**  
A near-constant offset applied to internal holes or contours.

## Formula Reference

```text
volumetric flow = speed * line width * layer height

maximum speed = MVS / (line width * layer height)

measured percentage = measured dimension / nominal dimension * 100

effective correction scale = 100 / measured percentage

effective feature flow = global flow ratio * feature flow ratio
```

