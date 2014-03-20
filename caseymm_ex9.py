import codecs
from operator import itemgetter

fp = codecs.open("ex9_courses.txt", encoding="utf-8")
fp.readline()
cis_list = []
for line in fp:
    line = line.strip()
    fields = line.split();
    course = fields[0]
    instructor = fields[1]
    semester = fields[2]
    tmp = {}
    tmp['course'] = course
    tmp['instructor'] = instructor
    tmp['semester'] = semester
    cis_list.append(tmp)
fp.close()
#print cis_list

c_counts = {} #course counts
for d in cis_list:
    c = d['course']
    c_counts[c] = c_counts.get(c,0) + 1
    
ci_counts = {} #course instructor counts
for d in cis_list:
    c = d['course']
    i = d['instructor']
    ci_counts[(c,i)] = ci_counts.get((c,i),0) + 1

#items gives you both things in the dictionary in tuple form
sorted_c_counts = sorted(c_counts.items(), key=itemgetter(1), reverse=True)

#iteritems will return an object, bu tis much faster
sorted_ci_counts = sorted(ci_counts.iteritems(), key=itemgetter(1), reverse=True)

for (course,count) in sorted_c_counts:
    print course, count
for ((course,instructor), count) in sorted_ci_counts:
    print course, instructor, count
print
print '##################'
print
    
print c_counts
print
print ci_counts
print
print sorted_c_counts
print
print sorted_ci_counts