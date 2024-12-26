import numpy as np
import pandas as pd


'''
Timestamp Object
Time stamps reference particular moments in time (e.g., Oct 24th, 2022 at 7:00pm)
'''

# creating a timestamp
pd.Timestamp('2023/1/5') #Timestamp('2023-01-05 00:00:00')

# variations
pd.Timestamp('2023-1-5')    #Timestamp('2023-01-05 00:00:00')
pd.Timestamp('2023, 1, 5')  #Timestamp('2023-01-05 00:00:00')

# only year
pd.Timestamp('2023')        #Timestamp('2023-01-01 00:00:00')

# using text
pd.Timestamp('5th January 2023')

# providing time also
pd.Timestamp('5th January 2023 9:21AM')





# using datetime.datetime object
import datetime as dt

x = pd.Timestamp(dt.datetime(2023,1,5,9,21,56)) #Timestamp('2023-01-05 09:21:56')
# datetime is by python and Timestamp is by pandas

# fetching attributes
x.year
x.month
x.day
x.hour
x.minute
x.second




# why separate objects to handle data and time when python already has datetime functionality?
'''
syntax wise datetime is very convenient
But the performance takes a hit while working with huge data. List vs Numpy Array
The weaknesses of Python's datetime format inspired the NumPy team to add a set of native time series data type to NumPy.
The datetime64 dtype encodes dates as 64-bit integers, and thus allows arrays of dates to be represented very compactly.
Because of the uniform type in NumPy datetime64 arrays, this type of operation can be accomplished much more quickly than if we were working directly with Python's datetime objects, especially as arrays get large
Pandas Timestamp object combines the ease-of-use of python datetime with the efficient storage and vectorized interface of numpy.datetime64
From a group of these Timestamp objects, Pandas can construct a DatetimeIndex that can be used to index data in a Series or DataFrame

'''



'''
For storing single datetime we use Timetamp onject
and for multiple datetime we use DatetimeIndex object
'''



# from strings
pd.DatetimeIndex(['2023/1/1','2022/1/1','2021/1/1'])

# using python datetime object
pd.DatetimeIndex([dt.datetime(2023,1,1),dt.datetime(2022,1,1),dt.datetime(2021,1,1)])

# using pd.timestamps
dt_index = pd.DatetimeIndex([pd.Timestamp(2023,1,1),pd.Timestamp(2022,1,1),pd.Timestamp(2021,1,1)])


# Date Range Function

# generate daily dates in a given range
pd.date_range(start='2023/1/5',end='2023/2/28',freq='3D') # normally D , but alternate 2D 

# B -> business days
pd.date_range(start='2023/1/5',end='2023/2/28',freq='B') # leave the sat and sun

# W -> one week per day
pd.date_range(start='2023/1/5',end='2023/2/28',freq='W') # returns only a single day from each week , by default return sunday

# W -> one week per day
pd.date_range(start='2023/1/5',end='2023/2/28',freq='W-THU') # customised to thursday

# H -> Hourly data(factor)
pd.date_range(start='2023/1/5',end='2023/2/28',freq='6H') # returns for each 6 hour timestamp

# M -> Month end
pd.date_range(start='2023/1/5',end='2023/2/28',freq='M')

# MS -> Month start
pd.date_range(start='2023/1/5',end='2023/2/28',freq='MS')

# A -> Year end
pd.date_range(start='2023/1/5',end='2030/2/28',freq='A')

# using periods(number of results)
pd.date_range(start='2023/1/5',periods=25,freq='M')
# the above will return 25 months from the start date anmd return the last day of each month




# to_datetime function
# converts an existing objects to pandas timestamp/datetimeindex object



# simple series example , converting string to datetime
s = pd.Series(['2023/1/1','2022/1/1','2021/1/1'])
pd.to_datetime(s) # return date wise all of them
pd.to_datetime(s).dt.day_name() # returns the day name of the date
pd.to_datetime(s).dt.year
pd.to_datetime(s).dt.month
pd.to_datetime(s).dt.month_name()


# with errors
s = pd.Series(['2023/1/1','2022/1/1','2021/130/1'])
pd.to_datetime(s,errors='coerce')
'''
0    January
1    January
2        NaT   not a time
dtype: object
'''


# converting all the datetime form string to date and time fromat
df = pd.read_csv('/content/expense_data.csv')
df['Date'] = pd.to_datetime(df['Date'])












