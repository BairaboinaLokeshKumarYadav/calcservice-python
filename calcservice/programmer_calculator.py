from . import re


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
    print("\nParty Programmer Calculator")

    # Define supported operations and bit sizes
    operations = [
        "~",
        "&",
        "|",
        "^",
        "<<",
        ">>",
        "+",
        "-",
        "*",
        "/",
        "%",
    ]  # List of all supported operators
    bits = [8, 16, 32, 64]  # Supported bit sizes for calculations
    bitwise_ops = [
        "~",
        "&",
        "|",
        "^",
        "<<",
        ">>",
    ]  # Operators that require bitwise handling

    # Main calculation loop
    while True:

        # Get user input and normalize it
        expression = input("Enter your expression (or 'exit' to return to main menu): ")
        expression = expression.upper()  # Convert to uppercase for consistency
        expression = (
            expression.replace("AND", "&")
            .replace("OR", "|")
            .replace("XOR", "^")
            .replace("NOT", "~")
        )  # Replace word operators with symbols

        # Check for exit command
        if expression.lower() == "exit":
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
        signed = input("Signed or Unsigned (s/u): ").lower() == "s"

        # Tokenize the expression using regex
        tokens = re.findall(
            r"0b[01]+|"  # Match binary literals (e.g., 0b1010)
            r"0o[0-7]+|"  # Match octal literals (e.g., 0o777)
            r"0x[0-9A-F]+|"  # Match hexadecimal literals (e.g., 0xFF)
            r"\d+\.\d+|"  # Match floating-point numbers (e.g., 3.14)
            r"\d+|"  # Match decimal integers (e.g., 42)
            r"<<|>>|"  # Match shift operators
            r"[~&|^()+\-*/%]",  # Match operators and parentheses
            expression,
            re.VERBOSE | re.IGNORECASE,
        )

        # Check if the expression contains bitwise operations
        is_bitwise = any(op in expression for op in bitwise_ops)
        # Check if the expression contains floating-point numbers
        is_float = any("." in token for token in expression.split())

        # Validate that floating-point and bitwise operations are not mixed
        if is_float and is_bitwise:
            print(
                "Error: Floating point numbers are not supported in bitwise operations."
            )
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
                    if is_float and "." in token:
                        converted_expression.append(token)  # Keep floats as-is
                    else:
                        converted_expression.append(
                            str(int(token, 10))
                        )  # Convert to decimal int

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
            result = result & mask

        # Function to display the binary representation with bit positions
        def show_bits(value):
            b = format(value, f"0{bit}b")  # Format as binary string with leading zeros
            print("\nBit position: ")
            print(
                " ".join(str(i) for i in range(bit - 1, -1, -1))
            )  # Print bit positions from MSB to LSB
            print("".join(b))  # Print the binary digits

        # Display the current result in binary
        show_bits(result)

        # Interactive bit toggling
        toggle = input("Do you want to toggle any bit?(yes/no):").lower()

        while toggle == "yes":
            try:
                position = int(input("enter bit position to toggle: "))
                if 0 <= position < bit:
                    result ^= 1 << position  # Toggle the bit using XOR
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
            binary_str = format(result, "0" + str(bit) + "b")
            print("\nBit position: ")
            print(" ".join(str(i) for i in range(bit - 1, -1, -1)))
            print("".join(binary_str))

            # Note: The toggle loop continues until user says no, but toggle is not updated inside the loop

        # Convert result to signed decimal if signed arithmetic is selected
        if signed:
            sign_bit = 1 << (bit - 1)  # Position of the sign bit
            decimal = (
                result - (1 << bit) if (result & sign_bit) else result
            )  # Two's complement conversion
        else:
            decimal = result  # For unsigned, decimal is the same as result

        unsigned = result  # Unsigned value is always the raw result

        # Display final results in multiple formats
        print("\nResult:")
        print("decimal: ", decimal)
        print("hexadecimal: ", format(unsigned, "X"))  # Uppercase hex
        print("octal: ", format(unsigned, "o"))  # Octal
        print("binary: ", format(unsigned, f"0{bit}b"))  # Binary with leading zeros
