import pandas as pd

# Head 
# to preview the first 5 rows of the series
subs.head()
# to preview the custom number of rows
subs.head(10)



# Tail
# to preview the last 5 rows of the series
subs.tail()
# to preview the custom number of rows
subs.tail(10)



# Sample
# to preview the random 1 row of the series
subs.sample()
# to preview the custom number of random rows
subs.sample(10)


# Value counts
# to get the count of each value occur in the series
subs.value_counts()
# against each unique value it will return the count of that value occurs in descending order


# sort values
vk.sort_values() # it will sort the values in asending order
vk.sort_values(ascending=False) # it will sort the values in descending order
vk.sort_values(ascending=False).head(1).values # to get the highest score he has made in numpy arrar format
vk.sort_values(ascending=False).head(1).values[0] # to get the only score/value

# to make the changes in the original series
vk.sort_values(ascending=False,inplace=True) # it will sort the values in descending order and make changes in the original series

# to sort the index
vk.sort_index() # it will sort the index in asending order











