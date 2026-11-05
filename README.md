# FAIR-DAMA
FAIR Data Principles and DAMA DMBok Alignment for success

## Documentation setup

Use Python 3.14. Create a virtual environment and install the pinned documentation dependencies:

```sh
python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Build the documentation site with `.venv/bin/zensical build --strict`. The generated files are in `site/`.

## Updating the DAMA documentation

`scripts/split_dama_segments.py` splits `artefacts/DAMA_Segments_High_Level_v1.17.0.md` at its H2 headings into 20 pages under `docs/dama/`. The source table of contents becomes site navigation. Run `.venv/bin/python scripts/split_dama_segments.py` after updating that source file, then build the site.

The FAIR alignment page embeds the standalone diagram from `artefacts/DAMA_FAIR_Sankey_v1.2.0.zip` after a reader chooses to load it. The worksheet download comes from `artefacts/DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx`.

After changing the split pages or their headings, build the site, run `.venv/bin/python scripts/link_sankey_pages.py`, then build again. The script maps all 11 DAMA labels to individual segment pages and all 15 FAIR labels to headings in the principle page. It checks the built pages before updating the packaged diagram.
