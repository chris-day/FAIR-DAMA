# FAIR-DAMA
FAIR Data Principles and DAMA DMBok Alignment for success

## Documentation setup

Use Python 3.14. Create a virtual environment and install the pinned documentation dependencies:

```sh
python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Build the documentation site with `.venv/bin/zensical build --strict`. The generated files are in `site/`.
