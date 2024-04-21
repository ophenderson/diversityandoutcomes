
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

# These replace functions aren't working
graddf.replace('-1', '0')
graddf.replace('-1.0', '0')











# Importing
import pandas as pd
import requests

def get(owner, repo, folder_path, file_name):
    # Construct the URL to list the contents of the folder
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{folder_path}"
    
    # Send a GET request to the GitHub API
    response = requests.get(url)
    
    if response.status_code == 200:
        contents = response.json()  # Parse the JSON response
        for item in contents:
            if item['name'] == file_name:
                # If the file is found, construct the raw URL to download it
                download_url = item['download_url']
                file_content = requests.get(download_url).text
                return file_content
        print(f"File '{file_name}' not found in folder '{folder_path}'")
        return None
    else:
        print(f"Failed to fetch contents of folder '{folder_path}'")
        return None

# Example usage
owner = 'ophenderson'
repo = 'diversityandoutcomes'
folder_path = 'raw/'
file_name = ['OVERALL_GRADRATE1718.xlsx', 'OVERALL_GRADRATE1819.xlsx', 'OVERALL_GRADRATE1920.xlsx', 'OVERALL_GRADRATE2021.xlsx', 'OVERALL_GRADRATE2022.xlsx', 'OVERALL_GRADRATE2023.xlsx']

file_content = get(owner, repo, folder_path, file_name)

if file_content:
    # Now you have the content of the file, you can further process it as needed
    pd.read_excel(file_name)

    
    
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



  




