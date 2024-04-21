# Importing 
import pandas as pd
import requests

# Reading in a file
graddf = pd.read_excel('raw/OVERALL_GRADRATE1718.xlsx')

# Performing cleaning functions
year = '2017-2018'
graddf['Year'] = year
keep_cols = ['DISTRICT', 'SCHOOL', 'GNUMERATOR_RACE_W', 'GDENOM_RACE_W', 'GNUMERATOR_RACE_B', 'GDENOM_RACE_B', 'GNUMERATOR_RACE_H', 'GDENOM_RACE_H']
graddf = graddf[keep_cols]
graddf.fillna('N/A')
graddf.replace('-1', '0')
graddf.replace('-1.0', '0')