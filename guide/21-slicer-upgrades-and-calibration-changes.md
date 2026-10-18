# Slicer Upgrades and Calibration Changes

An application update can change the experiment even when the preset name and
entered numbers stay the same. Separate a corrected generator, a changed
toolpath, a migrated preset, and an actual change in the filament's behavior.
This review covers tuning-relevant changes checked on **2026-10-18**, not a
claim that every upstream feature has been ported or physically validated.

## Which Application Are You Using?

- **Public Tinman:** `v2026.10.17-preview.4`, source
  `90e25afac2f79bc38f9018442e0a028587d89d53`. Preview 4 retains the selected
  Orca fixes introduced in Preview 3 and separates Tinman branding/versioning
  from the older compatibility metadata.
- **OrcaSlicer stable:** `v2.4.2` remains the latest stable release at this
  review date. Its calibration behavior is not automatically the alpha's.
- **OrcaSlicer preview:** `v2.5.0-alpha`, released 2026-10-16, is a testing
  release. Use a backed-up, separate experiment before moving production work.
- **TinmanX1:** the private experimental test bed. Historical custom-tool
  documentation is not a promise of inclusion in a public Tinman release.

Use the [public Tinman release page](https://github.com/Tinman-FP/Tinman/releases/tag/v2026.10.17-preview.4)
for downloads. At review time its published binary is macOS Apple Silicon;
other CI outputs are not equivalent to published, qualified installers.
See the [pinned Tinman upstream review](https://github.com/Tinman-FP/Tinman/blob/90e25afac2f79bc38f9018442e0a028587d89d53/docs/ORCA_2_5_REVIEW.md)
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

## Additional Orca Alpha Calibration Changes

The following are **upstream alpha changes, not documented Tinman backports**.
Calibration-family names can match while the generated experiment differs.

### Temperature and VFA

Nozzle-aware scaling and a flow-limited VFA generator change test geometry and
attainable speeds. Record actual layer height, width, scale, MVS, and speed
range after generation. A requested high speed is not evidence that the nozzle
sustained it. Compare like geometry or label the result as a different
experiment. Do not infer a temperature optimum from a flow-starved section.

Source: [nozzle-aware calibration, 14759](https://github.com/OrcaSlicer/OrcaSlicer/pull/14759).

### Pressure Advance

PA Line uses a tighter reported footprint; PA Tower step geometry changes.
Keep each specimen's generated mapping rather than reusing a remembered height
formula. A different adaptive-mesh area can change the first-layer context of
a line test, so check that before comparing line quality. Adaptive-PA input
validation checks measurement structure; valid syntax is not physical
validation. Keep fixed PA as the control and qualify adaptive behavior on the
actual firmware before production use.

Sources: [PA Line, 14440](https://github.com/OrcaSlicer/OrcaSlicer/pull/14440),
[tower changes, 14759](https://github.com/OrcaSlicer/OrcaSlicer/pull/14759), and
[adaptive input validation, 14198](https://github.com/OrcaSlicer/OrcaSlicer/pull/14198).

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
validate a representative part. These are not blanket Tinman Preview 4
capabilities. See the upstream release notes linked above.

<!-- pdf:page-break-before -->

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
not a Tinman Preview 4 instruction. Preserve the original user data and projects
before migration, and verify printer/slot assignments after synchronization.
Sources: [migration, 16367](https://github.com/OrcaSlicer/OrcaSlicer/pull/16367),
[follow-up, 16523](https://github.com/OrcaSlicer/OrcaSlicer/pull/16523), and
[filament identity, 15513](https://github.com/OrcaSlicer/OrcaSlicer/pull/15513).

For command-line slicing, compare resolved inheritance and dimensional
compensation against the GUI before substituting its output. Upstream alpha
changes CLI profile resolution; identical filenames do not guarantee equivalent
settings across versions. Source: [CLI loading, 15438](https://github.com/OrcaSlicer/OrcaSlicer/pull/15438).

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
