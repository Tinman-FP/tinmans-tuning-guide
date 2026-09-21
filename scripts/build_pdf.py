#!/usr/bin/env python3
"""Build the complete linked PDF edition of Tinmans Tuning Guide."""

from __future__ import annotations

import argparse
import html
import re
import textwrap
from pathlib import Path, PurePosixPath

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    Image,
    ListFlowable,
    ListItem,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Tinmans-Tuning-Guide.pdf"

DOCUMENTS = [
    ("Introduction", Path("README.md")),
    ("How to Use This Guide", Path("guide/00-how-to-use-this-guide.md")),
    ("Foundations", Path("guide/01-foundations.md")),
    ("Conditioning and Temperature", Path("guide/02-conditioning-and-temperature.md")),
    ("Maximum Volumetric Flow", Path("guide/03-volumetric-flow.md")),
    ("Pressure Advance", Path("guide/04-pressure-advance.md")),
    ("Global and Feature-Specific Flow", Path("guide/05-flow-ratio.md")),
    ("Cooling, Bridges, Retraction, and Travel", Path("guide/06-cooling-and-retraction.md")),
    ("Dimensional Accuracy and Tolerances", Path("guide/07-dimensional-accuracy.md")),
    ("Seams and Surface Quality", Path("guide/08-seams-and-surfaces.md")),
    ("Validation and Profile Release", Path("guide/09-validation.md")),
    ("Material-Family Priorities", Path("guide/10-material-families.md")),
    ("Settings Reference and Versions", Path("guide/11-orca-tinmanx1-settings-reference.md")),
    ("Quality Tab", Path("guide/12-quality-tab.md")),
    ("Strength Tab", Path("guide/13-strength-tab.md")),
    ("Speed Tab", Path("guide/14-speed-tab.md")),
    ("Support Tab", Path("guide/15-support-tab.md")),
    ("Multimaterial Tab", Path("guide/16-multimaterial-tab.md")),
    ("Others Tab", Path("guide/17-others-tab.md")),
    ("TinmanX1 Fiber and Strength Tools", Path("guide/18-tinmanx1-fiber-and-strength-tools.md")),
    ("Diagnostic Matrix", Path("guide/diagnostic-matrix.md")),
    ("Glossary", Path("guide/glossary.md")),
    ("Experiment Log", Path("templates/experiment-log.md")),
    ("Profile Release Checklist", Path("templates/profile-release-checklist.md")),
    ("Sources and Further Reading", Path("SOURCES.md")),
    ("Credits", Path("CREDITS.md")),
    ("License", Path("LICENSE")),
]
DOCUMENT_TITLES = {path.as_posix(): title for title, path in DOCUMENTS}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[`*_]", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "section"


def strip_markdown(value: str) -> str:
    value = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"[`*_]", "", value)
    return html.unescape(value).strip()


class GuideDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="body",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(PageTemplate(id="body", frames=[frame], onPage=self._draw_page))

    def _draw_page(self, canvas, doc):
        if doc.page <= 1:
            return
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#C9CDD2"))
        canvas.setLineWidth(0.4)
        canvas.line(self.leftMargin, 0.52 * inch, letter[0] - self.rightMargin, 0.52 * inch)
        canvas.setFillColor(colors.HexColor("#4B5563"))
        canvas.setFont("Helvetica", 8)
        canvas.drawString(self.leftMargin, 0.34 * inch, "Tinmans Tuning Guide")
        canvas.drawRightString(letter[0] - self.rightMargin, 0.34 * inch, str(doc.page))
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        level = getattr(flowable, "_toc_level", None)
        key = getattr(flowable, "_bookmark_name", None)
        if level is None or key is None:
            return
        title = strip_markdown(flowable.getPlainText())
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(title, key, level=level, closed=level > 0)
        self.notify("TOCEntry", (level, title, self.page, key))


