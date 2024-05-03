# Importing
import pandas as pd
import glob
import os

# Making a list of teacher files
# Changed the names of the files to match each other
teacher_files = glob.glob('raw/SOUTH CAROLINA TEACHERS BY RACE AND GENDER*')

# Function 
dictionary = {'DISTRICT':'SCHOOL DISTRICT/ CAREER CENTER','WHITE MALE':'WHITE MALES', 'WHITE FEMALE': 'WHITE FEMALES','WHITE, GENDER   NOT REPORTED':'WHITE GENDER NOT REPORTED','BLACK MALE':'BLACK MALES', 'BLACK FEMALE':'BLACK FEMALES', 'BLACK, GENDER NOT REPORTED':'BLACK GENDER NOT REPORTED','HISPANIC MALE':'HISPANIC MALES', 'HISPANIC FEMALE':'HISPANIC FEMALES', 'HISPANIC, GENDER NOT REPORTED':'HISPANIC GENDER NOT REPORTED', 'TOTAL STAFF':'TOTAL NUMBER OF TEACHERS'}
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
    
teacher_dataset = teacher_dataset.reset_index(0)
teacher_dataset = teacher_dataset.rename(columns={'level_0':'Year'})
teacher_keep_cols = ['Year','SCHOOL YEAR','DISTRICT ID','SCHOOL DISTRICT/ CAREER CENTER','WHITE MALES','WHITE FEMALES','WHITE GENDER NOT REPORTED','BLACK MALES', 'BLACK FEMALES', 'BLACK GENDER NOT REPORTED','HISPANIC MALES', 'HISPANIC FEMALES', 'HISPANIC GENDER NOT REPORTED', 'TOTAL NUMBER OF TEACHERS']
teacher_dataset = teacher_dataset[teacher_keep_cols]
teacher_dataset['WHITE TEACHERS'] = teacher_dataset['WHITE MALES'] + teacher_dataset["WHITE FEMALES"] + teacher_dataset["WHITE GENDER NOT REPORTED"]
teacher_dataset['BLACK TEACHERS'] = teacher_dataset['BLACK MALES'] + teacher_dataset["BLACK FEMALES"] + teacher_dataset["BLACK GENDER NOT REPORTED"]
teacher_dataset['HISPANIC TEACHERS'] = teacher_dataset['HISPANIC MALES'] + teacher_dataset["HISPANIC FEMALES"] + teacher_dataset["HISPANIC GENDER NOT REPORTED"]
teacher_drop_cols = ['WHITE MALES','WHITE FEMALES','WHITE GENDER NOT REPORTED','BLACK MALES', 'BLACK FEMALES', 'BLACK GENDER NOT REPORTED','HISPANIC MALES', 'HISPANIC FEMALES', 'HISPANIC GENDER NOT REPORTED',]
teacher_dataset.drop(columns = teacher_drop_cols, inplace=True)

# Dropping rows with special school districts and dropping rows that contained notes while in Excel format
teacher_drop_schools = ['ANDERSON ALTERNATIVE', 'SC PUBLIC CHARTER SCHOOL DISTRICT', 'CHARTER INSTITUTE AT ERSKINE',
                        'LIMESTONE CHARTER ASSOCIATION', 'JOHN DE LA HOWE L12', 'DEAF & BLIND SCHOOL', 'JUVENILE JUSTICE', 
                        'ANDERSON ALTERNATIVE SCHOOL', 'ANDERSON 1 & 2 CAREER', 'BARNWELL CO AVC', 'BEAUFORT-JASPER CAREER', 
                        'F E DUBOSE AVC', 'DILLON COUNTY TECHNOLOGY','DORCHESTER CAREER SCHOOL', 'GREENWOOD CO AVC', 'COPE AVC', 
                        'DANIEL MORGAN VOC', 'R D ANDERSON TECH', 'H B SWOFFORD', 'Charter Institute at Erskine', 'SCH FOR DEAF & BLIND', 
                        '3410', 'STATE CHARTER','PALMETTO UNIFIED', 'SPARTANBURG 80', 'SPARTANBURG 81','SPARTANBURG 82',
                        'SC PUBLIC CHARTER DISTRICT','STATE TOTAL', 'SOUTH CAROLINA', 'ANDERSON 80','ANDERSON 81', 'BEAUFORT 80', 'BARNWELL 80',
                        'CLARENDON 80', 'DILLON 80', 'DORCHESTER 80', 'GREENWOOD 80', 'ORANGEBURG 80', 'ORANGEBURG 81']
teacher_bad = teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'].isin(teacher_drop_schools)
teacher_dataset = teacher_dataset[teacher_bad == False]
teacher_bad = teacher_dataset[['WHITE TEACHERS', 'BLACK TEACHERS']].isna().all(axis = 'columns')
teacher_dataset = teacher_dataset[teacher_bad == False]
teacher_drop_cols = ['SCHOOL YEAR', 'DISTRICT ID']
teacher_dataset = teacher_dataset.drop(columns = teacher_drop_cols)
