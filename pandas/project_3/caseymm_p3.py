from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np
import json

#changes format to allow for floating point numbers
pd.options.display.float_format = '{0:.2f}'.format

#creates dataframes from all of the .dat files
artists_df = pd.read_csv('artists.dat', sep='\t', index_col='name')
user_artists_df = pd.read_csv('user_artists.dat', sep='\t', index_col=['userID', 'artistID'])
user_artists_df_b = pd.read_csv('user_artists.dat', sep='\t', index_col=['artistID', 'userID'])
user_taggedartists_df = pd.read_csv('User_taggedartists.dat',
                                    sep='\t', index_col=['artistID', 'userID'])

#renames the index artist
artists_df.index.name = 'artist'

#keeps only the 'id' column
new_artists = artists_df[['id']]

#renames the id column artistID
new_artists.columns = ['artistID']

#prints user > artist > weight
sorted_user_weights = user_artists_df.sort_index().sum(level=0).sort('weight', ascending=False)

#prints artist > user > weight
sorted_artist_weights = user_artists_df_b.sort_index().sum(level=0).sort('weight', ascending=False)

#filters out tags that are before 2000
user_tagged =  (user_taggedartists_df[user_taggedartists_df['year']>=2005])

#for both August and September:
    #gets only entries tagged in Aug/Sept of 2005
    #assigns new count to all frame columns, pulls count from tagID column
    #merges w/new_artists to grab artist name
    #renames 'tagID' to 'count' since it now describes the count
    #keeps only artistID and count colums & sorts by count
    #slice top 10 for each

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

print
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print
print "1. Who are the top artists?"
print

#takes most popular artists by playcount, merges to get name, slices top 10
most_popular = pd.merge(new_artists, sorted_artist_weights, left_on='artistID',
                        right_index=True).sort('weight', ascending=False)

print most_popular[:10]

print
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print
print "2. Who are the top users?"
print

#slices top 10 from frame showing top users by playcount
print sorted_user_weights[:10]

print
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print
print "3. What artists have the most listeners?"
print

#creates new df sorted by artistID and then userID to count how many
#individual listeners an artist has - then merges to get artist name
artist_to_user = user_artists_df_b.sort_index().count(level=0)
artist_to_user_merge = pd.merge(new_artists, artist_to_user, left_on='artistID',
                                right_index=True).sort('weight', ascending=False)

#slices df to get top 10 artists with the most listeners
print artist_to_user_merge[:10]

print
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print
print "4. What artists with at least 50 listeners have the highest average \
number of plays per listener?"
print

#sets most_popular to only display artistID and total_plays columns
most_popular.columns = ['artistID', 'total_plays']

#merges the most popular artists with the df mapping artists to user count
average_merge = pd.merge(artist_to_user_merge, most_popular, left_index=True, right_index=True)

#creates df that only displays artists in this new table w/ 50+ user count
fifty_plus =  (average_merge[average_merge['weight']>=50])

#creates 'avg' column to calculate and display avg playcount per listener
fifty_plus['avg'] = (fifty_plus['total_plays'])/(fifty_plus['weight'])

#merged table has two artistID cols, rename to better explain
fifty_plus['artistID'] = fifty_plus['artistID_x']

#only keep artistID and avg columns from the df
selected = fifty_plus[['artistID','avg']]

#sort the avg top played artists and slice top 10
avg_plays = selected.sort('avg', ascending=False)[:10]
print avg_plays

print
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print
print "5. For August and September 2005, what artists were tagged the most?"
print
print shorter_aug[:10]
print
print shorter_sept[:10]

#this is an example of what I'd thought about doing with the json
#it would work, but I'd have to sort all of the data again.

#for Aug/Sept:
    #create the frame ([month]_json)that will be written to the json
    #need to flip in order to extract variables more easily
    #create a variable ([month]_dict) to hold the json we just created
    #extract artist, artistIDs, and tags for month from json

#print "Aug 2005"        
#aug_json = aug_output.T.to_json()
#aug_dict = json.loads(aug_json)
#print aug_dict
#for entry in aug_dict:
    #artist_ID = aug_dict[entry]['artistID']
    #count = aug_dict[entry]['count']
    #print '  '+entry +' ('+str(artist_ID)+'):  num tags = '+ str(count)

print
print "Reflection Statement"
print
print "While I realize that this project was shorter than Project 2, and that\
I was already familiar with the data because of the second project, I did find \
this project to be a lot easier. It wasn't easy, but it wasn't quite as difficult \
as the previous two. Learning how to better use dictionaries has really helped me \
in some of the other work that I've done lately; however, I found using pandas to \
be a much more efficient, and enjoyable, way of completing this project. Rather than \
having to manually pull elements out of dictionaries in order to build new ones, I \
could easily manipulate the dataframe in pandas and merge it with another. I was also \
incredibly pleased to find export .to_json(). I didn't end up using it since I would have\
had to re-sort all of my data, but it's nice to know that it's an option. I love that I \
can essentially do all of my data manipulation with pandas and numpy, and then export \
my output directly to json."
