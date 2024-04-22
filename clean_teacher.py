# Importing
import pandas as pd

# Reading in a file
teacherdf = pd.read_excel('raw/SOUTH CAROLINA TEACHERS BY RACE AND GENDER FOR THE 2017-18 SCHOOL YEAR (HEADCOUNT BY SCHOOL DISTRICT), MARCH 29, 2019.xlsx')

# Performing cleaning functions
teacherdf['YEAR'] = '2017-2018' # once again, not sure how to make sure this is done differently for each file and also j
keep_cols = ['DISTRICT ID', 'SCHOOL DISTRICT/ CAREER CENTER', 'WHITE MALES', 'WHITE FEMALES', 'WHITE GENDER NOT REPORTED', 'BLACK MALES', 'BLACK FEMALES', 'BLACK GENDER NOT REPORTED','HISPANIC MALES', 'HISPANIC FEMALES', 'HISPANIC GENDER NOT REPORTED', 'TOTAL NUMBER OF TEACHERS']
teacherdf = teacherdf[keep_cols]
teacherdf['totalw'] = teacherdf['WHITE MALES'] + teacherdf["WHITE FEMALES"] + teacherdf["WHITE GENDER NOT REPORTED"]
teacherdf['totalb'] = teacherdf['BLACK MALES'] + teacherdf["BLACK FEMALES"] + teacherdf["BLACK GENDER NOT REPORTED"]
teacherdf ['totalh'] = teacherdf['HISPANIC MALES'] + teacherdf["HISPANIC FEMALES"] + teacherdf["HISPANIC GENDER NOT REPORTED"]
teacherdf = teacherdf.drop(columns =['WHITE MALES', 'WHITE FEMALES', 'WHITE GENDER NOT REPORTED', 'BLACK MALES', 'BLACK FEMALES', 'BLACK GENDER NOT REPORTED','HISPANIC MALES', 'HISPANIC FEMALES', 'HISPANIC GENDER NOT REPORTED'])
teacherdf.fillna('N/A')

