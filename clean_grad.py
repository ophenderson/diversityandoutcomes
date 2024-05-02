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
grad_keep_cols = ['Year', 'DISTRICT', 'SCHOOL', 'GNUMERATOR_RACE_W', 'GDENOM_RACE_W', 'GNUMERATOR_RACE_B', 'GDENOM_RACE_B', 'GNUMERATOR_RACE_H', 'GDENOM_RACE_H']
grad_dataset = grad_dataset[grad_keep_cols]
grad_dataset.fillna('NaN')
grad_dataset = grad_dataset.replace(-1, 0)
grad_dataset = grad_dataset.query("SCHOOL != 'DISTRICT NO CHARTER' & SCHOOL != 'DISTRICT WITH CHARTER'")
grad_dataset = grad_dataset.drop('SCHOOL', axis=1)
grad_by_dist = grad_dataset.groupby(['Year', 'DISTRICT']).sum()
grad_by_dist['Graduation Rate - W'] = grad_by_dist['GNUMERATOR_RACE_W']/grad_by_dist['GDENOM_RACE_W']
grad_by_dist['Graduation Rate - B'] = grad_by_dist['GNUMERATOR_RACE_B']/grad_by_dist['GDENOM_RACE_B']
grad_by_dist['Graduation Rate - H'] = grad_by_dist['GNUMERATOR_RACE_H']/grad_by_dist['GDENOM_RACE_H']

# Dropping rows with special school districts
grad_drop_schools = ['SC Department of Corrections', 'SC Department of Juvenile Justice', 'SC Public Charter District', 'SC School for the Deaf and the Blind', 'Charter Institute at Erskine','Department of Juvenile Justice', "Governor's Schools","Governor's School for Agriculture at John de la Howe", 'Limestone Charter Association', 'SC Department Of Juvenile Justice' ]
grad_by_dist = grad_by_dist.query('DISTRICT != @grad_drop_schools')
