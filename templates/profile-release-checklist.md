# Filament Profile Release Checklist

## Traceability

- [ ] Filament identity, color, lot, and condition are recorded.
- [ ] Printer, tool, nozzle, firmware, and slicer versions are recorded.
- [ ] Parent printer and process profiles are identified.
- [ ] Every promoted value links to an accepted experiment.
- [ ] Project files, final G-code, photos, and measurements are preserved.
- [ ] Profile purpose and known limitations are stated.

## Calibration Order

- [ ] Machine baseline and first layer are repeatable.
- [ ] Filament was dried or its known-dry condition was documented.
- [ ] Temperature optimum was bracketed, not selected at an untested endpoint.
- [ ] Maximum volumetric flow includes a suitable production margin.
- [ ] Pressure/Linear Advance was tuned at representative conditions.
- [ ] Global flow produces continuous surfaces without ridges.
- [ ] Feature-specific flow changes are justified separately.
- [ ] Cooling and bridge settings preserve required adhesion.
- [ ] Retraction is the shortest reliable value for the tested path.
- [ ] Dimensions were tuned only after extrusion stabilized.
- [ ] Seam settings were tuned after PA, flow, and retraction.

<!-- pdf:page-break-before -->

## Validation

- [ ] Broad top surface passes.
- [ ] External X/Y/Z dimensions pass after cooling.
- [ ] Internal holes and required fits pass.
- [ ] Elephant foot is within the defined limit.
- [ ] Bridges, overhangs, and small features pass.
- [ ] Representative production part passes.
- [ ] Mechanical comparison passes where strength matters.
- [ ] G-code review confirms the expected tool, temperatures, fans, PA, flow,
      MVS, mesh, offsets, and compensation.
- [ ] A clean project reproduces the result without calibration overrides.

## Release

```text
Profile name:
Version:
Optimization target:
Release date:
Author / reviewer:
Accepted operating envelope:
Known limitations:
Supersedes:
```
