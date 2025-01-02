import numpy as np
import pandas as pd


#1  Binning concept

'''
The main motive of doing it to categories the data as per our bin size and bin style
'''

bins = linspace(min(data), max(data), 4) # making it into 3 bins

group_names = ['Low', 'Medium', 'High']

data['categories'] = pd.cut(data, bins, labels=group_names , include_lowest=True) # It is necessary to add include lowest or it will not work











#2 How to handle categorial data 
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












#3 Splitting of the dataset
#  It means dividing the dataset into training and testing dataset

'''
Why the need to split the dataset?

The main motive of splitting the dataset is to train the model on the training dataset and
then test the model on the testing on unknown dataset .
'''
#NOTE: continuing with the encoded data

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
# test_size is the size of the testing dataset here given as 20%
# random_state is used to make the split same everytime , means to randomly chosen the rows for testing or training








#4 Feature Scaling

'''
This is basically used to scale the data in the same range so that the model can be trained properly
and suppose if a number is very high as compared with the other and it will dominate the overall term.
So in order to adjust it, we need to scale the data  accordingly .

The value gets bound within a fixed range only .


Types:
    Simple Feature Scaling 
        x = x/max(x)
    
    Min-Max Scaling(Normalisation) lies between -3 to 3
        x = (x - min(x))/(max(x) - min(x))

    Z-Score Normalisation(Standardisation) lies between 0 to 3
        x = (x - mean(x))/std(x)

'''

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train.iloc[:, 3:] = sc.fit_transform(X.iloc[:, 3:]) 
# fit -> calculate the mean and std for the entire row or col
# transform -> apply the formula to the entire row or col

X_test.iloc[:, 3:] = sc.transform(X_test.iloc[:, 3:]) 
# here we are not fitting the data because we have already fitted the 
# data on the training dataset and we do not calculate the mean and std again here

#NOTE: We do not need to scale the y because it is the dependent variable and it is 
#      not necessary to scale it




