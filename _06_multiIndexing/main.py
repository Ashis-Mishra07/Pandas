import numpy as np
import pandas as pd


# can we have multiple index? Let's try
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
a = pd.Series([1,2,3,4,5,6,7,8],index=index_val)
'''
(cse, 2019)    1
(cse, 2020)    2
(cse, 2021)    3
(cse, 2022)    4
(ece, 2019)    5
(ece, 2020)    6
(ece, 2021)    7
(ece, 2022)    8
dtype: int64
'''

# The problem?
a['cse'] # KeyError: 'cse' is not indivisual index so return an error
a['cse',2019] # 1


# how to create MULTIINDEX OBJECT  
 
# 1. pd.MultiIndex.from_tuples()
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
multiindex = pd.MultiIndex.from_tuples(index_val)
'''
MultiIndex([('cse', 2019),
            ('cse', 2020),
            ('cse', 2021),
            ('cse', 2022),
            ('ece', 2019),
            ('ece', 2020),
            ('ece', 2021),
            ('ece', 2022)],
           )
'''
multiindex.levels # return FrozenList([['cse', 'ece'], [2019, 2020, 2021, 2022]])
multiindex.levels[0] # ['cse', 'ece']
multiindex.levels[1] # [2019, 2020, 2021, 2022]


# 2. pd.MultiIndex.from_product()
pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]])



# creating a series with multiindex object
s = pd.Series([1,2,3,4,5,6,7,8],index=multiindex)
'''
cse  2019    1
     2020    2
     2021    3
     2022    4
ece  2019    5
     2020    6
     2021    7
     2022    8
dtype: int64
'''

# how to fetch items from such a series
s['cse'] # return all the values of cse




# To convert a multiindex series to a dataframe
# unstack
temp = s.unstack()
'''

    2019	2020	2021	2022
cse	  1	     2	     3	      4
ece	  5	     6	     7	      8
'''
# To convert a dataframe to a multiindex series
# stack
temp.stack()


'''
NOTE : The main objective of multiindexing is to convert higher nD Dataframes into
       lower level of nD Dataframes.(most likely into 2D Dataframes)
'''

# multiindex df from row perspective
branch_df1 = pd.DataFrame(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10],
        [11,12],
        [13,14],
        [15,16],
    ],
    index = multiindex,
    columns = ['avg_package','students']
)



# multiindex df from columns perspective
branch_df2 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
    ],
    index = [2019,2020,2021,2022],
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)
'''

             delhi	                 mumbai
    avg_package	students	avg_package	students
2019	1	        2	         0	        0
2020	3	        4	         0	        0
2021	5	        6	         0	        0
2022	7	        8	         0	        0

'''




# Multiindex df in terms of both cols and index (4D Dataframe)
branch_df3 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
        [9,10,0,0],
        [11,12,0,0],
        [13,14,0,0],
        [15,16,0,0],
    ],
    index = multiindex,
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)






# Stacking and Unstacking
'''
NOTE : Unstack will basically convert the rows of the dataframe into columns 
       it will not affect the columns rather it will add the rows as columns down to it .


NOTE : Stack will basically convert the columns of the dataframe into rows




NOTE : In case of Unstacking the the multiindex at row level that is present will get 
       convert into columns and the level of multiindexing decreases.

       In same way in case of  Stacking the dataframe the cols that present will
       get convert into rows and the level of multiindexing increases.
'''


# Fetching Data from Multiindex Dataframe

# Extracting rows single
branch_df3.loc[('cse',2022)]
# multiple
branch_df3.loc[('cse',2019):('ece',2020):2]
# using iloc
branch_df3.iloc[0:5:2] # gives the row 0,2,4


# Extracting cols
branch_df3['delhi']['students']
branch_df3.iloc[:,1:3] # gives the entire row for 1 and 2 indexed cols


# Extracting both
branch_df3.iloc[[0,4],[1,2]] # return frorm 0 to 4 row and 1 to 2 col


# sort index
# both -> descending -> diff order
# based on one level
branch_df3.sort_index(ascending=False)
branch_df3.sort_index(ascending=[False,True]) # it will sort the level0 in descending and level1 in ascending in multilevel index
branch_df3.sort_index(level=0,ascending=[False]) # it will sort the level0 specifically in descending order


# multiindex dataframe(col) -> transpose
branch_df3.transpose()

# swaplevel
branch_df3.swaplevel(axis=1) # it will swap the level of multiindexing in cols
branch_df3.swaplevel(axis=0) # it will swap the level of multiindexing in rows




