import json
fp = open("ex1.json", "r")
s = fp.read()
j = json.loads(s)
print j
print

print "first = ", j['firstName']
print "last = ", j['lastName']
print "age = ", j['age']
print "city = ", j['address']['city']
for phnum in j['phoneNumbers']:
    print phnum['type'], " = ", phnum['number']