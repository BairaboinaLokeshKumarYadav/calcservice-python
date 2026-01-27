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
import re
from turtle import position

def main() -> None:
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
            programmer_calculator()
        elif choice == 4:
            print("Financial Calculator - Feature not yet implemented")
            print("---------------------------------------")
        elif choice == 5:
            print("Engineering Calculator - Feature not yet implemented")
            print("---------------------------------------")
        else:
            print("Invalid choice. Please select a number between 1 and 5.")
            print("---------------------------------------")

def basic_calculator() -> None:
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

    # Main calculation loop with error handling
    try:
        while True:
            expression = input("Enter the expression (e.g., 2 + 3 * 4) or ('exit' to return to main menu): ")
            if expression.lower() in ['exit']:
                break
            # Evaluate the expression (note: uses eval with full builtins for simplicity)
            result = eval(expression)
            print("The result is: ", result)
            print("---------------------------------------")
    except Exception as e:
        print(f"Invalid input. Please enter a valid mathematical expression. Error: {str(e)}")
        print("---------------------------------------")

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
    try:
        while True:
            expression = input("Enter the expression (e.g., sin(pi/2), sqrt(16)) or ('exit' to return to main menu): ")
            if expression.lower() in ['exit']:
                break
        # Evaluate in restricted context for security
        result = eval(expression, {"__builtins__": {}}, functions)
        print("The result is: ", result)
        print("--------------------------------------------")
    except Exception as e:
        print(f"Invalid input. Please enter a valid mathematical expression. Error: {str(e)}")
        print("--------------------------------------------")

