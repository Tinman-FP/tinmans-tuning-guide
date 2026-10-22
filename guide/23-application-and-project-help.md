# Application and Project Help

Application preferences govern the workspace. They do not qualify a filament
tune. Keep machine-specific settings in the appropriate machine, filament, and
process profiles and follow the [tuning order](../README.md#start-here).

## Profiles, Sync, and Preservation

Back up user profiles and projects before migration. Distinguish account sync,
printer inventory sync, and the effective profiles embedded in a project.
Receiving a spool color or material name does not verify its tuned values.
After sync or import, recheck the selected physical machine, nozzle, process,
filament, tool/slot assignments, and resolved settings.

Preserve other active slicer sessions and isolated print workspaces. The
[profile integrity chapter](20-profile-integrity-and-experimental-resets.md)
explains why a new instance or copied data directory is not proof of freshness.

## Import and Export

STL and ordinary mesh exports primarily carry geometry. A 3MF can contain only
geometry or a complete slicer project, depending on its producer. Importing a
project may replace presets, plate state, modifiers, or assignments. Verify
what was actually imported before slicing.

STEP conversion tessellates surfaces into printable geometry. Inspect curvature,
small features, scale, orientation, and conversion resolution. OBJ color data
is distinct from printable material/tool assignments.

Save the source project and audited executable output. Ordinary saved
calibration projects may not retain their runtime sweep on reopening; see
[calibration changes](21-slicer-upgrades-and-calibration-changes.md).

## Transferring or Discarding Changes

Transferring changes carries edited values into another preset; discarding
returns to saved values. Review the changed fields and destination scope first.
Save a named candidate when the values represent a real experiment. Do not
transfer another machine's tune just because its material name matches.

## Display and Editing Preferences

Language, theme, units, view layout, and visibility modes change presentation.
Advanced or developer mode exposes additional controls without establishing
that those controls should be changed. Inspect units and the option tooltip;
zero may mean automatic, inherited, or disabled depending on the setting.

## Network and Device Preferences

Select the intended device and verify its saved identity, address, and transport.
Treat status, camera, file upload, and print start as separate channels. A
working camera is not proof that an uploaded job targets the correct printer.
Use manufacturer documentation for model-specific hardware/service faults.

Keep credentials private. Guide links and diagnostic records should contain
setting identifiers and public documentation, never access codes or tokens.
