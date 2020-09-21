[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```python
from scipy.stats import norm

height_dist = norm(loc=178, scale=7.7)

height_dist.cdf(185.4) - height_dist.cdf(177.8)
```

Approximately 34% of the US male population falls between 5'10'' and 6'1'' (177.8 and 185.4 cm, respectively).