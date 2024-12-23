import pandas as pd
import numpy as np



courses = pd.read_csv('/content/courses.csv')
students = pd.read_csv('/content/students.csv')
nov = pd.read_csv('/content/reg-month1.csv')
dec = pd.read_csv('/content/reg-month2.csv')

matches = pd.read_csv('/content/matches.csv')
delivery = pd.read_csv('/content/deliveries.csv')

# pd.concat
# df.concat
# ignore_index
# df.append
# mullitindex -> fetch using iloc
# concat dataframes horizontally


# pd.concat
'''
To add the files vertically stack
'''
regs = pd.concat([nov,dec]) # it will start from 0 to 30 the  again from 0 to 30
regs = pd.concat([nov,dec], ignore_index=True) # it will form new indexes from 0 to 60


# NOTE : append is deprecated
# df.append
nov.append(dec) # it will start from 0 to 30 the  again from 0 to 30
nov.append(dec,ignore_index=True)  # it will form new indexes from 0 to 60


# The below will separate the data frame based on 'NOV' and 'DEC' and make it 0 to 30 for each
# Mulitindex Dataframe
multi = pd.concat([nov,dec],keys=['Nov','Dec'])

multi.loc['Nov'] # this will fetch the Nov data from it 
multi.loc[('Dec' , 4)] # this will fetch the 5th row of Dec dataframe 



#NOTE: iloc is used for retriving integer based data and loc is used for fetching the non integer labels

# if want to stack the dataframes horizontally
'''
if the size of two dataframes are not same then NaN values will be added in place of absent values
'''
pd.concat([nov,dec],axis=1)



# MERGING DATAFRAMES


# inner join
students.merge(regs,how='inner',on='student_id')
# left join
courses.merge(regs,how='left',on='course_id')
# right join
students.merge(regs,how='right',on='student_id')
# outer join  -> means full join 
students.merge(regs,how='outer',on='student_id')




# Merging multiple table
# cols -> name -> course -> price
regs.merge(students,on='student_id').merge(courses,on='course_id')[['name','course_name','price']]




# Intersection
# 5. find students who enrolled in both the months
common_student_id = np.intersect1d(nov['student_id'],dec['student_id'])
common_student_id

# Set diff
# 6. find course that got no enrollment
# courses['course_id']
# regs['course_id']

course_id_list = np.setdiff1d(courses['course_id'],regs['course_id'])
courses[courses['course_id'].isin(course_id_list)]

# 8. Print student name -> partner name for all enrolled students
# self join
students.merge(students,how='inner',left_on='partner',right_on='student_id')[['name_x','name_y']]

'''
Since two same tables so only on will cause error , 
so making left_on for first table and right_on for second table
'''


# Alternate syntax for merge
# students.merge(regs)

pd.merge(students,regs,how='inner',on='student_id')



