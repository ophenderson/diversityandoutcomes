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
# Empty dictionary that will contain each of the years that are in the dataframe
teacher_data_list = {}
# For loop
for fname in teacher_files:
    # grabbing the file
    teacher = read_teacher_file(fname)
    # getting the school year off the end of the file and creating a column of school years
    (basename, ext) = os.path.splitext(fname) 
    tail = basename[-2:]
    teacher_data_list[tail]=teacher
    # concatenating all 6 files into 1 dataframe
    teacher_dataset = pd.concat(teacher_data_list)
# Ending the for loop, resetting the index
teacher_dataset = teacher_dataset.reset_index(0)
# Renaming the year column
teacher_dataset = teacher_dataset.rename(columns={'level_0':'Year'})
# Dropping unneeded columns
teacher_keep_cols = ['Year','SCHOOL YEAR','DISTRICT ID','SCHOOL DISTRICT/ CAREER CENTER','WHITE MALES','WHITE FEMALES',
                     'WHITE GENDER NOT REPORTED','BLACK MALES', 'BLACK FEMALES', 'BLACK GENDER NOT REPORTED','HISPANIC MALES',
                     'HISPANIC FEMALES', 'HISPANIC GENDER NOT REPORTED', 'TOTAL NUMBER OF TEACHERS']
teacher_dataset = teacher_dataset[teacher_keep_cols]
# Combining the columns that are separated by gender into 1 column
teacher_dataset['WHITE TEACHERS'] = teacher_dataset['WHITE MALES'] + teacher_dataset["WHITE FEMALES"] + teacher_dataset["WHITE GENDER NOT REPORTED"]
teacher_dataset['BLACK TEACHERS'] = teacher_dataset['BLACK MALES'] + teacher_dataset["BLACK FEMALES"] + teacher_dataset["BLACK GENDER NOT REPORTED"]
teacher_dataset['HISPANIC TEACHERS'] = teacher_dataset['HISPANIC MALES'] + teacher_dataset["HISPANIC FEMALES"] + teacher_dataset["HISPANIC GENDER NOT REPORTED"]
# Dropping the columns now that they're combined
teacher_drop_cols = ['WHITE MALES','WHITE FEMALES','WHITE GENDER NOT REPORTED','BLACK MALES', 'BLACK FEMALES', 
                     'BLACK GENDER NOT REPORTED','HISPANIC MALES', 'HISPANIC FEMALES', 'HISPANIC GENDER NOT REPORTED',]
teacher_dataset.drop(columns = teacher_drop_cols, inplace=True)

# Dropping rows with special school districts and dropping rows that contained notes while in Excel format
teacher_drop_schools = ['ANDERSON ALTERNATIVE', 'SC PUBLIC CHARTER SCHOOL DISTRICT', 'CHARTER INSTITUTE AT ERSKINE',
                        'LIMESTONE CHARTER ASSOCIATION', 'JOHN DE LA HOWE L12', 'DEAF & BLIND SCHOOL', 'JUVENILE JUSTICE', 
                        'ANDERSON ALTERNATIVE SCHOOL', 'ANDERSON 1 & 2 CAREER', 'BARNWELL CO AVC', 'BEAUFORT-JASPER CAREER', 
                        'F E DUBOSE AVC', 'DILLON COUNTY TECHNOLOGY','DORCHESTER CAREER SCHOOL', 'GREENWOOD CO AVC', 'COPE AVC', 
                        'DANIEL MORGAN VOC', 'R D ANDERSON TECH', 'H B SWOFFORD', 'Charter Institute at Erskine', 'SCH FOR DEAF & BLIND', 
                        'STATE CHARTER','PALMETTO UNIFIED', 'SPARTANBURG 80', 'SPARTANBURG 81','SPARTANBURG 82',
                        'SC PUBLIC CHARTER DISTRICT','STATE TOTAL', 'SOUTH CAROLINA', 'ANDERSON 80','ANDERSON 81', 'BEAUFORT 80', 'BARNWELL 80',
                        'CLARENDON 80', 'DILLON 80', 'DORCHESTER 80', 'GREENWOOD 80', 'ORANGEBURG 80', 'ORANGEBURG 81']
