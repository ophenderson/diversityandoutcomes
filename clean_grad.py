# Importing
import pandas as pd
import requests

# 
def fetch(repo_owner, repo_name, path_to_file):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{path_to_file}"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.json()['content']
        file_content = base64.b64decode(content).decode('utf-8')
        return file_content
    else: 
        return None
    
repo_owner = 'ophenderson'
repo_name = 'diversityandoutcomes'
path_to_file = raw/OVERALL_GRADRATE1718.xlsx
file_content = fetch(repo_owner, repo_name, path_to_file)
if file_content:
    print(file_content)
#%%

    
    
    
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



  




