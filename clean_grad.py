# Couldn't figure out how to make this flexible for all my grad files so just decided to clean one and make sure it all works and then I can apply to rest of my files later

# Importing 
import pandas as pd
import requests

# Reading in a file
graddf1718 = pd.read_excel('raw/OVERALL_GRADRATE1718.xlsx')

# Performing cleaning functions
 # Adding year column, won't add year column
year = '2017-2018'
graddf1718['Year'] = year

# Keeping only the columns I need
keep_cols = ['DISTRICT', 'SCHOOL', 'GNUMERATOR_RACE_W', 'GDENOM_RACE_W', 'GNUMERATOR_RACE_B', 'GDENOM_RACE_B', 'GNUMERATOR_RACE_H', 'GDENOM_RACE_H']
graddf1718 = graddf1718[keep_cols]

# Filling in missing values and replacing negatives with 0
graddf1718.fillna('NaN')
graddf1718 = graddf1718.replace(-1, 0)

# Creating a columns that calculates the graduation rate for each race
graddf1718['Graduation Rate - W'] = graddf1718['GNUMERATOR_RACE_W']/graddf1718['GDENOM_RACE_W']
graddf1718['Graduation Rate - B'] = graddf1718['GNUMERATOR_RACE_B']/graddf1718['GDENOM_RACE_B']
graddf1718['Graduation Rate - H'] = graddf1718['GNUMERATOR_RACE_H']/graddf1718['GDENOM_RACE_H']



  




