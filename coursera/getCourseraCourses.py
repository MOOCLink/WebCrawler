import requests
import json
from sys import argv

# Define fields to be retrieved from Coursera API
fields = ["language",
		  "shortDescription",
		  "video",
		  "aboutTheCourse",
		  "estimatedClassWorkload",
		  "subtitleLanguagesCsv",
		  "courseSyllabus",
		  "courseFormat",
		  "instructor",
		  "faq",
		  "aboutTheInstructor",
		  "recommendedBackground"]
link = "https://api.coursera.org/api/catalog.v1/courses?fields="
link = link + ','.join(fields)
link = link + "&includes=categories,instructors";

# Retrieve courses, convert to JSON, format
courses = requests.get(link)
courses = courses.json()
# courses = courses["elements"]

# Write to file
filename = "data/coursera/courses.json"
with open(filename, 'w') as outfile:
	json.dump(courses, outfile, indent=4)
