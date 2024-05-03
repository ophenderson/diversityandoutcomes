# Importing pandas, glob, and os
import pandas as pd
import glob
import os

# Making a list of all the grad rate files from raw folder
# In order to make this easier to do, I changed the names of the 2023 file to be match the format of the others
grad_files = glob.glob('raw/OVERALL_GRADRATE*')

# Function 
def read_grad_file(fname):
    # Reading the excel file
    raw = pd.read_excel(fname)
    # Information about the file
    info = len(raw)
    print('Number of entries:' ,fname, info)
    return raw
# Empty dictionary that will contain each of the years that are in the dataframe
grad_data_list = {}

# For loop
for fname in grad_files:
    # grabbing the file
    grad = read_grad_file(fname)
    # getting the school year off the end of the file and creating a column of school years
    (basename, ext) = os.path.splitext(fname)
    tail = basename[-2:]
    grad_data_list[tail]=grad
    # concatenating all 6 files into 1 dataframe
    grad_dataset = pd.concat(grad_data_list)
# Ending the for loop, resetting the index
grad_dataset = grad_dataset.reset_index(0)
# renaming the year column
grad_dataset = grad_dataset.rename(columns={'level_0':'Year'})
# Dropping unneeded columns
grad_keep_cols = ['Year', 'DISTRICT', 'SCHOOL', 'GNUMERATOR_RACE_W', 'GDENOM_RACE_W', 'GNUMERATOR_RACE_B', 
                  'GDENOM_RACE_B', 'GNUMERATOR_RACE_H', 'GDENOM_RACE_H']
grad_dataset = grad_dataset[grad_keep_cols]
# Filling in missing values
grad_dataset.fillna('NaN')
# replacing all the -1 with 0
grad_dataset = grad_dataset.replace(-1, 0)
# Dropping district with and without charter rows because they are sums of all the charter and non-charter schools
grad_dataset = grad_dataset.query("SCHOOL != 'DISTRICT NO CHARTER' & SCHOOL != 'DISTRICT WITH CHARTER'")
grad_dataset = grad_dataset.drop('SCHOOL', axis=1)
# grouping by year and district since the data was originally separated by school
grad_by_dist = grad_dataset.groupby(['Year', 'DISTRICT']).sum()
# calculating graduation rates by race
grad_by_dist['Graduation Rate - W'] = grad_by_dist['GNUMERATOR_RACE_W']/grad_by_dist['GDENOM_RACE_W']
grad_by_dist['Graduation Rate - B'] = grad_by_dist['GNUMERATOR_RACE_B']/grad_by_dist['GDENOM_RACE_B']
grad_by_dist['Graduation Rate - H'] = grad_by_dist['GNUMERATOR_RACE_H']/grad_by_dist['GDENOM_RACE_H']

# Dropping rows with special school districts
grad_drop_schools = ['SC Department of Corrections', 'SC Department of Juvenile Justice', 'SC Public Charter District', 
                     'SC School for the Deaf and the Blind', 'Charter Institute at Erskine','Department of Juvenile Justice',
                     "Governor's Schools","Governor's School for Agriculture at John de la Howe", 
                     'Limestone Charter Association', 'SC Department Of Juvenile Justice', 'Palmetto Unified']
grad_by_dist = grad_by_dist.query('DISTRICT != @grad_drop_schools')

# Combining districts that were consolidated prior to 2023 (this will be in all my scripts)
# Bamberg 1 and 2 became Bamberg 3 in 2022
grad_by_dist = grad_by_dist.rename(index = {'Bamberg 1':'Bamberg 3', 'Bamberg 2':'Bamberg 3'})
# Barnwell 19 and 29 became Barnwell 48 in 2022
grad_by_dist = grad_by_dist.rename(index = {'Barnwell 19':'Barnwell 48', 'Barnwell 29':'Barnwell 48'})
# Orangeburg 3, 4, 5 became Orangeburg in 2019
grad_by_dist = grad_by_dist.rename(index = {'Orangeburg 3': 'Orangeburg', 'Orangeburg 4': 'Orangeburg', 'Orangeburg 5':'Orangeburg'})
# For Grad Only - need to change Lexington/Richland 5 to Lexington 5
grad_by_dist = grad_by_dist.rename(index = {'Lexington/Richland  5':'Lexington 5', 'LEXINGTON/ RICHLAND  5': 'Lexington 5'})
# Summing up the combined rows
grad_by_dist = grad_by_dist.groupby(['Year', 'DISTRICT']).sum()
# Resetting index
grad_by_dist.reset_index(inplace=True)

# District column consistency 
grad_by_dist.rename(columns = {'DISTRICT':'District'}, inplace=True)
grad_by_dist['District'] = grad_by_dist['District'].str.upper()

# Saving as pickle file
grad_by_dist.to_pickle('grad.pkl')


