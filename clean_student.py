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
    raw = pd.read_excel(fname)
    # Information about the file
    info = len(raw)
    print('Number of entries:' ,fname, info)
    return raw
# need to go through and make these grad specific
student_data_list = {}

for fname in student_files:
    student = read_student_file(fname)
    (basename, ext) = os.path.splitext(fname)
    tail = basename[-2:]
    student_data_list[tail]=student
    student_dataset = pd.concat(student_data_list)
    student_dataset = student_dataset.reset_index(0)
    #%%
    student_dataset = student_dataset.rename(columns={'level_0':'Year'})
   
#%%   
    
    
    
    
    keep_cols = ['Year', 'DISTRICT', 'SCHOOL', 'GNUMERATOR_RACE_W', 'GDENOM_RACE_W', 'GNUMERATOR_RACE_B', 'GDENOM_RACE_B', 'GNUMERATOR_RACE_H', 'GDENOM_RACE_H']
    dataset = dataset[keep_cols]
    dataset.fillna('NaN')
    dataset = dataset.replace(-1, 0)
    dataset['Graduation Rate - W'] = dataset['GNUMERATOR_RACE_W']/dataset['GDENOM_RACE_W']
    dataset['Graduation Rate - B'] = dataset['GNUMERATOR_RACE_B']/dataset['GDENOM_RACE_B']
    dataset['Graduation Rate - H'] = dataset['GNUMERATOR_RACE_H']/dataset['GDENOM_RACE_H']



# Reading in a file
studentdf = pd.read_excel('raw/180 Day DistrictHeadcountbyRaceGender2017-18.xlsx')

# Performing cleaning functions
year = 2017-2018
studentdf['YEAR'] = year
 # once again, not sure how to make sure this is done differently for each file
keep_cols = ['District', 'District Name', 'Total # Actively Enrolled Students', 'Black or African American', 'Hispanic or Latino', 'White'] 
# Issue with this because of the way the file is formatted
studentdf = studentdf[keep_cols]
studentdf.fillna('N/A')



