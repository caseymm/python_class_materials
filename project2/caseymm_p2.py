import codecs
from operator import itemgetter

fp = codecs.open("artists.dat", encoding="utf-8")
fp.readline() #skip first line of headers
artist_info = []
for line in fp:
    line = line.strip()
    #artist_info.append(line)
    fields = line.split();
    artist = fields[1]
    artist_id = fields[0]
    tmp = {}
    tmp['artist'] = artist
    tmp['artist_id'] = artist_id
    artist_info.append(tmp)
fp.close()

artist_info_sortable = {} #sortable artist info
for item in artist_info:
    a = item['artist']
    pk = item['artist_id']
    artist_info_sortable[(a,pk)] = artist_info_sortable.get(a,pk)

#print artist_info_sortable
sorted_artist_info = sorted(artist_info_sortable.iteritems(), key=itemgetter(1))
#print sorted_artist_info

#this isn't really sorted since it's going by first number in sequence, not the whole number
for ((artist, artist_id), artist_id) in sorted_artist_info:
    print artist, artist_id
