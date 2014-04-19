from pandas import Series, DataFrame

import pandas as pd
from numpy.random import randn
import numpy as np

df = pd.read_table('courses.txt', sep=':', header=None, index_col=[1,0])
print df

df.index.names = ['semester', 'course']
print df

mylabels = ['enrollment', 'assignments']
df.columns = mylabels

#or
#df.columns = ['enrollment', 'assignments']

print
print df

#other
#df = pd.read_table('courses.txt', sep=':', header=None, names=['sem', 'course', 'enroll', 'assign'],
#index_col=['sem', 'course'])