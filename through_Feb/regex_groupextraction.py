import re
a = "A765-2781-ZFQ"
match = re.search(r'([AB])([0-9]+)-([0-9]+)-([A-Z0-9]+)',a)
print match.group()
print match.group(1)
print match.group(2)
print match.group(3)
print match.group(4)
print
print "NEW"
print
a = "crate"
b = "state"
match = re.search(r'(cr|st)ate',a)
print match.group()
match = re.search(r'(cr|st)ate',b)
print match.group()