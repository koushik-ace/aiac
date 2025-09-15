import csv

filename = 'input.csv'  # Change this to your CSV file path

total = 0
invalid_count = 0

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            total += int(row['value'])
        except (ValueError, KeyError):
            invalid_count += 1

print(total)
print("Invalid rows:", invalid_count)