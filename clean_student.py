# Importing
import pandas as pd
import glob
import os

# Creating a list of all student files
# I changed the name of the 2017-2018 student district data to make this easier!!
student_files = glob.glob('raw/*District Headcount by Gender, Ethnicity and Pupils in Poverty*')

# Function 
def read_student_file(fname):
    # Reading the excel file
    skips = [0,1,2,3,4,5]
    if '2017_18' in fname:
        skips = [0]
    raw = pd.read_excel(fname,skiprows = skips)
    # Information about the file
    info = len(raw)
    print('Number of entries:' ,fname, info)
    return raw

student_data_list = {}

for fname in student_files:
    student = read_student_file(fname)
    (basename, ext) = os.path.splitext(fname)
    tail = basename[-2:]
    student_data_list[tail]=student
    student_dataset = pd.concat(student_data_list)
    
student_dataset = student_dataset.reset_index(0)
student_dataset = student_dataset.rename(columns={'level_0':'Year', 'Unnamed: 0':'District ID','Unnamed: 1':'District','Unnamed: 2':'Total Number of Students','Yes':'Pupils in Poverty'})
student_keep_cols = ['Year', 'District ID', 'District', 'Total Number of Students','Black or African-American','Hispanic or Latino', 'White']
student_dataset = student_dataset[student_keep_cols]


# Dropping rows with special school districts
student_drop_schools = ['4701','4801','5205','5207','5208','5209','5364','5395','4901','Statewide Totals', 'Statewide Total', 'Statewide Percentage', 'Statewide Percentages', '']
student_bad = student_dataset['District ID'].isin(student_drop_schools)
student_dataset = student_dataset[student_bad == False]
student_bad = student_dataset[['District', 'Total Number of Students']].isna().all(axis = 'columns')
student_dataset = student_dataset[student_bad == False]
#%%
# Combining districts that were consolidated prior to 2023 (this will be in all my scripts)
# Bamberg 1 and 2 became Bamberg 3 in 2022
# Barnwell 19 and 29 became Barnwell 48 in 2022
# Orangeburg 3, 4, 5 became Orangeburg in 2019






