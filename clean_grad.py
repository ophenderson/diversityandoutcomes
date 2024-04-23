# Couldn't figure out how to make this flexible for all my grad files so just decided to clean one and make sure it all works and then I can apply to rest of my files later

# Importing 
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
                        # skiprows=[0]) for student
    # Information about the file
    info = len(raw)
    print('Number of entries:' ,fname, info)
    return raw
# need to go through and make these grad specific
grad_data_list = {}

for fname in grad_files:
    grad = read_grad_file(fname)
    (basename, ext) = os.path.splitext(fname)
    tail = basename[-2:]
    grad_data_list[tail]=grad
    grad_dataset = pd.concat(grad_data_list)
    grad_dataset = grad_dataset.reset_index(0)
    grad_dataset = grad_dataset.rename(columns={'level_0':'Year'})
    keep_cols = ['Year', 'DISTRICT', 'SCHOOL', 'GNUMERATOR_RACE_W', 'GDENOM_RACE_W', 'GNUMERATOR_RACE_B', 'GDENOM_RACE_B', 'GNUMERATOR_RACE_H', 'GDENOM_RACE_H']
    grad_dataset = grad_dataset[keep_cols]
    grad_dataset.fillna('NaN')
    grad_dataset = grad_dataset.replace(-1, 0)
    grad_dataset['Graduation Rate - W'] = grad_dataset['GNUMERATOR_RACE_W']/grad_dataset['GDENOM_RACE_W']
    grad_dataset['Graduation Rate - B'] = grad_dataset['GNUMERATOR_RACE_B']/grad_dataset['GDENOM_RACE_B']
    grad_dataset['Graduation Rate - H'] = grad_dataset['GNUMERATOR_RACE_H']/grad_dataset['GDENOM_RACE_H']
    grad_dataset = grad_dataset.query("SCHOOL != 'DISTRICT NO CHARTER' & SCHOOL != 'DISTRICT WITH CHARTER'")
    grad_dataset = grad_dataset.drop('SCHOOL', axis=1)
    # OK so now I want it to group by district (ex: take the 2 abbeville's and sum them together but leave the year column alone)



