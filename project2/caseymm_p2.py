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
    artist_id = int(fields[0])
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
    #artist_info_sortable[(a)] = artist_info_sortable.get(a,pk)
print artist_info
#sorted_artist_info = sorted(artist_info_sortable.iteritems(), key=itemgetter(1))

#this isn't really sorted since it's going by first number in sequence, not the whole number
#for ((artist, artist_id), artist_id) in sorted_artist_info:
    #print artist, artist_id

fp2 = codecs.open("user_taggedartists.dat", encoding="utf-8")
fp2.readline() #skip first line of headers
tag_info = []
for line in fp2:
    line = line.strip()
    fields = line.split();
    userID = int(fields[0])
    artistID = int(fields[1])
    tagID = int(fields[2])
    day = int(fields[3])
    month = fields[4]
    year = int(fields[5])
    tmp = {}
    tmp['userID'] = userID
    tmp['artistID'] = artistID
    tmp['tagID'] = tagID
    tmp['day'] = day
    tmp['month'] = month
    tmp['year'] = year
    
    #don't know if artist id is working
    for artistID in artist_info[1]:
        #year filtering is workin
        if year >= 2000:
            tag_info.append(tmp)
fp2.close()

#print tag_info

fp3 = codecs.open("user_artists.dat", encoding="utf-8")
fp3.readline() #skip first line of headers
play_info = []
for line in fp3:
    line = line.strip()
    fields = line.split();
    userID = int(fields[0])
    artistID = int(fields[1])
    weight = int(fields[2])
    tmp = {}
    tmp['userID'] = userID
    tmp['artistID'] = artistID
    tmp['weight'] = weight
    play_info.append(tmp)
fp3.close()
#need to create a new dictionary that gets the artist number and addes the playcount of that artist for each user to output total
#print play_info

artist_plays_w_name = dict()

for item in artist_info:
    artist_plays_w_name.setdefault(artist_info[1],{}).setdefault(artist_info[0],[]).append(linenum)

