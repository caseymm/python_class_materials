import re
a = "199987659955"
match = re.search(r'9+',a)
print match.group()
match = re.search(r'19*',a)
print match.group()
match = re.search(r'9*',a)
print match.group()
match = re.search(r'9+.*9+',a)
print match.group()

print "NEW"

match = re.search(r'pi+', 'piiig')
print match.group()
match = re.search(r'i+', 'piigiiii')
print match.group()
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
print match.group()
match = re.search(r'\d\s*\d\s*\d', 'xx12 3xx')
print match.group()
match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
print match.group()