[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```python
import nsfg
import numpy as np

# using the nsfg package from thinkstats2 to import and clean data
df = nsfg.ReadFemPreg()
df

first_child = df[df.pregordr == 1]
other_child = df[df.pregordr != 1]

diff_means = first_child.totalwgt_lb.mean() - other_child.totalwgt_lb.mean()

first_n = len(first_child.totalwgt_lb)
other_n = len(other_child.totalwgt_lb)
pooled_var = (first_n * first_child.totalwgt_lb.var() + other_n * other_child.totalwgt_lb.var()) / (first_n + other_n)

cohens_d = diff_means/np.sqrt(pooled_var)

cohens_d
```

> > Cohen's d was calculated to be about -.07, suggesting that first born children may be slightly lighter on average compared to other children. While the magnitude of the effect is slightly larger compared to the difference in pregnancy length (Cohen's d was computed to be about .03), -.07 standard deviations is still an incredibly small difference that is likely the result of random chance.