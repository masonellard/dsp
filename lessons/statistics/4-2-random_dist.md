[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```python
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

```

![image-20200920220737246](/home/mason/.config/Typora/typora-user-images/image-20200920220737246.png)

![image-20200920220749628](/home/mason/.config/Typora/typora-user-images/image-20200920220749628.png)

According to the PMF and CDF, the distribution of random.random does appear to be uniform.