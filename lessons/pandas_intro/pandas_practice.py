#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Sep  9 13:33:20 2020

@author: mason
"""

import numpy as np
import pandas as pd

s = pd.Series([1,3,5,np.nan,6,8])

s

df = pd.DataFrame({'A': 1.,
                   'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index = list(range(4)), dtype = 'float32'), 
                   'D': np.array([3]*4, dtype = 'int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})

df

dates = pd.date_range('20130101', periods=6)

dates

df2 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

df2

df.dtypes

df.head()

df.tail(3)

df.index

df.columns

df.describe()

df.T

df

df.sort_index(axis = 1, ascending=False)

df

df2.sort_index(axis=0, ascending=False)

df2

df2.sort_values(by='B')

df2

df2['A']

df2[0:3]

df2['20130102':'20130104']

df2.loc[dates[0]]

df2.loc[:, ['A', 'B']]

df2.loc['20130102':'20130104', ['A', 'B']]

df2.loc['20130102', ['A', 'B']]

df2.loc[dates[0], 'A']

df2.at[dates[0], 'A']

df2.iloc[3]

df2.iloc[3:5, 0:3]

df2.iloc[[1, 2, 4], [0, 2]]

df2.iloc[:, 1:3]

df2.iloc[1, 1]

df2.iat[1, 1]

##### Boolean indexing #####

df2[df2['A'] > 0]

df2[df2 > 0]

df = df2.copy()

df['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

df

df[df['E'].isin(['two', 'four'])]

##### Setting #####

s1 =pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))

s1

df2['F'] = s1

df2

df2.at[dates[0], 'A'] = 0

df2

df2.iat[0, 1] = 0

df2

df2.loc[:, 'D'] = np.array([5] * len(df2))

df2

df = df2.copy()

df[df > 0] = -df

df

# Missing Data

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])

df1

df1.loc[dates[0]:dates[1], 'E'] = 1

df1

df1.dropna(how='any')

df1

df1.fillna(value=5)

df1

pd.isna(df1)

# Operations

df.mean()

df.mean(1)

df

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)

s

df.sub(s, axis='index')

df

df.apply(np.cumsum)

df.apply(lambda x: x.max() - x.min())

s = pd.Series(np.random.randint(0, 7, size=10))

s

s.value_counts()

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])

s.str.lower()

# Merge

df = pd.DataFrame(np.random.randn(10, 4))

df

pieces = [df[:3], df[3:7], df[7:]]

pd.concat(pieces)

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

pd.merge(left, right, on='key')

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})

right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})

pd.merge(left, right, on='key')

# Grouping

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8), 
                   'D': np.random.randn(8)})

df

df.groupby('A').sum()

df.groupby(['A', 'B']).sum()

# Reshaping

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 
                     'foo', 'foo', 'qux', 'qux'], 
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])

df

df2 = df[:4]

df2

stacked = df2.stack()

stacked

stacked.unstack()

stacked.unstack(1)

stacked.unstack(0)

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})

df

pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'] )

# Time series

rng = pd.date_range('1/1/2012', periods=100, freq='S')

rng

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

ts

ts.resample('5Min').sum()

rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')

rng

ts = pd.Series(np.random.randn(len(rng)), rng)

ts

ts_utc = ts.tz_localize('UTC')

ts_utc

ts_utc.tz_convert('US/Eastern')

ts_utc

rng = pd.date_range('1/1/2012', periods=5, freq='M')

ts = pd.Series(np.random.randn(len(rng)), index=rng)

ts

ps = ts.to_period()

ps

ps.to_timestamp()

# Categoricals

df = pd.DataFrame({'id': [1, 2, 3, 4, 5, 6],
                   'raw_grade': ['a', 'b', 'b', 'a', 'a', 'e']})

df

df['grade'] = df['raw_grade'].astype('category')

df['grade']

df['grade'].cat.categories = ['very good', 'good', 'very bad']

df['grade']

df['grade'] = df['grade'].cat.set_categories(['very bad', 'bad', 'medium', 'good', 'very good'])

df['grade']

df.sort_values(by='grade')

df.groupby('grade').size()

# Plotting

import matplotlib.pyplot as plt

plt.close('all')

ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2012', periods=1000))

ts = ts.cumsum()

ts.plot()

df = pd.DataFrame(np.random.randn(1000, 4),
                  index=ts.index,
                  columns=['A', 'B', 'C', 'D'])

df = df.cumsum()

plt.figure()

df.plot()

plt.legend(loc='best')

