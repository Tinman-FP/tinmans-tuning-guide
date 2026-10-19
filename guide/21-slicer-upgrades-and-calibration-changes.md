# Slicer Upgrades and Calibration Changes

An application update can change the experiment even when the preset name and
entered numbers stay the same. Separate a corrected generator, a changed
toolpath, a migrated preset, and an actual change in the filament's behavior.
This review covers tuning-relevant changes checked on **2026-10-19**, not a
claim that every upstream feature has been ported or physically validated.

## Which Application Are You Using?

- **Public Tinman Preview 5:** `v2026.10.19-preview.5`, source `eb1bd6d028`,
  with calibration/build changes at `b0db6431c5`. It retains Previews 3/4 fixes
  and adds the batch below. Packaged macOS calibration exports were checked;
  platform build results are linked in the release. These software checks do
  not approve a material tune or qualify every printer connection.
- **OrcaSlicer stable:** `v2.4.2` remains the latest stable release at this
  review date. Its calibration behavior is not automatically the alpha's.
- **OrcaSlicer preview:** `v2.5.0-alpha`, released 2026-10-16, is a testing
  release. Use a backed-up, separate experiment before moving production work.
- **TinmanX1:** the private experimental test bed. Historical custom-tool
  documentation is not a promise of inclusion in a public Tinman release.

