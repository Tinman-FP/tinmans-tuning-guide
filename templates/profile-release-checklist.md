# Filament Profile Release Checklist

## Traceability

- [ ] Filament identity, color, lot, and condition are recorded.
- [ ] Printer, tool, nozzle, firmware, and slicer versions are recorded.
- [ ] The installed physical tool and nozzle match the printer definition.
- [ ] Resolved layer heights and line widths are credible for that nozzle.
- [ ] The filament profile is compatibility-gated to this machine/tool/nozzle.
- [ ] Parent printer and process profiles are identified.
- [ ] Every promoted value links to an accepted experiment.
- [ ] Project files, final G-code, photos, and measurements are preserved.
- [ ] Profile purpose and known limitations are stated.
- [ ] Selections and overrides were rechecked after imports, sync, calibration
      generation, resets, and reopening.
- [ ] No calibration test values (raised MVS, start temperature, layer time)
      were saved into the profile.
- [ ] The pass marks written before tuning are met, or each exception is noted.

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

## Validation

- [ ] Broad top surface passes.
- [ ] External X/Y/Z dimensions pass after cooling.
- [ ] Internal holes and required fits pass.
- [ ] Elephant foot is within the defined limit.
- [ ] Bridges, overhangs, and small features pass.
- [ ] VAL01 (chapter 09) passes every check A–H; the tightest sliding pin
      is recorded.
- [ ] Representative production part passes.
- [ ] Mechanical comparison passes where strength matters.
- [ ] G-code review confirms the expected tool, temperatures, fans, PA, flow,
      MVS, mesh, offsets, and compensation.
- [ ] G-code contains no unintended tool-change, fiber, auxiliary, or
      calibration commands.
- [ ] Start, transition, and end G-code map every load, purge, cutter, and
      unload operation to the intended physical tool path.
- [ ] The printer was homed before launch and live state confirms the intended
      uploaded file is executing.
- [ ] Important emitted commands agree with effective live firmware state where
      that state is available.
- [ ] A clean project reproduces the result without calibration overrides.

## Release

- [ ] The tested candidate passed all required stages for this exact setup.
- [ ] Filament and process use `TUNED - Machine ID - Nozzle mm - Brand Product
      Material - ... - rNN` (no `|`), including layer height/purpose for the
      process.
- [ ] IDs, inheritance, compatibility, and project/printer associations resolve
      correctly after promotion and reopening.
- [ ] One recommended current pair is recorded for this scope; deliberate
      Quality/Draft/Strength alternatives are clearly distinguished.
- [ ] Replaced user presets have a recoverable backup and old-to-new mapping,
      and are hidden from active choices or labeled `RETIRED - DO NOT USE`.
- [ ] Shared parents, other machines' presets, and active jobs remain intact.

### Optional: shared printers and automated tuning

For labs, shared installations, or tuning run by scripts or assistants:

- [ ] Each physical print used its own project with no other printer's state
      carried into the job, and no two slicer windows shared one data folder.
- [ ] Session owner, app version, data directory, printer, and job identity are
      recorded; whoever started a job is responsible for its cleanup.
- [ ] Copied profiles match the authoritative machine tuning record, not merely
      the newest file timestamp.

```text
Profile name:
Recommended filament/process pair:
Version:
Optimization target:
Release date:
Author / reviewer:
Accepted operating envelope:
Known limitations:
Supersedes:
```
