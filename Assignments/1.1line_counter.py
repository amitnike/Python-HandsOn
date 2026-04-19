#!/usr/bin/env python3
# line_counter.py - Counts the number of lines in a given file.
# Usage: python line_counter.py <filename>

import sys

def count_lines(filename):
    """Open the file and return the number of lines."""
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

def main():
    # Ensure exactly one argument (the filename) is provided
    if len(sys.argv) != 2:
        print("Usage: python line_counter.py <filename>")
        print("Error: Please provide exactly one filename as an argument.")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        line_count = count_lines(filename)
        print(f"{filename} has {line_count} line(s).")
    except FileNotFoundError:
        # Triggered when the specified file does not exist
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except IsADirectoryError:
        # Triggered when a directory path is given instead of a file
        print(f"Error: '{filename}' is a directory, not a file.")
        sys.exit(1)
    except PermissionError:
        # Triggered when the script lacks read permissions for the file
        print(f"Error: Permission denied when reading '{filename}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
