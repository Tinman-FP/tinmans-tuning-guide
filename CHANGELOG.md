# Changelog

## 1.2.1 - 2026-11-21

VAL01 model correction.

- VAL01 v2: the boss bore is now blind and starts on the deck top. In v1 it
  ran down through the bridged deck into the cable channel. The first bridge
  layer then had to print the bore's edge in mid-air, and on the first print
  the 40 mm bridge strands tangled around it. That would fail with almost any
  filament, so it tested the model, not the profile. Nothing else changed:
  pass marks A–H, outside size, holes, pins and file names are the same.
  `models/val01_template.scad` and `models/val01.stl` now hold v2, and the
  template's default label is "VAL01".
- The dimensioned drawing gains a section through the boss, showing the blind
  bore with v1's bore dashed. The render gains a view of the underside.
- Chapter 09: a VAL01 revision history, and VAL01's first result. PCTG on a
  CORE One+ INDX passed every check A–H on the v2 reprint, graded from
  measurements. The bridge held with about 0.2 mm sag, the deck top had no
  crater, and the tightest sliding pin gives a 0.2 mm sliding-fit allowance.
  The profile was then released as TUNED r7 with its values unchanged, the
  first release through VAL01. Observation is kept apart from inference.
  Chapter 26's INDX example says the same.
- Chapter 09 and the release checklist: a Tinman promotion trap. Saving a
  CANDIDATE as TUNED can write the new preset as a child of the candidate,
  so retiring the candidate would orphan it. Tick the save dialog's parent
  box (developer mode), check that `inherits` is empty, then retire.
- VAL01 pass marks: B may be graded by measuring the holes (at least the
  screw size plus 0.2 mm) instead of a screw test, and D now says how to
  measure sag (mid-span against both ends of each opening).
- Profile names: the status comes first and the revision last; the machine
  and material parts may come in either order, one order per printer.
  Chapter 09's INDX example now matches the real profile
  (`CANDIDATE - 3D-Fuel Pro PCTG - CORE One+ INDX 8T 0.4 HF - r7`), and
  chapter 20 and the release checklist say the same.
- Chapter 09: a known limitation. The pin dimples print as short dashes and
  can be hard to read, so the text adds the pins' order on the plate. The
  model is unchanged.
- PDF: the title page's edition line still said 1.0.4; it now says 1.2.1.
  Link text and captions keep underscores inside names, so
  `val01_template.scad` no longer prints as "val01template.scad". The
  contents fit on two pages again (1.2.0 put its last line on a third), and
  a heading directly above a figure now moves to the next page with it
  instead of ending a page alone (three places).

## 1.2.0 - 2026-11-21

Design and readability pass on edition 1.1, plus the VAL01 test.

- New: VAL01, the functional bracket and fit coupon that is the last test
  before a profile is called TUNED (chapter 09), with its OpenSCAD template
  and STL in `models/`, a dimensioned drawing, pass marks A–H, and where to
  go back when a check fails. New help route `validation_val01` for a
  Tinman Calibration-menu item.
  The quick path now starts a new filament with a stock 3DBenchy and ends
  with VAL01.

- Every chapter opens with an "At a glance" box: what you decide, the test to
  use, and what you keep. It replaces 1.1's "Quick path" boxes.
- Every test has a visual: five more field photographs (a clean pin break,
  too-high flow coupons, overhang fins, a retraction tower that never strung,
  the five-shape seam test) and four original diagrams (reading a Max
  flowrate ramp, reading a PA chevron, the dimension frames test, where each
  tuned value lives in the filament settings). The PET-CF support figure is
  also shown in the validation chapter.
- The settings reference (chapters 12-18) is set out as an "At a glance"
  table and a control table for each group instead of solid prose.
- Typography: temperatures written with °C, arrows as →, number ranges with
  en dashes, and plain numbers no longer set in code style (inline code spans
  down from about 1,030 to about 330; code style is kept for setting names,
  G-code, versions and file names).
- PDF: contents cut to chapters plus the sections of the tuning chapters (two
  pages instead of ten); forced page breaks removed; figures capped lower so
  they stop leaving large gaps; "At a glance" boxes render as callouts.

## 1.1.0 - 2026-11-21

Written against Tinman on its OrcaSlicer 2.5.1 base (source `baf3f00dfe`) and
the guide's November tuning runs.

Corrections:

- YOLO flow tests **add** the coupon label to the current flow ratio; Pass 1 and
  Pass 2 multiply. The earlier flow example left this to the reader, and one
  field run misrecorded a result because of it.
- Withdrew the 255 °C Elegoo PET-CF selection. After a first-layer fault was
  fixed, the same printer and nozzle gave 275 °C; the cold-flow margin lesson
  is kept.
- Profile names now use ` - ` separators instead of `|`, which Windows does not
  allow in file names.
- The Max flowrate "cap" seen in the field is not built in: it appears when the
  printing filament is not the one open for editing.
- Rewrote the upgrade chapter and version notes for the OrcaSlicer 2.5.1 base;
  removed "Preview 5 versus 2.5 alpha" framing throughout.
- Replaced two published photographs whose files still carried location
  metadata; every published JPEG is now metadata-free. Reduced two oversized
  photographs.

Additions:

- Chapter 25, Running Tinman's Calibration Tests: every Calibration-menu test,
  its fields, defaults and reading formula, what it changes, a safe recipe, and
  known issues.
- Chapter 26, Worked Examples: complete PCTG, PET-CF and ABS tuning runs on a
  K2 Plus, CORE One+ INDX, Qidi Plus4 and Snapmaker U1, including wrong turns.
- A one-page quick path on the home page with a new tuning-path diagram, and a
  "Quick path" box at the top of each core chapter.
- Step 0 (write pass marks first) and a stop rule; tuning versus validation
  prints; naming, versioning and promotion rules.
- Drying records from the field runs; color change within a spool; a simple
  comparative bond check and when it cannot work.
- Foundations: measuring the first layer, repeatable-but-wrong probing, plate
  changes, machine events that are not filament results.
- MVS: which signal ended the test, and five field results. PA: tower then
  pattern at production speeds, chamber effects, "nothing changes" results.
  Flow: grading without touch, a sanity bound. Retraction: towers that never
  string, wipe, small-feature whiskers. Dimensions: proportional versus
  constant-offset field examples, multi-filament shrinkage. Seams: a seam test
  and a top-surface path example. Materials: PCTG, PET-CF, PC, ABS and HIPS
  field results; mixed-plate bed temperature.
- Diagnostic-matrix rows and glossary terms for calibration traps.
- Seven new field photographs and figures, all cropped and metadata-free.
- Grouped wiki sidebar.

## 1.0.5 - 2026-10-22

- Add original illustrated Benchy inspection and dimension locators, a
  photographed foundation-failure example, and full model/figure/photo credits.
- Add an unresolved temperature-tower example and stop rules: distinguish
  moisture-compatible symptoms from proof, audit repeated path-linked defects,
  preserve actual conditioning history and do not promote failed bands.
- Mark historical 255 °C PET-CF evidence as setup-specific and outside the
  manufacturer's currently cited 260–290 °C range; do not silently reuse it.
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
  assumed 0.6 mm process produced misleading seam experiments and how the
  verified 0.4 mm baseline collapsed the broad disturbance to one narrow seam.
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
  255 °C as the test-specific working value above the observed cold-flow
  boundary for the documented Qidi Plus 4 and 0.6 mm nozzle.
- Expanded the photographed FibreSeek VFA case study with representative-part
  confirmation, releasing 70 mm/s for the documented machine/profile and
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
