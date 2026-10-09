import math


def _read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def engineering_calculator() -> None:
    """Small engineering toolkit with common formulas."""
    print("\nEngineering Calculator")
    while True:
        print("\nChoose an engineering tool:")
        print("1. Ohm's law")
        print("2. Power (P = V * I)")
        print("3. Force (F = m * a)")
        print("4. Quadratic roots")
        print("5. Temperature conversion")
        print("6. Return to main menu")
        choice = input("Enter your choice: ").strip()

        if choice.lower() in {"exit", "6", "quit"}:
            print("Returning to main menu...")
            break

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please select a number between 1 and 6.")
            continue

        if choice == 1:
            voltage = _read_float("Voltage (V): ")
            resistance = _read_float("Resistance (ohm): ")
            current = voltage / resistance if resistance else 0
            print(f"Current: {current:.4f} A")
        elif choice == 2:
            voltage = _read_float("Voltage (V): ")
            current = _read_float("Current (A): ")
            power = voltage * current
            print(f"Power: {power:.4f} W")
        elif choice == 3:
            mass = _read_float("Mass (kg): ")
            acceleration = _read_float("Acceleration (m/s^2): ")
            force = mass * acceleration
            print(f"Force: {force:.4f} N")
        elif choice == 4:
            a = _read_float("Coefficient a: ")
            b = _read_float("Coefficient b: ")
            c = _read_float("Coefficient c: ")
            disc = b * b - 4 * a * c
            if disc < 0:
                print("The equation has no real roots.")
            else:
                root1 = (-b + math.sqrt(disc)) / (2 * a)
                root2 = (-b - math.sqrt(disc)) / (2 * a)
                print(f"Root 1: {root1:.4f}")
                print(f"Root 2: {root2:.4f}")
        elif choice == 5:
            temp = _read_float("Temperature value: ")
            unit = input("Convert from C/F/K? ").strip().lower()
            if unit == "c":
                print(f"F: {(temp * 9 / 5) + 32:.2f}")
                print(f"K: {temp + 273.15:.2f}")
            elif unit == "f":
                print(f"C: {(temp - 32) * 5 / 9:.2f}")
                print(f"K: {((temp - 32) * 5 / 9) + 273.15:.2f}")
            elif unit == "k":
                print(f"C: {temp - 273.15:.2f}")
                print(f"F: {((temp - 273.15) * 9 / 5) + 32:.2f}")
            else:
                print("Unsupported unit. Use C, F, or K.")
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please select 1 to 6.")


__all__ = ["engineering_calculator"]
