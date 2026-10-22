#!/usr/bin/env python3
"""Publishable GitHub wiki pages and Tinman's setting-help routing contract."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/Tinman-FP/tinmans-tuning-guide'
RAW = 'https://raw.githubusercontent.com/Tinman-FP/tinmans-tuning-guide/main/'
LINK = re.compile(r'(!?\[[^\]]*\]\()([^\s)]+)(\))')


def slug(text):
    text = re.sub(r'<[^>]+>', '', text).replace('`', '')
    text = re.sub(r'[^\w\-\s]', '', text.lower())
    return re.sub(r'\s', '-', text)


def headings(text):
    found = set()
    counts = {}
    fenced = False
    for line in text.splitlines():
        if line.startswith('```'):
            fenced = not fenced
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if match and not fenced:
            anchor = slug(match[1])
            number = counts.get(anchor, 0)
            counts[anchor] = number + 1
            found.add(anchor + (f'-{number}' if number else ''))
    return found


def source_pages():
    paths = [ROOT/'README.md', *sorted((ROOT/'guide').glob('*.md')),
             *sorted((ROOT/'templates').glob('*.md')), ROOT/'SOURCES.md', ROOT/'CREDITS.md']
    pages = {path.resolve(): ('Home' if path.name == 'README.md' else path.stem) for path in paths}
    assert len(set(pages.values())) == len(pages), 'Duplicate wiki page name'
    return pages


def convert(text, source, pages, anchors):
    def destination(target):
        url = urlsplit(target)
        if url.scheme or url.netloc:
            return target
        local = (source.parent/unquote(url.path)).resolve() if url.path else source.resolve()
        if not local.is_relative_to(ROOT):
            raise ValueError(f'Link escapes repository: {source}: {target}')
        if local in pages:
            if url.fragment and unquote(url.fragment) not in anchors[pages[local]]:
                raise ValueError(f'Missing anchor: {source}: {target}')
            return quote(pages[local]) + ('#' + url.fragment if url.fragment else '')
        if not local.exists():
            raise ValueError(f'Missing file: {source}: {target}')
        relative = local.relative_to(ROOT).as_posix()
        return RAW + quote(relative) if local.suffix.lower() in {'.png','.jpg','.jpeg','.svg','.webp'} else REPO+'/blob/main/'+quote(relative)

    text = LINK.sub(lambda match: match[1]+destination(match[2])+match[3], text)
    text = re.sub(r'(src=")([^"]+)(")', lambda match: match[1]+destination(match[2])+match[3], text)
    return re.sub(r'<!--\s*pdf:[\s\S]*?-->', '', text)


def validate_routes(contract, anchors):
    assert contract['base_url'] == REPO+'/wiki/'
    targets = [contract['default'], *contract['routes'].values(), *contract['prefixes'].values()]
    for target in targets:
        page, _, anchor = target.partition('#')
        if page not in anchors or (anchor and anchor not in anchors[page]):
            raise ValueError(f'Missing wiki route destination: {target}')


def header_text(contract):
    digest = hashlib.sha256((ROOT/'wiki/routes.json').read_bytes()).hexdigest()
    lines = ['// Generated from Tinmans Tuning Guide wiki/routes.json; edit that contract first.',
             '// Contract SHA-256: '+digest, '#pragma once', '#include <algorithm>', '#include <cctype>',
             '#include <map>', '#include <string>', '#include <utility>', '', 'namespace Slic3r {',
             'inline std::string tuning_guide_url(std::string path)', '{',
             '    const std::string base = '+json.dumps(contract['base_url'])+';',
             '    for (const std::string prefix : {"https://www.orcaslicer.com/wiki/", "https://orcaslicer.com/wiki/"})',
             '        if (path.compare(0, prefix.size(), prefix) == 0) path.erase(0, prefix.size());',
             '    const auto fragment = path.find(\'#\');',
             '    if (fragment != std::string::npos) {',
             '        std::transform(path.begin() + fragment, path.end(), path.begin() + fragment,',
             '                       [](unsigned char c) { return c == \' \' ? \'-\' : std::tolower(c); });',
             '    }',
             '    // Newer Orca paths add folders; setting identifiers remain the final component.',
             '    const auto slash = path.rfind(\'/\', fragment);',
             '    if (slash != std::string::npos) path.erase(0, slash + 1);',
             '    static const std::map<std::string, std::string> routes = {']
    for key, value in sorted(contract['routes'].items()):
        lines.append('        {'+json.dumps(key)+', '+json.dumps(value)+'},')
    lines.extend(['    };', '    auto found = routes.find(path);',
                  '    if (found != routes.end()) return base + found->second;',
                  '    path.erase(path.find(\'#\') == std::string::npos ? path.size() : path.find(\'#\'));',
                  '    found = routes.find(path);',
                  '    if (found != routes.end()) return base + found->second;',
                  '    static const std::pair<const char*, const char*> prefixes[] = {'])
    for key, value in contract['prefixes'].items():
        lines.append('        {'+json.dumps(key)+', '+json.dumps(value)+'},')
    lines.extend(['    };', '    for (const auto& prefix : prefixes)',
                  '        if (path.compare(0, std::char_traits<char>::length(prefix.first), prefix.first) == 0)',
                  '            return base + prefix.second;',
                  '    return base + '+json.dumps(contract['default'])+';', '}', '} // namespace Slic3r', ''])
    return '\n'.join(lines)


def build(output, header=None):
    contract = json.loads((ROOT/'wiki/routes.json').read_text())
    pages = source_pages()
    texts = {path: path.read_text() for path in pages}
    anchors = {pages[path]: headings(text) for path, text in texts.items()}
    validate_routes(contract, anchors)
    output.mkdir(parents=True, exist_ok=True)
    for path, name in pages.items():
        (output/(name+'.md')).write_text(convert(texts[path], path, pages, anchors))
    sidebar = ['[Home](Home)', '[Diagnostic Matrix](diagnostic-matrix)', '[Settings Reference](11-orca-tinmanx1-settings-reference)', '', '## Chapters', '']
    for path, name in pages.items():
        if path.parent.name == 'guide':
            title = texts[path].splitlines()[0].lstrip('# ')
            sidebar.append(f'- [{title}]({name})')
    sidebar.extend(['', '[Experiment Log](experiment-log) · [Release Checklist](profile-release-checklist)',
                    '[Sources](SOURCES) · [Credits](CREDITS)'])
    (output/'_Sidebar.md').write_text('\n'.join(sidebar)+'\n')
    (output/'_Footer.md').write_text('[Tinmans Tuning Guide source]('+REPO+') · [PDF releases]('+REPO+'/releases/latest) · [CC BY 4.0]('+REPO+'/blob/main/LICENSE)\n\nPublished from the maintained guide. Edit its source chapters and rebuild this wiki to keep editions synchronized.\n')
    if header:
        header.write_text(header_text(contract))
    print(f'Validated and generated {len(pages)} wiki pages, sidebar/footer, and {len(contract["routes"])} help routes.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--tinman-header', type=Path)
    args = parser.parse_args()
    build(args.output, args.tinman_header)
