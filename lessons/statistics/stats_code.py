#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:11:30 2020

@author: mason
"""

import nsfg
import numpy as np

df = nsfg.ReadFemPreg()
df

first_child = df[df.pregordr == 1]
other_child = df[df.pregordr != 1]

diff_means = first_child.totalwgt_lb.mean() - other_child.totalwgt_lb.mean()

first_n = len(first_child.totalwgt_lb)
other_n = len(other_child.totalwgt_lb)

pooled_var = (first_n*first_child.totalwgt_lb.var()+other_n*other_child.totalwgt_lb.var())/(first_n+other_n)

cohens_d = diff_means/np.sqrt(pooled_var)

cohens_d


import numpy as np
import nsfg
import thinkstats2
import thinkplot

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

df = nsfg.ReadFemResp()
num_chil = df.numkdhh

unbiased_pmf = thinkstats2.Pmf(num_chil, label='num_children')

thinkplot.Pmf(unbiased_pmf)
thinkplot.Config(xlabel='Number of Children', ylabel='PMF')

biased_pmf = BiasPmf(unbiased_pmf, label='Biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([unbiased_pmf, biased_pmf])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

biased_pmf.Mean()
unbiased_pmf.Mean()

import numpy as np
import thinkstats2
import thinkplot


x = np.random.random(1000)

pmf = thinkstats2.Pmf(x, label='Random Numbers') 
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Random', ylabel='PMF')

cdf = thinkstats2.Cdf(x, label='Random Numbers')
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random', ylabel='CDF')

from scipy.stats import norm

height_dist = norm(loc=178, scale=7.7)

height_dist.cdf(185.4) - height_dist.cdf(177.8)

def InterpolateSample(df, log_upper=6.0):
    """Makes a sample of log10 household income.

    Assumes that log10 income is uniform in each range.

    df: DataFrame with columns income and freq
    log_upper: log10 of the assumed upper bound for the highest range

    returns: NumPy array of log10 household income
    """
    # compute the log10 of the upper bound for each range
    df['log_upper'] = np.log10(df.income)

    # get the lower bounds by shifting the upper bound and filling in
    # the first element
    df['log_lower'] = df.log_upper.shift(1)
    df.loc[0, 'log_lower'] = 3.0

    # plug in a value for the unknown upper bound of the highest range
    df.loc[41, 'log_upper'] = log_upper
    
    # use the freq column to generate the right number of values in
    # each range
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)

    # collect the arrays into a single sample
    log_sample = np.concatenate(arrays)
    return log_sample


import hinc
income_df = hinc.ReadData()

log_sample = InterpolateSample(income_df, log_upper=6.0)

sample = np.power(10, log_sample)

Mean(sample), Median(sample)
Skewness(sample), PearsonMedianSkewness(sample)

cdf = thinkstats2.Cdf(sample)
cdf.Prob(Mean(sample))