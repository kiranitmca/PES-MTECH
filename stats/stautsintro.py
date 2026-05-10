import scipy
from scipy import stats

# print("SciPy version:", scipy.__version__)

# data = [10, 20, 30, 40, 50]
# print("Mean:", stats.tmean(data))


# GMAT score normal ,mean = 680,std= 40 ,var = 1600

# what is the probablity , we will score more than 740
# what is the probablity , we will score less than 680
# what is the probablity , we will score between 720 and 760

# print(stats.norm.sf(740,680,40))
# print(stats.norm.cdf(680,680,40))
# print(stats.norm.cdf(760,680,40) - stats.norm.cdf(720,680,40))

#print(stats.norm.interval(0.90,420))
# x_bar=420
# n=25
# sigma = 20
# scale = sigma/pow(n,0.5)

# print(stats.norm.interval(0.9,x_bar,scale))

# 90 % chance is there this CI will contain population mean mu

# xbar=420
# n=25
# s=22
# scale = s/pow(n,0.5)

# print(stats.t.interval(0.9,n-1,xbar,scale))

import numpy as np
sample=[1,2,3,4,5]
print(np.mean(sample))  
print(np.std(sample,ddof=1))


