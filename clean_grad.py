# Importing
import pandas as pd
import requests
from io import BytesIO


# Defining a function that fetches and cleans graduation rate files
def fetch_and_clean(repo_owner, repo_name, folder_path, file_name, branch = 'main')
  url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{folder_path}/{file_name}"
  response = requests.get('url')
  if response.status_code == 200
    excel_bytes = response.content
    excel_file = BytesIO(excel_bytes)
    graddf = pd.read_excel(excel_file)
    graddf['BEDSCODE'] = Year # the idea for this was that I would replace the BEDSCODE column with the school year that the data is from, not sure how to do this?
    graddf.rename(columns={'BEDSCODE':'YEAR'}, inplace=True)
    keep_cols = ['DISTRICT', 'SCHOOL', 'GNUMERATOR_RACE_W', 'GDENOM_RACE_W', 'GNUMERATOR_RACE_B', 'GDENOM_RACE_B', 'GNUMERATOR_RACE_H', 'GDENOM_RACE_H')
    graddf = graddf[keep_cols]
    graddf.fillna('N/A')
    graddf.replace('-1', 'N/A')
    graddf.replace('-1.00', 'N/A')
  else:
    print(f"Failed to fetch and clean file: {response.status_code} - {response.reason}")
    return None

# Trying to do this with API

api = 




  




