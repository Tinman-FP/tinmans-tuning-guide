# Slicer Upgrades and Calibration Changes

> **At a glance**
> - **Decide:** what to re-test after a slicer update
> - **Test:** re-slice your last test in the new build and compare the G-code
> - **Keep:** the old tune until a new result passes

An application update can change the experiment even when the preset name and
entered numbers stay the same. Separate a corrected generator, a changed
toolpath, a migrated preset, and an actual change in the filament's behavior.
This review was checked on **2026-11-21** against Tinman's source. It is not a
claim that every upstream feature has been physically validated.

## Which Application Are You Using?

Check **Help > About** and write the version and source revision into your
experiment record.

- **Tinman on OrcaSlicer 2.5.1.** Tinman's source moved to OrcaSlicer 2.5.1 on
  2026-11-15 (Tinman PR 20). The calibration menu, dialogs and generators are
  OrcaSlicer 2.5.1's with the Tinman fixes listed in
  [Running Tinman's Calibration Tests](25-running-tinman-calibrations.md#tinman-changes-to-the-upstream-tests).
  This edition of the guide describes this base.
- **Public Tinman previews.** The newest public downloads are Preview 5
  (`v2026.10.19-preview.5`) and the Preview 6 pre-release
  (`v2026.10.22-preview.6`). Both predate the 2.5.1 base: they are OrcaSlicer
  2.4.2 with selected 2.5 backports. Menus and dialogs can differ from this
  edition; when they do, regenerate tests and read the values from the G-code.
- **OrcaSlicer.** 2.5.0 (2026-11-07), 2.5.1 (2026-11-14) and 2.5.2
  (2026-11-21) are official releases. Everything in chapter 25 applies to
  2.5.1 except the Tinman-only lines. 2.5.2 was not reviewed for this edition.
- **TinmanX1** is the private experimental test bed. Historical custom-tool
  documentation is not a promise of inclusion in a public Tinman release.

## What the 2.5.1 Base Changed for Tuners

The October edition listed OrcaSlicer 2.5 changes that public Tinman did not
yet have. With the 2.5.1 base they are all present. The ones that change a
tuning experiment:

| Area | What changed | What to do |
| --- | --- | --- |
| PA Pattern, absolute extrusion | Extrusion reset corrected; no large unintended retraction | Regenerate old PA Pattern files; never reprint an old one |
| Retraction tower | Scarf seams disabled on the generated object | Check object overrides after generating |
| Temperature and VFA towers | Optional **Auto-scale for nozzle** resizes the tower and layer height; VFA can adjust to the filament's MVS | Record scale, layer height and range; do not reuse an old height-to-value formula |
| PA Tower and PA Line | Layer-based interpolation; PA Line reports its real footprint | Keep each specimen with its own G-code |
| Adaptive PA | Measurement input is validated; malformed models stop slicing | Keep a fixed PA as the control |
| Scarf seams | Tiny segments and ramp ends corrected | Re-slice a control before judging old scarf settings |
| Nozzle variants | Per-variant settings, including pressure advance | Audit every tool's resolved values on multi-tool printers |
| Tool-change retraction | Separate tool-change retraction settings | Tune travel and tool-change retraction separately |
| Seam placement | Precise seam placement modifiers | Hold seam position fixed while diagnosing pressure transitions |
| Features on "Default" | Use the object's own filament | Check feature-to-filament assignment on multi-material plates |
| Motion tests | Input shaping and cornering use machine limits; high test MVS | Keep calibration overrides out of production presets |
| Filament migration | **Help > Migrate Filament Presets** repairs compatibility after a backup | Reselect and verify the migrated preset |

Upstream sources: OrcaSlicer pull requests
[14473](https://github.com/OrcaSlicer/OrcaSlicer/pull/14473),
[15543](https://github.com/OrcaSlicer/OrcaSlicer/pull/15543),
[14759](https://github.com/OrcaSlicer/OrcaSlicer/pull/14759),
[14440](https://github.com/OrcaSlicer/OrcaSlicer/pull/14440),
[14198](https://github.com/OrcaSlicer/OrcaSlicer/pull/14198),
[15832](https://github.com/OrcaSlicer/OrcaSlicer/pull/15832),
[15986](https://github.com/OrcaSlicer/OrcaSlicer/pull/15986),
[15039](https://github.com/OrcaSlicer/OrcaSlicer/pull/15039),
[12974](https://github.com/OrcaSlicer/OrcaSlicer/pull/12974),
[13658](https://github.com/OrcaSlicer/OrcaSlicer/pull/13658),
[16367](https://github.com/OrcaSlicer/OrcaSlicer/pull/16367), and the
[OrcaSlicer releases](https://github.com/OrcaSlicer/OrcaSlicer/releases).
None of these approves a numerical material value.

## Tinman Changes That Affect Tuning

| Tinman PR | Change | Why it matters |
| --- | --- | --- |
| 53 | Retraction-tower bands are exactly 1 mm; PA Pattern preview tags follow the printer | Older retraction towers had uneven bands; read them from G-code comments |
| 32 | Presets that tuned profiles inherit from are kept in a local layer when a vendor bundle is updated | Before this, an update could delete a profile's parent so it no longer loaded |
| 6, 9, 13, 15 | **Printer scope** when saving; move or import profiles onto one physical printer | A tune made on one printer does not appear for another |
| 35, 45 | Names containing `|` can be saved (macOS) | Windows still forbids `|` in file names; use ` - ` |
| 52 | Opening a project no longer marks the printer preset modified | Fewer false "unsaved changes" prompts |
| 48 | Prime tower is kept off objects; warning before slicing | Fewer failed multi-material starts |

Pull requests are in the [Tinman repository](https://github.com/Tinman-FP/Tinman/pulls?q=is%3Apr+is%3Amerged).

## New Controls Do Not Replace the Tuning Order

New settings are tempting during a stalled tune. Leave unrelated
transformations (plugins, textured geometry, color mixing, new infill options,
belt printing, parallel multi-tool printing) out of a baseline. For intentional
use, record versions, generated geometry, tool mapping and mode, then validate
a representative part.

On multi-tool printers, a scalar setting inherited across nozzle variants is
shared: selecting another nozzle does not prove each value was tuned for it.

## Saving a Calibration Is Not Saving Its Schedule

A tower calibration's ramp (its start, end and step) lives in memory, not in
the project file. Reopening a saved temperature, max-flowrate, PA-tower,
retraction or VFA project restores the model and presets but slices it at a
single value. PA Pattern and flow-ratio coupons keep their values in the
project. This is confirmed in Tinman's current
source and was seen in field runs: a reopened PA test sliced at one constant
PA, and a reopened retraction tower at one length throughout.

Keep the audited G-code with the specimen. To repeat a test, generate it again
from the Calibration menu and check the preview before printing.

## Revalidate Toolpaths, Not Only Entered Values

Several upstream changes alter what an unchanged preset produces:

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

Keep old specimens and G-code as evidence; regenerate new work. Do not change
five profile values to compensate for one changed toolpath.

## Re-slice and Compare After Every Update

The field runs used one simple habit after every new build: re-slice the last
completed test in the new build and compare the executable G-code with the old
file. Twice during the K2 Plus run the comparison was identical apart from
timestamps and one comment, so the next result could be compared with the old
ones. Had it differed, the difference would have been explained first.

On printers that change settings at start, compare the printer's live state
too. The last command wins: a printer's own start routine can replace a value
the slicer sent.

## Profiles Across Updates

Tuned profiles usually inherit from a printer or process preset that came with
the slicer. Updates can move or remove those parents.

- **Back up first.** Copy your user profiles (and the printer and process
  presets they inherit from) before installing a new build.
- **Check the parents after updating.** A profile whose parent is gone does not
  load, or loads with defaults. Before Tinman PR 32, updating a vendor's
  bundle deleted presets that user profiles depended on; current Tinman keeps
  them in a local layer.
- **Bundles can also change stock values under you.** If a tuned filament does
  not set its own retraction, a newer printer bundle with a different stock
  retraction changes the filament's effective retraction. Set the values that
  matter in your own profile.
- **Command-line slicing resolves parents differently.** In one run, slicing
  from the command line with only user presets available silently fell back
  to default walls, widths and layer heights. Writing the important values into
  the tuned process explicitly fixed it. Compare a CLI slice with a GUI slice
  before trusting either.
- **Migration.** **Help > Migrate Filament Presets** repairs filament
  compatibility after making a backup. Reselect the migrated preset and verify
  its effective settings. Never substitute a similar generic material for a
  missing machine-specific tune.

Sources: [migration, 16367](https://github.com/OrcaSlicer/OrcaSlicer/pull/16367),
[follow-up, 16523](https://github.com/OrcaSlicer/OrcaSlicer/pull/16523),
[filament identity, 15513](https://github.com/OrcaSlicer/OrcaSlicer/pull/15513),
[CLI loading, 15438](https://github.com/OrcaSlicer/OrcaSlicer/pull/15438).

## A Controlled Upgrade Procedure

1. Back up application identity, profiles and parents, a representative project,
   final G-code, and accepted evidence. Keep a rollback.
2. Record the new tag/source revision and actual data directory. Confirm that
   a second installed copy is not the app you launched.
3. Select the physical machine, installed nozzle, process, and filament
   explicitly in a fresh project. Compare against your saved profiles; copied
   data is not necessarily current.
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