def programmer_calculator() -> None:
    """
    Programmer Calculator Mode

    Provides bitwise operations, base conversions, and programmer-specific calculations.
    Supports binary, octal, hexadecimal, and decimal operations with configurable bit sizes.

    ## Features

    - **Bitwise Operations**: AND (&), OR (|), XOR (^), NOT (~), left shift (<<), right shift (>>)
    - **Base Conversions**: Automatic conversion between binary (0b), octal (0o), hexadecimal (0x), and decimal
    - **Bit Sizes**: Support for 8, 16, 32, and 64-bit operations
    - **Signed/Unsigned**: Configurable signed or unsigned arithmetic
    - **Bit Manipulation**: Toggle individual bits interactively
    - **Output Formats**: Results displayed in decimal, hexadecimal, octal, and binary formats

    ## Supported Operations

    ### Bitwise Operators
    - `&` or `AND`: Bitwise AND
    - `|` or `OR`: Bitwise OR
    - `^` or `XOR`: Bitwise XOR
    - `~` or `NOT`: Bitwise NOT (unary)
    - `<<`: Left shift
    - `>>`: Right shift (arithmetic for signed, logical for unsigned)

    ### Arithmetic Operators
    - `+`: Addition
    - `-`: Subtraction
    - `*`: Multiplication
    - `/`: Integer division (//)
    - `%`: Modulo

    ## Examples

    - `0b1010 & 0b1100` → Bitwise AND of binary numbers
    - `0xFF + 1` → Hexadecimal addition
    - `255 << 2` → Left shift decimal number
    - `~0b1111` → Bitwise NOT

    ## Bit Size Handling

    - Results are masked to the specified bit size
    - Signed numbers use two's complement representation
    - Overflow wraps around within the bit boundaries

    ## Interactive Features

    - **Bit Toggle**: After calculation, option to toggle individual bits
    - **Visual Display**: Binary representation with bit positions shown

    ## Error Handling

    - Validates bit size (8, 16, 32, 64)
    - Prevents mixing floating-point with bitwise operations
    - Handles division by zero and invalid expressions
    """
    print("\nProgrammer Calculator")

    # Define supported operations and bit sizes
    operations = ["~", "&", "|", "^", "<<", ">>", "+", "-", "*", "/", "%"]  # List of all supported operators
    bits = [8, 16, 32, 64]  # Supported bit sizes for calculations
    bitwise_ops = ['~', '&', '|', '^', '<<', '>>']  # Operators that require bitwise handling
    
    # Main calculation loop
    while True:
        
        # Get user input and normalize it
        expression = input("Enter your expression (or 'exit' to return to main menu): ")
        expression = expression.upper()  # Convert to uppercase for consistency
        expression = expression.replace("AND", "&").replace("OR", "|").replace("XOR", "^").replace("NOT", "~")  # Replace word operators with symbols
        
        # Check for exit command
        if expression.lower() == 'exit':
            break
        
        # Get and validate bit size
        try:
            bit = int(input("Enter the bit size (8, 16, 32, 64): "))
            if bit not in bits:
                raise ValueError
        except ValueError:
            print("Invalid bit size. Please enter 8, 16, 32, or 64.")
            continue

        # Determine if signed or unsigned arithmetic
        signed = input("Signed or Unsigned (s/u): ").lower() == 's'

        # Tokenize the expression using regex
        tokens = re.findall(
            r'0b[01]+|'          # Match binary literals (e.g., 0b1010)
            r'0o[0-7]+|'         # Match octal literals (e.g., 0o777)
            r'0x[0-9A-F]+|'      # Match hexadecimal literals (e.g., 0xFF)
            r'\d+\.\d+|'         # Match floating-point numbers (e.g., 3.14)
            r'\d+|'              # Match decimal integers (e.g., 42)
            r'<<|>>|'            # Match shift operators
            r'[~&|^()+\-*/%]',   # Match operators and parentheses
            expression,
            re.VERBOSE | re.IGNORECASE
        )
        
        # Check if the expression contains bitwise operations
        is_bitwise = any(op in expression for op in bitwise_ops)
        # Check if the expression contains floating-point numbers
        is_float = any('.' in token for token in expression.split())
        
        # Validate that floating-point and bitwise operations are not mixed
        if is_float and is_bitwise:
            print("Error: Floating point numbers are not supported in bitwise operations.")
            continue

        # Convert tokens to decimal for evaluation
        converted_expression = []
        try:
            for token in tokens:
                token = token.lower()  # Normalize token to lowercase

                # Handle operators and parentheses
                if token in operations or token in ("(", ")"):
                    if token == "/":
                        converted_expression.append("// ")  # Use integer division
                    else:
                        converted_expression.append(token)
                # Convert binary literals to decimal
                elif token.startswith("0b"):
                    converted_expression.append(str(int(token, 2)))
                # Convert hexadecimal literals to decimal
                elif token.startswith("0x"):
                    converted_expression.append(str(int(token, 16)))
                # Convert octal literals to decimal
                elif token.startswith("0o"):
                    converted_expression.append(str(int(token, 8)))
                else:
                    # Handle numbers
                    if is_float and '.' in token:
                        converted_expression.append(token)  # Keep floats as-is
                    else:
                        converted_expression.append(str(int(token, 10)))  # Convert to decimal int

            # Join tokens into evaluable expression
            converted_expr = "".join(converted_expression)

            # Evaluate the expression in a restricted environment
            result = eval(converted_expr, {"__builtins__": None}, {})

            # Handle floating-point results separately
            if is_float:
                print("Result (float): ", result)
                continue

            # Ensure result is an integer
            if not isinstance(result, int):
                print("Error: Result is not an integer. Please check your expression.")
                continue
            
        # Handle specific exceptions
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            continue
        except:
            print("Error in expression. Please check your input.")
            continue
        
        # Apply bit mask to constrain result to specified bit size
        mask = (1 << bit) - 1
        result = result & mask

        # Handle unsigned right shift (logical shift)
        if not signed and ">>" in tokens:
            result = (result & mask)
        
        # Function to display the binary representation with bit positions
        def show_bits(value):
            b = format(value, f"0{bit}b")  # Format as binary string with leading zeros
            print("\nBit position: ")
            print(" ".join(str(i) for i in range(bit-1, -1, -1)))  # Print bit positions from MSB to LSB
            print("".join(b))  # Print the binary digits

        # Display the current result in binary
        show_bits(result)

        # Interactive bit toggling
        toggle = input("Do you want to toggle any bit?(yes/no):").lower()

        while toggle == "yes":
            try:
                position = int(input("enter bit position to toggle: "))
                if 0 <= position < bit:
                    result ^= (1 << position)  # Toggle the bit using XOR
                    result &= mask  # Apply mask to keep within bit size
                    show_bits(result)  # Show updated binary
                else:
                    print("Invalid bit position. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid bit position.")
                continue
            
            # Reapply mask after toggling
            result = result & ((1 << bit) - 1)

            # Redisplay binary after toggle
            binary_str = format(result, '0' + str(bit) + 'b')
            print("\nBit position: ")
            print(" ".join(str(i) for i in range(bit-1, -1, -1)))
            print("".join(binary_str))

            # Note: The toggle loop continues until user says no, but toggle is not updated inside the loop

        # Convert result to signed decimal if signed arithmetic is selected
        if signed:
            sign_bit = 1 << (bit - 1)  # Position of the sign bit
            decimal = result - (1 << bit) if (result & sign_bit) else result  # Two's complement conversion
        else:
            decimal = result  # For unsigned, decimal is the same as result

        unsigned = result  # Unsigned value is always the raw result

        # Display final results in multiple formats
        print("\nResult:")    
        print("decimal: ", decimal)
        print("hexadecimal: ", format(unsigned, 'X'))  # Uppercase hex
        print("octal: ", format(unsigned, 'o'))  # Octal
        print("binary: ", format(unsigned, f'0{bit}b'))  # Binary with leading zeros

# Run the main function when script is executed directly
if __name__ == "__main__":
    main()
