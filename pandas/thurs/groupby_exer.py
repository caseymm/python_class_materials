from pandas import Series, DataFrame

import pandas as pd
from numpy.random import randn
import numpy as np

d = [[12,15,26], [2,0,4], [1,0,3], [3,0,4], [24,18,31], [8,12,5], [6,3,0], [8,14,27], [28,21,16]]

df = DataFrame(d, index=[['uid123','uid123','uid123','uid345','uid345','uid345','uid678','uid678','uid678'], ['Bowie', 'Gaga', 'Spears', 'Bowie', 'Gaga', 'Spears','Bowie', 'Gaga', 'Spears']], columns=['Aug','Sep','Nov'])

df.index.names['uid', 'artist']
print df