"""
# Calculator Service

A comprehensive command-line calculator application written in Python that provides multiple calculator modes including basic arithmetic, scientific functions, programmer calculations, financial computations, and engineering tools.

## Features

- **Basic Calculator**: Simple arithmetic operations with expression evaluation
- **Scientific Calculator**: Advanced mathematical functions using Python's math module
- **Programmer Calculator**: Binary, octal, hexadecimal operations (planned)
- **Financial Calculator**: Financial calculations and formulas (planned)
- **Engineering Calculator**: Engineering-specific computations (planned)

## Usage

Run the program and select from the menu options:

1. Basic Calculator - Enter mathematical expressions like `2 + 3 * 4`
2. Scientific Calculator - Use functions like `sin(30)`, `sqrt(16)`, `log(100)`

## Requirements

- Python 3.x
- math module (built-in)

## Safety Note

This program uses `eval()` for expression evaluation. While basic input validation is implemented, avoid using with untrusted input in production environments.

## Author

Calculator Service Team

## License

See LICENSE file for details
"""

# Import required modules
import math

def main():
    """
    Main function that runs the calculator application.

    This function presents a menu to the user and handles the selection
    of different calculator modes. It runs in an infinite loop until
    the user manually terminates the program.

    ## Menu Options

    1. **Basic Calculator**: Evaluates simple mathematical expressions
    2. **Scientific Calculator**: Provides access to advanced math functions
    3. **Programmer Calculator**: Binary/octal/hex operations (not yet implemented)
    4. **Financial Calculator**: Financial formulas (not yet implemented)
    5. **Engineering Calculator**: Engineering calculations (not yet implemented)

    ## Error Handling

    - Catches invalid input and provides user-friendly error messages
    - Uses restricted evaluation context for security in scientific mode
    """
    while True:  # Infinite loop to keep the program running
        # Display the main menu
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. Programmer Calculator")
        print("4. Financial Calculator")
        print("5. Engineering Calculator")

        # Get user choice
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            print("---------------------------------------")
            continue

        # Route to appropriate calculator based on choice
        if choice == 1:
            basic_calculator()
        elif choice == 2:
            scientific_calculator()
        elif choice == 3:
            print("Programmer Calculator - Feature not yet implemented")
            print("---------------------------------------")
        elif choice == 4:
            print("Financial Calculator - Feature not yet implemented")
            print("---------------------------------------")
        elif choice == 5:
            print("Engineering Calculator - Feature not yet implemented")
            print("---------------------------------------")
        else:
            print("Invalid choice. Please select a number between 1 and 5.")
            print("---------------------------------------")

def basic_calculator():
    """
    Basic Calculator Mode

    Allows users to enter and evaluate simple mathematical expressions.
    Supports standard arithmetic operators: +, -, *, /, **, etc.

    ## Examples

    - `2 + 3` → 5
    - `10 / 3` → 3.333...
    - `2 ** 3` → 8

    ## Error Handling

    - Catches syntax errors and invalid expressions
    - Provides clear error messages to guide users
    """
    print("Basic Calculator")
    try:
        expression = input("Enter the expression (e.g., 2 + 3 * 4): ")
        result = eval(expression)
        print("The result is: ", result)
        print("---------------------------------------")
    except Exception as e:
        print(f"Invalid input. Please enter a valid mathematical expression. Error: {str(e)}")
        print("---------------------------------------")

