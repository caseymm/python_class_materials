from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np

tips = pd.read_csv('tips.csv')

#print tips[:10]

tips['tip_pct'] = tips['tip'] / tips['total_bill']

g = tips.groupby(['sex', 'smoker'])

gpct = g['tip_pct']

print gpct.mean()

print tips.groupby(['sex','smoker'], as_index=False).mean()

print tips.pivot_table(rows=['sex', 'smoker'])

print tips.pivot_table(['tip_pct', 'size'], rows=['sex', 'day'], cols='smoker')

print tips.pivot_table('tip_pct', rows=['sex', 'smoker'], cols='day', aggfunc=len, margins=True)

print tips.pivot_table('tip_pct', rows=['time', 'smoker'], cols='sex', margins=True)
#'sex', 