import json
fp = open("ex2.json", "r")
s = fp.read()
j = json.loads(s)
print j
print
print "Report date = ", j['reportDate']
if j['reportType'] == 'emprec':
    for emp in j['empData']:
        print
        print "first = ", emp['firstName']
        print "last = ", emp['lastName']
        print "age = ", emp['age']
        print "city = ", emp['address']['city']
        for phnum in emp['phoneNumbers']:
            print phnum['type'], " = ", phnum['number']