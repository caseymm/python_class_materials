import json
import urllib2

url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=large&q=cats"
fp = urllib2.urlopen(url)
html = fp.read()
myjson = json.loads(html)
print myjson
for result in myjson['responseData']['results']:
    print result
print
count = 0
for result in myjson['responseData']['results']:
    if result['GsearchResultClass'] == 'GwebSearch':
        count += 1
print count,
print "title = ", result['titleNoFormatting']
print " url = ", result['unescapedUrl']
print " snippet = ", result['content']
