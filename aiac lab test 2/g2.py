import csv

# Sample CSV data as lists (replace with file reading if needed)
csv1 = [
    ['id', 'price'],
    ['A', '10'],
    ['B', '20']
]
csv2 = [
    ['id', 'qty'],
    ['A', '2'],
    ['C', '5']
]

# Parse CSVs into dicts keyed by id
def parse_csv(data):
    header = data[0]
    return {row[0]: row[1:] for row in data[1:]}

data1 = parse_csv(csv1)
data2 = parse_csv(csv2)

# INNER JOIN
inner = []
for id1 in data1:
    if id1 in data2:
        inner.append((id1, int(data1[id1][0]), int(data2[id1][0])))

# LEFT JOIN
left = []
for id1 in data1:
    qty = int(data2[id1][0]) if id1 in data2 else None
    left.append((id1, int(data1[id1][0]), qty))

print("inner=", inner)
print("left=", left)