import numpy as np
import pandas as pd


# MELT

# wide to long
pd.DataFrame({'cse':[120]})
'''
  cse 	
0 120
'''
pd.DataFrame({'cse':[120]}).melt()
'''
  variable	value
0	cse	     120
'''


# Chnaging the name of the column
pd.DataFrame({'cse':[120],'ece':[100],'mech':[50]}).melt(var_name='branch',value_name='num_students')
'''
   branch   num_students
0	cse	        120
1	ece	        100
2	mech	     50

'''

# skipping some columns to remain as it is and for rest making it melt
# id_vars
pd.DataFrame(
    {
        'branch':['cse','ece','mech'],
        '2020':[100,150,60],
        '2021':[120,130,80],
        '2022':[150,140,70]
    }
).melt(id_vars=['branch'],var_name='year',value_name='students')















