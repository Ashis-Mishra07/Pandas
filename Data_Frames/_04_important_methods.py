import numpy as np
import pandas as pd


# Adding new cols
# if this column is not present it will write a new column 
movies['Country'] = 'India'


# from existing ones
# Making a new column lead actor from the actor column
movies['lead actor'] = movies['actors'].str.split('|').apply(lambda x:x[0])




# Important DataFrame Methods


# 1. astype() - to change the datatype of a column
ipl['ID'] = ipl['ID'].astype('int32')
ipl['Season'] = ipl['Season'].astype('category')


# 2. value_counts(series and dataframe)
a = pd.Series([1,1,1,2,2,3])
a.value_counts()
'''
1    3
2    2
3    1
dtype: int64
'''
marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])
marks.value_counts()
'''
How many rows are repeated
    iq   marks  package
    80   70     14         2
    90   70     7          1
    100  80     10         1
    120  100    14         1
dtype: int64
'''

# Q.Find which player has won most potm -> in finals and qualifiers
ipl = pd.read_csv('ipl-matches.csv')
ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()

# Q.Toss decision plot
ipl['TossDecision'].value_counts().plot(kind='pie')

# Q.How many matches each team has played
(ipl['Team2'].value_counts() + ipl['Team1'].value_counts()).sort_values(ascending=False)





# 3. sort_values(series and dataframe) 
#        -> ascending -> na_position -> inplace -> multiple cols

x = pd.Series([12,14,1,56,89])
x.sort_values() # ascending order 

movies = pd.read_csv('movies.csv')

movies.sort_values('title_x',ascending=False)  # sort it according to titlw in desc


students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)
'''
     name	   college	 branch	 cgpa	package
0	nitish	     bit	  eee	 6.66	  4.0
1	ankit	     iit	  it	 8.25	  5.0
2	rupesh	     vit	  cse	 6.41	  6.0
3	NaN	         NaN	  NaN	 NaN	  NaN
4	mrityunjay	 NaN	  me	 5.60	  6.0
5	NaN	         vlsi	  ce	 9.00	  7.0
6	rishabh	     ssit	  civ	 7.40	  8.0
7	NaN	         NaN	  cse	 10.00	  9.0
8	aditya	     NaN	  bio	 7.40	  NaN
9	NaN	         git	  NaN	 NaN	  NaN
   
'''

students.sort_values('name') # it will sort the values and make the NaN values at the end
students.sort_values('name',na_position='first') # it will sort the values and make the NaN values at the start
# sorting on multiple columns
movies.sort_values(['year_of_release','title_x']) 
# the above will sort first as year then acc to title in ascending order
movies.sort_values(['year_of_release','title_x'],ascending=[True,False])





# 3.rank(series)
batsman = pd.read_csv('batsman_runs_ipl.csv')
  # give the rank acc to the runs he make in the match
batsman['batting_rank'] = batsman['batsman_run'].rank(ascending=False)
batsman.sort_values('batting_rank')
'''
Basically u have to write on which column u have to decide the ranking i.e. runs here 
'''


 # 4.sort_index(series and dataframe)
marks = {
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}
marks_series.sort_index(ascending=False)
'''
It will sort according to the index value in descending order

science     89
maths       67
hindi      100
english     57
dtype: int64

'''

# 5.set_index(dataframe) -> inplace
batsman.set_index('batter',inplace=True) # when u want to make ur better column as index


# 6.reset_index(series + dataframe) -> drop parameter
batsman.reset_index(inplace=True) # makes it normal again


# how to replace existing index without loosing
batsman.reset_index().set_index('batting_rank')
'''
Reset index convert the series into a dataframe
'''

# 7.rename(dataframe) -> index
movies.set_index('title_x',inplace=True) 
      # to change the name of the column
movies.rename(columns={'imdb_id':'imdb','poster_path':'link'},inplace=True)
      # to change the name of the index / any row 
movies.rename(index={'Uri: The Surgical Strike':'Uri','Battalion 609':'Battalion'})



# 8.unique(series)
temp = pd.Series([1,1,2,2,3,3,4,4,5,5,np.nan,np.nan])
print(temp)
len(temp.unique()) # temp.unique will also count the null value
temp.nunique() # it will not count the null value


# 9.To check null values
#    i.isnull ( series and dataframe) 
students['name'].isnull() # go and check for missing values

#   ii.notnull ( series and dataframe)
students['name'].notnull() # go and check for not missing values

#   iii.hasnans ( series )
students['name'].hasnans # check for any missing value if one , return true


# 10.dropna(series + dataframe) -> how parameter -> works like or
students['name'].dropna() # if it has missing values then drop them in series
students.dropna() # if it has missing values then drop them in dataframe
students.dropna(how='any') # if any of the value is missing then drop them

'''
by default the dropna has how='any' parameter so if any col value of the row contains
NaN value it will drop the row completely
'''
students.dropna(how='all') # if all the values are missing then only drop them

students.dropna(subset=['name']) # it will delete the row where the name is missing only , not depend on any other
students.dropna(subset=['name','college']) # it will delete the row where the name or college is missing


# 11.fillna(series + dataframe)
students['name'].fillna('unknown') # fill the missing values with unknown as name
students['package'].fillna(students['package'].mean()) # fill the package with mean value
students.fillna(0) # fill all the missing values with 0 ( not recommended)

students['name'].fillna(method='ffill') # forward fill  if NaN it will take the upper value
students['name'].fillna(method='bfill') # backward fill  if NaN it will take the lower value


# 12.drop_duplicates(series + dataframe) -> works like and -> duplicated()
temp = pd.Series([1,1,1,2,3,3,4,4])
temp.drop_duplicates()
'''
0    1
3    2
4    3
6    4
dtype: int64
'''
marks.drop_duplicates() # it will keep the first value and removes the next occurings
marks.drop_duplicates(keep='last') # here it will keep the last occuring and remove the prevs
'''
 by default is first
 i.e. marks.drop_duplicates(keep='first')
'''


# 13.drop(series + dataframe)
temp = pd.Series([10,2,3,16,45,78,10])
temp.drop(index=[0,6])
students.drop(columns=['branch','cgpa'],inplace=True) # it will drop the two columns
students.set_index('name').drop(index=['nitish','rupesh']) # it will drop the two rows


# 14.apply(series + dataframe)
temp = pd.Series([10,20,30,40,50])
def sigmoid(value):
  return 1/1+np.exp(-value)

temp.apply(sigmoid)
'''
0    1.000045
1    1.000000
2    1.000000
3    1.000000
4    1.000000
dtype: float64
'''

# difference between two points
points_df = pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)
def euclidean(row):
  pt_A = row['1st point']
  pt_B = row['2nd point']

  return ((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2)**0.5

points_df['distance'] = points_df.apply(euclidean,axis=1)
points_df # add a new column to the end of the dataframe about the distance















