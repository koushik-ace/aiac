G1:
This code reads values from a CSV file named input.csv and calculates the sum of the values in the column named 'value'. It also counts how many rows have invalid or missing data in that column.

How it works:

Imports the csv module.
Sets the filename to 'input.csv'.
Initializes total for the sum and invalid_count for invalid rows.
Opens the CSV file and reads it as a dictionary.
For each row, it tries to add the integer value from the 'value' column to total.
If the value is missing or not a valid integer, it increases invalid_count.
Finally, it prints the total sum and the number of invalid rows.


G2:
This code demonstrates how to perform INNER JOIN and LEFT JOIN operations on two sets of sample CSV data using Python.

How it works:

Two sample CSV datasets (csv1 and csv2) are defined as lists of lists.
csv1 contains id and price.
csv2 contains id and qty.
The parse_csv function converts each CSV dataset into a dictionary keyed by id, with the remaining columns as values.
data1 and data2 store the parsed dictionaries.
INNER JOIN: For each id in data1, if the same id exists in data2, a tuple of (id, price, qty) is added to the inner list.
LEFT JOIN: For each id in data1, a tuple of (id, price, qty) is added to the left list. If qty is missing in data2, it is set to None.
The results of both joins are printed.
Output:

inner contains rows where id exists in both datasets.
left contains all rows from data1, with matching qty from data2 or None if not found.