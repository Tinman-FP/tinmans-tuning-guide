# Sources and Further Reading

This guide favors official documentation and well-documented experimental work.
Pages can change over time, so record the access date when using a source for a
formal experiment or publication.

Last source review: 2026-09-21.

## Prusa Research

- [Extrusion multiplier calibration](https://help.prusa3d.com/article/extrusion-multiplier-calibration_2257)
- [Drying filament](https://help.prusa3d.com/article/drying-filament_332086)
- [Warping](https://help.prusa3d.com/article/warping_2011)
- [ABS material guide](https://help.prusa3d.com/article/abs_2058)
- [Under-extrusion](https://help.prusa3d.com/article/under-extrusion_2007)
- [Calibration index](https://help.prusa3d.com/category/calibration_199)

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

## Firmware Documentation

- [Klipper pressure advance](https://www.klipper3d.org/Pressure_Advance.html)
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