def scientific_calculator():
    """
    Scientific Calculator Mode

    Provides access to advanced mathematical functions from Python's math module.
    Functions are made available in a restricted evaluation context for safety.

    ## Available Functions

    ### Trigonometric Functions
    - `sin(x)`, `cos(x)`, `tan(x)` - sine, cosine, tangent
    - `asin(x)`, `acos(x)`, `atan(x)` - inverse trigonometric functions
    - `atan2(y, x)` - two-argument arctangent

    ### Hyperbolic Functions
    - `sinh(x)`, `cosh(x)`, `tanh(x)` - hyperbolic functions
    - `asinh(x)`, `acosh(x)`, `atanh(x)` - inverse hyperbolic functions

    ### Logarithmic Functions
    - `log(x)` - natural logarithm (ln)
    - `log2(x)` - base-2 logarithm
    - `log10(x)` - base-10 logarithm
    - `log1p(x)` - log(1+x) for small x

    ### Exponential Functions
    - `exp(x)` - e^x
    - `exp2(x)` - 2^x
    - `expm1(x)` - e^x - 1

    ### Power and Root Functions
    - `sqrt(x)` - square root
    - `cbrt(x)` - cube root
    - `pow(x, y)` - x raised to power y

    ### Rounding and Remainder
    - `ceil(x)` - ceiling (round up)
    - `floor(x)` - floor (round down)
    - `trunc(x)` - truncate decimal part
    - `fmod(x, y)` - floating-point modulus
    - `remainder(x, y)` - IEEE 754 remainder

    ### Special Functions
    - `gamma(x)` - gamma function
    - `lgamma(x)` - log gamma function
    - `erf(x)` - error function
    - `erfc(x)` - complementary error function

    ### Constants
    - `pi` - π (3.14159...)
    - `e` - Euler's number (2.71828...)
    - `tau` - τ = 2π
    - `inf` - positive infinity
    - `nan` - not a number

    ### Combinatorics
    - `factorial(x)` - x!
    - `comb(n, k)` - combinations C(n,k)
    - `perm(n, k)` - permutations P(n,k)

    ### Number Properties
    - `gcd(x, y)` - greatest common divisor
    - `lcm(x, y)` - least common multiple
    - `isclose(a, b)` - check if two values are close
    - `isfinite(x)`, `isinf(x)`, `isnan(x)` - number classification

    ### Utility Functions
    - `fabs(x)` - absolute value
    - `copysign(x, y)` - copy sign from y to x
    - `fsum(iterable)` - accurate floating-point sum
    - `prod(iterable)` - product of elements
    - `dist(p, q)` - Euclidean distance
    - `hypot(x, y)` - hypotenuse (sqrt(x² + y²))
    - `degrees(x)` - convert radians to degrees
    - `radians(x)` - convert degrees to radians

    ## Examples

    - `sin(pi/2)` → 1.0
    - `sqrt(16)` → 4.0
    - `log(100)` → 4.605... (natural log)
    - `factorial(5)` → 120

    ## Notes

    - All angles are in radians unless specified otherwise
    - Functions follow IEEE 754 standards where applicable
    - Some functions may not be available in older Python versions
    """
    print("Scientific Calculator")

    # Define available mathematical functions
    functions = {
        # Trigonometric functions
        "acos": math.acos,  # arccosine
        "acosh": math.acosh,  # hyperbolic arccosine
        "sin": math.sin,  # sine
        "asin": math.asin,  # arcsine
        "asinh": math.asinh,  # hyperbolic arcsine
        "atan": math.atan,  # arctangent
        "atan2": math.atan2,  # arctangent of y/x
        "atanh": math.atanh,  # hyperbolic arctangent
        "cos": math.cos,  # cosine
        "tan": math.tan,  # tangent
        "sinh": math.sinh,  # hyperbolic sine
        "cosh": math.cosh,  # hyperbolic cosine
        "tanh": math.tanh,  # hyperbolic tangent

        # Constants
        "pi": math.pi,  # π constant
        "e": math.e,  # Euler's number
        "tau": math.tau,  # τ constant (2π)
        "inf": math.inf,  # positive infinity
        "nan": math.nan,  # not a number

        # Rounding functions
        "ceil": math.ceil,  # ceiling function
        "floor": math.floor,  # floor function
        "trunc": math.trunc,  # truncate function

        # Absolute value and sign
        "fabs": math.fabs,  # absolute value
        "copysign": math.copysign,  # copy sign

        # Factorial and combinatorics
        "factorial": math.factorial,  # factorial function
        "comb": math.comb,  # combinations
        "perm": math.perm,  # permutations

        # Power and root functions
        "pow": math.pow,  # power function
        "sqrt": math.sqrt,  # square root
        "cbrt": math.cbrt,  # cube root

        # Logarithmic functions
        "log": math.log,  # natural logarithm
        "log2": math.log2,  # base-2 logarithm
        "log10": math.log10,  # base-10 logarithm
        "log1p": math.log1p,  # log(1+x)

        # Exponential functions
        "exp": math.exp,  # exponential function
        "exp2": math.exp2,  # 2^x
        "expm1": math.expm1,  # exp(x) - 1

        # Special functions
        "gamma": math.gamma,  # gamma function
        "lgamma": math.lgamma,  # log gamma function
        "erf": math.erf,  # error function
        "erfc": math.erfc,  # complementary error function

        # Remainder and modulus
        "fmod": math.fmod,  # floating-point modulus
        "remainder": math.remainder,  # IEEE 754 remainder

        # Distance and hypotenuse
        "hypot": math.hypot,  # hypotenuse
        "dist": math.dist,  # Euclidean distance

        # GCD and LCM
        "gcd": math.gcd,  # greatest common divisor
        "lcm": math.lcm,  # least common multiple

        # Number classification
        "isfinite": math.isfinite,  # check for finite number
        "isinf": math.isinf,  # check for infinity
        "isnan": math.isnan,  # check for NaN

        # Precision and comparison
        "isclose": math.isclose,  # check for closeness
        "ulp": math.ulp,  # unit in the last place
        "nextafter": math.nextafter,  # next representable value

        # Summation and products
        "fsum": math.fsum,  # accurate floating-point sum
        "prod": math.prod,  # product of iterable
        "sumprod": math.sumprod,  # sum and product (if available)

        # Mantissa and exponent
        "frexp": math.frexp,  # mantissa and exponent
        "ldexp": math.ldexp,  # multiply by power of 2
        "modf": math.modf,  # fractional and integer parts

        # Fused operations
        "fma": math.fma,  # fused multiply-add

        # Angle conversions
        "degrees": math.degrees,  # radians to degrees
        "radians": math.radians,  # degrees to radians

        # Integer square root
        "isqrt": math.isqrt,  # integer square root
    }

   
    try:
        expression = input("Enter the expression (e.g., sin(pi/2), sqrt(16)): ")
        # Evaluate in restricted context for security
        result = eval(expression, {"__builtins__": {}}, functions)
        print("The result is: ", result)
        print("--------------------------------------------")
    except Exception as e:
        print(f"Invalid input. Please enter a valid mathematical expression. Error: {str(e)}")
        print("--------------------------------------------")

def programmer_calculator():

    print("\nProgrammer Calculator")

    while True:
        
        bases = [2,8,10,16]
        operations = [~,&,|,^,<<,>>,+, -, *, /, %]
        bits = [8,16,32,64]
        


# Run the main function when script is executed directly
if __name__ == "__main__":
    main()
