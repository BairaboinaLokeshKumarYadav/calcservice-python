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