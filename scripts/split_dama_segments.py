"""Split the authoritative DAMA document into Zensical pages at H2 headings."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "artefacts/DAMA_Segments_High_Level_v1.17.0.md"
DOCS = ROOT / "docs"

PAGES = [
    ("Overview", "dama/index.md"),
    ("DAMA-DMBOK Core Knowledge Areas", "dama/core-knowledge-areas.md"),
    ("DAMA Segments and FAIR Alignment", "dama/segments-and-fair-alignment.md"),
    ("0. Data Management", "dama/segments/00-data-management.md"),
    ("1. Data Governance", "dama/segments/01-data-governance.md"),
    ("2. Data Architecture Management", "dama/segments/02-data-architecture-management.md"),
    ("3. Data Development", "dama/segments/03-data-development.md"),
    ("4. Data Operations Management", "dama/segments/04-data-operations-management.md"),
    ("5. Data Security Management", "dama/segments/05-data-security-management.md"),
    ("6. Reference & Master Data Management", "dama/segments/06-reference-master-data-management.md"),
    ("7. Data Warehousing & Business Intelligence Management", "dama/segments/07-data-warehousing-business-intelligence.md"),
    ("8. Document & Content Management", "dama/segments/08-document-content-management.md"),
    ("9. Meta-data Management", "dama/segments/09-metadata-management.md"),
    ("10. Data Quality Management", "dama/segments/10-data-quality-management.md"),
    ("11. Data Integration & Interoperability", "dama/segments/11-data-integration-interoperability.md"),
    ("12. Data Management Maturity Assessment", "dama/segments/12-data-management-maturity-assessment.md"),
    ("FAIR Alignment Gaps", "dama/fair-alignment-gaps.md"),
    ("Implementation-oriented alignment for all 15 FAIR principles", "dama/fair-principles.md"),
    ("Persona", "dama/personas.md"),
    ("Appendix", "dama/appendix.md"),
]

H2 = re.compile(r"^## (.+)$", re.MULTILINE)
SUBHEADING = re.compile(r"^(#{3,6})( .+)$", re.MULTILINE)


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    headings = list(H2.finditer(text))
    expected = ["Table of Contents", *(title for title, _ in PAGES)]
    actual = [match.group(1) for match in headings]
    if actual != expected:
        raise ValueError(f"Unexpected H2 structure: {actual!r}")

    for index, (title, relative_path) in enumerate(PAGES, start=1):
        start = headings[index].end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        body = text[start:end].strip("\n")
        body = SUBHEADING.sub(lambda match: match.group(1)[1:] + match.group(2), body)
        if title == "Overview":
            body = body.replace(
                "assets/dama-fair-sankey_v1.0.0.svg",
                "../fair-alignment/assets/dama-fair-sankey_v1.0.0.svg",
            )
            body = (
                "> Source: *DAMA Segments — High Level*, v1.17.0, Chris Day. "
                "The alignments are potential and proposed; implementation and "
                "compliance require supporting evidence. Source DAMA images carry "
                "copyright © DAMA International.\n\n" + body.lstrip("\n")
            )
        if title == "FAIR Alignment Gaps":
            body = body.replace(
                "](DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx)",
                "](../assets/downloads/DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx)",
            )
        destination = DOCS / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(f"# {title}\n\n{body.rstrip()}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
