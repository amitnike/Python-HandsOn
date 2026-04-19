#!/usr/bin/env python3
# csv_filter.py - Reads a sales CSV file and filters records by a user-specified year.
# Uses a generator to process rows one at a time, keeping memory usage low.
# Outputs filtered records to a new CSV file, preserving the original header.

import csv
import os


# --- Generator Function ---

def filtered_rows(reader, year):
    """
    Generator that yields only rows whose 'date' field matches the given year.
    Processes one row at a time — never loads the entire file into memory.

    Args:
        reader: A csv.DictReader instance (iterable of row dicts).
        year  : The target year as a string (e.g. '2023').
    """
    for row in reader:
        # Extract the year portion from the date field (expected format: YYYY-MM-DD)
        row_year = row["date"].split("-")[0]
        if row_year == year:
            yield row  # Only yield rows that match the target year


def filter_csv_by_year(input_file, output_file, year):
    """
    Read input_file, filter rows matching year, and write results to output_file.
    The CSV header is always preserved in the output.
    """
    # Verify the input file exists before proceeding
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    try:
        with open(input_file, "r", newline="", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)  # Reads header automatically as field names

            # Capture the header from the reader before iterating
            fieldnames = reader.fieldnames
            if not fieldnames:
                print("Error: CSV file appears to be empty or has no header.")
                return

            with open(output_file, "w", newline="", encoding="utf-8") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()  # Write the original header to the output file

                count = 0
                # Use the generator — rows are processed one at a time
                for row in filtered_rows(reader, year):
                    writer.writerow(row)
                    count += 1

        if count > 0:
            print(f"Done. {count} record(s) for year {year} written to '{output_file}'.")
        else:
            print(f"No records found for year {year}. Output file created but is empty (header only).")

    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_file}'.")
    except KeyError:
        print("Error: 'date' column not found in the CSV file.")
    except csv.Error as e:
        print(f"Error: Failed to parse CSV — {e}")


# --- Main Script ---

input_file = input("Enter path to input CSV file : ").strip()
year       = input("Enter year to filter (e.g. 2023): ").strip()

# Validate year input
if not year.isdigit() or len(year) != 4:
    print("Error: Please enter a valid 4-digit year.")
else:
    # Build output filename automatically: sales_data_2023.csv
    base, ext  = os.path.splitext(input_file)
    output_file = f"{base}_{year}{ext}"

    filter_csv_by_year(input_file, output_file, year)
