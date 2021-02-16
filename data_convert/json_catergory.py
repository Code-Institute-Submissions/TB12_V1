import csv
import json
from decimal import Decimal

# Open the CSV file for reading, and a new JSON file for writing
csvfile = open('data_convert/category.csv', 'r')
jsonfile = open('categories.json', 'w')

# Google the CSV module to see how this is going to iterate through the CSV row by row
reader = csv.reader(csvfile)
headers = next(reader)
rows = []
for row in reader:
    # Create a dict that will have an integer PK (in order)
    # And the model you want to create the fixture for
	row_dict = {
		'pk': int(row[0]), # This is the first column of the CSV
		'model': 'products.category',
	}
    # This empty dict will be for all the model's fields
	field_dict = {}
    # Each column header in the CSV file should map to a model field
	for header in headers[1:]: # Start at column 2 (index 1) to eliminate the PK column from being included here...we already included it above
		if header in ['price', 'rating']: # If the field is price/rating, make it a float
			field_dict[header] = float(row[headers.index(header)])
		elif header == 'category': # Category is an int (the PK of the category)
			field_dict[header] = int(row[headers.index(header)])
		else:
			field_dict[header] = row[headers.index(header)] # Otherwise just take the cell value
	# Now take the field_dict and put it in a key called 'fields' for this row
	row_dict['fields'] = field_dict 
    # And append the row
	rows.append(row_dict)
# Dump all rows to JSON
j = json.dumps(rows)
# Write and close the JSON file
jsonfile.write(j)
jsonfile.close()