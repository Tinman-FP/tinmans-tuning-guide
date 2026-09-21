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

- [Calibration overview](https://github.com/OrcaSlicer/OrcaSlicer/wiki/Calibration)
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
