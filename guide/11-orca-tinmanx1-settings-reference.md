# OrcaSlicer and TinmanX1 Settings Reference

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

This edition was checked against the following fixed references on
2026-09-21:

| Reference | Version or revision | What it establishes |
| --- | --- | --- |
| OrcaSlicer application source | `v2.4.2`, commit `8500fcdccaa10b5099ac20d252af3a7c560046f1` | The upstream 2.4.2 process tabs and controls |
| OrcaSlicer Wiki | commit `f132cbf1c1e48573d229d1783ee471e61e50aaf3`, dated 2026-09-17 | Current upstream terminology and supporting context |
| TinmanX1 source | upstream-compatible version `2.4.2`, commit `cf0cabb04146c4ff9f21b963517717acfec66055` | The TinmanX1 UI, fiber planner, Strength Lens, and Wave Overhang extensions |
| Installed TinmanX1 application | `CFBundleShortVersionString 2.4.2` | The application version visible to the user |

TinmanX1 keeps the OrcaSlicer `2.4.2` version number because that is its
compatibility base. The TinmanX1 commit is therefore the more precise identity
for custom features. A later TinmanX1 build may show the same application
version while containing newer custom work.

Official download pages:

- [OrcaSlicer releases](https://github.com/SoftFever/OrcaSlicer/releases/latest)
- [TinmanX1 releases](https://github.com/Tinman-FP/TinManX1/releases/latest)

The links intentionally point to each project's latest public release. Compare
the downloaded version with the fixed documentation baseline above before
assuming every screen and option will be identical.

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

These labels describe the stated source revisions, not every older or future
release. A setting added to OrcaSlicer after 2.4.2 may later become shared.

<!-- pdf:page-break-before -->

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
