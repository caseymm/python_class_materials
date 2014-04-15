from pandas import Series, DataFrame

import pandas as pd
from numpy.random import randn
import numpy as np

stats_df = pd.read_csv('mlb.csv')

print stats_df

city_df = pd.read_csv('teams-cities.csv')

print city_df

print pd.merge(stats_df, city_df)

z = city_df[:3]

print z

#gives all info but only for first 3
print pd.merge(stats_df,z)

stats_df = pd.read_csv('mlb.csv', index_col='team')
print stats_df

city_df = pd.read_csv('teams-cities.csv', index_col='team')
print city_df

#for merging on index instead of column
print pd.merge(stats_df, city_df, left_index=True, right_index=True)

city_df = pd.read_csv('teams-cities.csv')
#now stats has index of team, but city has column of team

print pd.merge(stats_df, city_df, left_index=True, right_on='team')