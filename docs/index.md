# Calculator Service

**A straightforward command-line calculator with five specialized modes.**

[Get started](#quick-start){ .md-button .md-button--primary }
[Explore the user guide](USER_GUIDE.md){ .md-button }

## Choose a calculator

| Mode | Use it for |
| --- | --- |
| **Basic** | Everyday arithmetic, parentheses, powers, and a few handy functions. |
| **Scientific** | Trigonometry, logarithms, exponentials, roots, and other math functions. |
| **Programmer** | Integer arithmetic, bitwise operations, and binary/octal/hexadecimal values. |
| **Financial** | Simple and compound interest, loan payments, and payment growth. |
| **Engineering** | Ohm's law, power, force, quadratic roots, and temperature conversions. |

Each mode guides you through its inputs. The [user guide](USER_GUIDE.md) has syntax, examples, formulas, and important limitations for every calculator.

## Quick start

You need Python 3.11 or newer. The calculator uses only the Python standard library.

```bash
python main.py
```

Choose a calculator from the menu and follow the prompts. Use `exit` or `quit` to return from expression prompts, and choose **6. Exit** to close the application.

## Try an expression

```text
2 + 3 * 4
sin(pi / 2)
0xFF + 1
0b1010 & 0b1100
```

Expressions are parsed using a restricted set of operations and functions; the calculator is not a Python interpreter. Scientific trigonometric functions use radians.

!!! warning "Use calculations responsibly"
    Financial results are estimates, not financial advice. Engineering calculations are basic formula helpers and are not a substitute for validated analysis, particularly in safety-critical applications.

## Project links

- [Source code](https://github.com/BairaboinaLokeshKumarYadav/calcservice-python)
- [Report a bug](https://github.com/BairaboinaLokeshKumarYadav/calcservice-python/issues/new?template=bug_report.yml)
- [Request a feature](https://github.com/BairaboinaLokeshKumarYadav/calcservice-python/issues/new?template=feature_request.yml)
- [Contribution and community information](community.md)
