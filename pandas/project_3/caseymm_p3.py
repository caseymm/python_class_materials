from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np

artists_df = pd.read_csv('artists.dat', sep='\t')

user_artists_df = pd.read_csv('user_artists.dat', sep='\t', index_col=['userID', 'artistID'])
user_artists_df_b = pd.read_csv('user_artists.dat', sep='\t', index_col=['artistID', 'userID'])

#user_taggedartists_df = pd.read_csv('User_taggedartists.dat', sep='\t', index_col=['artistID', 'userID'])
user_taggedartists_df = pd.read_csv('User_taggedartists.dat', sep='\t')

###############

print "111111111111111111111111111"

new_artists = artists_df[['id','name']]
#flipped = artists_df.T[:2]
#artists_sliced = flipped.T
#print artists_sliced
new_artists.columns = ['artistID', 'artist']
print new_artists



print
print "222222222222222222222222222222222"

#prints user > artist > weight
print user_artists_df.sort_index()

#prints artist > user > weight
print str(user_artists_df_b.sort_index())



print
print "333333333333333333333333333333333333"
#print user_taggedartists_df

#filters out tags that are before 2000
user_tagged =  (user_taggedartists_df[user_taggedartists_df['year']>=2005])
#print user_tagged

merged_info = pd.merge(user_tagged, new_artists)

result = merged_info.sort(['userID', 'artistID'])
print result
