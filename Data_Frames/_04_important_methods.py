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



