import codecs
from operator import itemgetter

fp = codecs.open("artists.dat", encoding="utf-8")
fp.readline() #skip first line of headers
artist_info = []
artist_info_dict = {}
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
    artist_info_dict.setdefault(artist_id,[]).append(artist)
fp.close()

#print artist_info_dict
#for keys in artist_info_dict:
    #print keys


artist_info_sortable = {} #sortable artist info
for item in artist_info:
    a = item['artist']
    pk = item['artist_id']
    artist_info_sortable[(a,pk)] = artist_info_sortable.get(a,pk)
    #artist_info_sortable[(a)] = artist_info_sortable.get(a,pk)
    
#print artist_info
sorted_artist_info = sorted(artist_info_sortable.iteritems(), key=itemgetter(1))
#print sorted_artist_info


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
    month = int(fields[4])
    year = int(fields[5])
    tmp = {}
    tmp['userID'] = userID
    tmp['artistID'] = artistID
    tmp['tagID'] = tagID
    tmp['day'] = day
    tmp['month'] = month
    tmp['year'] = year
    if year >= 2000:
        tag_info.append(tmp)
fp2.close()

#print tag_info
#This JUST filters out artists that shouldn't be in the dict, not add the artist name
tag_info_final = []
for entry in tag_info:
    pk = entry['artistID']
    
    if pk in artist_info_dict:
        #this_artist = artist_info_dict.get(pk)
        tag_info_final.append(entry)

#Prints only tag info with correct years and with valid artist ids        
#print tag_info_final
            

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

#print play_info

#get the play count for each artist id - doesn't list artist
total_play_count = {}
for entry in play_info:
    pk = entry['artistID']
    weight = entry['weight']
    #total_play_count.setdefault(pk,[]).append(query_word)
    total_play_count[pk] = total_play_count.get(pk,0) + weight

print total_play_count
#artist_plays_w_name = dict()

#maybe use .get(number) from other dict and just match that to the artist
#for item in artist_info:
#    artist_plays_w_name.setdefault(artist_info[1],{}).setdefault(artist_info[0],[]).append(linenum)

#could do for each time that the artist appears in a tag save that playcount and append it to a list
#then add all of the list items together to get the total play count

