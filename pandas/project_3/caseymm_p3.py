from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np

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
#print user_tagged

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

#count = merged_info_sept['count']

################ OUTPUT ####################

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
print selected.sort('avg', ascending=False)[:10]

print
print "Question 5"
print

#DON'T forget to ask about counts/sorting for august
print shorter_aug[:10]
test = shorter_aug[:10]
print shorter_sept[:10]

rapid = test.to_json()
#print rapid["artistID"]

print rapid
