# This is the joining script. It will take join one of the dataframes on another and then join the remaining dataframe onto the joined dataframe to create 1 file

# Importing
import pandas as pd 

# Reading pickle
grads = pd.read_pickle('grad.pkl')
teachers = pd.read_pickle('teacher.pkl')
students = pd.read_pickle('student.pkl')



# Merging teacher and grad dataset by the Year and District columns
merged = teachers.merge(grads, on=['Year', 'District'], how = 'outer', indicator=True)
# Looking at the merge indicator to make sure everything says 'Both'
print(merged['_merge'])
# Merge indicator looks good... drop the merge indicator before my next merge 
merged.drop(columns = ['_merge'], inplace=True)
# Merging student data
merged = merged.merge(students, on=['Year', 'District'], how = 'outer', indicator=True)