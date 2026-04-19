#!/usr/bin/env python3
# squares.py - Demonstrates list comprehensions vs generator expressions.

import sys

# --- Part 1: List Comprehension ---
# Syntax: [expression for item in iterable]
# Builds the ENTIRE list in memory immediately when this line executes.
# Use when you need random access, len(), or to reuse the collection multiple times.

squares_list = [x ** 2 for x in range(1, 21)]

print("=== List Comprehension ===")
print(squares_list)
print(f"Memory used: {sys.getsizeof(squares_list)} bytes\n")


# --- Part 2: Generator Expression ---
# Syntax: (expression for item in iterable)  <-- parentheses instead of brackets
# Does NOT compute values upfront. It yields one value at a time on demand (lazy evaluation).
# Much more memory-efficient for large sequences since only one value exists in memory at a time.
# Trade-off: can only be iterated ONCE; no indexing or len() support.

squares_gen = (x ** 2 for x in range(1, 21))

print("=== Generator Expression ===")
for square in squares_gen:   # Values are computed one by one here, not before
    print(square, end=" ")
print()
print(f"Memory used: {sys.getsizeof(squares_gen)} bytes\n")
