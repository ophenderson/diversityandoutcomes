# Importing
import pandas as pd
import glob
import os

# Making a list of teacher files
# Changed the names of the files to match each other
teacher_files = glob.glob('raw/SOUTH CAROLINA TEACHERS BY RACE AND GENDER*')

# Function 
def read_teacher_file(fname):
    # Reading the excel file
    raw = pd.read_excel(fname)
    # Information about the file
    info = len(raw)
    print('Number of entries:' ,fname, info)
    return raw
# need to go through and make these teacher specific
data_list = {}

for fname in teacher_files:
    teacher = read_teacher_file(fname)
    (basename, ext) = os.path.splitext(fname)
    tail = basename[-2:]
    data_list[tail]=teacher
    dataset = pd.concat(data_list)
    dataset = dataset.reset_index(0)
    dataset = dataset.rename(columns={'level_0':'Year'})
    # need to drop the bottom rows and then the numbers should align with the student data.... eeeeee!!!!

#%%

# Importing
import pandas as pd
import glob

# Making a list of teacher files
# Changed the names of the files to match each other
teacher_files = glob.glob('raw/SOUTH CAROLINA TEACHERS BY RACE AND GENDER*')
#%%
# Reading in a file
teacherdf = pd.read_excel('raw/SOUTH CAROLINA TEACHERS BY RACE AND GENDER FOR THE 2017-18 SCHOOL YEAR (HEADCOUNT BY SCHOOL DISTRICT), MARCH 29, 2019.xlsx')

# Adding year column, not working
teacherdf['YEAR'] = '2017-2018' 

# Keeping only columns needed
keep_cols = ['DISTRICT ID', 'SCHOOL DISTRICT/ CAREER CENTER', 'WHITE MALES', 'WHITE FEMALES', 'WHITE GENDER NOT REPORTED', 'BLACK MALES', 'BLACK FEMALES', 'BLACK GENDER NOT REPORTED','HISPANIC MALES', 'HISPANIC FEMALES', 'HISPANIC GENDER NOT REPORTED', 'TOTAL NUMBER OF TEACHERS']
teacherdf = teacherdf[keep_cols]

# Adding the total number of teachers across races
teacherdf['totalw'] = teacherdf['WHITE MALES'] + teacherdf["WHITE FEMALES"] + teacherdf["WHITE GENDER NOT REPORTED"]
teacherdf['totalb'] = teacherdf['BLACK MALES'] + teacherdf["BLACK FEMALES"] + teacherdf["BLACK GENDER NOT REPORTED"]
teacherdf ['totalh'] = teacherdf['HISPANIC MALES'] + teacherdf["HISPANIC FEMALES"] + teacherdf["HISPANIC GENDER NOT REPORTED"]

# Dropping the columns that separate teachers by gender
teacherdf = teacherdf.drop(columns =['WHITE MALES', 'WHITE FEMALES', 'WHITE GENDER NOT REPORTED', 'BLACK MALES', 'BLACK FEMALES', 'BLACK GENDER NOT REPORTED','HISPANIC MALES', 'HISPANIC FEMALES', 'HISPANIC GENDER NOT REPORTED'])

# Filling in missing values
teacherdf.fillna('N/A')

