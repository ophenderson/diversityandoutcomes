# Importing
import pandas as pd
import glob
import os

# Creating a list of all student files
# I changed the name of the 2017-2018 student district data to make this easier!!
student_files = glob.glob('raw/*District Headcount by Gender, Ethnicity and Pupils in Poverty*')

# Function 
def read_student_file(fname):
    # Reading the excel file
    skips = [0,1,2,3,4,5]
    if '2017_18' in fname:
        skips = [0]
    raw = pd.read_excel(fname,skiprows = skips)
    # Information about the file
    info = len(raw)
    print('Number of entries:' ,fname, info)
    return raw
# Empty dictionary that will contain each of the years that are in the dataframe
student_data_list = {}

# For loop
for fname in student_files:
    # grabbing the file
    student = read_student_file(fname)
    # getting the school year off the end of the file and creating a column of school years
    (basename, ext) = os.path.splitext(fname)
    tail = basename[-2:]
    student_data_list[tail]=student
    # concatenating all 6 files into 1 dataframe
    student_dataset = pd.concat(student_data_list)
# Ending the for loop, resetting the index
student_dataset = student_dataset.reset_index(0)
# Renaming columns - I had to do this because in one of the excel files the names didn't match the others. This line of code aligns that file back with the consistent names. 
student_dataset = student_dataset.rename(columns={'level_0':'Year', 'Unnamed: 0':'District ID','Unnamed: 1':'District',
                                                  'Unnamed: 2':'Total Number of Students','Yes':'Pupils in Poverty'})
# Dropping unneeded columns
student_keep_cols = ['Year', 'District ID', 'District', 'Total Number of Students','Black or African-American',
                     'Hispanic or Latino', 'White']
student_dataset = student_dataset[student_keep_cols]


# Dropping rows with special school districts
student_drop_schools = ['4701','4801','5205','5207','5208','5209','5364','5395','4901','Statewide Totals', 
                        'Statewide Total', 'Statewide Percentage', 'Statewide Percentages']
student_bad = student_dataset['District ID'].isin(student_drop_schools)
student_dataset = student_dataset[student_bad == False]
student_bad = student_dataset[['District', 'Total Number of Students']].isna().all(axis = 'columns')
student_dataset = student_dataset[student_bad == False]

# Combining districts that were consolidated prior to 2023 (this will be in all my scripts)
# Bamberg 1 and 2 became Bamberg 3 in 2022
student_dataset['District'] = student_dataset['District'].replace({'Bamberg 01' :'Bamberg 03', 'Bamberg 02':'Bamberg 03'})
# Barnwell 19 and 29 became Barnwell 48 in 2022
student_dataset['District'] = student_dataset['District'].replace({'Barnwell 19':'Barnwell 48', 'Barnwell 29':'Barnwell 48'})
# Orangeburg 3, 4, 5 became Orangeburg in 2019
student_dataset['District'] = student_dataset['District'].replace({'Orangeburg 03': 'Orangeburg', 'Orangeburg 04': 'Orangeburg', 'Orangeburg 05':'Orangeburg'})
# Hampton 1 and 2 became Hampton 3 in 2022
student_dataset['District'] = student_dataset['District'].replace({'Hampton 01':'Hampton 3', 'Hampton 02':'Hampton 3'})
# Summing up the combined rows
student_dataset = student_dataset.groupby(['Year', 'District']).sum()
# Resetting index and dropping District ID column
student_dataset.reset_index(inplace=True)
student_dataset.drop(columns = ['District ID'], inplace=True)

# District column consistency
student_dataset['District'] = student_dataset['District'].str.upper()
student_dataset['District'] = student_dataset['District'].str.replace(r' 0',' ')
student_dataset['District'] = student_dataset['District'].replace({'ABBEVILLE 60':'ABBEVILLE', 'AIKEN 1':'AIKEN', 
                                                                   'ALLENDALE 1':'ALLENDALE', 'BEAUFORT 1': 'BEAUFORT', 
                                                                   'BERKELEY 1':'BERKELEY', 'CALHOUN 1':'CALHOUN', 
                                                                   'CHARLESTON 1':'CHARLESTON', 'CHEROKEE 1':'CHEROKEE', 
                                                                   'CHESTER 1':'CHESTER', 'CHESTERFIELD 1':'CHESTERFIELD', 
                                                                   'COLLETON 1':'COLLETON', 'DARLINGTON 1':'DARLINGTON',
                                                                   'EDGEFIELD 1':'EDGEFIELD', 'FAIRFIELD 1':'FAIRFIELD', 
                                                                   'GEORGETOWN 1':'GEORGETOWN', 'GREENVILLE 1':'GREENVILLE', 
                                                                   'HORRY 1':'HORRY', 'JASPER 1':'JASPER','KERSHAW 1':'KERSHAW', 
                                                                   'LANCASTER 1':'LANCASTER', 'LEE 1':'LEE', 'MARLBORO 1':'MARLBORO', 
                                                                   'MCCORMICK 1':'MCCORMICK', 'NEWBERRY 1':'NEWBERRY', 
                                                                   'OCONEE 1':'OCONEE', 'PICKENS 1':'PICKENS', 'SALUDA 1':'SALUDA', 
                                                                   'SUMTER 1':'SUMTER', 'UNION 1':'UNION', 
                                                                   'WILLIAMSBURG 1':'WILLIAMSBURG','HAMPTON':'HAMPTON 3'})




# student_dataset['District'] = student_dataset['District'].str.replace(r' 1$','')

# Saving as pickle file
student_dataset.to_pickle('student.pkl')



