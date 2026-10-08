# Sources and Further Reading

This guide favors official documentation and well-documented experimental work.
Pages can change over time, so record the access date when using a source for a
formal experiment or publication.

Last source review: 2026-10-07.

## Prusa Research

- [Extrusion multiplier calibration](https://help.prusa3d.com/article/extrusion-multiplier-calibration_2257)
- [Drying filament](https://help.prusa3d.com/article/drying-filament_332086)
- [Warping](https://help.prusa3d.com/article/warping_2011)
- [ABS material guide](https://help.prusa3d.com/article/abs_2058)
- [Under-extrusion](https://help.prusa3d.com/article/under-extrusion_2007)
- [Calibration index](https://help.prusa3d.com/category/calibration_199)
- [CORE One, CORE One L, and CORE One INDX belt alignment and tension](https://help.prusa3d.com/article/adjusting-belt-tension-core-one-core-one-indx-core-one-l_845048)
- [CORE One L+ belts upgrade](https://help.prusa3d.com/guide/3-belts-upgrade_1178740)
- [CORE One L selftest and X-rail settling](https://help.prusa3d.com/article/selftest-failed-core-one-l_972648)
- [CORE One family X-homing and motor-pulley checks](https://help.prusa3d.com/article/homing-error-x-31304-core-one-35304-core-one-l-36304-core-one-indx-17304-xl_857401)
- [GT1.5 21-tooth pulley](https://www.prusa3d.com/product/pulley-gt1-5-21t/)
- [CORE One and CORE One L phase stepping](https://help.prusa3d.com/article/phase-stepping-core-one-l-core-one_914247)
- [Input Shaper](https://help.prusa3d.com/article/input-shaper-core-one-mk4-s-mk3-9-s-mk3-5-s-xl-mini_451816)
- [Firmware 6.8.1 release and CORE One L+ GT1.5 support](https://github.com/prusa3d/Prusa-Firmware-Buddy/releases/tag/v6.8.1)

Prusa documents both visual and measured extrusion-multiplier methods. This
guide recommends the visual/tactile top-surface method for routine filament
flow tuning, while using dimensions and fit tests for geometry.

## OrcaSlicer

The application comparison in the settings reference is based on OrcaSlicer
`v2.4.2`, source commit `8500fcdccaa10b5099ac20d252af3a7c560046f1`.
The terminology review used the official OrcaSlicer Wiki at commit
`f132cbf1c1e48573d229d1783ee471e61e50aaf3`, dated 2026-09-17. Fixing these
revisions makes later UI changes distinguishable from errors in this edition.

- [Calibration overview](https://github.com/OrcaSlicer/OrcaSlicer/wiki/Calibration)
- [Official OrcaSlicer downloads](https://github.com/SoftFever/OrcaSlicer/releases/latest)
- [Temperature calibration](https://github.com/OrcaSlicer/OrcaSlicer/wiki/temp_calib)
- [Pressure-advance calibration](https://github.com/OrcaSlicer/OrcaSlicer/wiki/pressure_advance_calib)
- [Flow ratio and pressure advance settings](https://github.com/OrcaSlicer/OrcaSlicer/wiki/material_flow_ratio_and_pressure_advance)
- [Material information and shrinkage](https://github.com/OrcaSlicer/OrcaSlicer/wiki/material_basic_information)
- [Precision and XY compensation](https://github.com/OrcaSlicer/OrcaSlicer/wiki/quality_settings_precision)
- [Tolerance calibration](https://github.com/OrcaSlicer/OrcaSlicer/wiki/tolerance-calib)
- [Seam settings](https://github.com/OrcaSlicer/OrcaSlicer/wiki/quality_settings_seam)
- [Line-width settings](https://github.com/OrcaSlicer/OrcaSlicer/wiki/quality_settings_line_width)
- [Top and bottom shell settings](https://github.com/OrcaSlicer/OrcaSlicer/wiki/strength_settings_top_bottom_shells)
- [Infill and surface pattern reference](https://github.com/OrcaSlicer/OrcaSlicer/wiki/strength_settings_patterns)
- [VFA calibration](https://github.com/OrcaSlicer/OrcaSlicer/wiki/vfa_calib)

## Firmware Documentation

- [Klipper pressure advance](https://www.klipper3d.org/Pressure_Advance.html)
- [Klipper resonance compensation](https://www.klipper3d.org/Resonance_Compensation.html)
- [Klipper accelerometer-based resonance measurement](https://www.klipper3d.org/Measuring_Resonances.html)
- [Klipper ringing-tower test model](https://github.com/Klipper3d/klipper/blob/master/docs/prints/ringing_tower.stl)
- [Marlin Linear Advance](https://marlinfw.org/docs/features/lin_advance.html)

Firmware implementations use different commands and numeric ranges. Never copy
a pressure-advance value between firmware families without recalibrating.

## Experimental Guides

- [Ellis' Print Tuning Guide](https://ellis3dp.com/Print-Tuning-Guide/)
- [Ellis: extrusion multiplier](https://ellis3dp.com/Print-Tuning-Guide/articles/extrusion_multiplier.html)
- [Ellis: determining maximum volumetric flow](https://ellis3dp.com/Print-Tuning-Guide/articles/determining_max_volumetric_flow_rate.html)
- [Ellis: common misconceptions](https://ellis3dp.com/Print-Tuning-Guide/articles/misconceptions.html)
- [CNC Kitchen: extrusion-system benchmark tool](https://www.cnckitchen.com/blog/extrusion-system-benchmark-tool-for-fast-prints)

These authors emphasize empirical testing and distinguish melt-capacity limits
from commanded extrusion. Their exact methods and conclusions should be read at
the source before reproducing a formal benchmark.

## Motion-System Mechanics

- [CoreXY kinematic theory](https://corexy.com/theory.html)
- [Gates PowerGrip GT3 drive-design manual](https://www.gates.com/content/dam/documents-library/catalogs/powergrip-gt3-drive-design-manual-en.pdf)
- [Gates light-power and precision-drive manual](https://www.gates.com/content/dam/documents-library/catalogs/light-power-and-precision-manual.pdf)
- [THK linear-guide mounting and maintenance](https://www.thk.com/us/en/products/lm_guide/maintenance/0002/)

The CoreXY transform and belt-drive references support the angle-to-loop and
tooth-order method in the motion-diagnostics chapter. They do not establish
that a matching frequency identifies one failed component; pulley, idler,
belt-plane, rail, and gantry interfaces still require controlled physical
inspection and a one-change repeat.

## Source Use

No source listed above endorses Tinmans Tuning Guide. This repository does not
bundle third-party calibration models or images. Follow each source's license
and attribution requirements before redistributing its files.

The settings chapters are an original operational interpretation. Upstream
documentation and source code were used to identify controls and behavior, then
the material was reorganized around diagnosis, appropriate use, and acceptance
criteria. Text was not copied from the OrcaSlicer Wiki.

## TinmanX1 Reference

The TinmanX1 comparison and custom-feature documentation are based on source
commit `cf0cabb04146c4ff9f21b963517717acfec66055`, whose application compatibility
version is `2.4.2`. The installed macOS application examined on 2026-09-21 also
reported `CFBundleShortVersionString 2.4.2`. TinmanX1 custom features documented
from that revision include continuous-fiber planning, FibreSeek profile
contracts, Strength Lens, and experimental Wave Overhangs.

- [Official public TinmanX1 downloads](https://github.com/Tinman-FP/TinManX1/releases/latest)
