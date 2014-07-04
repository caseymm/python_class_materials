import json
from operator import itemgetter
from collections import Counter

#parse json data into list of dicts

fp = open('usagov_ex1.txt')
records = []
for line in fp:
    records.append(json.loads(line))
fp.close()

print
print "short version"
print

fp = open('usagov_ex1.txt')
records = [json.loads(line) for line in fp]
fp.close()

tzs = []
for rec in records:
    #need to check if timezone in dictionary
    if 'tz' in rec:
        tzs.append(rec['tz'])
#print records[0]
#print tzs
#print len(tzs)

#3 equivalent methods

tz_counts = {}
for tz in tzs:
    if tz in tz_counts:
        tz_counts[tz] += 1
    else:
        tz_counts[tz] = 1
#print tz_counts['America/New_York']

tz_counts2 = {}
for tz in tzs:
    tz_counts2[tz] = tz_counts2.get(tz,0) + 1
#print tz_counts2['America/New_York']

#default dict is part of collection
#when you put things in taht aren't there, it automatically initializes something
#straigt from docs on python website

from collections import defaultdict
tz_counts3 = defaultdict(int)
#will default create an integer that is zero if it's never seen this value/thing before
for tz in tzs:
    tz_counts3[tz] += 1
#print tz_counts3['America/New_York']

#.items returns a list of tuples
sorted_tzc = sorted(tz_counts.items(), key=itemgetter(1), reverse=True)
for tz, c in sorted_tzc[:10]:
    print tz, c
    
print

tzs2 = [rec['tz'] for rec in records if 'tz' in rec]
cc = Counter(tzs2)
print cc
print cc.most_common(10)
