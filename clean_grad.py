# Importing
import pandas as pd
import requests
from io import BytesIO


# Defining a function that fetches and cleans graduation rate files
def fetch_file(repo_owner, repo_name, folder_path, file_name, branch = 'main')
  url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{folder_path}/{file_name}"
  response = requests.get('url')
  if response.status_code == 200
    excel_bytes = response.content
    excel_file = BytesIO(excel_bytes)
    graddf = pd.read_excel(excel_file)
    keep_cols = ['DISTRICT', 'SCHOOL', 'GNUMERATOR_RACE_W', 'GDENOM_RACE_W', 'GNUMERATOR_RACE_B', 'GDENOM_RACE_B', 'GNUMERATOR_RACE_H', 'GDENOM_RACE_H')


  
    return response.text
  else:
    print(f"Failed to fetch file: {response.status_code} - {response.reason}")
    return None

# Cleaning the file
pd.read


  




