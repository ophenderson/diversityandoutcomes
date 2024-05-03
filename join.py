# This is the joining script. It will take join one of the dataframes on another and then join the remaining dataframe onto the joined dataframe to create 1 file

# Importing
import pandas as pd 

# Reading pickle
grads = pd.read_pickle('grad.pkl')
teachers = pd.read_pickle('teacher.pkl')
students = pd.read_pickle('student.pkl')



# Attempting the join on my own...
merged = teachers.merge(grads, on='District', how = 'outer', indicator=True)
# look at merge indicator
# drop merge indicator
# merged = merged.students()
