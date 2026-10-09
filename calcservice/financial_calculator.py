import math


def _read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def financial_calculator() -> None:
    """Interactive financial calculator with common formulas."""
    print("\nFinancial Calculator")
    while True:
        print("\nChoose an option:")
        print("1. Simple interest")
        print("2. Compound interest")
        print("3. Monthly loan payment")
        print("4. Future value")
        print("5. Return to main menu")
        choice = input("Enter your choice: ").strip()

        if choice.lower() in {"exit", "5", "quit"}:
            print("Returning to main menu...")
            break

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please select a number between 1 and 5.")
            continue

        if choice == 1:
            principal = _read_float("Principal amount: ")
            rate = _read_float("Annual rate (%) : ") / 100.0
            years = _read_float("Time in years: ")
            interest = principal * rate * years
            total = principal + interest
            print(f"Interest: {interest:.2f}")
            print(f"Total amount: {total:.2f}")
        elif choice == 2:
            principal = _read_float("Principal amount: ")
            rate = _read_float("Annual rate (%) : ") / 100.0
            years = _read_float("Time in years: ")
            periods = _read_float("Compounding periods per year: ")
            total = principal * ((1 + rate / periods) ** (periods * years))
            interest = total - principal
            print(f"Future value: {total:.2f}")
            print(f"Compound interest: {interest:.2f}")
        elif choice == 3:
            principal = _read_float("Loan amount: ")
            annual_rate = _read_float("Annual interest rate (%) : ") / 100.0
            months = _read_float("Loan term in months: ")
            monthly_rate = annual_rate / 12.0
            if monthly_rate == 0:
                payment = principal / months
            else:
                payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** (-months))
            print(f"Monthly payment: {payment:.2f}")
        elif choice == 4:
            payment = _read_float("Regular payment: ")
            annual_rate = _read_float("Annual rate (%) : ") / 100.0
            years = _read_float("Years: ")
            periods = _read_float("Payments per year: ")
            rate = annual_rate / periods
            total = payment * (((1 + rate) ** (periods * years) - 1) / rate)
            print(f"Future value: {total:.2f}")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


__all__ = ["financial_calculator"]
