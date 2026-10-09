# User Guide

This guide covers the calculator modes currently available in the command-line application. Start the program with `python main.py` and choose the mode from the main menu.

## Returning to the menu

At expression prompts, enter `exit` or `quit` to return to the main menu. In financial and engineering menus, select the return option; `exit` and `quit` also return. The main menu's final option closes the application.

## Basic calculator

Enter an arithmetic expression. Supported operations are addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), floor division (`//`), modulo (`%`), exponentiation (`**`), unary plus/minus, and parentheses. The constants `pi`, `e`, and `tau` and the functions `sqrt`, `pow`, `abs`, and `round` are also available.

Examples:

```text
2 + 3 * 4
(10 - 2) / 4
sqrt(16) + pi
round(10 / 3, 2)
```

Only numeric expressions using the supported syntax are evaluated; this is not a Python interpreter.

## Scientific calculator

Scientific mode supports arithmetic expressions, parentheses, the constants `pi`, `e`, `tau`, `inf`, and `nan`, and selected math functions:

- Trigonometry: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2`
- Hyperbolic functions: `sinh`, `cosh`, `tanh`, `asinh`, `acosh`, `atanh`
- Logarithms and exponentials: `log`, `log2`, `log10`, `log1p`, `exp`, `exp2`, `expm1`
- Roots, powers, and rounding: `sqrt`, `cbrt`, `pow`, `ceil`, `floor`, `trunc`
- Integer and number helpers: `factorial`, `gcd`, `lcm`, `comb`, `perm`, `isclose`, `isfinite`, `isinf`, `isnan`
- Other math functions: `fabs`, `copysign`, `hypot`, `dist`, `degrees`, `radians`, `fsum`, `prod`, `erf`, `erfc`, `gamma`, `lgamma`

Angles are in radians unless converted with `degrees()` or `radians()`. For example:

```text
sin(pi / 2)
degrees(atan(1))
factorial(5)
log(100, 10)
```

Functions accept positional arguments. Iterable-based functions such as `fsum`, `prod`, and `dist` currently cannot be called with list or tuple literals in the expression parser.

## Programmer calculator

Enter an integer expression using decimal, binary (`0b`), octal (`0o`), or hexadecimal (`0x`) literals. Supported arithmetic operators are `+`, `-`, `*`, `//`, `%`, and `**`; supported bitwise operators are `&`, `|`, `^`, `~`, `<<`, and `>>`. The word forms `AND`, `OR`, `XOR`, and `NOT` are converted to their corresponding operators.

After entering an expression, select an 8-, 16-, 32-, or 64-bit width and signed (`s`) or unsigned (`u`) display. Results wrap to the selected width. The calculator shows the bit positions and result in decimal, hexadecimal, octal, and binary. You can optionally toggle bit positions before the result is displayed.

Examples:

```text
0xFF + 1
0b1010 AND 0b1100
255 << 2
~0b1111
```

## Financial calculator

Choose one of the menu calculations:

1. **Simple interest**: enter principal, annual interest rate as a percentage, and time in years. Interest is calculated as `principal * annual_rate * years`.
2. **Compound interest**: enter principal, annual rate as a percentage, time in years, and compounding periods per year. Future value is `principal * (1 + annual_rate / periods) ** (periods * years)`.
3. **Monthly loan payment**: enter loan amount, annual rate as a percentage, and loan term in months. The annual rate is divided by 12 for the monthly rate.
4. **Future value of regular payments**: enter payment amount, annual rate as a percentage, number of years, and payments per year. This uses the ordinary-annuity formula, where each payment is assumed to occur at the end of a period.

Rates are entered as percentages (for example, enter `5` for 5%). Enter non-zero compounding/payment periods, years, and loan terms where the formula requires them. The future-value-of-payments calculation currently requires a non-zero rate; a zero rate is not handled separately. Calculations do not account for taxes, fees, inflation, payment timing variations, or rounding conventions used by financial institutions. Results are estimates, not financial advice.

## Engineering calculator

- **Ohm's law**: enter voltage in volts and resistance in ohms. Current is calculated as `I = V / R`. The current implementation displays zero when resistance is zero.
- **Electrical power**: enter voltage in volts and current in amperes. Power is calculated as `P = V * I` and displayed in watts.
- **Force**: enter mass in kilograms and acceleration in meters per second squared. Force is calculated as `F = m * a` and displayed in newtons.
- **Quadratic roots**: enter coefficients `a`, `b`, and `c` for `a*x^2 + b*x + c = 0`. Use a non-zero `a`. Real roots are displayed; equations with a negative discriminant are reported as having no real roots.
- **Temperature conversion**: enter a temperature and its source unit (`C`, `F`, or `K`). The equivalent values in the other two scales are displayed.

These are basic formula helpers and do not replace validated engineering analysis. Check units and assumptions before using results in real-world designs.

## Troubleshooting

- If an expression is rejected, check parentheses, operator spelling, and whether the function is supported in the selected mode.
- Scientific trigonometric functions expect radians.
- Programmer mode accepts integers only. Select the bit width and signedness when prompted.
- Financial period counts and loan terms must be non-zero for the formulas to be defined.
- Press `Ctrl+C` to interrupt the application if needed.
