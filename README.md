





# 🧹 CSV Cleaner Tool

A Python tool to inspect and clean messy CSV files — check for missing values, remove duplicate rows, and fill or drop missing data, with results saved back to a new CSV.

## Features

- 📂 Load any CSV file by name (type `close` anytime at the file prompt to exit)
- 🔍 Check missing values — see exactly how many are missing per column
- 🔁 Remove duplicate rows, with an option to save the cleaned file
- 🧹 Clean the data three ways:
  - Fill missing values with `0`
  - Delete rows that have any missing values
  - Fill missing values with the column average (numeric columns only)
- 💾 Save cleaned data under a new filename — the original file is never overwritten unless you save with the same name
- ⚠️ Leaving the save filename blank simply skips saving, instead of crashing
- ❌ Handles missing files, invalid menu options, and read errors gracefully

## Requirements

- Python 3.x
- pandas (`pip install pandas`)

## How to Run

```bash
python csv_cleaner.py
```

## How to Use

1. Run the program.
2. Enter the name of the CSV file you want to clean (it must be in the same folder, or give the full path). Type `close` instead to exit without opening a file.
3. Once loaded, the file's contents are shown, and you can choose from the menu:
   - **1** — Check missing values per column
   - **2** — Remove duplicate rows (you'll be asked for a filename to save the result)
   - **3** — Clean the data (fill with 0s, drop rows, or fill with the average), then save
   - **4** — Close this file and return to the file prompt
4. If you leave the "Save file name" prompt blank, your changes stay in memory for that session but aren't written to disk.
5. Type `close` at the file prompt anytime to exit the program.

## Technologies Used

- Python
- Pandas

## Author

**Charan Aade | Python Developer**
