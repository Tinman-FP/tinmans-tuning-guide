# Wiki Publication

The public wiki is https://github.com/Tinman-FP/tinmans-tuning-guide/wiki.
Maintained Markdown in this repository is the source of truth. Do not maintain
a second independent copy of the tuning advice in the wiki editor.

The generator rewrites chapter links and images for GitHub Wiki, checks every
local destination and heading fragment, and creates navigation and credits.
`routes.json` maps Tinman's setting-help identifiers to existing guide sections.
Specific mappings take priority over group mappings; an unknown setting stays
in the Tinman settings reference. Manufacturer service/fault links are separate.

To publish with the existing maintainer Git credentials:

```bash
git clone https://github.com/Tinman-FP/tinmans-tuning-guide.wiki.git ../tinmans-guide-wiki
python3 scripts/build_wiki.py --output ../tinmans-guide-wiki
git -C ../tinmans-guide-wiki diff --check
git -C ../tinmans-guide-wiki add -- '*.md'
git -C ../tinmans-guide-wiki commit -m "Synchronize wiki from guide"
git -C ../tinmans-guide-wiki push origin master
```

Inspect the cloned wiki's default branch before pushing; do not force-push or
remove pages created by other maintainers. The generator overwrites its named
pages only and leaves unrelated wiki files intact. Review concurrent edits
before publishing. GitHub requires the initial wiki page to be created through
its web editor before the wiki Git repository can be cloned.

When the route contract changes, regenerate Tinman's helper and run its focused
link tests in the same update:

```bash
python3 scripts/build_wiki.py --output ../tinmans-guide-wiki --tinman-header ../Tinman/src/libslic3r/TuningGuide.hpp
```

Wiki publication uses the maintainer's existing Git authentication. The check
workflow validates pages without storing credentials or creating a new token.
After a chapter change, publish the wiki with that change; a repository push
alone does not update GitHub's separate wiki repository.
