#!/usr/bin/env python3
# filter_even.py - Filters even numbers from a list using filter_even_numbers().

def filter_even_numbers(numbers):
    """
    Accepts a list of numbers and returns a new list containing only the even ones.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        list: A list of even numbers from the input.
    """
    even_numbers = []  # Start with an empty result list

    # Iterate over each number in the input list
    for num in numbers:
        # Check if the number is divisible by 2 (i.e., even)
        if num % 2 == 0:
            even_numbers.append(num)  # Add even number to the result list

    return even_numbers


# --- Main script ---

# Predefined list of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 33, 42,43]

print(f"Original list : {numbers}")

# Call the function and store the result
evens = filter_even_numbers(numbers)

print(f"Even numbers  : {evens}")
