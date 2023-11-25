import csv

# read csv hw/sw files and store in variables
# hardware
hw_header = []
hw_items = []

with open('hw_spec.csv', 'r') as hw_spec_file:
    hw_csvreader = csv.reader(hw_spec_file)
    hw_header = next(hw_csvreader)

    for row in hw_csvreader:
        hw_items.append(row)

# software
sw_header = []
sw_items = []

with open('sw_spec.csv', 'r') as sw_spec_file:
    sw_csvreader = csv.reader(sw_spec_file)
    sw_header = next(sw_csvreader)

    for row in sw_csvreader:
        sw_items.append(row)

print("hardware")
print(hw_header)
print(hw_items)
print("")
print("software")
print(sw_header)
print(sw_items)

# generate 3point for hardware
# generate 3point for software
# generate 3point for testing

# generate 3point for total
