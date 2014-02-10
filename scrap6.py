import string 
fp = open("courses2.txt", "r")
hist = dict()

for line in fp:
    line = line.strip()
    row = line.split()
    courses = row[0]
    instructors = row[1] 

    if courses in hist:
        hist[courses].append(instructors)
    else:
        hist[courses] = [instructors]

print hist

