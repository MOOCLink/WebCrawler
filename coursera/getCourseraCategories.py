import requests
import json
from sys import argv

# Define fields to be retrieved from Coursera API
fields = ["name", "shortName", "id", "description"]
link = "https://api.coursera.org/api/catalog.v1/categories?fields="
link = link + ','.join(fields)

# Retrieve categories, convert to JSON, format
categories = requests.get(link)
categories = categories.json()
# categories = categories["elements"]

# Write to file
filename = "data/coursera/categories.json"
with open(filename, 'w') as outfile:
	json.dump(categories, outfile, indent=4)
