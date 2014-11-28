import coursera_requests as c
import sys

try:
	c.getCourseraCategories()
	c.getCourseraCourses()
	c.getCourseraInstructors()
	c.getCourseraSessions()
	c.getCourseraUniversities()
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise