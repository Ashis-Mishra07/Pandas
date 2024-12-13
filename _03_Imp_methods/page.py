import numpy as np
import pandas as pd


# astype
import sys
sys.getsizeof(vk)

vk.astype('int32')
# this basically used to reduce the size , to save memory


# between
vk.between(51, 99) # return true or false against each value in the series
vk[vk.between(51, 99)].size # this will return the size of score oin between the two



# Clip
subs.clip(100,200) # this will clip the values in the series between 100 and 200
# for the value less than 100 -> makes it 100 , more than 200 makes it 200


# Drop Duplicates
temp = pd.Series([1,1,2,2,3,3,4,4])
temp.drop_duplicates() # this will drop the duplicates from the series and keep the first occurance
temp.drop_duplicates(keep='last') # this will keep the last value of the duplicates

temp.duplicated() # checks if the value against is duplicate or not
temp.duplicated().sum()  # return number of duplicate values
temp.drop_duplicates()



# Working on missing values
temp = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])

temp.isnull() # return true or false against each value in the series
temp.isnull().sum() # return number of missing values
temp.size # return 10
temp.count() # return 7

temp.dropna()  # drop the missing values
# fillna
temp.fillna(0) # fill the missing values with 0
temp.fillna(temp.mean()) # fill the missing values with mean of the series


# isin
'''
Below are the two ways of doing it
'''
temp[(temp == 49) | (temp == 99)]
temp[temp.isin([49, 99])]

'''
The result shows as
    match_no
    82    99
    86    49
    Name: runs, dtype: int64
'''


# Apply

# used to design and custom function and apply it to the series

# the below will give the first word of the string in capital letter
temp.apply( lambda x:x.split()[0].upper())

# the below will print whether the day is good or bad based on the temperature
temp.apply(lambda x:'good day' if x>temp.mean() else 'bad day')




# Copy and View
'''
The main difference between copy and view is , that if any changes in copy is made it 
will reflect to the original series , but if any changes in view is made it will
not reflect to the original series .


By default the head and tail takes the view of the table so it makes changes to the
original array if u r making any changes .
'''

temp = pd.Series([1,2,3,4,5,6,7,8,9,10])
new = temp.head() # gives the first 5 values
new[1] = 1  # this will also reflect to the original series

temp_copy = temp.copy()
temp_copy[1] = 1 # this will not reflect to the original series , as it is a copy








