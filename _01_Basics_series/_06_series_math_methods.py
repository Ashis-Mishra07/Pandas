import pandas as pd

# count
'''
It will count the number of elements in the series .
The main diff between size and count is that size will also count
the NaN/missing values but count will not count it .
'''
vk.count() # return 365


# sum
'''
It will return the sum of all the elements in the series
'''
vk.sum() # return 5878


# Product
vk.prod() # return 0 



# mean -> median -> mode -> std -> var
subs.mean()
vk.median()
movies.mode()
subs.std()
vk.var()



# min/max
subs.max()
vk.min()


# describe
# gives the summary of the series
subs.describe()

'''
The OUTPUT will be
    count    365.000000
    mean     135.643836
    std       62.675023
    min       33.000000
    25%       88.000000
    50%      123.000000
    75%      177.000000
    max      396.000000
    Name: Subscribers gained, dtype: float64
'''