class FullPageCover(Flowable):
    def __init__(
        self,
        image_path: Path,
        page_width: float,
        page_height: float,
        frame_height: float,
        left_margin: float,
        bottom_margin: float,
    ):
        super().__init__()
        self.image_path = image_path
        self.page_width = page_width
        self.page_height = page_height
        self.left_margin = left_margin
        self.bottom_margin = bottom_margin
        self.width = 1
        self.height = frame_height

    def draw(self):
        image_width, image_height = ImageReader(str(self.image_path)).getSize()
        rendered_height = self.page_width
        scale = rendered_height / image_height
        rendered_width = image_width * scale
        page_x = -self.left_margin
        page_y = -self.bottom_margin
        image_x = page_x + (self.page_width - rendered_width) / 2
        image_y = page_y + (self.page_height - rendered_height) / 2

        self.canv.saveState()
        self.canv.setFillColor(colors.HexColor("#181F26"))
        self.canv.rect(page_x, page_y, self.page_width, self.page_height, stroke=0, fill=1)
        self.canv.drawImage(
            str(self.image_path),
            image_x,
            image_y,
            width=rendered_width,
            height=rendered_height,
            preserveAspectRatio=True,
            mask="auto",
        )
        self.canv.restoreState()


def build_styles():
    sample = getSampleStyleSheet()
    body = ParagraphStyle(
        "Body",
        parent=sample["BodyText"],
        fontName="Helvetica",
        fontSize=9.4,
        leading=13.2,
        textColor=colors.HexColor("#20252B"),
        spaceAfter=6,
        allowWidows=0,
        allowOrphans=0,
    )
    styles = {
        "body": body,
        "lead": ParagraphStyle(
            "Lead",
            parent=body,
            fontSize=11,
            leading=15.5,
            textColor=colors.HexColor("#39424E"),
            spaceAfter=12,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=sample["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=21,
            leading=25,
            textColor=colors.HexColor("#111827"),
            spaceBefore=0,
            spaceAfter=13,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=sample["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=colors.HexColor("#0D6B63"),
            spaceBefore=13,
            spaceAfter=7,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "H3",
            parent=sample["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=11.2,
            leading=14,
            textColor=colors.HexColor("#8A4B16"),
            spaceBefore=10,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=body,
            fontSize=7.5,
            leading=10,
            wordWrap="CJK",
        ),
        "code": ParagraphStyle(
            "Code",
            parent=body,
            fontName="Courier",
            fontSize=7.3,
            leading=9.5,
            leftIndent=8,
            rightIndent=8,
            borderColor=colors.HexColor("#D1D5DB"),
            borderWidth=0.5,
            borderPadding=7,
            backColor=colors.HexColor("#F6F7F8"),
            spaceBefore=4,
            spaceAfter=9,
        ),
        "flow_number": ParagraphStyle(
            "FlowNumber",
            parent=body,
            fontName="Helvetica-Bold",
            fontSize=8.5,
            leading=11,
            textColor=colors.white,
            alignment=TA_CENTER,
            spaceAfter=0,
        ),
        "flow_text": ParagraphStyle(
            "FlowText",
            parent=body,
            fontSize=8.8,
            leading=11.5,
            spaceAfter=0,
        ),
        "toc_title": ParagraphStyle(
            "TOCTitle",
            parent=sample["Title"],
            fontName="Helvetica-Bold",
            fontSize=25,
            leading=29,
            textColor=colors.HexColor("#111827"),
            alignment=TA_LEFT,
            spaceAfter=18,
        ),
        "front_title": ParagraphStyle(
            "FrontTitle",
            parent=sample["Title"],
            fontName="Helvetica-Bold",
            fontSize=25,
            leading=30,
            textColor=colors.HexColor("#111827"),
            alignment=TA_CENTER,
            spaceAfter=12,
        ),
        "front_subtitle": ParagraphStyle(
            "FrontSubtitle",
            parent=body,
            fontSize=12,
            leading=17,
            textColor=colors.HexColor("#4B5563"),
            alignment=TA_CENTER,
            spaceAfter=12,
        ),
    }
    return styles


def collect_anchors(documents):
    file_anchors = {}
    heading_anchors = {}
    for _, rel_path in documents:
        key = rel_path.as_posix()
        file_anchor = "doc-" + slugify(key)
        file_anchors[key] = file_anchor
        path = ROOT / rel_path
        if not path.exists():
            raise FileNotFoundError(path)
        seen = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^(#{1,3})\s+(.+?)\s*$", line)
            if not match:
                continue
            base = slugify(strip_markdown(match.group(2)))
            count = seen.get(base, 0)
            seen[base] = count + 1
            fragment = base if count == 0 else f"{base}-{count}"
            heading_anchors[(key, fragment)] = f"{file_anchor}-{fragment}"
    return file_anchors, heading_anchors


def resolve_link(target: str, source: Path, file_anchors, heading_anchors) -> str | None:
    if target.startswith(("https://", "http://", "mailto:")):
        return target
    if target.startswith("#"):
        fragment = slugify(target[1:])
        return "#" + heading_anchors.get((source.as_posix(), fragment), file_anchors[source.as_posix()])
    raw_path, _, raw_fragment = target.partition("#")
    if raw_path.startswith("output/pdf/"):
        return None
    resolved = PurePosixPath(source.parent.as_posix()) / PurePosixPath(raw_path)
    normalized = str(PurePosixPath(resolved))
    while normalized.startswith("./"):
        normalized = normalized[2:]
    parts = []
    for part in PurePosixPath(normalized).parts:
        if part == ".." and parts:
            parts.pop()
        elif part not in (".", ""):
            parts.append(part)
    key = PurePosixPath(*parts).as_posix()
    if key not in file_anchors:
        return None
    if raw_fragment:
        fragment = slugify(raw_fragment)
        return "#" + heading_anchors.get((key, fragment), file_anchors[key])
    return "#" + file_anchors[key]


def inline_markup(text: str, source: Path, file_anchors, heading_anchors) -> str:
    placeholders = {}

    def hold(value: str) -> str:
        token = f"@@TOKEN{len(placeholders)}@@"
        placeholders[token] = value
        return token

    def code_repl(match):
        return hold(f'<font name="Courier" color="#7C2D12">{html.escape(match.group(1))}</font>')

    text = re.sub(r"`([^`]+)`", code_repl, text)

    def link_repl(match):
        label = html.escape(strip_markdown(match.group(1)))
        target = resolve_link(match.group(2).strip(), source, file_anchors, heading_anchors)
        if not target:
            return label
        color = "#0D6B63" if target.startswith("#") else "#155E9A"
        return hold(f'<link href="{html.escape(target, quote=True)}" color="{color}">{label}</link>')

    text = re.sub(r"\[([^]]+)\]\(([^)]+)\)", link_repl, text)
    text = re.sub(r"!\[([^]]*)\]\(([^)]+)\)", lambda m: html.escape(m.group(1)), text)
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    for token, value in placeholders.items():
        text = text.replace(html.escape(token), value)
    return text


def make_heading(text, level, anchor, styles):
    style = styles[{1: "h1", 2: "h2", 3: "h3"}[level]]
    paragraph = Paragraph(f'<a name="{anchor}"/>{html.escape(strip_markdown(text))}', style)
    paragraph._toc_level = level - 1
    paragraph._bookmark_name = anchor
    return paragraph


def split_table_row(line: str):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def make_table(lines, source, file_anchors, heading_anchors, styles, available_width):
    rows = [split_table_row(line) for line in lines]
    if len(rows) > 1 and is_table_separator(lines[1]):
        rows.pop(1)
    column_count = max(len(row) for row in rows)
    for row in rows:
        row.extend([""] * (column_count - len(row)))
    weights = []
    for index in range(column_count):
        longest = max(8, min(45, max(len(strip_markdown(row[index])) for row in rows)))
        weights.append(longest)
    total = sum(weights)
    widths = [available_width * weight / total for weight in weights]
    data = []
    for row_index, row in enumerate(rows):
        style = styles["small"]
        data.append([
            Paragraph(("<b>" if row_index == 0 else "") + inline_markup(cell, source, file_anchors, heading_anchors) + ("</b>" if row_index == 0 else ""), style)
            for cell in row
        ])
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EFEE")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#111827")),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#C8CDD2")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAF9")]),
    ]))
    return table


