import re

faculty = open("faculty.html","r")

emails = re.findall(r'[\w\.-]+@[\w\.-]+', faculty.read())
emails = list(set(emails))
print emails