from pandas import Series, DataFrame

import pandas as pd
from numpy.random import randn
import numpy as np

artist_list = {'David Bowie': {"August": 571, "Sept": 623, "Nov": 409}, 'The Beatles': {"August": 725, "Sept": 518, "Nov": 822}, 'New Order': {"August": 274, "Sept": 492, "Nov": 368}}

df = DataFrame(artist_list)
#print df.T['Sept']
flipped = df.T
print "September sum"
print df.T['Sept'].sum()
print
print "Bowie Sum"
print df['David Bowie'].values.sum()
