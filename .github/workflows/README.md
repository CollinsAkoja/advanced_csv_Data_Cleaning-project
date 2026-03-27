Student CSV Cleaner

A simple Python script for parsing, validating, and cleaning student data from a CSV file.

Description

This project reads a CSV file containing student records, validates each row, and outputs a cleaned version of the data. Invalid rows are optionally saved in a separate file for review.

Features
Reads CSV data using csv.DictReader
Validates required fields
Supports multiple name formats
Cleans and standardizes data
Outputs clean and invalid datasets
Supported Input Formats
Format 1
name,score,department
Chinedu,Okafor,85,Computer Science
Format 2
first_name,last_name,score,department
Chinedu,Okafor,85,Computer Science
Validation Rules
department must not be empty
score must:
exist
be numeric
be between 0 and 100
A valid name must exist:
either name
or first_name (with optional last_name)
Usage
1. Prepare your input file

Place your CSV file in the project folder and name it:

students.csv
2. Run the script
python script.py
3. Output

After running, the script generates:

cleaned_students.csv — valid and cleaned records
invalid_rows.csv — invalid records (if any)
Example Output
Cleaned Data
first_name,last_name,score,department
John,Doe,85.0,Engineering
Invalid Data
name,score,department,reason
Jane Doe,,HR,missing/invalid field or score out of range
Common Issues
Empty cleaned file
Check that column names match exactly (name, score, department)
Ensure no required fields are missing
Ensure scores are valid numbers
Header mismatch
CSV headers are case-sensitive
Project Structure
.
├── students.csv
├── cleaned_students.csv
├── invalid_rows.csv
├── main.py
└── README.md
Technologies Used
Python 3
Built-in csv module
Author

Collins Akoja Nathaniels

License

This project is open for learning and personal use.