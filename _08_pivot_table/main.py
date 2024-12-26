# The pivot table takes simple column-wise data as input, and groups the entries 
# into a two-dimensional table that provides a multidimensional summarization of the data.


import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('tips')

# to find the average male/female smoker/non-smoker bill
df.groupby(['sex','smoker']).mean().unstack()

# in pivot table
df.pivot_table(index='sex',columns='smoker',values='total_bill')
'''
pivot_table( which col to make index ,  which to make col , which to make values)
'''

# NOTE : The default value of the aggfunc is mean

# aggfunc
df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='std')



# all cols together
# if the values col is not specified, all the numeric cols are taken
df.pivot_table(index='sex',columns='smoker') 

# You can set the row and col wise dept 
df.pivot_table(index=['sex','smoker'] , columns=['date','time'])

# customised aggfunc
df.pivot_table(index=['sex','smoker'],columns=['day','time'],aggfunc={'size':'mean','tip':'max','total_bill':'sum'})


# margins
df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum',margins=True)
''' 
This margin returns an extra column and a row that contains the total sum of the values


smoker	     Yes	   No	      All
sex			
Male	   1337.07	  1919.75	3256.82
Female	    593.27	  977.68	1570.95
All	       1930.34	  2897.43	4827.77

'''


























































