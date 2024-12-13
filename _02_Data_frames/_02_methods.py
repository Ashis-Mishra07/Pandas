import numpy as np
import pandas as pd



# using read_csv
movies = pd.read_csv('movies.csv')
movies


# to know the shape
movies.shape # returns u a tuple (rows,cols)


# dtypes
movies.dtypes   # return a series of data types of each col


# index
movies.index    # RangeIndex(start=0, stop=950, step=1)

# columns
movies.columns  # Index(['movieId', 'title', 'genres'], dtype='object')


# values
movies.values   # returns a 2D numpy array


# head and tail
movies.head(2)
movies.tail()


# sample
ipl.sample(5) # returns a random sample of 5 rows


# info
movies.info()
'''
      This will result in:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1629 entries, 0 to 1628
Data columns (total 18 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   title_x           1629 non-null   object 
 1   imdb_id           1629 non-null   object 
 2   poster_path       1526 non-null   object 
 3   wiki_link         1629 non-null   object 
 4   title_y           1629 non-null   object 
 5   original_title    1629 non-null   object 
 6   is_adult          1629 non-null   int64  
 7   year_of_release   1629 non-null   int64  
 8   runtime           1629 non-null   object 
 9   genres            1629 non-null   object 
 10  imdb_rating       1629 non-null   float64
 11  imdb_votes        1629 non-null   int64  
 12  story             1609 non-null   object 
 13  summary           1629 non-null   object 
 14  tagline           557 non-null    object 
 15  actors            1624 non-null   object 
 16  wins_nominations  707 non-null    object 
 17  release_date      1522 non-null   object 
dtypes: float64(1), int64(3), object(14)
memory usage: 229.2+ KB
'''


# describe
movies.describe()    # shows only the numerical columns
'''
	  is_adult	  year_of_release	 imdb_rating	imdb_votes
count	1629.0	     1629.000000	1629.000000	    1629.000000
mean	 0.0	     2010.263966	5.557459	    5384.263352
std	     0.0	      5.381542	    1.567609	    14552.103231
min	     0.0	      2001.000000	0.000000	    0.000000
25%	     0.0	      2005.000000	4.400000	    233.000000
50%	     0.0	      2011.000000	5.600000	    1000.000000
75%	     0.0	      2015.000000	6.800000	    4287.000000
max	     0.0	      2019.000000	9.400000	    310481.000000
    
'''

# isnull
movies.isnull().sum()   # shows column wise how many missing values are there
'''
title_x                0
imdb_id                0
poster_path          103
wiki_link              0
title_y                0
original_title         0
is_adult               0
year_of_release        0
runtime                0
genres                 0
imdb_rating            0
imdb_votes             0
story                 20
summary                0
tagline             1072
actors                 5
wins_nominations     922
release_date         107
dtype: int64
'''


# duplicated
movies.duplicated().sum()   # count which rows are duplicates


# rename   -> change the column name 
students.rename(columns={'marks':'percent','package':'lpa'})  # this will not make permanent change
students.rename(columns={'marks':'percent','package':'lpa'},inplace=True)
# inplace true means it will replicate as permanent change











# MATHS FUNCTIONS

# sum -> axis argument
students.sum()   # returns the sum of each cols
students.sum(axis=0)  # returns sum along the rows


# mean/median
students.mean(axis=1)
stduents.median(axis=0)
students.std() # standard deviation
students.var() # variance

# max/min
students.max()  # shows u the row wise max value
students.min()  # shows u the column wise min value





