import pandas as pd

# csv are the comma separated values file and 
# contains the data in the form of rows and columns

# To read the csv file 


# With One column
pd.read_csv('/pathname/filename.csv') # by default it will return in dataframe
pd.read_csv('/pathname/filename.csv',squeeze=True) # will return in series

'''
0       48
1       57
2       40
3       43
4       44
      ... 
360    231
361    226
362    155
363    144
364    172
Name: Subscribers gained, Length: 365, dtype: int64

NOTE: if more rows are there it will truncate the middle ones 
      and show the first 5 and last 5 rows

      And column name is stored as name 
'''


# With two columns
vk = pd.read_csv('/content/kohli_ipl.csv',index_col='match_no',squeeze=True)
vk
'''
Here u need to specify which column to use as index
'''



