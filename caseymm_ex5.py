import re

faculty = open("faculty.html","r")

for aline in faculty:
    
    #values = aline.split()
    match = re.search(r'[\w.-]+@[\w.-]+', aline)

    if match:
        print match.group()
        #can only get ot print the first match on the page
        
    else:
        print "no match"

faculty.close()