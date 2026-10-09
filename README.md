# Calculator Service

A lightweight, interactive command-line calculator written in Python. Choose a mode for everyday arithmetic, scientific expressions, programmer bit operations, financial formulas, or common engineering calculations.

## Requirements

- Python 3.11 or newer is recommended. The CI workflow tests Python 3.11 and 3.12.
- No third-party packages are needed to run the calculator.
- `pytest` is needed to run the test suite.

## Quick start

From the repository root, run:

```bash
python main.py
```

Choose a calculator from the menu and follow its prompts. Enter `exit` or `quit` at an expression prompt, or choose the return option in a submenu, to go back. Choose **6. Exit** from the main menu to close the program.

Read the [documentation website](https://bairaboinalokeshkumaryadav.github.io/calcservice-python/) or the [user guide](docs/USER_GUIDE.md) for calculator features, examples, formulas, and limitations.

## Calculator modes

| Mode | What it does |
| --- | --- |
| Basic | Evaluates arithmetic expressions with numeric literals, parentheses, and common operators. |
| Scientific | Evaluates mathematical expressions using selected functions and constants from Python's `math` module. Trigonometric angles are in radians. |
| Programmer | Evaluates integer arithmetic and bitwise expressions, then displays the result in decimal, hexadecimal, octal, and binary. |
| Financial | Calculates simple interest, compound interest, loan payments, and regular-payment future value. |
| Engineering | Provides Ohm's law, electrical power, force, real quadratic roots, and Celsius/Fahrenheit/Kelvin conversions. |

## Example expressions

Enter these in the relevant expression-based mode:

```text
2 + 3 * 4
sqrt(16) + log10(100)
sin(pi / 2)
0xFF + 1
0b1010 & 0b1100
```

## Development

Run tests from the repository root:

```bash
python -m pip install pytest
python -m pytest -q
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and contribution guidelines. Please review the [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

## Project health

- [Report a bug](https://github.com/BairaboinaLokeshKumarYadav/calcservice-python/issues/new?template=bug_report.yml)
- [Request a feature](https://github.com/BairaboinaLokeshKumarYadav/calcservice-python/issues/new?template=feature_request.yml)
- [Get support](SUPPORT.md)
- [Report a security issue](SECURITY.md)

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).
