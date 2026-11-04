# ==============================================================================
# PANDAS DATAFRAME: COLUMN ACCESS, ROW INSERTION, EXPORT & DISPLAY OPTIONS
# ==============================================================================
# A DataFrame is a two-dimensional, size-mutable tabular data structure with
# labeled axes (rows and columns).
#
# Topics covered:
# 1. Accessing Single vs Multiple Columns
# 2. Dynamic Column Addition (df["Grade"] = ...)
# 3. Dynamic Row Insertion using .loc (df.loc[index] = ...)
# 4. Exporting DataFrames to External Files (.to_csv and .to_excel)
# 5. Configuring Pandas Display Settings (pd.options.display.max_rows & to_string)
# ==============================================================================

import pandas as pd
import numpy as np
import os

print("==================================================================")
print("1. DATAFRAME CREATION & COLUMN ACCESS")
print("==================================================================")

data = {
    "Name": ["Anu", "Ravi", "Priya", "Kiran"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Access a single column:
# Passing a single string returns a 1D Pandas Series
print("\n--- Access Single Column (Series): df['Name'] ---")
print(df["Name"])
print("Type:", type(df["Name"]))

# Access multiple columns:
# Passing a list of strings returns a 2D Pandas DataFrame
print("\n--- Access Multiple Columns (DataFrame): df[['Name', 'Marks']] ---")
print(df[["Name", "Marks"]])
print("Type:", type(df[["Name", "Marks"]]))


print("\n==================================================================")
print("2. DYNAMIC COLUMN & ROW INSERTION")
print("==================================================================")

# Adding a new column directly:
# Provide a list matching the exact row count of the DataFrame
df["Grade"] = ["A", "A+", "B", "A"]
print("DataFrame after adding 'Grade' column:")
print(df)

# Adding / modifying a row using .loc[label]:
# df.loc[4] inserts a new row at index 4 with the supplied values
df.loc[4] = ["Meena", 20, 92, "A+"]
print("\nDataFrame after inserting row at index 4:")
print(df)


print("\n==================================================================")
print("3. EXPORTING DATAFRAME TO CSV & EXCEL")
print("==================================================================")
# index=False prevents writing the numeric row index column into the exported file

# 1. Exporting to CSV (Comma-Separated Values)
csv_filename = "output.csv"
df.to_csv(csv_filename, index=False)
print(f"Successfully exported DataFrame to CSV: '{csv_filename}'")
if os.path.exists(csv_filename):
    print(f"File verified on disk ({os.path.getsize(csv_filename)} bytes)")

# 2. Exporting to Excel (.xlsx)
# Note: Requires openpyxl engine. Handled gracefully with fallback.
xlsx_filename = "output.xlsx"
try:
    df.to_excel(xlsx_filename, index=False)
    print(f"Successfully exported DataFrame to Excel: '{xlsx_filename}'")
    if os.path.exists(xlsx_filename):
        print(f"File verified on disk ({os.path.getsize(xlsx_filename)} bytes)")
except ImportError:
    print(f"Note: openpyxl is not installed. To enable Excel export, install with: pip install openpyxl")
    print(f"Syntax for Excel export: df.to_excel('{xlsx_filename}', index=False)")


print("\n==================================================================")
print("4. PANDAS DISPLAY SETTINGS & FORMATTING")
print("==================================================================")
# By default, Pandas truncates output when a DataFrame has many rows.
# pd.options.display.max_rows controls the maximum number of rows printed.

# Check current max_rows setting
current_max = pd.options.display.max_rows
print(f"Default pd.options.display.max_rows: {current_max}")

# Set max_rows to a high limit (e.g. 9999) to display entire datasets without truncation
pd.options.display.max_rows = 9999
print(f"Updated pd.options.display.max_rows to: {pd.options.display.max_rows}")

# df.to_string():
# Renders the full DataFrame as a plain formatted string without ellipsis truncation
print("\nRendering DataFrame using df.to_string():")
print(df.to_string())

# Restore default max_rows
pd.options.display.max_rows = current_max

