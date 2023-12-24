# open file name golfers_fixtures.json
import json

# Open the JSON file
with open('golfers_fixture.json', 'r') as file:
    data = json.load(file)  # Load the JSON data

# Modify values of the 'model' key
for item in data:
    if item['model'] == 'chamster_api.Chamster':
        item['model'] = 'chamsterapp.Chamster'  # Change value to 'chamsterapp'

# Write the updated data back to the file
with open('golfers_fixture_new.json', 'w') as file:
    json.dump(data, file, indent=4)  # Write the modified data back to the file with indentation for readability

