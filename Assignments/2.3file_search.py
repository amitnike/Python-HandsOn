#!/usr/bin/env python3
# file_search.py - Searches for a string across all .txt files in a given directory.
# Usage: python file_search.py

import os

def search_in_files(directory, search_string):
    """
    Search for search_string in every .txt file inside directory.
    Prints the name of each file that contains the string.
    """
    # Verify the directory exists and is actually a directory
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        return

    # List all entries in the directory
    try:
        entries = os.listdir(directory)
    except PermissionError:
        print(f"Error: Permission denied when accessing '{directory}'.")
        return

    # Filter to .txt files only
    txt_files = [f for f in entries if f.endswith(".txt")]

    if not txt_files:
        print(f"No .txt files found in '{directory}'.")
        return

    print(f"\nSearching for '{search_string}' in {len(txt_files)} .txt file(s)...\n")

    matches = []

    for filename in txt_files:
        filepath = os.path.join(directory, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                contents = f.read()

            # Case-insensitive search — compare both in lowercase
            if search_string.lower() in contents.lower():
                matches.append(filename)

        except PermissionError:
            print(f"  [SKIPPED] Permission denied: '{filename}'")
        except UnicodeDecodeError:
            print(f"  [SKIPPED] Could not decode file (non-UTF-8): '{filename}'")
        except OSError as e:
            print(f"  [SKIPPED] Could not read '{filename}': {e}")

    # --- Report results ---
    if matches:
        print(f"Found '{search_string}' in {len(matches)} file(s):")
        for name in matches:
            print(f"  - {name}")
    else:
        print(f"No files contain the string '{search_string}'.")


# --- Main Script ---

directory     = input("Enter directory path to search: ").strip()
search_string = input("Enter string to search for   : ").strip()

if not search_string:
    print("Error: Search string cannot be empty.")
else:
    search_in_files(directory, search_string)