def make_mermaid_flow(lines, styles, available_width):
    steps = []
    seen = set()
    for line in lines:
        for node, label in re.findall(r"([A-Za-z0-9_]+)\[([^]]+)\]", line):
            if node in seen:
                continue
            seen.add(node)
            steps.append(label)

    if not steps:
        return Preformatted("\n".join(lines), styles["code"])

    data = [
        [
            Paragraph(str(index), styles["flow_number"]),
            Paragraph(html.escape(label), styles["flow_text"]),
        ]
        for index, label in enumerate(steps, start=1)
    ]
    table = Table(data, colWidths=[0.34 * inch, available_width - 0.34 * inch], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#0D6B63")),
        ("ROWBACKGROUNDS", (1, 0), (1, -1), [colors.HexColor("#F3F7F6"), colors.white]),
        ("BOX", (0, 0), (-1, -1), 0.45, colors.HexColor("#BFCAC8")),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#D7DEDC")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (0, -1), 3),
        ("RIGHTPADDING", (0, 0), (0, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (1, 0), (1, -1), 7),
        ("RIGHTPADDING", (1, 0), (1, -1), 7),
    ]))
    return table


def markdown_flowables(rel_path, styles, file_anchors, heading_anchors, available_width):
    source = rel_path
    lines = (ROOT / rel_path).read_text(encoding="utf-8").splitlines()
    has_heading = any(re.match(r"^#{1,3}\s+", line) for line in lines)
    flows = []
    index = 0
    first_heading = True
    if not has_heading:
        title = DOCUMENT_TITLES.get(rel_path.as_posix(), rel_path.stem.replace("-", " ").title())
        flows.append(make_heading(title, 1, file_anchors[rel_path.as_posix()], styles))
        first_heading = False
    in_html_block = False
    paragraph_lines = []

    def flush_paragraph():
        nonlocal paragraph_lines
        if not paragraph_lines:
            return
        joined = " ".join(line.strip() for line in paragraph_lines).strip()
        paragraph_lines = []
        if not joined:
            return
        plain_text = strip_markdown(joined)
        if re.match(
            r"^(Proceed to|Continue with|Move to|Next, tune|Finish with|Return to)\b",
            plain_text,
        ):
            return
        style = styles["lead"] if first_heading and len(flows) < 3 else styles["body"]
        flows.append(Paragraph(inline_markup(joined, source, file_anchors, heading_anchors), style))

    seen_slugs = {}
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped.startswith("<p "):
            flush_paragraph()
            in_html_block = True
            index += 1
            continue
        if in_html_block:
            if stripped == "</p>":
                in_html_block = False
            index += 1
            continue
        if stripped.startswith("```"):
            flush_paragraph()
            language = stripped[3:].strip()
            index += 1
            code_lines = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                for wrapped in textwrap.wrap(lines[index], width=92, replace_whitespace=False, drop_whitespace=False) or [""]:
                    code_lines.append(wrapped)
                index += 1
            if language.lower() == "mermaid":
                flows.append(make_mermaid_flow(code_lines, styles, available_width))
            else:
                flows.append(Preformatted("\n".join(code_lines), styles["code"]))
            index += 1
            continue
        heading = re.match(r"^(#{1,3})\s+(.+?)\s*$", line)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            title = heading.group(2)
            base = slugify(strip_markdown(title))
            count = seen_slugs.get(base, 0)
            seen_slugs[base] = count + 1
            fragment = base if count == 0 else f"{base}-{count}"
            anchor = heading_anchors.get((source.as_posix(), fragment), file_anchors[source.as_posix()])
            if first_heading:
                anchor = file_anchors[source.as_posix()]
                first_heading = False
            flows.append(make_heading(title, level, anchor, styles))
            index += 1
            continue
        if stripped.startswith("|") and index + 1 < len(lines) and is_table_separator(lines[index + 1]):
            flush_paragraph()
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            flows.append(make_table(table_lines, source, file_anchors, heading_anchors, styles, available_width))
            flows.append(Spacer(1, 8))
            continue
        list_match = re.match(r"^\s*([-*]|\d+\.)\s+(.+)", line)
        if list_match:
            flush_paragraph()
            ordered = list_match.group(1)[0].isdigit()
            items = []
            while index < len(lines):
                item_match = re.match(r"^\s*([-*]|\d+\.)\s+(.+)", lines[index])
                if not item_match or item_match.group(1)[0].isdigit() != ordered:
                    break
                item = item_match.group(2).strip()
                index += 1
                while index < len(lines):
                    continuation = lines[index]
                    if not continuation.strip():
                        break
                    if re.match(r"^\s*([-*]|\d+\.)\s+", continuation):
                        break
                    if re.match(r"^(#{1,3})\s+", continuation) or continuation.strip().startswith(("|", "```")):
                        break
                    if continuation.startswith("  "):
                        item += " " + continuation.strip()
                        index += 1
                    else:
                        break
                item_para = Paragraph(inline_markup(item, source, file_anchors, heading_anchors), styles["body"])
                items.append(ListItem(item_para, leftIndent=12))
                if index < len(lines) and not lines[index].strip():
                    lookahead = index + 1
                    if lookahead < len(lines) and re.match(r"^\s*([-*]|\d+\.)\s+", lines[lookahead]):
                        index = lookahead
            list_options = {
                "bulletType": "1" if ordered else "bullet",
                "leftIndent": 22,
                "bulletFontName": "Helvetica",
                "bulletFontSize": 8,
                "spaceAfter": 7,
            }
            if ordered:
                list_options["start"] = "1"
            flows.append(ListFlowable(items, **list_options))
            continue
        if not stripped or stripped == "---":
            flush_paragraph()
            if stripped == "---":
                flows.append(Spacer(1, 7))
            index += 1
            continue
        paragraph_lines.append(line)
        index += 1
    flush_paragraph()
    return flows


