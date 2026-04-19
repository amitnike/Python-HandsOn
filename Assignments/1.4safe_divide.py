#!/usr/bin/env python3
# safe_divide.py - Asks the user for two numbers and divides the first by the second.
# Handles invalid input and division by zero gracefully using try-except blocks.

def get_number(prompt):
    """
    Prompt the user for a number and return it as a float.
    Raises ValueError if the input cannot be converted to a number.
    """
    value = input(prompt).strip()
    return float(value)  # Raises ValueError for non-numeric input


def divide(a, b):
    """
    Divide a by b and return the result.
    Raises ZeroDivisionError if b is zero.
    """
    return a / b  # Raises ZeroDivisionError when b == 0


# --- Main script ---

try:
    # Attempt to read two numbers from the user
    num1 = get_number("Enter the first number  : ")
    num2 = get_number("Enter the second number : ")

    # Attempt the division
    result = divide(num1, num2)

    print(f"\nResult: {num1} / {num2} = {result}")

except ValueError:
    # Triggered when the user enters something that isn't a valid number
    print("Error: Invalid input. Please enter numeric values only (e.g. 5, 3.14).")

except ZeroDivisionError:
    # Triggered when the second number is zero
    print("Error: Division by zero is not allowed. Please enter a non-zero divisor.")
