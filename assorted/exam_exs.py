import re
a = "A765-2781-ZFQ"
match = re.search(r'([AB])([0-9]+)-([0-9]+)-([A-Z0-9]+)',a)
print match.group() #A765-2781-ZFQ
print match.group(1) #A
print match.group(2) #765
print match.group(3) #2781
print match.group(4) #ZFQ

a = "crate"
b = "state"
match = re.search(r'(cr|st)ate',a)
#prints crate
match = re.search(r'(cr|st)ate',b)
#prints state