Use the [public Tinman release page](https://github.com/Tinman-FP/Tinman/releases/tag/v2026.10.19-preview.5)
for downloads and the tested-platform scope. A successful platform build is not
an interactive test on every operating system or a physical printer validation.
See the [revision-pinned Tinman upstream review](https://github.com/Tinman-FP/Tinman/blob/eb1bd6d028/docs/ORCA_2_5_REVIEW.md)
and [Orca release notes](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/v2.5.0-alpha)
for provenance. Application branding is not a profile-format migration.

## Fixes Included in Public Tinman

These selected backports are also in Orca 2.5 alpha:

| Area | Changed behavior | What the tuner should do |
| --- | --- | --- |
| PA Pattern, absolute E | Corrected extrusion reset avoids a large unintended retraction | Regenerate old calibration G-code; verify E mode and resets |
| Retraction tower | Generated object has scarf seams disabled | Check object overrides; the saved production preset is unchanged |
| Calibration model loading | Failed/canceled loads stop affected generators | Retry from a clean project; a canceled generator produces no usable new result |
| Scarf path planning | Tiny segments and ramp endpoints are corrected to reduce planner speed dips | Re-slice the control before changing flow, PA, or seams |
| Bambu LAN help | Missing printer artwork no longer causes the affected crash | Separate onboarding repair from nozzle or filament calibration |

Sources: Orca changes [14473](https://github.com/OrcaSlicer/OrcaSlicer/pull/14473),
[15543](https://github.com/OrcaSlicer/OrcaSlicer/pull/15543),
[14546](https://github.com/OrcaSlicer/OrcaSlicer/pull/14546),
[15832](https://github.com/OrcaSlicer/OrcaSlicer/pull/15832), and
[16191](https://github.com/OrcaSlicer/OrcaSlicer/pull/16191), plus the pinned
Tinman review above. No numerical material tune is approved by these fixes.

## New in Tinman Preview 5

The following selected Orca alpha changes are implemented in Preview 5, with additional
Tinman validation and boundary checks. Calibration-family names can match
older versions while the generated experiment differs. Regenerate test files.

### Temperature and VFA

Optional nozzle-aware resizing changes temperature/VFA tower geometry. With
resizing off, retain and record the selected process layer height; with it on,
record the generated scale and layer height rather than assuming the previous
tower dimensions. Do not reuse a height-to-value formula from another build.

For VFA, select the intended nozzle, process and filament before generation.
Keep the filament's validated maximum volumetric speed (MVS). With both
**Auto-scale for nozzle** and **Auto-adjust to max volumetric speed** enabled,
flow-limit adjustment selects a compatible layer height, then proposes a lower
end speed if needed. The new endpoint stays on the requested speed-step grid.
If even the first two blocks are unreachable, generation stops: reduce the
requested range or revise the test geometry, not the validated MVS merely to
make the warning disappear.

With resizing disabled, the generator warns instead of automatically changing
the process layer height. If you explicitly continue after a flow warning,
label the result **flow-clamped**. Inspect sliced speed and volumetric flow;
the requested speed is not proof of the executed speed. Record actual layer
height, width, scale, MVS, and range after generation. Compare like geometry or
label it a different experiment. Do not infer a temperature optimum from a
flow-starved section.

Source: [nozzle-aware calibration, 14759](https://github.com/OrcaSlicer/OrcaSlicer/pull/14759).

### Pressure Advance

PA Line reports its actual footprint, including optional numbers and line
width. Preview extrusion thickness is distinct from absolute Z height. PA
Tower uses bounded, layer-count-based interpolation. Temperature towers divide
the sliced layers across the requested temperature steps; they do not use a
fixed 25-layer band. In the packaged 0.4 mm nozzle check, a 230/225/220 C tower
used 50 layers per temperature at 0.20 mm, and 63/62/62 layers at 0.16 mm with
resizing disabled. VFA geometry targets 25-layer speed blocks; inspect the
exported boundaries, including first-layer and rounding effects.
Keep each specimen's generated mapping rather than reusing a remembered height
formula. A different adaptive-mesh area can change the first-layer context of
a line test, so check that before comparing line quality. Adaptive-PA input
validation checks each filament's measurement structure. Each measurement row
contains PA, flow, and acceleration; incomplete, malformed or nonfinite numbers
are rejected. Enabled malformed models also fail slice validation. Valid
syntax is not physical validation, and quantities with different units must
not be compared numerically to each other. Read the Prusa firmware warning
where shown; keep fixed PA as the control and qualify adaptive behavior on the
actual firmware before production use. Clearer field labels do not change an
existing physical tune.

Sources: [PA Line, 14440](https://github.com/OrcaSlicer/OrcaSlicer/pull/14440),
[tower changes, 14759](https://github.com/OrcaSlicer/OrcaSlicer/pull/14759), and
[adaptive input validation, 14198](https://github.com/OrcaSlicer/OrcaSlicer/pull/14198),
[Prusa warning, 14271](https://github.com/OrcaSlicer/OrcaSlicer/pull/14271), and
[measurement labels, 14411](https://github.com/OrcaSlicer/OrcaSlicer/pull/14411).

### Upload Diagnostics

Moonraker upload failures now expose readable server error details where
available. Save the returned message and job identity before retrying. This
does not alter authentication, firmware, or whether a printer is reachable.
Source: [upload errors, 14841](https://github.com/OrcaSlicer/OrcaSlicer/pull/14841).

### Saving a Calibration Is Not Saving Its Schedule

In the Preview 5 packaged-app check, reopening a saved VFA project preserved
the model and presets, but re-slicing did **not** restore its speed sweep.
The calibration schedule is runtime state, not a guaranteed part of a project
3MF. Keep the audited final G-code (or sliced G-code 3MF), generator inputs,
application revision, and specimen together. To repeat or revise the test,
generate it again from the Calibration menu and inspect the exported commands.
Do not print a re-sliced calibration project merely because its tower still
looks correct. This finding is not evidence that every Orca version has the
same behavior; verify the build you use.

## Orca Alpha Changes Not Included in This Tinman Batch

### Motion and Volumetric Limits

Input-shaping and cornering generators use machine limits, and affected tests
retain high MVS values rather than applying the previous ceiling. Audit those
configured limits. A larger software range is not a new mechanical or hotend
rating. Preserve the production MVS margin and keep calibration overrides out
of the approved production preset.

Source: [calibration limits, 13658](https://github.com/OrcaSlicer/OrcaSlicer/pull/13658).

## New Controls Do Not Replace the Tuning Order

**Nozzle variants and multiple tools:** upstream alpha expands mixed-nozzle
handling and per-variant settings. Audit each tool's resolved temperature,
cooling, PA, geometry, and material assignment. A scalar inherited setting can
be shared across variants; selecting another nozzle does not prove that every
value is independently tuned. Source: [per-nozzle settings, 15986](https://github.com/OrcaSlicer/OrcaSlicer/pull/15986).

**Seam placement:** precise seam modifiers add a placement method. Hold the
location fixed while diagnosing pressure transitions; moving a defect out of
view is not correcting it. Source: [precise seams, 12974](https://github.com/OrcaSlicer/OrcaSlicer/pull/12974).

**Retraction:** new tool-change controls add another override layer. Qualify
normal travel and tool changes separately, then inspect both in the executable
file. Do not copy a tool-change distance into ordinary travel retraction.
Source: [filament tool-change retraction, 15039](https://github.com/OrcaSlicer/OrcaSlicer/pull/15039).

**Path-changing features:** plugins, textured geometry, color mixing, new
infill options, belt printing, and parallel multi-tool printing can change the
test itself. Leave unrelated transformations out of a baseline. For intentional
use, record plugin versions, generated geometry, tool mapping, and mode, then
validate a representative part. These are not blanket Tinman Preview 5
capabilities. See the upstream release notes linked above.

## Revalidate Toolpaths, Not Only Entered Values

Several upstream alpha fixes change what an unchanged preset produces:

- Wall ordering and outline consistency can change. Compare perimeter count,
  direction, width, and order before interpreting a surface change as a new
  flow optimum. Sources: [narrow walls, 16174](https://github.com/OrcaSlicer/OrcaSlicer/pull/16174)
  and [outline consistency, 15316](https://github.com/OrcaSlicer/OrcaSlicer/pull/15316).
- Overhang speed/fan targeting and bridge-flow re-slicing can change the
  effective experiment. Inspect feature types, speed, cooling, and deposited
  flow in the affected region; test bridges as well as ordinary walls.
  Sources: [overhang targeting, 15945](https://github.com/OrcaSlicer/OrcaSlicer/pull/15945)
  and [bridge-flow invalidation, 15626](https://github.com/OrcaSlicer/OrcaSlicer/pull/15626).
- Support-interface behavior can change. Recheck layer count, material, contact
  gap, and removal quality before trusting an old support result.
  Source: [support interfaces, 14678](https://github.com/OrcaSlicer/OrcaSlicer/pull/14678).

These are not additional Tinman backports. Keep old specimens and G-code as
evidence; regenerate new work. Do not change five profile values to compensate
for one changed toolpath.

## Profile Migration and Missing Filaments

A catalog update can rename parents or alter identity and compatibility
without changing the spool. Orca 2.5 alpha's migration workflow can repair
compatibility after making a preset backup. Reselect the migrated preset and
verify effective settings. Never substitute a similar generic material for a
missing machine-specific tune without resolving inheritance and compatibility.

Use **Help > Migrate Filament Presets** only in a build providing it. This is
not a Tinman Preview 5 instruction. Preserve the original user data and projects
before migration, and verify printer/slot assignments after synchronization.
Sources: [migration, 16367](https://github.com/OrcaSlicer/OrcaSlicer/pull/16367),
[follow-up, 16523](https://github.com/OrcaSlicer/OrcaSlicer/pull/16523), and
[filament identity, 15513](https://github.com/OrcaSlicer/OrcaSlicer/pull/15513).

For command-line slicing, compare resolved inheritance and dimensional
compensation against the GUI before substituting its output. Upstream alpha
changes CLI profile resolution; identical filenames do not guarantee equivalent
settings across versions. Source: [CLI loading, 15438](https://github.com/OrcaSlicer/OrcaSlicer/pull/15438).

<!-- pdf:page-break-before -->

## A Controlled Upgrade Procedure

1. Back up application identity, profiles and parents, a representative project,
   final G-code, and accepted evidence. Keep a rollback.
2. Record the new tag/source revision and actual data directory. Confirm that
   a second installed copy is not the app you launched.
3. Use a fresh job-owned session. Select the physical machine, installed nozzle,
   process, and filament explicitly. Compare against the authoritative library;
   copied data is not necessarily current. Preserve other live sessions.
4. Recheck after project imports, device sync, calibration generation, and
   reopening. Record object overrides and intentional test limits.
5. Re-slice an unchanged control. Compare tools, geometry, speeds, volumetric
   limits, PA, retraction, temperatures, fans, and start/end commands. Profile
   names alone are not the comparison.
6. Repeat tests affected by changed behavior. Finish with a cooled, measured
   functional part. Retain the old tune until the new result passes; an
   application upgrade alone does not justify changing its numerical values.
7. Promote the actual tested candidate. Retire only the superseded preset for
   that machine/nozzle/material/purpose, preserving dependencies and history.

Use [profile integrity](20-profile-integrity-and-experimental-resets.md) and the
[release checklist](../templates/profile-release-checklist.md) to record the
decision. A cosmetic version change requires identity verification; a changed
generator or planner requires evidence appropriate to its affected behavior.
