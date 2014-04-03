import codecs
from operator import itemgetter
from time import strftime
from datetime import datetime

fp = codecs.open("artists.dat", encoding="utf-8")
fp.readline() #skip first line of headers
artist_info = []
artist_info_dict = {}
for line in fp:
    line = line.strip()
    fields = line.split("\t")
    artist = fields[1]
    artist_id = int(fields[0])
    tmp = {}
    tmp['artist'] = artist
    tmp['artist_id'] = artist_id
    artist_info.append(tmp)
    artist_info_dict.setdefault(artist_id,[]).append(artist)
fp.close()

#print artist_info
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
total_user_play_count = {}
artist_to_users = {}
users_to_artist = {}
for entry in play_info:
    pk = entry['artistID']
    user_pk = entry['userID']
    weight = entry['weight']
    #total_play_count.setdefault(pk,[]).append(query_word)
    total_play_count[pk] = total_play_count.get(pk,0) + weight
    total_user_play_count[user_pk] = total_user_play_count.get(user_pk,0) + weight
    artist_to_users[pk] = artist_to_users.get(pk,0) + 1
    
    #this is for question 7, creates dict w/ key or artist_id and value of user_id
    users_to_artist.setdefault(pk, []).append(user_pk)

#print total_play_count

artist_name_id_count = {}
for (entry, count) in total_play_count.items():
    #print entry, count
    if entry in artist_info_dict:
        this_artist = artist_info_dict.get(entry)
        for i in this_artist:
            #artist_name_id_count.setdefault(i,{}).setdefault(entry, []).append(count)
            artist_name_id_count.setdefault(count,{}).setdefault(i, entry)

artist_name_to_users = {}
for (entry, user_count) in artist_to_users.items():
    #print entry, count
    if entry in artist_info_dict:
        this_artist = artist_info_dict.get(entry)
        for i in this_artist:
            #i is artist name, entry is artist id
            artist_name_to_users.setdefault(user_count,{}).setdefault(i, entry)
            
average_plays = {}
average_plays_b = {}
average_plays_50 = {}
for entry in artist_to_users:
    #print entry, artist_to_users[entry]
    user_count = artist_to_users[entry]
    if entry in total_play_count:
        count = total_play_count[entry]
        if entry in artist_info_dict:
            this_artist = artist_info_dict.get(entry)
            for i in this_artist:
                #i is artist name, entry is artist id
                tmp = {}
                tmp['avg_count'] = count/user_count
                tmp['user_count'] = user_count
                tmp['playcount'] = count
                tmp['artist'] = i
                tmp['artist_id'] = entry
                average_plays_b.setdefault((count/user_count),[]).append(tmp)
                average_plays.setdefault((count/user_count),{}).setdefault(i, entry)
                if user_count > 49:
                    average_plays_50.setdefault((count/user_count),[]).append(tmp)
        
sorted_artist_name_id_count = sorted(artist_name_id_count.items(), key=itemgetter(0), reverse=True)
sorted_total_user_play_count = sorted(total_user_play_count.items(), key=itemgetter(1), reverse=True)
sorted_artist_name_to_users = sorted(artist_name_to_users.items(), key=itemgetter(0), reverse=True)
sorted_average_plays = sorted(average_plays.items(), key=itemgetter(0), reverse=True)
sorted_average_plays_b = sorted(average_plays_b.items(), key=itemgetter(0), reverse=True)
sorted_average_plays_50 = sorted(average_plays_50.items(), key=itemgetter(0), reverse=True)

#This starts number 6
fp4 = codecs.open("user_friends.dat", encoding="utf-8")
fp4.readline() #skip first line of headers
friend_info = []
for line in fp4:
    line = line.strip()
    fields = line.split();
    userID = int(fields[0])
    friendID = int(fields[1])
    tmp = {}
    tmp['userID'] = userID
    tmp['friendID'] = friendID
    friend_info.append(tmp)
fp4.close()

total_friend_count = {}
for entry in friend_info:
    userID = entry['userID']
    friendID = entry['friendID']
    total_friend_count[userID] = total_friend_count.get(userID,0) + 1

five_or_more = {}
less_than_five = {}
for entry in total_friend_count:
    count = total_friend_count.get(entry)
    if count >= 5:
        five_or_more.setdefault(entry, count)
    elif count < 5:
        less_than_five.setdefault(entry, count)

total_plays_five_or_more = {}
for user_pk, weight in sorted_total_user_play_count:
    if user_pk in five_or_more:
        total_plays_five_or_more[user_pk] = total_plays_five_or_more.get(user_pk,0) + weight

total_plays_less_than_five = {}
for user_pk, weight in sorted_total_user_play_count:
    if user_pk in less_than_five:
        total_plays_less_than_five[user_pk] = total_plays_less_than_five.get(user_pk,0) + weight

