from . import math

def scientific_calculator() -> None:
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

    # Main calculation loop with error handling
    
    while True:
        expression = input("\nEnter the expression (e.g., sin(pi/2), sqrt(16)) or ('exit' to return to main menu): ")
        if expression.lower() in ['exit']:
            break

        try:
             # Evaluate in restricted context for security
            result = eval(expression, {"__builtins__": {}}, functions)
            print("-"*50)
            print("The result is: ", result)
            print("-"*50)
        except Exception as e:
            print("-"*50)
            print(f"Invalid input. Please enter a valid mathematical expression. Error: {str(e)}")
            print("-"*50)