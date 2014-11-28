import requests
import json
from sys import argv

# Define fields to be retrieved from Coursera API
fields = ["homeLink",
		  "durationString",
		  "courseId",
		  "status",
		  "active",
		  "startDay",
		  "startMonth",
		  "startYear",
		  "name",
		  "eligibleForCertificates",
		  "eligibleForSignatureTrack"]
link = "https://api.coursera.org/api/catalog.v1/sessions?fields="
link = link + ','.join(fields)

# Retrieve sessions, convert to JSON, format
sessions = requests.get(link)
sessions = sessions.json()
# sessions = sessions["elements"]

# Write to file
filename = "data/coursera/sessions.json"
with open(filename, 'w') as outfile:
	json.dump(sessions, outfile, indent=4)