#start question 7
def artist_sim(aid1, aid2):
    shared_users = []
    aid1_only = []
    aid2_only = []
    value_aid1 = users_to_artist.get(aid1)
    value_aid2 = users_to_artist.get(aid2)
    artist1 = ''
    artist1_list = artist_info_dict.get(aid1)
    for artist in artist1_list:
        artist1 = artist
    
    artist2 = ''
    artist2_list = artist_info_dict.get(aid2)
    for artist in artist2_list:
        artist2 = artist
    
    for user in value_aid1:
        if user in value_aid2:
            shared_users.append(user)
        else:
            aid1_only.append(user)
    for user in value_aid2:
        if user not in value_aid1:
            aid2_only.append(user)
    
    shared_users_length = len(shared_users)
    aid1_only_length = len(aid1_only)
    aid2_only_length = len(aid2_only)
            
    total = shared_users_length + aid1_only_length + aid2_only_length
    index = float(shared_users_length)/float(total)
    print artist1+', '+ artist2+'   '+ str(index)

#started question 8
popular_alltime = {}
popular_aug = {}
popular_sept = {}
popular_octob = {}
popular_nov = {}
popular_dec = {}

tag_info_final_sortable = {} #sortable artist info
for tag_item in tag_info_final:
    year = tag_item['year']
    month = tag_item['month']
    day = tag_item['day']
    userID = tag_item['userID']
    artistID = tag_item['artistID']
    tagID = tag_item['tagID']
    tmp = {}
    tmp['userID'] = userID
    tmp['artistID'] = artistID
    tmp['tagID'] = tagID
    tmp['day'] = day
    tmp['month'] = month
    tmp['year'] = year
    
    tag_info_final_sortable.setdefault((year, month), []).append(tmp)
    
    #tag_info_final[(month, year)] = tag_info_final_sortable.get(artistID, userID, month, day, year)
    #sorted_tag_info_final_year = sorted(tag_item.item(5), key=itemgetter(1))
    #print sorted_tag_info_final_year
    popular_alltime[artistID] = popular_alltime.get(artistID,0) + 1
    
    if year == 2005:
        if month == 8:
            popular_aug[artistID] = popular_aug.get(artistID,0) + 1
        elif month == 9:
            popular_sept[artistID] = popular_sept.get(artistID,0) + 1
        elif month == 10:
            popular_octob[artistID] = popular_octob.get(artistID,0) + 1
        elif month == 11:
            popular_nov[artistID] = popular_nov.get(artistID,0) + 1
        elif month == 12:
            popular_dec[artistID] = popular_dec.get(artistID,0) + 1
            

#sorted_tag_info_final_month = sorted(sorted_tag_info_final_year.items(), key=itemgetter(2))
sorted_popular_alltime = sorted(popular_alltime.items(), key=itemgetter(1), reverse=True)
the_top_ten = sorted_popular_alltime[:10]

sorted_tag_info_final_sortable = sorted(tag_info_final_sortable.items(), key=itemgetter(0))

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "1. Who are the top artists?"
print
for (count, artist) in sorted_artist_name_id_count[:10]:
    for (artist_name, artist_id) in artist.items():
        print '' + artist_name + ' ('+ str(artist_id) +') ' + str(count) + ''

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "2. Who are the top users?"
print
for user_pk, weight in sorted_total_user_play_count[:10]:
    #print user_pk, weight
    print 'user: ' + str(user_pk) + ', playcount: ' + str(weight) + ''

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "3. Which artists have the most listeners?"
print
for (user_count, artist) in sorted_artist_name_to_users[:10]:
    for (artist_name, artist_id) in artist.items():
        print '' + artist_name + ' ('+ str(artist_id) +'): ' + str(user_count) + ''

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "4. Which artists have the highest average number of plays per listener?"
print
#for (avg_per, artist) in sorted_average_plays[:10]:
#    for (artist_name, artist_id) in artist.items():
#        print '' + artist_name + ' ('+ str(artist_id) +') ' + str(avg_per) + ''

for i, info_list in sorted_average_plays_b[:10]:
    for info_item in info_list:
        #print info_item
        avg_count = info_item['avg_count']
        user_count = info_item['user_count']
        playcount = info_item['playcount']
        artist = info_item['artist']
        artist_id = info_item['artist_id']
        print 'Artist: '+ artist + ' ('+ str(artist_id) +'), Total plays: '+ str(playcount) +', Listeners: '+ str(user_count) +', Average plays: '+ str(avg_count) 

#print sorted_average_plays_50[:10]

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "5. Which artists with at least 50 listeners have the highest average number of plays per listener?"
print

