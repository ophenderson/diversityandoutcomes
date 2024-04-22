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
    data_list[tail]=grad
    dataset = pd.concat(data_list)
    dataset = dataset.reset_index(0)
    dataset = dataset.rename(columns={'level_0':'Year'})
    keep_cols = ['Year', 'DISTRICT', 'SCHOOL', 'GNUMERATOR_RACE_W', 'GDENOM_RACE_W', 'GNUMERATOR_RACE_B', 'GDENOM_RACE_B', 'GNUMERATOR_RACE_H', 'GDENOM_RACE_H']
    dataset = dataset[keep_cols]
    dataset.fillna('NaN')
    dataset = dataset.replace(-1, 0)
    dataset['Graduation Rate - W'] = dataset['GNUMERATOR_RACE_W']/dataset['GDENOM_RACE_W']
    dataset['Graduation Rate - B'] = dataset['GNUMERATOR_RACE_B']/dataset['GDENOM_RACE_B']
    dataset['Graduation Rate - H'] = dataset['GNUMERATOR_RACE_H']/dataset['GDENOM_RACE_H']

# dataset = dataset.groupby('DISTRICT') - figure out how to group by district name, prof gave us a sheet with this code
  