def build_pdf(output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    styles = build_styles()
    file_anchors, heading_anchors = collect_anchors(DOCUMENTS)
    doc = GuideDocTemplate(
        str(output),
        pagesize=letter,
        rightMargin=0.72 * inch,
        leftMargin=0.72 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.68 * inch,
        title="Tinmans Tuning Guide",
        author="William Tinney and Codex by OpenAI",
        subject="A printer-neutral filament tuning handbook with OrcaSlicer and TinmanX1 settings reference",
        creator="Tinmans Tuning Guide build script",
    )
    story = []
    cover = ROOT / "assets" / "tinmans-tuning-guide-cover.png"
    story.append(FullPageCover(
        cover,
        letter[0],
        letter[1],
        doc.height,
        doc.leftMargin,
        doc.bottomMargin,
    ))
    story.append(PageBreak())
    story.append(Spacer(1, 0.55 * inch))
    story.append(Paragraph("Tinmans Tuning Guide", styles["front_title"]))
    story.append(Paragraph(
        "A printer-neutral handbook for filament calibration, diagnosis, profile release, and practical OrcaSlicer/TinmanX1 settings.",
        styles["front_subtitle"],
    ))
    story.append(Spacer(1, 0.18 * inch))
    story.append(Paragraph(
        "Project initiated and experimentally informed by William Tinney. Researched, written, organized, and published with Codex by OpenAI.",
        styles["front_subtitle"],
    ))
    story.append(Spacer(1, 0.25 * inch))
    story.append(Paragraph(
        "PDF edition generated 2026-09-21. Settings comparison baseline: OrcaSlicer 2.4.2 and TinmanX1 2.4.2 at source commit cf0cabb04146c4ff9f21b963517717acfec66055.",
        styles["front_subtitle"],
    ))
    story.append(PageBreak())
    story.append(Paragraph("Contents", styles["toc_title"]))
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("TOC1", fontName="Helvetica-Bold", fontSize=10, leading=14, leftIndent=0, firstLineIndent=0, textColor=colors.HexColor("#111827"), spaceBefore=4),
        ParagraphStyle("TOC2", fontName="Helvetica", fontSize=8.5, leading=11, leftIndent=15, firstLineIndent=0, textColor=colors.HexColor("#374151")),
        ParagraphStyle("TOC3", fontName="Helvetica", fontSize=7.5, leading=9.5, leftIndent=30, firstLineIndent=0, textColor=colors.HexColor("#6B7280")),
    ]
    story.append(toc)
    story.append(PageBreak())

    for doc_index, (_, rel_path) in enumerate(DOCUMENTS):
        if doc_index:
            story.append(PageBreak())
        story.extend(markdown_flowables(rel_path, styles, file_anchors, heading_anchors, doc.width))

    doc.multiBuild(story)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    build_pdf(args.output.resolve())
    print(args.output.resolve())


if __name__ == "__main__":
    main()
