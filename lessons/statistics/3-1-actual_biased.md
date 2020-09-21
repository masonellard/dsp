[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python
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
```

![](/home/mason/.config/Typora/typora-user-images/image-20200920203814150.png)

The unbiased mean of children under 18 per household is about 1.02, and the biased mean is about 2.4 - over double the unbiased mean. Graphically, the bias has appeared to shift the plotted pmf to the right. 

