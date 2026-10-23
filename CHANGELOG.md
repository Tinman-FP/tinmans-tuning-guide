# Changelog

## 1.0.5 - 2026-10-22

- Add original illustrated Benchy inspection and dimension locators, a
  photographed foundation-failure example, and full model/figure/photo credits.
- Add an unresolved temperature-tower example and stop rules: distinguish
  moisture-compatible symptoms from proof, audit repeated path-linked defects,
  preserve actual conditioning history and do not promote failed bands.
- Mark historical 255 C PET-CF evidence as setup-specific and outside the
  manufacturer's currently cited 260-290 C range; do not silently reuse it.
- Restore chapters 22 and 23 to the complete PDF, matching the maintained web edition.
- Add official-source 3DBenchy feature inspection, complete nominal dimension
  table, generic reference settings, and a reusable evidence-based grading record.
- Distinguish official design references from local acceptance decisions,
  unmeasured properties, and nonstandard benchmark conditions.
- Link foundations and validation to the checklist; rebuild PDF and synchronize wiki.

## Unreleased - 2026-10-20

- Replaced the dark industrial cover with the lighter Airframe brand system
  and added a dedicated portrait cover for the PDF edition.

## 1.0.4 - 2026-10-19

- Updated the public Tinman reference to Preview 5 and its packaged-app validation evidence.
- Corrected temperature-band guidance: steps are distributed across the sliced
  layer count, not fixed at 25 layers. Included measured 0.20/0.16 mm examples.
- Recorded successful PA line numbers-on/off, bounded PA tower and temperature
  exports; retained the calibration-project schedule persistence warning.
- Rechecked official Orca releases: 2.4.2 stable and 2.5.0-alpha preview.
- Rebuilt and checked the linked PDF against these chapters.

## 1.0.3 - 2026-10-19

- Distinguished public Tinman Preview 4 from the Preview 5 validation candidate; Orca 2.4.2 remains
  latest stable and 2.5.0-alpha the current numbered prerelease at review time.
- Documented optional nozzle-aware towers, VFA flow-limit adjustment and
  unreachable ranges, PA interpolation/footprint/input checks, and readable
  Moonraker upload errors. Distinguished software checks from physical tuning.
- Kept motion-limit changes, mixed-nozzle support, precise seams, migration,
  and larger alpha features explicitly outside this Tinman backport batch.
- Distinguished historical 5 mm VFA specimens from the new layer-based bands;
  documented the observed calibration-project schedule persistence limitation.
- Rebuilt the linked PDF from the same source chapters.

## 1.0.2 - 2026-10-18

- Updated public download links and version identification for Tinman Preview 4;
  distinguished its selected backports from Orca 2.5 alpha and stable 2.4.2.
- Added an upgrade chapter covering changed calibration generators, scarf
  planning, nozzle variants, migration, CLI profile resolution, and targeted
  revalidation of walls, bridges, overhangs, and support interfaces.
- Updated PA, retraction, and seam instructions with version-specific behavior.
- Added standard machine-specific candidate/tuned/retired naming, recoverable
  retirement, authoritative-profile checks, and job-owned session cleanup.
- Rebuilt the linked PDF with the updated version reference and upgrade chapter.

### Changes Since 1.0.1

- Added an image-backed R3Men carbon-fiber build-plate adhesion section. The
  field result records Vision Miner Nano Polymer as the only consistently
  successful adhesive in the maintained Tinman tests, while preserving the
  required thorough soap-and-water cleaning, fresh application, small-part
  brim, and physical-inspection boundaries.
- Added networked multi-tool workflow controls: one isolated slicer session per
  physical print, a required pre-launch home, live-state confirmation after
  upload, and complete start-to-end tool-path auditing.
- Clarified that a bridge-focused artifact is required to validate bridge
  cooling and that bridge-only stress overrides must not silently replace
  normal production cooling.

- Added a photographed FibreSeek profile-integrity case study showing how an
  assumed `0.6 mm` process produced misleading seam experiments and how the
  verified `0.4 mm` baseline collapsed the broad disturbance to one narrow seam.
- Added a four-identity preflight gate covering the physical machine, printer
  profile, machine-specific filament profile, process, and final G-code.
- Added an experimental-reset procedure that preserves useful negative results
  while preventing values from an invalid baseline from entering a released
  profile.
- Expanded seam diagnosis, validation, the diagnostic matrix, and the release
  checklist with nozzle/profile mismatch, machine-specific compatibility, and
  unintended tool or fiber-command checks.
- Added a controlled Elegoo PET-CF undried-versus-dried photo comparison to the
  conditioning chapter, with original field-photo attribution and a warning
  against compensating for moisture through unrelated slicer settings.
- Documented a repeatable low-temperature PET-CF flow stop and selected
  `255 C` as the test-specific working value above the observed cold-flow
  boundary for the documented Qidi Plus 4 and `0.6 mm` nozzle.
- Expanded the photographed FibreSeek VFA case study with representative-part
  confirmation, releasing `70 mm/s` for the documented machine/profile and
  separating the remaining layer-context band from broad VFA.
- Added production-cover photographs, a toolpath-based cooling diagnosis, and
  guidance explaining why adaptive layer height does not correct vertical XY
  curves.
- Use the guide's body typeface for plain-language examples, formulas, acceptance
  criteria, and worksheet fields while reserving monospace type for actual code.
- Correct bullet and numbered-list alignment and tighten list spacing for faster
  scanning and cleaner page endings.
- Keep the settings-reference scope and the diagnostic triage sequence together
  across intentional PDF page transitions.
- Rebalance the material guide, Others tab, experiment worksheet, and release
  checklist so sections no longer continue as isolated lines on nearly empty pages.
- Keep complete strength, fiber-contract, and instructional sections together,
  and compact the credits typography enough to avoid an orphaned closing sentence.

- Corrected the PDF cover renderer to preserve the artwork's native X/Y
  proportions and center the circular composition on the portrait page.
- Removed Markdown fence-language labels from literal examples and converted
  the calibration-order Mermaid source into a reader-facing workflow table.
- Suppressed web-only end-of-chapter navigation crumbs in the PDF so they do
  not create stranded single-line pages.
- Added a complete process-tab reference for OrcaSlicer and TinmanX1.
- Added original plain-language guidance for every setting group: what it
  controls, when to use it, and the desired result.
- Documented all TinmanX1 process-level fiber settings, filament fiber fields,
  FibreSeek printer-contract fields, Strength Lens, and Wave Overhang groups.
- Annotated shared and TinmanX1-only features and published the exact source,
  Wiki, and application versions used for the comparison.
- Added a single linked PDF edition with internal contents and cross-references.
- Added a toolpath-first diagnostic for repeated top-surface line-end defects.
- Documented how short unretracted hops can create endpoint beads even after
  flow ratio and pressure advance are correctly tuned.
- Added a one-variable Monotonic Line versus Monotonic comparison procedure.

## 1.0.1 - 2026-09-20

- Added a full-width cover to the repository front page.
- Centered the original TinmanX1 thumbnail logo inside circular title lettering.
- Retained an editable SVG source, rendered PNG, and logo provenance record.

## 1.0.0 - 2026-09-20

- Published the printer-neutral dependency-aware tuning workflow.
- Added detailed chapters for temperature, volumetric flow, pressure advance,
  flow ratio, cooling, retraction, dimensional accuracy, seams, and validation.
- Added a diagnostic matrix, glossary, experiment log, and release checklist.
- Added the experimentally validated measured-percentage dimensional example.
- Added source attribution, contribution guidance, and CC BY 4.0 licensing.