teacher_bad = teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'].isin(teacher_drop_schools)
teacher_dataset = teacher_dataset[teacher_bad == False]
# Excel files contained notes at the bottom and since the script
# was concatenated they are throughout the dataframe
# this code goes through the dataframe and drops all the rows that contain "nan" 
# as a result of having notes in the index columns
teacher_bad = teacher_dataset[['WHITE TEACHERS', 'BLACK TEACHERS']].isna().all(axis = 'columns')
teacher_dataset = teacher_dataset[teacher_bad == False]
# Dropping school year and district ID columns
teacher_drop_cols = ['SCHOOL YEAR', 'DISTRICT ID']
teacher_dataset = teacher_dataset.drop(columns = teacher_drop_cols)

# Combining districts that were consolidated prior to 2023 (this will be in all my scripts)
# Bamberg 1 and 2 became Bamberg 3 in 2022
teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'] = teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'].replace({'BAMBERG 1':'BAMBERG 3', 'BAMBERG 2':'BAMBERG 3', 'BAMBERG 01':'BAMBERG 3', 'BAMBERG 02':'BAMBERG 3'})
# Barnwell 19 and 29 became Barnwell 48 in 2022
teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'] = teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'].replace({'BARNWELL 19':'BARNWELL 48', 'BARNWELL 29':'BARNWELL 48'})
# Orangeburg 3, 4, 5 became Orangeburg in 2019
teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'] = teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'].replace({'ORANGEBURG 3': 'ORANGEBURG', 'ORANGEBURG 4': 'ORANGEBURG', 'ORANGEBURG 5':'ORANGEBURG'})
# Adding back Marion 10
teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'] = teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'].replace({'3410': 'MARION 10'})
# Hampton 1 and 2 became Hampton 3 in 2022
teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'] = teacher_dataset['SCHOOL DISTRICT/ CAREER CENTER'].replace({'HAMPTON 1':'HAMPTON 3', 'HAMPTON 2':'HAMPTON 3', 'HAMPTON 01':'HAMPTON 3', 'HAMPTON 02':'HAMPTON 3'})

# Summing up the combined rows
teacher_dataset = teacher_dataset.groupby(['Year', 'SCHOOL DISTRICT/ CAREER CENTER']).sum()
# Restting index
teacher_dataset.reset_index(inplace=True)

# District column consistency
teacher_dataset.rename(columns = {'SCHOOL DISTRICT/ CAREER CENTER':'District'}, inplace=True)
teacher_dataset['District'] = teacher_dataset['District'].str.replace(r' 0',' ')
teacher_dataset['District'] = teacher_dataset['District'].replace({'ABBEVILLE 60':'ABBEVILLE', 'AIKEN 1':'AIKEN', 
                                                                   'ALLENDALE 1':'ALLENDALE', 'BEAUFORT 1': 'BEAUFORT', 
                                                                   'BERKELEY 1':'BERKELEY', 'CALHOUN 1':'CALHOUN', 
                                                                   'CHARLESTON 1':'CHARLESTON', 'CHEROKEE 1':'CHEROKEE', 
                                                                   'CHESTER 1':'CHESTER', 'CHESTERFIELD 1':'CHESTERFIELD', 
                                                                   'COLLETON 1':'COLLETON', 'DARLINGTON 1':'DARLINGTON',
                                                                   'EDGEFIELD 1':'EDGEFIELD', 'FAIRFIELD 1':'FAIRFIELD', 
                                                                   'GEORGETOWN 1':'GEORGETOWN', 'GREENVILLE 1':'GREENVILLE', 
                                                                   'HORRY 1':'HORRY', 'JASPER 1':'JASPER','KERSHAW 1':'KERSHAW', 
                                                                   'LANCASTER 1':'LANCASTER', 'LEE 1':'LEE', 
                                                                   'LEXINGTON/  RICHLAND  5':'LEXINGTON 5', 'MARLBORO 1':'MARLBORO', 
                                                                   'MCCORMICK 1':'MCCORMICK', 'NEWBERRY 1':'NEWBERRY', 
                                                                   'OCONEE 1':'OCONEE', 'PICKENS 1':'PICKENS', 'SALUDA 1':'SALUDA', 
                                                                   'SUMTER 1':'SUMTER', 'UNION 1':'UNION', 
                                                                   'WILLIAMSBURG 1':'WILLIAMSBURG', 'YORK 1 (YORK)':'YORK 1', 
                                                                   'YORK 2 (CLOVER)':'YORK 2', 'YORK 3 (ROCK HILL)':'YORK 3', 
                                                                   'YORK 4 (FORT MILL)':'YORK 4', 'SUMTER COUNTY':'SUMTER', 
                                                                   'HAMPTON':'HAMPTON 3'}) 

# Saving as pickle file
teacher_dataset.to_pickle('teacher.pkl')


