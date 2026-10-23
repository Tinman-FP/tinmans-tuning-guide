"""Regression checks for the maintained wiki publication contract."""
import json
import ast
import unittest

from build_wiki import ROOT, convert, headings, source_pages, validate_routes


class WikiLinks(unittest.TestCase):
    def setUp(self):
        self.pages = source_pages()
        self.anchors = {name: headings(path.read_text()) for path, name in self.pages.items()}

    def test_wrapped_link_label(self):
        text = '[Orca and Tinman\nsettings reference](guide/11-orca-tinmanx1-settings-reference.md).'
        self.assertEqual(convert(text, ROOT/'README.md', self.pages, self.anchors),
                         '[Orca and Tinman\nsettings reference](11-orca-tinmanx1-settings-reference).')

    def test_route_destinations_exist(self):
        validate_routes(json.loads((ROOT/'wiki/routes.json').read_text()), self.anchors)

    def test_missing_heading_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Missing anchor'):
            convert('[bad](README.md#nonexistent)', ROOT/'README.md', self.pages, self.anchors)

    def test_local_images_resolve_to_source(self):
        self.assertIn('https://raw.githubusercontent.com/Tinman-FP/',
                      convert('![cover](assets/tinmans-tuning-guide-cover.png)',
                              ROOT/'README.md', self.pages, self.anchors))

    def test_complete_pdf_includes_every_guide_chapter(self):
        tree = ast.parse((ROOT/'scripts/build_pdf.py').read_text())
        documents = next(node.value for node in tree.body if isinstance(node, ast.Assign)
                         and any(isinstance(t, ast.Name) and t.id == 'DOCUMENTS' for t in node.targets))
        included = {entry.elts[1].args[0].value for entry in documents.elts}
        expected = {path.relative_to(ROOT).as_posix() for path in (ROOT/'guide').glob('*.md')}
        self.assertFalse(expected - included, 'Maintained guide chapters missing from complete PDF')


if __name__ == '__main__':
    unittest.main()
