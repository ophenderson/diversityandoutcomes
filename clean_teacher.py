# Importing
import pandas as pd
import glob
import os

# Making a list of teacher files
# Changed the names of the files to match each other
teacher_files = glob.glob('raw/SOUTH CAROLINA TEACHERS BY RACE AND GENDER*')

# Function 
dictionary = {'DISTRICT':'SCHOOL DISTRICT/ CAREER CENTER','WHITE MALE':'WHITE MALES', 'WHITE FEMALE': 'WHITE FEMALES','WHITE, GENDER NOT REPORTED':'WHITE GENDER NOT REPORTED','BLACK MALE':'BLACK MALES', 'BLACK FEMALE':'BLACK FEMALES', 'BLACK, GENDER NOT REPORTED':'BLACK GENDER NOT REPORTED','HISPANIC MALE':'HISPANIC MALES', 'HISPANIC FEMALE':'HISPANIC FEMALES', 'HISPANIC, GENDER NOT REPORTED':'HISPANIC GENDER NOT REPORTED', 'TOTAL STAFF':'TOTAL NUMBER OF TEACHERS'}
def read_teacher_file(fname):
    # Reading the excel file
    raw = pd.read_excel(fname)
    if f"2019 file" :
        raw = raw.rename(columns = dictionary)
    # Information about the file
    info = len(raw)
    print('Number of entries:' ,fname, info)
    return raw

teacher_data_list = {}

for fname in teacher_files:
    teacher = read_teacher_file(fname)
    (basename, ext) = os.path.splitext(fname) 
    tail = basename[-2:]
    teacher_data_list[tail]=teacher
    teacher_dataset = pd.concat(teacher_data_list)
 #%%   
teacher_dataset = teacher_dataset.reset_index(0)
teacher_dataset = teacher_dataset.rename(columns={'level_0':'Year'})
teacher_keep_cols = ['Year','SCHOOL DISTRICT/ CAREER CENTER','WHITE MALES','WHITE FEMALES','WHITE GENDER NOT REPORTED','BLACK MALES', 'BLACK FEMALES', 'BLACK GENDER NOT REPORTED','HISPANIC MALES', 'HISPANIC FEMALES', 'HISPANIC GENDER NOT REPORTED', 'TOTAL NUMBER OF TEACHERS']
teacher_dataset = teacher_dataset[teacher_keep_cols]


teacher_dataset['totalw'] = teacher_dataset['WHITE MALES'] + teacher_dataset["WHITE FEMALES"] + teacher_dataset["WHITE GENDER NOT REPORTED"]
teacher_dataset['totalb'] = teacher_dataset['BLACK MALES'] + teacher_dataset["BLACK FEMALES"] + teacher_dataset["BLACK GENDER NOT REPORTED"]
teacher_dataset['totalh'] = teacher_dataset['HISPANIC MALES'] + teacher_dataset["HISPANIC FEMALES"] + teacher_dataset["HISPANIC GENDER NOT REPORTED"]
teacher_dataset.fillna('N/A')

