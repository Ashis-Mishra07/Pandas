import pandas as pd
import numpy as np

'''
Vectorised String Operations are fast and optimized.

'''

s = pd.Series(['cat','mat',None,'rat'])
# string accessor
s.str.startswith('c')


# import titanic
df = pd.read_csv('/content/titanic.csv')

# Common Functions


# lower/upper/capitalize/title
df['Name'].str.upper()
df['Name'].str.capitalize()  # first letter of each sentence
df['Name'].str.title()       # first letter of each word
df['Name'][df['Name'].str.len() == 82].values[0]

"            nitish                              ".strip()
df['Name'].str.strip()


# split -> get
df['lastname'] = df['Name'].str.split(',').str.get(0)

'''
split has some functions
str.split(  , n=2) # this will split the string n times
str.split(  , expand=True) # this will return a DataFrame
'''

# replace
df['title'] = df['title'].str.replace('Ms.','Miss.')
df['title'] = df['title'].str.replace('Mlle.','Miss.')


# filtering
# startswith/endswith
df[df['firstname'].str.endswith('A')]
# isdigit/isalpha...
df[df['firstname'].str.isdigit()]


# applying regex
# contains

# search john -> both case
df[df['firstname'].str.contains('john',case=False)] # can be john or JOHN or JoHn
df[df['firstname'].str.contains('john',case=True)]  # casn only be john



# find lastnames with start and end char vowel
df[df['lastname'].str.contains('^[^aeiouAEIOU].+[^aeiouAEIOU]$')]

'''

The above will filter whose lastname starts with vowel and end with vowel

^ -> start of string
. -> any number of characters 
$ -> end of string

'''


# slicing
df['Name'].str[::-1] # reverse the string












