import requests
import json
from sys import argv

# Define fields to be retrieved from Coursera API
fields = ["fullName", "id"]
link = "https://api.coursera.org/api/catalog.v1/instructors?fields="
link = link + ','.join(fields)
link = link + "&includes=universities"

# Retrieve categories, convert to JSON, format
instructors = requests.get(link)
instructors = instructors.json()
# categories = categories["elements"]

# Write to file
filename = "data/coursera/instructors.json"
with open(filename, 'w') as outfile:
	json.dump(instructors, outfile, indent=4)
