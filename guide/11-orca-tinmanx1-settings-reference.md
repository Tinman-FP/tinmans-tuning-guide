# OrcaSlicer and Tinman Settings Reference

> **At a glance**
> - **Decide:** which settings group matches a symptom
> - **Test:** the tab chapters that follow, starting from the symptom
> - **Keep:** one change per print, and the default when there is no evidence

This part of the guide translates the process-profile screens into practical
decisions. It is not a replacement for calibration and it is not a rewritten
copy of the OrcaSlicer Wiki. Each setting group answers three questions:

1. **What does this group control?**
2. **When should you use it?**
3. **What result should you be trying to produce?**

The control maps name the settings found in the interface, but the advice is
organized around print evidence. If a part does not show the symptom described
for a group, leave that group alone.

## Version Basis

The current release review was checked on 2026-11-21 against Tinman's source.
The detailed tab survey in chapters 12–18 keeps its explicitly identified
historical source baseline; changed behavior is documented in
[Slicer Upgrades and Calibration Changes](21-slicer-upgrades-and-calibration-changes.md)
and [Running Tinman's Calibration Tests](25-running-tinman-calibrations.md).

| Reference | Version or revision | What it establishes |
| --- | --- | --- |
| Tinman source, `main` | `baf3f00dfe` (2026-11-21), on the OrcaSlicer 2.5.1 base since 2026-11-15 | Calibration menu, dialogs, generators and filament-setting labels described in this edition |
| OrcaSlicer releases | `v2.5.0` (2026-11-07), `v2.5.1` (2026-11-14), `v2.5.2` (2026-11-21) | Current official upstream; 2.5.2 not reviewed for this edition |
| Public Tinman previews | Preview 5 `v2026.10.19-preview.5`; Preview 6 pre-release `v2026.10.22-preview.6` | Public downloads that predate the 2.5.1 base (2.4.2 with selected backports) |
| OrcaSlicer application source (historical survey) | `v2.4.2`, commit `8500fcdccaa10b5099ac20d252af3a7c560046f1` | The 2.4.2 process tabs and controls surveyed for chapters 12–17 |
| OrcaSlicer Wiki survey (historical) | commit `f132cbf1c1e48573d229d1783ee471e61e50aaf3`, dated 2026-09-17 | Historical tab terminology |
| Historical TinmanX1 source | compatibility base 2.4.2, commit `cf0cabb04146c4ff9f21b963517717acfec66055` | The original custom-feature survey, not a public-download promise |

Record the product version, release tag, and source revision shown in
**Help > About**, not just a number embedded in an exported preset. TinmanX1
remains the private experimental test bed.

Official download pages:

- [OrcaSlicer releases](https://github.com/SoftFever/OrcaSlicer/releases/latest)
- [Public Tinman releases](https://github.com/Tinman-FP/Tinman/releases)

Use the releases list to distinguish stable and preview builds. Compare
the downloaded version with the baseline above before assuming every screen
and option will be identical.

## Difference Labels

- **Shared 2.4.2:** the group and surveyed controls are present in both
  OrcaSlicer 2.4.2 and the TinmanX1 baseline.
- **TinmanX1 addition:** the group or control is part of TinmanX1 and is not in
  upstream OrcaSlicer 2.4.2.
- **Profile contract:** the field describes hardware or saved planner data. It
  normally belongs to a validated printer, filament, or process preset rather
  than routine user tuning.
- **Experimental:** preview the sliced paths and validate on a disposable test
  before using the feature on a valuable print.

These labels describe the original tab-survey revisions, not every older or
future release. **TinmanX1 addition** is historical provenance, not proof that
the feature is available or validated in public Tinman. The upgrade chapter
takes precedence for changed behavior. A control documented for OrcaSlicer 2.5
exists in Tinman on the 2.5.1 base, but not necessarily in the older public
previews.

## Scope

The following chapters cover every process-profile tab and group in the
reference builds:

- [Quality](12-quality-tab.md)
- [Strength](13-strength-tab.md)
- [Speed](14-speed-tab.md)
- [Support](15-support-tab.md)
- [Multimaterial](16-multimaterial-tab.md)
- [Others](17-others-tab.md)
- [TinmanX1 fiber and strength tools](18-tinmanx1-fiber-and-strength-tools.md)

The last chapter also explains the continuous-fiber fields in the TinmanX1
filament and FibreSeek printer profiles. Those fields are outside the ordinary
process tabs, but they are included because a complete fiber setup depends on
all three profile layers.

## How to Use the Reference

Start with the symptom, not the menu. Read the group-level **What**, **Use it
when**, and **Desired result** statements. Change the smallest relevant control,
slice again, and inspect the preview before printing. Preserve a control sample
and avoid changing material flow, geometry compensation, and path generation in
the same experiment.

Expert mode exposes more controls but does not make them equally useful. Zero
often means "inherit," "automatic," or "disabled," depending on the field.
Confirm the field's units and preview the effect instead of assuming that zero
has one universal meaning.

Continue with the [Quality tab](12-quality-tab.md).
