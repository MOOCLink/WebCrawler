import requests
import json
from sys import argv

def getCourseraCategories():
	# Define fields to be retrieved from Coursera API
	fields = ["name", "shortName", "id", "description"]
	link = "https://api.coursera.org/api/catalog.v1/categories?fields="
	link = link + ','.join(fields)

	# Retrieve categories, convert to JSON, format
	categories = requests.get(link)
	categories = categories.json()
	# categories = categories["elements"]

	# Write to file
	filename = "../data/coursera/categories.json"
	with open(filename, 'w') as outfile:
		json.dump(categories, outfile, indent=4)

def getCourseraCourses():
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
	filename = "../data/coursera/courses.json"
	with open(filename, 'w') as outfile:
		json.dump(courses, outfile, indent=4)

def getCourseraInstructors():
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
	filename = "../data/coursera/instructors.json"
	with open(filename, 'w') as outfile:
		json.dump(instructors, outfile, indent=4)

def getCourseraSessions():
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
	filename = "../data/coursera/sessions.json"
	with open(filename, 'w') as outfile:
		json.dump(sessions, outfile, indent=4)

def getCourseraUniversities():
	# Define fields to be retrieved from Coursera API
	fields = ["name", "id", "website"]
	link = "https://api.coursera.org/api/catalog.v1/universities?fields="
	link = link + ','.join(fields)

	# Retrieve universities, convert to JSON, format
	universities = requests.get(link)
	universities = universities.json()
	# universities = universities["elements"]

	# Write to file
	filename = "../data/coursera/universities.json"
	with open(filename, 'w') as outfile:
		json.dump(universities, outfile, indent=4)