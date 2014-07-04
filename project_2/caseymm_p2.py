import codecs
from operator import itemgetter
from time import strftime
from datetime import datetime

#creates dict with artist_id and name
fp = codecs.open("artists.dat", encoding="utf-8")
fp.readline() #skip first line of headers
artist_info_dict = {}
for line in fp:
    line = line.strip()
    fields = line.split("\t")
    artist = fields[1]
    artist_id = int(fields[0])
    tmp = {}
    tmp['artist'] = artist
    tmp['artist_id'] = artist_id
    artist_info_dict.setdefault(artist_id,[]).append(artist)
fp.close()

#info for questions 2 and 3
#creates dict containing info for each user tag
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

#This JUST filters out artists that shouldn't be in the dict, not add the artist name
tag_info_final = []
for entry in tag_info:
    artistID = entry['artistID']
    
    if artistID in artist_info_dict:
        tag_info_final.append(entry)

#tag_info_final prints only tag info with correct years and with valid artist ids

#creates dict containing user to artist playcount
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


total_play_count = {}
total_user_play_count = {}
artist_to_users = {}
users_to_artist = {}
for entry in play_info:
    artistID = entry['artistID']
    userID = entry['userID']
    weight = entry['weight']
    
    #get the play count for each artist id - doesn't list artist
    total_play_count[artistID] = total_play_count.get(artistID,0) + weight
    
    #get the play count for each user
    total_user_play_count[userID] = total_user_play_count.get(userID,0) + weight
    
    #get number of users who listen to an artist
    artist_to_users[artistID] = artist_to_users.get(artistID,0) + 1
    
    #this is for question 7, creates dict w/ key or artist_id and value of user_id
    #get all artists who a user listens to
    users_to_artist.setdefault(artistID, []).append(userID)

#set total playcount as key and append artists and ids with that number of plays
artist_name_id_count = {}
for (entry, count) in total_play_count.items():
    if entry in artist_info_dict:
        this_artist = artist_info_dict.get(entry)
        for i in this_artist:
            artist_name_id_count.setdefault(count,{}).setdefault(i, entry)

#get all users who listen to an artist
artist_name_to_users = {}
for (entry, user_count) in artist_to_users.items():
    if entry in artist_info_dict:
        this_artist = artist_info_dict.get(entry)
        for i in this_artist:
            artist_name_to_users.setdefault(user_count,{}).setdefault(i, entry)

#starts questions 4 and 5
average_plays = {}
average_plays_50 = {}
for entry in artist_to_users:
    user_count = artist_to_users[entry]
    if entry in total_play_count:
        count = total_play_count[entry]
        if entry in artist_info_dict:
            this_artist = artist_info_dict.get(entry)
            for i in this_artist:
                tmp = {}
                tmp['avg_count'] = count/user_count
                tmp['user_count'] = user_count
                tmp['playcount'] = count
                tmp['artist'] = i
                tmp['artist_id'] = entry
                
                #gets the average plays and sets as default, appends other play info
                average_plays.setdefault((count/user_count),[]).append(tmp)
                
                #gets the average plays 50+ and sets as default, appends other play info
                if user_count > 49:
                    average_plays_50.setdefault((count/user_count),[]).append(tmp)

#sorts all of the dictionaries created above        
sorted_artist_name_id_count = sorted(artist_name_id_count.items(), key=itemgetter(0), reverse=True)
sorted_total_user_play_count = sorted(total_user_play_count.items(), key=itemgetter(1), reverse=True)
sorted_artist_name_to_users = sorted(artist_name_to_users.items(), key=itemgetter(0), reverse=True)
sorted_average_plays = sorted(average_plays.items(), key=itemgetter(0), reverse=True)
sorted_average_plays_50 = sorted(average_plays_50.items(), key=itemgetter(0), reverse=True)

#start question 6
fp4 = codecs.open("user_friends.dat", encoding="utf-8")
fp4.readline() #skip first line of headers
#creates dict with users and friends
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

#creates dict w/ userIDs paired to number of friends they have
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
        #creates dicts w/userIDs paired to friends if have 5+ friends
        five_or_more.setdefault(entry, count)
    elif count < 5:
        #creates dicts w/userIDs paired to friends if have <5 friends
        less_than_five.setdefault(entry, count)

