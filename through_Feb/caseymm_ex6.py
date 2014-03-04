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

course_numbers = list(hist.keys())
print course_numbers

print hist.get('523')

course_list = []
for key in hist:
    if 'Capra' in hist[key]:
        course_list.append(key)
print course_list

instructor_names = list(hist.values())
instructor_list = []
 
for i in instructor_names:
    for name in i:
        if name not in instructor_list:
            instructor_list.append(name)

print instructor_list
    
