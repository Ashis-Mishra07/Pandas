import numpy as np
import pandas as pd

# GroupBy Attributes and Methods
# find total number of groups -> len
# find items in each group -> size
# first()/last() -> nth item
# get_group -> vs filtering
# groups
# describe
# sample
# nunique

movies = pd.read_csv('/content/imdb-taop-1000.csv')


# total groups formed
len(movies.groupby('Genre'))
movies['Genre'].nunique()


movies.groupby('Genre').size() # in a table how many rows covered by each grp but return in asc order of name
movies.groupby('Genre').value_counts() # same as above but return in desc order of value counts
'''
Genre
Action       172
Adventure     72
Animation     82
Biography     88
Comedy       155
Crime        107
Drama        289
Family         2
Fantasy        2
Film-Noir      3
Horror        11
Mystery       12
Thriller       1
Western        4
dtype: int64
'''


genres = movies.groupby('Genre')
genres.first() # for each group it will show u the first movie
genres.last()  # for each group it will show u the last movie
genres.nth(6)  # for each group it will show u the 7th movie and if not present it will not return anything


# To get all the info of a particular group
genres.get_group('Action')
movies[movies['Genre'] == 'Action']


# groups
genres.groups
'''
It will return u a dictionary where key is the group name and 
value it will store the indexes where it is present in the movies dataframe
'''


# describe
genres.describe() # it will give u the summary of each group like mode count  std max min mean



# sample
genres.sample() # it will return u a random sample from each group
genres.sample(2) # it will return u 2 random sample  but this will return u false if the sample is big
                 # so u have to add inplace = True

genres.sample(2,inplace=True) 


# nunique
genres.nunique() # it will return u the unique values in each group for every column






























