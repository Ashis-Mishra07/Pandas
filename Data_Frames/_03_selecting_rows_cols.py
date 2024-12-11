import numpy as np
import pandas as pd



# Selecting cols from a DataFrame

# single cols
movies['title_x']  # this will give u a series 

# multiple cols
movies[['year_of_release','actors','title_x']]  # this will give u a DataFrame

'''
If single row/col fetched then it will return a series
If multiple row/col fetched then it will return a DataFrame
'''








# Selecting rows from a DataFrame

'''
    iloc - searches using index positions
    loc - searches using index labels
'''

# single row
movies.iloc[5]  # return the 6th movie row and return a series

# multiple row
movies.iloc[:5]  # since multiple rows are fetched so it will return a DataFrame

# fancy indexing
movies.iloc[[0,4,5]]



# single col
students.loc['nitish']

# multiple cols
students.loc['nitish' : 'rishabh']  # here from nitish to rishabh all rows will be included

# fancy indexing
students.loc[['nitish','ankita','rupesh']]
students.iloc[[0,3,4]]









# Selecting both rows and cols

# fetch first three columns for first three rows
movies.iloc[ 0:3 , 0:3 ]
movies.loc[0:2,'title_x':'poster_path']  # here 2 is included in the range

'''
If working with iloc make sure toi deal with index
but when working with loc , deal witn the value not index
'''







# Filtering


# find all the final winners
temp = ipl['MatchNumber']=='Final'
new_temp = ipl[temp]
new_temp[['Season' , 'WinningTeam']]

ipl[ipl['MatchNumber'] == 'Final'][['Season','WinningTeam']]   # all can be done in a single match


# how many super over finishes have occured
ipl[ipl['SuperOver'] == 'Y'].shape[0]  # shape will give u the tuple and tuple[0] will give u the row number


# how many matches has csk won in kolkata
ipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0]


# toss winner is match winner in percentage
(ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100


# Action movies with rating higher than 7.5
mask1 = movies['genres'].str.split('|').apply(lambda x:'Action' in x)
mask1 = movies['genres'].str.contains('Action')
mask2 = movies['imdb_rating'] > 7.5

movies[mask1 & mask2]

'''
movies['fdd'].spilt('|')  # this will give u an error because split is not a method 
                            of series rather it is a string method
'''








