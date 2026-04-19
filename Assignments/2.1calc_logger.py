#!/usr/bin/env python3
# calc_logger.py - A simple calculator that logs all operations and errors to error_log.txt.
# Supports: addition (+), subtraction (-), multiplication (*), division (/)

import os
from datetime import datetime

# Always place error_log.txt in the same folder as this script
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "error_log.txt")

# --- Custom Exceptions ---

class InvalidOperationError(Exception):
    """Raised when the user enters an unsupported operator."""
    pass

class InvalidNumberError(Exception):
    """Raised when the user enters a non-numeric value."""
    pass


# --- Logging Helper ---

def log(level, message):
    """Append a timestamped entry to the log file and print it to the console.
    The log file is created in the same folder as this script if not already present.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{level}] {message}"
    print(entry)
    # "a" mode: creates the file if it doesn't exist, appends if it does
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")


# --- Input Helpers ---

def get_number(prompt):
    """Prompt for a number and return it as a float. Raises InvalidNumberError on bad input."""
    raw = input(prompt).strip()
    try:
        return float(raw)
    except ValueError:
        raise InvalidNumberError(f"'{raw}' is not a valid number.")

def get_operator():
    """Prompt for an operator and validate it. Raises InvalidOperationError on bad input."""
    op = input("Enter operator (+, -, *, /): ").strip()
    if op not in ("+", "-", "*", "/"):
        raise InvalidOperationError(f"'{op}' is not a supported operator.")
    return op


# --- Calculator Logic ---

def calculate(a, op, b):
    """Perform the calculation and return the result."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero is undefined.")
        return a / b


# --- Main Script ---

print("Simple Calculator — all operations are logged to error_log.txt\n")

try:
    a  = get_number("Enter first number  : ")
    op = get_operator()
    b  = get_number("Enter second number : ")

    result = calculate(a, op, b)

    # Log successful operation
    log("INFO", f"{a} {op} {b} = {result}")
    print(f"\nResult: {result}")

except InvalidNumberError as e:
    log("ERROR", f"InvalidNumberError — {e}")

except InvalidOperationError as e:
    log("ERROR", f"InvalidOperationError — {e}")

except ZeroDivisionError as e:
    log("ERROR", f"ZeroDivisionError — {e}")
