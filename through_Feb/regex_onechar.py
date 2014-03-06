import re
b = "March 19, 1995"
c = "on March 9, 1995"
match = re.search(r'19',c)
print match.group()
match = re.search(r'1?9',c)
print match.group()
match = re.search(r'^March',b)
print match.group()
match = re.search(r'^March',c)
if match:
    print match.group()
else:
    print "not found"