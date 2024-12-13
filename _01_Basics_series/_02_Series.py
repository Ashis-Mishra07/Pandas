

'''

Pandas Series
    A Pandas Series is like a column in a table. 
    It is a 1-D array holding data of any type.

'''

# Importing pandas
        import numpy as np
        import pandas as pd

# Creating a Series

# Creating a Series from a list

        country = ['India', 'USA', 'Canada', 'Australia']
        series = pd.Series(country)
        '''
        -> The above code will output as :
        0       India
        1    Pakistan
        2         USA
        3       Nepal
        4    Srilanka
        dtype: object

        Mostly Object type means String type (99%) .

        '''

        # Creating a Series from integers
        runs = [13,24,56,78,100]

        runs_ser = pd.Series(runs)

        '''
        The above will make the index by its own . 
        If u want custom index then u can pass it .
        '''

        # custom index
        marks = [67,57,89,100]
        subjects = ['maths','english','science','hindi']

        pd.Series(marks,index=subjects)
        '''
        maths       67
        english     57
        science     89
        hindi      100
        dtype: int64
        '''

        # setting a name
        marks = pd.Series(marks,index=subjects,name='Nitish ke marks')
        marks
        '''
        maths       67
        english     57
        science     89
        hindi      100
        Name: Nitish ke marks, dtype: int64
        '''


# Creating a Series from a dictionary

        marks = {
            'maths':67,
            'english':57,
            'science':89,
            'hindi':100
        }

        marks_series = pd.Series(marks,name='nitish ke marks')
        marks_series

        '''
        maths       67
        english     57
        science     89
        hindi      100
        Name: nitish ke marks, dtype: int64
        '''



























