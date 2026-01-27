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
from calservice import basic_calculator, scientific_calculator, programmer_calculator

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

# Run the main function when script is executed directly
if __name__ == "__main__":
    main()
