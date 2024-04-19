# Importing
import pandas as pd
import requests


    
    
    
    # Cleaning code
    graddf = pd.read_excel(excel_file)
    graddf['BEDSCODE'] = pd.to_datetime(graddf['BEDSCODE'])
    graddf['YEAR'] = graddf['BEDSCODE'].dt.year
    graddf.rename(columns={'BEDSCODE':'YEAR'}, inplace=True)
    keep_cols = ['DISTRICT', 'SCHOOL', 'GNUMERATOR_RACE_W', 'GDENOM_RACE_W', 'GNUMERATOR_RACE_B', 'GDENOM_RACE_B', 'GNUMERATOR_RACE_H', 'GDENOM_RACE_H']
    graddf = graddf[keep_cols]
    graddf.fillna('N/A')
    graddf.replace('-1', 'N/A')
    graddf.replace('-1.00', 'N/A')
  else:
    print(f"Failed to fetch and clean file: {response.status_code} - {response.reason}")
    return None



  




