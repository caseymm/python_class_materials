import re

faculty = open("faculty.html","r")

emails = re.findall(r'[\w\.-]+@[\w\.-]+', faculty.read()) 
for email in emails:
    print email