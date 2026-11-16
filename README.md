# FAIR-DAMA
FAIR Data Principles and DAMA DMBok Alignment for success.

[![DOI](https://zenodo.org/badge/1446917256.svg)](https://doi.org/10.5281/zenodo.23987712)

## Documentation setup

Use Python 3.14. Create a virtual environment and install the pinned documentation dependencies:

```sh
python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Build the documentation site with `.venv/bin/zensical build --strict`. The generated files are in `site/`.

## Updating the DAMA documentation

`scripts/split_dama_segments.py` splits `artefacts/DAMA_Segments_High_Level_v1.17.0.md` at its H2 headings into 20 pages under `docs/dama/`. The source table of contents becomes site navigation. Run `.venv/bin/python scripts/split_dama_segments.py` after updating that source file, then build the site.

The Big Data & Data Science and Data Handling Ethics pages are extracted from `artefacts/DAMA_Segments_High_Level_v1.18.0.md`. Their diagrams and the V3 workbook are served locally from `docs/assets/`. The splitter above still targets v1.17.0 and does not regenerate these two pages.

The FAIR alignment page displays a local preview copied from `artefacts/dama-fair-sankey_v1.3.0.svg` and loads the standalone diagram from `artefacts/DAMA_FAIR_Sankey_v1.3.0.zip` only after a reader chooses to open it. The expanded diagram has 13 areas and topics, 15 FAIR principles, and 74 mappings. The original 11-area static SVG remains in the DAMA overview. The historical workbook is `artefacts/DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx`; the new topic pages use `artefacts/DAMA-PDOC_FAIR-MASTER_2026-11-16_V3.xlsx`.

The Ontologies page is adapted from `artefacts/ontologies.md`. Its relationship diagram is a local SVG generated from `scripts/ontologies.dot` with `dot -Tsvg scripts/ontologies.dot -o docs/assets/images/ontologies.svg`.

After changing the split pages or their headings, build the site, run `.venv/bin/python scripts/link_sankey_pages.py`, then build again. The script maps all 13 area and topic labels to individual segment pages and all 15 FAIR labels to headings in the principle page. It checks the built pages before updating the packaged diagram.
