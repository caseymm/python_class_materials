import json
import re
from operator import itemgetter

#parse json data into list of dicts

fp = open('usagov_ex1.txt')
records = [json.loads(line) for line in fp]
fp.close()

urls = []
for rec in records:
    if 'u' in rec:
        urls.append(rec['u'])
#print urls

url_counts = {}
for url in urls:
    match = re.search(r'://([^/]*)',url)
    #need to strip ://
    if match:
        new_url = match.group(1)
        url_counts [new_url] = url_counts.get(new_url, 0) + 1
#print url_counts

sorted_url_counts = sorted(url_counts.items(), key=itemgetter(1), reverse=True)
#print sorted_url_counts[:10]
for url, count in sorted_url_counts[:10]:
    print url, count
