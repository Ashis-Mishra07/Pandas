import pandas as pd

marks = [67,57,89,100]
subjects = ['maths','english','science','hindi']

mark_series = pd.Series(marks,index=subjects ,name='Ashis_ke_marks')
# mark_series is of Series class , so being a class it will follow certain attributes

# Series Attributes

# Size
mark_series_size = mark_series.size # return 4

# dtype
mark_series_dtype = mark_series.dtype # return dtype('int64')

# name
mark_series_name = mark_series.name # return Ashis_ke_marks

# is_unique
mark_series_is_unique = mark_series.is_unique # return True
''' Return true if all the elements of the series are unique '''

# index
mark_series_index = mark_series.index 
''' return Index(['maths', 'english', 'science', 'hindi'], dtype='object') '''

'''
NOTE:
    If the series class contains Integes then the index function 
    will return RangeIndex(start=0, stop=4, step=1)

    But if the series class contains Strings then the index function
    will return Index(['maths', 'english', 'science', 'hindi'], dtype='object')

'''

# values
mark_series_values = mark_series.values
''' return array([ 67,  57,  89, 100], dtype=int64) '''


