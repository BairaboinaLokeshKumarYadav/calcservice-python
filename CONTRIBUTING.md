# Contributing

Thanks for your interest in improving Calculator Service. Bug fixes, clear documentation, tests, and focused feature proposals are welcome.

## Before you begin

- Read the [Code of Conduct](CODE_OF_CONDUCT.md).
- Search existing issues and pull requests before opening a duplicate.
- For a substantial or behavior-changing feature, open an issue first to discuss its scope.
- For security concerns, follow [SECURITY.md](SECURITY.md) instead of opening a public issue.

## Local setup

The application uses only the Python standard library. Python 3.11 or newer is recommended; continuous integration currently tests Python 3.11 and 3.12.

```bash
git clone https://github.com/BairaboinaLokeshKumarYadav/calcservice-python.git
cd calcservice-python
python main.py
```

Install the test dependency and run the suite:

```bash
python -m pip install pytest
python -m pytest -q
```

## Project layout

```text
calcservice-python/
|-- calcservice/       # Calculator modes and package exports
|-- docs/              # End-user documentation
|-- tests/             # Automated tests
|-- .github/           # CI and contribution templates
|-- main.py            # Interactive command-line entry point
|-- README.md          # Project overview and quick start
|-- CONTRIBUTING.md    # Contribution guide
|-- CODE_OF_CONDUCT.md # Community standards
|-- SECURITY.md        # Security reporting guidance
`-- SUPPORT.md         # Help and support guidance
```

## Making a change

1. Create a focused branch from `main`.
2. Keep changes scoped to one bug fix, feature, or documentation improvement.
3. Add or update tests for behavior changes. Keep tests deterministic and independent of external services.
4. Update the README or user guide when behavior or usage changes.
5. Run `python -m pytest -q` and check the diff for unintended files or generated artifacts.
6. Open a pull request using the repository template. Explain the motivation, summarize the change, and include test results.

## Code and documentation expectations

- Follow the surrounding Python style and use descriptive names.
- Prefer small, understandable changes and standard-library solutions unless a dependency is justified.
- Do not add secrets, personal data, or unrelated generated files.
- For calculator expressions, preserve the restricted parsing model; do not use unrestricted `eval`.
- Document supported behavior and limitations accurately. Avoid claiming that a calculation is suitable for professional, financial, or safety-critical decisions.

## Pull requests

Pull requests should be ready for review, include relevant tests and documentation, and explain any trade-offs or known limitations. CI must pass before a change is merged. Maintainers may request revisions or additional tests.
