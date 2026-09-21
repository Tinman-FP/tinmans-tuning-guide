# Credits

Tinmans Tuning Guide is an original synthesis built on the work of the open
3D-printing community. It summarizes methods in fresh language and links to
the source material instead of reproducing it.

## Project Authors

- **William Tinney** initiated the project, supplied the practical tuning
  questions, performed the physical experiments and measurements, documented
  print orientation and results, and directed publication.
- **Codex by OpenAI** researched the sources, developed the dependency-aware
  method, analyzed the experimental evidence, wrote and organized the guide,
  created the repository, and published this edition.

The worked `20.00 mm -> 20.13 mm -> 100.65% -> 20.00 mm` dimensional example
comes from a controlled calibration performed by William Tinney and analyzed
with Codex in September 2026.

## Cover Artwork

- The central TinmanX1 thumbnail logo is the original project icon supplied by
  William Tinney. It is reproduced without redrawing or replacing the mark.
- The circular title composition, calibration-ring motif, typography, layout,
  and production artwork were designed and prepared by Codex, OpenAI, at
  William Tinney's direction.
- The editable source, rendered cover, original logo copy, and provenance are
  retained in the repository's `assets` directory.

## Technical Foundations

- **Prusa Research** for its public knowledge base, especially its extrusion
  multiplier, drying, warping, first-layer, and material guidance.
- **SoftFever and the OrcaSlicer contributors** for the integrated calibration
  tools and documentation covering temperature, volumetric speed, flow ratio,
  pressure advance, tolerance, shrinkage, precision, seams, and surfaces.
- **Kevin O'Connor and the Klipper contributors** for the pressure-advance
  implementation and calibration documentation.
- **The Marlin contributors** for Linear Advance and its calibration
  documentation.
- **Andrew Ellis** for Ellis' Print Tuning Guide, especially the practical
  visual extrusion-multiplier method, dimensional-calibration cautions, and
  maximum-volumetric-flow guidance.
- **Stefan Hermann of CNC Kitchen** for empirical extrusion-system and hotend
  flow benchmarking. His work is part of the test lineage cited by both Ellis'
  guide and the broader calibration community.
- **The PrusaSlicer and SuperSlicer contributors** for the slicer features and
  calibration lineage inherited by later open-source slicers.

Specific links are collected in [SOURCES.md](SOURCES.md).

## Attribution Policy

All third-party projects, names, and trademarks belong to their respective
owners. Attribution acknowledges technical influence and does not imply
authorship of this guide, sponsorship, affiliation, or endorsement.

Contributors should identify the source of any new method, formula, diagram,
or test model in the same pull request that introduces it.
