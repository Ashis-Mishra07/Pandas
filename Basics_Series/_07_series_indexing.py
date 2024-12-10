import pandas as pd

# Indexing

x = pd.Series([12,13,14,35,46,57,58,79,9])
x[0] # will give u 12
x[-1] # will give u an error

'''
movie
Zor Lagaa Ke...Haiya!            Meghan Jadhav
Zokkomon                       Darsheel Safary
Zindagi Tere Naam           Mithun Chakraborty
Zindagi Na Milegi Dobara        Hrithik Roshan
Zindagi 50-50                      Veena Malik
                                   ...        
2 States (2014 film)              Arjun Kapoor
1971 (2007 film)                Manoj Bajpayee
1920: The Evil Returns             Vicky Ahuja
1920: London                     Sharman Joshi
1920 (film)                   Rajniesh Duggall
Name: lead, Length: 1500, dtype: object
'''
movies[0] # give u 'Meghan Jadhav'
movies[-1] # give u 'Rajniesh Duggall'


# Slicing
x[0:3] # will give u 12,13,14
x[-2:] # will give u 79,9
x[::2] # will give u 12,14,46,58,9
x[[1,2,3]] # will give u 13,14,35
movies['Zokkomon'] # will give u 'Darsheel Safary'





# Editing

# using indexing
marks_series[1] = 100
marks_series

# what if an index does not exist
marks_series['evs'] = 100
'''
It will add a new index 'evs' with value 100
'''

#  can be done through slicing
runs_ser[2:4] = [100,100]
runs_ser # make the 2d and 3rd index as 100