for i, info_list in sorted_average_plays_50[:10]:
    for info_item in info_list:
        avg_count = info_item['avg_count']
        user_count = info_item['user_count']
        playcount = info_item['playcount']
        artist = info_item['artist']
        artist_id = info_item['artist_id']
        print 'Artist: '+ artist + ' ('+ str(artist_id) +'), Total plays: '+ str(playcount) +', Listeners: '+ str(user_count) +', Average plays: '+ str(avg_count)

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "6. Do users with five or more friends listen to more songs?"
print
five_or_more_length = len(five_or_more)
less_than_five_length = len(less_than_five)
sum_total_plays_five_or_more = sum(total_plays_five_or_more.values())
sum_total_plays_less_than_five = sum(total_plays_less_than_five.values())
five_or_more_avg = sum_total_plays_five_or_more/five_or_more_length
less_than_five_avg = sum_total_plays_less_than_five/less_than_five_length

print 'Five or more friends:'
print 'Average plays: '+ str(five_or_more_avg) +', Total plays: '+ str(sum_total_plays_five_or_more) +', Users: '+ str(five_or_more_length)
print
print 'Less than five friends:'
print 'Average plays: '+ str(less_than_five_avg) +', Total plays: '+ str(sum_total_plays_less_than_five) +', Users: '+ str(less_than_five_length) 

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "7. How similar are two artists?"

artist_sim(735,562)
artist_sim(735,89)
artist_sim(735,289)
artist_sim(89,289)
artist_sim(89,67)
artist_sim(67,735)

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "8. For each month in 2005, what artists were tagged the most?"
print
print "August 2005"

sorted_popular_aug = sorted(popular_aug.items(), key=itemgetter(1), reverse=True)
for artistID, count in sorted_popular_aug[:10]:
    artist_name_list = artist_info_dict.get(artistID)
    for artist_name in artist_name_list:
        print '  '+ artist_name + ' (' + str(artistID) + '):  num tags = ' + str(count)

print
print "September 2005"

sorted_popular_sept = sorted(popular_sept.items(), key=itemgetter(1), reverse=True)
for artistID, count in sorted_popular_sept[:10]:
    artist_name_list = artist_info_dict.get(artistID)
    for artist_name in artist_name_list:
        print '  '+ artist_name + ' (' + str(artistID) + '):  num tags = ' + str(count)

print
print "October 2005"

sorted_popular_octob = sorted(popular_octob.items(), key=itemgetter(1), reverse=True)
for artistID, count in sorted_popular_octob[:10]:
    artist_name_list = artist_info_dict.get(artistID)
    for artist_name in artist_name_list:
        print '  '+ artist_name + ' (' + str(artistID) + '):  num tags = ' + str(count)

print
print "November 2005"

sorted_popular_nov = sorted(popular_nov.items(), key=itemgetter(1), reverse=True)
for artistID, count in sorted_popular_nov[:10]:
    artist_name_list = artist_info_dict.get(artistID)
    for artist_name in artist_name_list:
        print '  '+ artist_name + ' (' + str(artistID) + '):  num tags = ' + str(count)

print
print "December 2005"

sorted_popular_dec = sorted(popular_dec.items(), key=itemgetter(1), reverse=True)
for artistID, count in sorted_popular_dec[:10]:
    artist_name_list = artist_info_dict.get(artistID)
    for artist_name in artist_name_list:
        print '  '+ artist_name + ' (' + str(artistID) + '):  num tags = ' + str(count)

print

artistID_counts = {}
for (date, info) in sorted_tag_info_final_sortable:
    tags_in_month = {}
    #stim_10 = ""
    for info_item in info:
        artistID = info_item['artistID']
        
        #if artistID in the_top_ten:
        tags_in_month[artistID] = tags_in_month.get(artistID,0) + 1
    sorted_tags_in_month = sorted(tags_in_month.items(), key=itemgetter(1), reverse=True)
    stim_10 = sorted_tags_in_month[:10]
    artistID_counts.setdefault(date, []).append(stim_10)
    sorted_artistID_counts = sorted(artistID_counts.items(), key=itemgetter(0))

artist_months = {}
for (date,top_artists) in sorted_artistID_counts:
    for inner_list in top_artists:
        for (artistID, tags) in inner_list:
            #print artistID
            artist_months.setdefault(artistID, []).append(date)

#print artist_months

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "9. Artists with the highest number of overall tags, the first month they entered the top 10, and the number of times they appeared in the top ten."
print

for artistID, count in the_top_ten:
    date_list = []
    
    artist_name_list = artist_info_dict.get(artistID)
    for artist_name in artist_name_list:
        print artist_name + ' (' + str(artistID) + '):  num tags = ' + str(count)
        artist_months_list = artist_months.get(artistID)
        for (year, month) in artist_months_list:
            formated_month = datetime(year, int(month), 1)
            selected_month = formated_month.strftime("%b")
            date_str = selected_month +' '+str(year)
            date_list.append(date_str)
        #print date_list[0]
        print "  first month in top10 = " + date_list[0]
 
        months_in_top_10 = len(artist_months_list)
        print "  months in top10 = " + str(months_in_top_10)
        print
    
###MAKE SURE to specify method like Capra said in email