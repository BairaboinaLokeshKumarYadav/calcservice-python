# Community and contributing

Calculator Service welcomes bug reports, focused improvements, tests, and documentation contributions. Please follow the repository's policies and guidance:

- [Contributing guide](https://github.com/BairaboinaLokeshKumarYadav/calcservice-python/blob/main/CONTRIBUTING.md): local setup, tests, and pull request expectations.
- [Code of Conduct](https://github.com/BairaboinaLokeshKumarYadav/calcservice-python/blob/main/CODE_OF_CONDUCT.md): community standards and enforcement.
- [Support](https://github.com/BairaboinaLokeshKumarYadav/calcservice-python/blob/main/SUPPORT.md): where to ask questions and report bugs.
- [Security policy](https://github.com/BairaboinaLokeshKumarYadav/calcservice-python/blob/main/SECURITY.md): how to report a suspected vulnerability privately.

## Run the tests

The application itself needs no third-party packages. Install `pytest` to run the test suite:

```bash
python -m pip install pytest
python -m pytest -q
```

## Documentation changes

The website is built from Markdown files in `docs/` using MkDocs Material. To preview changes locally:

```bash
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
```

Open the local address printed by MkDocs. To build the deployable site:

```bash
python -m mkdocs build --strict
```
