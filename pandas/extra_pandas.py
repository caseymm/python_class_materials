from pandas import Series, DataFrame

import pandas as pd
from numpy.random import randn
import numpy as np

s = Series([31,25, 18])

print s

s13 = Series([31, 25, 18], index=['inls285', 'inls382', 'inls523'])

s14 = Series([29, 23, 14], index=['inls285', 'inls382', 'inls523'])

print s13 > 20
print s13[s13 > 20]

print
print
############

d = {'a': 5, 'b': 10, 'c': 15}

b = Series(d)

print b
print

if 'a' in b:
    print b['a']
print

############

t = ['b', 'c', 'd']

new_series = Series(d, index=t)
print new_series
print
#can't have an NaN with integers, will give you a float if you have missing data

##########

s14.name = "Spring 14"
s14.index.name = "Course names"
print s14

##########

print "Exercise"
print

aug_plays = Series([190, 274, 344], index=['Britney Spears', 'Depeche Mode', 'Lady Gaga'])
#new_august = Series(float([190, 274, 344]), index=['Britney Spears', 'Depeche Mode', 'Lady Gaga'])
sept_plays = Series([123, 497, 273], index=['Britney Spears', 'Depeche Mode', 'Lady Gaga'])
#new_sept = Series(float([123, 497, 273]), index=['Britney Spears', 'Depeche Mode', 'Lady Gaga'])

#avg_plays = (new_august + new_sept)/2
avg_plays = (aug_plays + sept_plays)/2

print avg_plays

##########

d_frame = {'course': ['inls285', 'inls285', 'inls382', 'inls382', 'inls523', 'inls523'], 'semester': ['s13', 's14', 's13', 's14', 's13', 's14'], 'enrollment': [31, 58, 26, 46, 19, 28]}

df = DataFrame(d_frame)

print df
print
print df.values
print df.index
print df.columns

get_from = df['course']
print get_from
#gives back series with index the same as the dataframe

get_from = df.course
print get_from
print

df = DataFrame(d_frame, index=['c1234', 'c2345', 'c8822', 'c7654', 'c5512', 'c4321'])

print df
print df.course
print
print df.ix['c1234']
print

df['tmp'] = [1, 3, 5, 7, 8, 9]

print df
print

schools = {'unc': {2012: 4.1, 2013: 4.3, 2014: 4.5}, 'duke': {2012: 3.8, 2013: 3.8, 2014: 4.1}}

df = DataFrame(schools)
print df
print df.T  #transpose

new_a = df.unc
print new_a
new_array = df.unc.values
print new_array

print new_a.sum()

##########

artist_list = {'David Bowie': {"August": 571, "Sept": 623, "Nov": 409}, 'The Beatles': {"August": 725, "Sept": 518, "Nov": 822}, 'New Order': {"August": 274, "Sept": 492, "Nov": 368}}

df = DataFrame(artist_list)
print df.T['Sept']
flipped = df.T
print df.T['Sept'].sum()

#df = DataFrame(flipped, index=['Bowie', 'Beatles', 'NewOrder'])
#flip = df
print df['David Bowie'].values.sum()




