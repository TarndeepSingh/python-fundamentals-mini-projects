"""
Project: Calculator
Description: A command-line calculator that performs basic arithmetic
operations and allows continuous calculations.
"""

from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    # Get first number safely
    try:
        num1 = float(input("What is the first number?: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return calculator()

    should_continue = True

    while should_continue:
        print("\nAvailable operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ").strip()

        if operation_symbol not in operations:
            print("❌ Invalid operation. Please choose a valid operator.")
            continue

        try:
            num2 = float(input("What is the next number?: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        try:
            result = operations[operation_symbol](num1, num2)
        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")
            continue

        print(f"\n{num1} {operation_symbol} {num2} = {result}")

        choice = input(
            f"\nType 'y' to continue calculating with {result}, "
            "or type 'n' to start a new calculation, "
            "or type 'q' to quit:\n"
        ).lower().strip()

        if choice == "y":
            num1 = result
        elif choice == "n":
            print("\n" * 20)
            calculator()
            return
        elif choice == "q":
            print("Goodbye 👋")
            should_continue = False
        else:
            print("❌ Invalid choice. Please try again.")


calculator()

