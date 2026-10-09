from calcservice import (
    basic_calculator,
    engineering_calculator,
    financial_calculator,
    programmer_calculator,
    scientific_calculator,
)


def main() -> None:
    while True:
        print("\nCalculator Service")
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. Programmer Calculator")
        print("4. Financial Calculator")
        print("5. Engineering Calculator")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            basic_calculator()
        elif choice == 2:
            scientific_calculator()
        elif choice == 3:
            programmer_calculator()
        elif choice == 4:
            financial_calculator()
        elif choice == 5:
            engineering_calculator()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
