from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np
import json

pd.options.display.float_format = '{0:.2f}'.format

artists_df = pd.read_csv('artists.dat', sep='\t', index_col='name')

user_artists_df = pd.read_csv('user_artists.dat', sep='\t', index_col=['userID', 'artistID'])
user_artists_df_b = pd.read_csv('user_artists.dat', sep='\t', index_col=['artistID', 'userID'])

user_taggedartists_df = pd.read_csv('User_taggedartists.dat', sep='\t', index_col=['artistID', 'userID'])

###############

artists_df.index.name = 'artist'
new_artists = artists_df[['id']]
new_artists.columns = ['artistID']

#prints user > artist > weight
sorted_user_weights = user_artists_df.sort_index().sum(level=0).sort('weight', ascending=False)

#prints artist > user > weight
sorted_artist_weights = user_artists_df_b.sort_index().sum(level=0).sort('weight', ascending=False)

#filters out tags that are before 2000
user_tagged =  (user_taggedartists_df[user_taggedartists_df['year']>=2005])

august = user_tagged[(user_tagged['year']==2005) & (user_tagged['month']==8)]
sorted_aug = august.count(level=0).sort('tagID', ascending=False)
merged_info_aug = pd.merge(new_artists, sorted_aug, left_on='artistID', right_index=True)
merged_info_aug['count'] = merged_info_aug['tagID']
shorter_aug = merged_info_aug[['artistID', 'count']].sort('count', ascending=False)

september = user_tagged[(user_tagged['year']==2005) & (user_tagged['month']==9)]
sorted_sept = september.count(level=0).sort('tagID', ascending=False)
merged_info_sept = pd.merge(new_artists, sorted_sept, left_on='artistID', right_index=True)
merged_info_sept['count'] = merged_info_sept['tagID']
shorter_sept = merged_info_sept[['artistID', 'count']].sort('count', ascending=False)

################ OUTPUT ####################

#think about renaming weight

print "Question 1"
print
most_popular = pd.merge(new_artists, sorted_artist_weights, left_on='artistID', right_index=True).sort('weight', ascending=False)

#need to delete index from this
print most_popular[:10]

print
print "Question 2"
print
print sorted_user_weights[:10]

print
print "Question 3"
print
artist_to_user = user_artists_df_b.sort_index().count(level=0)
artist_to_user_merge = pd.merge(new_artists, artist_to_user, left_on='artistID', right_index=True).sort('weight', ascending=False)
print artist_to_user_merge[:10]

print
print "Question 4"
print
most_popular.columns = ['artistID', 'total_plays']
average_merge = pd.merge(artist_to_user_merge, most_popular, left_index=True, right_index=True)
fifty_plus =  (average_merge[average_merge['weight']>=50])
fifty_plus['avg'] = (fifty_plus['total_plays'])/(fifty_plus['weight'])
fifty_plus['artistID'] = fifty_plus['artistID_x']
selected = fifty_plus[['artistID','avg']]
#print selected.sort('avg', ascending=False)[:10]

avg_plays = selected.sort('avg', ascending=False)[:10]
avg_plays_json = avg_plays.T.to_json()
avg_plays_dict = json.loads(avg_plays_json)
for entry in avg_plays_dict:
    artist_ID = avg_plays_dict[entry]['artistID']
    avg = avg_plays_dict[entry]['avg']
    print entry +' ('+str(artist_ID)+') '+ str(avg)


print
print "Question 5"
print

#DON'T forget to ask about counts/sorting for august

#print shorter_aug[:10]
aug_output = shorter_aug[:10]

#print shorter_sept[:10]
sept_output = shorter_sept[:10]

print "Aug 2005"        
aug_json = aug_output.T.to_json()
aug_dict = json.loads(aug_json)
for entry in aug_dict:
    artist_ID = aug_dict[entry]['artistID']
    count = aug_dict[entry]['count']
    print '  '+entry +' ('+str(artist_ID)+'): '+ str(count)

print
print "Sep 2005" 
sept_json = sept_output.T.to_json()
sept_dict = json.loads(sept_json)
for entry in sept_dict:
    artist_ID = sept_dict[entry]['artistID']
    count = sept_dict[entry]['count']
    print '  '+entry +' ('+str(artist_ID)+'): '+ str(count)
    
