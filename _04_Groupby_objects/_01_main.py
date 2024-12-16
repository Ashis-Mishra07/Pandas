import numpy as np
import pandas as pd

'''
Group by functions are basically applied on column
and specifically group by is addlied on categorial column datatype
'''


movies = pd.read_csv('/content/imdb-top-1000.csv')
genres = movies.groupby('Genre')
# and now we can apply aggrefate functions likesum,min,max, etc on it 

# find the top 3 genres by total earning
movies.groupby('Genre').sum()['Gross'].sort_values(ascending=False).head(3)
movies.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head(3) # or 


# find the genre with highest avg IMDB rating
movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(1)


# find director with most popularity
movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1)


# find number of movies done by each actor
movies['Star1'].value_counts()
movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False)


