# Couldn't figure out how to make this flexible for all my grad files so just decided to clean one and make sure it all works and then I can apply to rest of my files later

# Importing 
import pandas as pd
import requests

# Reading in a file
graddf = pd.read_excel('raw/OVERALL_GRADRATE1718.xlsx')

# Performing cleaning functions
 # Adding year column, won't add year column
year = '2017-2018'
graddf['Year'] = year

# Keeping only the columns I need
keep_cols = ['DISTRICT', 'SCHOOL', 'GNUMERATOR_RACE_W', 'GDENOM_RACE_W', 'GNUMERATOR_RACE_B', 'GDENOM_RACE_B', 'GNUMERATOR_RACE_H', 'GDENOM_RACE_H']
graddf = graddf[keep_cols]

# Filling in missing values
graddf.fillna('N/A')

# These replace functions aren't working, trying to replace -1 and -1.0 with 0
graddf = graddf.replace(-1, 0)




  




