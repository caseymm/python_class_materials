from pandas import Series, DataFrame

import pandas as pd
from numpy.random import randn
import numpy as np

schools = {'unc': {'aug': 4.1, 'sep': 4.3, 'oct': 4.5}, 'duke': {'aug': 3.8, 'sep': 3.8, 'oct': 4.1}}

df = DataFrame(schools)

#print df.unc
#print df.unc.oct

##########

school_yr = {'unc': {2012: 4.1, 2013: 4.3, 2014: 4.5}, 'duke': {2012: 3.8, 2013: 3.8, 2014: 4.1}, 'ncstate': {2012: 3.9, 2013: 3.8, 2014: 4.3}}

df = DataFrame(school_yr)

print str(df[['unc','ncstate']]) #retrieves columns
print
print str(df[:2]) #slices on rows
print
print "ADFGQRDBADFBDSFBNSDsldkbnadlkfbnad;fnFNSFNFXNS"
print df['duke']>4.0
print str(df[df['duke']>4.0])

##########

d = {'unc': 0.4, 'duke': 0.8, 'ncstate': 0.6}
s = Series(d)
print
print s
print
print str(df - s)

print "df2df2df2df2df2df2df2df2df2df2df2df2df2df2df2df2df2df2df2"
df2 = df.ix[[2014, 2012, 2013], ['unc', 'duke', 'ncstate']]
print str(df2)
print
#sort by row index (row is 0 index)
print str(df2.sort_index())
#sort by column (column is 1 index)
print
#sorts by both school and year
print str(df2.sort_index().sort_index(axis=1))

#########

d = {'unc': {2012: 4.1, 2013: 4.3, 2014: 4.5}, 'duke': {2012: 3.8, 2013: 3.8, 2014: 4.1}, 'ncstate': {2012: 3.9, 2013: 3.8, 2014: 4.3}}

df = DataFrame(d)
df['ncstate'][2012] = np.nan
print df
print df['ncstate'].mean()
print df.sum()
print df.sum(axis=1)
print df.idxmax()

#########

df = DataFrame({'cb': [6, 2, 8, 4], 'ca': [7, 3, 1, 5]}, index=['id', 'ia', 'ib', 'ic'])
print
print df
print
print df.sort_index()
print
print df.sort_index(axis=1, ascending=False)
print
print df.sort_index(by='cb')

########

df = DataFrame({'a': [5, 7, 1, 1], 'b': [2, 4, 8, 6]})
print
print df
#sorts by a and then by the assoc b vals
print df.sort_index(by=['a','b'])
print

######

s = Series([8, 2, 5, 9, 4, 7, 5, 3], index=[['a','a','b','b','c','c','d','d'], ['x','y','x','y','x','y','x','y']])
print s
print s['b']
#can slice
print s[1:2]
#can sel particular items
print s.ix[['a','c']]

s2 = s.unstack()
print s2
#can also restack to put back in original form
print s2.stack()
print

#####
d = np.arange(12).reshape((4,3))
df = DataFrame(d, index=[['a','a','b','b'], [1, 2, 1, 2]], columns=[['unc','unc','duke'], ['x','y','x']])
print df

#this sums the outermost thing
print df.sum(level=0)




















