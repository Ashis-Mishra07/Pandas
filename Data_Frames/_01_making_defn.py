import numpy as np
import pandas as pd


'''

The table consisting of rows and cols is called a DataFrame .
And each row or Each col is called as a single series .

So in short combining a set of series row wise or col wise 
constructs a DataFrame .

DataFrame by default add a index column in the table .

'''

# Methods of making a Dataframe :

# using lists
student_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]

pd.DataFrame(student_data,columns=['iq','marks','package'])
'''
The resultant table will look like this

    iq	 marks	package
0	100	   80	   10
1	90	   70	    7
2	120	  100	   14
3	80	   50       2

'''


# using dicts

student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}

students = pd.DataFrame(student_dict)




