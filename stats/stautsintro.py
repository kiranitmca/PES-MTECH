import scipy
from scipy import stats
import numpy as np

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

# import numpy as np
# sample=[1,2,3,4,5]
# print(np.mean(sample))  
# print(np.std(sample,ddof=1))

# x_bar= 78
# mu = 75
# sigma = 6
# n = 16

# standrd_error = sigma/pow(n,0.5)
# z_score = (x_bar - mu)/standrd_error
# p_value = stats.t.sf(z_score,n-1)*100

# print("Standard Error:", standrd_error)
# print("Z-Score:", z_score)
# print("P-Value:", p_value)


# x_bar= 2.2
# mu = 2
# sd = 0.5
# n=50
# alpha = 0.05
# ts = (x_bar - mu)/(sd/pow(n,0.5))
# p_value = stats.t.sf(ts,n-1)*100
# print("Test Statistic:", ts)
# print("P-Value:", p_value)
# print("Alpha:", alpha)
# if p_value < alpha:
#     print("Reject the null hypothesis")
# else:
#     print("Fail to reject the null hypothesis")


# p_value = stats.t.cdf(-1.667,27)*2
# print(p_value*100)

sample1 = [10,11,12,13,19,18,23]
sample2=[20,35,22,11,12,10,23,38,42]

# print(stats.ttest_ind(sample1,sample2,alternative="two-sided"))

# # two-sided ,greatet,less


# sample = [9,3,-7,-4,0,-11,1,8,3]

# n= len(sample)
# sample_mean =np.mean(sample)
# std = np.std(sample,ddof=1)
# ts = sample_mean/(std/pow(n,0.5))
# print(ts)

# print(stats.t.sf(ts,n-1)*100)

# before =[33,32,38,45,37,47,48,41,45]
# after =[42,35,31,41,37,36,49,49,48]

# print(stats.ttest_rel(after,before,alternative="greater"))

# chi_test=stats.chisquare([90,10,40,40],[54,36,54,36])
# print(chi_test)

chi_test_ind = stats.chisquare([245,354,243],[98,220,140])
print(chi_test_ind)

# chi_2 = stats.chi2_contingency([[245,98],[354,220],[243,140]])
# print(chi_2)

# H1 Accepted because p-value is less than 0.05