total_plays_five_or_more = {}
for userID, weight in sorted_total_user_play_count:
    if userID in five_or_more:
        #takes the users with 5+ friends and adds of of their plays together
        total_plays_five_or_more[userID] = total_plays_five_or_more.get(userID,0) + weight

total_plays_less_than_five = {}
for userID, weight in sorted_total_user_play_count:
    if userID in less_than_five:
        #takes the users with <5 friends and adds of of their plays together
        total_plays_less_than_five[userID] = total_plays_less_than_five.get(userID,0) + weight

#start question 7
def artist_sim(aid1, aid2):
    shared_users = []
    aid1_only = []
    aid2_only = []
    
    #get all users who are attached to that artistID in the users_to_artist dict
    value_aid1 = users_to_artist.get(aid1)
    value_aid2 = users_to_artist.get(aid2)
    
    #get the names of the artists that correspond to artistIDs
    artist1 = ''
    artist1_list = artist_info_dict.get(aid1)
    for artist in artist1_list:
        artist1 = artist
    
    artist2 = ''
    artist2_list = artist_info_dict.get(aid2)
    for artist in artist2_list:
        artist2 = artist
    
    #cross check values from the aid1 and aid2 lists and filter & append appropriately
    for user in value_aid1:
        if user in value_aid2:
            shared_users.append(user)
        else:
            aid1_only.append(user)
    for user in value_aid2:
        if user not in value_aid1:
            aid2_only.append(user)
    
    #get number of users in each filtered list
    shared_users_length = len(shared_users)
    aid1_only_length = len(aid1_only)
    aid2_only_length = len(aid2_only)
     
    #takes computed info and runs jaccard       
    total = shared_users_length + aid1_only_length + aid2_only_length
    index = float(shared_users_length)/float(total)
    print artist1+', '+ artist2+'   '+ str(index)

#start question 8 and builds dict for 9
#this does use the manual method for the first part
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
    
    #build original dict of all tags+info appended to tuple of year/month
    tag_info_final_sortable.setdefault((year, month), []).append(tmp)
    
    #count the occurrances of the artist for most popular total
    popular_alltime[artistID] = popular_alltime.get(artistID,0) + 1
    
    #make dicts for 2005 to get most popular artists
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

#start question 9
#sort most popular artists
sorted_popular_alltime = sorted(popular_alltime.items(), key=itemgetter(1), reverse=True)

#slice most popular artists and get the 10 most popular
the_top_ten = sorted_popular_alltime[:10]

#create sorted dict with by key of yr/month tuple, appends dict for each tag info 
sorted_tag_info_final_sortable = sorted(tag_info_final_sortable.items(), key=itemgetter(0))

artistID_counts = {}
for (date, info) in sorted_tag_info_final_sortable:
    tags_in_month = {}
    for info_item in info:
        artistID = info_item['artistID']
        
        #count the number of times that the artist appears in each month
        tags_in_month[artistID] = tags_in_month.get(artistID,0) + 1
    
    #for each month, sort the artists in it by count    
    sorted_tags_in_month = sorted(tags_in_month.items(), key=itemgetter(1), reverse=True)
    
    #get the top 10 artist for each month
    stim_10 = sorted_tags_in_month[:10]
    
    #append the list of the top 10 artist to that month in dict
    artistID_counts.setdefault(date, []).append(stim_10)
    
    #sort full dictionary by date tuple to get correct order
    sorted_artistID_counts = sorted(artistID_counts.items(), key=itemgetter(0))

artist_months = {}
for (date,top_artists) in sorted_artistID_counts:
    for inner_list in top_artists:
        for (artistID, tags) in inner_list:
            
            #for each month that the artist was in the top 10
            #take that m/yr pair and append it to the artist id
            artist_months.setdefault(artistID, []).append(date)

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "1. Who are the top artists?"
print

#for items in top 10 (slided), get name and id
for (count, artist) in sorted_artist_name_id_count[:10]:
    for (artist_name, artist_id) in artist.items():
        print '' + artist_name + ' ('+ str(artist_id) +') ' + str(count) + ''

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "2. Who are the top users?"
print

