import requests
import json
from sys import argv

# Define fields to be retrieved from Coursera API
fields = ["name", "id", "website"]
link = "https://api.coursera.org/api/catalog.v1/universities?fields="
link = link + ','.join(fields)

# Retrieve universities, convert to JSON, format
universities = requests.get(link)
universities = universities.json()
# universities = universities["elements"]

# Write to file
filename = "data/coursera/universities.json"
with open(filename, 'w') as outfile:
	json.dump(universities, outfile, indent=4)
