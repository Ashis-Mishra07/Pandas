import numpy as np
import pandas as pd


# Binning concept

'''
The main motive of doing it to categories the data as per our bin size and bin style
'''

bins = linspace(min(data), max(data), 4) # making it into 3 bins

group_names = ['Low', 'Medium', 'High']

data['categories'] = pd.cut(data, bins, labels=group_names , include_lowest=True) # It is necessary to add include lowest or it will not work


