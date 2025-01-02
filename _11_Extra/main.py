import numpy as np
import pandas as pd


# Binning concept

'''
The main motive of doing it to categories the data as per our bin size and bin style
'''

bins = linspace(min(data), max(data), 4) # making it into 3 bins

group_names = ['Low', 'Medium', 'High']

data['categories'] = pd.cut(data, bins, labels=group_names , include_lowest=True) # It is necessary to add include lowest or it will not work




# How to handle categorial data 
# One-Hot Encoding , Label Encoding

'''
The need of making the categorial data into numerical data is because the machine learning model only understand the numerical data
and in order to make precise prediction we need to convert the categorial data into numerical data
'''

# One-Hot Encoding - Pandas
data = pd.read_csv('data.csv')
data_dummy = pd.get_dummies(data['column_name']) # suppose here country name , it will create the columns for each country and will assign 1 or 0 based on the data


# Level Order Encoding - Scikit 
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
'''
Lebel Encoding applies on the column which is having onky two values only
'''

data['column_name'] = label_encoder.fit_transform(data['column_name'])

# One Hot Encoding - Scikit
from sklearn.compose import ColumnTransformer  # this ensures whcih column u want ot make the one hot encoding
from sklearn.preprocessing import OneHotEncoder  # this ensures what basically u want to apply

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough') # 0 is the column number
'''
Transformer takes 3 values in the list
1. Name of the transformer
2. Which startegy to apply
3. Which column to apply

remainder = 'passthrough' means that the other columns will be as it is
          = 'drop' means that the other columns will be dropped

'''

data = ct.fit_transform(data) # this will return the numpy array
type(data) # numpy.ndarray

data= pd.DataFrame(data) # converting it into the  dataframe but it will remove the column names
data.columns = ['column1', 'column2', 'column3'] # adding the column names accordingly
