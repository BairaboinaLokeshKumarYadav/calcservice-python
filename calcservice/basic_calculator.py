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
    print("\nBasic Calculator")

    # Main calculation loop with error handling

    while True:

        expression = input(
            "\nEnter the expression (e.g., 2 + 3 * 4) or ('exit' to return to main menu): "
        )
        if expression.lower() in ["exit"]:
            break
        try:
            # Evaluate the expression
            result = eval(expression)
            print("-" * 50)
            print("The result is: ", result)
            print("-" * 50)
        except Exception as e:
            print("-" * 50)
            print(
                f"Invalid input. Please enter a valid mathematical expression. Error: {str(e)}"
            )
            print("-" * 50)
