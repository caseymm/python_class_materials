from pandas import Series, DataFrame

import pandas as pd
from numpy.random import randn
import numpy as np

df = pd.read_csv('courses2.csv')
print df

g = df['enroll'].groupby(df['sem'])

#creates series with index of semester
print g.sum()
print g.sum().index
print
g = df['enroll'].groupby([df['sem'], df['course']])
print g.sum()

#get a dataframe out when you unstack it
print g.sum().unstack()

print df.groupby('sem')['enroll'].sum()
print df['enroll'].groupby(df['sem']).sum()
print

z = df.groupby('course')['enroll'].sum().order (ascending=False)[:2]
print z
zdf = DataFrame(z.values, index=z.index)
print zdf
zdf.columns = ['enroll']
print zdf
print
y = DataFrame(['Tools', 'InfoSys'], index=['inls161', 'inls382'])
y.columns = ['coursename']
print y

zdfy = zdf.join(y)
print zdfy

print pd.merge(zdf, y, right_index=True, left_index=True)
print zdf.join(y)
