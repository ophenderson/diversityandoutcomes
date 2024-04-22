# Importing
import pandas as pd
import glob

# Creating a list of all student files
# I changed the name of the 2017-2018 student district data to make this easier!!
student_files = glob.glob('raw/*District Headcount by Gender, Ethnicity and Pupils in Poverty*')

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



