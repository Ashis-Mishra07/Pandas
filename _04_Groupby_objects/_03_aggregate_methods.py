import numpy as np
import pandas as pd


'''
We are adding the aggregate functions indivisually ,
but we can add all the functions at once using the agg() method.
'''
movies = pd.read_csv('/content/imdb-taop-1000.csv')
genres = movies.groupby('Genre')


genres.sum()
genres.mean()


genres.agg(
    {
        'Runtime':'mean',
        'IMDB_Rating':'mean',
        'No_of_Votes':'sum',
        'Gross':'sum',
        'Metascore':'min'
    }

    # This will add different agg function on diff columns
)
'''
The above will result is

Genre        Runtime	IMDB_Rating	 No_of_Votes	    Gross	  Metascore
					
Action	    129.046512	7.949419	  72282412	    3.263226e+10	33.0
Adventure	134.111111	7.937500	  22576163	    9.496922e+09	41.0
Animation	99.585366	7.930488	  21978630	    1.463147e+10	61.0
Biography	136.022727	7.938636	  24006844	    8.276358e+09	48.0
Comedy	    112.129032	7.901290	  27620327	    1.566387e+10	45.0


     # Here u have to apply through a dict
'''  


# passing list
genres.agg(['min','max','mean','sum'])
''' 
The above will show min,max,mean,sum for all the columns

    Runtime	          IMDB_Rating	       No_of_Votes	          Gross	     
sum min	max	mean	sum	min	max	mean	sum	min	max	mean	sum	min	max	mean	


   # Here u have to pass a list of agg functions u want to apply on the columns
'''


# Adding both the syntax
genres.agg(
    {
        'Runtime':['min','mean'],
        'IMDB_Rating':'mean',
        'No_of_Votes':['sum','max'],
        'Gross':'sum',
        'Metascore':'min'
    }
)





# Looping on groups 
for group,data in genres:
    print(type(group) , type(data))

'''
type(group) will return str class
type(data) will return dataframe class
'''

# Q. The question is to find the highest rated movie of each genre.

for group,data in genres:
    print( (data['IMDB_rating']==data['IMDB_rating'].max()) )


# Q.Making a new dataframe with the highest rated movie of each genre.

df=pd.DataFrame(columns=movies.columns)
# here we are creating a new(empty) dataframe with the same columns as the movies dataframe

for group,data in genres:
    df=df.append(data[data['IMDB_rating']==data['IMDB_rating'].max()])

df # here it will show the highest rated movies of each genre





# Apply
'''
Split function is like groupby function that will split the dataframe into groups 
and then apply function will apply transformation oneach grp
'''


genres.apply(min)  # for each group and each genre it will the min value for each column

# find number of movies starting with A for each group
def foo(group):
  return group['Series_Title'].str.startswith('A').sum()
  
genres.apply(foo)



# find ranking of each movie in the group according to IMDB score
def rank_movie(group):
  group['genre_rank'] = group['IMDB_Rating'].rank(ascending=False)
  return group

genres.apply(rank_movie)




# find normalized IMDB rating group wise

def normal(group):
  group['norm_rating'] = (group['IMDB_Rating'] - group['IMDB_Rating'].min())/(group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
  return group

genres.apply(normal)




# Make groups on multiple columns
'''
Combining multiple columns to make groups will create multiindex dataframes
'''

duo = movies.groupby(['Director','Actor']) #  This will create the group as per ur query
duo.get_group(('Christopher Nolan','Christian Bale')) # This will return the group of the director and actor u have passed

# find the most earning actor->director combo
duo['Gross'].sum().sort_values(ascending=False).head(1)

# find the best(in-terms of metascore(avg)) actor->genre combo
movies.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False).head(1)

# agg on multiple groupby
duo.agg(['min','max','mean'])


