#get info for top 10 users who have played most songs
for userID, weight in sorted_total_user_play_count[:10]:
    print 'user: ' + str(userID) + ', playcount: ' + str(weight) + ''

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "3. Which artists have the most listeners?"
print

#from slided dict, get top 10 artists w/most plays
for (user_count, artist) in sorted_artist_name_to_users[:10]:
    for (artist_name, artist_id) in artist.items():
        print '' + artist_name + ' ('+ str(artist_id) +'): ' + str(user_count) + ''

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "4. Which artists have the highest average number of plays per listener?"
print

#4 and 5 do the same thing, but 4 doesn't require specific number of users

#get top 10 artists sorted by most average pays
for i, info_list in sorted_average_plays[:10]:
    for info_item in info_list:
        avg_count = info_item['avg_count']
        user_count = info_item['user_count']
        playcount = info_item['playcount']
        artist = info_item['artist']
        artist_id = info_item['artist_id']
        print 'Artist: '+ artist + ' ('+ str(artist_id) +'), Total plays: '+ str(playcount) +',\
Listeners: '+ str(user_count) +', Average plays: '+ str(avg_count) 

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "5. Which artists with at least 50 listeners have the highest avg number of plays per listener?"
print

for i, info_list in sorted_average_plays_50[:10]:
    for info_item in info_list:
        avg_count = info_item['avg_count']
        user_count = info_item['user_count']
        playcount = info_item['playcount']
        artist = info_item['artist']
        artist_id = info_item['artist_id']
        print 'Artist: '+ artist + ' ('+ str(artist_id) +'), Total plays: \
'+ str(playcount) +', Listeners: '+ str(user_count) +', Average plays: '+ str(avg_count)

print
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
print "6. Do users with five or more friends listen to more songs?"
print

#count the respecitve lists to get total number of users in them
five_or_more_length = len(five_or_more)
less_than_five_length = len(less_than_five)

#add each user's plays together for the artist to get the total number
#of plays for the artist
sum_total_plays_five_or_more = sum(total_plays_five_or_more.values())
sum_total_plays_less_than_five = sum(total_plays_less_than_five.values())

#use varaibles defined above to get total number of plays for those with
#5+ or <5 users attached to them
five_or_more_avg = sum_total_plays_five_or_more/five_or_more_length
less_than_five_avg = sum_total_plays_less_than_five/less_than_five_length

print 'Five or more friends:'
print 'Average plays: '+ str(five_or_more_avg) +', Total plays: \
'+ str(sum_total_plays_five_or_more) +', Users: '+ str(five_or_more_length)
print
print 'Less than five friends:'
print 'Average plays: '+ str(less_than_five_avg) +', Total plays: \
'+ str(sum_total_plays_less_than_five) +', Users: '+ str(less_than_five_length) 

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

#for each of these, sort the respective dict, slice to get 10 most popular
#run through artist dictionary to get name from id

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
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print
# I am using the top 10 artists in terms of **overall** numbers of tags
print "9. Artists with the highest number of overall tags, the first month they entered"
print "the top 10, and the number of times they appeared in the top ten."
print

#only do the following things for artists in the top 10
for artistID, count in the_top_ten:
    date_list = []
    
    #get the artist's name from the info dict
    artist_name_list = artist_info_dict.get(artistID)
    for artist_name in artist_name_list:
        print artist_name + ' (' + str(artistID) + '):  num tags = ' + str(count)
        artist_months_list = artist_months.get(artistID)
        
        #for each date info item in list for artist, convert the month number into name
        for (year, month) in artist_months_list:
            formated_month = datetime(year, int(month), 1)
            selected_month = formated_month.strftime("%b")
            
            #convert date object into a string
            date_str = selected_month +' '+str(year)
            
            #append each date string to the list for the corresponding artist
            date_list.append(date_str)
        
        #to get the first time that the artist appeared in the top ten, get the first
        #object in the date list for the artist
        print "  first month in top10 = " + date_list[0]
        
        #use len to get total number of times that the artist appeared in top ten
        months_in_top_10 = len(artist_months_list)
        print "  months in top10 = " + str(months_in_top_10)
        print