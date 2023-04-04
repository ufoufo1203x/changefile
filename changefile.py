import csv
import json

# Open the CSV file for reading
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Convert the CSV data to a list of dictionaries
    data = [row for row in csv_reader]

# Open the JSON file for writing
with open('data.json', 'w') as json_file:
    # Write the data to the JSON file
    json.dump(data, json_file)
